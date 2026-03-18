# Komplett: 3.4.21 – Services und Ressourcen eines Servers nutzen

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.21
- **Thema:** Services und Ressourcen eines Servers nutzen koennen

## Ziel

Du musst die Grundprinzipien von REST und SOAP kennen, ihre Unterschiede erklaeren und begruenden koennen, wann welcher Ansatz geeignet ist. REST ist der aktuelle Standard fuer Web-APIs, SOAP wird in Enterprise-Umgebungen verwendet.

## Themenkreise

| Nr. | Themenkreis | Schwerpunkt |
|-----|-------------|-------------|
| 1 | REST | Ressourcenorientierte Webservices, HTTP-Methoden, Statelessness |
| 2 | SOAP | XML-basierte Webservices, WSDL, Envelope-Struktur |

---

## Grundlagen

### REST (Representational State Transfer)

**Definition:** REST ist ein Architekturstil fuer verteilte Systeme, der auf dem HTTP-Protokoll basiert. Ressourcen werden ueber URLs identifiziert und mit HTTP-Methoden manipuliert.

**Sechs Prinzipien von REST:**

| Prinzip | Bedeutung |
|---------|-----------|
| Client-Server | Klare Trennung von Client und Server |
| Stateless (Zustandslos) | Jede Anfrage enthaelt alle noetige Information, Server speichert keinen Client-Zustand |
| Cacheable | Antworten koennen zwischengespeichert werden |
| Uniform Interface | Einheitliche Schnittstelle (URLs, HTTP-Methoden) |
| Layered System | Mehrschichtige Architektur moeglich (z.B. Load Balancer dazwischen) |
| Code on Demand (optional) | Server kann ausfuehrbaren Code an Client senden |

**HTTP-Methoden (CRUD-Mapping):**

| HTTP-Methode | CRUD-Operation | Beschreibung | Beispiel |
|-------------|---------------|-------------|----------|
| GET | Read | Ressource abrufen | `GET /api/kunden/42` |
| POST | Create | Neue Ressource erstellen | `POST /api/kunden` |
| PUT | Update | Ressource vollstaendig ersetzen | `PUT /api/kunden/42` |
| PATCH | Update (teilweise) | Ressource teilweise aendern | `PATCH /api/kunden/42` |
| DELETE | Delete | Ressource loeschen | `DELETE /api/kunden/42` |

**HTTP-Statuscodes:**

| Code | Bedeutung | Typischer Einsatz |
|------|-----------|------------------|
| 200 | OK | Erfolgreiche GET-Anfrage |
| 201 | Created | Ressource erfolgreich erstellt (POST) |
| 204 | No Content | Erfolgreich, aber keine Rueckgabe (DELETE) |
| 400 | Bad Request | Fehlerhafte Anfrage (z.B. ungueltige Daten) |
| 401 | Unauthorized | Authentifizierung erforderlich |
| 403 | Forbidden | Zugriff verweigert |
| 404 | Not Found | Ressource existiert nicht |
| 500 | Internal Server Error | Serverfehler |

**REST-API-Beispiel:**

```
GET    /api/kunden          → Liste aller Kunden (JSON-Array)
GET    /api/kunden/42       → Einzelner Kunde mit ID 42
POST   /api/kunden          → Neuen Kunden anlegen (Daten im Body)
PUT    /api/kunden/42       → Kunde 42 aktualisieren (alle Felder)
DELETE /api/kunden/42       → Kunde 42 loeschen

Anfrage (POST):
POST /api/kunden
Content-Type: application/json

{
  "name": "Firma Tech GmbH",
  "email": "info@tech.de",
  "stadt": "Berlin"
}

Antwort (201 Created):
{
  "id": 43,
  "name": "Firma Tech GmbH",
  "email": "info@tech.de",
  "stadt": "Berlin"
}
```

---

### SOAP (Simple Object Access Protocol)

**Definition:** SOAP ist ein XML-basiertes Protokoll fuer den Austausch von Nachrichten zwischen Systemen. Es ist stark strukturiert und nutzt WSDL zur Schnittstellenbeschreibung.

**Bestandteile:**

