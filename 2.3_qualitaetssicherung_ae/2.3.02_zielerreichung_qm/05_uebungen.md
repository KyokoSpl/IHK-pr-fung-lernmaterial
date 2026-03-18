# Uebungen: 2.3.02 – Methoden zur Messung der Zielerreichung im QM-Prozess

## Aufgabe 1: Soll-Ist-Vergleich berechnen
Ein IT-Dienstleister hat folgende SLA-Kennzahlen vereinbart und gemessen:

| Kennzahl | Soll (SLA) | Ist |
|---|---|---|
| Verfuegbarkeit | 99,5% | 98,8% |
| Reaktionszeit | max. 2h | 2,5h |
| Loesung innerhalb | max. 8h | 7h |
| Kundenzufriedenheit | > 4,0 | 4,2 |

a) Berechne die Abweichungen (absolut und relativ).
b) Welche SLA-Werte wurden eingehalten, welche nicht?
c) Welche Massnahme wuerdest du fuer die kritischste Abweichung vorschlagen?

---
---

**Loesung Aufgabe 1:**
a)
- Verfuegbarkeit: 98,8 - 99,5 = -0,7 PP → SLA verletzt
- Reaktionszeit: 2,5 - 2 = +0,5h (+25%) → SLA verletzt
- Loesungszeit: 7 - 8 = -1h (-12,5%) → SLA eingehalten (besser als Soll)
- Kundenzufriedenheit: 4,2 - 4,0 = +0,2 → SLA eingehalten

b) Eingehalten: Loesungszeit und Kundenzufriedenheit. Verletzt: Verfuegbarkeit und Reaktionszeit.

c) Kritischste Abweichung: **Verfuegbarkeit** (98,8% statt 99,5% = ca. 6h zusaetzliche Ausfallzeit pro Monat). Massnahme: Ursache der Ausfaelle analysieren (z.B. Hardware, Netzwerk), Redundanz erhoehen (z.B. Cluster, Failover), Monitoring-Schwellwerte anpassen, um Probleme frueher zu erkennen.

---

## Aufgabe 2: PDCA anwenden
Die Fehlerquote in einem Softwareprojekt betraegt 5% (Ziel: < 2%). Beschreibe einen vollstaendigen PDCA-Zyklus zur Verbesserung.

---
---

**Loesung Aufgabe 2:**
- **Plan:** Fehlerursachen analysieren (z.B. fehlende Code-Reviews, unzureichende Tests). Massnahme planen: Pflicht-Code-Review vor jedem Merge einfuehren und Testabdeckung auf min. 80% erhoehen.
- **Do:** Code-Review-Richtlinie erstellen, in Teammeeting vorstellen. CI/CD-Pipeline um Test-Coverage-Check erweitern. 6 Wochen Pilotphase.
- **Check:** Nach 6 Wochen messen: Fehlerquote von 5% auf 2,3% gesunken. Testabdeckung von 55% auf 78% gestiegen. Ziel noch nicht ganz erreicht.
- **Act:** Code-Review als Standard beibehalten. Zusaetzlich: Pair Programming fuer komplexe Module einfuehren. Neues Ziel: Testabdeckung > 85%, Fehlerquote < 1,5%. Naechsten PDCA-Zyklus starten.

---

## Aufgabe 3: Testprotokoll erstellen
Erstelle ein Testprotokoll mit mindestens 4 Testfaellen fuer eine Login-Funktion (Benutzername + Passwort).

---
---

**Loesung Aufgabe 3:**

| Nr | Beschreibung | Eingabe | Erwartet | Ergebnis | Status |
|---|---|---|---|---|---|
| T-01 | Gueltige Anmeldung | admin / Pass123! | Dashboard | Dashboard | Bestanden |
| T-02 | Falsches Passwort | admin / falsch | Fehlermeldung | Fehlermeldung | Bestanden |
| T-03 | Leerer Benutzername | "" / Pass123! | Validierungsfehler | Validierungsfehler | Bestanden |
| T-04 | SQL-Injection | ' OR 1=1 -- / x | Fehlermeldung | Login erfolgreich! | **Fehlgeschlagen** |
| T-05 | 3x falsches Passwort | admin / falsch (3x) | Account gesperrt | Erneuter Versuch moeglich | **Fehlgeschlagen** |

Tester: M. Schmidt | Datum: 15.03.2024 | Version: 1.2.0 | Umgebung: Testserver

---

## Aufgabe 4: Abnahmeprotokoll beurteilen
Ein Abnahmeprotokoll enthaelt folgenden Eintrag:
"Software wurde am 01.03.2024 installiert. Laeuft."
a) Welche Informationen fehlen?
b) Welche Risiken entstehen durch ein unvollstaendiges Abnahmeprotokoll?

---
---

**Loesung Aufgabe 4:**
a) Fehlende Informationen: (1) Projektbezeichnung und Versionsnummer. (2) Auftraggeber und Auftragnehmer mit Unterschriften. (3) Konkreter Abnahmegegenstand (was genau wurde installiert?). (4) Pruefergebnisse / durchgefuehrte Tests. (5) Maengelliste oder Feststellung "keine Maengel". (6) Abnahmestatus (abgenommen / unter Vorbehalt / verweigert). (7) Nachbesserungsfristen.
b) Risiken: (1) Keine klare Verteilung der Verantwortung bei spaeter auftretenden Problemen. (2) Gewaehrleistungsansprueche sind schwer durchsetzbar. (3) Keine Grundlage fuer Nachbesserungsforderungen. (4) Streitigkeiten ueber den Leistungsumfang.
