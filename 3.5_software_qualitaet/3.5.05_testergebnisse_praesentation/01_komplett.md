# Ueberblick und Grundlagen: 3.5.05 – Testdaten erstellen

## Einordnung

- **Pruefungsteil:** 3.5 – Sicherstellen der Qualitaet von Softwareanwendungen
- **Thema-ID:** 3.5.05
- **Thema:** Testdaten generieren und sinnvolle Testdatenstrategien anwenden koennen

## Themenkreise

### 1. Testdaten generieren

**Definition:** Testdaten sind Eingabewerte und Datensaetze, die gezielt fuer das Testen von Software erstellt werden. Sie simulieren reale Nutzungsbedingungen und decken sowohl Normal- als auch Fehlerfaelle ab.

**Kernaussagen:**
- Testdaten sind die Grundlage jedes Tests – ohne passende Daten sind Tests wertlos
- Testdaten muessen systematisch erstellt werden (nicht zufaellig)
- Sie muessen gueltige und ungueltige Eingaben abdecken
- Grenzwerte und Sonderfaelle muessen enthalten sein
- Testdaten duerfen keine echten personenbezogenen Daten enthalten (DSGVO)

---

## Strategien zur Testdatenerstellung

| Strategie | Beschreibung | Beispiel |
|---|---|---|
| **Aequivalenzklassen** | Eingabewerte in Klassen mit gleichem Verhalten einteilen, pro Klasse einen Repraesentanten waehlen | Alter: <18 (ungueltig), 18–65 (gueltig), >65 (ungueltig) |
| **Grenzwerte** | Werte an den Grenzen der Aequivalenzklassen testen | Alter: 17, 18, 65, 66 |
| **Sonderfaelle / Edge Cases** | Ungewoehnliche oder extreme Eingaben testen | Leere Eingabe, null, Sonderzeichen, maximale Laenge |
| **Positivdaten** | Gueltige Eingaben, die das System akzeptieren muss | E-Mail: "max@firma.de" |
| **Negativdaten** | Ungueltige Eingaben, die das System abweisen muss | E-Mail: "max@", "max firma.de", "" |
| **Zufallsdaten** | Automatisch generierte Daten fuer Massen- oder Lasttests | 10.000 zufaellige Kundendatensaetze |

**Erklaerung:** Die Strategien Aequivalenzklassen und Grenzwerte sind direkt mit den Testverfahren aus 3.5.01 verknuepft. In der Pruefung wird haeufig verlangt, zu einem gegebenen Szenario passende Testdaten abzuleiten.

---

## Techniken und Werkzeuge

### Fixtures

**Definition:** Fixtures sind vorgefertigte, wiederverwendbare Testdaten-Sets, die vor jedem Test geladen werden und einen definierten Ausgangszustand herstellen.

**Kernaussagen:**
- Stellen sicher, dass Tests unter identischen Bedingungen laufen
- Werden vor dem Test aufgebaut (Setup) und danach abgebaut (Teardown)
- Typisch fuer Datenbank-Tests: Tabellen mit bekannten Datensaetzen befuellen
- Frameworks: pytest Fixtures, JUnit @Before/@After, TestNG

**Beispiel (Pseudocode):**
```
FIXTURE kundenFixture:
    SETUP:
        Datenbank.einfuegen(Kunde(id=1, name="Max Muster", alter=30))
        Datenbank.einfuegen(Kunde(id=2, name="Erika Test", alter=17))
    TEARDOWN:
        Datenbank.loeschen(alle_Testdaten)
```

### Factories

**Definition:** Factories sind Hilfsfunktionen oder -klassen, die Testdaten dynamisch erzeugen. Im Gegensatz zu Fixtures werden die Daten im Test flexibel zusammengestellt.

**Kernaussagen:**
- Flexibler als Fixtures – nur die relevanten Felder werden ueberschrieben
- Standardwerte fuer nicht relevante Felder
- Beliebt in agilen Projekten mit haeufig wechselnden Datenmodellen
- Frameworks: Factory Bot (Ruby), Faker (Python/JS), Model Bakery (Django)

**Beispiel (Pseudocode):**
```
FACTORY erstelleKunde(ueberschreibungen):
    STANDARD:
        name = "Max Muster"
        email = "max@test.de"
        alter = 30
        status = "aktiv"
    UEBERNEHME ueberschreibungen
    RUECKGABE neuer Kunde mit Werten

// Verwendung:
testKunde1 = erstelleKunde()                           // Standardkunde
testKunde2 = erstelleKunde({alter: 17, status: "neu"}) // Minderjaehriger Neukunde
```

