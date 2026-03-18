# Grundlagen: 3.4.22 – Datenbankabfrage, Datenpflege mit SQL

## SQL-Kategorien

| Kategorie | Abkuerzung | Befehle | Zweck |
|-----------|-----------|---------|-------|
| Data Query Language | DQL | SELECT | Daten abfragen |
| Data Manipulation Language | DML | INSERT, UPDATE, DELETE | Daten aendern |
| Data Definition Language | DDL | CREATE, ALTER, DROP | Struktur aendern |
| Data Control Language | DCL | GRANT, REVOKE | Rechte verwalten |

**Beispiel-Datenbank fuer alle Abfragen:**

```
Tabelle: kunden
+----+----------------+----------+--------+
| id | name           | stadt    | typ    |
+----+----------------+----------+--------+
|  1 | Mueller GmbH   | Berlin   | Premium|
|  2 | Schmidt AG     | Hamburg  | Normal |
|  3 | Weber IT       | Berlin   | Premium|
|  4 | Fischer KG     | Muenchen | Normal |
+----+----------------+----------+--------+

Tabelle: bestellungen
+----+-----------+------------+--------+
| id | kunden_id | datum      | betrag |
+----+-----------+------------+--------+
|  1 |         1 | 2025-01-15 | 500.00 |
|  2 |         1 | 2025-03-22 | 750.00 |
|  3 |         2 | 2025-02-10 | 200.00 |
|  4 |         3 | 2025-04-05 | 1200.00|
|  5 |         3 | 2025-05-18 | 300.00 |
+----+-----------+------------+--------+

Tabelle: artikel
+----+------------------+--------+----------+
| id | bezeichnung      | preis  | kategorie|
+----+------------------+--------+----------+
|  1 | Laptop           | 899.99 | Hardware |
|  2 | Maus             |  29.99 | Zubehoer |
|  3 | Monitor          | 349.00 | Hardware |
|  4 | USB-Kabel        |   9.99 | Zubehoer |
|  5 | Tastatur         |  59.99 | Zubehoer |
+----+------------------+--------+----------+
```

---

## Projektion (SELECT FROM)

**Definition:** Projektion waehlt bestimmte Spalten aus einer Tabelle aus.

```sql
-- Alle Spalten
SELECT * FROM kunden;

-- Bestimmte Spalten (Projektion)
SELECT name, stadt FROM kunden;

-- Ohne Duplikate
SELECT DISTINCT stadt FROM kunden;

-- Berechnete Spalte mit Alias
SELECT bezeichnung, preis, preis * 1.19 AS brutto FROM artikel;
```

---

## Selektion (SELECT FROM WHERE) und verschachtelte SELECTs

**Definition:** Selektion filtert Zeilen anhand von Bedingungen.

```sql
-- Einfache Bedingung
SELECT * FROM kunden WHERE stadt = 'Berlin';

-- Mehrere Bedingungen
SELECT * FROM kunden WHERE stadt = 'Berlin' AND typ = 'Premium';

-- Verschachteltes SELECT (Subquery)
SELECT * FROM kunden
WHERE id IN (SELECT kunden_id FROM bestellungen WHERE betrag > 500);
```

**Subquery-Arten:**

| Art | Beschreibung | Beispiel |
|-----|-------------|----------|
| Skalare Subquery | Gibt genau einen Wert zurueck | `WHERE betrag > (SELECT AVG(betrag) FROM bestellungen)` |
| Zeilen-Subquery | Gibt eine Liste von Werten zurueck | `WHERE id IN (SELECT kunden_id FROM ...)` |
| EXISTS-Subquery | Prueft, ob Ergebnis existiert | `WHERE EXISTS (SELECT 1 FROM bestellungen WHERE ...)` |

---

## Ausdruecke / Bedingungen

| Operator | Bedeutung | Beispiel |
|----------|-----------|----------|
| `=` | Gleich | `WHERE stadt = 'Berlin'` |
| `<>` oder `!=` | Ungleich | `WHERE typ <> 'Premium'` |
| `<`, `>`, `<=`, `>=` | Vergleich | `WHERE preis >= 100` |
| `AND` | Logisches UND | `WHERE preis > 50 AND kategorie = 'Hardware'` |
| `OR` | Logisches ODER | `WHERE stadt = 'Berlin' OR stadt = 'Hamburg'` |
| `NOT` | Logische Verneinung | `WHERE NOT typ = 'Premium'` |
| `BETWEEN` | Bereich (inklusiv) | `WHERE preis BETWEEN 10 AND 100` |
| `IN` | Wert in Liste | `WHERE stadt IN ('Berlin', 'Hamburg')` |
| `LIKE` | Mustervergleich | `WHERE name LIKE 'M%'` (beginnt mit M) |
| `IS NULL` | Pruefung auf NULL | `WHERE stadt IS NULL` |
| `IS NOT NULL` | Pruefung auf nicht NULL | `WHERE stadt IS NOT NULL` |

