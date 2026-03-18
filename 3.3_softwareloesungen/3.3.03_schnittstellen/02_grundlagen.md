# 3.3.03 – Grundlagen: Festlegen von Schnittstellen

## TK 1: API (REST)

### Was ist eine API?

**API** = Application Programming Interface – eine definierte Schnittstelle, ueber die Softwarekomponenten miteinander kommunizieren.

### REST-Prinzipien

**REST** = Representational State Transfer – ein Architekturstil fuer verteilte Systeme.

| Prinzip | Beschreibung |
|---------|-------------|
| **Client-Server** | Klare Trennung zwischen Client (Anfrage) und Server (Antwort) |
| **Stateless** | Jede Anfrage enthaelt alle noetige Information; Server speichert keinen Client-Zustand |
| **Cacheable** | Antworten koennen als cachebar markiert werden |
| **Uniform Interface** | Einheitliche Schnittstelle: Ressourcen durch URIs identifiziert |
| **Layered System** | Schichten (z.B. Load Balancer, Cache) zwischen Client und Server moeglich |

### HTTP-Methoden (CRUD)

| HTTP-Methode | CRUD-Operation | Beschreibung | Beispiel |
|-------------|---------------|-------------|----------|
| **GET** | Read | Ressource lesen/abrufen | `GET /api/kunden/42` |
| **POST** | Create | Neue Ressource anlegen | `POST /api/kunden` |
| **PUT** | Update | Ressource vollstaendig aktualisieren | `PUT /api/kunden/42` |
| **PATCH** | Update (teilw.) | Ressource teilweise aktualisieren | `PATCH /api/kunden/42` |
| **DELETE** | Delete | Ressource loeschen | `DELETE /api/kunden/42` |

### HTTP-Statuscodes

| Code-Bereich | Bedeutung | Wichtige Codes |
|-------------|-----------|---------------|
| **1xx** | Informativ | 100 Continue |
| **2xx** | Erfolg | 200 OK, 201 Created, 204 No Content |
| **3xx** | Umleitung | 301 Moved Permanently, 304 Not Modified |
| **4xx** | Client-Fehler | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found |
| **5xx** | Server-Fehler | 500 Internal Server Error, 503 Service Unavailable |

### REST-API-Design: Beispiel

```
Ressource: Kunden

GET    /api/kunden           → Alle Kunden abrufen
GET    /api/kunden/42        → Kunde mit ID 42 abrufen
POST   /api/kunden           → Neuen Kunden anlegen
PUT    /api/kunden/42        → Kunde 42 vollstaendig aktualisieren
PATCH  /api/kunden/42        → Kunde 42 teilweise aktualisieren
DELETE /api/kunden/42        → Kunde 42 loeschen

Verschachtelte Ressourcen:
GET    /api/kunden/42/bestellungen     → Alle Bestellungen von Kunde 42
GET    /api/kunden/42/bestellungen/7   → Bestellung 7 von Kunde 42
```

### Aufbau einer HTTP-Anfrage

```
POST /api/kunden HTTP/1.1
Host: api.beispiel.de
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiJ9...

{
  "name": "Max Mueller",
  "email": "max@beispiel.de"
}
```

### Aufbau einer HTTP-Antwort

```
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/kunden/43

{
  "id": 43,
  "name": "Max Mueller",
  "email": "max@beispiel.de",
  "erstelltAm": "2026-03-17"
}
```

---

## TK 2: Datenaustauschformate (XML, JSON)

### JSON (JavaScript Object Notation)

**Merkmale**: Leichtgewichtig, gut lesbar, weit verbreitet in Web-APIs

```json
{
  "kunde": {
    "id": 42,
    "name": "Max Mueller",
    "email": "max@beispiel.de",
    "aktiv": true,
    "adressen": [
      {
        "strasse": "Hauptstr. 1",
        "plz": "10115",
        "ort": "Berlin"
      },
      {
        "strasse": "Nebenstr. 5",
        "plz": "80331",
        "ort": "Muenchen"
      }
    ]
  }
}
```

**JSON-Datentypen**:

