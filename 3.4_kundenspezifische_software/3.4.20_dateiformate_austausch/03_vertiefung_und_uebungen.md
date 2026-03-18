# Vertiefung und Uebungen: 3.4.20 – Dateiformate zum Datenaustausch

## Vertiefung

### Vergleich: CSV vs. JSON vs. XML

| Kriterium | CSV | JSON | XML |
|-----------|-----|------|-----|
| Lesbarkeit (Mensch) | Gut (tabellarisch) | Sehr gut | Mittel (verbose) |
| Lesbarkeit (Maschine) | Einfach | Einfach | Komplex (Parser noetig) |
| Verschachtelung | Nein | Ja | Ja |
| Datentypen | Nein (alles Text) | Ja (String, Number, Boolean, null) | Nein (alles Text, Schema noetig) |
| Schema-Validierung | Nein | Ja (JSON Schema) | Ja (XSD, DTD) |
| Dateigroesse | Sehr klein | Klein | Gross (viele Tags) |
| Kommentare | Nein (inoffiziell) | Nein | Ja (`<!-- ... -->`) |
| MIME-Type | text/csv | application/json | application/xml |
| Verbreitung | Tabellenexport, Import | Web-APIs (REST) | SOAP, Konfiguration, Dokumente |
| Standard | RFC 4180 (informell) | RFC 8259 | W3C-Standard |

### Wann welches Format?

| Einsatzzweck | Empfohlenes Format | Begruendung |
|-------------|-------------------|-------------|
| Tabellendaten exportieren (z.B. Excel) | CSV | Einfach, kompakt, weit unterstuetzt |
| REST-API-Kommunikation | JSON | Standard fuer Web-APIs, leichtgewichtig |
| SOAP-Webservices | XML | SOAP basiert auf XML |
| Konfigurationsdateien | JSON oder XML | Strukturiert, lesbar |
| Dokumentenaustausch mit Schema | XML | Schema-Validierung (XSD) moeglich |
| Datenbank-Import/Export | CSV oder JSON | CSV fuer flache Tabellen, JSON fuer verschachtelte Daten |

### Dasselbe Daten in drei Formaten

**CSV:**
```
id;name;preis
1;Laptop;899.99
2;Maus;29.99
```

**JSON:**
```json
[
  { "id": 1, "name": "Laptop", "preis": 899.99 },
  { "id": 2, "name": "Maus", "preis": 29.99 }
]
```

**XML:**
```xml
<produkte>
  <produkt id="1">
    <name>Laptop</name>
    <preis>899.99</preis>
  </produkt>
  <produkt id="2">
    <name>Maus</name>
    <preis>29.99</preis>
  </produkt>
</produkte>
```

**Groessenvergleich (ca.):**
- CSV: ~40 Bytes
- JSON: ~100 Bytes
- XML: ~180 Bytes

→ CSV ist am kompaktesten, XML am ausfuehrlichsten.

### Haeufige Syntaxfehler

**JSON – Typische Fehler:**
- Schluessel ohne Anfuehrungszeichen: `{ name: "Max" }` → Falsch! Muss `"name"` sein
- Einfache Anfuehrungszeichen: `{ 'name': 'Max' }` → Falsch! Muss `"..."` sein
- Komma nach letztem Element: `{ "a": 1, }` → Falsch! Kein Trailing Comma
- Kommentare: `// Kommentar` → In JSON nicht erlaubt

**XML – Typische Fehler:**
- Tag nicht geschlossen: `<name>Laptop` → Muss `<name>Laptop</name>` sein
- Kein Wurzelelement: Zwei Tags auf oberster Ebene → Braucht ein umschliessendes Root
- Gross-/Kleinschreibung: `<Name>` und `</name>` → Stimmt nicht ueberein

**CSV – Typische Fehler:**
- Trennzeichen im Wert ohne Anfuehrungszeichen: `USB-Kabel, 2m` → Wird als zwei Spalten interpretiert
- Verschiedene Trennzeichen in einer Datei → Inkonsistenz

### Typische Pruefungsaspekte
- Syntaxfehler in JSON/XML erkennen und korrigieren
- Daten von einem Format in ein anderes umwandeln (z.B. CSV → JSON)
- Vergleich: Wann CSV, wann JSON, wann XML?
- MIME-Types zuordnen
- XML auf Well-formedness pruefen
- JSON-Datentypen benennen

