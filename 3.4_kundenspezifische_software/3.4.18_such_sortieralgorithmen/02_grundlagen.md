# Grundlagen: 3.4.18 – Einfache Such- und Sortier-Algorithmen

## Lineare Suche

**Definition:** Die lineare Suche (Sequential Search) durchlaeuft eine Liste Element fuer Element von Anfang bis Ende, bis der gesuchte Wert gefunden wird oder das Ende der Liste erreicht ist.

**Voraussetzung:** Keine – funktioniert auf beliebigen (auch unsortierten) Listen.

**Pseudocode:**

```
METHODE lineareSuche(liste: Liste, gesucht: Wert): Zahl
    FUER i VON 0 BIS laenge(liste) - 1
        WENN liste[i] == gesucht DANN
            RUECKGABE i          // Index zurueckgeben
        ENDE WENN
    ENDE FUER
    RUECKGABE -1                 // Nicht gefunden
ENDE METHODE
```

**Ablaufverfolgung (Trace):**

Liste: `[12, 45, 7, 23, 38, 9]`, gesucht: `23`

| Schritt | i | liste[i] | Vergleich | Ergebnis |
|---------|---|----------|-----------|----------|
| 1 | 0 | 12 | 12 == 23? | Nein |
| 2 | 1 | 45 | 45 == 23? | Nein |
| 3 | 2 | 7 | 7 == 23? | Nein |
| 4 | 3 | 23 | 23 == 23? | **Ja → Rueckgabe 3** |

→ 4 Vergleiche noetig.

**Komplexitaet:**

| Fall | Vergleiche | O-Notation |
|------|-----------|------------|
| Best Case | 1 (erstes Element) | O(1) |
| Worst Case | n (letztes Element oder nicht vorhanden) | O(n) |
| Average Case | n/2 | O(n) |

---

## Binaere Suche

**Definition:** Die binaere Suche halbiert in jedem Schritt den Suchbereich. Sie vergleicht den gesuchten Wert mit dem mittleren Element und entscheidet, ob in der linken oder rechten Haelfte weitergesucht wird.

**Voraussetzung:** Die Liste muss **sortiert** sein!

**Pseudocode:**

```
METHODE binaereSuche(liste: Liste, gesucht: Wert): Zahl
    links = 0
    rechts = laenge(liste) - 1

    SOLANGE links <= rechts
        mitte = (links + rechts) / 2     // ganzzahlig
        WENN liste[mitte] == gesucht DANN
            RUECKGABE mitte
        SONST WENN liste[mitte] < gesucht DANN
            links = mitte + 1             // rechte Haelfte
        SONST
            rechts = mitte - 1            // linke Haelfte
        ENDE WENN
    ENDE SOLANGE

    RUECKGABE -1                          // Nicht gefunden
ENDE METHODE
```

**Ablaufverfolgung (Trace):**

Liste: `[3, 7, 12, 23, 38, 45, 67]`, gesucht: `38`

| Schritt | links | rechts | mitte | liste[mitte] | Vergleich | Aktion |
|---------|-------|--------|-------|-------------|-----------|--------|
| 1 | 0 | 6 | 3 | 23 | 23 < 38 | links = 4 |
| 2 | 4 | 6 | 5 | 45 | 45 > 38 | rechts = 4 |
| 3 | 4 | 4 | 4 | 38 | 38 == 38 | **Gefunden! Index 4** |

→ Nur 3 Vergleiche statt 5 (linear).

**Komplexitaet:**

| Fall | Vergleiche | O-Notation |
|------|-----------|------------|
| Best Case | 1 (mittleres Element) | O(1) |
| Worst Case | log₂(n) | O(log n) |
| Average Case | log₂(n) | O(log n) |

**Beispielrechnung:** Bei 1.000.000 Elementen:
- Lineare Suche: bis zu 1.000.000 Vergleiche
- Binaere Suche: max. log₂(1.000.000) ≈ **20 Vergleiche**

---

## Bubble Sort

**Definition:** Bubble Sort vergleicht wiederholt benachbarte Elemente und tauscht sie, wenn sie in der falschen Reihenfolge stehen. Grosse Werte "blubbern" nach oben (rechts).

**Pseudocode:**

