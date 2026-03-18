# 3.3.08 – Qualitaetssicherung und Tests

## Einordnung

Dieses Thema gehoert zum Bereich **3.3 Programmieren von Softwareloesungen** und behandelt grundlegende Testverfahren und Strategien der Qualitaetssicherung in der Softwareentwicklung.

## Themenkreise

| Nr. | Themenkreis | Schwerpunkt |
|-----|-------------|-------------|
| 1 | Black Box-/White Box-Tests | Testverfahren nach Kenntnisstand des inneren Aufbaus |
| 2 | Grundsaetzliches Vorgehen beim Testen | TDD, Unit-Test, E2E-Test, Print-Debugging |

---

## Querverweise

- **3.3.01** – Qualitaetsmerkmale (Testbarkeit als Qualitaetsmerkmal)
- **3.3.05** – Algorithmen (Code-Traces als manueller Test)
- **3.1** – Qualitaetsmanagement allgemein

---

## TK 1: Black Box- vs. White Box-Tests

### Definitionen

| Merkmal | Black Box-Test | White Box-Test |
|---------|---------------|----------------|
| **Prinzip** | Tester kennt die innere Struktur NICHT | Tester kennt die innere Struktur (Code) |
| **Fokus** | Was kommt rein, was kommt raus? | Logische Pfade, Verzweigungen, Schleifen |
| **Synonyme** | Funktionstest, spezifikationsbasiert | Strukturtest, codebasiert |
| **Testbasis** | Anforderungen, Spezifikation | Quellcode, Architektur |
| **Wer testet?** | Tester, Fachbereich, Endanwender | Entwickler |
| **Beispiel** | Eingabe von Werten, Pruefen der Ausgabe | Code-Coverage messen, Pfade abdecken |

```
Black Box:
+------------------+
|                  |
Eingabe ──→ |   ? ? ? ?   | ──→ Ausgabe
|   (unbekannt)    |
+------------------+
Pruefe: Stimmt die Ausgabe mit der Erwartung ueberein?

White Box:
+------------------+
|  if (x > 0)     |
Eingabe ──→ |    return x*2  | ──→ Ausgabe
|  else            |
|    return 0      |
+------------------+
Pruefe: Werden alle Pfade (if/else) durchlaufen?
```

### Black Box-Techniken

| Technik | Beschreibung | Beispiel |
|---------|-------------|---------|
| **Aequivalenzklassenbildung** | Eingabewerte in Klassen einteilen, eine pro Klasse testen | Alter 0-17 (minderjaehrig), 18-120 (volljaehrig) |
| **Grenzwertanalyse** | Werte an den Grenzen der Klassen testen | 17, 18, 0, -1, 121 |
| **Entscheidungstabelle** | Alle Kombinationen von Bedingungen testen | Rabatt bei Stammkunde UND Grossbestellung |
| **Zustandsuebergangstest** | Testen basierend auf Zustandsdiagramm | Bestellung: Neu → Bezahlt → Versendet |

### White Box-Techniken

| Technik | Beschreibung | Ziel |
|---------|-------------|------|
| **Anweisungsueberdeckung** (Statement Coverage) | Jede Anweisung mind. 1x ausfuehren | C0-Abdeckung |
| **Zweigueberdeckung** (Branch Coverage) | Jeden Zweig (if/else) mind. 1x durchlaufen | C1-Abdeckung |
| **Pfadueberdeckung** (Path Coverage) | Jeden moeglichen Pfad testen | C2-Abdeckung (aufwendig!) |
| **Bedingungsueberdeckung** | Jede Teilbedingung auf true/false testen | Bei zusammengesetzten Bedingungen |

### Grenzwertanalyse – Beispiel

```
Regel: Rabatt von 10% bei Bestellwert >= 100 EUR

Aequivalenzklassen:
  Klasse 1: Bestellwert < 100  → kein Rabatt
  Klasse 2: Bestellwert >= 100 → 10% Rabatt

Grenzwerte testen:
  99.99 EUR  → kein Rabatt (Grenze untere Klasse)
  100.00 EUR → 10% Rabatt  (Grenze obere Klasse)
  100.01 EUR → 10% Rabatt  (knapp ueber Grenze)
  0.00 EUR   → kein Rabatt (Minimum)
  -1.00 EUR  → Fehler/ungueltig (ungueltige Eingabe)
```

---

## TK 2: Grundsaetzliches Vorgehen beim Testen

### Die Testpyramide

```
         /\
        /  \           E2E-Tests
       / E2E\          (wenige, langsam, teuer)
      /------\
     /        \        Integrationstests
    / Integr.  \       (mittlere Anzahl)
   /------------\
  /              \     Unit-Tests
 /   Unit-Tests   \    (viele, schnell, guenstig)
/------------------\
```

| Teststufe | Beschreibung | Geschwindigkeit | Anzahl |
|-----------|-------------|----------------|--------|
| **Unit-Test** | Testet einzelne Funktionen/Methoden isoliert | Sehr schnell (ms) | Viele (Hunderte) |
| **Integrationstest** | Testet Zusammenspiel mehrerer Komponenten | Mittel (Sekunden) | Mittel |
| **E2E-Test** (End-to-End) | Testet gesamtes System aus Benutzersicht | Langsam (Minuten) | Wenige |

