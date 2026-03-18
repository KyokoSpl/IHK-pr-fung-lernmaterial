# Grundlagen: 1.4.07 – Programmierwerkzeuge

## Pseudocode

**Definition:** Allgemein verstaendliche, sprachunabhaengige Darstellung eines Algorithmus. Dient als Planungswerkzeug vor der eigentlichen Programmierung.

**Regeln:**
- Keine spezifische Syntax einer Programmiersprache
- Kontrollstrukturen muessen klar erkennbar sein
- Einrueckung zeigt Blockzugehoerigkeit
- Standardbegriffe: WENN/DANN/SONST, FUER, SOLANGE, EINGABE, AUSGABE, RUECKGABE

**Beispiel – Rabattberechnung:**
```
FUNKTION berechneRabatt(preis: Double, rabattProzent: Double): Double
    WENN rabattProzent < 0 ODER rabattProzent > 100 DANN
        AUSGABE "Ungueltiger Rabatt"
        RUECKGABE preis
    ENDE WENN
    rabattBetrag = preis * rabattProzent / 100
    RUECKGABE preis - rabattBetrag
ENDE FUNKTION
```

---

## Entwurf der Bildschirmausgabemasken

**Definition:** Gestaltung von Benutzeroberflaechen (GUI) vor der Implementierung.

**Softwareergonomie:**
- Konsistentes Layout (gleiche Position fuer gleiche Elemente)
- Klare Beschriftungen und Fehlermeldungen
- Tab-Reihenfolge logisch
- Wichtige Aktionen hervorgehoben (z.B. „Speichern"-Button prominent)
- DIN EN ISO 9241: Dialoggestaltung (Aufgabenangemessenheit, Selbstbeschreibungsfaehigkeit, Steuerbarkeit, Erwartungskonformitaet, Fehlertoleranz, Individualisierbarkeit, Lernfoerderlichkeit)

**Corporate Identity (CI):**
- Firmenfarben und -schriften verwenden
- Logo an definierter Position
- Einheitliches Design ueber alle Anwendungen

**Barrierefreiheit:**
- Kontrastreiche Farben
- Schriftgroesse anpassbar
- Alt-Texte fuer Bilder
- Tastaturnavigation moeglich

---

## Fehler in Quellcode finden

**Definition:** Analyse eines gegebenen Code-Fragments zur Identifikation von Fehlern.

**Vorgehensweise:**
1. Syntaxpruefung: Klammern, Semikolons, Schluesselwoerter korrekt?
2. Variablen: Deklariert? Initialisiert? Richtig verwendet?
3. Kontrollstrukturen: Bedingungen logisch korrekt? Schleifen terminieren?
4. Datentypen: Kompatibel? Korrekte Konvertierung?
5. Grenzwerte: Was passiert bei 0, -1, Maximum?

---

## Schreibtischtest

**Definition:** Manuelle Simulation der Code-Ausfuehrung Zeile fuer Zeile mit einer Tabelle, die den Zustand aller Variablen nach jedem Schritt dokumentiert.

**Vorgehensweise:**
1. Alle Variablen als Spalten anlegen
2. Zeilenweise durch den Code gehen
3. Nach jeder Anweisung: Variablenwerte aktualisieren
4. Bei Verzweigungen: Bedingung auswerten und entsprechend fortfahren
5. Endergebnis pruefen

**Beispiel:**
```
x = 5
y = 3
z = x + y
x = z * 2
```

| Schritt | x | y | z |
|---|---|---|---|
| 1 | 5 | – | – |
| 2 | 5 | 3 | – |
| 3 | 5 | 3 | 8 |
| 4 | 16 | 3 | 8 |

---

## UML-Diagramme

### Use-Case-Diagramm (Anwendungsfalldiagramm)
- Zeigt Akteure und deren Interaktionen mit dem System
- Elemente: Akteur (Strichmaennchen), Use Case (Ellipse), Systemgrenze (Rechteck)
- Beziehungen: include (immer enthalten), extend (optional)
- Zweck: Anforderungsanalyse – Was macht das System fuer wen?

### Klassendiagramm
- Zeigt Klassen mit Attributen und Methoden
- Notation: Klassenname | Attribute | Methoden
- Sichtbarkeit: + public, - private, # protected
- Beziehungen: Assoziation, Aggregation (◇), Komposition (◆), Vererbung (△)
- Kardinalitaeten: 1, 0..1, 0..*, 1..*

### Aktivitaetsdiagramm
- Zeigt den Ablauf eines Prozesses oder Algorithmus
- Elemente: Startknoten (●), Endknoten (◉), Aktion (abgerundetes Rechteck), Entscheidung (◇), Zusammenfuehrung, Parallelisierung (schwarzer Balken)
- Zweck: Ablauflogik, Geschaeftsprozesse, Algorithmen

## Querverweise
- → 1.4.06 (Kontrollstrukturen, OOP als Basis)
- → 3.3.02 (UML-Diagramme im Detail, Sequenzdiagramm, Zustandsdiagramm)
- → 3.4.09 (UML-Diagramme erstellen koennen)
- → 3.4.14 (Benutzeroberflaeche, Usability, UX)
