# 3.3.03 – Vertiefung und Uebungen: Festlegen von Schnittstellen

## Vertiefung

### REST vs. SOAP

| Merkmal | REST | SOAP |
|---------|------|------|
| Protokoll | HTTP/HTTPS | HTTP, SMTP, TCP etc. |
| Datenformat | JSON, XML | Nur XML |
| Zustandslosigkeit | Ja (Kernprinzip) | Moeglich, aber nicht zwingend |
| Komplexitaet | Einfach | Komplex (WSDL, Envelope) |
| Performance | Schneller (weniger Overhead) | Langsamer (XML-Overhead) |
| Sicherheit | HTTPS, OAuth, JWT | WS-Security (umfangreicher) |
| Einsatz | Moderne Web-APIs, Mobile Apps | Enterprise, Banken, Versicherungen |

### API-Authentifizierung

| Methode | Beschreibung | Sicherheit |
|---------|-------------|-----------|
| API Key | Schluessel im Header oder URL | Niedrig (leicht abfangbar) |
| Basic Auth | Benutzername:Passwort (Base64) | Niedrig (nur mit HTTPS sicher) |
| Bearer Token / JWT | Token im Authorization-Header | Mittel bis hoch |
| OAuth 2.0 | Autorisierungsframework mit Tokens | Hoch (Standard fuer 3rd-Party-Zugriff) |

### JSON-Pfadnavigation

```json
{
  "firma": {
    "name": "TechAG",
    "mitarbeiter": [
      { "id": 1, "name": "Anna", "abteilung": "IT" },
      { "id": 2, "name": "Ben", "abteilung": "HR" }
    ]
  }
}
```

| Pfad | Ergebnis |
|------|---------|
| `firma.name` | `"TechAG"` |
| `firma.mitarbeiter[0].name` | `"Anna"` |
| `firma.mitarbeiter[1].abteilung` | `"HR"` |
| `firma.mitarbeiter.length` | `2` |

---

### Pruefungsaspekte

**Typische Fragestellungen**:
1. "Welche HTTP-Methode verwenden Sie zum Anlegen einer neuen Ressource?" → POST
2. "Was bedeutet der Statuscode 404?" → Ressource nicht gefunden
3. "Nennen Sie zwei Vorteile von JSON gegenueber XML" → Kompakter, native Datentypen
4. "Was ist SQL Injection und wie schuetzt man sich?" → Prepared Statements

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| GET fuer Datenmanipulation verwenden | GET ist nur zum Lesen (idempotent, sicher) |
| PUT und PATCH verwechseln | PUT = vollstaendiges Ersetzen, PATCH = teilweises Aendern |
| 401 und 403 verwechseln | 401 = nicht authentifiziert, 403 = authentifiziert aber nicht autorisiert |
| JSON mit einfachen Anfuehrungszeichen | JSON erfordert doppelte Anfuehrungszeichen: `"key"` |
| SQL ohne WHERE bei UPDATE/DELETE | Ohne WHERE werden ALLE Datensaetze betroffen! |

---

## Uebungen

### Aufgabe 1: HTTP-Methoden zuordnen

Welche HTTP-Methode verwenden Sie fuer folgende Aktionen?

| Aktion | HTTP-Methode? |
|--------|--------------|
| a) Alle Produkte einer Kategorie abrufen | |
| b) Einen neuen Benutzer registrieren | |
| c) Die E-Mail-Adresse eines Kunden aendern | |
| d) Einen Artikel aus dem Warenkorb entfernen | |
| e) Alle Informationen eines Kunden vollstaendig aktualisieren | |

---

### Aufgabe 2: JSON schreiben

Erstelle ein gueltiges JSON-Objekt fuer folgenden Sachverhalt:
- Ein Produkt mit ID 101, Name "Laptop Pro 15", Preis 1299.99
- Kategorie: "Elektronik"
- Verfuegbar: ja
- Spezifikationen: RAM 16 GB, SSD 512 GB, Display 15.6 Zoll
- Tags: "laptop", "business", "premium"

