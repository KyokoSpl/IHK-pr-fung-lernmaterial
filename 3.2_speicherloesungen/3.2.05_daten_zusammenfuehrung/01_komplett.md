# Ueberblick und Grundlagen: 3.2.05 – Daten heterogener Quellen zusammenfuehren

## Einordnung

- **Pruefungsteil:** 3.2 – Inbetriebnehmen von Speicherloesungen
- **Thema-ID:** 3.2.05
- **Thema:** Daten heterogener Quellen zusammenfuehren koennen

## Ziel

Du musst verstehen, wie Daten aus unterschiedlichen Systemen und Formaten zusammengefuehrt werden. Dazu gehoeren das Konzept eines Data Lake, der ETL-Prozess und die gaengigen Datenaustauschformate XML, JSON und CSV.

## Themenkreise im Ueberblick

| Nr. | Themenkreis | Schwerpunkt |
|-----|-------------|-------------|
| 1 | Bildung eines Data Lake o.ae. | Data Lake vs. Data Warehouse, ETL-Prozess |
| 2 | Datenaustauschformate: XML, JSON, CSV u.a. | Aufbau, Vergleich, Einsatzbereiche |

### Querverweise
- Thema 3.2.04: Service- und Liefermodelle (Cloud-Speicher als Datenquelle)
- Thema 3.2.06: Netzwerkprotokolle (NAS, SAN als Speicherloesungen)
- Thema 2.4.03: SQL und Datenbanken (strukturierte Daten)

---

## Grundlagen

### 1. Data Lake und Datenintegration

**Definition:** Ein Data Lake ist ein zentraler Speicher, der grosse Mengen an Roh-Daten in ihrem nativen Format aufnimmt – strukturiert, semi-strukturiert und unstrukturiert. Die Daten werden erst bei der Analyse aufbereitet (Schema-on-Read).

**Data Lake vs. Data Warehouse:**

| Kriterium | Data Lake | Data Warehouse |
|-----------|----------|---------------|
| Datenformat | Roh-Daten (alle Formate) | Bereinigte, strukturierte Daten |
| Schema | Schema-on-Read (bei Analyse) | Schema-on-Write (beim Laden) |
| Datentypen | Strukturiert, semi-strukturiert, unstrukturiert | Nur strukturiert |
| Speicherkosten | Guenstig (z.B. Object Storage) | Teurer (relationale Datenbank) |
| Nutzer | Data Scientists, Analysten | Business-Analysten, Reporting |
| Flexibilitaet | Hoch (alle Daten verfuegbar) | Geringer (nur vordefinierte Daten) |
| Risiko | "Data Swamp" bei fehlender Governance | Hoher Aufwand bei der Datenaufbereitung |

**ETL-Prozess (Extract, Transform, Load):**

```
+-------------+     +--------------+     +------------------+
| EXTRACT     | --> | TRANSFORM    | --> | LOAD             |
| Daten aus   |     | Bereinigung, |     | Laden in Ziel-   |
| Quellen     |     | Umwandlung,  |     | system (DWH,     |
| extrahieren |     | Validierung  |     | Data Lake)       |
+-------------+     +--------------+     +------------------+
     |                    |                      |
 Datenbanken         Formate an-          Data Warehouse
 CSV-Dateien         gleichen,            Data Lake
 APIs                Duplikate            Datenbank
 IoT-Sensoren        entfernen
```

| Phase | Beschreibung | Beispiel |
|-------|-------------|---------|
| **Extract** | Daten aus verschiedenen Quellen auslesen | Lesen aus SQL-Datenbank, CSV-Import, API-Abfrage |
| **Transform** | Daten bereinigen, umwandeln, vereinheitlichen | Datumsformat vereinheitlichen, Duplikate entfernen, Kodierung anpassen |
| **Load** | Aufbereitete Daten in das Zielsystem laden | Import in Data Warehouse oder Data Lake |

**Variante: ELT (Extract, Load, Transform)**
- Daten werden zuerst in den Data Lake geladen und erst spaeter transformiert
- Vorteil: Schnelleres Laden, Transformation bei Bedarf
- Typisch fuer Cloud-basierte Data Lakes

