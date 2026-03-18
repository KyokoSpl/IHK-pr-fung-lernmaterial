# Vertiefung und Uebungen: 3.5.02 – Qualitaetssicherung von Softwareanwendungen

## Vertiefung

### Teststufen im V-Modell – Detaillierter Vergleich

| Kriterium | Unit-Test | Integrationstest | Systemtest | Abnahmetest |
|---|---|---|---|---|
| Testgegenstand | Einzelne Funktion/Methode | Schnittstellen, Module | Gesamtsystem | Gesamtsystem aus Kundensicht |
| Testbasis | Quellcode | Technischer Entwurf | Pflichtenheft | Lastenheft / Vertrag |
| Testverfahren | White-Box | White-Box / Grey-Box | Black-Box | Black-Box |
| Durchfuehrung | Entwickler | Entwickler / Tester | Testteam | Kunde / Auftraggeber |
| Automatisierung | Hoch (JUnit, pytest) | Mittel | Teilweise (Selenium) | Gering (manuell) |
| Fehlerkosten | Gering | Mittel | Hoch | Sehr hoch |

### Regressionstest und CI/CD

**Regressionstest in der Praxis:**

```
Code-Aenderung
     |
     v
Commit → CI-Pipeline startet automatisch
     |
     v
Unit-Tests → Integrationstests → Systemtests
     |
     v
Alle Tests bestanden?
     |          |
    JA         NEIN
     |          |
     v          v
  Deploy    Build bricht ab
             → Entwickler wird benachrichtigt
```

**Kernaussagen:**
- Regressionstests stellen sicher, dass neue Aenderungen keine bestehenden Funktionen brechen
- In CI/CD-Pipelines werden Regressionstests automatisch bei jedem Commit ausgefuehrt
- Testautomatisierung ist Voraussetzung fuer effektive Regressionstests
- Testabdeckung (Code Coverage) wird als Qualitaetsmetrik gemessen
- Gute Praxis: Mindestens 80% Code Coverage als Ziel

**CI/CD und Testing:**

| CI/CD-Phase | Testarten | Automatisierung |
|---|---|---|
| Continuous Integration | Unit-Tests, Lint-Checks | Vollautomatisch |
| Continuous Delivery | Integrations-, Systemtests | Weitgehend automatisch |
| Continuous Deployment | Smoke-Tests, Monitoring | Automatisch nach Deployment |

### Testplanung und Testdokumentation

**Bestandteile eines Testplans:**

| Element | Beschreibung |
|---|---|
| Testziele | Was soll mit den Tests erreicht werden? |
| Testumfang (Scope) | Welche Funktionen werden getestet? |
| Teststrategie | Welche Testarten und -verfahren? |
| Testumgebung | Hardware, Software, Daten |
| Zeitplan | Wann wird welche Teststufe durchgefuehrt? |
| Verantwortlichkeiten | Wer testet was? |
| Abbruchkriterien | Wann werden Tests abgebrochen? |
| Abnahmekriterien | Wann gelten Tests als bestanden? |

**Testfallbeschreibung (Aufbau):**

| Feld | Beispiel |
|---|---|
| Testfall-ID | TC-001 |
| Beschreibung | Login mit gueltigem Benutzernamen und Passwort |
| Vorbedingung | Benutzer ist registriert, nicht eingeloggt |
| Eingabe | Benutzername: "max", Passwort: "Geheim123!" |
| Erwartetes Ergebnis | Weiterleitung auf Dashboard, Begruessung "Hallo Max" |
| Tatsaechliches Ergebnis | (wird bei Durchfuehrung eingetragen) |
| Status | Bestanden / Nicht bestanden |

### Statisches vs. Dynamisches Testen

| Kriterium | Statisches Testen | Dynamisches Testen |
|---|---|---|
| Code wird ausgefuehrt | Nein | Ja |
| Methoden | Code-Review, Walkthrough, Lint-Tools | Unit-Test, Systemtest, Lasttest |
| Zeitpunkt | Frueh (schon vor Kompilierung) | Nach Implementierung |
| Findet | Stilfehler, potenzielle Bugs, Regelverletzungen | Laufzeitfehler, funktionale Fehler |

