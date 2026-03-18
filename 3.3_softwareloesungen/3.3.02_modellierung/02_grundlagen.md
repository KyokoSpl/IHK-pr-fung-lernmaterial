# 3.3.02 – Grundlagen: Planen mit geeigneten Modellen

## TK 1: Entity-Relationship-Modell (ERM)

### Definition
Das ERM ist ein **konzeptionelles Datenmodell** zur Darstellung von Datenstrukturen und deren Beziehungen – unabhaengig von der technischen Umsetzung.

### Bestandteile

| Element | Symbol | Beschreibung |
|---------|--------|-------------|
| Entitaet (Entity) | Rechteck | Ein Objekt der realen Welt (z.B. Kunde, Artikel) |
| Attribut | Oval/Ellipse | Eigenschaft einer Entitaet (z.B. Name, Preis) |
| Beziehung (Relationship) | Raute | Verbindung zwischen Entitaeten (z.B. "bestellt") |
| Primaerschluessel | Unterstrichenes Attribut | Eindeutige Identifikation (z.B. KundenNr) |

### Kardinalitaeten

| Notation | Bedeutung | Beispiel |
|----------|-----------|---------|
| 1 : 1 | Eins zu Eins | Person – Personalausweis |
| 1 : n | Eins zu Viele | Abteilung – Mitarbeiter |
| n : m | Viele zu Viele | Student – Vorlesung |

### ASCII-Beispiel: ERM

```
+----------+         +----------+         +----------+
|  Kunde   |---< bestellt >---|  Artikel |
+----------+         +----------+         +----------+
| KundenNr |         | Datum    |         | ArtikelNr|
| Name     |         | Menge    |         | Bezeichn.|
| Adresse  |                              | Preis    |
+----------+                              +----------+
     1                                         n
     Ein Kunde bestellt viele Artikel (1:n nach Auflosung)
```

---

## TK 2: Mockup

### Definition
Ein **Mockup** ist ein visueller Entwurf einer Benutzeroberflaeche – ohne Funktionalitaet. Es dient der fruehen Abstimmung mit Stakeholdern.

### Abstufungen

| Typ | Detail | Einsatz |
|-----|--------|---------|
| Sketch/Skizze | Grob, handgezeichnet | Erste Ideenfindung |
| Wireframe | Strukturlayout ohne Design | Funktionsplanung, Navigation |
| Mockup | Detailliert mit Farben/Schriften | Design-Abstimmung |
| Prototyp | Interaktiv, klickbar | Usability-Tests |

### Werkzeuge

| Tool | Typ | Besonderheit |
|------|-----|-------------|
| Balsamiq | Wireframe | Skizzenhafter Stil |
| Figma | Mockup/Prototyp | Kollaborativ, browserbasiert |
| Adobe XD | Mockup/Prototyp | Integration mit Adobe-Suite |
| Pencil Project | Wireframe | Open Source |
| draw.io | Wireframe | Kostenlos, vielseitig |

---

## TK 3: Relationales Datenbankmodell

### Definition
Das relationale Modell organisiert Daten in **Tabellen (Relationen)** mit Zeilen (Tupel) und Spalten (Attribute).

### Schluesselkonzepte

| Begriff | Beschreibung | Beispiel |
|---------|-------------|----------|
| Relation/Tabelle | Strukturierte Datenmenge | `Kunde`, `Bestellung` |
| Tupel/Zeile | Ein Datensatz | (1, "Mueller", "Berlin") |
| Attribut/Spalte | Eine Eigenschaft | `Name`, `PLZ` |
| Primaerschluessel (PK) | Eindeutige Identifikation | `KundenNr` |
| Fremdschluessel (FK) | Verweis auf anderen PK | `KundenNr` in `Bestellung` |
| Referenzielle Integritaet | FK muss auf existierenden PK verweisen | Keine Bestellung ohne Kunde |

### ERM → Relationales Modell (Transformation)