### Mock-Daten und Stubs

**Definition:** Mock-Daten simulieren externe Abhaengigkeiten (z.B. APIs, Datenbanken), damit Tests isoliert und unabhaengig laufen koennen.

| Konzept | Beschreibung | Einsatz |
|---|---|---|
| **Mock** | Simuliertes Objekt, das Aufrufe aufzeichnet und vordefinierte Antworten liefert | API-Aufrufe simulieren |
| **Stub** | Vereinfachte Implementierung, die feste Werte zurueckgibt | Datenbankabfrage simulieren |
| **Fake** | Funktionierende, aber vereinfachte Implementierung | In-Memory-Datenbank statt echte DB |

**Beispiel:**
```
// Stub fuer einen Waehrungskurs-Service
STUB WaehrungsService.getKurs("EUR", "USD"):
    RUECKGABE 1.08

// Test kann jetzt unabhaengig vom echten Waehrungsservice laufen
```

---

## Aequivalenzklassen fuer Testdaten – Systematische Ableitung

**Vorgehensweise:**

1. Eingabefelder identifizieren
2. Fuer jedes Feld: gueltige und ungueltige Wertebereiche bestimmen
3. Pro Aequivalenzklasse mindestens einen Repraesentanten waehlen
4. Grenzwerte ergaenzen
5. Sonderfaelle ergaenzen (null, leer, Sonderzeichen)

**Beispiel: Registrierungsformular**

| Feld | Gueltige Klasse | Ungueltige Klasse(n) | Grenzwerte | Sonderfaelle |
|---|---|---|---|---|
| Benutzername | 3–20 Zeichen, alphanumerisch | <3 Zeichen, >20 Zeichen, Sonderzeichen | 2, 3, 20, 21 Zeichen | Leer, nur Leerzeichen |
| Passwort | 8–64 Zeichen, mind. 1 Grossbuchstabe, 1 Zahl | <8 Zeichen, ohne Grossbuchstabe, ohne Zahl | 7, 8, 64, 65 Zeichen | Leer, nur Zahlen |
| E-Mail | Gueltiges Format (name@domain.tld) | Ohne @, ohne Domain, ohne TLD | – | "a@b.c", sehr lange Adressen |
| Alter | 18–120 (Ganzzahl) | <18, >120, Dezimalzahl, Buchstaben | 17, 18, 120, 121 | 0, negativ, leer |

---

## DSGVO und Testdaten

**Definition:** Die Datenschutz-Grundverordnung (DSGVO) regelt den Umgang mit personenbezogenen Daten in der EU. Sie hat direkte Auswirkungen auf die Erstellung und Nutzung von Testdaten.

**Kernaussagen:**

| Aspekt | Anforderung |
|---|---|
| Keine echten Daten | Produktivdaten duerfen nicht ohne Weiteres fuer Tests verwendet werden |
| Anonymisierung | Wenn Produktivdaten noetig: Personenbezogene Daten muessen anonymisiert werden |
| Pseudonymisierung | Personenbezogene Merkmale werden durch Pseudonyme ersetzt (Rueckschluss theoretisch moeglich) |
| Synthetische Daten | Kuenstlich erzeugte Daten, die keine realen Personen betreffen → bevorzugt |
| Datensparsamkeit | Nur die fuer den Test notwendigen Daten verwenden |
| Dokumentation | Es muss dokumentiert werden, welche Daten fuer Tests verwendet werden und warum |

**Wichtige Begriffe:**
- **Personenbezogene Daten** – Alle Informationen, die sich auf eine identifizierbare Person beziehen (Name, E-Mail, IP-Adresse etc.)
- **Anonymisierung** – Personenbezug wird unwiderruflich entfernt (keine DSGVO mehr anwendbar)
- **Pseudonymisierung** – Personenbezug wird verschleiert, ist aber theoretisch wiederherstellbar (DSGVO weiter anwendbar)
- **Synthetische Testdaten** – Kuenstlich generierte Daten ohne Bezug zu realen Personen

---

## Typische Pruefungsaspekte

- Testdaten zu einem gegebenen Szenario ableiten (Aequivalenzklassen, Grenzwerte)
- Unterschied Fixture vs. Factory erklaeren
- Mock/Stub/Fake unterscheiden und Einsatzzweck benennen
- DSGVO-konforme Testdatenerstellung beschreiben
- Positive und negative Testdaten fuer ein Eingabefeld definieren

