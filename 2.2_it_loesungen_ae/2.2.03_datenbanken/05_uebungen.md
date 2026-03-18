# Uebungen: 2.2.03 – Datenbanken modellieren und erstellen

## Aufgabe 1: Normalformen erkennen
In welcher Normalform befindet sich die folgende Tabelle? Begruende und normalisiere bis zur 3NF.

| BestellNr | KundenNr | KundenName | KundenOrt | ArtikelNr | ArtikelName | Menge | Einzelpreis |
|---|---|---|---|---|---|---|---|
| 1001 | K01 | Mueller | Berlin | A10 | Server | 1 | 5000 |
| 1001 | K01 | Mueller | Berlin | A20 | Switch | 2 | 500 |
| 1002 | K02 | Schmidt | Hamburg | A10 | Server | 1 | 5000 |

---
---

**Loesung Aufgabe 1:**
Die Tabelle ist in **1NF** (alle Werte atomar, keine Wiederholungsgruppen).
Nicht in 2NF: PK = {BestellNr, ArtikelNr}. KundenNr/Name/Ort haengen nur von BestellNr ab (nicht vom ganzen PK).

**2NF:**
- **Bestellung**(BestellNr, KundenNr, KundenName, KundenOrt)
- **BestellPosition**(BestellNr, ArtikelNr, ArtikelName, Menge, Einzelpreis)

Nicht in 3NF: KundenName/Ort haengen transitiv von KundenNr ab. ArtikelName haengt transitiv von ArtikelNr ab.

**3NF:**
- **Kunde**(KundenNr, KundenName, KundenOrt)
- **Artikel**(ArtikelNr, ArtikelName, Einzelpreis)
- **Bestellung**(BestellNr, KundenNr FK)
- **BestellPosition**(BestellNr FK, ArtikelNr FK, Menge)

---

## Aufgabe 2: SQL-Abfragen schreiben
Gegeben: Tabelle **Mitarbeiter**(MID, Name, AbtID, Gehalt) und **Abteilung**(AbtID, AbtName)

a) Zeige alle Mitarbeiter der Abteilung "Entwicklung" mit Name und Gehalt.
b) Berechne das Durchschnittsgehalt pro Abteilung.
c) Zeige Abteilungen, deren Durchschnittsgehalt ueber 50.000 liegt.
d) Fuege einen neuen Mitarbeiter ein (MID=42, Name="Weber", AbtID=3, Gehalt=55000).
e) Erhoehe das Gehalt aller Mitarbeiter der Abteilung 1 um 5%.

---
---

**Loesung Aufgabe 2:**
a)
```sql
SELECT m.Name, m.Gehalt
FROM Mitarbeiter m
INNER JOIN Abteilung a ON m.AbtID = a.AbtID
WHERE a.AbtName = 'Entwicklung';
```

b)
```sql
SELECT a.AbtName, AVG(m.Gehalt) AS Durchschnittsgehalt
FROM Mitarbeiter m
INNER JOIN Abteilung a ON m.AbtID = a.AbtID
GROUP BY a.AbtName;
```

c)
```sql
SELECT a.AbtName, AVG(m.Gehalt) AS Durchschnitt
FROM Mitarbeiter m
INNER JOIN Abteilung a ON m.AbtID = a.AbtID
GROUP BY a.AbtName
HAVING AVG(m.Gehalt) > 50000;
```

d)
```sql
INSERT INTO Mitarbeiter (MID, Name, AbtID, Gehalt)
VALUES (42, 'Weber', 3, 55000);
```

e)
```sql
UPDATE Mitarbeiter
SET Gehalt = Gehalt * 1.05
WHERE AbtID = 1;
```

---

## Aufgabe 3: ER-Modell erstellen
Ein Online-Shop benoetigt eine Datenbank mit folgenden Anforderungen:
- Kunden haben eine KundenNr, Name, E-Mail und Adresse
- Produkte haben eine ProduktNr, Bezeichnung, Preis und Kategorie
- Ein Kunde kann mehrere Bestellungen aufgeben
- Jede Bestellung hat ein Datum und kann mehrere Produkte enthalten
- Pro Position wird die Menge festgehalten

Erstelle das ER-Modell und leite die Tabellen in 3NF ab.

---
---

**Loesung Aufgabe 3:**

**ER-Modell:**
```
Kunde 1──n Bestellung n──m Produkt
                          (mit Menge)
```

**Tabellen (3NF):**
```sql
CREATE TABLE Kunde (
    KundenNr INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(150),
    Adresse VARCHAR(200)
);

CREATE TABLE Produkt (
    ProduktNr INT PRIMARY KEY,
    Bezeichnung VARCHAR(100) NOT NULL,
    Preis DECIMAL(10,2),
    Kategorie VARCHAR(50)
);

CREATE TABLE Bestellung (
    BestellNr INT PRIMARY KEY,
    KundenNr INT NOT NULL,
    Datum DATE NOT NULL,
    FOREIGN KEY (KundenNr) REFERENCES Kunde(KundenNr)
);

CREATE TABLE BestellPosition (
    BestellNr INT,
    ProduktNr INT,
    Menge INT NOT NULL,
    PRIMARY KEY (BestellNr, ProduktNr),
    FOREIGN KEY (BestellNr) REFERENCES Bestellung(BestellNr),
    FOREIGN KEY (ProduktNr) REFERENCES Produkt(ProduktNr)
);
```

---

## Aufgabe 4: Relational vs. NoSQL
Ordne die folgenden Anwendungsfaelle der passenden Datenbankart zu und begruende:
a) Buchungssystem einer Bank (Ueberweisungen)
b) Social-Media-Plattform mit Millionen Nutzern und flexiblen Profilen
c) Sensordaten eines IoT-Systems (Temperatur, alle 5 Sekunden)
d) Personalverwaltung mit fest definierten Feldern

---
---

**Loesung Aufgabe 4:**
a) **Relational (SQL)** – Bankbuchungen erfordern strenge Konsistenz (ACID), Transaktionssicherheit ist kritisch. Ein Konto darf nicht im inkonsistenten Zustand sein.
b) **NoSQL (Dokumentenbasiert, z.B. MongoDB)** – Flexible Profilstrukturen (jeder Nutzer andere Felder), horizontale Skalierung fuer Millionen Nutzer.
c) **NoSQL (Zeitreihen-DB, z.B. InfluxDB oder Cassandra)** – Massenhaft sequenzielle Daten, hoher Schreibdurchsatz, keine komplexen Beziehungen.
d) **Relational (SQL)** – Festes Schema, klare Beziehungen (Mitarbeiter → Abteilung → Standort), Reporting und Abfragen mit SQL effizient.
