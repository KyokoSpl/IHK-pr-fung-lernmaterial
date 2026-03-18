# Uebungen: 3.4.22 – Datenbankabfrage, Datenpflege mit SQL

## Uebungsdatenbank

Alle Aufgaben beziehen sich auf folgende Tabellen:

```
Tabelle: kunden
+----+------------------+----------+--------+
| id | firma            | stadt    | typ    |
+----+------------------+----------+--------+
|  1 | Mueller GmbH     | Berlin   | Premium|
|  2 | Schmidt AG       | Hamburg  | Normal |
|  3 | Weber IT         | Berlin   | Premium|
|  4 | Fischer KG       | Muenchen | Normal |
|  5 | Braun Systems    | Hamburg  | Premium|
+----+------------------+----------+--------+

Tabelle: bestellungen
+----+-----------+------------+---------+
| id | kunden_id | datum      | betrag  |
+----+-----------+------------+---------+
|  1 |         1 | 2025-01-15 |  500.00 |
|  2 |         1 | 2025-03-22 |  750.00 |
|  3 |         2 | 2025-02-10 |  200.00 |
|  4 |         3 | 2025-04-05 | 1200.00 |
|  5 |         3 | 2025-05-18 |  300.00 |
|  6 |         5 | 2025-06-01 |  980.00 |
+----+-----------+------------+---------+

Tabelle: artikel
+----+------------------+--------+----------+
| id | bezeichnung      | preis  | kategorie|
+----+------------------+--------+----------+
|  1 | Laptop           | 899.99 | Hardware |
|  2 | Maus             |  29.99 | Zubehoer |
|  3 | Monitor          | 349.00 | Hardware |
|  4 | USB-Kabel        |   9.99 | Zubehoer |
|  5 | Tastatur         |  59.99 | Zubehoer |
|  6 | SSD 1TB          | 129.99 | Hardware |
+----+------------------+--------+----------+
```

---

## Projektion und Selektion

**Aufgabe 1:** Schreibe eine SQL-Abfrage, die alle Firmennamen und Staedte der Kunden anzeigt.

**Aufgabe 2:** Zeige alle Artikel mit einem Preis ueber 50 EUR, sortiert nach Preis absteigend.

**Aufgabe 3:** Finde alle Kunden aus Berlin oder Hamburg.

**Aufgabe 4:** Zeige alle Artikel, deren Bezeichnung mit "M" beginnt.

---

## Aggregatfunktionen und Gruppierung

**Aufgabe 5:** Ermittle die Anzahl der Artikel pro Kategorie.

**Aufgabe 6:** Berechne den Gesamtumsatz (Summe aller Betraege) aller Bestellungen.

**Aufgabe 7:** Zeige fuer jeden Kunden (kunden_id) die Anzahl der Bestellungen und den Gesamtumsatz. Nur Kunden mit einem Gesamtumsatz ueber 500 EUR sollen angezeigt werden.

**Aufgabe 8:** Berechne den durchschnittlichen Bestellbetrag pro Stadt.

---

## JOINs

**Aufgabe 9:** Zeige den Firmennamen, das Bestelldatum und den Betrag fuer alle Bestellungen (INNER JOIN).

**Aufgabe 10:** Zeige ALLE Kunden mit ihren Bestellungen. Kunden ohne Bestellungen sollen ebenfalls angezeigt werden.

**Aufgabe 11:** Finde alle Kunden, die noch nie bestellt haben.

---

## Subqueries

**Aufgabe 12:** Zeige alle Kunden, deren Bestellungen einen hoeheren Betrag haben als der Durchschnitt aller Bestellungen.

**Aufgabe 13:** Finde den Artikel mit dem hoechsten Preis (verwende eine Subquery).

---

## DML

**Aufgabe 14:** Fuege einen neuen Kunden "Neumann Ltd" aus Koeln, Typ "Normal" ein.

**Aufgabe 15:** Erhoehe den Preis aller Artikel in der Kategorie "Hardware" um 10%.

**Aufgabe 16:** Loesche alle Bestellungen mit einem Betrag unter 250 EUR.

---

## DDL

**Aufgabe 17:** Erstelle die Tabelle `bestellpositionen` mit folgenden Spalten:
- `id` (Ganzzahl, Primaerschluessel, auto increment)
- `bestell_id` (Ganzzahl, Fremdschluessel auf bestellungen.id, NOT NULL)
- `artikel_id` (Ganzzahl, Fremdschluessel auf artikel.id, NOT NULL)
- `menge` (Ganzzahl, Standard 1, muss groesser als 0 sein)

**Aufgabe 18:** Fuege der Tabelle `kunden` eine neue Spalte `email` (VARCHAR 100) hinzu.

**Aufgabe 19:** Erstelle einen Index auf die Spalte `datum` der Tabelle `bestellungen`.

---

## Komplexe Aufgaben (Pruefungsniveau)

**Aufgabe 20:** Schreibe eine Abfrage, die fuer jeden Premium-Kunden den Firmennamen, die Anzahl der Bestellungen und den Gesamtumsatz anzeigt, sortiert nach Gesamtumsatz absteigend.

**Aufgabe 21:** Zeige alle Staedte, in denen der durchschnittliche Bestellbetrag ueber 500 EUR liegt.

**Aufgabe 22:** Erstelle eine Abfrage, die den Firmennamen und den Betrag der jeweils hoechsten Bestellung pro Kunde anzeigt.

---
---

# Loesungen

## Aufgabe 1

```sql
SELECT firma, stadt FROM kunden;
```

## Aufgabe 2

```sql
SELECT bezeichnung, preis
FROM artikel
WHERE preis > 50
ORDER BY preis DESC;
```