## Haeufige Fehler

| Fehler | Richtigstellung |
|---|---|
| Produktivdaten einfach fuer Tests kopieren | Datenschutzverstoss – Anonymisierung oder synthetische Daten erforderlich |
| Nur gueltige Testdaten erstellen | Ungueltige Daten und Grenzwerte sind genauso wichtig |
| Zufallsdaten reichen fuer alle Tests | Nein – systematische Aequivalenzklassen und Grenzwerte sind notwendig |
| Mock und Stub sind dasselbe | Mock zeichnet Aufrufe auf und kann Verhalten pruefen. Stub gibt nur feste Werte zurueck |
| Testdaten muessen nur einmal erstellt werden | Testdaten muessen bei Aenderungen am Datenmodell aktualisiert werden |

---

## Beispiele

### Beispiel 1: Testdaten fuer einen Rabattrechner

**Szenario:** Ein Onlineshop gewaehrt ab einem Bestellwert von 50 EUR einen Rabatt von 10%. Ab 100 EUR betraegt der Rabatt 20%.

**Aequivalenzklassen und Testdaten:**

| Klasse | Wertebereich | Erwarteter Rabatt | Testdatum |
|---|---|---|---|
| K1 | < 50 EUR | 0% | 49,99 EUR |
| K2 | 50 – 99,99 EUR | 10% | 75,00 EUR |
| K3 | >= 100 EUR | 20% | 150,00 EUR |

**Grenzwerte:**

| Eingabe | Erwarteter Rabatt | Begruendung |
|---|---|---|
| 49,99 EUR | 0% | Knapp unter der 50-EUR-Grenze |
| 50,00 EUR | 10% | Exakt an der Grenze |
| 99,99 EUR | 10% | Knapp unter der 100-EUR-Grenze |
| 100,00 EUR | 20% | Exakt an der Grenze |

**Sonderfaelle:**

| Eingabe | Erwartetes Verhalten |
|---|---|
| 0 EUR | Fehler oder 0% Rabatt |
| Negativer Betrag (-10 EUR) | Fehlermeldung |
| Sehr grosser Betrag (999.999 EUR) | 20% Rabatt (Obergrenze) |

---

### Beispiel 2: Fixture fuer Datenbank-Tests

**Szenario:** Ein Test prueft die Suchfunktion einer Kundenverwaltung.

**Fixture-Setup:**

| ID | Vorname | Nachname | Stadt | Status |
|---|---|---|---|---|
| 1 | Max | Muster | Berlin | aktiv |
| 2 | Erika | Test | Muenchen | aktiv |
| 3 | Hans | Probe | Berlin | inaktiv |
| 4 | Anna | Demo | Hamburg | aktiv |

**Testfaelle mit diesen Fixture-Daten:**

| Testfall | Suche nach | Erwartetes Ergebnis |
|---|---|---|
| Suche nach Stadt | "Berlin" | 2 Treffer (ID 1, 3) |
| Suche nach Status "aktiv" | Status=aktiv | 3 Treffer (ID 1, 2, 4) |
| Suche mit unbekanntem Wert | "Tokio" | 0 Treffer |
| Suche nach Nachname | "Muster" | 1 Treffer (ID 1) |

**Teardown:** Alle 4 Testdatensaetze werden nach dem Test aus der Datenbank entfernt → naechster Test startet mit sauberem Zustand.

---

### Beispiel 3: DSGVO-konforme Testdaten

**Szenario:** Ein Unternehmen muss die Gehaltsabrechnung testen, benoetigt aber realistische Daten.

**Falsch (Datenschutzverstoss):**
Kopie der Produktivdatenbank mit echten Mitarbeiterdaten (Namen, Gehaelter, Steuer-IDs).

**Richtig (DSGVO-konform):**

| Feld | Produktivdaten | Anonymisierte Testdaten |
|---|---|---|
| Name | Max Mustermann | Mitarbeiter_001 |
| Geburtsdatum | 15.03.1985 | 01.01.1985 |
| Steuer-ID | 12 345 678 901 | 00 000 000 001 |
| Gehalt | 4.500 EUR | 4.500 EUR (kann beibehalten werden, wenn kein Rueckschluss moeglich) |
| IBAN | DE89 3704 0044 0532 0130 00 | DE00 0000 0000 0000 0000 00 |

