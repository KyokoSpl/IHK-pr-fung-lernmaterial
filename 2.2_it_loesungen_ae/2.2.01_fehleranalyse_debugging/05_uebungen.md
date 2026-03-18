# Uebungen: 2.2.01 – Fehler erkennen, analysieren und beheben

## Aufgabe 1: Fehlerarten zuordnen
Ordne die folgenden Fehler der richtigen Fehlerart zu (Syntax, Laufzeit, Logik):
a) `int x = 10 / 0;`
b) `if (alter >= 18) { print("Minderjaehrig"); }`
c) `int[] arr = new int[5]; arr[5] = 10;`
d) `System.out.println("Hallo"` (fehlende Klammer)

---
---

**Loesung Aufgabe 1:**
a) **Laufzeitfehler** – Division durch 0 wird erst bei Ausfuehrung erkannt.
b) **Logikfehler** – Programm laeuft, aber Bedingung und Ausgabe passen nicht zusammen (>= 18 = volljaehrig, nicht minderjaehrig).
c) **Laufzeitfehler** – Array hat Index 0-4, Index 5 = ArrayIndexOutOfBounds.
d) **Syntaxfehler** – Fehlende schliessende Klammer, wird vom Compiler erkannt.

---

## Aufgabe 2: Testverfahren zuordnen
Ordne die folgenden Aktivitaeten dem richtigen Testverfahren zu:
a) Ein Kollege liest deinen Code und sucht nach Fehlern
b) Du testest eine Funktion mit verschiedenen Eingabewerten, ohne den Code zu kennen
c) Du pruefst, ob jeder If-Zweig im Code mindestens einmal durchlaufen wird
d) Du fuehrst eine automatische Pruefung des Codes auf Stilfehler durch

---
---

**Loesung Aufgabe 2:**
a) **Review** (statisches Testverfahren)
b) **Black-Box-Test** (dynamisches Testverfahren)
c) **White-Box-Test** / Zweigueberdeckung (dynamisch)
d) **Statische Analyse** / Linter (statisches Testverfahren)

---

## Aufgabe 3: Testdaten erstellen
Eine Funktion erwartet ein Passwort mit folgenden Regeln:
- Laenge: mindestens 8, maximal 20 Zeichen
- Mindestens ein Grossbuchstabe
- Mindestens eine Ziffer

Erstelle Testdaten mit Aequivalenzklassen und Grenzwerten (mind. 6 Testfaelle).

---
---

**Loesung Aufgabe 3:**

| Nr. | Testdaten | AEK | Erwartung |
|---|---|---|---|
| 1 | "Ab1" (3 Zeichen) | Ungueltig: zu kurz | Abgelehnt |
| 2 | "Abcdefg1" (8 Zeichen) | Gueltig: Untergrenze | Akzeptiert |
| 3 | "Passwort123" (11 Zeichen) | Gueltig: Mitte | Akzeptiert |
| 4 | "AbcdefghijklmnopQrs1" (20 Z.) | Gueltig: Obergrenze | Akzeptiert |
| 5 | "AbcdefghijklmnopQrs12" (21 Z.) | Ungueltig: zu lang | Abgelehnt |
| 6 | "abcdefgh1" (kein Grossbuchstabe) | Ungueltig: Regel verletzt | Abgelehnt |
| 7 | "Abcdefgh" (keine Ziffer) | Ungueltig: Regel verletzt | Abgelehnt |

---

## Aufgabe 4: Git-Workflow
Beschreibe den korrekten Git-Workflow fuer folgendes Szenario:
Zwei Entwickler (A und B) arbeiten parallel an unterschiedlichen Features. A entwickelt ein Login, B entwickelt eine Suchfunktion. Beide sollen ihre Aenderungen in den main-Branch integrieren.

---
---

**Loesung Aufgabe 4:**
1. Beide starten von einem aktuellen `main`-Branch: `git pull origin main`
2. **A:** `git checkout -b feature/login` → entwickelt Login-Funktion → `git commit` → `git push origin feature/login`
3. **B:** `git checkout -b feature/suche` → entwickelt Suchfunktion → `git commit` → `git push origin feature/suche`
4. **A:** Erstellt Pull Request fuer feature/login. Nach Review: Merge in main.
5. **B:** Vor eigenem Merge: `git checkout feature/suche` → `git merge main` (A's Aenderungen einbinden) → eventuelle Konflikte loesen → `git push`
6. **B:** Erstellt Pull Request fuer feature/suche. Nach Review: Merge in main.
7. Beide: Feature-Branches loeschen: `git branch -d feature/login` bzw. `feature/suche`