| Typ | Beispiel |
|-----|---------|
| String | `"Hallo Welt"` |
| Number | `42`, `3.14` |
| Boolean | `true`, `false` |
| null | `null` |
| Array | `[1, 2, 3]` |
| Object | `{"key": "value"}` |

### XML (Extensible Markup Language)

**Merkmale**: Strukturiert, selbstbeschreibend, mit Schema-Validierung

```xml
<?xml version="1.0" encoding="UTF-8"?>
<kunde>
  <id>42</id>
  <name>Max Mueller</name>
  <email>max@beispiel.de</email>
  <aktiv>true</aktiv>
  <adressen>
    <adresse>
      <strasse>Hauptstr. 1</strasse>
      <plz>10115</plz>
      <ort>Berlin</ort>
    </adresse>
    <adresse>
      <strasse>Nebenstr. 5</strasse>
      <plz>80331</plz>
      <ort>Muenchen</ort>
    </adresse>
  </adressen>
</kunde>
```

### Vergleich JSON vs. XML

| Merkmal | JSON | XML |
|---------|------|-----|
| Lesbarkeit | Gut, kompakt | Gut, aber ausfuehrlicher |
| Dateigroesse | Kleiner | Groesser (durch Tags) |
| Datentypen | Nativ (String, Number, Boolean, null) | Alles ist Text (Typisierung ueber Schema) |
| Schema-Validierung | JSON Schema (optional) | XSD, DTD (verbreitet) |
| Kommentare | Nicht moeglich | `<!-- Kommentar -->` |
| Verbreitung (Web-APIs) | Dominant | Aeltere Systeme, SOAP |
| Namespaces | Nein | Ja |
| Parsing | Einfach (nativ in JS) | Komplexer (DOM/SAX Parser) |

---

## TK 3: SQL als Schnittstelle

### SQL-CRUD-Operationen

| Operation | SQL-Befehl | Beispiel |
|-----------|-----------|---------|
| **Create** | INSERT INTO | `INSERT INTO kunden (name, email) VALUES ('Mueller', 'max@mail.de');` |
| **Read** | SELECT | `SELECT * FROM kunden WHERE id = 42;` |
| **Update** | UPDATE | `UPDATE kunden SET email = 'neu@mail.de' WHERE id = 42;` |
| **Delete** | DELETE | `DELETE FROM kunden WHERE id = 42;` |

### SQL als Datenschnittstelle

SQL wird als Schnittstelle zwischen Anwendung und Datenbank genutzt:

```
+-------------+    SQL-Abfragen    +-----------+
| Anwendung   | ←---------------→ | Datenbank |
| (Java, C#,  |    Ergebnisse     | (MySQL,   |
|  Python)    |                    |  PostgreSQL)|
+-------------+                    +-----------+

Typische Architektur:
  Anwendung → Repository/DAO → SQL → Datenbank
```

### Wichtige SQL-Klauseln (Kurzuebersicht)

| Klausel | Funktion | Beispiel |
|---------|----------|---------|
| SELECT | Spalten auswaehlen | `SELECT name, email` |
| FROM | Tabelle angeben | `FROM kunden` |
| WHERE | Bedingung filtern | `WHERE aktiv = true` |
| JOIN | Tabellen verknuepfen | `INNER JOIN bestellungen ON ...` |
| GROUP BY | Gruppieren | `GROUP BY stadt` |
| HAVING | Gruppenbedingung | `HAVING COUNT(*) > 5` |
| ORDER BY | Sortieren | `ORDER BY name ASC` |
| LIMIT | Ergebnisse begrenzen | `LIMIT 10` |

### Prepared Statements (SQL Injection verhindern)

```
UNSICHER (SQL Injection moeglich):
  query = "SELECT * FROM users WHERE name = '" + userInput + "'";
  → Eingabe: ' OR '1'='1  → Alle Daten werden zurueckgegeben!

SICHER (Prepared Statement):
  query = "SELECT * FROM users WHERE name = ?";
  statement.setParameter(1, userInput);
  → Parameter wird als Wert behandelt, nicht als SQL-Code
```
