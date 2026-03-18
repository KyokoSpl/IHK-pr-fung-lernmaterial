# Vertiefung: 3.4.09 – UML-Diagramme erstellen

## Wann welches Diagramm?

| Diagramm | Zeigt | Kategorie | Typische Fragestellung |
|----------|-------|----------|----------------------|
| Aktivitaetsdiagramm | Ablaeufe, Workflows | Verhaltensdiagramm | "Wie laeuft der Prozess ab?" |
| Anwendungsfalldiagramm | Funktionen und Akteure | Verhaltensdiagramm | "WAS kann das System? Wer nutzt es?" |
| Klassendiagramm | Statische Struktur | Strukturdiagramm | "Welche Klassen gibt es und wie haengen sie zusammen?" |
| Sequenzdiagramm | Zeitlicher Nachrichtenaustausch | Verhaltensdiagramm | "In welcher Reihenfolge kommunizieren die Objekte?" |
| Zustandsdiagramm | Zustaende und Uebergaenge | Verhaltensdiagramm | "Welche Zustaende hat ein Objekt?" |

## Diagrammtypen mit ASCII-Beispielen

### Aktivitaetsdiagramm – Bestellprozess

```
          (●) Start
           |
  +--------v--------+
  | Artikel in       |
  | Warenkorb legen  |
  +---------+--------+
            |
  +---------v--------+
  | Zur Kasse gehen  |
  +---------+--------+
            |
         <◇>─────────────────────+
        /   \                     |
   [Kunde]  [Gast]               |
      |        |                  |
  +---v---+ +--v-----------+     |
  | Login | | Gastbestellung|     |
  +---+---+ +--+-----------+     |
      |        |                  |
      +---+----+                  |
          |                       |
  +-------v--------+             |
  | Zahlung         |             |
  | durchfuehren    |             |
  +-------+--------+             |
          |                       |
       <◇>                       |
      /    \                      |
  [ok]    [fehler]                |
    |        |                    |
  +-v------+ +--v---------+      |
  |Bestae- | |Fehlermel-  |      |
  |tigung  | |dung zeigen |------+
  +---+----+ +------------+
      |
     (◉) Ende
```

### Anwendungsfalldiagramm – Online-Shop

```
+------------------------------------------+
|            Online-Shop (System)          |
|                                          |
|   (Artikel suchen)                       |
|        /                                 |
|  (Bestellung aufgeben)                   |
|        |                                 |
|        |---<<include>>-->(Login pruefen) |
|        |                                 |
|        |---<<extend>>-->(Gutschein       |
|        |                 einloesen)      |
|   (Bewertung schreiben)                 |
|                                          |
+------------------------------------------+
     |             |
  Kunde        Administrator
  (Akteur)     (Akteur)
                   |
            (Artikel verwalten)
            (Bestellungen einsehen)
```

### Klassendiagramm – Bestellsystem

```
+------------------+          +-------------------+
|     Kunde        |          |    Bestellung     |
+------------------+  1    * +-------------------+
| - kundeId: int   |─────────| - bestellNr: int  |
| - name: String   |         | - datum: Date     |
| - email: String  |         | - status: String  |
+------------------+         +-------------------+
| + bestellen()    |         | + berechneGesamt()|
| + getAdresse()   |         | + stornieren()    |
+------------------+         +--------+----------+
                                      | *
                                      |
                              +-------v----------+
                              | BestellPosition   |
                              +-------------------+
                              | - menge: int      |
                              | - einzelpreis:    |
                              |   double          |
                              +-------------------+
                              | + getGesamt()     |
                              +--------+----------+
                                       | *
                                       |
                              +--------v----------+
                              |     Artikel       |
                              +-------------------+
                              | - artikelNr: int  |
                              | - bezeichnung:    |
                              |   String          |
                              | - preis: double   |
                              +-------------------+
                              | + getDetails()    |
                              +-------------------+
```

### Sequenzdiagramm – Login-Vorgang

