# 3.3.02 – Vertiefung: Planen mit geeigneten Modellen

## Diagramm-Auswahl: Wann verwende ich welches Diagramm?

| Fragestellung | Geeignetes Diagramm |
|--------------|-------------------|
| Welche Daten muessen gespeichert werden? | ERM, Relationales Modell |
| Wie sieht die Oberflaeche aus? | Mockup / Wireframe |
| Wer nutzt das System und wofuer? | Anwendungsfalldiagramm |
| Wie ist der Code/die Architektur strukturiert? | Klassendiagramm |
| Wie laeuft ein Prozess ab? | Aktivitaetsdiagramm |
| Wie kommunizieren Objekte miteinander? | Sequenzdiagramm |
| Welche Zustaende durchlaeuft ein Objekt? | Zustandsdiagramm |

---

## Vergleich: Strukturdiagramme vs. Verhaltensdiagramme

```
UML-Diagramme
├── Strukturdiagramme (statisch)
│   ├── Klassendiagramm         ← pruefungsrelevant
│   ├── Objektdiagramm
│   ├── Paketdiagramm
│   └── Komponentendiagramm
│
└── Verhaltensdiagramme (dynamisch)
    ├── Anwendungsfalldiagramm  ← pruefungsrelevant
    ├── Aktivitaetsdiagramm     ← pruefungsrelevant
    ├── Zustandsdiagramm        ← pruefungsrelevant (FI AE)
    └── Interaktionsdiagramme
        ├── Sequenzdiagramm     ← pruefungsrelevant
        └── Kommunikationsdiagramm
```

---

## Vertiefung ERM → Relationales Modell

### Transformationsregeln im Detail

**Regel 1: 1:n-Beziehung**
```
ERM:  Abteilung ──1:n── Mitarbeiter

Relational:
  Abteilung (AbtNr PK, Name, Standort)
  Mitarbeiter (MitNr PK, Name, Gehalt, AbtNr FK→Abteilung)
                                        ↑
                              FK auf der n-Seite!
```

**Regel 2: n:m-Beziehung**
```
ERM:  Schueler ──n:m── Kurs
      mit Attribut "Note" an der Beziehung

Relational:
  Schueler (SchuelerNr PK, Name, Klasse)
  Kurs (KursNr PK, Bezeichnung, Lehrer)
  Belegung (SchuelerNr FK, KursNr FK, Note)
            PK = (SchuelerNr, KursNr)
```

**Regel 3: 1:1-Beziehung**
```
ERM:  Person ──1:1── Personalausweis

Relational (Option A - FK in einer Tabelle):
  Person (PersonNr PK, Name, Geburtsdatum)
  Personalausweis (AusweisNr PK, Ablaufdatum, PersonNr FK UNIQUE)
```

---

## Vertiefung Klassendiagramm: Beziehungen

### Aggregation vs. Komposition

| Merkmal | Aggregation (◇) | Komposition (◆) |
|---------|-----------------|-----------------|
| Staerke | Schwach ("hat-ein") | Stark ("besteht-aus") |
| Teil ohne Ganzes | Kann existieren | Kann NICHT existieren |
| Beispiel | Team ◇── Mitarbeiter | Haus ◆── Raum |
| Loeschverhalten | Teil bleibt bestehen | Teil wird mitgeloescht |
| Lebenszyklus | Unabhaengig | Abhaengig vom Ganzen |

### Vererbung: Regeln

```
         +-------------+
         |    Tier      |    Oberklasse / Basisklasse
         +-------------+
         | - name       |
         | - alter      |
         +-------------+
         | + fressen()  |
         | + schlafen() |
         +-------------+
              △  △
             /    \
+----------+      +----------+
|   Hund   |      |  Katze   |    Unterklassen / abgeleitete Klassen
+----------+      +----------+
| - rasse  |      | - indoor |
+----------+      +----------+
| + bellen()|     | + miauen()|
+----------+      +----------+

Hund und Katze ERBEN name, alter, fressen(), schlafen() von Tier.
Sie ERGAENZEN eigene Attribute und Methoden.
```

---

## Vertiefung Aktivitaetsdiagramm: Schwimmbahnen (Swimlanes)

Schwimmbahnen zeigen, WER eine Aktivitaet ausfuehrt:

```
    | Kunde          | System           | Lager            |
    |                |                  |                  |
    | ●              |                  |                  |
    | |              |                  |                  |
    | [Artikel       |                  |                  |
    |  auswaehlen]   |                  |                  |
    | |              |                  |                  |
    | [Bestellen]--->|[Bestellung       |                  |
    |                | pruefen]         |                  |
    |                | |                |                  |
    |                | ◇                |                  |
    |                | / \              |                  |
    |                |ja  nein          |                  |
    |                |/     \           |                  |
    |                |[Bestae-][Fehler- |                  |
    |                | tigung] meldung] |                  |
    |                |  |               |                  |
    |                |  |-------------->|[Ware             |
    |                |                  | kommissionieren] |
    |                |                  | |                |
    |                |                  | [Versand]        |
    |                |                  | |                |
    |                |                  | ◉                |
```

---

## Pruefungsaspekte

### Typische Fragestellungen

1. **Diagramm erstellen**: "Zeichnen Sie ein Klassendiagramm fuer folgendes Szenario..."
2. **Diagramm lesen**: "Welche Aussagen lassen sich aus dem Diagramm ableiten?"
3. **ERM transformieren**: "Ueberführen Sie das ERM in ein relationales Modell"
4. **Diagramm korrigieren**: "Finden Sie die Fehler im folgenden Sequenzdiagramm"
5. **Diagramm-Auswahl**: "Welches UML-Diagramm eignet sich fuer...?"

### Haeufige Fehler in der Pruefung

| Fehler | Korrektur |
|--------|-----------|
| Aggregation und Komposition verwechseln | Komposition = Teil kann nicht ohne Ganzes existieren |
| Kardinalitaeten im ERM vergessen | Immer angeben: 1:1, 1:n, n:m |
| <<include>> und <<extend>> verwechseln | include = zwingend enthalten, extend = optional |
| Fremdschluessel auf falsche Seite bei 1:n | FK kommt auf die n-Seite |
| Sichtbarkeit im Klassendiagramm vergessen | + public, - private, # protected |
| Zustandsdiagramm mit Aktivitaetsdiagramm verwechseln | Zustand = Objektzustand, Aktivitaet = Prozessablauf |
| Rueckgabepfeile im Sequenzdiagramm vergessen | Gestrichelte Pfeile fuer Antworten |
| n:m-Beziehung nicht aufloesen | IMMER Zwischentabelle bei n:m |

---

## Normalformen (Kurzuebersicht fuer ERM-Transformation)

| Normalform | Regel | Beispiel-Verletzung |
|------------|-------|-------------------|
| 1NF | Jedes Attribut ist atomar (keine Wiederholungsgruppen) | "Telefon: 0123, 0456" in einer Zelle |
| 2NF | 1NF + Jedes Nicht-Schluessel-Attribut voll vom PK abhaengig | Bei zusammengesetztem PK: Attribut haengt nur von Teil-PK ab |
| 3NF | 2NF + Keine transitiven Abhaengigkeiten | PLZ → Ort (Ort haengt von PLZ ab, nicht vom PK) |
