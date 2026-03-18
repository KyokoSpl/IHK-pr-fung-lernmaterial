# Komplett: 3.4.10 – Datenmodelle erstellen

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.10
- **Thema:** Datenmodelle erstellen koennen

## Ziel

Du musst ER-Modelle (Entity-Relationship) erstellen, die Notation (Chen und Kraehenfuss) beherrschen, Kardinalitaeten festlegen und ER-Modelle in relationale Modelle (Tabellen) ueberfuehren koennen.

## Themenkreise

| Nr. | Themenkreis | Schwerpunkte |
|-----|------------|-------------|
| 1 | ER-Modell | Entitaeten, Attribute, Beziehungen, Kardinalitaeten, Chen/Kraehenfuss |
| 2 | Relationales Modell | Tabellen, Primaerschluessel, Fremdschluessel, Transformation aus ER |

---

## Grundlagen

### TK 1: ER-Modell (Entity-Relationship-Modell)

**Definition:** Das ER-Modell ist ein grafisches Modell zur Beschreibung von Datenstrukturen und deren Beziehungen. Es wird in der Datenbank-Entwurfsphase verwendet, bevor Tabellen erstellt werden.

**Grundelemente:**

| Element | Symbol (Chen) | Beschreibung |
|---------|--------------|-------------|
| Entitaet | Rechteck | Ein Objekt der realen Welt (z.B. Kunde, Artikel) |
| Attribut | Ellipse | Eigenschaft einer Entitaet (z.B. Name, Preis) |
| Beziehung (Relationship) | Raute | Verbindung zwischen Entitaeten (z.B. "bestellt") |
| Primaerschluessel | Unterstrichenes Attribut | Eindeutige Identifikation (z.B. KundenNr) |

**Kardinalitaeten:**

| Notation | Bedeutung | Beispiel |
|----------|-----------|---------|
| 1:1 | Genau eins zu genau eins | Person ── Personalausweis |
| 1:n | Eins zu viele | Kunde ── Bestellung |
| n:m | Viele zu viele | Student ── Vorlesung |

### Chen-Notation (Beispiel)

```
+----------+          +-----------+          +----------+
|  Kunde   |---<bestellt>---| Bestellung|
+----------+          +-----------+          
| KundeNr  |          | BestellNr |          
| Name     |          | Datum     |          
| Adresse  |          | Status    |          
+----------+          +-----------+          

      1          bestellt          n
  Kunde ─────────<>───────── Bestellung
```

### Kraehenfuss-Notation (Crow's Foot)

Die Kraehenfuss-Notation ist in der Praxis weiter verbreitet und nutzt spezielle Symbole an den Beziehungsenden:

| Symbol | Bedeutung |
|--------|-----------|
| ─── \|\| | Genau eins (obligatorisch) |
| ─── \|O | Null oder eins (optional) |
| ─── >< | Viele (obligatorisch, mindestens 1) |
| ─── >O | Null oder viele (optional) |

**Kraehenfuss-Beispiel:**

```
+----------+            +-----------+
|  Kunde   | 1       n  | Bestellung|
+----------+──||────><──+-----------+
| KundeNr  |            | BestellNr |
| Name     |            | Datum     |
| Adresse  |            | KundeNr(FK)|
+----------+            +-----------+

Lesen: Ein Kunde hat EINE bis VIELE Bestellungen.
       Eine Bestellung gehoert zu GENAU EINEM Kunden.
```

### Aufloesung von n:m-Beziehungen

n:m-Beziehungen koennen nicht direkt in Tabellen abgebildet werden. Sie werden durch eine **Zwischentabelle** (Assoziationstabelle) aufgeloest.

**Beispiel: Student n:m Vorlesung**

```
Vorher (ER):
  Student ────n:m──── Vorlesung

Nachher (aufgeloest):
  Student ──1:n── Belegung ──n:1── Vorlesung

  +----------+       +-----------+       +------------+
  | Student  | 1   n | Belegung  | n   1 | Vorlesung  |
  +----------+───────+-----------+───────+------------+
  | MatrNr   |       | MatrNr(FK)|       | VorlNr     |
  | Name     |       | VorlNr(FK)|       | Bezeichnung|
  +----------+       | Semester  |       | Dozent     |
                      +-----------+       +------------+
```

---

### TK 2: Relationales Modell

**Definition:** Das relationale Modell speichert Daten in Tabellen (Relationen). Jede Zeile ist ein Datensatz (Tupel), jede Spalte ein Attribut. Beziehungen werden ueber Primaer- und Fremdschluessel hergestellt.

**Grundbegriffe:**

| Begriff | Beschreibung |
|---------|-------------|
| Relation (Tabelle) | Strukturierte Menge von Datensaetzen |
| Tupel (Zeile) | Ein einzelner Datensatz |
| Attribut (Spalte) | Eine Eigenschaft der Relation |
| Primaerschluessel (PK) | Eindeutige Identifikation jedes Tupels |
| Fremdschluessel (FK) | Verweis auf den Primaerschluessel einer anderen Tabelle |
| Domaene | Wertebereich eines Attributs (z.B. INT, VARCHAR) |

### Transformation: ER → Relationales Modell

| ER-Element | Relationales Modell |
|-----------|-------------------|
| Entitaet | Tabelle |
| Attribut | Spalte |
| Primaerschluessel | PRIMARY KEY |
| 1:n-Beziehung | Fremdschluessel in der n-Seite |
| n:m-Beziehung | Zwischentabelle mit zwei Fremdschluesseln |
| 1:1-Beziehung | Fremdschluessel in einer der beiden Tabellen |

