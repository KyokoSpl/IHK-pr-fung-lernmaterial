# 3.3.05 – Vertiefung und Uebungen: Algorithmen darstellen

## Vertiefung

### Vergleich: Algorithmen-Darstellungen

| Darstellungsform | Vorteile | Nachteile | Einsatz |
|-----------------|---------|-----------|---------|
| Pseudocode | Praezise, sprachunabhaengig | Keine visuelle Darstellung | Pruefung, Dokumentation |
| Programmablaufplan (PAP) | Visuell, leicht verstaendlich | Platzaufwendig, unuebersichtlich bei Groesse | Einfache Ablaeufe |
| Struktogramm (Nassi-Shneiderman) | Strukturiert, kein Spaghetti-Code | Schwer zu zeichnen bei Komplexitaet | Lehre, Entwurf |
| Aktivitaetsdiagramm (UML) | Standard, Parallelitaet | UML-Kenntnisse erforderlich | Geschaeftsprozesse |
| Quellcode | Direkt ausfuehrbar | Sprachspezifisch | Implementierung |

### Rekursion

```
FUNKTION fakultaet(n)
    WENN n <= 1 DANN
        RUECKGABE 1
    SONST
        RUECKGABE n * fakultaet(n - 1)
    ENDE-WENN
ENDE-FUNKTION

Aufruf: fakultaet(4)
  → 4 * fakultaet(3)
    → 3 * fakultaet(2)
      → 2 * fakultaet(1)
        → 1  (Basisfall)
      → 2 * 1 = 2
    → 3 * 2 = 6
  → 4 * 6 = 24
```

**Wichtig bei Rekursion**:
1. **Basisfall** (Abbruchbedingung) muss vorhanden sein
2. **Rekursiver Aufruf** muss sich dem Basisfall naehern
3. Ohne Basisfall → **Endlosrekursion** (StackOverflow)

### Algorithmus-Komplexitaet (Big-O-Notation)

| Notation | Name | Beispiel |
|----------|------|---------|
| O(1) | Konstant | Array-Zugriff per Index |
| O(log n) | Logarithmisch | Binaere Suche |
| O(n) | Linear | Lineare Suche |
| O(n log n) | Linearithmisch | Mergesort, Quicksort (Durchschnitt) |
| O(n²) | Quadratisch | Bubble Sort, Selection Sort |
| O(2^n) | Exponentiell | Brute-Force bei Kombinatorik |

---

### Pruefungsaspekte

**Typische Fragestellungen**:
1. "Was gibt folgender Pseudocode aus?" (Code-Trace)
2. "Schreiben Sie einen Algorithmus in Pseudocode, der..."
3. "Welche Kontrollstruktur wird hier verwendet?"
4. "Korrigieren Sie den folgenden Algorithmus"

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| Off-by-one-Fehler bei Schleifen | Sorgfaeltig pruefen: `<` oder `<=`? Index ab 0 oder 1? |
| Endlosschleife: Abbruchbedingung nie erreicht | Variable im Schleifenkoerper muss sich veraendern |
| Binaere Suche auf unsortierter Liste | Binaere Suche funktioniert NUR auf sortierten Listen |
| Variablen nicht initialisiert | Vor der Schleife Startwerte setzen |
| Rekursion ohne Basisfall | Immer einen Abbruch definieren |

---

## Uebungen

### Aufgabe 1: Code-Trace

Was gibt folgender Pseudocode aus?

```
a = 10
b = 3
ergebnis = 0

SOLANGE a >= b TUE
    a = a - b
    ergebnis = ergebnis + 1
ENDE-SOLANGE

AUSGABE("Ergebnis: " + ergebnis + ", Rest: " + a)
```

Erstelle eine Trace-Tabelle.

---

### Aufgabe 2: Pseudocode schreiben

Schreibe einen Algorithmus in Pseudocode, der:
- Eine Liste von Zahlen entgegennimmt
- Den **Durchschnitt** (Mittelwert) aller Zahlen berechnet
- Das Ergebnis ausgibt

---

### Aufgabe 3: Kontrollstrukturen erkennen

Welche Kontrollstrukturen (Sequenz, einfache Selektion, mehrfache Selektion, kopfgesteuerte Schleife, fussgesteuerte Schleife, Zaehlschleife) werden jeweils verwendet?

a)
```
FUER i VON 1 BIS 100 TUE
    WENN i MOD 2 == 0 DANN
        AUSGABE(i)
    ENDE-WENN
ENDE-FUER
```

b)
```
WIEDERHOLE
    EINGABE(zahl)
BIS zahl > 0
```