| ERM-Element | Relationales Modell |
|-------------|-------------------|
| Entitaet | Tabelle |
| Attribut | Spalte |
| Primaerschluessel | PRIMARY KEY |
| 1:n-Beziehung | Fremdschluessel auf der n-Seite |
| n:m-Beziehung | Zwischentabelle mit zwei Fremdschluesseln |
| 1:1-Beziehung | FK in einer der beiden Tabellen (UNIQUE) |

### Beispiel: n:m-Auflosung

```
ERM:
  Student ──n:m── Vorlesung

Relationales Modell:
  Student (StudentNr PK, Name, Matrikelnr)
  Vorlesung (VorlesungNr PK, Titel, SWS)
  Belegung (StudentNr FK, VorlesungNr FK)  ← Zwischentabelle
           PK = (StudentNr, VorlesungNr)    ← zusammengesetzter PK
```

---

## TK 4: UML-Aktivitaetsdiagramm

### Definition
Modelliert den **Ablauf von Aktivitaeten** (Kontrollfluss), aehnlich einem Programmablaufplan, aber mit UML-Notation.

### Symbole

| Symbol | Bedeutung | Darstellung |
|--------|-----------|-------------|
| Ausgefuellter Kreis | Startknoten | ● |
| Kreis mit Rand | Endknoten | ◉ |
| Abgerundetes Rechteck | Aktivitaet/Aktion | ( Aktion ) |
| Raute | Entscheidung/Verzweigung | ◇ |
| Balken (horizontal) | Fork/Join (Parallelitaet) | ═══ |
| Pfeil | Kontrollfluss | → |

### ASCII-Beispiel: Bestellprozess

```
        ●  (Start)
        |
  [Bestellung eingeben]
        |
       ◇ Lager pruefen
      / \
    ja    nein
    /       \
[Versand     [Nachbestellen]
 vorbereiten]      |
    \         [Warten auf
     \         Lieferung]
      \       /
  ═══════════════  (Join)
        |
  [Rechnung erstellen]
        |
  [Bestellung abschliessen]
        |
        ◉  (Ende)
```

---

## TK 5: UML-Anwendungsfalldiagramm (Use Case Diagram)

### Definition
Zeigt die **Funktionalitaet eines Systems** aus Sicht der **Akteure** (Benutzer oder externe Systeme).

### Elemente

| Element | Symbol | Beschreibung |
|---------|--------|-------------|
| Akteur | Strichmaennchen | Benutzer oder externes System |
| Use Case | Ellipse | Eine Funktion des Systems |
| Systemgrenze | Rechteck | Grenzt das System ab |
| Assoziation | Linie | Akteur nutzt Use Case |
| <<include>> | Gestrichelter Pfeil | Use Case enthaelt anderen zwingend |
| <<extend>> | Gestrichelter Pfeil | Use Case kann optional erweitert werden |

### ASCII-Beispiel: Online-Banking

```
+----------------------------------------+
|         Online-Banking-System          |
|                                        |
|   (Kontostand anzeigen)               |
|        /                               |
| Kunde ----(Ueberweisung taetigen)     |
|        \                               |
|   (Dauerauftrag einrichten)            |
|                                        |
|   (Ueberweisung taetigen)             |
|        - - -<<include>>- - ->          |
|              (TAN eingeben)            |
|                                        |
| Admin ----(Konto sperren)             |
|                                        |
+----------------------------------------+
```

**<<include>>**: TAN-Eingabe ist IMMER Teil der Ueberweisung
**<<extend>>**: Optionale Erweiterung (z.B. SMS-Benachrichtigung)

---

## TK 6: UML-Klassendiagramm

### Definition
Zeigt die **statische Struktur** eines Systems: Klassen, ihre Attribute, Methoden und Beziehungen.

### Aufbau einer Klasse

```
+-------------------------+
|       Klassenname       |
+-------------------------+
| - attribut1: Typ        |   (-) private
| # attribut2: Typ        |   (#) protected
| + attribut3: Typ        |   (+) public
+-------------------------+
| + methode1(): Rueckgabe |
| - methode2(param: Typ)  |
+-------------------------+
```

### Beziehungstypen

