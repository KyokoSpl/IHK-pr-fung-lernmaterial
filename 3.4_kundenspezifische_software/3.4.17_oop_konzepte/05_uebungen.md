# Uebungen: 3.4.17 – OOP-Methodenkonzepte anwenden

## Kapselung

**Aufgabe 1:** Erklaere, warum Attribute in der OOP als `private` deklariert werden sollten. Nenne zwei Vorteile gegenueber `public`.

**Aufgabe 2:** Gegeben ist folgende Klasse. Ergaenze einen Setter fuer das Attribut `alter`, der sicherstellt, dass das Alter zwischen 0 und 150 liegt.

```
KLASSE Person
    PRIVAT name: String
    PRIVAT alter: Zahl

    OEFFENTLICH METHODE getAlter(): Zahl
        RUECKGABE alter
    ENDE METHODE

    // Hier Setter ergaenzen
ENDE KLASSE
```

---

## Vererbung

**Aufgabe 3:** Erstelle eine Klassenhierarchie in Pseudocode fuer eine Bibliothek:
- Elternklasse `Medium` mit Attributen `titel` (String) und `jahr` (Zahl) und Methode `info(): String`
- Kindklasse `Buch` mit zusaetzlichem Attribut `autor` (String) und ueberschriebener Methode `info()`
- Kindklasse `DVD` mit zusaetzlichem Attribut `laufzeit` (Zahl, in Minuten) und ueberschriebener Methode `info()`

**Aufgabe 4:** Erklaere den Unterschied zwischen einer "ist-ein"-Beziehung und einer "hat-ein"-Beziehung. Gib je ein Beispiel.

---

## Polymorphie

**Aufgabe 5:** Was ist der Unterschied zwischen Overloading und Overriding? Fuelle die Tabelle aus:

| Kriterium | Overloading | Overriding |
|-----------|------------|------------|
| Wo definiert? | | |
| Was aendert sich? | | |
| Bindungszeitpunkt | | |

**Aufgabe 6:** Gegeben ist folgender Code. Was wird ausgegeben?

```
KLASSE Form
    METHODE flaeche(): Zahl
        RUECKGABE 0
    ENDE METHODE
ENDE KLASSE

KLASSE Kreis ERBT VON Form
    ATTRIBUT radius: Zahl = 5
    METHODE flaeche(): Zahl
        RUECKGABE 3.14 * radius * radius
    ENDE METHODE
ENDE KLASSE

KLASSE Rechteck ERBT VON Form
    ATTRIBUT breite: Zahl = 4
    ATTRIBUT hoehe: Zahl = 6
    METHODE flaeche(): Zahl
        RUECKGABE breite * hoehe
    ENDE METHODE
ENDE KLASSE

formen: Liste von Form = [neuer Kreis(), neues Rechteck()]
FUER JEDES f IN formen
    ausgabe(f.flaeche())
ENDE FUER
```

---

## Interfaces

**Aufgabe 7:** Erklaere den Unterschied zwischen einem Interface und einer abstrakten Klasse. Nenne je ein Einsatzbeispiel.

**Aufgabe 8:** Schreibe ein Interface `Suchbar` mit einer Methode `suche(suchbegriff: String): Liste`. Implementiere das Interface in einer Klasse `ProduktKatalog`.

---

## Fehlerbehandlung

**Aufgabe 9:** Erklaere den Ablauf von try-catch-finally. Was passiert in jedem Block?

**Aufgabe 10:** Der folgende Pseudocode enthaelt einen typischen Fehler in der Fehlerbehandlung. Finde und korrigiere ihn.

```
METHODE liesDatei(pfad: String): String
    VERSUCHE
        datei = oeffne(pfad)
        inhalt = datei.lese()
        datei.schliesse()
        RUECKGABE inhalt
    FANGE FehlerTyp DateiNichtGefunden
        // Nichts tun
    ENDE VERSUCHE
ENDE METHODE
```

---

## Gesamtaufgaben