Ergebnis: Laptop (899.99), Monitor (349.00), SSD 1TB (129.99), Tastatur (59.99)

## Aufgabe 3

```sql
SELECT * FROM kunden
WHERE stadt IN ('Berlin', 'Hamburg');
```

Alternativ: `WHERE stadt = 'Berlin' OR stadt = 'Hamburg'`

## Aufgabe 4

```sql
SELECT * FROM artikel
WHERE bezeichnung LIKE 'M%';
```

Ergebnis: Maus, Monitor

## Aufgabe 5

```sql
SELECT kategorie, COUNT(*) AS anzahl
FROM artikel
GROUP BY kategorie;
```

Ergebnis: Hardware: 3, Zubehoer: 3

## Aufgabe 6

```sql
SELECT SUM(betrag) AS gesamtumsatz FROM bestellungen;
```

Ergebnis: 3930.00

## Aufgabe 7

```sql
SELECT kunden_id, COUNT(*) AS anzahl, SUM(betrag) AS umsatz
FROM bestellungen
GROUP BY kunden_id
HAVING SUM(betrag) > 500;
```

Ergebnis:
```
| kunden_id | anzahl | umsatz  |
|         1 |      2 | 1250.00 |
|         3 |      2 | 1500.00 |
|         5 |      1 |  980.00 |
```

## Aufgabe 8

```sql
SELECT k.stadt, AVG(b.betrag) AS avg_betrag
FROM kunden k
INNER JOIN bestellungen b ON k.id = b.kunden_id
GROUP BY k.stadt;
```

Ergebnis:
```
| stadt   | avg_betrag |
| Berlin  |     687.50 |  (500+750+1200+300) / 4
| Hamburg  |     590.00 |  (200+980) / 2
```

## Aufgabe 9

```sql
SELECT k.firma, b.datum, b.betrag
FROM kunden k
INNER JOIN bestellungen b ON k.id = b.kunden_id;
```

## Aufgabe 10

```sql
SELECT k.firma, b.datum, b.betrag
FROM kunden k
LEFT JOIN bestellungen b ON k.id = b.kunden_id;
```

→ Fischer KG erscheint mit NULL bei datum und betrag.

## Aufgabe 11

```sql
SELECT k.firma
FROM kunden k
LEFT JOIN bestellungen b ON k.id = b.kunden_id
WHERE b.id IS NULL;
```

Ergebnis: Fischer KG

## Aufgabe 12

```sql
SELECT DISTINCT k.firma
FROM kunden k
INNER JOIN bestellungen b ON k.id = b.kunden_id
WHERE b.betrag > (SELECT AVG(betrag) FROM bestellungen);
```

Durchschnitt: 3930/6 = 655. Ergebnis: Mueller GmbH (750), Weber IT (1200), Braun Systems (980).

## Aufgabe 13

```sql
SELECT * FROM artikel
WHERE preis = (SELECT MAX(preis) FROM artikel);
```

Ergebnis: Laptop (899.99)

## Aufgabe 14

```sql
INSERT INTO kunden (firma, stadt, typ)
VALUES ('Neumann Ltd', 'Koeln', 'Normal');
```

## Aufgabe 15

```sql
UPDATE artikel
SET preis = preis * 1.10
WHERE kategorie = 'Hardware';
```

→ Laptop: 989.99, Monitor: 383.90, SSD: 142.99

## Aufgabe 16

```sql
DELETE FROM bestellungen
WHERE betrag < 250;
```

→ Loescht Bestellung id=3 (200.00).

## Aufgabe 17

```sql
CREATE TABLE bestellpositionen (
    id INT PRIMARY KEY AUTO_INCREMENT,
    bestell_id INT NOT NULL,
    artikel_id INT NOT NULL,
    menge INT DEFAULT 1,
    FOREIGN KEY (bestell_id) REFERENCES bestellungen(id),
    FOREIGN KEY (artikel_id) REFERENCES artikel(id),
    CHECK (menge > 0)
);
```

## Aufgabe 18

```sql
ALTER TABLE kunden ADD email VARCHAR(100);
```

## Aufgabe 19

```sql
CREATE INDEX idx_bestellungen_datum ON bestellungen(datum);
```

## Aufgabe 20

```sql
SELECT k.firma,
       COUNT(b.id) AS anzahl_bestellungen,
       SUM(b.betrag) AS gesamtumsatz
FROM kunden k
INNER JOIN bestellungen b ON k.id = b.kunden_id
WHERE k.typ = 'Premium'
GROUP BY k.firma
ORDER BY gesamtumsatz DESC;
```

Ergebnis:
```
| firma          | anzahl_bestellungen | gesamtumsatz |
| Weber IT       |                   2 |      1500.00 |
| Mueller GmbH   |                   2 |      1250.00 |
| Braun Systems  |                   1 |       980.00 |
```

## Aufgabe 21

```sql
SELECT k.stadt, AVG(b.betrag) AS avg_betrag
FROM kunden k
INNER JOIN bestellungen b ON k.id = b.kunden_id
GROUP BY k.stadt
HAVING AVG(b.betrag) > 500;
```

Ergebnis: Berlin (687.50), Hamburg (590.00)

## Aufgabe 22

```sql
SELECT k.firma, MAX(b.betrag) AS max_betrag
FROM kunden k
INNER JOIN bestellungen b ON k.id = b.kunden_id
GROUP BY k.firma;
```

Ergebnis:
```
| firma          | max_betrag |
| Mueller GmbH   |     750.00 |
| Schmidt AG     |     200.00 |
| Weber IT       |    1200.00 |
| Braun Systems  |     980.00 |
```
