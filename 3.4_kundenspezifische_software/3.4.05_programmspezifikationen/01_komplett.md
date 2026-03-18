# Komplett: 3.4.05 – Programmspezifikationen, Datenmodelle, Schnittstellen, Programmiersprachen

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.05
- **Thema:** Programmspezifikationen festlegen, Datenmodelle und Strukturen aus fachlichen Anforderungen ableiten, Schnittstellen festlegen, geeignete Programmiersprachen auswaehlen

## Ziel

Du musst wissen, wie aus fachlichen Anforderungen technische Spezifikationen, Datenmodelle, Schnittstellendefinitionen und die Wahl der Programmiersprache abgeleitet werden.

## Grundlagen

### Programmspezifikationen festlegen

**Definition:** Programmspezifikationen beschreiben detailliert, was eine Software leisten soll und wie sie sich verhalten muss. Sie bilden die Grundlage fuer die Implementierung.

**Inhalte einer Spezifikation:**

| Bestandteil | Beschreibung |
|------------|-------------|
| Funktionale Anforderungen | Was das System tun soll (Eingabe → Verarbeitung → Ausgabe) |
| Nichtfunktionale Anforderungen | Performance, Sicherheit, Skalierbarkeit, Usability |
| Ein-/Ausgabespezifikation | Datenformate, Wertebereiche, Validierungsregeln |
| Algorithmen | Berechnungsvorschriften, Geschaeftslogik |
| Fehlerbehandlung | Reaktion auf ungueltige Eingaben, Systemfehler |
| Randbedingungen | Betriebssystem, Hardware, Abhaengigkeiten |

**Erklaerung:** Aus dem Pflichtenheft (3.4.01) werden die Programmspezifikationen abgeleitet. Waehrend das Pflichtenheft das Gesamtsystem beschreibt, geht die Programmspezifikation ins technische Detail fuer einzelne Module/Funktionen.

---

### Datenmodelle und Strukturen aus Anforderungen ableiten

**Definition:** Aus den fachlichen Anforderungen werden die Datenstrukturen abgeleitet, die das System benoetigt (Entitaeten, Attribute, Beziehungen).

**Vorgehen:**
1. Anforderungen analysieren → Substantive = Entitaeten
2. Eigenschaften der Entitaeten → Attribute
3. Beziehungen zwischen Entitaeten → Kardinalitaeten
4. ER-Modell erstellen
5. In relationales Modell ueberfuehren (Tabellen)
6. Normalisierung durchfuehren (1NF → 2NF → 3NF)

**Beispiel:**
> Anforderung: "Ein Kunde kann mehrere Bestellungen aufgeben. Jede Bestellung enthaelt mehrere Artikel."

| Schritt | Ergebnis |
|---------|---------|
| Entitaeten | Kunde, Bestellung, Artikel |
| Attribute | Kunde: KundenNr, Name; Bestellung: BestellNr, Datum; Artikel: ArtikelNr, Bezeichnung, Preis |
| Beziehungen | Kunde 1:n Bestellung, Bestellung n:m Artikel |
| Aufloesung n:m | Zwischentabelle BestellPosition (BestellNr, ArtikelNr, Menge) |

---

### Schnittstellen festlegen

**Definition:** Schnittstellen (Interfaces/APIs) definieren, wie verschiedene Systeme oder Module miteinander kommunizieren. Sie beschreiben Formate, Protokolle und Regeln fuer den Datenaustausch.

**Arten von Schnittstellen:**

| Art | Beschreibung | Beispiel |
|-----|-------------|---------|
| REST-API | HTTP-basierte Schnittstelle mit Ressourcen-URLs | GET /api/kunden/{id} |
| SOAP | XML-basiertes Protokoll mit WSDL-Beschreibung | Webservice fuer Bankdaten |
| Datei-Schnittstelle | Import/Export ueber Dateien | CSV-Import von Kundendaten |
| Datenbank-Schnittstelle | Direkter Zugriff auf eine Datenbank | JDBC/ODBC-Verbindung |
| Nachrichten-Queue | Asynchroner Nachrichtenaustausch | RabbitMQ, Apache Kafka |

**API-Vertrag (Contract):**

| Element | Beschreibung |
|---------|-------------|
| Endpoint / URL | Adresse der Schnittstelle |
| HTTP-Methode | GET, POST, PUT, DELETE |
| Request-Format | Eingabedaten (JSON, XML, Form-Data) |
| Response-Format | Ausgabedaten (JSON, XML) |
| Statuscodes | 200 OK, 201 Created, 400 Bad Request, 404 Not Found |
| Authentifizierung | API-Key, OAuth, JWT |

---

### Geeignete Programmiersprachen auswaehlen

**Definition:** Die Wahl der Programmiersprache haengt von fachlichen, technischen und organisatorischen Kriterien ab.

**Auswahlkriterien:**