**Wichtige Begriffe:**
- **Data Lake** – zentraler Speicher fuer Roh-Daten aller Formate
- **Data Warehouse** – zentraler Speicher fuer bereinigte, strukturierte Daten
- **ETL** – Extract, Transform, Load (Datenpipeline)
- **Schema-on-Read** – Datenstruktur wird erst beim Lesen definiert
- **Schema-on-Write** – Datenstruktur wird beim Schreiben festgelegt
- **Data Governance** – Regeln zur Qualitaet, Sicherheit und Verwaltung von Daten

---

### 2. Datenaustauschformate: XML, JSON, CSV

**Definition:** Datenaustauschformate definieren die Struktur, in der Daten zwischen Systemen uebertragen werden. Die drei wichtigsten textbasierten Formate sind XML, JSON und CSV.

**Vergleich der Formate:**

| Kriterium | XML | JSON | CSV |
|-----------|-----|------|-----|
| Ausgeschrieben | Extensible Markup Language | JavaScript Object Notation | Comma-Separated Values |
| Struktur | Hierarchisch (Baumstruktur) | Hierarchisch (Key-Value) | Tabellarisch (Zeilen/Spalten) |
| Lesbarkeit | Mittel (ausfuehrlich) | Gut (kompakt) | Gut (sehr einfach) |
| Verschachtelung | Ja (beliebig tief) | Ja (beliebig tief) | Nein |
| Schema/Validierung | XSD, DTD | JSON Schema | Keine Standardvalidierung |
| Datentypen | Nur Text (Typen ueber Schema) | String, Number, Boolean, Array, Object, null | Nur Text |
| Verbreitung | Konfiguration, SOAP, Dokumenten-Austausch | REST-APIs, Web, NoSQL | Tabellen, Import/Export, einfache Daten |
| Dateigroesse | Gross (viele Tags) | Mittel | Klein |

**Beispiel: Dieselben Daten in drei Formaten**

**XML:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<mitarbeiter>
  <person>
    <name>Max Mustermann</name>
    <abteilung>IT</abteilung>
    <gehalt>55000</gehalt>
  </person>
  <person>
    <name>Erika Muster</name>
    <abteilung>Vertrieb</abteilung>
    <gehalt>48000</gehalt>
  </person>