---

### Aufgabe 3: Statuscodes zuordnen

Welcher HTTP-Statuscode passt?

| Situation | Code? |
|-----------|-------|
| a) Anfrage erfolgreich, neue Ressource erstellt | |
| b) Client sendet fehlerhafte Daten | |
| c) Server hat einen internen Fehler | |
| d) Angefragte URL existiert nicht | |
| e) Zugriff verweigert (nicht eingeloggt) | |
| f) Anfrage erfolgreich, keine Daten zurueck | |

---

### Aufgabe 4: REST-Endpunkte entwerfen

Entwirf REST-Endpunkte fuer ein Aufgabenverwaltungssystem (Todo-App):
- Alle Aufgaben eines Benutzers abrufen
- Eine neue Aufgabe erstellen
- Eine einzelne Aufgabe abrufen
- Den Status einer Aufgabe auf "erledigt" setzen
- Eine Aufgabe loeschen

---

### Aufgabe 5: JSON in XML umwandeln

Wandle folgendes JSON in XML um:

```json
{
  "bestellung": {
    "bestellNr": 4711,
    "datum": "2026-03-17",
    "positionen": [
      { "artikel": "Maus", "menge": 2, "preis": 29.99 },
      { "artikel": "Tastatur", "menge": 1, "preis": 79.99 }
    ]
  }
}
```

---
---

## Loesung Aufgabe 1

| Aktion | HTTP-Methode |
|--------|-------------|
| a) Alle Produkte abrufen | **GET** |
| b) Neuen Benutzer registrieren | **POST** |
| c) E-Mail-Adresse aendern | **PATCH** (nur ein Feld) |
| d) Artikel aus Warenkorb entfernen | **DELETE** |
| e) Kunden vollstaendig aktualisieren | **PUT** |

---

## Loesung Aufgabe 2

```json
{
  "id": 101,
  "name": "Laptop Pro 15",
  "preis": 1299.99,
  "kategorie": "Elektronik",
  "verfuegbar": true,
  "spezifikationen": {
    "ram": "16 GB",
    "ssd": "512 GB",
    "display": "15.6 Zoll"
  },
  "tags": ["laptop", "business", "premium"]
}
```

---

## Loesung Aufgabe 3

| Situation | Code |
|-----------|------|
| a) Neue Ressource erstellt | **201 Created** |
| b) Fehlerhafte Daten | **400 Bad Request** |
| c) Interner Serverfehler | **500 Internal Server Error** |
| d) URL existiert nicht | **404 Not Found** |
| e) Nicht eingeloggt | **401 Unauthorized** |
| f) Erfolgreich, keine Daten | **204 No Content** |

---

## Loesung Aufgabe 4

```
GET    /api/benutzer/{benutzerId}/aufgaben          → Alle Aufgaben eines Benutzers
POST   /api/benutzer/{benutzerId}/aufgaben          → Neue Aufgabe erstellen
GET    /api/benutzer/{benutzerId}/aufgaben/{id}      → Einzelne Aufgabe abrufen
PATCH  /api/benutzer/{benutzerId}/aufgaben/{id}      → Status auf "erledigt" setzen
DELETE /api/benutzer/{benutzerId}/aufgaben/{id}      → Aufgabe loeschen

Beispiel: PATCH-Request-Body fuer Statusaenderung:
{
  "status": "erledigt"
}
```

---

## Loesung Aufgabe 5

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bestellung>
  <bestellNr>4711</bestellNr>
  <datum>2026-03-17</datum>
  <positionen>
    <position>
      <artikel>Maus</artikel>
      <menge>2</menge>
      <preis>29.99</preis>
    </position>
    <position>
      <artikel>Tastatur</artikel>
      <menge>1</menge>
      <preis>79.99</preis>
    </position>
  </positionen>
</bestellung>
```
