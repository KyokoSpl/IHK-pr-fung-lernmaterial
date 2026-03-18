# Grundlagen: 2.2.01 – Fehler erkennen, analysieren und beheben

## Debugging und Breakpoints

**Definition:** Debugging ist der systematische Prozess der Fehlersuche und -behebung in Software.

**Breakpoint:** Ein Haltepunkt im Quellcode, an dem die Programmausfuehrung pausiert wird, um den Zustand zu inspizieren.

**Debugging-Werkzeuge:**

| Werkzeug | Funktion |
|---|---|
| Breakpoint | Programm an bestimmter Zeile anhalten |
| Step Over | Naechste Zeile ausfuehren (Funktionen ueberspringen) |
| Step Into | In Funktionsaufruf hineinspringen |
| Step Out | Aktuelle Funktion bis zum Ende ausfuehren |
| Watch | Variable ueberwachen |
| Call Stack | Aufrufhierarchie anzeigen |
| Conditional Breakpoint | Nur anhalten, wenn Bedingung erfuellt |

**Fehlerarten:**

| Fehlerart | Beschreibung | Beispiel |
|---|---|---|
| Syntaxfehler | Regelverstoss der Sprache | Fehlende Klammer, Semikolon |
| Laufzeitfehler | Fehler waehrend Ausfuehrung | Division durch 0, NullPointer |
| Logikfehler | Falsches Ergebnis, kein Absturz | Falsche Berechnung, endlose Schleife |

---

## Teststufen

```
+-------------------+
| Systemtest        |  ← Gesamtsystem im Einsatzkontext
+-------------------+
         ^
+-------------------+
| Integrationstest  |  ← Zusammenspiel der Module
+-------------------+
         ^
+-------------------+
| Komponententest    |  ← Einzelne Module/Klassen
| (Unit-Test)       |
+-------------------+
```

| Teststufe | Was wird getestet? | Wer testet? |
|---|---|---|
| Komponententest (Unit) | Einzelne Funktionen/Klassen | Entwickler |
| Integrationstest | Zusammenspiel mehrerer Module | Entwickler/Tester |
| Systemtest | Gesamtsystem gegen Anforderungen | Tester/QA |
| Abnahmetest | Kundensicht, Akzeptanz | Kunde/Auftraggeber |

---

## Testverfahren

### Statische Testverfahren (ohne Ausfuehrung)

| Verfahren | Beschreibung |
|---|---|
| Review | Manuelle Pruefung des Codes durch Kollegen |
| Code-Inspektion | Formale Pruefung mit Checkliste |
| Statische Analyse | Automatische Pruefung (Linter, SonarQube) |
| Walkthrough | Entwickler fuehrt Reviewer durch den Code |

### Dynamische Testverfahren (mit Ausfuehrung)

| Verfahren | Beschreibung | Kenntnis des Codes |
|---|---|---|
| Black-Box-Test | Test anhand Spezifikation, Code unbekannt | Nein |
| White-Box-Test | Test anhand Code-Struktur | Ja |
| Grey-Box-Test | Teilwissen ueber Code | Teilweise |

**Black-Box-Methoden:**
- Aequivalenzklassenbildung (gueltige/ungueltige Eingaben)
- Grenzwertanalyse (Extremwerte testen)
- Zustandsbasierter Test

**White-Box-Methoden:**
- Anweisungsueberdeckung (jede Zeile mindestens 1x)
- Zweigueberdeckung (jeder Zweig mindestens 1x)
- Pfadueberdeckung (jeder Pfad mindestens 1x)

---

## Testdaten

**Erstellung von Testdaten:**

| Methode | Beschreibung | Beispiel |
|---|---|---|
| Aequivalenzklassen | Repraesentative Werte pro Klasse | Alter: <0 (ungueltig), 0-17, 18-65, >65 |
| Grenzwerte | Werte an den Grenzen | 17, 18, 65, 66 |
| Zufallsdaten | Generierte Testdaten | Testdatengeneratoren |
| Produktivdaten (anonymisiert) | Reale Daten ohne Personenbezug | Pseudonymisierte Kundendaten |

---

## Versionsmanagement (Git)

**Grundbegriffe:**

| Begriff | Beschreibung |
|---|---|
| Repository | Projektverzeichnis mit Versionshistorie |
| Commit | Gespeicherter Aenderungsstand mit Nachricht |
| Branch | Paralleler Entwicklungszweig |
| Merge | Zusammenfuehren zweier Branches |
| Pull | Aenderungen vom Server holen |
| Push | Lokale Aenderungen auf Server uebertragen |
| Conflict | Widerspruch beim Merge (manuell loesen) |
| Tag | Markierung eines bestimmten Standes (z.B. v1.0) |

**Typischer Workflow:**

```
main ─────●─────●─────────────●───── (stabile Version)
            \                /
feature ─────●──●──●──●────●  (neue Funktion)
                          merge
```