### Unit-Tests

**Definition**: Testen einer **einzelnen Einheit** (Methode/Funktion) **isoliert** von anderen Komponenten.

**AAA-Pattern** (Arrange – Act – Assert):

```
TESTFALL: "berechneRabatt gibt 10% bei Bestellwert >= 100"

// 1. ARRANGE (Vorbereiten)
bestellwert = 150.00
erwarteterRabatt = 15.00

// 2. ACT (Ausfuehren)
tatsaechlicherRabatt = berechneRabatt(bestellwert)

// 3. ASSERT (Pruefen)
PRUEFE_GLEICH(erwarteterRabatt, tatsaechlicherRabatt)        // ✓ Test bestanden
```

### Beispiel: Unit-Test in Pseudocode

```
FUNKTION berechneRabatt(wert)
    WENN wert >= 100 DANN
        RUECKGABE wert * 0.10
    SONST
        RUECKGABE 0
    ENDE-WENN
ENDE-FUNKTION

// --- Tests ---

TEST "Rabatt bei 150 EUR"
    PRUEFE_GLEICH(15.0, berechneRabatt(150))

TEST "Kein Rabatt bei 50 EUR"
    PRUEFE_GLEICH(0, berechneRabatt(50))

TEST "Grenzwert: Rabatt bei genau 100 EUR"
    PRUEFE_GLEICH(10.0, berechneRabatt(100))

TEST "Grenzwert: Kein Rabatt bei 99.99 EUR"
    PRUEFE_GLEICH(0, berechneRabatt(99.99))
```

### TDD – Test-Driven Development

**Prinzip**: Erst den Test schreiben, DANN den Code.

```
TDD-Zyklus: Red → Green → Refactor

1. RED:      Test schreiben → Test schlaegt fehl (rot)
             (weil die Funktion noch nicht existiert)

2. GREEN:    Minimalen Code schreiben → Test besteht (gruen)
             (nur so viel Code, dass der Test durchlaeuft)

3. REFACTOR: Code verbessern → Test besteht weiterhin
             (Aufraumen, ohne Funktionalitaet zu aendern)

             +---------+
             |   RED   | ← Test schreiben
             +----+----+
                  |
                  v
             +---------+
             |  GREEN  | ← Code schreiben
             +----+----+
                  |
                  v
             +---------+
             |REFACTOR | ← Code verbessern
             +----+----+
                  |
                  └──→ zurueck zu RED
```

**Vorteile von TDD**:
- Hohe Testabdeckung (jeder Code hat mindestens einen Test)
- Klarere Anforderungen (Test definiert gewuenschtes Verhalten)
- Weniger Bugs, sichereres Refactoring
- Dokumentation durch Tests

### Print-Debugging

**Definition**: Einfuegen von Ausgabebefehlen (`print`, `console.log`, `System.out.println`) zum Nachvollziehen des Programmflusses.

```
FUNKTION berechne(x, y)
    print("berechne aufgerufen: x=" + x + ", y=" + y)   // Debug
    ergebnis = x * y + 10
    print("ergebnis = " + ergebnis)                       // Debug
    RUECKGABE ergebnis
ENDE-FUNKTION
```

| Vorteile | Nachteile |
|---------|-----------|
| Einfach, schnell einsetzbar | Muss nach dem Debugging entfernt werden |
| Kein Debugger-Setup noetig | Ueberflutet die Ausgabe bei vielen Prints |
| Funktioniert ueberall | Professioneller: Logging-Framework oder Debugger |

### Mock-Objekte

**Definition**: Simulierte Objekte, die das Verhalten realer Abhaengigkeiten nachahmen, um **isolierte Unit-Tests** zu ermoeglichen.

```
Problem: Die zu testende Methode braucht eine Datenbank
         → Im Test wollen wir NICHT die echte DB verwenden

Loesung: Mock-Objekt simuliert die Datenbank

KLASSE MockDatenbank
    FUNKTION ladeKunde(id)
        // Statt echte DB-Abfrage: fester Testwert
        RUECKGABE neuer Kunde(id=42, name="Testperson")
    ENDE-FUNKTION
ENDE-KLASSE

TEST "Bestellung fuer Bestandskunde"
    db = neues MockDatenbank()          // Mock statt echte DB
    service = neuer BestellService(db)
    ergebnis = service.bestelle(kundeId=42, artikelId=1)
    PRUEFE_GLEICH("Bestellung erfolgreich", ergebnis)
```

**Warum Mocks?**
- Unit-Tests sollen **schnell** und **unabhaengig** sein
- Keine reale Datenbank, kein Netzwerk, kein Dateisystem noetig
- Kontrollierbare Testbedingungen (z.B. Fehlerfaelle simulieren)

---

## Zusammenfassung: Teststufen im Entwicklungsprozess

