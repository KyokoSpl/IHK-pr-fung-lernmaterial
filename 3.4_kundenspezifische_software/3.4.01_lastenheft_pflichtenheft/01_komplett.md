# Komplett: 3.4.01 – Lasten-/Pflichtenheft erstellen

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.01
- **Thema:** Lasten-/Pflichtenheft erstellen koennen

## Ziel

Du musst den Unterschied zwischen Lastenheft und Pflichtenheft kennen, wissen, wer welches Dokument erstellt, welche Inhalte darin stehen und warum beide Dokumente fuer ein IT-Projekt verbindlich sind.

## Grundlagen

### Lastenheft

**Definition:** Das Lastenheft beschreibt die Gesamtheit der Anforderungen des Auftraggebers an die Lieferungen und Leistungen eines Auftragnehmers. Es beantwortet die Frage **WAS** geliefert werden soll.

**Kernaussagen:**
- Wird vom **Auftraggeber** (Kunden) erstellt
- Beschreibt die fachlichen Anforderungen aus Kundensicht
- Grundlage fuer die Angebotserstellung
- Orientiert sich an DIN 69901 (Projektmanagement)

**Typische Inhalte eines Lastenhefts:**

| Abschnitt | Beschreibung |
|-----------|-------------|
| Ausgangssituation | IST-Zustand und Problemstellung |
| Zielsetzung | SOLL-Zustand, was soll erreicht werden |
| Funktionale Anforderungen | Was muss das System koennen (Use Cases) |
| Nichtfunktionale Anforderungen | Performance, Sicherheit, Verfuegbarkeit |
| Rahmenbedingungen | Budget, Zeitrahmen, technische Vorgaben |
| Schnittstellen | Anbindung an bestehende Systeme |
| Qualitaetsanforderungen | Testkriterien, Abnahmekriterien |
| Lieferumfang | Was genau wird erwartet (Software, Doku, Schulung) |

### Pflichtenheft

**Definition:** Das Pflichtenheft beschreibt, wie und womit der Auftragnehmer die Anforderungen des Lastenhefts umsetzen will. Es beantwortet die Frage **WIE** die Loesung realisiert wird.

**Kernaussagen:**
- Wird vom **Auftragnehmer** (Dienstleister/Entwickler) erstellt
- Basiert auf dem Lastenheft
- Beschreibt die technische Loesung und Umsetzungsstrategie
- Wird vom Auftraggeber abgenommen und freigegeben
- Vertragliche Grundlage fuer die Umsetzung

**Typische Inhalte eines Pflichtenhefts:**

| Abschnitt | Beschreibung |
|-----------|-------------|
| Systemarchitektur | Technischer Aufbau (Client-Server, Cloud etc.) |
| Technologien | Programmiersprachen, Frameworks, Datenbanken |
| Detaillierte Funktionsbeschreibung | Technische Umsetzung jeder Anforderung |
| Datenmodell | ER-Diagramm, Tabellenstruktur |
| Schnittstellenbeschreibung | API-Definitionen, Protokolle, Formate |
| Testkonzept | Teststrategie, Testfaelle |
| Zeitplan | Meilensteine, Phasenplanung |
| Abnahmekriterien | Messbare Kriterien fuer die Abnahme |

### Gegenueber­stellung Lastenheft vs. Pflichtenheft

| Kriterium | Lastenheft | Pflichtenheft |
|-----------|-----------|---------------|
| Erstellt von | Auftraggeber | Auftragnehmer |
| Fragestellung | WAS soll geliefert werden? | WIE wird es umgesetzt? |
| Perspektive | Fachlich/Kundensicht | Technisch/Entwicklersicht |
| Zeitpunkt | Vor der Angebotserstellung | Nach Auftragserteilung |
| Verbindlichkeit | Grundlage fuer Angebote | Vertragliche Grundlage |
| Detailgrad | Anforderungen (abstrakt) | Loesungen (konkret) |
| DIN-Norm | DIN 69901-5 | DIN 69901-5 |

---

## Vertiefung

### Zusammenhang im Projektverlauf

```
Auftraggeber                     Auftragnehmer
     |                                |
     |  1. Erstellt Lastenheft        |
     |------------------------------->|
     |                                |
     |  2. Erstellt Pflichtenheft     |
     |<-------------------------------|
     |                                |
     |  3. Prueft und gibt frei       |
     |------------------------------->|
     |                                |
     |  4. Umsetzung beginnt          |
     |                                |
```