| Bestandteil | Funktion |
|-------------|----------|
| SOAP Envelope | Umschliesst die gesamte Nachricht |
| SOAP Header | Optionale Metadaten (Authentifizierung, Transaktions-ID) |
| SOAP Body | Eigentliche Nutzdaten (Request/Response) |
| WSDL | Web Services Description Language – beschreibt die verfuegbaren Methoden |

**SOAP-Nachricht (Beispiel):**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Header>
    <auth:Token xmlns:auth="http://beispiel.de/auth">
      abc123token
    </auth:Token>
  </soap:Header>
  <soap:Body>
    <getKunde xmlns="http://beispiel.de/kunden">
      <kundenId>42</kundenId>
    </getKunde>
  </soap:Body>
</soap:Envelope>
```

**SOAP-Antwort:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <getKundeResponse xmlns="http://beispiel.de/kunden">
      <kunde>
        <id>42</id>
        <name>Firma Tech GmbH</name>
        <email>info@tech.de</email>
      </kunde>
    </getKundeResponse>
  </soap:Body>
</soap:Envelope>
```

**WSDL (Web Services Description Language):**
- Beschreibt die verfuegbaren Operationen des Webservices
- Definiert Eingangs- und Ausgangsparameter
- Wird vom Client genutzt, um automatisch passende Anfragen zu erzeugen
- Vergleichbar mit einer API-Dokumentation, aber maschinenlesbar

---

## Vertiefung

### REST vs. SOAP – Vergleich

| Kriterium | REST | SOAP |
|-----------|------|------|
| Protokoll | HTTP | HTTP, SMTP, TCP (flexibel) |
| Datenformat | JSON (typisch), XML, CSV | Nur XML |
| Schnittstellenbeschreibung | OpenAPI / Swagger (optional) | WSDL (erforderlich) |
| Zustandslosigkeit | Ja (Pflicht) | Moeglich, aber nicht zwingend |
| Sicherheit | HTTPS, OAuth, JWT | WS-Security (integriert) |
| Komplexitaet | Gering | Hoch |
| Performance | Schnell (kompaktes JSON) | Langsamer (grosses XML) |
| Fehlerbehandlung | HTTP-Statuscodes | SOAP-Fault-Element |
| Eignung | Web-Apps, Mobile Apps, Microservices | Enterprise, Banken, Behoerden |
| Transaktionssicherheit | Nicht eingebaut | Ja (WS-AtomicTransaction) |
| Caching | Ja (HTTP-Cache) | Schwierig |

### Wann REST, wann SOAP?

| Szenario | Empfehlung | Begruendung |
|----------|-----------|-------------|
| Mobile App kommuniziert mit Backend | REST | Leichtgewichtig, JSON, schnell |
| Microservice-Architektur | REST | Einfache, entkoppelte Kommunikation |
| Bankensystem mit Transaktionen | SOAP | Transaktionssicherheit, WS-Security |
| Integration alter Enterprise-Systeme | SOAP | Viele Legacy-Systeme nutzen SOAP |
| Oeffentliche Web-API | REST | Standard, breite Tool-Unterstuetzung |
| B2B mit strengen Schnittstellenvertraegen | SOAP | WSDL als formaler Vertrag |

### REST – URL-Design Best Practices

```
GUT:                              SCHLECHT:
/api/kunden                       /api/getKunden
/api/kunden/42                    /api/kunde?id=42
/api/kunden/42/bestellungen       /api/getBestellungenFuerKunde/42

Regeln:
- Nomen (Substantive) verwenden, keine Verben
- Plural: /kunden statt /kunde
- Hierarchisch: /kunden/42/bestellungen
- HTTP-Methode bestimmt die Aktion (GET, POST, PUT, DELETE)
```

### Typische Pruefungsaspekte
- REST-Prinzipien benennen (v.a. Statelessness)
- HTTP-Methoden den CRUD-Operationen zuordnen
- REST vs. SOAP Vergleichstabelle
- SOAP-Envelope-Struktur erklaeren
- HTTP-Statuscodes kennen und zuordnen
- Szenario: REST oder SOAP empfehlen?