**Aufgabe 11:** Zeichne ein UML-Klassendiagramm (ASCII) fuer folgendes Szenario:
- Interface `Bezahlbar` mit Methode `bezahle(betrag: Zahl)`
- Abstrakte Klasse `Transaktion` mit Attributen `datum` und `betrag`
- Klasse `KartenZahlung` erbt von `Transaktion` und implementiert `Bezahlbar`
- Klasse `BarZahlung` erbt von `Transaktion` und implementiert `Bezahlbar`

**Aufgabe 12:** Ein Personalverwaltungssystem verwaltet Festangestellte und Freiberufler.
- Erstelle eine Elternklasse `Mitarbeiter` mit Attributen `name` und `stundensatz`
- Kindklasse `Festangestellter` berechnet das Gehalt als `stundensatz * 160` (Monatsstunden)
- Kindklasse `Freiberufler` berechnet das Gehalt als `stundensatz * gearbeitetStunden`
- Verwende polymorphe Methode `berechneGehalt()`
- Fuege Fehlerbehandlung fuer negativen Stundensatz hinzu

---
---

# Loesungen

## Aufgabe 1
Private Attribute schuetzen die Daten vor unkontrolliertem Zugriff von aussen.
- **Vorteil 1:** Validierung moeglich – der Setter kann pruefen, ob ein Wert gueltig ist (z.B. Alter >= 0).
- **Vorteil 2:** Interne Darstellung aenderbar – man kann die interne Speicherung aendern, ohne den externen Code anzupassen.

## Aufgabe 2

```
OEFFENTLICH METHODE setAlter(wert: Zahl)
    WENN wert >= 0 UND wert <= 150 DANN
        alter = wert
    SONST
        ausgabe("Ungueltiges Alter!")
    ENDE WENN
ENDE METHODE
```

## Aufgabe 3

```
KLASSE Medium
    GESCHUETZT titel: String
    GESCHUETZT jahr: Zahl

    METHODE info(): String
        RUECKGABE titel + " (" + jahr + ")"
    ENDE METHODE
ENDE KLASSE

KLASSE Buch ERBT VON Medium
    PRIVAT autor: String

    METHODE info(): String
        RUECKGABE titel + " von " + autor + " (" + jahr + ")"
    ENDE METHODE
ENDE KLASSE

KLASSE DVD ERBT VON Medium
    PRIVAT laufzeit: Zahl

    METHODE info(): String
        RUECKGABE titel + " (" + jahr + "), " + laufzeit + " Min."
    ENDE METHODE
ENDE KLASSE
```

## Aufgabe 4
- **"Ist-ein"-Beziehung (Vererbung):** Ein PKW ist ein Fahrzeug. PKW erbt von Fahrzeug.
- **"Hat-ein"-Beziehung (Komposition):** Ein Auto hat einen Motor. Motor ist ein Attribut der Klasse Auto, keine Elternklasse.

## Aufgabe 5

| Kriterium | Overloading | Overriding |
|-----------|------------|------------|
| Wo definiert? | In derselben Klasse | In der Kindklasse |
| Was aendert sich? | Parameterliste (Anzahl/Typen) | Implementierung (Methodenkoerper) |
| Bindungszeitpunkt | Compile-Time (statisch) | Runtime (dynamisch) |

## Aufgabe 6
Ausgabe:
```
78.5
24
```
Erklaerung: `3.14 * 5 * 5 = 78.5` (Kreis) und `4 * 6 = 24` (Rechteck). Durch Polymorphie wird zur Laufzeit die Methode des tatsaechlichen Objekttyps aufgerufen.

## Aufgabe 7
- **Interface:** Definiert nur Methodensignaturen, keine Implementierung. Eine Klasse kann mehrere Interfaces implementieren. Beispiel: Interface `Druckbar` mit Methode `drucke()` – verschiedene Dokumenttypen implementieren es.
- **Abstrakte Klasse:** Kann Attribute und teilweise implementierte Methoden enthalten. Nur einfache Vererbung moeglich. Beispiel: Abstrakte Klasse `Tier` mit implementierter Methode `getName()` und abstrakter Methode `laut()`.

## Aufgabe 8

