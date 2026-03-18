# Beispiele: 1.4.06 – Programmiersprachen

## Kontrollstrukturen

**Beispiel 1 – Verzweigung (Pseudocode):**
```
EINGABE alter
WENN alter >= 18 DANN
    AUSGABE "Volljaehrig"
SONST
    AUSGABE "Minderjaehrig"
ENDE WENN
```

**Beispiel 2 – Zaehlschleife:**
```
summe = 0
FUER i VON 1 BIS 100
    summe = summe + i
ENDE FUER
AUSGABE summe    // Ergebnis: 5050
```

**Beispiel 3 – while-Schleife:**
```
passwort = ""
SOLANGE passwort != "geheim"
    EINGABE passwort
    WENN passwort != "geheim" DANN
        AUSGABE "Falsches Passwort"
    ENDE WENN
ENDE SOLANGE
AUSGABE "Zugang gewaehrt"
```

---

## OOP – Klasse und Objekt

**Beispiel 4 – Pseudocode Klasse:**
```
KLASSE Kunde
    PRIVAT name: String
    PRIVAT kundennummer: Integer

    OEFFENTLICH METHODE getName(): String
        RUECKGABE name
    ENDE METHODE

    OEFFENTLICH METHODE setName(neuerName: String)
        name = neuerName
    ENDE METHODE
ENDE KLASSE

// Objekt erzeugen:
kunde1 = NEU Kunde()
kunde1.setName("Mueller")
AUSGABE kunde1.getName()    // "Mueller"
```

---

## Fehlerarten

**Beispiel 5 – Syntaxfehler:**
```
int x = 10
// Fehlendes Semikolon → Compiler meldet Fehler, Programm startet nicht
```

**Beispiel 6 – Laufzeitfehler:**
```
int a = 10
int b = 0
int ergebnis = a / b    // Division durch Null → Programmabbruch zur Laufzeit
```

**Beispiel 7 – Logikfehler:**
```
// Aufgabe: MwSt berechnen (19%)
double netto = 100.0
double brutto = netto * 0.19    // FALSCH: Ergebnis = 19.0 (nur MwSt, nicht Brutto)
// Korrekt: brutto = netto * 1.19 = 119.0
```

---

## Compiler vs. Interpreter

**Beispiel 8:** Ein Java-Programm wird kompiliert (`javac Programm.java` → `Programm.class`), dann auf der JVM ausgefuehrt (`java Programm`). → Compiler erzeugt Bytecode, JVM interpretiert diesen.

**Beispiel 9:** Ein Python-Skript wird direkt ausgefuehrt (`python skript.py`). Der Interpreter liest, uebersetzt und fuehrt Zeile fuer Zeile aus. Fehler in Zeile 50 werden erst erkannt, wenn die Ausfuehrung diese Zeile erreicht.
