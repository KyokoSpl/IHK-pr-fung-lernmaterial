# Komplett: 3.4.16 – Algorithmen erstellen

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.16
- **Thema:** Algorithmen erstellen koennen

## Ziel

Du musst Algorithmen in Pseudocode formulieren koennen. In der Pruefung werden haeufig Aufgaben gestellt, bei denen ein Algorithmus in allgemein verstaendlichem Pseudocode geschrieben oder analysiert werden muss. Dazu gehoeren gaengige Muster wie Suche, Sortierung, Akkumulator und Schleifen.

## Themenkreise

| Nr. | Themenkreis | Schwerpunkt |
|-----|-------------|-------------|
| 1 | Pseudocode | Konventionen, Lesbarkeit, Pruefungsformat |

---

## Grundlagen

### Was ist ein Algorithmus?

**Definition:** Ein Algorithmus ist eine eindeutige, endliche Folge von Anweisungen zur Loesung eines Problems.

**Eigenschaften eines Algorithmus:**

| Eigenschaft | Bedeutung |
|-------------|-----------|
| Eindeutigkeit | Jeder Schritt ist klar definiert |
| Endlichkeit | Der Algorithmus terminiert nach endlich vielen Schritten |
| Ausfuehrbarkeit | Jeder Schritt ist ausfuehrbar |
| Allgemeinheit | Loesung gilt fuer eine Klasse von Problemen, nicht nur fuer einen Einzelfall |
| Determiniertheit | Gleiche Eingabe fuehrt immer zum gleichen Ergebnis |

### Pseudocode-Konventionen (IHK-Pruefung)

In IHK-Pruefungen wird Pseudocode verwendet, der sprachunabhaengig und allgemein verstaendlich ist. Es gibt keinen festen Standard, aber folgende Konventionen haben sich durchgesetzt:

**Kontrollstrukturen:**

```
// Verzweigung
WENN bedingung DANN
    anweisungen
SONST WENN andere_bedingung DANN
    anweisungen
SONST
    anweisungen
ENDE WENN

// Schleife mit Zaehler
FUER i VON 1 BIS n
    anweisungen
ENDE FUER

// Schleife mit Bedingung
SOLANGE bedingung
    anweisungen
ENDE SOLANGE

// Schleife ueber Sammlung
FUER JEDES element IN sammlung
    anweisungen
ENDE FUER

// Wiederhole-bis-Schleife
WIEDERHOLE
    anweisungen
BIS bedingung
```

**Weitere Konventionen:**

| Element | Pseudocode-Schreibweise |
|---------|------------------------|
| Variable zuweisen | `x = 5` oder `setze x auf 5` |
| Ausgabe | `ausgabe("Text")` oder `AUSGABE "Text"` |
| Eingabe | `eingabe(x)` oder `LIES x` |
| Rueckgabe | `RUECKGABE wert` |
| Kommentar | `// Kommentar` |
| Methode/Funktion | `METHODE name(parameter): Rueckgabetyp` |
| Klasse | `KLASSE Name` ... `ENDE KLASSE` |
| Array-Zugriff | `liste[i]` oder `liste[0]` (0-basiert) |
| Laenge | `laenge(liste)` |

### Gaengige Algorithmus-Muster

#### 1. Akkumulator-Muster (Summierung)

```
METHODE berechneSumme(zahlen: Liste): Zahl
    summe = 0
    FUER JEDES z IN zahlen
        summe = summe + z
    ENDE FUER
    RUECKGABE summe
ENDE METHODE
```

#### 2. Zaehler-Muster

```
METHODE zaehleGerade(zahlen: Liste): Zahl
    anzahl = 0
    FUER JEDES z IN zahlen
        WENN z MOD 2 == 0 DANN
            anzahl = anzahl + 1
        ENDE WENN
    ENDE FUER
    RUECKGABE anzahl
ENDE METHODE
```

#### 3. Minimum/Maximum finden

```
METHODE findeMaximum(zahlen: Liste): Zahl
    max = zahlen[0]
    FUER i VON 1 BIS laenge(zahlen) - 1
        WENN zahlen[i] > max DANN
            max = zahlen[i]
        ENDE WENN
    ENDE FUER
    RUECKGABE max
ENDE METHODE
```

#### 4. Lineare Suche

