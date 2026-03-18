# Vertiefung: 3.4.22 – Datenbankabfrage, Datenpflege mit SQL

## SQL-Abfragereihenfolge (Ausfuehrung vs. Schreibweise)

**Schreibreihenfolge:**
```
SELECT → FROM → JOIN → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT
```

**Ausfuehrungsreihenfolge (intern):**
```
1. FROM / JOIN    → Tabellen laden und verknuepfen
2. WHERE          → Zeilen filtern
3. GROUP BY       → Gruppieren
4. HAVING         → Gruppen filtern
5. SELECT         → Spalten auswaehlen
6. DISTINCT       → Duplikate entfernen
7. ORDER BY       → Sortieren
8. LIMIT          → Ergebnismenge begrenzen
```

→ Deswegen kann HAVING auf Aggregatfunktionen zugreifen, WHERE aber nicht.

---

## JOIN-Vertiefung

### Mehrfach-JOIN

```sql
-- Drei Tabellen verknuepfen (Annahme: Tabelle bestellpositionen existiert)
-- bestellpositionen: id, bestell_id, artikel_id, menge
SELECT k.name, b.datum, a.bezeichnung, bp.menge
FROM kunden k
INNER JOIN bestellungen b ON k.id = b.kunden_id
INNER JOIN bestellpositionen bp ON b.id = bp.bestell_id
INNER JOIN artikel a ON bp.artikel_id = a.id
WHERE k.stadt = 'Berlin';
```

### Self-JOIN

```sql
-- Mitarbeiter und ihre Vorgesetzten (gleiche Tabelle)
-- mitarbeiter: id, name, vorgesetzter_id
SELECT m.name AS mitarbeiter, v.name AS vorgesetzter
FROM mitarbeiter m
LEFT JOIN mitarbeiter v ON m.vorgesetzter_id = v.id;
```

### LEFT JOIN: Datensaetze OHNE Verknuepfung finden

```sql
-- Kunden, die noch NIE bestellt haben
SELECT k.name
FROM kunden k
LEFT JOIN bestellungen b ON k.id = b.kunden_id
WHERE b.id IS NULL;
```

---

## Subqueries – Vertiefung

### Korrelierte Subquery

```sql
-- Kunden, deren Bestellsumme ueber dem Durchschnitt liegt
SELECT name
FROM kunden k
WHERE (SELECT SUM(betrag) FROM bestellungen b WHERE b.kunden_id = k.id)
      > (SELECT AVG(betrag) FROM bestellungen);
```

### Subquery im SELECT

```sql
-- Kundenname mit Anzahl Bestellungen
SELECT name,
       (SELECT COUNT(*) FROM bestellungen b WHERE b.kunden_id = k.id) AS anzahl
FROM kunden k;
```

### Subquery im FROM (Derived Table)

```sql
-- Durchschnittlicher Umsatz pro Kunde ermitteln
SELECT AVG(kundenumsatz) AS durchschnitt
FROM (
    SELECT kunden_id, SUM(betrag) AS kundenumsatz
    FROM bestellungen
    GROUP BY kunden_id
) AS umsatzTabelle;
```

---

## DDL-Vertiefung: Datentypen

| Datentyp | Beschreibung | Beispiel |
|----------|-------------|----------|
| INT / INTEGER | Ganzzahl | `42` |
| DECIMAL(p,s) | Festkommazahl (p Stellen, s Nachkomma) | `DECIMAL(10,2)` → 12345678.90 |
| FLOAT / DOUBLE | Gleitkommazahl | `3.14` |
| VARCHAR(n) | Variable Zeichenkette (max. n Zeichen) | `VARCHAR(100)` |
| CHAR(n) | Feste Zeichenkette (genau n Zeichen) | `CHAR(5)` |
| TEXT | Langer Text | Beschreibungstexte |
| DATE | Datum | `2025-03-17` |
| DATETIME / TIMESTAMP | Datum + Uhrzeit | `2025-03-17 14:30:00` |
| BOOLEAN | Wahrheitswert | `TRUE`, `FALSE` |