```
METHODE bubbleSort(liste: Liste)
    n = laenge(liste)
    FUER i VON 0 BIS n - 2
        FUER j VON 0 BIS n - 2 - i
            WENN liste[j] > liste[j + 1] DANN
                // Tauschen
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp
            ENDE WENN
        ENDE FUER
    ENDE FUER
ENDE METHODE
```

**Ablaufverfolgung (Trace):**

Liste: `[5, 3, 8, 1]`

```
Durchlauf 1: [5,3,8,1] → [3,5,8,1] → [3,5,8,1] → [3,5,1,8]
              (5>3: Tausch) (5<8: kein) (8>1: Tausch)
              → 8 ist am richtigen Platz

Durchlauf 2: [3,5,1,8] → [3,5,1,8] → [3,1,5,8]
              (3<5: kein) (5>1: Tausch)
              → 5 ist am richtigen Platz

Durchlauf 3: [3,1,5,8] → [1,3,5,8]
              (3>1: Tausch)
              → Fertig: [1,3,5,8]
```

**Komplexitaet:** O(n²) in allen Faellen (Optimierung mit Abbruchflag: O(n) Best Case).

---

## Selection Sort

**Definition:** Selection Sort sucht in der unsortierten Teilliste das kleinste Element und tauscht es an die richtige Position (vorne).

**Pseudocode:**

```
METHODE selectionSort(liste: Liste)
    n = laenge(liste)
    FUER i VON 0 BIS n - 2
        minIndex = i
        FUER j VON i + 1 BIS n - 1
            WENN liste[j] < liste[minIndex] DANN
                minIndex = j
            ENDE WENN
        ENDE FUER
        // Tauschen
        WENN minIndex != i DANN
            temp = liste[i]
            liste[i] = liste[minIndex]
            liste[minIndex] = temp
        ENDE WENN
    ENDE FUER
ENDE METHODE
```

**Ablaufverfolgung (Trace):**

Liste: `[5, 3, 8, 1]`

```
Durchlauf 1: Minimum in [5,3,8,1] = 1 (Index 3)
             Tausche Index 0 und 3 → [1,3,8,5]

Durchlauf 2: Minimum in [3,8,5] = 3 (Index 1)
             Kein Tausch noetig → [1,3,8,5]

Durchlauf 3: Minimum in [8,5] = 5 (Index 3)
             Tausche Index 2 und 3 → [1,3,5,8]

→ Fertig: [1,3,5,8]
```

**Komplexitaet:** O(n²) in allen Faellen.

---

## Insertion Sort

**Definition:** Insertion Sort nimmt nacheinander jedes Element und fuegt es an der richtigen Stelle in den bereits sortierten Teil der Liste ein (aehnlich wie Karten sortieren auf der Hand).

**Pseudocode:**

```
METHODE insertionSort(liste: Liste)
    n = laenge(liste)
    FUER i VON 1 BIS n - 1
        schluessel = liste[i]
        j = i - 1
        SOLANGE j >= 0 UND liste[j] > schluessel
            liste[j + 1] = liste[j]       // nach rechts schieben
            j = j - 1
        ENDE SOLANGE
        liste[j + 1] = schluessel          // einfuegen
    ENDE FUER
ENDE METHODE
```

**Ablaufverfolgung (Trace):**

Liste: `[5, 3, 8, 1]`

```
Schritt 1: Schluessel = 3, sortierter Teil [5]
           3 < 5 → 5 nach rechts → [_,5,8,1] → 3 einfuegen → [3,5,8,1]

Schritt 2: Schluessel = 8, sortierter Teil [3,5]
           8 > 5 → kein Verschieben → [3,5,8,1]

Schritt 3: Schluessel = 1, sortierter Teil [3,5,8]
           1 < 8 → 8 nach rechts
           1 < 5 → 5 nach rechts
           1 < 3 → 3 nach rechts
           → [_,3,5,8] → 1 einfuegen → [1,3,5,8]

→ Fertig: [1,3,5,8]
```

**Komplexitaet:**

| Fall | O-Notation |
|------|------------|
| Best Case (bereits sortiert) | O(n) |
| Worst Case (umgekehrt sortiert) | O(n²) |
| Average Case | O(n²) |