| Beziehung | Symbol | Beschreibung | Beispiel |
|-----------|--------|-------------|----------|
| Assoziation | ——— | Allgemeine Verbindung | Kunde — Bestellung |
| Aggregation | ——◇ | "hat-ein" (lose, Teil kann allein existieren) | Team ◇— Mitarbeiter |
| Komposition | ——◆ | "besteht-aus" (stark, Teil nicht ohne Ganzes) | Haus ◆— Raum |
| Vererbung | ——▷ | "ist-ein" (Generalisierung) | Hund ▷— Tier |
| Implementierung | - -▷ | Klasse implementiert Interface | Klasse - -▷ Interface |

### Multiplizitaeten

| Notation | Bedeutung |
|----------|-----------|
| 1 | Genau eins |
| 0..1 | Null oder eins |
| * | Beliebig viele |
| 1..* | Eins oder mehr |
| 0..* | Null oder mehr |

### ASCII-Beispiel

```
+------------------+          +------------------+
|     Fahrzeug     |          |      Motor       |
+------------------+  1    1  +------------------+
| - marke: String  |◆--------| - ps: int        |
| - baujahr: int   |         | - typ: String    |
+------------------+         +------------------+
| + starten()      |         | + anlassen()     |
| + bremsen()      |         +------------------+
+------------------+
        △
        |
+------------------+
|       PKW        |
+------------------+
| - sitzplaetze: int|
+------------------+
| + kofferraum()   |
+------------------+
```

---

## TK 7: UML-Sequenzdiagramm

### Definition
Zeigt den **zeitlichen Ablauf von Nachrichten** zwischen Objekten (Lebenslinien).

### Elemente

| Element | Beschreibung |
|---------|-------------|
| Lebenslinie | Gestrichelte vertikale Linie unter einem Objekt |
| Nachricht (synchron) | Durchgezogener Pfeil → |
| Antwort | Gestrichelter Pfeil ← |
| Aktivierung | Schmales Rechteck auf Lebenslinie |
| Schleife (loop) | Rahmen mit Bezeichnung "loop" |
| Alternative (alt) | Rahmen mit Bezeichnung "alt" und Bedingungen |

### ASCII-Beispiel: Login-Prozess

```
  Benutzer        LoginUI        AuthService       Datenbank
     |               |               |                |
     |--eingeben()--->|               |                |
     |               |--login()----->|                |
     |               |               |--query()------>|
     |               |               |<--Ergebnis-----|
     |               |               |                |
     |               |  [alt]        |                |
     |               |  [ok]         |                |
     |               |<--Token-------|                |
     |<--Startseite--|               |                |
     |               |  [fehlgeschl.]|                |
     |               |<--Fehler------|                |
     |<--Fehlermeldg-|               |                |
     |               |               |                |
```

---

## TK 8: UML-Zustandsdiagramm (FI AE)

### Definition
Zeigt die **Zustaende eines Objekts** und die **Uebergaenge (Transitionen)** zwischen diesen Zustaenden, ausgeloest durch Ereignisse.

### Elemente

| Element | Symbol | Beschreibung |
|---------|--------|-------------|
| Startzustand | ● | Ausgefuellter Kreis |
| Endzustand | ◉ | Kreis mit innrem Punkt |
| Zustand | Abgerundetes Rechteck | Zustand des Objekts |
| Transition | Pfeil mit Beschriftung | Zustandswechsel |
| Ereignis/Bedingung | Text am Pfeil | Ausloser fuer Transition |

### Transitionsbeschriftung

```
Ereignis [Bedingung] / Aktion
```

### ASCII-Beispiel: Bestellstatus

```
    ●
    |
    v
+----------+  bezahlt   +-----------+  versendet  +-----------+
|  Neu     |----------->| Bezahlt   |------------>| Versendet |
+----------+            +-----------+             +-----------+
    |                        |                         |
    | storniert              | storniert                | zugestellt
    v                        v                         v
+-----------+          +-----------+             +-----------+
| Storniert |          | Storniert |             | Zugestellt|
+-----------+          | (Erstattg)|             +-----------+
                       +-----------+                   |
                                                       | reklamiert
                                                       v
                                                 +-----------+
                                                 | Reklamiert|
                                                 +-----------+
                                                       |
                                                       v
                                                       ◉
```
