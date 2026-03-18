# 3.3.01 – Beispiele: Softwareanforderungen erfassen

## Beispiel 1: Webshop-Anforderungen klassifizieren

Ein Unternehmen plant einen Online-Shop. Folgende Anforderungen wurden gesammelt:

| Nr. | Anforderung | Typ | Qualitaetsmerkmal |
|-----|-------------|-----|-------------------|
| A1 | Kunden koennen Produkte in den Warenkorb legen | Funktional | Funktionalitaet |
| A2 | Die Seite laedt in max. 2 Sekunden | Nicht-funktional | Effizienz |
| A3 | Der Shop laeuft auf Chrome, Firefox und Safari | Nicht-funktional | Uebertragbarkeit |
| A4 | Kunden koennen per Kreditkarte bezahlen | Funktional | Funktionalitaet |
| A5 | Das System ist 99,5% der Zeit erreichbar | Nicht-funktional | Zuverlaessigkeit |
| A6 | Neue Zahlungsarten koennen in < 2 Tagen integriert werden | Nicht-funktional | Aenderbarkeit |
| A7 | Ein neuer Nutzer findet die Suchfunktion ohne Hilfe | Nicht-funktional | Benutzbarkeit |
| A8 | Der Quellcode entspricht den firmeninternen Coding-Guidelines | Nicht-funktional | Wartbarkeit |

---

## Beispiel 2: Anforderungen messbar umformulieren

**Aufgabe**: Die folgenden vagen Anforderungen sollen messbar formuliert werden.

| Vage Anforderung | Messbare Anforderung |
|------------------|---------------------|
| "Das System soll performant sein" | "Die durchschnittliche Antwortzeit bei einer Datenbankabfrage betraegt max. 500ms bei 500 gleichzeitigen Nutzern" |
| "Die Software soll benutzerfreundlich sein" | "90% der Testnutzer koennen die Hauptaufgabe innerhalb von 3 Minuten ohne Hilfe abschliessen" |
| "Das System muss sicher sein" | "Alle Passwoerter werden mit bcrypt (min. 10 Rounds) gehasht; Brute-Force-Schutz nach 5 Fehlversuchen" |
| "Die Daten muessen gesichert werden" | "Taeglich um 02:00 Uhr erfolgt ein automatisches Backup; Recovery Point Objective (RPO) = 24h" |

---

## Beispiel 3: ISO 25010 in einem Projekt anwenden

**Szenario**: Eine Stadtverwaltung beauftragt die Entwicklung einer Buerger-App.

**Anforderungsanalyse nach ISO 25010**:

| Qualitaetsmerkmal | Konkrete Anforderung | Pruefkriterium |
|-------------------|---------------------|----------------|
| Funktionalitaet | Buerger koennen Termine online buchen | Buchung funktioniert Ende-zu-Ende |
| Effizienz | App startet in < 3 Sekunden | Gemessen auf Referenzgeraet (Mittelklasse-Smartphone) |
| Benutzbarkeit | App erfuellt WCAG 2.1 Level AA | Barrierefreiheitstest bestanden |
| Zuverlaessigkeit | App funktioniert auch bei schlechter Netzverbindung | Offline-Cache fuer geladene Daten |
| Wartbarkeit | Modularer Aufbau mit dokumentierter API | Code-Review-Checkliste erfuellt |
| Uebertragbarkeit | Verfuegbar fuer Android und iOS | Laeuft auf Android >= 10, iOS >= 15 |
| Aenderbarkeit | Neue Dienste koennen per Plugin ergaenzt werden | Plugin-Schnittstelle dokumentiert |

---

## Beispiel 4: Zielkonflikte erkennen

**Szenario**: Ein Echtzeit-Handelssystem (Trading-Plattform)

| Konflikt | Entscheidung | Begruendung |
|----------|-------------|-------------|
| Effizienz vs. Wartbarkeit | Effizienz bevorzugt | Millisekundengenauigkeit noetig, optimierter Code wichtiger als Lesbarkeit |
| Sicherheit vs. Benutzbarkeit | Sicherheit bevorzugt | Finanzbranche erfordert strenge Authentifizierung (2FA, Session-Timeout) |
| Funktionalitaet vs. Uebertragbarkeit | Funktionalitaet bevorzugt | Spezielle Trading-Features wichtiger als Multi-Plattform-Support |

**Fazit**: Die Priorisierung von Qualitaetsmerkmalen haengt vom Projektkontext und den Stakeholder-Beduerfnissen ab. In der Pruefung muss man Trade-offs begruenden koennen.

---

## Beispiel 5: Anforderungsdokument-Auszug

```
Projekt: Lagerverwaltungssystem "StockMaster 3.0"
Version: 1.2 | Datum: 15.03.2026

FUNKTIONALE ANFORDERUNGEN:
---------------------------------------------------------------------------
FA-001: Wareneingang erfassen
  Beschreibung: Das System muss den Wareneingang per Barcode-Scan erfassen.
  Eingabe:      EAN-13 Barcode
  Ausgabe:      Bestaetigung der Erfassung, aktualisierter Bestand
  Prioritaet:   Hoch

FA-002: Bestandsabfrage
  Beschreibung: Benutzer koennen den aktuellen Bestand je Artikel abfragen.
  Eingabe:      Artikelnummer oder Suchbegriff
  Ausgabe:      Artikelliste mit Menge, Lagerort, Status
  Prioritaet:   Hoch

NICHT-FUNKTIONALE ANFORDERUNGEN:
---------------------------------------------------------------------------
NFA-001: Performance
  Qualitaetsmerkmal: Effizienz
  Beschreibung:      Die Bestandsabfrage liefert Ergebnisse in < 1 Sekunde
                     bei einem Datenbestand von bis zu 500.000 Artikeln.
  Metrik:            Antwortzeit in Millisekunden

NFA-002: Verfuegbarkeit
  Qualitaetsmerkmal: Zuverlaessigkeit
  Beschreibung:      Das System ist werktags 06:00-22:00 verfuegbar
                     mit einer Verfuegbarkeit von mindestens 99,5%.
  Metrik:            Verfuegbarkeit in Prozent pro Monat
```