**LIKE-Platzhalter:**
- `%` = beliebig viele Zeichen (auch null)
- `_` = genau ein Zeichen

```sql
WHERE name LIKE 'M%'      -- beginnt mit M
WHERE name LIKE '%GmbH'   -- endet mit GmbH
WHERE name LIKE '%IT%'    -- enthaelt IT
WHERE name LIKE 'M____'   -- M gefolgt von genau 4 Zeichen
```

---

## Sortieren (ORDER BY)

```sql
-- Aufsteigend (Standard)
SELECT * FROM artikel ORDER BY preis ASC;

-- Absteigend
SELECT * FROM artikel ORDER BY preis DESC;

-- Mehrere Spalten
SELECT * FROM artikel ORDER BY kategorie ASC, preis DESC;
```

---

## Aggregatfunktionen

| Funktion | Beschreibung | Beispiel |
|----------|-------------|----------|
| COUNT(*) | Anzahl aller Zeilen | `SELECT COUNT(*) FROM kunden;` → 4 |
| COUNT(spalte) | Anzahl nicht-NULL-Werte | `SELECT COUNT(stadt) FROM kunden;` |
| SUM(spalte) | Summe | `SELECT SUM(betrag) FROM bestellungen;` → 2950.00 |
| AVG(spalte) | Durchschnitt | `SELECT AVG(betrag) FROM bestellungen;` → 590.00 |
| MIN(spalte) | Minimum | `SELECT MIN(preis) FROM artikel;` → 9.99 |
| MAX(spalte) | Maximum | `SELECT MAX(preis) FROM artikel;` → 899.99 |

```sql
-- Kombiniert
SELECT COUNT(*) AS anzahl, SUM(betrag) AS gesamt, AVG(betrag) AS durchschnitt
FROM bestellungen;
```

---

## Gruppieren (GROUP BY, HAVING)

**GROUP BY** fasst Zeilen mit gleichen Werten in Gruppen zusammen.
**HAVING** filtert Gruppen (wie WHERE, aber fuer Aggregatfunktionen).

```sql
-- Anzahl Bestellungen pro Kunde
SELECT kunden_id, COUNT(*) AS anzahl_bestellungen
FROM bestellungen
GROUP BY kunden_id;

-- Ergebnis:
-- kunden_id | anzahl_bestellungen
-- 1         | 2
-- 2         | 1
-- 3         | 2

-- Nur Kunden mit mehr als einer Bestellung
SELECT kunden_id, COUNT(*) AS anzahl
FROM bestellungen
GROUP BY kunden_id
HAVING COUNT(*) > 1;

-- Umsatz pro Stadt
SELECT k.stadt, SUM(b.betrag) AS umsatz
FROM kunden k
JOIN bestellungen b ON k.id = b.kunden_id
GROUP BY k.stadt
HAVING SUM(b.betrag) > 500;
```

**Reihenfolge der Klauseln:**
```
SELECT    → Welche Spalten?
FROM      → Aus welcher Tabelle?
JOIN      → Mit welcher Tabelle verknuepft?
WHERE     → Welche Zeilen (vor Gruppierung)?
GROUP BY  → Wie gruppieren?
HAVING    → Welche Gruppen (nach Gruppierung)?
ORDER BY  → Wie sortieren?
LIMIT     → Wie viele Ergebnisse?
```

**Merke:** WHERE filtert **Zeilen** (vor GROUP BY), HAVING filtert **Gruppen** (nach GROUP BY).

---

## Abfrage ueber mehrere Tabellen (JOINs)

**Definition:** JOINs verknuepfen zwei oder mehr Tabellen ueber Schluesselbeziehungen.

### JOIN-Typen

| JOIN-Typ | Beschreibung | Ergebnis |
|----------|-------------|----------|
| INNER JOIN | Nur uebereinstimmende Zeilen aus beiden Tabellen | Schnittmenge |
| LEFT JOIN | Alle Zeilen der linken Tabelle + uebereinstimmende der rechten | Links komplett, rechts ggf. NULL |
| RIGHT JOIN | Alle Zeilen der rechten Tabelle + uebereinstimmende der linken | Rechts komplett, links ggf. NULL |
| CROSS JOIN | Jede Zeile mit jeder (kartesisches Produkt) | Alle Kombinationen |

**ASCII-Diagramm:**