### Typische Pruefungsaspekte

- V-Modell zeichnen und Teststufen zuordnen koennen
- Unterschied Verifikation vs. Validierung erklaeren
- Geeignete Testart/Teststufe fuer ein Szenario bestimmen
- Regressionstests im Kontext von CI/CD einordnen
- Testfaelle aus Anforderungen ableiten
- Integrationsteststrategie (Top-Down, Bottom-Up, Big-Bang) vergleichen

### Haeufige Fehler

| Fehler | Richtigstellung |
|---|---|
| Testarten und Teststufen werden verwechselt | Testarten = WAS wird geprueft (Funktion, Last). Teststufen = WANN/AUF WELCHER EBENE (Unit, System) |
| Der Abnahmetest wird vom Entwickler durchgefuehrt | Nein – der Abnahmetest wird vom Kunden/Auftraggeber durchgefuehrt |
| Regressionstests sind nur bei grossen Projekten noetig | Nein – auch kleine Aenderungen koennen bestehende Funktionen brechen |
| V-Modell = Wasserfallmodell | Nein – das V-Modell ergaenzt das Wasserfall um die Testseite (Verifikation) |
| Unit-Tests garantieren fehlerfreie Software | Nein – sie pruefen nur einzelne Bausteine, nicht das Zusammenspiel |

---

## Uebungen

**Aufgabe 1:** Ordne die folgenden Aktivitaeten der korrekten Teststufe im V-Modell zu:
- a) Der Kunde prueft, ob die Software seine Geschaeftsprozesse korrekt abbildet.
- b) Ein Entwickler testet eine einzelne Methode zur Berechnung des Nettopreises.
- c) Das Testteam prueft, ob die Datenbankanbindung mit dem REST-API korrekt funktioniert.
- d) Das Testteam fuehrt einen End-to-End-Test der gesamten Anwendung durch.

**Aufgabe 2:** Erklaere den Unterschied zwischen Verifikation und Validierung. Gib je ein Beispiel.

**Aufgabe 3:** Ein Entwicklungsteam hat einen Bug in der Benutzerverwaltung behoben. Welche Testart sollte anschliessend durchgefuehrt werden und warum? Wie laesst sich diese Testart in einer CI/CD-Pipeline integrieren?

---

## Loesungen

**Aufgabe 1:**
- a) **Abnahmetest** – Der Kunde prueft gegen seine Anforderungen (Lastenheft/Vertrag)
- b) **Unit-Test** – Einzelne Methode wird isoliert getestet
- c) **Integrationstest** – Zusammenspiel zweier Komponenten (Datenbank + API) wird geprueft
- d) **Systemtest** – Gesamtsystem wird gegen die Spezifikation (Pflichtenheft) getestet

**Aufgabe 2:**
- **Verifikation:** "Bauen wir das Produkt richtig?" – Pruefung, ob die Implementierung der Spezifikation entspricht. Beispiel: Ein Unit-Test prueft, ob die Methode `berechneNetto(119.00)` den Wert `100.00` zurueckgibt (wie im technischen Entwurf spezifiziert).
- **Validierung:** "Bauen wir das richtige Produkt?" – Pruefung, ob das System die tatsaechlichen Beduerfnisse des Kunden erfuellt. Beispiel: Der Kunde prueft im Abnahmetest, ob die Rechnungserstellung seinen Geschaeftsprozess vollstaendig abbildet.

**Aufgabe 3:**
- Testart: **Regressionstest** – Damit wird sichergestellt, dass der Bug-Fix keine bestehenden Funktionen beeintraechtigt hat.
- Begruendung: Aenderungen am Code koennen Seiteneffekte haben. Regressionstests decken solche unbeabsichtigten Auswirkungen auf.
- CI/CD-Integration: Die Regressionstests werden als automatisierte Testsuite in die CI-Pipeline integriert. Bei jedem Commit/Merge wird die Testsuite automatisch ausgefuehrt. Schlaegt ein Test fehl, bricht der Build ab und der Entwickler wird benachrichtigt. So wird verhindert, dass fehlerhafter Code in die Produktivumgebung gelangt.
