# Ueberblick und Grundlagen: 3.5.03 – Code-Review / Versionsverwaltung

## Einordnung

- **Pruefungsteil:** 3.5 – Sicherstellen der Qualitaet von Softwareanwendungen
- **Thema-ID:** 3.5.03
- **Thema:** Code-Review und Versionsverwaltung kennen und anwenden koennen

## Themenkreise

### 1. Code-Review

**Definition:** Ein Code-Review ist die systematische Pruefung von Quellcode durch eine oder mehrere Personen, die den Code nicht selbst geschrieben haben. Ziel ist es, Fehler, Stilverstoesse und Verbesserungsmoeglichkeiten fruehzeitig zu erkennen.

**Kernaussagen:**
- Code-Review ist eine Form des **statischen Testens** (Code wird nicht ausgefuehrt)
- Erkennt Fehler frueh im Entwicklungsprozess → geringere Behebungskosten
- Foerdert Wissenstransfer im Team (alle lernen den Code kennen)
- Verbessert die Codequalitaet und -konsistenz
- Ist ein zentraler Bestandteil professioneller Softwareentwicklung

**Arten von Code-Reviews:**

| Art | Beschreibung | Formalitaet |
|---|---|---|
| **Pair Programming** | Zwei Entwickler arbeiten gleichzeitig am selben Code | Informell, kontinuierlich |
| **Peer Review** | Ein Kollege prueft den Code eines anderen Entwicklers | Mittel |
| **Pull Request Review** | Code-Aenderung wird als Pull/Merge Request eingereicht und muss vor dem Merge genehmigt werden | Formell, dokumentiert |
| **Walkthrough** | Der Autor stellt seinen Code dem Team vor und erklaert die Logik | Mittel |
| **Formale Inspektion** | Strukturierter Prozess mit definierten Rollen (Moderator, Autor, Gutachter, Protokollant) | Sehr formell |

**Ablauf eines Pull-Request-Reviews:**

```
Entwickler erstellt Feature-Branch
         |
         v
Code wird geschrieben und committet
         |
         v
Pull Request (PR) wird erstellt
         |
         v
Reviewer prueft den Code:
  - Logik und Korrektheit
  - Coding-Standards und Stil
  - Testabdeckung
  - Sicherheitsaspekte
         |
         v
Feedback (Kommentare, Aenderungswuensche)
         |
         v
Entwickler arbeitet Feedback ein
         |
         v
Approval → Merge in Hauptbranch
```

**Pruefkriterien bei einem Code-Review:**

| Kriterium | Fragen |
|---|---|
| Korrektheit | Macht der Code, was er soll? Gibt es logische Fehler? |
| Lesbarkeit | Ist der Code verstaendlich? Sind Variablennamen aussagekraeftig? |
| Standards | Werden Coding-Conventions eingehalten? |
| Testabdeckung | Gibt es Tests fuer den neuen Code? Sind Randfaelle abgedeckt? |
| Sicherheit | Gibt es SQL-Injection, XSS oder andere Schwachstellen? |
| Performance | Gibt es unnoetige Schleifen, N+1-Queries oder Speicherlecks? |
| Wartbarkeit | Ist der Code modular und erweiterbar? DRY-Prinzip eingehalten? |

**Wichtige Begriffe:**
- **Pull Request (PR) / Merge Request (MR)** – Anfrage, Code-Aenderungen in einen Branch zu uebernehmen
- **Approval** – Genehmigung des Reviews
- **Linting** – Automatische Pruefung auf Stilregeln (z.B. ESLint, Pylint, Checkstyle)
- **Statische Codeanalyse** – Automatische Pruefung auf potenzielle Fehler ohne Ausfuehrung (z.B. SonarQube)

---

### 2. Versionsverwaltung

**Definition:** Ein Versionsverwaltungssystem (VCS) zeichnet alle Aenderungen an Dateien (insbesondere Quellcode) auf, sodass jede Version nachvollziehbar, wiederherstellbar und vergleichbar ist.

