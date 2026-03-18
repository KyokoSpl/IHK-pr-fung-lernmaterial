# Grundlagen: 2.2.02 – Algorithmen formulieren und Programme entwickeln

## Kontrollstrukturen mittels Pseudocode / Aktivitaetsdiagramm

### Pseudocode – Grundelemente

| Struktur | Pseudocode | Beschreibung |
|---|---|---|
| Sequenz | Anweisung1; Anweisung2 | Hintereinander ausfuehren |
| Verzweigung | WENN ... DANN ... SONST | Bedingungsabhaengig |
| Schleife (kopfgesteuert) | SOLANGE ... TUE | Pruefung vor Durchlauf |
| Schleife (fussgesteuert) | TUE ... BIS | Mind. 1 Durchlauf |
| Zaehlschleife | FUER i = 1 BIS n TUE | Feste Anzahl Durchlaeufe |

**Beispiel: Rabattberechnung**
```
EINGABE: preis, kundentyp
WENN kundentyp == "Premium" DANN
    rabatt = preis * 0.15
SONST WENN kundentyp == "Standard" DANN
    rabatt = preis * 0.05
SONST
    rabatt = 0
ENDE WENN
endpreis = preis - rabatt
AUSGABE: endpreis
```

### Aktivitaetsdiagramm (UML)

Symbole:
- **Ausgefuellter Kreis:** Startknoten
- **Abgerundetes Rechteck:** Aktion/Aktivitaet
- **Raute:** Entscheidung (Verzweigung)
- **Balken:** Parallelisierung (Fork/Join)
- **Kreis mit Ring:** Endknoten

---

## Entwurf Bildschirmausgabemasken

### Softwareergonomie (DIN EN ISO 9241)

| Grundsatz | Beschreibung | Beispiel |
|---|---|---|
| Aufgabenangemessenheit | Nur notwendige Elemente | Kein ueberfluessiges Feld |
| Selbstbeschreibungsfaehigkeit | Bedienung ohne Handbuch | Tooltips, Platzhaltertext |
| Steuerbarkeit | Nutzer bestimmt Ablauf | Abbrechen-Button, Navigation |
| Erwartungskonformitaet | Verhalten wie erwartet | Speichern = Disketten-Icon |
| Fehlertoleranz | Fehler abfangen | Validierung, Undo-Funktion |
| Individualisierbarkeit | Anpassbar an Nutzer | Schriftgroesse, Farbschema |
| Lernfoerderlichkeit | Einfacher Einstieg | Tutorial, kontextsensitive Hilfe |

### Barrierefreiheit (WCAG / BITV)

| Prinzip | Massnahme |
|---|---|
| Wahrnehmbar | Alternativtexte fuer Bilder, ausreichender Kontrast |
| Bedienbar | Tastaturnavigation, keine Zeitlimits |
| Verstaendlich | Klare Sprache, konsistente Navigation |
| Robust | Kompatibel mit Screenreadern |

---

## UML-Diagramme

### Use-Case-Diagramm (Anwendungsfalldiagramm)

```
+---------------------------+
|        System             |
|  +-------------------+    |
|  | Login             |    |    Akteur
|  +-------------------+    |   +------+
|  | Passwort aendern  |----+---|Nutzer|
|  +-------------------+    |   +------+
|  | Bericht erstellen |    |
|  +-------------------+    |   +-------+
|  | Nutzer verwalten  |----+---|Admin  |
|  +-------------------+    |   +-------+
+---------------------------+
```

### Klassendiagramm

```
+----------------------------+
|        Fahrzeug            |
+----------------------------+
| - marke: String            |
| - baujahr: int             |
| # kilometerstand: double   |
+----------------------------+
| + getMarke(): String       |
| + fahren(km: double): void |
+----------------------------+
         ^
         | (Vererbung)
+----------------------------+
|        PKW                 |
+----------------------------+
| - sitzplaetze: int         |
+----------------------------+
| + getSitzplaetze(): int    |
+----------------------------+
```

**Sichtbarkeit:** + public, - private, # protected

### Aktivitaetsdiagramm

```
    (●)  Start
     |
[Eingabe lesen]
     |
    <◇>  Eingabe gueltig?
   / \
  ja  nein
  |     |
[Verarbeiten]  [Fehlermeldung]
  |              |
  +------+-------+
         |
    (◉)  Ende
```
