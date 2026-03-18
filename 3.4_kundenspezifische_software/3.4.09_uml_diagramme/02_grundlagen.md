# Grundlagen: 3.4.09 – UML-Diagramme erstellen

## Aktivitaetsdiagramm

**Definition:** Ein Aktivitaetsdiagramm modelliert den Ablauf von Aktivitaeten (Aktionen) mit Kontrollfluss, Verzweigungen, Parallelisierungen und Synchronisierungen. Es ist ein Verhaltensdiagramm.

**Notationselemente:**

| Element | Symbol | Beschreibung |
|---------|--------|-------------|
| Startknoten | Gefuellter Kreis ● | Beginn des Ablaufs |
| Endknoten | Kreis mit Punkt ◉ | Ende des Ablaufs |
| Aktivitaet | Abgerundetes Rechteck | Eine Aktion/Taetigkeit |
| Entscheidung | Raute ◇ | Verzweigung mit Bedingung |
| Zusammenfuehrung | Raute ◇ | Zusammenfuehrung von Pfaden |
| Parallelisierung | Dicker Balken ═ (Fork) | Aufspaltung in parallele Pfade |
| Synchronisierung | Dicker Balken ═ (Join) | Zusammenfuehrung paralleler Pfade |
| Swimlane | Vertikale Spalte | Zuordnung von Aktivitaeten zu Akteuren |

**Kernaussagen:**
- Zeigt den Ablauf von Geschaeftsprozessen oder Algorithmen
- Entscheidungen werden mit Bedingungen in eckigen Klammern beschriftet: [ja] / [nein]
- Parallele Ablaeufe werden zwischen Fork und Join modelliert

---

## Anwendungsfalldiagramm (Use-Case-Diagramm)

**Definition:** Ein Anwendungsfalldiagramm zeigt die funktionalen Anforderungen eines Systems: Welche Akteure nutzen welche Funktionen (Use Cases)?

**Notationselemente:**

| Element | Symbol | Beschreibung |
|---------|--------|-------------|
| Akteur | Strichmaennchen | Person oder externes System, das mit dem System interagiert |
| Use Case | Ellipse | Eine Funktion/Anforderung des Systems |
| Systemgrenze | Rechteck | Grenze des betrachteten Systems |
| Assoziation | Linie ── | Akteur nutzt einen Use Case |
| Include | Gestrichelter Pfeil + <<include>> | Use Case wird immer eingebunden |
| Extend | Gestrichelter Pfeil + <<extend>> | Use Case wird optional eingebunden |
| Generalisierung | Pfeil mit Dreieck | Spezialisierung eines Akteurs oder Use Cases |

**Kernaussagen:**
- Zeigt WAS das System kann, nicht WIE es funktioniert
- Akteure stehen ausserhalb der Systemgrenze
- <<include>>: "Bestellung aufgeben" includes "Login pruefen" (wird immer ausgefuehrt)
- <<extend>>: "Bestellung aufgeben" extended by "Gutschein einloesen" (optional)

---

## Klassendiagramm

**Definition:** Ein Klassendiagramm zeigt die statische Struktur eines Systems: Klassen mit Attributen, Methoden, Sichtbarkeiten und Beziehungen.

**Notation einer Klasse:**

```
+---------------------------+
|       Klassenname         |
+---------------------------+
| - attribut1: Typ          |
| - attribut2: Typ          |
+---------------------------+
| + methode1(): Rueckgabetyp|
| + methode2(param: Typ)    |
+---------------------------+
```

**Sichtbarkeiten:**

| Symbol | Bedeutung |
|--------|-----------|
| + | public |
| - | private |
| # | protected |
| ~ | package |

**Beziehungstypen:**

| Beziehung | Symbol | Beschreibung | Beispiel |
|-----------|--------|-------------|---------|
| Assoziation | ── | Allgemeine Beziehung | Kunde ── Bestellung |
| Aggregation | ──◇ | "Hat-ein" (Teil kann eigenstaendig existieren) | Abteilung ◇── Mitarbeiter |
| Komposition | ──◆ | "Besteht-aus" (Teil existiert nicht ohne Ganzes) | Haus ◆── Raum |
| Vererbung | ──▷ | "Ist-ein" (Generalisierung/Spezialisierung) | Hund ──▷ Tier |
| Realisierung | --▷ | Klasse implementiert Interface | Klasse --▷ Interface |
| Gerichtete Assoziation | ──> | Einseitige Navigierbarkeit | Bestellung ──> Artikel |

**Kardinalitaeten:**

| Notation | Bedeutung |
|----------|-----------|
| 1 | Genau eins |
| 0..1 | Null oder eins |
| * oder 0..* | Null bis beliebig viele |
| 1..* | Eins bis beliebig viele |
| n..m | Zwischen n und m |

---

## Sequenzdiagramm

**Definition:** Ein Sequenzdiagramm zeigt die zeitliche Abfolge von Nachrichten (Methodenaufrufen) zwischen Objekten entlang einer Zeitachse (von oben nach unten).

**Notationselemente:**

| Element | Symbol | Beschreibung |
|---------|--------|-------------|
| Objekt/Teilnehmer | Rechteck oben auf Lebenslinie | Beteiligte Instanz oder Klasse |
| Lebenslinie | Gestrichelte vertikale Linie | Existenzdauer des Objekts |
| Nachricht (synchron) | Pfeil mit ausgefuellter Spitze ──▶ | Methodenaufruf (Aufrufer wartet) |
| Antwort | Gestrichelter Pfeil ◁── | Rueckgabewert |
| Nachricht (asynchron) | Pfeil mit offener Spitze ──> | Nachricht ohne Warten auf Antwort |
| Aktivierungsbalken | Duennes Rechteck auf Lebenslinie | Zeigt aktive Verarbeitung |
| Fragment (alt) | Rahmen mit "alt" | Alternative Ablaeufe (if/else) |
| Fragment (loop) | Rahmen mit "loop" | Schleife |

**Kernaussagen:**
- Zeit laeuft von oben nach unten
- Nachrichten werden horizontal zwischen Lebenslinien gezeichnet
- Synchrone Nachrichten: Aufrufer wartet auf Antwort
- Fragmente (alt, loop, opt) modellieren Kontrollstrukturen

---

## Zustandsdiagramm

**Definition:** Ein Zustandsdiagramm modelliert die verschiedenen Zustaende eines Objekts und die Transitionen (Uebergaenge) zwischen den Zustaenden, ausgeloest durch Ereignisse.

**Notationselemente:**

| Element | Symbol | Beschreibung |
|---------|--------|-------------|
| Zustand | Abgerundetes Rechteck | Ein Zustand des Objekts |
| Startzustand | Gefuellter Kreis ● | Anfangszustand |
| Endzustand | Kreis mit Punkt ◉ | Endzustand |
| Transition | Pfeil ──> | Uebergang mit Anschrift: Ereignis [Bedingung] / Aktion |
| Entscheidung | Raute ◇ | Verzweigung basierend auf Bedingung |

**Transition-Syntax:**
```
Ereignis [Bedingung] / Aktion
```
- **Ereignis:** Was loest den Uebergang aus? (z.B. "Zahlung eingegangen")
- **Bedingung (Guard):** Voraussetzung fuer den Uebergang (z.B. "[Betrag korrekt]")
- **Aktion:** Was passiert beim Uebergang (z.B. "/ Rechnung erstellen")

**Kernaussagen:**
- Ein Objekt befindet sich immer in genau einem Zustand
- Transitionen werden durch Ereignisse ausgeloest
- Fuer die Pruefung: Zustaende aus Anforderungstext ableiten und Uebergaenge definieren