### Haeufige Fehler
- REST wird als Protokoll bezeichnet → REST ist ein Architekturstil, kein Protokoll
- Statelessness missverstanden: Der Server speichert keine Session-Daten, NICHT "es gibt keinen Zustand" → Der Zustand wird vom Client mit jeder Anfrage mitgesendet (z.B. Token)
- SOAP wird als veraltet abgeschrieben → In Enterprise-Umgebungen immer noch verbreitet
- REST-URL mit Verben: `/api/getKunden` → sollte `/api/kunden` + GET-Methode sein

---

## Uebungen

**Aufgabe 1:** Nenne die fuenf HTTP-Methoden und ordne sie den CRUD-Operationen zu.

**Aufgabe 2:** Erklaere, was "Stateless" bei REST bedeutet. Warum ist dieses Prinzip wichtig?

**Aufgabe 3:** Vergleiche REST und SOAP anhand von vier Kriterien.

**Aufgabe 4:** Ein Mobilfunkanbieter moechte eine REST-API fuer die Kundenverwaltung bereitstellen. Entwirf die URLs fuer folgende Operationen:
- Alle Kunden abrufen
- Einzelnen Kunden abrufen (ID 17)
- Neuen Kunden anlegen
- Kunden 17 loeschen
- Alle Vertraege von Kunde 17 abrufen

**Aufgabe 5:** Was ist WSDL und wozu dient es?

**Aufgabe 6:** Ein Unternehmen muss zwischen REST und SOAP waehlen. Szenario A: Oeffentliche API fuer eine Wetter-App. Szenario B: Interne Schnittstelle fuer eine Bankueberweisung. Empfehle jeweils und begruende.

---
---

# Loesungen

## Aufgabe 1

| HTTP-Methode | CRUD | Beschreibung |
|-------------|------|-------------|
| GET | Read | Daten abrufen |
| POST | Create | Neue Daten erstellen |
| PUT | Update | Daten vollstaendig ersetzen |
| PATCH | Update (teilweise) | Daten teilweise aendern |
| DELETE | Delete | Daten loeschen |

## Aufgabe 2
"Stateless" bedeutet, dass der Server keinen Zustand ueber vorherige Anfragen des Clients speichert. Jede Anfrage muss alle Informationen enthalten, die der Server zur Verarbeitung benoetigt (z.B. Authentifizierungs-Token). Wichtig, weil: (1) Server kann beliebig skaliert werden (kein Session-Speicher), (2) Anfragen koennen auf verschiedene Server verteilt werden (Load Balancing), (3) Einfachere Fehlerbehandlung.

## Aufgabe 3

| Kriterium | REST | SOAP |
|-----------|------|------|
| Datenformat | JSON (typisch) | Nur XML |
| Komplexitaet | Gering | Hoch |
| Performance | Schnell (kompaktes JSON) | Langsamer (XML-Overhead) |
| Sicherheit | HTTPS, OAuth, JWT | WS-Security (integriert) |

## Aufgabe 4
```
GET    /api/kunden            → Alle Kunden abrufen
GET    /api/kunden/17         → Kunde 17 abrufen
POST   /api/kunden            → Neuen Kunden anlegen
DELETE /api/kunden/17         → Kunde 17 loeschen
GET    /api/kunden/17/vertraege  → Alle Vertraege von Kunde 17
```

## Aufgabe 5
WSDL (Web Services Description Language) ist eine XML-basierte Beschreibungssprache fuer SOAP-Webservices. Sie beschreibt: (1) Welche Operationen verfuegbar sind, (2) Welche Parameter erwartet werden, (3) Welche Datentypen zurueckgegeben werden, (4) Unter welcher URL der Service erreichbar ist. WSDL dient als maschinenlesbarer Vertrag, aus dem Client-Code automatisch generiert werden kann.

## Aufgabe 6
- **Szenario A (Wetter-App):** **REST** – Oeffentliche APIs sollten leichtgewichtig und einfach konsumierbar sein. JSON ist kleiner als XML (wichtig fuer mobile Daten), HTTP-Caching beschleunigt wiederholte Anfragen, und die breite Tool-Unterstuetzung erleichtert die Integration.
- **Szenario B (Bankueberweisung):** **SOAP** – Bankueberweisungen erfordern Transaktionssicherheit (WS-AtomicTransaction) und starke Sicherheitsmechanismen (WS-Security). WSDL bietet einen formalen Schnittstellenvertrag, der in regulierten Umgebungen wichtig ist.
