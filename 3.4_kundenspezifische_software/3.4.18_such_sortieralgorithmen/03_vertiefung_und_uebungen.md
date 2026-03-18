# Vertiefung und Uebungen: 3.4.18 – Einfache Such- und Sortier-Algorithmen

## Vertiefung

### Gesamtvergleich: Suchalgorithmen

| Kriterium | Lineare Suche | Binaere Suche |
|-----------|--------------|--------------|
| Voraussetzung | Keine | Liste muss sortiert sein |
| Prinzip | Element fuer Element | Halbierung des Suchbereichs |
| Best Case | O(1) | O(1) |
| Worst Case | O(n) | O(log n) |
| Average Case | O(n) | O(log n) |
| Eignung | Kleine/unsortierte Listen | Grosse, sortierte Listen |
| Bei 1.000 Elementen max. | 1.000 Vergleiche | 10 Vergleiche |
| Bei 1.000.000 Elementen max. | 1.000.000 Vergleiche | 20 Vergleiche |

### Gesamtvergleich: Sortieralgorithmen

| Kriterium | Bubble Sort | Selection Sort | Insertion Sort |
|-----------|------------|---------------|---------------|
| Prinzip | Benachbarte Elemente tauschen | Minimum suchen und tauschen | Am richtigen Platz einfuegen |
| Best Case | O(n)* | O(n²) | O(n) |
| Worst Case | O(n²) | O(n²) | O(n²) |
| Average Case | O(n²) | O(n²) | O(n²) |
| Stabil** | Ja | Nein | Ja |
| Tauschoperationen | Viele | Wenige (max. n-1) | Wenige (Verschieben) |
| Eignung | Lernzweck, kleine Listen | Wenn Tauschoperationen teuer sind | Fast sortierte Listen |

*mit Optimierung (Abbruch wenn keine Taeusche in einem Durchlauf)
**Stabil = Elemente mit gleichem Wert behalten ihre urspruengliche Reihenfolge

### O-Notation (Landau-Notation) – Zusammenfassung

Die O-Notation beschreibt das Wachstumsverhalten eines Algorithmus im Worst Case:

```
Geschwindigkeit:  O(1) > O(log n) > O(n) > O(n log n) > O(n²)
                  beste                                  schlechteste

Beispiel mit n = 1.000:
O(1)       = 1           (konstant)
O(log n)   = ~10         (logarithmisch)
O(n)       = 1.000       (linear)
O(n log n) = ~10.000     (linearithmisch)
O(n²)      = 1.000.000   (quadratisch)
```

### Wann welchen Algorithmus verwenden?

| Situation | Empfohlener Algorithmus | Begruendung |
|-----------|----------------------|-------------|
| Unsortierte kleine Liste durchsuchen | Lineare Suche | Kein Sortieren noetig |
| Grosse sortierte Liste durchsuchen | Binaere Suche | O(log n) statt O(n) |
| Kleine Liste sortieren (<50 Elemente) | Insertion Sort | Einfach, schnell bei kleinen Listen |
| Fast sortierte Liste sortieren | Insertion Sort | Best Case: O(n) |
| Lernzweck / Pruefung | Bubble Sort | Am einfachsten zu verstehen |
| Grosse Datenmengen sortieren | Quicksort, Mergesort* | O(n log n) |

*nicht IHK-Pruefungsstoff, aber gut zu wissen

### Zusammenhang: Sortieren und Suchen

```
Unsortierte Liste         Sortierte Liste
[38, 12, 7, 45, 3]   →   [3, 7, 12, 38, 45]
       |                          |
  Lineare Suche            Binaere Suche
    O(n)                     O(log n)
```

→ Wenn mehrfach gesucht werden muss: Einmal sortieren, dann binaer suchen!

### Typische Pruefungsaspekte
- Ablaufverfolgung (Trace) eines Sortier- oder Suchalgorithmus durchfuehren
- Pseudocode eines Algorithmus ergaenzen oder schreiben
- O-Notation angeben und erklaeren
- Vergleich: Warum ist binaere Suche schneller als lineare Suche?
- Szenario: Welcher Algorithmus passt zu welchem Problem?
- Voraussetzung der binaeren Suche nennen (sortierte Liste!)

### Haeufige Fehler
- Binaere Suche auf unsortierter Liste anwenden → falsches Ergebnis
- Off-by-one bei der Berechnung von `mitte`: Muss ganzzahlig sein (abrunden)
- Bubble Sort: Innere Schleife laeuft zu weit → unnoetige Vergleiche mit bereits sortiertem Bereich
- O-Notation: O(n²) wird als "doppelt so langsam" missverstanden → es ist quadratisch (bei n=10: 100, bei n=100: 10.000)
- Verwechslung der Sortieralgorithmen: Bubble = Tausch Nachbarn, Selection = Minimum suchen, Insertion = Einfuegen

---

## Uebungen

**Aufgabe 1:** Fuehre eine lineare Suche auf der Liste `[17, 42, 8, 33, 5, 29]` durch. Gesucht wird der Wert `33`. Gib an, wie viele Vergleiche noetig sind.

**Aufgabe 2:** Fuehre eine binaere Suche auf der sortierten Liste `[2, 5, 8, 12, 17, 23, 38, 45]` durch. Gesucht wird der Wert `17`. Zeige jeden Schritt mit links, rechts, mitte und Vergleich.