**Beispiel – Vollstaendige Transformation:**

ER-Modell: Kunde (1) ── bestellt (n) ── Bestellung (n) ── enthaelt (m) ── Artikel

**Relationales Modell (Tabellenschreibweise):**

```
Kunde (KundeNr [PK], Name, Adresse, Email)
Bestellung (BestellNr [PK], Datum, Status, KundeNr [FK → Kunde])
Artikel (ArtikelNr [PK], Bezeichnung, Preis)
BestellPosition (BestellNr [FK], ArtikelNr [FK], Menge, Einzelpreis)
    → PK: (BestellNr, ArtikelNr) = zusammengesetzter Primaerschluessel
```

---

## Vertiefung

### Chen vs. Kraehenfuss im Vergleich

| Aspekt | Chen-Notation | Kraehenfuss-Notation |
|--------|--------------|---------------------|
| Entitaeten | Rechteck | Rechteck |
| Beziehungen | Raute mit Beschriftung | Linie mit Symbolen an den Enden |
| Kardinalitaeten | 1, n, m an der Linie | Symbole: \|\|, >O, ><, \|O |
| Attribute | Ellipsen | In der Entitaet aufgelistet |
| Verbreitung | Akademisch, Lehre | Praxis, Tools (MySQL Workbench, ERDPlus) |
| Platzbedarf | Hoch (viele Ellipsen) | Kompakt |

### Typische Pruefungsaspekte
- Aus Anforderungstext ein ER-Diagramm ableiten
- Kardinalitaeten bestimmen und begruenden
- n:m-Beziehung aufloesen
- ER-Modell in relationale Tabellen ueberfuehren
- Primaer- und Fremdschluessel korrekt setzen
- Chen- und Kraehenfuss-Notation kennen

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| n:m-Beziehung direkt in Tabellen abgebildet | n:m muss durch Zwischentabelle aufgeloest werden |
| Fremdschluessel auf der falschen Seite | Bei 1:n kommt der FK in die n-Seite (die "viele"-Tabelle) |
| Primaerschluessel vergessen | Jede Tabelle braucht einen eindeutigen PK |
| Attribute der Beziehung vergessen | Bei n:m koennen Attribute an der Beziehung haengen (z.B. Menge, Datum) |
| Chen und Kraehenfuss verwechselt | Chen = Raute fuer Beziehung; Kraehenfuss = Symbole am Linienende |

---

## Uebungen

**Aufgabe 1:** Erstelle ein ER-Diagramm fuer folgendes Szenario:
> "Ein Verlag verwaltet Autoren und Buecher. Ein Autor kann mehrere Buecher schreiben. Ein Buch kann von mehreren Autoren verfasst werden. Jedes Buch hat eine ISBN, einen Titel und ein Erscheinungsjahr. Autoren haben eine AutorID und einen Namen."

Bestimme die Kardinalitaet und loese die Beziehung ggf. auf.

**Aufgabe 2:** Ueberfuehre das ER-Modell aus Aufgabe 1 in ein relationales Modell (Tabellenschreibweise mit PK und FK).

**Aufgabe 3:** Erklaere den Unterschied zwischen Primaerschluessel und Fremdschluessel in je einem Satz. Nenne dazu ein Beispiel.

**Aufgabe 4:** In welche Tabelle kommt der Fremdschluessel bei einer 1:n-Beziehung? Begruende.

---
---

# Loesungen

## Aufgabe 1

**Entitaeten:** Autor, Buch
**Kardinalitaet:** n:m (ein Autor schreibt mehrere Buecher, ein Buch hat mehrere Autoren)
**Aufloesung:** Zwischentabelle "Autorschaft"

```
+----------+       +-------------+       +----------+
|  Autor   | 1   n |  Autorschaft| n   1 |   Buch   |
+----------+───────+-------------+───────+----------+
| AutorID  |       | AutorID (FK)|       | ISBN     |
| Name     |       | ISBN (FK)   |       | Titel    |
+----------+       +-------------+       | Jahr     |
                                         +----------+
```

## Aufgabe 2

```
Autor (AutorID [PK], Name)
Buch (ISBN [PK], Titel, Erscheinungsjahr)
Autorschaft (AutorID [FK → Autor], ISBN [FK → Buch])
    → PK: (AutorID, ISBN)
```

## Aufgabe 3
- **Primaerschluessel (PK):** Identifiziert einen Datensatz in einer Tabelle eindeutig und darf nicht NULL sein. Beispiel: `KundeNr` in der Tabelle `Kunde`.
- **Fremdschluessel (FK):** Verweist auf den Primaerschluessel einer anderen Tabelle und stellt die Beziehung zwischen Tabellen her. Beispiel: `KundeNr` in der Tabelle `Bestellung` verweist auf `Kunde.KundeNr`.

## Aufgabe 4
Der Fremdschluessel kommt in die Tabelle auf der **n-Seite** (die "viele"-Seite). Begruendung: Jeder Datensatz auf der n-Seite gehoert zu genau einem Datensatz auf der 1-Seite. Der FK speichert diese Zuordnung. Beispiel: Bei Kunde (1) ── Bestellung (n) steht `KundeNr` als FK in der Tabelle `Bestellung`, weil jede Bestellung zu genau einem Kunden gehoert.