```
INTERFACE Suchbar
    METHODE suche(suchbegriff: String): Liste
ENDE INTERFACE

KLASSE ProduktKatalog IMPLEMENTIERT Suchbar
    PRIVAT produkte: Liste von Produkt

    METHODE suche(suchbegriff: String): Liste
        ergebnis = neue leere Liste
        FUER JEDES p IN produkte
            WENN p.name ENTHAELT suchbegriff DANN
                ergebnis.hinzufuegen(p)
            ENDE WENN
        ENDE FUER
        RUECKGABE ergebnis
    ENDE METHODE
ENDE KLASSE
```

## Aufgabe 9
1. **try:** Code wird ausgefuehrt. Wenn kein Fehler auftritt, wird catch uebersprungen.
2. **catch:** Wird NUR ausgefuehrt, wenn im try-Block ein Fehler auftritt. Faengt den Fehler ab und behandelt ihn.
3. **finally:** Wird IMMER ausgefuehrt – egal ob Fehler aufgetreten ist oder nicht. Typisch fuer Aufraeumaarbeiten (Datei schliessen, Verbindung trennen).

## Aufgabe 10
Fehler: Der catch-Block ist leer → der Fehler wird verschluckt. Die Methode gibt bei einem Fehler keinen Wert zurueck.

Korrektur:

```
METHODE liesDatei(pfad: String): String
    VERSUCHE
        datei = oeffne(pfad)
        inhalt = datei.lese()
        RUECKGABE inhalt
    FANGE FehlerTyp DateiNichtGefunden als fehler
        ausgabe("Datei nicht gefunden: " + pfad)
        RUECKGABE ""
    ABSCHLIESSEND
        WENN datei != NULL DANN
            datei.schliesse()
        ENDE WENN
    ENDE VERSUCHE
ENDE METHODE
```

## Aufgabe 11

```
+---------------------+       +-------------------------+
| <<interface>>       |       | <<abstract>>            |
| Bezahlbar           |       | Transaktion             |
|---------------------|       |-------------------------|
|                     |       | # datum: Datum          |
|---------------------|       | # betrag: Zahl          |
| + bezahle(betrag)   |       |-------------------------|
+---------------------+       +-------------------------+
        ^        ^                     ^          ^
        |        |                     |          |
   impl.|   impl.|                erbt |     erbt |
        |        |                     |          |
+-------+------+ +--------+---------+ |          |
| KartenZahlung|-|                   |-+          |
|--------------| | BarZahlung       |             |
| + bezahle()  | |------------------+-------------+
+--------------+ | + bezahle()     |
                 +-----------------+
```

## Aufgabe 12

```
KLASSE Mitarbeiter
    GESCHUETZT name: String
    GESCHUETZT stundensatz: Zahl

    KONSTRUKTOR Mitarbeiter(name: String, satz: Zahl)
        WENN satz < 0 DANN
            WIRF neuen Fehler("Stundensatz darf nicht negativ sein!")
        ENDE WENN
        DIESER.name = name
        DIESER.stundensatz = satz
    ENDE KONSTRUKTOR

    METHODE berechneGehalt(): Zahl
        RUECKGABE 0
    ENDE METHODE
ENDE KLASSE

KLASSE Festangestellter ERBT VON Mitarbeiter
    METHODE berechneGehalt(): Zahl
        RUECKGABE stundensatz * 160
    ENDE METHODE
ENDE KLASSE

KLASSE Freiberufler ERBT VON Mitarbeiter
    PRIVAT gearbeitetStunden: Zahl

    METHODE berechneGehalt(): Zahl
        RUECKGABE stundensatz * gearbeitetStunden
    ENDE METHODE
ENDE KLASSE

// Verwendung:
VERSUCHE
    fest = neuer Festangestellter("Anna", 25)
    frei = neuer Freiberufler("Ben", 50, 120)

    ausgabe(fest.name + ": " + fest.berechneGehalt())   // Anna: 4000
    ausgabe(frei.name + ": " + frei.berechneGehalt())   // Ben: 6000

    fehler = neuer Festangestellter("X", -10)           // Fehler!
FANGE FehlerTyp Exception als e
    ausgabe("Fehler: " + e.nachricht)
ENDE VERSUCHE
```
