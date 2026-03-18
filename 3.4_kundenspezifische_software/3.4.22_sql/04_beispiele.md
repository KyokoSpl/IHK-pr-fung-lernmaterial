# Beispiele: 3.4.22 – Datenbankabfrage, Datenpflege mit SQL

## Beispiel-Datenbank

Alle Abfragen beziehen sich auf folgende Tabellen:

```
Tabelle: mitarbeiter
+----+----------+-----------+--------+----------+
| id | vorname  | nachname  | gehalt | abt_id   |
+----+----------+-----------+--------+----------+
|  1 | Anna     | Mueller   | 4200   |        1 |
|  2 | Ben      | Schmidt   | 3800   |        2 |
|  3 | Clara    | Weber     | 4500   |        1 |
|  4 | David    | Fischer   | 3600   |        3 |
|  5 | Eva      | Braun     | 5000   |        2 |
|  6 | Frank    | Meier     | 3900   |     NULL |
+----+----------+-----------+--------+----------+

Tabelle: abteilungen
+----+------------------+
| id | bezeichnung      |
+----+------------------+
|  1 | Entwicklung      |
|  2 | Vertrieb         |
|  3 | Support          |
|  4 | Marketing        |
+----+------------------+

Tabelle: projekte
+----+---------------+-----------+------------+
| id | name          | leiter_id | budget     |
+----+---------------+-----------+------------+
|  1 | Webshop 2.0   |         1 | 50000.00   |
|  2 | CRM-Migration |         3 | 30000.00   |
|  3 | App-Release   |         5 | 75000.00   |
+----+---------------+-----------+------------+
```

---

## Projektion und Selektion

**Beispiel 1: Einfache Projektion**

```sql
SELECT vorname, nachname FROM mitarbeiter;
```

Ergebnis:
```
| vorname | nachname |
| Anna    | Mueller  |
| Ben     | Schmidt  |
| Clara   | Weber    |
| David   | Fischer  |
| Eva     | Braun    |
| Frank   | Meier    |
```

**Beispiel 2: Selektion mit Bedingung**

```sql
SELECT vorname, nachname, gehalt
FROM mitarbeiter
WHERE gehalt > 4000;
```

Ergebnis:
```
| vorname | nachname | gehalt |
| Anna    | Mueller  | 4200   |
| Clara   | Weber    | 4500   |
| Eva     | Braun    | 5000   |
```

**Beispiel 3: Berechnete Spalte**

```sql
SELECT vorname, nachname, gehalt, gehalt * 12 AS jahresgehalt
FROM mitarbeiter
WHERE gehalt BETWEEN 3800 AND 4500
ORDER BY gehalt DESC;
```

Ergebnis:
```
| vorname | nachname | gehalt | jahresgehalt |
| Clara   | Weber    | 4500   | 54000        |
| Anna    | Mueller  | 4200   | 50400        |
| Ben     | Schmidt  | 3800   | 45600        |
```

---

## Aggregatfunktionen und Gruppierung

**Beispiel 4: Aggregatfunktionen**

```sql
SELECT COUNT(*) AS anzahl,
       AVG(gehalt) AS durchschnitt,
       MIN(gehalt) AS minimum,
       MAX(gehalt) AS maximum,
       SUM(gehalt) AS gesamtgehalt
FROM mitarbeiter;
```

Ergebnis:
```
| anzahl | durchschnitt | minimum | maximum | gesamtgehalt |
|      6 |      4166.67 |    3600 |    5000 |        25000 |
```

**Beispiel 5: GROUP BY mit HAVING**

```sql
SELECT a.bezeichnung, COUNT(*) AS mitarbeiter_anzahl, AVG(m.gehalt) AS avg_gehalt
FROM mitarbeiter m
INNER JOIN abteilungen a ON m.abt_id = a.id
GROUP BY a.bezeichnung
HAVING COUNT(*) > 1;
```

Ergebnis:
```
| bezeichnung | mitarbeiter_anzahl | avg_gehalt |
| Entwicklung |                  2 |    4350.00 |
| Vertrieb    |                  2 |    4400.00 |
```

→ Support (1 Mitarbeiter) faellt durch HAVING raus. Frank (NULL abt_id) faellt durch INNER JOIN raus. Marketing (0 Mitarbeiter) faellt durch INNER JOIN raus.

---

## JOINs

**Beispiel 6: INNER JOIN**

```sql
SELECT m.vorname, m.nachname, a.bezeichnung
FROM mitarbeiter m
INNER JOIN abteilungen a ON m.abt_id = a.id;
```