### Beispieleintraege fuer ein IT-Projekt

**Szenario:** Ein Handwerksbetrieb moechte eine Auftragsverwaltung.

**Eintrag im Lastenheft (WAS):**
> "Das System soll es ermoeglichen, Kundenauftraege mit Adresse, Auftragsbeschreibung und Termin zu erfassen. Auftraege sollen nach Status (offen, in Bearbeitung, abgeschlossen) filterbar sein."

**Eintrag im Pflichtenheft (WIE):**
> "Die Auftragsverwaltung wird als Webanwendung mit React-Frontend und Node.js-Backend realisiert. Daten werden in einer PostgreSQL-Datenbank gespeichert. Die Tabelle `auftraege` enthaelt die Spalten: id (PK), kunde_id (FK), beschreibung (TEXT), termin (DATE), status (ENUM: offen, in_bearbeitung, abgeschlossen). Filterung ueber parametrisierte SQL-Abfragen."

### Typische Pruefungsaspekte
- Zuordnung: Welcher Satz gehoert ins Lastenheft, welcher ins Pflichtenheft?
- Wer erstellt welches Dokument?
- Reihenfolge: Lastenheft vor Pflichtenheft
- Inhalte benennen koennen
- Bedeutung fuer die Vertragsgestaltung

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| Lastenheft und Pflichtenheft verwechselt | Lastenheft = WAS (Kunde), Pflichtenheft = WIE (Entwickler) |
| Pflichtenheft wird vor dem Lastenheft erstellt | Immer zuerst Lastenheft, dann Pflichtenheft |
| Lastenheft enthaelt technische Details | Lastenheft ist fachlich, keine Technologievorgaben |
| Pflichtenheft hat keine Abnahmekriterien | Messbare Kriterien sind essenziell fuer die Abnahme |

---

## Uebungen

**Aufgabe 1:** Erklaere in je einem Satz den Unterschied zwischen Lastenheft und Pflichtenheft. Nenne jeweils den Ersteller und die zentrale Fragestellung.

**Aufgabe 2:** Ordne die folgenden Aussagen dem Lastenheft (L) oder Pflichtenheft (P) zu:
- a) "Das System wird mit Java und Spring Boot implementiert."
- b) "Der Nutzer soll Rechnungen als PDF exportieren koennen."
- c) "Die Daten werden in einer MySQL-Datenbank gespeichert."
- d) "Das System muss 500 gleichzeitige Nutzer unterstuetzen."
- e) "Die REST-API stellt einen Endpoint /api/invoices bereit."

**Aufgabe 3:** Ein Kunde moechte eine Lagerverwaltungssoftware. Formuliere je zwei Beispieleintraege fuer das Lastenheft und das Pflichtenheft.

---
---

# Loesungen

## Aufgabe 1
- **Lastenheft:** Wird vom Auftraggeber erstellt und beschreibt, WAS das System leisten soll (fachliche Anforderungen).
- **Pflichtenheft:** Wird vom Auftragnehmer erstellt und beschreibt, WIE die Anforderungen technisch umgesetzt werden.

## Aufgabe 2
- a) **P** – Technologieentscheidung (WIE)
- b) **L** – Funktionale Anforderung aus Nutzersicht (WAS)
- c) **P** – Technische Umsetzungsentscheidung (WIE)
- d) **L** – Nichtfunktionale Anforderung (WAS, keine Technologie)
- e) **P** – Technische Schnittstellenspezifikation (WIE)

## Aufgabe 3
**Lastenheft (WAS):**
1. "Das System soll den aktuellen Lagerbestand aller Artikel in Echtzeit anzeigen."
2. "Bei Unterschreitung eines Mindestbestands soll automatisch eine Benachrichtigung an den Lagerverantwortlichen gesendet werden."

**Pflichtenheft (WIE):**
1. "Der Lagerbestand wird in der Tabelle `artikel` (Spalten: id, bezeichnung, bestand, mindestbestand) gespeichert und ueber eine React-Oberflaeche mit Echtzeit-Updates via WebSocket dargestellt."
2. "Bei `bestand < mindestbestand` wird ein Cronjob (alle 5 Minuten) eine E-Mail ueber den SMTP-Server an die hinterlegte Adresse des Lagerverantwortlichen senden."
