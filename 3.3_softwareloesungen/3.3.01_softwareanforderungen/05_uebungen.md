# 3.3.01 – Uebungen: Softwareanforderungen erfassen

## Aufgabe 1: Zuordnung Qualitaetsmerkmale

Ordne die folgenden Anforderungen dem passenden ISO-25010-Qualitaetsmerkmal zu:

| Nr. | Anforderung | Qualitaetsmerkmal? |
|-----|-------------|-------------------|
| a) | Das System antwortet innerhalb von 500ms | |
| b) | Der Quellcode hat eine Testabdeckung von > 80% | |
| c) | Die App laeuft auf Windows, macOS und Linux | |
| d) | Das System ist im Jahresmittel 99,9% erreichbar | |
| e) | Ein neuer Mitarbeiter kann das System nach 2h Schulung bedienen | |
| f) | Neue Module koennen ueber eine Plugin-Schnittstelle integriert werden | |
| g) | Die Volltextsuche findet alle relevanten Dokumente | |
| h) | Das System erfuellt die Vorgaben der ISO 9241 | |

---

## Aufgabe 2: Funktional oder nicht-funktional?

Klassifiziere die folgenden Anforderungen:

1. "Das System erstellt taeglich um 03:00 Uhr ein automatisches Backup."
2. "Die Datenbank kann 10 Millionen Datensaetze verwalten."
3. "Benutzer koennen ihr Passwort zuruecksetzen."
4. "Die Software unterstuetzt Screenreader."
5. "Reports koennen als PDF exportiert werden."
6. "Das System uebersteht den Ausfall eines Datenbankservers ohne Datenverlust."

---

## Aufgabe 3: Anforderungen messbar formulieren

Formuliere die folgenden Anforderungen messbar um:

a) "Das System soll schnell starten."
b) "Die Anwendung soll stabil laufen."
c) "Die Oberflaeche soll intuitiv sein."
d) "Das System soll erweiterbar sein."

---

## Aufgabe 4: Zielkonflikt-Analyse

Ein Kunde wuenscht sich fuer eine mobile Banking-App:
- Hoechste Sicherheit (2FA, biometrische Authentifizierung, automatisches Logout nach 2 Min.)
- Maximale Benutzerfreundlichkeit (schneller Zugriff, wenige Klicks, kein staendiges Einloggen)

**Frage**: Welcher Zielkonflikt besteht? Wie wuerdest du diesen loesen?

---

## Aufgabe 5: Pruefungstypische Zuordnung

Ein Softwareprojekt hat folgende Probleme. Welches Qualitaetsmerkmal ist jeweils betroffen?

a) Nach einem Serverausfall dauert die Wiederherstellung 12 Stunden.
b) Eine kleine Aenderung an Modul A fuehrt zu Fehlern in Modul B, C und D.
c) Die Software laeuft nur auf einer bestimmten Linux-Distribution.
d) Neue Mitarbeiter brauchen 3 Wochen Einarbeitung fuer einfache Aufgaben.
e) Bei 100 gleichzeitigen Nutzern bricht die Performance ein.

---
---

## Loesung Aufgabe 1

| Nr. | Anforderung | Qualitaetsmerkmal |
|-----|-------------|-------------------|
| a) | Antwortzeit 500ms | **Effizienz** (Zeitverhalten) |
| b) | Testabdeckung > 80% | **Wartbarkeit** (Testbarkeit) |
| c) | Windows, macOS, Linux | **Uebertragbarkeit** (Anpassbarkeit) |
| d) | 99,9% erreichbar | **Zuverlaessigkeit** (Verfuegbarkeit) |
| e) | 2h Schulung | **Benutzbarkeit** (Erlernbarkeit) |
| f) | Plugin-Schnittstelle | **Aenderbarkeit/Erweiterbarkeit** |
| g) | Volltextsuche findet alle Dokumente | **Funktionalitaet** (Vollstaendigkeit) |
| h) | ISO 9241 | **Normen anwenden** |

---

## Loesung Aufgabe 2

1. **Funktional** – beschreibt eine konkrete Systemfunktion (Backup erstellen)
2. **Nicht-funktional** – beschreibt die Kapazitaet (Effizienz)
3. **Funktional** – beschreibt eine konkrete Benutzerfunktion
4. **Nicht-funktional** – beschreibt Barrierefreiheit (Benutzbarkeit)
5. **Funktional** – beschreibt eine konkrete Exportfunktion
6. **Nicht-funktional** – beschreibt Fehlertoleranz (Zuverlaessigkeit)

---

## Loesung Aufgabe 3

a) "Die Applikation ist innerhalb von 5 Sekunden nach Start vollstaendig bedienbar (gemessen auf Referenzhardware: Intel i5, 8 GB RAM, SSD)."

b) "Das System laeuft im Dauerbetrieb (7x24h) mit einer Verfuegbarkeit von mindestens 99,5% pro Monat (max. 3,6h ungeplante Ausfallzeit)."

c) "90% der Testnutzer koennen ohne vorherige Schulung innerhalb von 5 Minuten eine Standardaufgabe (z.B. Bestellung aufgeben) erfolgreich abschliessen."

d) "Ein neues Modul kann innerhalb von maximal 5 Personentagen integriert werden, ohne bestehende Module zu veraendern. Die Plugin-Schnittstelle ist dokumentiert."

---

## Loesung Aufgabe 4

**Zielkonflikt**: Sicherheit vs. Benutzbarkeit

**Loesungsansatz**:
- **Biometrische Authentifizierung** (Fingerabdruck/Face ID) als Kompromiss: sicher UND schnell
- **Risiko-basierte Authentifizierung**: Bei bekanntem Geraet und normaler Nutzung weniger streng, bei unbekanntem Geraet oder hohen Betraegen strengere Pruefung
- **Session-Timeout differenzieren**: Lesen (z.B. Kontostand) = laengeres Timeout, Schreiben (z.B. Ueberweisung) = kuerzeres Timeout + erneute Authentifizierung
- **Push-Benachrichtigung statt manuellem 2FA-Code**: Schnellere Bestaetigung bei gleichem Sicherheitsniveau

---

## Loesung Aufgabe 5

a) **Zuverlaessigkeit** (Wiederherstellbarkeit) – Recovery Time ist zu hoch
b) **Wartbarkeit** / **Aenderbarkeit** – zu hohe Kopplung zwischen Modulen
c) **Uebertragbarkeit** (Anpassbarkeit) – keine Plattformunabhaengigkeit
d) **Benutzbarkeit** (Erlernbarkeit) – System ist zu komplex in der Einarbeitung
e) **Effizienz** (Kapazitaet/Zeitverhalten) – Skalierungsproblem
