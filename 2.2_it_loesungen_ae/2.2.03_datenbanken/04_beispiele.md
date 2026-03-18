# Beispiele: 2.2.03 – Datenbanken modellieren und erstellen

## Beispiel 1: ER-Modell → Relationales Modell

**Sachtext:** Ein IT-Dienstleister verwaltet Projekte. Jedes Projekt hat eine Nummer, einen Namen und ein Budget. Mitarbeiter haben eine PersonalNr und einen Namen. Ein Mitarbeiter kann an mehreren Projekten arbeiten, ein Projekt hat mehrere Mitarbeiter. Fuer jede Zuordnung wird die Rolle (z.B. Entwickler, Tester) festgehalten.

**ER-Modell:**
```
+------------+     n:m      +------------+
| Mitarbeiter|----arbeitet--| Projekt    |
+------------+   an (Rolle) +------------+
| PNr (PK)   |              | ProjNr (PK)|
| Name        |              | Name       |
+------------+              | Budget     |
                             +------------+
```

**Relationales Modell (3NF):**
```sql
CREATE TABLE Mitarbeiter (
    PNr INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL
);

CREATE TABLE Projekt (
    ProjNr INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Budget DECIMAL(12,2)
);

CREATE TABLE ProjektMitarbeiter (
    PNr INT,
    ProjNr INT,
    Rolle VARCHAR(50),
    PRIMARY KEY (PNr, ProjNr),
    FOREIGN KEY (PNr) REFERENCES Mitarbeiter(PNr),
    FOREIGN KEY (ProjNr) REFERENCES Projekt(ProjNr)
);
```

---

## Beispiel 2: SQL-Abfragen

**Tabellen:** Kunde(KID, Name, Ort), Bestellung(BID, KID, Datum, Betrag)

```sql
-- Alle Bestellungen eines Kunden mit Name
SELECT k.Name, b.BID, b.Datum, b.Betrag
FROM Kunde k
INNER JOIN Bestellung b ON k.KID = b.KID
WHERE k.Name = 'Mueller GmbH';

-- Gesamtumsatz pro Kunde, absteigend sortiert
SELECT k.Name, SUM(b.Betrag) AS Gesamtumsatz
FROM Kunde k
INNER JOIN Bestellung b ON k.KID = b.KID
GROUP BY k.Name
ORDER BY Gesamtumsatz DESC;

-- Kunden mit mehr als 5 Bestellungen
SELECT k.Name, COUNT(*) AS AnzahlBestellungen
FROM Kunde k
INNER JOIN Bestellung b ON k.KID = b.KID
GROUP BY k.Name
HAVING COUNT(*) > 5;

-- Kunden OHNE Bestellung (LEFT JOIN)
SELECT k.Name
FROM Kunde k
LEFT JOIN Bestellung b ON k.KID = b.KID
WHERE b.BID IS NULL;
```

---

## Beispiel 3: Normalisierung

**Ausgangstabelle (unnormalisiert):**

| MitarbeiterNr | Name | AbtNr | AbtName | Projekte |
|---|---|---|---|---|
| 101 | Mueller | 10 | Entwicklung | P1, P3 |
| 102 | Schmidt | 10 | Entwicklung | P2 |
| 103 | Weber | 20 | Support | P1, P2 |

**→ 1NF:** Projekte atomar machen.
**→ 2NF:** Projekt-Zuordnung in eigene Tabelle.
**→ 3NF:** AbtName haengt von AbtNr ab → eigene Tabelle.

**Ergebnis:**
- **Abteilung**(AbtNr, AbtName)
- **Mitarbeiter**(MitarbeiterNr, Name, AbtNr FK)
- **MitarbeiterProjekt**(MitarbeiterNr FK, ProjektNr FK)

---

## Beispiel 4: REST-API mit JSON

**GET /api/kunden/42 → Antwort:**
```json
{
    "kundenId": 42,
    "name": "Mueller GmbH",
    "ort": "Berlin",
    "bestellungen": [
        {"bestId": 1001, "datum": "2024-01-15", "betrag": 5500.00},
        {"bestId": 1002, "datum": "2024-01-20", "betrag": 50.00}
    ]
}
```

**POST /api/kunden → Neuen Kunden anlegen:**
```json
{
    "name": "Schmidt AG",
    "ort": "Hamburg"
}
```
