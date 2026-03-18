# Ueberblick und Grundlagen: 3.5.01 – Testverfahren

## Einordnung

- **Pruefungsteil:** 3.5 – Sicherstellen der Qualitaet von Softwareanwendungen
- **Thema-ID:** 3.5.01
- **Thema:** Testverfahren kennen und anwenden koennen

## Themenkreise

### 1. Black-Box-Test

**Definition:** Ein Testverfahren, bei dem die interne Struktur (Quellcode) des Testobjekts nicht bekannt ist. Der Tester prueft ausschliesslich anhand der Spezifikation (Eingabe → erwartete Ausgabe).

**Kernaussagen:**
- Tester kennt den Quellcode nicht – nur die Anforderungen
- Tests basieren auf der Spezifikation (Lasten-/Pflichtenheft)
- Ziel: Pruefen, ob die Software die geforderten Funktionen korrekt erfuellt
- Geeignet fuer Abnahmetests, Systemtests und funktionale Tests
- Kann von Nicht-Entwicklern (z.B. Fachabteilung, Tester) durchgefuehrt werden

**Methoden des Black-Box-Tests:**

| Methode | Beschreibung | Beispiel |
|---|---|---|
| **Aequivalenzklassenbildung** | Eingabewerte werden in Klassen unterteilt, die gleichartig verarbeitet werden. Pro Klasse wird ein Repraesentant getestet. | Altersfeld akzeptiert 18–65 → Klassen: <18, 18–65, >65 |
| **Grenzwertanalyse** | Es werden die Raender der Aequivalenzklassen getestet, da dort die meisten Fehler auftreten. | Testen mit 17, 18, 65, 66 |
| **Entscheidungstabellentest** | Alle Kombinationen von Bedingungen und deren erwartete Ergebnisse werden tabellarisch erfasst. | Rabattberechnung abhaengig von Kundenstatus und Bestellwert |
| **Zustandsbasierter Test** | Testen von Zustandsuebergaengen in einem System. | Bestellstatus: Offen → Bezahlt → Versendet → Abgeschlossen |

**Wichtige Begriffe:**
- **Aequivalenzklasse** – Menge von Eingabewerten, die dasselbe Verhalten ausloesen
- **Grenzwert** – Wert an der Grenze einer Aequivalenzklasse
- **Spezifikationsbasiert** – Tests leiten sich aus den Anforderungsdokumenten ab

**Erklaerung:** In der Pruefung wird haeufig ein Szenario beschrieben, in dem du Aequivalenzklassen bilden und Grenzwerte bestimmen sollst. Typisches Beispiel: Ein Eingabefeld fuer eine Postleitzahl (5 Ziffern, 01000–99999).

---

### 2. White-Box-Test

**Definition:** Ein Testverfahren, bei dem die interne Struktur (Quellcode) des Testobjekts bekannt ist und gezielt getestet wird. Der Tester analysiert den Code, um Testfaelle abzuleiten.

**Kernaussagen:**
- Tester kennt und analysiert den Quellcode
- Tests basieren auf der Codestruktur (Kontrollfluss, Verzweigungen, Schleifen)
- Ziel: Sicherstellen, dass alle Codepfade korrekt funktionieren
- Wird typischerweise vom Entwickler selbst durchgefuehrt
- Geeignet fuer Unit-Tests und Integrationstests

**Ueberdeckungsmetriken (Coverage):**

| Metrik | Beschreibung | Abdeckung |
|---|---|---|
| **Anweisungsueberdeckung (Statement Coverage)** | Jede Anweisung im Code wird mindestens einmal ausgefuehrt. | Schwach – erkennt nicht alle Fehler |
| **Zweigueberdeckung (Branch Coverage)** | Jeder Zweig einer Verzweigung (if/else) wird mindestens einmal durchlaufen. | Mittel – Standard-Mindestanforderung |
| **Pfadueberdeckung (Path Coverage)** | Jeder moegliche Pfad durch den Code wird getestet. | Stark – in der Praxis oft nicht vollstaendig erreichbar |
| **Bedingungsueberdeckung (Condition Coverage)** | Jede Teilbedingung in einer zusammengesetzten Bedingung wird einzeln getestet. | Ergaenzend zur Zweigueberdeckung |