</mitarbeiter>
```

**JSON:**
```json
{
  "mitarbeiter": [
    {
      "name": "Max Mustermann",
      "abteilung": "IT",
      "gehalt": 55000
    },
    {
      "name": "Erika Muster",
      "abteilung": "Vertrieb",
      "gehalt": 48000
    }
  ]
}
```

**CSV:**
```
name,abteilung,gehalt
Max Mustermann,IT,55000
Erika Muster,Vertrieb,48000
```

**Wichtige Begriffe:**
- **XML** – tag-basiertes Format mit oeffnenden und schliessenden Tags
- **JSON** – leichtgewichtiges Key-Value-Format, Standard fuer REST-APIs
- **CSV** – einfachstes Format, Werte durch Trennzeichen (Komma, Semikolon) getrennt
- **XSD (XML Schema Definition)** – definiert die Struktur eines XML-Dokuments
- **Well-formed** – syntaktisch korrektes XML (alle Tags geschlossen, korrekte Verschachtelung)
- **Parser** – Software, die ein Datenformat liest und verarbeitet

---

## Vertiefung

### Wann welches Format?

| Anwendungsfall | Empfohlenes Format | Begruendung |
|----------------|-------------------|-------------|
| REST-API | JSON | Kompakt, nativ in JavaScript, Standard fuer Web-APIs |
| SOAP-Webservice | XML | SOAP basiert auf XML |
| Tabellenexport aus Excel | CSV | Einfach, universell importierbar |
| Konfigurationsdateien | XML oder JSON | Hierarchische Struktur moeglich |
| Datenaustausch mit Behoerden | XML | Haeufig vorgeschrieben (z.B. ELSTER, XRechnung) |
| NoSQL-Datenbank (z.B. MongoDB) | JSON (BSON) | Natives Speicherformat |
| Grosser Datenimport (einfach) | CSV | Geringster Overhead, schnell zu verarbeiten |

### Typische Pruefungsaspekte
- XML, JSON, CSV vergleichen und Einsatzbereiche benennen
- Datenformat an einem Beispiel erkennen und erklaeren
- Data Lake vs. Data Warehouse unterscheiden
- ETL-Prozess in eigenen Worten beschreiben
- Schema-on-Read vs. Schema-on-Write erklaeren

### Haeufige Fehler
- Data Lake und Data Warehouse verwechseln: Data Lake = Roh-Daten, Data Warehouse = bereinigt und strukturiert
- JSON hat KEINE Kommentare – im Gegensatz zu XML (<!-- Kommentar -->)
- CSV hat keine Standardisierung fuer das Trennzeichen → in Deutschland oft Semikolon statt Komma
- ETL-Reihenfolge verwechselt: Extract → Transform → Load (nicht Load → Transform)

---

## Uebungen

**Aufgabe 1:** Erklaere den Unterschied zwischen einem Data Lake und einem Data Warehouse. Nenne je ein Anwendungsbeispiel.

**Aufgabe 2:** Beschreibe die drei Phasen des ETL-Prozesses und gib fuer jede Phase ein konkretes Beispiel.

**Aufgabe 3:** Gegeben ist folgender JSON-Code. Wandle ihn in XML und CSV um.
```json
{
  "produkte": [
    {"id": 1, "name": "Monitor", "preis": 299.99},
    {"id": 2, "name": "Tastatur", "preis": 49.99}
  ]
}
```

**Aufgabe 4:** Ein Unternehmen erhaelt Kundendaten aus drei Quellen: einer SQL-Datenbank, einer CSV-Datei und einer REST-API (JSON). Beschreibe, wie diese Daten in einem Data Lake zusammengefuehrt werden koennen.

**Aufgabe 5:** Nenne drei Vorteile von JSON gegenueber XML und einen Vorteil von XML gegenueber JSON.

---
---

# Loesungen

## Aufgabe 1
- **Data Lake:** Zentraler Speicher fuer Roh-Daten in beliebigen Formaten (strukturiert, semi-strukturiert, unstrukturiert). Daten werden erst bei der Analyse strukturiert (Schema-on-Read). Beispiel: Zentrale Ablage fuer IoT-Sensordaten, Log-Dateien und Bilder fuer spaeteren Machine-Learning-Einsatz.
- **Data Warehouse:** Speicher fuer bereinigte, strukturierte Daten mit festem Schema (Schema-on-Write). Daten werden vor dem Laden aufbereitet. Beispiel: Consolidierte Verkaufszahlen aus allen Filialen fuer monatliches Reporting.

## Aufgabe 2
1. **Extract:** Daten aus verschiedenen Quellen auslesen. Beispiel: Taeglich um 02:00 Uhr werden alle Bestellungen aus der MySQL-Datenbank exportiert.
2. **Transform:** Daten bereinigen und vereinheitlichen. Beispiel: Datumsformat von "MM/DD/YYYY" (US) auf "DD.MM.YYYY" (DE) umwandeln, Duplikate entfernen.
3. **Load:** Aufbereitete Daten ins Zielsystem laden. Beispiel: Die transformierten Bestelldaten werden in das Data Warehouse importiert.

## Aufgabe 3

**XML:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<produkte>
  <produkt>
    <id>1</id>
    <name>Monitor</name>
    <preis>299.99</preis>
  </produkt>
  <produkt>
    <id>2</id>
    <name>Tastatur</name>
    <preis>49.99</preis>
  </produkt>
</produkte>
```

**CSV:**
```
id,name,preis
1,Monitor,299.99
2,Tastatur,49.99
```

## Aufgabe 4
1. **Extract:** Daten aus allen drei Quellen extrahieren – SQL-Abfrage auf die Datenbank, CSV-Datei einlesen, REST-API mit GET-Anfrage abfragen.
2. **Transform:** Datenformate vereinheitlichen (z.B. Datumsformat, Zeichenkodierung), Duplikate ueber Kundennummer identifizieren und zusammenfuehren, fehlende Felder ergaenzen oder markieren.
3. **Load:** Alle Daten in den Data Lake laden (z.B. als JSON oder Parquet-Dateien in einem Object Storage wie AWS S3).

Alternativ bei ELT: Roh-Daten direkt in den Data Lake laden und erst bei Bedarf transformieren.

## Aufgabe 5
**Vorteile von JSON gegenueber XML:**
1. Kompakter (weniger Overhead, keine schliessenden Tags)
2. Nativ in JavaScript/Web-Anwendungen nutzbar
3. Unterstuetzt Datentypen direkt (Number, Boolean, Array)

**Vorteil von XML gegenueber JSON:**
XML unterstuetzt Schema-Validierung (XSD/DTD), Namespaces und ist in vielen offiziellen Standards und Behoerden-Schnittstellen vorgeschrieben (z.B. XRechnung, SOAP).