---

## Index-Vertiefung

### Wie funktioniert ein Index?

```
Ohne Index:                     Mit Index auf 'stadt':
+----+----------+               Index (B-Baum):
|  1 | Berlin   |                    Hamburg
|  2 | Hamburg  |                   /       \
|  3 | Berlin   |              Berlin      Muenchen
|  4 | Muenchen |               |  |          |
+----+----------+              [1] [3]        [4]

Suche nach 'Berlin':           Suche nach 'Berlin':
→ Alle 4 Zeilen pruefen        → Index → direkt Zeile 1, 3
  (Full Table Scan)               (Index Scan)
```

### Index und Performance

| Operation | Ohne Index | Mit Index |
|-----------|-----------|-----------|
| SELECT mit WHERE | Langsam (Full Scan) | Schnell (Index Scan) |
| INSERT | Schnell | Etwas langsamer (Index aktualisieren) |
| UPDATE | Schnell | Etwas langsamer (Index aktualisieren) |
| DELETE | Schnell | Etwas langsamer (Index aktualisieren) |

→ Indizes beschleunigen Lesezugriffe, verlangsamen aber Schreibzugriffe.

---

## SQL-Referenzkarte

### DQL (SELECT)

```sql
-- Grundstruktur
SELECT [DISTINCT] spalte1, spalte2, ...
FROM tabelle
[JOIN andere_tabelle ON bedingung]
[WHERE bedingung]
[GROUP BY spalte]
[HAVING bedingung]
[ORDER BY spalte [ASC|DESC]]
[LIMIT anzahl];
```

### DML (INSERT, UPDATE, DELETE)

```sql
INSERT INTO tabelle (spalte1, spalte2) VALUES (wert1, wert2);
UPDATE tabelle SET spalte1 = wert1 WHERE bedingung;
DELETE FROM tabelle WHERE bedingung;
```

### DDL (CREATE, ALTER, DROP)

```sql
CREATE TABLE tabelle (spalte1 TYP [CONSTRAINT], ...);
ALTER TABLE tabelle ADD spalte TYP;
ALTER TABLE tabelle MODIFY spalte TYP;
ALTER TABLE tabelle DROP COLUMN spalte;
DROP TABLE tabelle;
CREATE INDEX indexname ON tabelle(spalte);
```

---

## Typische Pruefungsaspekte
- SELECT-Abfragen mit JOIN, WHERE, GROUP BY, HAVING, ORDER BY schreiben
- Subqueries verstehen und schreiben
- Unterschied WHERE vs. HAVING erklaeren
- JOIN-Typen unterscheiden (INNER, LEFT, RIGHT)
- DDL: CREATE TABLE mit Primaer-/Fremdschluessel und Constraints
- INSERT/UPDATE/DELETE korrekt anwenden
- Index: Wann sinnvoll, Vor- und Nachteile
- Ergebnis einer SQL-Abfrage anhand einer gegebenen Tabelle bestimmen

## Haeufige Fehler
- WHERE statt HAVING fuer Aggregatfunktionen: `WHERE COUNT(*) > 3` → falsch! Muss HAVING sein
- DELETE/UPDATE ohne WHERE → loescht/aendert ALLE Zeilen
- LEFT JOIN: NULL-Werte in der Ergebnismenge werden nicht beruecksichtigt
- GROUP BY vergessen, wenn Aggregatfunktionen mit nicht-aggregierten Spalten gemischt werden
- LIKE: `_` ist EIN Zeichen, `%` sind beliebig viele – wird verwechselt
- Fremdschluessel auf nicht-existierenden Primaerschluessel → referenzielle Integritaetsverletzung
- Aliase: `AS` vergessen kann zu unlesbaren Fehlermeldungen fuehren