**Kernaussagen:**
- Jede Aenderung wird als **Commit** gespeichert (mit Autor, Zeitstempel, Nachricht)
- Ermoeglicht paralleles Arbeiten mehrerer Entwickler am selben Projekt
- Aenderungen koennen rueckgaengig gemacht werden (Rollback)
- **Git** ist der de-facto-Standard fuer Versionsverwaltung
- Zentrale Plattformen: GitHub, GitLab, Bitbucket

**Arten von Versionsverwaltung:**

| Art | Beschreibung | Beispiel |
|---|---|---|
| **Lokal** | Versionen nur auf dem eigenen Rechner | RCS |
| **Zentral (CVCS)** | Ein zentraler Server speichert alle Versionen | SVN (Subversion) |
| **Verteilt (DVCS)** | Jeder Entwickler hat eine vollstaendige Kopie des Repositories | Git |

**Grundlegende Git-Befehle:**

| Befehl | Funktion |
|---|---|
| `git init` | Neues Repository erstellen |
| `git clone <url>` | Bestehendes Repository klonen |
| `git add <datei>` | Aenderungen zur Staging Area hinzufuegen |
| `git commit -m "Nachricht"` | Aenderungen festschreiben |
| `git push` | Lokale Commits zum Remote-Repository hochladen |
| `git pull` | Aenderungen vom Remote-Repository herunterladen und mergen |
| `git branch <name>` | Neuen Branch erstellen |
| `git checkout <branch>` | Zu einem Branch wechseln |
| `git merge <branch>` | Branch in den aktuellen Branch zusammenfuehren |
| `git log` | Commit-Historie anzeigen |
| `git diff` | Aenderungen zwischen Versionen vergleichen |
| `git stash` | Aktuelle Aenderungen zwischenspeichern |

**Branching-Strategien:**