### Haeufige Fehler
- JSON-Schluessel ohne Anfuehrungszeichen → in der Pruefung ein beliebter Stolperstein
- CSV wird als "primitiv" abgetan → fuer flache Tabellendaten ist es optimal
- XML wird mit HTML verwechselt: HTML hat feste Tags, XML definiert eigene Tags
- MIME-Type nicht gewusst: `application/json`, `text/csv`, `application/xml`

---

## Uebungen

**Aufgabe 1:** Konvertiere die folgende CSV-Datei in JSON:

```
vorname;nachname;alter
Anna;Mueller;28
Ben;Schmidt;34
Clara;Weber;22
```

**Aufgabe 2:** Konvertiere den JSON-Datensatz in XML:

```json
{
  "kunde": {
    "id": 42,
    "name": "Firma Tech GmbH",
    "kontakt": {
      "email": "info@tech.de",
      "telefon": "030-123456"
    }
  }
}
```

**Aufgabe 3:** Finde und korrigiere die Fehler in folgendem JSON:

```
{
  name: "Max Mustermann",
  'alter': 30,
  "hobbies": ["Lesen", "Sport",],
  "adresse": {
    "stadt": "Berlin"
    "plz": "10115"
  }
}
```

**Aufgabe 4:** Erklaere den Unterschied zwischen "well-formed" und "valid" bei XML.

**Aufgabe 5:** Nenne drei Situationen, in denen CSV besser geeignet ist als JSON, und drei Situationen, in denen JSON besser ist.

**Aufgabe 6:** Welcher MIME-Type gehoert zu: a) JSON, b) CSV, c) XML?

---
---

# Loesungen

## Aufgabe 1

```json
[
  {
    "vorname": "Anna",
    "nachname": "Mueller",
    "alter": 28
  },
  {
    "vorname": "Ben",
    "nachname": "Schmidt",
    "alter": 34
  },
  {
    "vorname": "Clara",
    "nachname": "Weber",
    "alter": 22
  }
]
```

## Aufgabe 2

```xml
<?xml version="1.0" encoding="UTF-8"?>
<kunde>
  <id>42</id>
  <name>Firma Tech GmbH</name>
  <kontakt>
    <email>info@tech.de</email>
    <telefon>030-123456</telefon>
  </kontakt>
</kunde>
```

## Aufgabe 3
Fehler und Korrekturen:
1. `name:` → `"name":` (Schluessel muss in doppelten Anfuehrungszeichen stehen)
2. `'alter':` → `"alter":` (Keine einfachen Anfuehrungszeichen in JSON)
3. `"Sport",]` → `"Sport"]` (Kein Komma nach dem letzten Element)
4. `"stadt": "Berlin"` → `"stadt": "Berlin",` (Komma zwischen den Eintraegen fehlt)

Korrigiert:
```json
{
  "name": "Max Mustermann",
  "alter": 30,
  "hobbies": ["Lesen", "Sport"],
  "adresse": {
    "stadt": "Berlin",
    "plz": "10115"
  }
}
```

## Aufgabe 4
- **Well-formed (wohlgeformt):** XML ist syntaktisch korrekt – alle Tags sind geschlossen, es gibt genau ein Wurzelelement, Gross-/Kleinschreibung stimmt ueberein.
- **Valid (gueltig):** XML ist wohlgeformt UND entspricht zusaetzlich einem definierten Schema (XSD oder DTD). Das Schema legt fest, welche Elemente erlaubt sind und welche Datentypen erwartet werden.

Merke: Jedes valide XML ist wohlgeformt, aber nicht jedes wohlgeformte XML ist valide.

## Aufgabe 5
**CSV besser geeignet:**
1. Export von Tabellendaten fuer Excel-Import
2. Grosse Datenmengen ohne verschachtelte Struktur (z.B. Logdateien)
3. Einfacher Datenaustausch zwischen Datenbanken

**JSON besser geeignet:**
1. REST-API-Kommunikation im Web
2. Verschachtelte Datenstrukturen (z.B. Kunde mit Adressen und Bestellungen)
3. Konfigurationsdateien mit strukturierten Daten

## Aufgabe 6
- a) JSON: `application/json`
- b) CSV: `text/csv`
- c) XML: `application/xml` (oder `text/xml`)