| Kriterium | Beschreibung |
|-----------|-------------|
| Einsatzgebiet | Web, Desktop, Mobile, Embedded, Data Science |
| Performance | Hohe Performance → C, C++, Rust; moderate → Java, C# |
| Plattform | Plattformunabhaengig → Java, Python; Windows → C# |
| Oekosystem | Verfuegbarkeit von Bibliotheken und Frameworks |
| Team-Know-how | Vorhandene Kenntnisse im Team |
| Community/Support | Groesse der Community, Dokumentation |
| Lizenzkosten | Open Source vs. kommerzielle Tools |
| Wartbarkeit | Lesbarkeit, Typsicherheit, Tooling |

---

## Vertiefung

### Zusammenhang der vier Bereiche

```
  Lastenheft / Anforderungen
           |
           v
  +---------------------+
  | Programmspezifikation|
  +---------------------+
       |          |
       v          v
  +---------+  +---------------+
  | Daten-  |  | Schnittstellen|
  | modell  |  | (API-Vertrag) |
  +---------+  +---------------+
       |          |
       v          v
  +---------------------+
  | Programmiersprache   |
  | auswaehlen           |
  +---------------------+
           |
           v
     Implementierung
```

### Typische Pruefungsaspekte
- Aus einem Anforderungstext Entitaeten und Beziehungen ableiten
- REST-API-Endpunkte beschreiben (Methode, URL, Format)
- Kriterien fuer die Sprachauswahl nennen und begruenden
- Funktionale vs. nichtfunktionale Anforderungen unterscheiden

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| Spezifikation mit Lastenheft verwechselt | Spezifikation ist technischer, Lastenheft ist fachlich |
| n:m-Beziehung nicht aufgeloest | n:m-Beziehungen brauchen eine Zwischentabelle |
| API-Vertrag ohne Statuscodes | Fehlerfaelle muessen dokumentiert sein |
| Programmiersprache nur nach Vorliebe gewaehlt | Sachliche Kriterien (Einsatzgebiet, Performance, Team-Know-how) muessen begruendet werden |

---

## Uebungen

**Aufgabe 1:** Leite aus folgendem Anforderungstext die Entitaeten, Attribute und Beziehungen ab:
> "Ein Lehrer unterrichtet mehrere Faecher. Jedes Fach wird in mehreren Klassen unterrichtet. Schueler sind einer Klasse zugeordnet und erhalten Noten pro Fach."

**Aufgabe 2:** Beschreibe einen REST-API-Endpoint zum Abrufen aller Bestellungen eines Kunden. Nenne: HTTP-Methode, URL, Response-Format (Beispiel-JSON), moegliche Statuscodes.

**Aufgabe 3:** Ein Unternehmen moechte eine mobile App fuer Aussendienst-Mitarbeiter entwickeln. Die App soll auf iOS und Android laufen, Offline-Faehigkeit haben und auf eine bestehende REST-API zugreifen. Welche Programmiersprache/Technologie empfiehlst du? Begruende mit drei Kriterien.

---
---

# Loesungen

## Aufgabe 1

| Entitaet | Attribute |
|---------|-----------|
| Lehrer | LehrerNr, Name, Vorname |
| Fach | FachNr, Bezeichnung |
| Klasse | KlassenNr, Bezeichnung, Jahrgang |
| Schueler | SchuelerNr, Name, Vorname |
| Note | Wert, Datum |

**Beziehungen:**
- Lehrer n:m Fach (ein Lehrer unterrichtet mehrere Faecher, ein Fach kann von mehreren Lehrern unterrichtet werden)
- Fach n:m Klasse (ein Fach wird in mehreren Klassen unterrichtet)
- Schueler n:1 Klasse (ein Schueler gehoert zu genau einer Klasse)
- Schueler n:m Fach mit Attribut Note (Noten pro Fach und Schueler → Zwischentabelle)

## Aufgabe 2
- **HTTP-Methode:** GET
- **URL:** /api/kunden/{kundenId}/bestellungen
- **Response-Format (JSON):**
```json
[
  {
    "bestellNr": 1001,
    "datum": "2025-12-01",
    "status": "abgeschlossen",
    "gesamtPreis": 149.90
  },
  {
    "bestellNr": 1002,
    "datum": "2026-01-15",
    "status": "offen",
    "gesamtPreis": 89.50
  }
]
```
- **Statuscodes:** 200 OK (Bestellungen gefunden), 404 Not Found (Kunde existiert nicht), 401 Unauthorized (keine Berechtigung)

## Aufgabe 3
**Empfehlung: Flutter (Dart) oder React Native (JavaScript/TypeScript).**

Begruendung:
1. **Plattformuebergreifend:** Beide Technologien erzeugen aus einer Codebasis Apps fuer iOS und Android → geringerer Entwicklungsaufwand.
2. **Offline-Faehigkeit:** Beide Frameworks unterstuetzen lokale Datenbanken (z.B. SQLite) fuer Offline-Funktionalitaet.
3. **REST-API-Anbindung:** Beide bieten HTTP-Bibliotheken fuer die Kommunikation mit der bestehenden REST-API (z.B. Dio in Flutter, Axios in React Native).