| Stufe | Wer testet? | Was wird getestet? | Methode |
|-------|------------|-------------------|---------|
| **Unit-Test** | Entwickler | Einzelne Methoden/Funktionen | White Box |
| **Integrationstest** | Entwickler/Tester | Zusammenspiel von Modulen | White/Black Box |
| **Systemtest** | Tester | Gesamtsystem gegen Spezifikation | Black Box |
| **Abnahmetest** | Kunde/Fachbereich | System gegen Anforderungen | Black Box |

---

## Pruefungsaspekte

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| Black Box und White Box verwechseln | Black Box = Innenleben unbekannt, White Box = Code ist bekannt |
| "Unit-Test testet die ganze Anwendung" | Unit-Test testet EINE Einheit isoliert |
| TDD = "Tests nach dem Code schreiben" | TDD = Tests ZUERST schreiben! |
| E2E-Tests als einzige Teststrategie | Testpyramide beachten: Basis = viele Unit-Tests |
| Mock und Stub verwechseln | Mock = prueft Interaktion, Stub = liefert nur Daten |
| Grenzwertanalyse vergessen | Immer Grenzen der Aequivalenzklassen testen! |

---

## Uebungen

### Aufgabe 1: Black Box oder White Box?

Ordne zu:

| Nr. | Situation | BB oder WB? |
|-----|-----------|-------------|
| a) | Tester gibt verschiedene Eingabewerte ein und prueft die Ausgabe | |
| b) | Entwickler stellt sicher, dass jeder if-Zweig durchlaufen wird | |
| c) | Fachbereich prueft, ob die Anforderungen erfuellt sind | |
| d) | Entwickler misst die Code-Coverage | |
| e) | Tester testet mit Grenzwerten an der Bestellwert-Schwelle | |

### Aufgabe 2: Testfaelle mit Grenzwertanalyse

Eine Funktion gibt bei Alter >= 18 "volljaehrig" und bei Alter < 18 "minderjaehrig" zurueck. Gueltiger Wertebereich: 0-150.

Welche Testfaelle erstellst du?

### Aufgabe 3: TDD-Zyklus beschreiben

Beschreibe die drei Phasen des TDD-Zyklus anhand der Aufgabe: "Erstelle eine Funktion `istGerade(zahl)`, die `true` zurueckgibt wenn die Zahl gerade ist."

---
---

## Loesung Aufgabe 1

| Nr. | Situation | Typ |
|-----|-----------|-----|
| a) | Eingabe/Ausgabe pruefen | **Black Box** – kein Codewissen noetig |
| b) | if-Zweige durchlaufen | **White Box** – Code muss bekannt sein (Zweigueberdeckung) |
| c) | Fachbereich prueft Anforderungen | **Black Box** – Abnahmetest gegen Spezifikation |
| d) | Code-Coverage messen | **White Box** – Analyse des Quellcodes |
| e) | Grenzwerte testen | **Black Box** – Grenzwertanalyse ist Black-Box-Technik |

---

## Loesung Aufgabe 2

| Nr. | Eingabe (Alter) | Erwartete Ausgabe | Testkategorie |
|-----|-----------------|-------------------|---------------|
| 1 | 0 | "minderjaehrig" | Grenzwert (Minimum gueltig) |
| 2 | 17 | "minderjaehrig" | Grenzwert (unter Schwelle) |
| 3 | 18 | "volljaehrig" | Grenzwert (exakt Schwelle) |
| 4 | 19 | "volljaehrig" | Grenzwert (ueber Schwelle) |
| 5 | 150 | "volljaehrig" | Grenzwert (Maximum gueltig) |
| 6 | -1 | Fehler/ungueltig | Ungueltige Eingabe (unter Minimum) |
| 7 | 151 | Fehler/ungueltig | Ungueltige Eingabe (ueber Maximum) |
| 8 | 10 | "minderjaehrig" | Repraesentant Aequivalenzklasse 1 |
| 9 | 50 | "volljaehrig" | Repraesentant Aequivalenzklasse 2 |

---

## Loesung Aufgabe 3

### Phase 1: RED (Test schreiben – schlaegt fehl)

```
TEST "4 ist gerade"
    PRUEFE_GLEICH(true, istGerade(4))     // ✗ FEHLSCHLAG – Funktion existiert noch nicht

TEST "7 ist ungerade"
    PRUEFE_GLEICH(false, istGerade(7))    // ✗ FEHLSCHLAG
```

### Phase 2: GREEN (minimaler Code – Test besteht)

```
FUNKTION istGerade(zahl)
    RUECKGABE zahl MOD 2 == 0
ENDE-FUNKTION
```

Jetzt bestehen beide Tests. ✓

### Phase 3: REFACTOR (Code verbessern)

In diesem einfachen Fall ist kein Refactoring noetig, da der Code bereits minimal und klar ist. Bei komplexerem Code wuerde man:
- Variablen umbenennen fuer bessere Lesbarkeit
- Doppelten Code entfernen
- Kommentare hinzufuegen

Dann zurueck zu RED: Weitere Tests hinzufuegen (z.B. `istGerade(0)`, `istGerade(-2)`, `istGerade(1)`).
