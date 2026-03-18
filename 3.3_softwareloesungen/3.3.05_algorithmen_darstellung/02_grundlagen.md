# 3.3.05 – Grundlagen: Algorithmen in einer Programmiersprache darstellen

## TK 1: Allgemein verstaendlicher Pseudocode

### Definition
**Pseudocode** ist eine informelle, an natuerliche und Programmiersprache angelehnte Darstellung eines Algorithmus. Er ist nicht an eine bestimmte Programmiersprache gebunden.

### Pseudocode-Konventionen

| Element | Pseudocode | Erklaerung |
|---------|-----------|-----------|
| Zuweisung | `x = 5` oder `x ← 5` | Variable bekommt Wert |
| Eingabe | `EINGABE(x)` oder `LIES x` | Benutzereingabe |
| Ausgabe | `AUSGABE(x)` oder `SCHREIBE x` | Bildschirmausgabe |
| Kommentar | `// Kommentar` | Erklaerung |
| Methodenaufruf | `ergebnis = berechne(x, y)` | Funktion aufrufen |

### Schluesselwoerter (haeufig verwendet)

```
WENN ... DANN ... SONST ... ENDE-WENN
SOLANGE ... TUE ... ENDE-SOLANGE
FUER ... VON ... BIS ... TUE ... ENDE-FUER
WIEDERHOLE ... BIS ...
FUNKTION ... RUECKGABE ...
```

---

## TK 2: Code muss nicht 1:1 kompilierbar sein

### Was bedeutet das fuer die Pruefung?

| Akzeptabel | Nicht akzeptabel |
|------------|-----------------|
| `WENN alter >= 18 DANN` | Nur Prosa: "Wenn man alt genug ist..." |
| `liste.sortiere()` | Unklare Notation ohne Struktur |
| `summe = summe + wert` | Fehlende Logik/Algorithmus |
| Einrueckung zeigt Bloecke | Alles auf einer Ebene ohne Struktur |

**Merke**: Der Pruefer muss den Algorithmus **nachvollziehen** koennen. Die exakte Syntax (Semikolons, Klammern etc.) ist dabei zweitrangig.

---

## TK 3: Kontrollstrukturen

### Die drei Grundstrukturen der Programmierung

```
1. SEQUENZ          2. SELEKTION          3. ITERATION
   (Nacheinander)     (Verzweigung)         (Schleife)

   Anweisung 1        WENN Bedingung        SOLANGE Bedingung
   Anweisung 2          Anweisung A           Anweisung
   Anweisung 3        SONST                 ENDE
                         Anweisung B
                       ENDE
```

### Selektion (Verzweigung)

**Einfache Verzweigung (if)**:
```
WENN temperatur > 30 DANN
    AUSGABE("Es ist heiss")
ENDE-WENN
```

**Zweiseitige Verzweigung (if-else)**:
```
WENN alter >= 18 DANN
    AUSGABE("Volljaehrig")
SONST
    AUSGABE("Minderjaehrig")
ENDE-WENN
```

**Mehrseitige Verzweigung (if-else if / switch)**:
```
WENN note == 1 DANN
    AUSGABE("Sehr gut")
SONST WENN note == 2 DANN
    AUSGABE("Gut")
SONST WENN note == 3 DANN
    AUSGABE("Befriedigend")
SONST
    AUSGABE("Nicht bestanden")
ENDE-WENN
```

### Iteration (Schleifen)

**Kopfgesteuerte Schleife (while)** – Bedingung wird VOR dem Schleifenkoerper geprueft:
```
zaehler = 0
SOLANGE zaehler < 10 TUE
    AUSGABE(zaehler)
    zaehler = zaehler + 1
ENDE-SOLANGE
```

**Fussgesteuerte Schleife (do-while)** – Koerper wird mindestens EINMAL ausgefuehrt:
```
WIEDERHOLE
    EINGABE(passwort)
BIS passwort == "geheim"
```

**Zaehlschleife (for)**:
```
FUER i VON 1 BIS 10 TUE
    AUSGABE(i)
ENDE-FUER
```

**For-Each-Schleife**:
```
FUER JEDES element IN liste TUE
    AUSGABE(element)
ENDE-FUER
```

---

## Wichtige Standard-Algorithmen

### Lineare Suche

```
FUNKTION lineareSuche(liste, suchWert)
    FUER i VON 0 BIS laenge(liste) - 1 TUE
        WENN liste[i] == suchWert DANN
            RUECKGABE i    // Index gefunden
        ENDE-WENN
    ENDE-FUER
    RUECKGABE -1           // Nicht gefunden
ENDE-FUNKTION
```

**Komplexitaet**: O(n) – im schlimmsten Fall muss jedes Element geprueft werden.

### Binaere Suche (nur bei sortierter Liste!)

```
FUNKTION binaereSuche(liste, suchWert)
    links = 0
    rechts = laenge(liste) - 1

    SOLANGE links <= rechts TUE
        mitte = (links + rechts) / 2    // Ganzzahldivision

        WENN liste[mitte] == suchWert DANN
            RUECKGABE mitte
        SONST WENN liste[mitte] < suchWert DANN
            links = mitte + 1
        SONST
            rechts = mitte - 1
        ENDE-WENN
    ENDE-SOLANGE

    RUECKGABE -1
ENDE-FUNKTION
```

**Komplexitaet**: O(log n) – Halbierung des Suchbereichs bei jedem Schritt.

### Bubble Sort

```
FUNKTION bubbleSort(liste)
    n = laenge(liste)
    FUER i VON 0 BIS n - 2 TUE
        FUER j VON 0 BIS n - 2 - i TUE
            WENN liste[j] > liste[j + 1] DANN
                // Tausch
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp
            ENDE-WENN
        ENDE-FUER
    ENDE-FUER
    RUECKGABE liste
ENDE-FUNKTION
```

**Komplexitaet**: O(n²) – zwei verschachtelte Schleifen.

### Maximum finden

```
FUNKTION findeMaximum(liste)
    max = liste[0]
    FUER i VON 1 BIS laenge(liste) - 1 TUE
        WENN liste[i] > max DANN
            max = liste[i]
        ENDE-WENN
    ENDE-FUER
    RUECKGABE max
ENDE-FUNKTION
```

---

## Code-Trace (Schrittweises Durchrechnen)

### Methode
Bei einem Code-Trace fuehrt man den Algorithmus **Schritt fuer Schritt von Hand** aus und notiert die Variablenwerte nach jeder Anweisung.

### Beispiel: Was gibt folgender Code aus?

```
x = 5
y = 3
SOLANGE x > 0 TUE
    x = x - y
    y = y - 1
    AUSGABE(x, y)
ENDE-SOLANGE
```

### Trace-Tabelle

| Schritt | x | y | x > 0? | Ausgabe |
|---------|---|---|--------|---------|
| Start | 5 | 3 | ja | |
| 1 | 5-3=2 | 3-1=2 | ja | 2, 2 |
| 2 | 2-2=0 | 2-1=1 | nein | 0, 1 |

**Ausgabe**: `2, 2` dann `0, 1`

**Hinweis**: Bei Schritt 2 gilt nach `x = x - y`: x = 0. Da `0 > 0` falsch ist, wird die Schleife beendet – ABER die Ausgabe in Schritt 2 erfolgt noch, da sie VOR der Bedingungspruefung am Schleifenanfang steht. Korrektur: Die Ausgabe `0, 1` erfolgt, danach wird `0 > 0` geprueft → Schleife endet.
