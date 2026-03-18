# Grundlagen: 3.4.20 – Dateiformate zum Datenaustausch

## CSV (Comma-Separated Values)

**Definition:** CSV ist ein textbasiertes Tabellenformat, bei dem Datensaetze zeilenweise gespeichert werden und die einzelnen Werte durch ein Trennzeichen (Delimiter) getrennt sind.

**Syntax-Regeln:**
- Eine Zeile = ein Datensatz
- Erste Zeile = optional Spaltenkoepfe (Header)
- Trennzeichen: Komma (`,`), Semikolon (`;`) oder Tab (`\t`)
- Textwerte mit Sonderzeichen in Anfuehrungszeichen einschliessen
- Kein offizieller Standard fuer Zeichenkodierung (meist UTF-8)

**Beispiel:**

```csv
id;name;preis;kategorie
1;Laptop;899.99;Elektronik
2;Maus;29.99;Zubehoer
3;Monitor;349.00;Elektronik
4;"USB-Kabel, 2m";9.99;Zubehoer
```

**MIME-Type:** `text/csv`
**Dateiendung:** `.csv`

**Wichtige Begriffe:**
- **Delimiter** – Trennzeichen zwischen Werten
- **Header** – Kopfzeile mit Spaltennamen
- **Escaping** – Anfuehrungszeichen fuer Werte, die das Trennzeichen enthalten

---

## JSON (JavaScript Object Notation)

**Definition:** JSON ist ein textbasiertes, leichtgewichtiges Datenaustauschformat, das auf Schluessel-Wert-Paaren und geordneten Listen basiert.

**Syntax-Regeln:**
- Objekte: `{ "schluessel": "wert" }` (geschweift Klammern)
- Arrays: `[ wert1, wert2, wert3 ]` (eckige Klammern)
- Schluessel MUESSEN in doppelten Anfuehrungszeichen stehen
- Datentypen: String, Number, Boolean (true/false), null, Object, Array
- Kein Kommentar erlaubt
- Verschachtelung moeglich

**Datentypen in JSON:**

| Typ | Beispiel |
|-----|---------|
| String | `"Hallo Welt"` |
| Number | `42`, `3.14` |
| Boolean | `true`, `false` |
| null | `null` |
| Object | `{ "name": "Max" }` |
| Array | `[1, 2, 3]` |

**Beispiel:**

```json
{
  "artikel": [
    {
      "id": 1,
      "name": "Laptop",
      "preis": 899.99,
      "kategorie": "Elektronik",
      "verfuegbar": true
    },
    {
      "id": 2,
      "name": "Maus",
      "preis": 29.99,
      "kategorie": "Zubehoer",
      "verfuegbar": true
    },
    {
      "id": 3,
      "name": "Monitor",
      "preis": 349.00,
      "kategorie": "Elektronik",
      "verfuegbar": false
    }
  ]
}
```

**MIME-Type:** `application/json`
**Dateiendung:** `.json`

**Wichtige Begriffe:**
- **Key-Value-Pair** – Schluessel-Wert-Paar: `"name": "Max"`
- **Serialisierung** – Objekt in JSON-String umwandeln
- **Deserialisierung / Parsing** – JSON-String in Objekt umwandeln

---

## XML (Extensible Markup Language)

**Definition:** XML ist eine erweiterbare Auszeichnungssprache, die Daten hierarchisch in Tags strukturiert. Jedes Element hat ein oeffnendes und ein schliessendes Tag.

**Syntax-Regeln:**
- Genau ein Wurzelelement (Root-Element)
- Jedes oeffnende Tag muss ein schliessendes Tag haben: `<name>...</name>`
- Tags sind case-sensitive: `<Name>` ≠ `<name>`
- Attribute in oeffnenden Tags moeglich: `<artikel id="1">`
- Sonderzeichen durch Entities: `&lt;` fuer `<`, `&amp;` fuer `&`
- Optionale XML-Deklaration: `<?xml version="1.0" encoding="UTF-8"?>`

**Beispiel:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<artikelListe>
  <artikel id="1">
    <name>Laptop</name>
    <preis>899.99</preis>
    <kategorie>Elektronik</kategorie>
    <verfuegbar>true</verfuegbar>
  </artikel>
  <artikel id="2">
    <name>Maus</name>
    <preis>29.99</preis>
    <kategorie>Zubehoer</kategorie>
    <verfuegbar>true</verfuegbar>
  </artikel>
  <artikel id="3">
    <name>Monitor</name>
    <preis>349.00</preis>
    <kategorie>Elektronik</kategorie>
    <verfuegbar>false</verfuegbar>
  </artikel>
</artikelListe>
```

**MIME-Type:** `application/xml` oder `text/xml`
**Dateiendung:** `.xml`

**Wichtige Begriffe:**
- **Tag** – Auszeichnung: `<name>Wert</name>`
- **Attribut** – Eigenschaft im oeffnenden Tag: `id="1"`
- **Wurzelelement (Root)** – Aeusserstes Element, das alle anderen umschliesst
- **Well-formed** – XML ist syntaktisch korrekt (alle Tags geschlossen, ein Root)
- **Valid** – XML entspricht einem Schema (DTD oder XSD)
- **XSD (XML Schema Definition)** – Definiert Struktur und Datentypen
- **XSLT** – Transformation von XML in andere Formate (z.B. HTML)