**Aufgabe 3:** Sortiere die Liste `[7, 2, 5, 1]` mit Bubble Sort. Zeige jeden Durchlauf.

**Aufgabe 4:** Sortiere die Liste `[7, 2, 5, 1]` mit Selection Sort. Zeige jeden Durchlauf.

**Aufgabe 5:** Sortiere die Liste `[7, 2, 5, 1]` mit Insertion Sort. Zeige jeden Schritt.

**Aufgabe 6:** Fulle die folgende Tabelle aus:

| Algorithmus | Best Case | Worst Case | Voraussetzung |
|------------|-----------|------------|---------------|
| Lineare Suche | | | |
| Binaere Suche | | | |
| Bubble Sort | | | |
| Selection Sort | | | |
| Insertion Sort | | | |

**Aufgabe 7:** Ein Telefonbuch mit 500.000 Eintraegen ist alphabetisch sortiert. Wie viele Vergleiche benoetigt die binaere Suche maximal? Wie viele die lineare Suche?

**Aufgabe 8:** Warum kann die binaere Suche nicht auf eine unsortierte Liste angewendet werden? Erklaere anhand eines Beispiels.

---
---

# Loesungen

## Aufgabe 1
Liste: `[17, 42, 8, 33, 5, 29]`, gesucht: `33`

| Schritt | i | liste[i] | Vergleich | Ergebnis |
|---------|---|----------|-----------|----------|
| 1 | 0 | 17 | 17 == 33? | Nein |
| 2 | 1 | 42 | 42 == 33? | Nein |
| 3 | 2 | 8 | 8 == 33? | Nein |
| 4 | 3 | 33 | 33 == 33? | Ja → Index 3 |

→ **4 Vergleiche** noetig.

## Aufgabe 2
Liste: `[2, 5, 8, 12, 17, 23, 38, 45]`, gesucht: `17`

| Schritt | links | rechts | mitte | liste[mitte] | Vergleich | Aktion |
|---------|-------|--------|-------|-------------|-----------|--------|
| 1 | 0 | 7 | 3 | 12 | 12 < 17 | links = 4 |
| 2 | 4 | 7 | 5 | 23 | 23 > 17 | rechts = 4 |
| 3 | 4 | 4 | 4 | 17 | 17 == 17 | **Gefunden! Index 4** |

→ 3 Vergleiche (statt 5 bei linearer Suche).

## Aufgabe 3
Liste: `[7, 2, 5, 1]`

```
Durchlauf 1: [7,2,5,1] → [2,7,5,1] → [2,5,7,1] → [2,5,1,7]
Durchlauf 2: [2,5,1,7] → [2,5,1,7] → [2,1,5,7]
Durchlauf 3: [2,1,5,7] → [1,2,5,7]
→ Fertig: [1,2,5,7]
```

## Aufgabe 4
Liste: `[7, 2, 5, 1]`

```
Durchlauf 1: Minimum in [7,2,5,1] = 1 (Index 3) → Tausche [0] und [3] → [1,2,5,7]
Durchlauf 2: Minimum in [2,5,7] = 2 (Index 1) → Kein Tausch → [1,2,5,7]
Durchlauf 3: Minimum in [5,7] = 5 (Index 2) → Kein Tausch → [1,2,5,7]
→ Fertig: [1,2,5,7]
```

## Aufgabe 5
Liste: `[7, 2, 5, 1]`

```
Schritt 1: Schluessel = 2, sortiert [7]
           2 < 7 → 7 nach rechts → [2,7,5,1]

Schritt 2: Schluessel = 5, sortiert [2,7]
           5 < 7 → 7 nach rechts
           5 > 2 → Stopp → [2,5,7,1]

Schritt 3: Schluessel = 1, sortiert [2,5,7]
           1 < 7 → 7 nach rechts
           1 < 5 → 5 nach rechts
           1 < 2 → 2 nach rechts
           → [1,2,5,7]

→ Fertig: [1,2,5,7]
```

## Aufgabe 6

| Algorithmus | Best Case | Worst Case | Voraussetzung |
|------------|-----------|------------|---------------|
| Lineare Suche | O(1) | O(n) | Keine |
| Binaere Suche | O(1) | O(log n) | Sortierte Liste |
| Bubble Sort | O(n)* | O(n²) | Keine |
| Selection Sort | O(n²) | O(n²) | Keine |
| Insertion Sort | O(n) | O(n²) | Keine |

*mit Optimierung (Abbruchflag)

## Aufgabe 7
- **Binaere Suche:** max. log₂(500.000) ≈ **19 Vergleiche**
- **Lineare Suche:** max. **500.000 Vergleiche**

Die binaere Suche ist hier ca. 26.000-mal effizienter!

## Aufgabe 8
Die binaere Suche vergleicht den gesuchten Wert mit dem **mittleren** Element und entscheidet dann, ob in der linken oder rechten Haelfte weitergesucht wird. Diese Entscheidung setzt voraus, dass alle Elemente links kleiner und alle rechts groesser sind – das ist nur bei einer **sortierten** Liste der Fall.

Beispiel: Liste `[8, 3, 12, 1, 7]`, gesucht: `3`
- mitte = Index 2, Wert 12
- 3 < 12 → "suche links" → [8, 3] → mitte = Index 0, Wert 8
- 3 < 8 → "suche links" → [] → **Nicht gefunden** (obwohl 3 in der Liste ist!)