**Wichtige Begriffe:**
- **Kontrollflussgraph** – Grafische Darstellung aller moeglichen Programmpfade
- **Zyklomatische Komplexitaet** – Anzahl der unabhaengigen Pfade durch den Code (McCabe-Metrik)
- **Code Coverage** – Prozentualer Anteil des Codes, der durch Tests ausgefuehrt wird
- **Strukturbasiert** – Tests leiten sich aus der Codestruktur ab

**Erklaerung:** Fuer die Pruefung musst du die Ueberdeckungsmetriken kennen und einordnen koennen: Anweisungsueberdeckung ⊂ Zweigueberdeckung ⊂ Pfadueberdeckung (von schwach zu stark).

---

## Vergleich: Black-Box-Test vs. White-Box-Test

| Kriterium | Black-Box-Test | White-Box-Test |
|---|---|---|
| Codekenntnis | Nicht erforderlich | Erforderlich |
| Testbasis | Spezifikation / Anforderungen | Quellcode / Kontrollfluss |
| Durchführung durch | Tester, Fachabteilung, Kunde | Entwickler |
| Typische Teststufe | System-/Abnahmetest | Unit-/Integrationstest |
| Methoden | Aequivalenzklassen, Grenzwert | Statement/Branch/Path Coverage |
| Vorteile | Unabhaengig vom Code, nutzernah | Hohe Codeabdeckung, findet logische Fehler |
| Nachteile | Keine Aussage ueber Codequalitaet | Aufwaendig, nur durch Entwickler |
| Pruefungsrelevanz | Sehr hoch | Sehr hoch |

### Grey-Box-Test (Ergaenzung)

**Definition:** Kombination aus Black-Box- und White-Box-Test. Der Tester hat teilweise Kenntnis der internen Struktur (z.B. Datenbankschema, API-Schnittstellen), testet aber primaer auf Funktionsebene.

---

## Typische Pruefungsaspekte

- Aequivalenzklassen und Grenzwerte zu einem gegebenen Szenario bestimmen
- Unterschied Black-Box vs. White-Box erklaeren und Beispiele zuordnen
- Ueberdeckungsmetriken benennen und nach Staerke ordnen
- Geeignetes Testverfahren fuer ein Szenario empfehlen
- Code-Review als ergaenzende Qualitaetsmassnahme einordnen

## Haeufige Fehler

| Fehler | Richtigstellung |
|---|---|
| Black-Box-Test testet nur die Oberflaeche | Nein – er testet die Funktionalitaet gemaess Spezifikation, nicht nur die GUI |
| White-Box-Test und Code-Review sind dasselbe | Nein – White-Box ist dynamisches Testen (Code wird ausgefuehrt), Code-Review ist statisch |
| 100% Statement Coverage bedeutet fehlerfreien Code | Nein – Anweisungsueberdeckung ist die schwachste Metrik, Zweig-/Pfadabdeckung ist strenger |
| Grenzwertanalyse gilt nur fuer Zahlen | Nein – auch fuer Strings (Laenge), Daten (Zeitraeume) etc. |
| Black-Box braucht keine Planung | Doch – Aequivalenzklassen muessen sorgfaeltig gebildet werden |

---

## Beispiele

### Beispiel 1: Aequivalenzklassenbildung und Grenzwertanalyse

**Szenario:** Ein Onlineshop hat ein Eingabefeld fuer die Bestellmenge. Gueltige Werte: 1 bis 99.

**Aequivalenzklassen:**

| Klasse | Wertebereich | Gueltig? |
|---|---|---|
| K1 | < 1 (z.B. 0, -5) | Ungueltig |
| K2 | 1 – 99 | Gueltig |
| K3 | > 99 (z.B. 100, 999) | Ungueltig |

**Grenzwerte zum Testen:** 0, 1, 99, 100

**Erwartetes Ergebnis:**
- 0 → Fehlermeldung ("Mindestmenge ist 1")
- 1 → Bestellung wird akzeptiert
- 99 → Bestellung wird akzeptiert
- 100 → Fehlermeldung ("Maximalmenge ist 99")

---

### Beispiel 2: Anweisungs- und Zweigueberdeckung

**Szenario:** Folgende Funktion soll getestet werden:

```
FUNKTION berechneRabatt(betrag, istStammkunde):
    rabatt = 0
    WENN betrag > 100 DANN
        rabatt = 10
    ENDE WENN
    WENN istStammkunde == WAHR DANN
        rabatt = rabatt + 5
    ENDE WENN
    RUECKGABE rabatt
ENDE FUNKTION
```

**Anweisungsueberdeckung (100%):**
Ein einziger Testfall genuegt: `betrag=200, istStammkunde=WAHR` → Alle Anweisungen werden durchlaufen.

**Zweigueberdeckung (100%):**
Mindestens zwei Testfaelle noetig:
1. `betrag=200, istStammkunde=WAHR` → rabatt = 15 (beide WENN-Zweige betreten)
2. `betrag=50, istStammkunde=FALSCH` → rabatt = 0 (beide WENN-Zweige nicht betreten)

---

### Beispiel 3: Entscheidungstabellentest

**Szenario:** Ein Versandhaendler berechnet die Versandkosten:
- Bestellwert > 50 EUR → kostenloser Versand
- Stammkunde → 50% Rabatt auf Versand
- Standardversandkosten: 4,99 EUR

**Entscheidungstabelle:**

| Bedingung | Fall 1 | Fall 2 | Fall 3 | Fall 4 |
|---|---|---|---|---|
| Bestellwert > 50 EUR | Ja | Ja | Nein | Nein |
| Stammkunde | Ja | Nein | Ja | Nein |
| **Versandkosten** | **0,00 EUR** | **0,00 EUR** | **2,50 EUR** | **4,99 EUR** |

→ Bei Bestellwert > 50 EUR ist der Versand immer kostenlos (Stammkunde irrelevant).
→ Bei Bestellwert ≤ 50 EUR und Stammkunde: 50% von 4,99 = 2,50 EUR.

---

## Uebungen

**Aufgabe 1:** Ein Eingabefeld akzeptiert Passwoerter mit einer Laenge von 8 bis 20 Zeichen. Bestimme die Aequivalenzklassen und die Grenzwerte.

**Aufgabe 2:** Erklaere den Unterschied zwischen Anweisungsueberdeckung und Zweigueberdeckung. Warum reicht Anweisungsueberdeckung allein nicht aus?

**Aufgabe 3:** Ein Unternehmen laesst seine neue Buchhaltungssoftware vom Fachbereich testen. Der Tester kennt den Quellcode nicht und prueft anhand der Anforderungen aus dem Pflichtenheft. Um welches Testverfahren handelt es sich? Begruende.

---
---

# Loesungen

## Aufgabe 1

**Aequivalenzklassen:**

| Klasse | Wertebereich | Gueltig? |
|---|---|---|
| K1 | Laenge < 8 (z.B. 7 Zeichen) | Ungueltig |
| K2 | Laenge 8 – 20 | Gueltig |
| K3 | Laenge > 20 (z.B. 21 Zeichen) | Ungueltig |

**Grenzwerte:** 7, 8, 20, 21

Zusaetzlich zu testen: Leere Eingabe (Laenge 0) als Sonderfall der ungueltigen Klasse.

## Aufgabe 2

- **Anweisungsueberdeckung:** Jede Codezeile wird mindestens einmal ausgefuehrt. Problem: Verzweigungen werden ggf. nur in eine Richtung getestet.
- **Zweigueberdeckung:** Jeder Zweig (WAHR und FALSCH) einer Bedingung wird getestet. Strenger als Anweisungsueberdeckung.
- Anweisungsueberdeckung reicht nicht aus, weil ein Fehler im ELSE-Zweig unentdeckt bleiben kann, wenn nur der WENN-Zweig getestet wird.

**Beispiel:** Bei `WENN x > 0 DANN ... ENDE WENN` wuerde ein Testfall mit x=5 die Anweisungsueberdeckung erfuellen, aber der Fall x=0 (WENN-Bedingung ist FALSCH) bliebe ungetestet.

## Aufgabe 3

Es handelt sich um einen **Black-Box-Test**. Begruendung:
1. Der Tester kennt den Quellcode nicht (keine Codekenntnis)
2. Die Testbasis sind die Anforderungen aus dem Pflichtenheft (spezifikationsbasiert)
3. Der Tester stammt aus dem Fachbereich (nicht Entwickler)
4. Es wird geprueft, ob die geforderte Funktionalitaet korrekt umgesetzt wurde
