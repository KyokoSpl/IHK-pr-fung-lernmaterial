# Vertiefung und Uebungen: 3.4.03 – Strukturierte Analyse- und Designverfahren

## Vertiefung

### Top-down vs. Bottom-up im Vergleich

| Kriterium | Top-down | Bottom-up |
|-----------|---------|-----------|
| Startpunkt | Gesamtsystem | Einzelne Bausteine |
| Richtung | Vom Grossen zum Kleinen | Vom Kleinen zum Grossen |
| Eignung | Neues System, keine Vorarbeiten | Bestehende Module vorhanden |
| Gesamtueberblick | Frueh vorhanden | Erst spaet sichtbar |
| Testbarkeit einzelner Module | Spaet (erst wenn Module implementiert) | Frueh (Module einzeln testbar) |
| Risiko | Detail-Probleme werden spaet entdeckt | Gesamtkonzept passt evtl. nicht |
| Beispiel | Neues ERP-System planen | Bestehende Bibliotheken integrieren |

### Kombination: Meet-in-the-Middle

In der Praxis werden Top-down und Bottom-up oft kombiniert:
- **Top-down:** Architektur des Gesamtsystems wird definiert
- **Bottom-up:** Vorhandene Bibliotheken und Module werden eingebunden
- Der Treffpunkt in der Mitte ergibt die Integrationsebene

### Qualitaetskriterien fuer gute Module

| Kriterium | Gut | Schlecht |
|-----------|-----|---------|
| Kohaesion | Alle Funktionen eines Moduls gehoeren zum gleichen Thema | Ein Modul macht Login, PDF-Export und Datenbankzugriff |
| Kopplung | Module kommunizieren nur ueber definierte Schnittstellen | Ein Modul greift direkt auf interne Variablen eines anderen Moduls zu |
| Groesse | Ueberschaubarer Umfang (eine klare Aufgabe) | Riesiges Modul mit hunderten Funktionen |
| Namensgebung | Sprechender Name: `BenutzerAuthentifizierung` | Unklarer Name: `Modul_A` |

### Typische Pruefungsaspekte
- Szenario lesen und Top-down oder Bottom-up empfehlen mit Begruendung
- Kohaesion und Kopplung definieren und bewerten
- Vorteile der Modularisierung nennen (mindestens drei)
- Zerlegung eines Problems in Module darstellen (Baumdiagramm)

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| Top-down und Bottom-up verwechselt | Top-down = vom Ganzen zum Detail, Bottom-up = vom Detail zum Ganzen |
| Hohe Kopplung als positiv bewertet | Hohe Kopplung = schlecht (starke Abhaengigkeit), niedrig = gut |
| Kohaesion mit Kopplung verwechselt | Kohaesion = innerhalb eines Moduls, Kopplung = zwischen Modulen |
| Modularisierung nur als Aufteilung in Dateien verstanden | Es geht um fachliche Trennung mit definierten Schnittstellen |

---

## Uebungen

**Aufgabe 1:** Erklaere den Unterschied zwischen Top-down- und Bottom-up-Entwurf in je zwei Saetzen. Nenne fuer jeden Ansatz ein Beispiel.

**Aufgabe 2:** Definiere die Begriffe Kohaesion und Kopplung. Welche Auspraegung ist jeweils erstrebenswert und warum?

**Aufgabe 3:** Ein Team soll eine Webanwendung fuer Terminbuchungen entwickeln. Es gibt bereits eine fertige Authentifizierungskomponente und eine E-Mail-Bibliothek. Die Gesamtarchitektur muss aber noch entworfen werden.
- a) Welcher Entwurfsansatz wird hier vermutlich kombiniert?
- b) Zerlege das System Top-down in mindestens drei Module.
- c) Welche bestehenden Bausteine koennen Bottom-up eingebunden werden?

**Aufgabe 4:** Bewerte das folgende Modul hinsichtlich Kohaesion und Kopplung:
> Modul "AllInOne": Benutzerverwaltung, Rechnungserstellung, E-Mail-Versand, Datenbankzugriff. Das Modul greift direkt auf globale Variablen anderer Module zu.

---

## Loesungen

**Aufgabe 1:**
- **Top-down:** Man beginnt mit dem Gesamtproblem und zerlegt es schrittweise in kleinere Teilprobleme. Beispiel: Ein neues ERP-System wird zuerst in die Module Lager, Buchhaltung und Personal aufgeteilt, dann weiter in Untermodule verfeinert.
- **Bottom-up:** Man beginnt mit den kleinsten Bausteinen und fuegt sie zum Gesamtsystem zusammen. Beispiel: Ein Entwickler baut zuerst Login, PDF-Export und Datenbankzugriff als einzelne Module und setzt sie dann zur Anwendung zusammen.

**Aufgabe 2:**
- **Kohaesion:** Beschreibt, wie stark die Bestandteile eines Moduls inhaltlich zusammengehoeren. Hohe Kohaesion ist erstrebenswert, weil das Modul dann eine klare, abgegrenzte Aufgabe hat und leicht zu verstehen, testen und warten ist.
- **Kopplung:** Beschreibt, wie stark Module voneinander abhaengig sind. Niedrige Kopplung ist erstrebenswert, weil Aenderungen in einem Modul dann keine Auswirkungen auf andere Module haben.

**Aufgabe 3:**
- a) **Meet-in-the-Middle** (Kombination aus Top-down und Bottom-up).
- b) Top-down-Zerlegung: (1) Terminverwaltung (Buchung, Stornierung, Uebersicht), (2) Benutzerverwaltung (Registrierung, Login, Profil), (3) Benachrichtigungssystem (E-Mail-Bestaetigungen, Erinnerungen).
- c) Bottom-up: Die fertige Authentifizierungskomponente (Login) und die E-Mail-Bibliothek (Benachrichtigungen) werden eingebunden.

**Aufgabe 4:**
- **Kohaesion: Niedrig (schlecht).** Das Modul vereint vier voellig unterschiedliche Aufgabengebiete (Benutzer, Rechnung, E-Mail, Datenbank). Jeder Bereich sollte ein eigenes Modul sein.
- **Kopplung: Hoch (schlecht).** Das Modul greift direkt auf globale Variablen anderer Module zu, statt definierte Schnittstellen zu verwenden. Aenderungen an einer Stelle koennen das gesamte System beeinflussen.