c)
```
EINGABE(x)
y = x * 2
AUSGABE(y)
```

---

### Aufgabe 4: Algorithmus korrigieren

Der folgende Algorithmus soll alle Zahlen von 1 bis n addieren. Finde und korrigiere die Fehler:

```
FUNKTION summe(n)
    ergebnis = 1
    FUER i VON 1 BIS n TUE
        ergebnis = ergebnis + 1
    ENDE-FUER
    RUECKGABE ergebnis
ENDE-FUNKTION
```

---

### Aufgabe 5: Algorithmus entwickeln

Schreibe einen Pseudocode-Algorithmus, der prueft, ob eine eingegebene Zahl eine **Primzahl** ist.

Zur Erinnerung: Eine Primzahl ist eine natuerliche Zahl groesser als 1, die nur durch 1 und sich selbst teilbar ist.

---

### Aufgabe 6: Code-Trace (verschachtelte Schleifen)

Was gibt folgender Code aus?

```
FUER i VON 1 BIS 3 TUE
    FUER j VON 1 BIS i TUE
        AUSGABE("*")
    ENDE-FUER
    AUSGABE(NEUE ZEILE)
ENDE-FUER
```

---
---

## Loesung Aufgabe 1

| Schritt | a | b | a >= b? | ergebnis |
|---------|---|---|---------|----------|
| Start | 10 | 3 | ja | 0 |
| 1 | 7 | 3 | ja | 1 |
| 2 | 4 | 3 | ja | 2 |
| 3 | 1 | 3 | nein | 3 |

**Ausgabe**: `Ergebnis: 3, Rest: 1`

Dieser Algorithmus berechnet die **Ganzzahldivision**: 10 / 3 = 3 Rest 1

---

## Loesung Aufgabe 2

```
FUNKTION berechneDurchschnitt(liste)
    WENN laenge(liste) == 0 DANN
        AUSGABE("Liste ist leer")
        RUECKGABE 0
    ENDE-WENN

    summe = 0
    FUER JEDES zahl IN liste TUE
        summe = summe + zahl
    ENDE-FUER

    durchschnitt = summe / laenge(liste)
    AUSGABE("Durchschnitt: " + durchschnitt)
    RUECKGABE durchschnitt
ENDE-FUNKTION
```

---

## Loesung Aufgabe 3

a) **Zaehlschleife** (FUER...VON...BIS) mit **einfacher Selektion** (WENN...DANN) darin
b) **Fussgesteuerte Schleife** (WIEDERHOLE...BIS) – Koerper wird mindestens einmal ausgefuehrt
c) **Sequenz** – drei Anweisungen nacheinander, keine Verzweigung oder Schleife

---

## Loesung Aufgabe 4

**Fehler 1**: `ergebnis = 1` → sollte `ergebnis = 0` sein (falscher Startwert)
**Fehler 2**: `ergebnis = ergebnis + 1` → sollte `ergebnis = ergebnis + i` sein (muss `i` addieren, nicht `1`)

**Korrekter Algorithmus**:
```
FUNKTION summe(n)
    ergebnis = 0
    FUER i VON 1 BIS n TUE
        ergebnis = ergebnis + i
    ENDE-FUER
    RUECKGABE ergebnis
ENDE-FUNKTION
```

---

## Loesung Aufgabe 5

```
FUNKTION istPrimzahl(n)
    WENN n <= 1 DANN
        RUECKGABE FALSCH
    ENDE-WENN

    WENN n == 2 DANN
        RUECKGABE WAHR
    ENDE-WENN

    WENN n MOD 2 == 0 DANN
        RUECKGABE FALSCH
    ENDE-WENN

    FUER i VON 3 BIS wurzel(n) SCHRITT 2 TUE
        WENN n MOD i == 0 DANN
            RUECKGABE FALSCH
        ENDE-WENN
    ENDE-FUER

    RUECKGABE WAHR
ENDE-FUNKTION
```

**Optimierung**: Man prueft nur bis zur Wurzel von n, da groessere Teiler bereits als kleinere Teiler gefunden worden waeren. Gerade Zahlen > 2 werden sofort ausgeschlossen.

---

## Loesung Aufgabe 6

```
i=1: j laeuft von 1 bis 1 → *
     (Neue Zeile)
i=2: j laeuft von 1 bis 2 → **
     (Neue Zeile)
i=3: j laeuft von 1 bis 3 → ***
     (Neue Zeile)
```

**Ausgabe**:
```
*
**
***
```

Es entsteht ein **Dreiecksmuster** – eine typische Pruefungsaufgabe fuer verschachtelte Schleifen.
