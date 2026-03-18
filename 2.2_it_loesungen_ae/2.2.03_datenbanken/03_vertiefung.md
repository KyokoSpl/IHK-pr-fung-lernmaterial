# Vertiefung: 2.2.03 – Datenbanken modellieren und erstellen

## Zusammenhang der Themenkreise

```
Anforderungsanalyse
        |
        v
+----------------+     +------------------+
| ER-Modell      |---->| Relationales     |
| (konzeptionell)|     | Modell (logisch) |
+----------------+     +------------------+
                              |
                    +---------+---------+
                    |                   |
              +----------+        +-----------+
              | Normali- |        | SQL (DDL) |
              | sierung  |        | CREATE    |
              | 1NF-3NF  |        | TABLE     |
              +----------+        +-----------+
                    |                   |
                    v                   v
              Redundanzfreies     Physische
              Datenmodell         Datenbank
                                       |
                              +--------+--------+
                              |                 |
                        +---------+       +-----------+
                        | DML     |       | DQL       |
                        | INSERT  |       | SELECT    |
                        | UPDATE  |       | JOIN      |
                        | DELETE  |       | GROUP BY  |
                        +---------+       +-----------+
```

## Normalisierung: Durchgaengiges Beispiel

### Unnormalisiert:

| BestellNr | Datum | KundenName | KundenOrt | Artikel | Preis |
|---|---|---|---|---|---|
| 1001 | 2024-01-15 | Mueller GmbH | Berlin | Server, Switch | 5000, 500 |
| 1002 | 2024-01-20 | Mueller GmbH | Berlin | Kabel | 50 |

**Probleme:** Mehrere Werte in einer Zelle, Redundanz (KundenName/Ort).

### 1NF (atomar):

| BestellNr | Datum | KundenName | KundenOrt | Artikel | Preis |
|---|---|---|---|---|---|
| 1001 | 2024-01-15 | Mueller GmbH | Berlin | Server | 5000 |
| 1001 | 2024-01-15 | Mueller GmbH | Berlin | Switch | 500 |
| 1002 | 2024-01-20 | Mueller GmbH | Berlin | Kabel | 50 |

### 2NF (volle Abhaengigkeit vom PK):
PK ist {BestellNr, Artikel}. KundenName/Ort haengen nur von BestellNr ab → auslagern.

**Bestellung:** BestellNr, Datum, KundenName, KundenOrt
**BestellPosition:** BestellNr, Artikel, Preis

### 3NF (keine transitiven Abhaengigkeiten):
KundenOrt haengt von KundenName ab (transitiv) → auslagern.

**Kunde:** KundenID, KundenName, KundenOrt
**Bestellung:** BestellNr, Datum, KundenID (FK)
**BestellPosition:** BestellNr (FK), Artikel, Preis

## Referenzielle Integritaet

**Definition:** Fremdschluessel muessen immer auf einen existierenden Primaerschluessel verweisen.

| Aktion | Beschreibung |
|---|---|
| ON DELETE CASCADE | Loeschen des Elterndatensatzes → Kinddatensaetze auch geloescht |
| ON DELETE SET NULL | Loeschen → Fremdschluessel auf NULL setzen |
| ON DELETE RESTRICT | Loeschen verhindern, wenn Kinddatensaetze existieren |
| ON UPDATE CASCADE | PK-Aenderung wird an FK weitergegeben |

## Typische Pruefungsaspekte

- ER-Modell aus Sachtext ableiten
- n:m-Beziehung in Tabellen aufloesen
- Normalformen erkennen und herstellen
- SQL-Abfragen mit JOIN und GROUP BY schreiben
- ACID vs. BASE erklaeren
- Datentyp fuer ein Attribut waehlen

## Haeufige Fehler in Pruefungen

| Fehler | Richtig |
|---|---|
| n:m-Beziehung ohne Zwischentabelle | Immer aufloesen mit eigener Tabelle |
| GROUP BY vergessen bei Aggregatfunktionen | SELECT mit COUNT/SUM braucht GROUP BY |
| HAVING und WHERE verwechselt | WHERE = vor Gruppierung, HAVING = nach Gruppierung |
| FLOAT fuer Geldbetraege | DECIMAL verwenden (exakt) |
| JOIN ohne ON-Bedingung | Ergibt kartesisches Produkt = falsch |