**Besser:** Synthetische Testdaten mit einer Factory generieren:
```
FACTORY erstelleTestMitarbeiter(nr):
    name = "Mitarbeiter_" + nr
    geburtsdatum = zufaelligesDatum(1960, 2000)
    steuerID = "00 000 000 " + formatiere(nr, 3)
    gehalt = zufaelligerWert(2000, 8000)
    iban = "DE00 0000 0000 0000 " + formatiere(nr, 4)
    RUECKGABE neuer Mitarbeiter
```

→ Keine personenbezogenen Daten, beliebig viele Datensaetze generierbar, DSGVO-konform.

---

## Uebungen

**Aufgabe 1:** Ein Eingabefeld akzeptiert eine Postleitzahl (genau 5 Ziffern, Bereich 01000–99999). Erstelle eine Tabelle mit Aequivalenzklassen, Grenzwerten und mindestens 3 Sonderfaellen.

**Aufgabe 2:** Erklaere den Unterschied zwischen Mock, Stub und Fake. Nenne fuer jeden ein Einsatzszenario.

**Aufgabe 3:** Ein Unternehmen moechte seine Kundendatenbank fuer Tests nutzen. Die Datenbank enthaelt Namen, Adressen und Telefonnummern. Welche DSGVO-konformen Massnahmen muessen ergriffen werden? Beschreibe zwei Alternativen.

---
---

# Loesungen

## Aufgabe 1

**Aequivalenzklassen:**

| Klasse | Beschreibung | Gueltig? | Testdatum |
|---|---|---|---|
| K1 | 5 Ziffern, 01000–99999 | Gueltig | "50667" |
| K2 | Weniger als 5 Ziffern | Ungueltig | "1234" |
| K3 | Mehr als 5 Ziffern | Ungueltig | "123456" |
| K4 | Buchstaben oder Sonderzeichen | Ungueltig | "ABCDE", "123-5" |
| K5 | Unter 01000 | Ungueltig | "00999" |

**Grenzwerte:** "00999", "01000", "99999", "100000" (als String betrachtet: Laenge 5 vs. 6)

**Sonderfaelle:**
1. Leere Eingabe: "" → Fehlermeldung
2. Nur Leerzeichen: "     " → Fehlermeldung
3. Fuehrende Null: "01000" → Gueltig (niedrigste PLZ)
4. Nur Nullen: "00000" → Ungueltig (keine gueltige PLZ)
5. Dezimalzahl: "50.67" → Ungueltig (Punkt ist kein erlaubtes Zeichen)

## Aufgabe 2

| Konzept | Beschreibung | Einsatzszenario |
|---|---|---|
| **Mock** | Simuliertes Objekt, das Aufrufe aufzeichnet und vordefinierte Antworten liefert. Kann pruefen, ob bestimmte Methoden aufgerufen wurden. | Pruefen, ob die Methode `sendEmail()` genau einmal mit der richtigen Adresse aufgerufen wurde, ohne tatsaechlich eine E-Mail zu senden. |
| **Stub** | Vereinfachte Implementierung, die feste, vordefinierte Werte zurueckgibt. | Ein Stub fuer einen Wetterdienst gibt immer "22°C, sonnig" zurueck, damit der Test nicht vom echten Dienst abhaengt. |
| **Fake** | Funktionierende, aber vereinfachte Implementierung einer Abhaengigkeit. | Eine In-Memory-Datenbank (z.B. H2) anstelle der echten PostgreSQL-Datenbank fuer schnelle Unit-Tests. |

## Aufgabe 3

**Alternative 1: Anonymisierung**
- Alle personenbezogenen Daten (Namen, Adressen, Telefonnummern) werden unwiderruflich durch fiktive Werte ersetzt
- Beispiel: "Max Mustermann, Hauptstr. 1, 0171-1234567" wird zu "Kunde_001, Strasse_001, 0000-0000001"
- Vorteil: Datenstruktur und -menge bleiben realistisch
- Die anonymisierte Kopie unterliegt nicht mehr der DSGVO

**Alternative 2: Synthetische Testdaten generieren**
- Komplett kuenstliche Datensaetze mit einer Factory oder einem Tool (z.B. Faker) erzeugen
- Kein Bezug zu realen Personen
- Beispiel: Factory generiert 10.000 Kunden mit zufaelligen, aber realistisch aussehenden Namen und Adressen
- Vorteil: Beliebige Datenmenge, kein Datenschutzrisiko, DSGVO-konform von Anfang an