| Strategie | Beschreibung | Eignung |
|---|---|---|
| **Gitflow** | Feste Branches: main, develop, feature/*, release/*, hotfix/* | Grosse Teams, geplante Releases |
| **Trunk-Based Development** | Alle arbeiten auf einem Hauptbranch (main/trunk), kurzlebige Feature-Branches | Kleine Teams, CI/CD, haeufige Deployments |
| **GitHub Flow** | Einfach: main + Feature-Branches, PR → Review → Merge → Deploy | Webprojekte, kontinuierliches Deployment |

**Gitflow im Detail:**

```
main ─────────●───────────────────●──────── (stabile Releases)
               \                 /
develop ────────●───●───●───●───●────────── (Entwicklung)
                 \     / \     /
feature/login ────●───●   \   /
                           \ /
feature/dashboard ──────────●
```

- **main:** Nur stabile, getestete Releases
- **develop:** Aktueller Entwicklungsstand
- **feature/*:** Neue Funktionen (werden in develop gemergt)
- **release/*:** Vorbereitung eines Releases (Bug-Fixes, Versionsnummer)
- **hotfix/*:** Dringende Fehlerbehebung direkt auf main

**Merge-Konflikte:**

**Definition:** Ein Merge-Konflikt entsteht, wenn zwei Branches dieselbe Stelle in einer Datei unterschiedlich veraendert haben und Git die Aenderungen nicht automatisch zusammenfuehren kann.

**Vorgehensweise bei Merge-Konflikten:**
1. Git meldet den Konflikt und markiert die betroffenen Stellen
2. Die Markierung sieht so aus:
```
<<<<<<< HEAD
Eigene Aenderung
=======
Aenderung aus dem anderen Branch
>>>>>>> feature/login
```
3. Entwickler entscheidet manuell, welche Version uebernommen wird
4. Konfliktmarker entfernen, Datei speichern
5. `git add <datei>` → `git commit` → Konflikt ist geloest

**Commit Best Practices:**

| Regel | Beispiel |
|---|---|
| Aussagekraeftige Commit-Nachricht | "Fix: Nullpointer bei leerem Warenkorb behoben" statt "Bug fix" |
| Kleine, atomare Commits | Ein Commit pro logischer Aenderung |
| Imperativform in der Nachricht | "Add login validation" statt "Added login validation" |
| Kein nicht-funktionierender Code | Jeder Commit sollte kompilierbar/lauffaehig sein |
| Referenz auf Ticket/Issue | "Fix #42: Validierung der E-Mail-Adresse ergaenzt" |

**CI/CD-Integration:**

| Schritt | Beschreibung |
|---|---|
| Commit + Push | Entwickler pusht Code ins Remote-Repository |
| CI-Pipeline startet | Automatischer Build, Lint-Check, Tests |
| Code-Review | PR wird von Reviewer geprueft und genehmigt |
| Merge | Code wird in develop/main gemergt |
| CD-Pipeline | Automatisches Deployment (Staging → Produktion) |

**Wichtige Begriffe:**
- **Repository (Repo)** – Speicherort fuer den gesamten Code und die Versionshistorie
- **Branch** – Unabhaengiger Entwicklungszweig
- **Merge** – Zusammenfuehren zweier Branches
- **Conflict** – Widerspruch bei automatischem Merge
- **Remote** – Entferntes Repository (z.B. auf GitHub)
- **HEAD** – Zeiger auf den aktuellen Commit im aktiven Branch

---

## Typische Pruefungsaspekte

- Vorteile von Code-Reviews benennen koennen
- Git-Befehle kennen und deren Funktion beschreiben
- Branching-Strategien vergleichen (Gitflow vs. Trunk-Based)
- Merge-Konflikte erklaeren und Loesungsschritte benennen
- Zusammenhang Code-Review → Pull Request → CI/CD erklaeren
- Unterschied zentrale vs. verteilte Versionsverwaltung

## Haeufige Fehler

| Fehler | Richtigstellung |
|---|---|
| Git und GitHub sind dasselbe | Nein – Git ist das Versionsverwaltungssystem, GitHub ist eine Plattform, die Git hostet |
| Code-Review ersetzt Tests | Nein – Code-Review ist statisches Testen, es braucht zusaetzlich dynamische Tests |
| Merge-Konflikte bedeuten, dass etwas falsch gemacht wurde | Nein – sie sind normal bei paralleler Entwicklung und muessen manuell geloest werden |
| main ist ein geschuetzter Branch, auf den niemand pushen darf | main kann geschuetzt konfiguriert werden, ist es aber nicht standardmaessig |
| Ein Commit kann nicht rueckgaengig gemacht werden | Doch – mit `git revert` (neuer Commit, der die Aenderung rueckgaengig macht) oder `git reset` |

---

## Beispiele

### Beispiel 1: Pull-Request-Workflow

**Szenario:** Eine Entwicklerin soll eine Login-Validierung implementieren.

1. Sie erstellt einen Feature-Branch: `git checkout -b feature/login-validation`
2. Sie implementiert die Validierung und schreibt Unit-Tests
3. Sie committet: `git commit -m "Add email and password validation for login"`
4. Sie pusht: `git push origin feature/login-validation`
5. Sie erstellt einen Pull Request auf GitHub mit Beschreibung der Aenderung
6. Ein Kollege prueft den Code:
   - Findet: Passwoerter unter 8 Zeichen werden nicht abgefangen
   - Kommentar: "Bitte Mindestlaenge-Pruefung ergaenzen"
7. Sie ergaenzt die Pruefung und pusht erneut
8. Kollege genehmigt den PR (Approval)
9. Merge in `develop` → CI-Pipeline fuehrt alle Tests aus → alles gruen

---

### Beispiel 2: Merge-Konflikt loesen

**Szenario:** Zwei Entwickler haben in der Datei `config.py` die gleiche Zeile geaendert.

Entwickler A (Branch `feature/timeout`):
```
TIMEOUT = 60
```

Entwickler B (Branch `feature/performance`):
```
TIMEOUT = 30
```

Beim Merge meldet Git einen Konflikt:
```
<<<<<<< HEAD
TIMEOUT = 60
=======
TIMEOUT = 30
>>>>>>> feature/performance
```

Loesung: Das Team entscheidet sich fuer einen Kompromiss:
```
TIMEOUT = 45
```

Anschliessend: `git add config.py` → `git commit -m "Resolve merge conflict: set TIMEOUT to 45"`

---

### Beispiel 3: Gitflow in der Praxis

**Szenario:** Ein Team entwickelt eine Webanwendung mit geplantem Release alle 4 Wochen.

| Phase | Branch | Aktivitaet |
|---|---|---|
| Sprint-Arbeit | feature/shopping-cart | Neues Feature entwickeln |
| Feature fertig | develop | Feature-Branch in develop mergen (nach PR-Review) |
| Release vorbereiten | release/2.1.0 | Versionsnummer setzen, letzte Bug-Fixes |
| Release freigeben | main | release-Branch in main mergen, Tag setzen (v2.1.0) |
| Kritischer Bug | hotfix/payment-fix | Bug direkt auf main-Basis fixen, in main und develop mergen |

---

## Uebungen

**Aufgabe 1:** Nenne drei Vorteile von Code-Reviews und erklaere, warum sie als statisches Testen gelten.

**Aufgabe 2:** Erklaere den Unterschied zwischen zentraler und verteilter Versionsverwaltung. Nenne je ein Beispiel und je einen Vor- und Nachteil.

**Aufgabe 3:** Ein Entwicklerteam arbeitet mit Gitflow. Beschreibe den Weg einer neuen Funktion vom ersten Code bis zum Release (Branch-Abfolge und Schritte).

---
---

# Loesungen

## Aufgabe 1

**Drei Vorteile:**
1. **Frueherkennung von Fehlern:** Logische Fehler, Sicherheitsluecken und Stilverstoesse werden erkannt, bevor der Code in den Hauptbranch gelangt.
2. **Wissenstransfer:** Alle Teammitglieder lernen den Code kennen, Wissen wird nicht auf einzelne Personen konzentriert (Bus-Faktor).
3. **Codequalitaet:** Konsistenter Codestil, Einhaltung von Standards und Best Practices werden sichergestellt.

**Statisches Testen:** Code-Reviews gelten als statisches Testen, weil der Code nicht ausgefuehrt wird. Der Reviewer liest und analysiert den Quellcode, ohne ihn zu kompilieren oder laufen zu lassen. Im Gegensatz dazu wird beim dynamischen Testen (z.B. Unit-Test) der Code tatsaechlich ausgefuehrt.

## Aufgabe 2

| Kriterium | Zentrale VCS (z.B. SVN) | Verteilte VCS (z.B. Git) |
|---|---|---|
| Prinzip | Ein zentraler Server speichert alle Versionen | Jeder Entwickler hat eine vollstaendige Kopie des Repos |
| Vorteil | Einfachere Verwaltung, klare Single Source of Truth | Offline-Arbeit moeglich, schnellere Operationen, kein Single Point of Failure |
| Nachteil | Server-Ausfall = keine Versionsverwaltung moeglich | Hoehere Komplexitaet, groesserer Speicherbedarf lokal |

## Aufgabe 3

1. Entwickler erstellt einen Feature-Branch vom `develop`-Branch: `git checkout -b feature/neue-funktion develop`
2. Code wird entwickelt, getestet und committet (mehrere Commits moeglich)
3. Pull Request wird erstellt: `feature/neue-funktion` → `develop`
4. Code-Review durch Kollegen, ggf. Aenderungen einarbeiten
5. Nach Approval: Merge in `develop`
6. Wenn genug Features fuer ein Release vorhanden sind: `release/x.y.z`-Branch von `develop` erstellen
7. Auf dem Release-Branch: Letzte Tests, Bug-Fixes, Versionsnummer setzen
8. Release-Branch in `main` mergen → Tag setzen (z.B. `v2.0.0`)
9. Release-Branch auch zurueck in `develop` mergen (damit Bug-Fixes nicht verloren gehen)
10. Deployment aus `main`