```
  Benutzer          LoginController       Datenbank        Session
     |                    |                  |                |
     |  1: login(user,pw) |                  |                |
     |------------------->|                  |                |
     |                    | 2: pruefeUser    |                |
     |                    |  (user, pw)      |                |
     |                    |----------------->|                |
     |                    |                  |                |
     |                    | 3: Ergebnis      |                |
     |                    |<-----------------|                |
     |                    |                  |                |
     |              +-----+------+           |                |
     |              | alt        |           |                |
     |              | [gueltig]  |           |                |
     |              |     | 4: erzeugeSession|                |
     |              |     |------------------------------>    |
     |              |     |              5: SessionID         |
     |              |     |<------------------------------|   |
     |  6: Erfolg   |     |              |                |   |
     |<-------------|     |              |                |   |
     |              |------------|       |                |   |
     |              | [ungueltig]|       |                |   |
     |  7: Fehler   |     |              |                |   |
     |<-------------|     |              |                |   |
     |              +-----+------+       |                |   |
```

### Zustandsdiagramm – Bestellung

```
   (●)
    |
    v
+----------+   bestellen()    +-----------+
|  Neu     |----------------->| Bestaetigt|
+----------+                  +-----------+
                                   |
                    zahlung_ok()   |
                                   v
                             +----------+
            stornieren()     | Bezahlt  |
  +----------<---------------|          |
  |                          +----------+
  v                                |
+----------+          versenden()  |
|Storniert |                       v
+----------+              +-----------+
  |                       | Versendet |
  v                       +-----------+
 (◉)                           |
                  zugestellt() |
                               v
                        +-----------+
                        | Geliefert |
                        +-----------+
                               |
                               v
                              (◉)
```

---

## Beziehungen im Klassendiagramm – Vertiefung

### Aggregation vs. Komposition

| Aspekt | Aggregation (◇) | Komposition (◆) |
|--------|-----------------|-----------------|
| Beziehung | "Hat-ein" (schwach) | "Besteht-aus" (stark) |
| Existenzabhaengigkeit | Teil kann ohne Ganzes existieren | Teil existiert nicht ohne Ganzes |
| Beispiel | Abteilung ◇── Mitarbeiter | Haus ◆── Raum |
| Beim Loeschen des Ganzen | Teile bleiben bestehen | Teile werden mitgeloescht |

### Include vs. Extend im Use-Case-Diagramm

| Aspekt | <<include>> | <<extend>> |
|--------|-----------|----------|
| Richtung | Basis → eingebundener UC | Erweiterung → Basis-UC |
| Ausfuehrung | Immer (obligatorisch) | Optional (unter Bedingung) |
| Beispiel | "Bestellen" includes "Login" | "Bestellen" extended by "Gutschein" |
| Pfeilrichtung | Vom Basis-UC zum eingebundenen UC | Vom Erweiterungs-UC zum Basis-UC |

---

## Typische Pruefungsaspekte
- Aus einem Anforderungstext ein Klassendiagramm mit Attributen, Methoden und Beziehungen ableiten
- Zustandsdiagramm fuer ein Objekt (z.B. Bestellung) mit allen Zustaenden und Transitionen zeichnen
- Aktivitaetsdiagramm fuer einen Geschaeftsprozess erstellen
- Use-Case-Diagramm: Akteure und Anwendungsfaelle identifizieren, include/extend korrekt verwenden
- Sequenzdiagramm: Methodenaufrufe in zeitlicher Reihenfolge darstellen

## Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| Aggregation und Komposition verwechselt | Komposition = starke Abhaengigkeit (Teil stirbt mit Ganzem) |
| Include und Extend vertauscht | Include = obligatorisch, Extend = optional |
| Klassendiagramm ohne Sichtbarkeiten | Immer +, -, # angeben |
| Sequenzdiagramm ohne Rueckgabepfeile | Synchrone Aufrufe brauchen eine Antwort (gestrichelter Pfeil) |
| Zustandsdiagramm ohne Start-/Endzustand | Start (●) und Ende (◉) gehoeren immer dazu |
| Aktivitaeten im Use-Case-Diagramm | Use Cases beschreiben FUNKTIONEN, keine Ablaufschritte |