```
METHODE lineareSuche(liste: Liste, gesucht: Wert): Zahl
    FUER i VON 0 BIS laenge(liste) - 1
        WENN liste[i] == gesucht DANN
            RUECKGABE i       // Index des gefundenen Elements
        ENDE WENN
    ENDE FUER
    RUECKGABE -1              // Nicht gefunden
ENDE METHODE
```

#### 5. Tausch-Muster (Swap)

```
// Zwei Elemente in einer Liste tauschen
temp = liste[a]
liste[a] = liste[b]
liste[b] = temp
```

#### 6. Zeichenkette umkehren

```
METHODE umkehren(text: String): String
    ergebnis = ""
    FUER i VON laenge(text) - 1 BIS 0 (rueckwaerts)
        ergebnis = ergebnis + text[i]
    ENDE FUER
    RUECKGABE ergebnis
ENDE METHODE
```

### Darstellungsformen von Algorithmen

| Form | Beschreibung | Einsatz |
|------|-------------|---------|
| Pseudocode | Strukturierter Text, sprachunabhaengig | IHK-Pruefung, Entwurfsphase |
| Programmablaufplan (PAP) | Grafisch mit Symbolen (Raute, Rechteck, Oval) | Visualisierung fuer Entscheider |
| Struktogramm (Nassi-Shneiderman) | Verschachtelte Bloecke | Strukturierte Darstellung |
| Programmiersprache | Konkreter Code (Java, Python, C#) | Implementierung |

---

## Vertiefung

### Tipps fuer Pseudocode in der Pruefung

1. **Lesbarkeit vor Korrektheit:** Pruefende muessen den Code verstehen koennen
2. **Einrueckung verwenden:** Zeigt Blockzugehoerigkeit klar an
3. **Variablen sprechend benennen:** `summe` statt `s`, `kundenListe` statt `kl`
4. **ENDE-Markierungen setzen:** `ENDE WENN`, `ENDE FUER` – macht Bloecke eindeutig
5. **Keine sprachspezifische Syntax:** Kein `{`, kein `def`, kein `public static void`
6. **Datentypen angeben, wenn sinnvoll:** `anzahl: Ganzzahl`, `name: String`

### Zusammengesetztes Beispiel: Notendurchschnitt berechnen

```
METHODE berechneNotendurchschnitt(noten: Liste von Zahlen): Zahl
    WENN laenge(noten) == 0 DANN
        RUECKGABE 0
    ENDE WENN

    summe = 0
    FUER JEDES note IN noten
        summe = summe + note
    ENDE FUER

    durchschnitt = summe / laenge(noten)
    RUECKGABE durchschnitt
ENDE METHODE

// Verwendung:
schuelerNoten = [2, 1, 3, 2, 4]
ergebnis = berechneNotendurchschnitt(schuelerNoten)
ausgabe("Durchschnitt: " + ergebnis)     // Ausgabe: Durchschnitt: 2.4
```

### Zusammengesetztes Beispiel: Rabattberechnung

```
METHODE berechneRabatt(betrag: Zahl, kundentyp: String): Zahl
    WENN kundentyp == "Premium" DANN
        rabatt = betrag * 0.15      // 15% Rabatt
    SONST WENN kundentyp == "Stamm" DANN
        rabatt = betrag * 0.10      // 10% Rabatt
    SONST
        rabatt = 0                  // Kein Rabatt
    ENDE WENN

    endbetrag = betrag - rabatt
    RUECKGABE endbetrag
ENDE METHODE
```

### Typische Pruefungsaspekte
- Pseudocode lesen und das Ergebnis angeben (Trace / Ablaufverfolgung)
- Fehlenden Code in einem Algorithmus ergaenzen (Lueckentext)
- Algorithmus fuer eine beschriebene Aufgabe in Pseudocode schreiben
- Kontrollstrukturen korrekt anwenden (Verzweigung, Schleife)
- Variablen und ihre Werte waehrend des Ablaufs nachverfolgen

### Haeufige Fehler
- Endlosschleifen: Schleifenbedingung wird nie falsch (z.B. Zaehler vergessen zu erhoehen)
- Off-by-one-Fehler: Index beginnt bei 0, aber Schleife bei 1 (oder umgekehrt)
- Variablen nicht initialisiert: `summe` muss vor der Schleife auf 0 gesetzt werden
- RUECKGABE innerhalb der Schleife: Gibt sofort zurueck, statt alle Elemente zu durchlaufen
- Division durch Null nicht abgefangen

---

## Uebungen

**Aufgabe 1:** Schreibe einen Algorithmus in Pseudocode, der aus einer Liste von Zahlen alle geraden Zahlen in eine neue Liste uebernimmt und diese zurueckgibt.

**Aufgabe 2:** Was gibt folgender Pseudocode aus?

```
x = 10
y = 3
SOLANGE x > 0
    x = x - y
    ausgabe(x)
ENDE SOLANGE
```

**Aufgabe 3:** Schreibe einen Algorithmus in Pseudocode, der prueft, ob ein eingegebenes Wort ein Palindrom ist (vorwaerts und rueckwaerts gleich, z.B. "ANNA").

**Aufgabe 4:** Ein Onlineshop gewaehrt ab einem Bestellwert von 100 EUR kostenlosen Versand. Unter 100 EUR kostet der Versand 4,99 EUR. Schreibe den Algorithmus in Pseudocode, der den Gesamtpreis berechnet.

**Aufgabe 5:** Korrigiere den folgenden fehlerhaften Pseudocode, der die Fakultaet einer Zahl berechnen soll:

```
METHODE fakultaet(n: Zahl): Zahl
    ergebnis = 0
    FUER i VON 1 BIS n
        ergebnis = ergebnis * i
    ENDE FUER
    RUECKGABE ergebnis
ENDE METHODE
```

**Aufgabe 6:** Schreibe einen Algorithmus in Pseudocode, der eine Liste von Schueler-Noten einliest und die Anzahl der Schueler mit der Note 1 oder 2 zaehlt.

---
---

# Loesungen

## Aufgabe 1

```
METHODE filtereGerade(zahlen: Liste): Liste
    ergebnis = neue leere Liste
    FUER JEDES z IN zahlen
        WENN z MOD 2 == 0 DANN
            ergebnis.hinzufuegen(z)
        ENDE WENN
    ENDE FUER
    RUECKGABE ergebnis
ENDE METHODE
```

## Aufgabe 2
Ausgabe: 7, 4, 1, -2
Erklaerung: x wird sukzessive um 3 verringert (10→7→4→1→-2). Bei x = -2 ist die Bedingung x > 0 nicht mehr erfuellt → Schleife endet. Hinweis: -2 wird noch ausgegeben, weil die Ausgabe VOR der Bedingungspruefung der naechsten Iteration erfolgt.

## Aufgabe 3

```
METHODE istPalindrom(wort: String): Wahrheitswert
    links = 0
    rechts = laenge(wort) - 1
    SOLANGE links < rechts
        WENN wort[links] != wort[rechts] DANN
            RUECKGABE FALSCH
        ENDE WENN
        links = links + 1
        rechts = rechts - 1
    ENDE SOLANGE
    RUECKGABE WAHR
ENDE METHODE
```

## Aufgabe 4

```
METHODE berechneGesamtpreis(bestellwert: Zahl): Zahl
    WENN bestellwert >= 100 DANN
        versand = 0
    SONST
        versand = 4.99
    ENDE WENN
    gesamtpreis = bestellwert + versand
    RUECKGABE gesamtpreis
ENDE METHODE
```

## Aufgabe 5
Fehler: `ergebnis = 0` → Multiplikation mit 0 ergibt immer 0.
Korrektur: `ergebnis = 1`

```
METHODE fakultaet(n: Zahl): Zahl
    ergebnis = 1                    // <-- korrigiert (war 0)
    FUER i VON 1 BIS n
        ergebnis = ergebnis * i
    ENDE FUER
    RUECKGABE ergebnis
ENDE METHODE
```

## Aufgabe 6

```
METHODE zaehleGuteNoten(noten: Liste): Zahl
    anzahl = 0
    FUER JEDES note IN noten
        WENN note == 1 ODER note == 2 DANN
            anzahl = anzahl + 1
        ENDE WENN
    ENDE FUER
    RUECKGABE anzahl
ENDE METHODE

// Verwendung:
noten = [2, 3, 1, 4, 2, 1, 5, 2]
ergebnis = zaehleGuteNoten(noten)
ausgabe("Anzahl mit Note 1 oder 2: " + ergebnis)    // Ausgabe: 5
```