```
INNER JOIN:          LEFT JOIN:           RIGHT JOIN:
  +---+---+           +---+---+           +---+---+
  | A | B |           | A | B |           | A | B |
  +---+---+           +---+---+           +---+---+
    [###]              [A][###]              [###][B]
  Nur Schnitt-        Alles von A           Alles von B
  menge               + Matches von B       + Matches von A
```

**Beispiele:**

```sql
-- INNER JOIN: Kunden MIT Bestellungen
SELECT k.name, b.datum, b.betrag
FROM kunden k
INNER JOIN bestellungen b ON k.id = b.kunden_id;

-- LEFT JOIN: ALLE Kunden, auch ohne Bestellungen
SELECT k.name, b.datum, b.betrag
FROM kunden k
LEFT JOIN bestellungen b ON k.id = b.kunden_id;

-- Ergebnis LEFT JOIN:
-- Mueller GmbH   | 2025-01-15 | 500.00
-- Mueller GmbH   | 2025-03-22 | 750.00
-- Schmidt AG     | 2025-02-10 | 200.00
-- Weber IT       | 2025-04-05 | 1200.00
-- Weber IT       | 2025-05-18 | 300.00
-- Fischer KG     | NULL       | NULL        ← Keine Bestellung!
```

---

## Manipulation (INSERT, UPDATE, DELETE)

```sql
-- INSERT: Neuen Datensatz einfuegen
INSERT INTO kunden (name, stadt, typ)
VALUES ('Neumann Ltd', 'Koeln', 'Normal');

-- UPDATE: Bestehenden Datensatz aendern
UPDATE kunden
SET typ = 'Premium'
WHERE id = 2;

-- DELETE: Datensatz loeschen
DELETE FROM kunden
WHERE id = 4;

-- ACHTUNG: Ohne WHERE wird ALLES geloescht/geaendert!
DELETE FROM kunden;      -- Loescht ALLE Kunden!
UPDATE kunden SET typ = 'Normal';  -- Setzt ALLE auf Normal!
```

---

## Tabellenstruktur (CREATE TABLE, ALTER TABLE)

```sql
-- CREATE TABLE
CREATE TABLE kunden (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    stadt VARCHAR(50),
    typ VARCHAR(20) DEFAULT 'Normal',
    erstellt_am DATE DEFAULT CURRENT_DATE
);

-- Fremdschluessel
CREATE TABLE bestellungen (
    id INT PRIMARY KEY AUTO_INCREMENT,
    kunden_id INT NOT NULL,
    datum DATE NOT NULL,
    betrag DECIMAL(10,2),
    FOREIGN KEY (kunden_id) REFERENCES kunden(id)
);

-- ALTER TABLE: Spalte hinzufuegen
ALTER TABLE kunden ADD email VARCHAR(100);

-- ALTER TABLE: Spalte aendern
ALTER TABLE kunden MODIFY email VARCHAR(150) NOT NULL;

-- ALTER TABLE: Spalte loeschen
ALTER TABLE kunden DROP COLUMN email;

-- DROP TABLE: Tabelle loeschen
DROP TABLE bestellungen;
```

**Wichtige Constraints:**

| Constraint | Bedeutung |
|-----------|-----------|
| PRIMARY KEY | Eindeutiger Identifikator, darf nicht NULL sein |
| FOREIGN KEY | Verweis auf Primaerschluessel einer anderen Tabelle |
| NOT NULL | Wert darf nicht leer sein |
| UNIQUE | Wert muss einmalig sein |
| DEFAULT | Standardwert, wenn keiner angegeben wird |
| CHECK | Bedingung, die der Wert erfuellen muss |

---

## Index (CREATE INDEX)

**Definition:** Ein Index beschleunigt Abfragen auf bestimmte Spalten, verlangsamt aber INSERT/UPDATE/DELETE, da der Index mitgepflegt werden muss.

```sql
-- Index erstellen
CREATE INDEX idx_kunden_stadt ON kunden(stadt);

-- Zusammengesetzter Index
CREATE INDEX idx_best_datum_betrag ON bestellungen(datum, betrag);

-- Eindeutiger Index
CREATE UNIQUE INDEX idx_kunden_name ON kunden(name);

-- Index loeschen
DROP INDEX idx_kunden_stadt;
```

**Wann Index erstellen?**

| Index sinnvoll | Index nicht sinnvoll |
|---------------|---------------------|
| Spalte wird oft in WHERE verwendet | Kleine Tabellen (< 1000 Zeilen) |
| Spalte wird oft in JOIN-Bedingungen verwendet | Spalte wird selten abgefragt |
| Spalte wird oft in ORDER BY verwendet | Spalte aendert sich sehr haeufig |
| Spalte hat viele verschiedene Werte | Spalte hat wenige verschiedene Werte (z.B. ja/nein) |
