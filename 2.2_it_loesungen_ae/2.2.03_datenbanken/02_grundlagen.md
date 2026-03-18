# Grundlagen: 2.2.03 – Datenbanken modellieren und erstellen

## ER-Modell (Entity-Relationship)

**Bestandteile:**

| Element | Symbol | Beschreibung |
|---|---|---|
| Entitaet | Rechteck | Objekt/Datensatz (z.B. Kunde, Produkt) |
| Attribut | Oval | Eigenschaft einer Entitaet (z.B. Name) |
| Beziehung | Raute | Verbindung zwischen Entitaeten |
| Primaerschluessel | Unterstrichenes Attribut | Eindeutige Identifikation |

**Kardinalitaeten:**

| Notation | Bedeutung | Beispiel |
|---|---|---|
| 1:1 | Genau eine Zuordnung | Person → Personalausweis |
| 1:n | Eine Entitaet → mehrere | Abteilung → Mitarbeiter |
| n:m | Mehrere → mehrere | Student → Vorlesung |

**n:m-Aufloesung:** Zwischentabelle mit Fremdschluesseln beider Seiten.

---

## Datentypen

| Datentyp | Beschreibung | Beispiel |
|---|---|---|
| INT / INTEGER | Ganzzahl | Alter, Menge |
| FLOAT / DOUBLE | Gleitkommazahl | Preis (ungenau!) |
| DECIMAL(p,s) | Festkommazahl | Waehrung: DECIMAL(10,2) |
| VARCHAR(n) | Text variabler Laenge | Name VARCHAR(100) |
| CHAR(n) | Text fester Laenge | PLZ CHAR(5) |
| TEXT | Langer Text | Beschreibung |
| DATE | Datum | Geburtsdatum |
| DATETIME / TIMESTAMP | Datum + Uhrzeit | Erstellungszeitpunkt |
| BOOLEAN | Wahrheitswert | Aktiv: TRUE/FALSE |
| BLOB | Binaerdaten | Bilder, Dateien |

---

## Anomalien und Redundanzen

| Anomalie | Beschreibung | Beispiel |
|---|---|---|
| Einfuege-Anomalie | Daten koennen nicht ohne Zusatzinfo eingefuegt werden | Neuer Kunde ohne Auftrag |
| Aenderungs-Anomalie | Aenderung an mehreren Stellen noetig | Kundenadresse in jeder Bestellung |
| Loesch-Anomalie | Beim Loeschen gehen andere Daten verloren | Letzter Auftrag geloescht → Kundendaten weg |

**Loesung:** Normalisierung → Redundanzen eliminieren.

---

## Normalisierung (1. bis 3. Normalform)

### 1. Normalform (1NF)
- Jedes Attribut enthaelt nur **atomare** (unteilbare) Werte
- Keine Wiederholungsgruppen

**Verstoss:** Telefon = "0123, 0456" → Aufteilen in separate Datensaetze/Tabelle

### 2. Normalform (2NF)
- 1NF erfuellt
- Jedes Nicht-Schluessel-Attribut ist **voll funktional abhaengig** vom gesamten Primaerschluessel
- Relevant bei zusammengesetzten Schluesseln

### 3. Normalform (3NF)
- 2NF erfuellt
- Keine **transitiven Abhaengigkeiten** (Nicht-Schluessel-Attribut haengt nicht von anderem Nicht-Schluessel-Attribut ab)

**Beispiel transitive Abhaengigkeit:**
```
Mitarbeiter → AbteilungsNr → AbteilungsName  (transitiv!)
Loesung: AbteilungsName in eigene Tabelle "Abteilung"
```

---

## SQL-Grundlagen

### DDL (Data Definition Language)

```sql
CREATE TABLE Kunde (
    KundenID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(150) UNIQUE,
    Erstellt DATE DEFAULT CURRENT_DATE
);

ALTER TABLE Kunde ADD Telefon VARCHAR(20);

CREATE INDEX idx_name ON Kunde(Name);
```

### DML (Data Manipulation Language)

```sql
INSERT INTO Kunde (Name, Email) VALUES ('Mueller GmbH', 'info@mueller.de');

UPDATE Kunde SET Email = 'neu@mueller.de' WHERE KundenID = 1;

DELETE FROM Kunde WHERE KundenID = 5;
```

### DQL (Data Query Language)

```sql
-- Projektion + Selektion
SELECT Name, Email FROM Kunde WHERE KundenID > 10;

-- Sortieren
SELECT * FROM Kunde ORDER BY Name ASC;

-- Aggregatfunktionen + Gruppieren
SELECT AbteilungsID, COUNT(*) AS Anzahl, AVG(Gehalt) AS Durchschnitt
FROM Mitarbeiter
GROUP BY AbteilungsID
HAVING COUNT(*) > 5;
```

---

## JOINs (Abfrage ueber mehrere Tabellen)

| JOIN-Typ | Beschreibung |
|---|---|
| INNER JOIN | Nur uebereinstimmende Datensaetze |
| LEFT JOIN | Alle links + uebereinstimmende rechts |
| RIGHT JOIN | Alle rechts + uebereinstimmende links |
| CROSS JOIN | Kartesisches Produkt (jeder mit jedem) |

```sql
SELECT k.Name, b.Datum, b.Betrag
FROM Kunde k
INNER JOIN Bestellung b ON k.KundenID = b.KundenID
WHERE b.Betrag > 1000
ORDER BY b.Datum DESC;
```

---

## Relationale vs. NoSQL-Datenbanken

| Merkmal | Relational (SQL) | NoSQL |
|---|---|---|
| Struktur | Tabellen mit Spalten | Dokumente, Key-Value, Graphen |
| Schema | Festes Schema | Flexibles/kein Schema |
| Sprache | SQL | Abhaengig vom System |
| Konsistenz | ACID (stark) | BASE (eventual consistency) |
| Skalierung | Vertikal (groesserer Server) | Horizontal (mehr Server) |
| Beispiele | MySQL, PostgreSQL, MariaDB | MongoDB, Redis, Cassandra, Neo4j |
| Einsatz | Strukturierte Daten, Transaktionen | Big Data, flexible Strukturen |

---

## OpenData und API-Schnittstellen

**OpenData:** Frei zugaengliche Daten ohne Lizenzeinschraenkungen (z.B. GovData, Open-Meteo).

**REST-API:** Standardisierter Zugriff auf Daten ueber HTTP.

| HTTP-Methode | CRUD-Operation | Beschreibung |
|---|---|---|
| GET | Read | Daten abfragen |
| POST | Create | Daten erstellen |
| PUT | Update | Daten aktualisieren (komplett) |
| PATCH | Update | Daten teilweise aktualisieren |
| DELETE | Delete | Daten loeschen |

**Datenformate:** JSON (Standard), XML, CSV