Ergebnis:
```
| vorname | nachname | bezeichnung |
| Anna    | Mueller  | Entwicklung |
| Ben     | Schmidt  | Vertrieb    |
| Clara   | Weber    | Entwicklung |
| David   | Fischer  | Support     |
| Eva     | Braun    | Vertrieb    |
```

→ Frank fehlt (abt_id ist NULL → kein Match).

**Beispiel 7: LEFT JOIN**

```sql
SELECT m.vorname, m.nachname, a.bezeichnung
FROM mitarbeiter m
LEFT JOIN abteilungen a ON m.abt_id = a.id;
```

Ergebnis:
```
| vorname | nachname | bezeichnung |
| Anna    | Mueller  | Entwicklung |
| Ben     | Schmidt  | Vertrieb    |
| Clara   | Weber    | Entwicklung |
| David   | Fischer  | Support     |
| Eva     | Braun    | Vertrieb    |
| Frank   | Meier    | NULL        |
```

→ Frank ist jetzt dabei, mit NULL bei bezeichnung.

**Beispiel 8: LEFT JOIN – Abteilungen ohne Mitarbeiter finden**

```sql
SELECT a.bezeichnung
FROM abteilungen a
LEFT JOIN mitarbeiter m ON a.id = m.abt_id
WHERE m.id IS NULL;
```

Ergebnis:
```
| bezeichnung |
| Marketing   |
```

→ Marketing hat keine zugeordneten Mitarbeiter.

---

## Subqueries

**Beispiel 9: Mitarbeiter mit ueberdurchschnittlichem Gehalt**

```sql
SELECT vorname, nachname, gehalt
FROM mitarbeiter
WHERE gehalt > (SELECT AVG(gehalt) FROM mitarbeiter);
```

Ergebnis:
```
| vorname | nachname | gehalt |
| Anna    | Mueller  | 4200   |
| Clara   | Weber    | 4500   |
| Eva     | Braun    | 5000   |
```

→ Durchschnitt ist 4166.67, alle drei liegen darueber.

**Beispiel 10: Subquery mit IN**

```sql
-- Mitarbeiter, die Projektleiter sind
SELECT vorname, nachname
FROM mitarbeiter
WHERE id IN (SELECT leiter_id FROM projekte);
```

Ergebnis:
```
| vorname | nachname |
| Anna    | Mueller  |
| Clara   | Weber    |
| Eva     | Braun    |
```

---

## DML: INSERT, UPDATE, DELETE

**Beispiel 11: INSERT**

```sql
INSERT INTO mitarbeiter (vorname, nachname, gehalt, abt_id)
VALUES ('Greta', 'Hoffmann', 4100, 3);
```

**Beispiel 12: UPDATE**

```sql
-- Gehalterhoehung fuer alle in der Entwicklung (abt_id = 1)
UPDATE mitarbeiter
SET gehalt = gehalt * 1.05
WHERE abt_id = 1;
```

→ Anna: 4200 × 1.05 = 4410, Clara: 4500 × 1.05 = 4725.

**Beispiel 13: DELETE**

```sql
-- Mitarbeiter ohne Abteilung entfernen
DELETE FROM mitarbeiter
WHERE abt_id IS NULL;
```

→ Frank wird geloescht.

---

## DDL: CREATE TABLE

**Beispiel 14: Komplette Tabellenerstellung**

```sql
CREATE TABLE projekte (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    leiter_id INT,
    budget DECIMAL(12,2) DEFAULT 0,
    start_datum DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'Geplant',
    FOREIGN KEY (leiter_id) REFERENCES mitarbeiter(id),
    CHECK (budget >= 0)
);
```

**Beispiel 15: ALTER TABLE**

```sql
-- Neue Spalte hinzufuegen
ALTER TABLE mitarbeiter ADD eintrittsdatum DATE;

-- Spalte umbenennen (MySQL-Syntax)
ALTER TABLE mitarbeiter CHANGE gehalt monatsgehalt DECIMAL(10,2);

-- Constraint hinzufuegen
ALTER TABLE mitarbeiter ADD CONSTRAINT chk_gehalt CHECK (monatsgehalt > 0);
```

---

## Index

**Beispiel 16: Index fuer haeufige Abfragen**

```sql
-- Mitarbeiter werden oft nach Nachname gesucht
CREATE INDEX idx_mitarbeiter_nachname ON mitarbeiter(nachname);

-- Bestellungen werden oft nach Datum gefiltert
CREATE INDEX idx_bestellungen_datum ON bestellungen(datum);

-- Zusammengesetzter Index fuer kombinierte Abfragen
CREATE INDEX idx_ma_abt_gehalt ON mitarbeiter(abt_id, gehalt);
```
