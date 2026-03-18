# Uebungen: 3.4.07 – Software-Entwicklungswerkzeuge

## Compiler, Interpreter, Linker

**Aufgabe 1:** Erklaere den Unterschied zwischen Compiler und Interpreter. Nenne je zwei Beispielsprachen.

**Aufgabe 2:** Beschreibe die Aufgabe des Linkers im Build-Prozess. Was ist der Unterschied zwischen statischem und dynamischem Linken?

**Aufgabe 3:** Ordne die folgenden Fehlermeldungen dem passenden Werkzeug zu (Compiler, Linker, Debugger, Laufzeitumgebung):
- a) "Syntax error: unexpected token '(' in line 42"
- b) "undefined reference to 'berechneRabatt'"
- c) "NullPointerException at line 87"
- d) "Variable 'summe' has value 0 at breakpoint"

---

## IDE, Editor, Debugger

**Aufgabe 4:** Nenne drei Unterschiede zwischen einer IDE und einem einfachen Editor.

**Aufgabe 5:** Erklaere die Debugger-Funktionen "Breakpoint", "Step into" und "Watch" in je einem Satz.

**Aufgabe 6:** Ein Programm berechnet die Summe einer Liste, gibt aber immer 0 aus. Beschreibe in drei Schritten, wie du den Fehler mit einem Debugger finden wuerdest.

---

## Versionsverwaltung

**Aufgabe 7:** Erklaere die Git-Begriffe: Repository, Commit, Branch, Merge, Pull Request.

**Aufgabe 8:** Zwei Entwickler arbeiten am gleichen Projekt. Entwickler A aendert die Datei `login.js`, Entwickler B aendert die gleiche Datei. Beschreibe, was beim Merge passiert und wie ein Konflikt geloest wird.

---

## Testsoftware, Programmgenerator

**Aufgabe 9:** Ordne die folgenden Testart den passenden Werkzeugen zu:
- a) Unit-Test
- b) GUI-Test
- c) Lasttest
- d) Statische Analyse

**Aufgabe 10:** Nenne zwei Vorteile eines Programmgenerators und ein Beispiel fuer seinen Einsatz.

---
---

# Loesungen

## Aufgabe 1
- **Compiler:** Uebersetzt den gesamten Quellcode vor der Ausfuehrung in Maschinen- oder Bytecode. Fehler werden zur Compile-Zeit erkannt. Beispiele: C (gcc), Java (javac).
- **Interpreter:** Fuehrt den Quellcode zeilenweise zur Laufzeit aus. Fehler werden erst zur Laufzeit erkannt. Beispiele: Python, JavaScript (Node.js).

## Aufgabe 2
Der Linker verbindet kompilierte Objektdateien (.o, .obj) und Bibliotheken zu einem ausfuehrbaren Programm. Er loest externe Referenzen auf (z.B. Funktionsaufrufe zwischen Dateien).
- **Statisches Linken:** Bibliothekscode wird in die Programmdatei kopiert. Ergebnis ist eigenstaendig, aber groesser.
- **Dynamisches Linken:** Programm verweist auf externe Bibliotheken (.so, .dll), die zur Laufzeit geladen werden. Ergebnis ist kleiner, aber abhaengig von der installierten Bibliothek.

## Aufgabe 3
- a) **Compiler** – Syntaxfehler werden zur Compile-Zeit erkannt
- b) **Linker** – Fehlende Funktion in den Objektdateien (externe Referenz nicht aufgeloest)
- c) **Laufzeitumgebung** – Fehler tritt erst bei der Programmausfuehrung auf
- d) **Debugger** – Variablenwert an einem Breakpoint inspiziert

## Aufgabe 4
| Kriterium | IDE | Editor |
|-----------|-----|--------|
| Build/Kompilierung | Integriert (ein Klick) | Nicht integriert (extern) |
| Debugger | Eingebaut (Breakpoints, Watch) | Nicht vorhanden (ohne Plugin) |
| Projektverwaltung | Grosse Projekte mit Navigation | Einzelne Dateien |

## Aufgabe 5
- **Breakpoint:** Ein markierter Punkt im Code, an dem die Programmausfuehrung angehalten wird, sodass man den aktuellen Zustand inspizieren kann.
- **Step into:** Die Ausfuehrung springt in die aufgerufene Funktion hinein, um deren internen Ablauf Zeile fuer Zeile zu verfolgen.
- **Watch:** Eine Variable wird dauerhaft ueberwacht – ihr aktueller Wert wird bei jedem Ausfuehrungsschritt angezeigt.

## Aufgabe 6
1. Breakpoint an der Zeile setzen, die die Summe berechnet (z.B. innerhalb der Schleife).
2. Programm im Debug-Modus starten und am Breakpoint die Variable `summe` und die Listenelemente inspizieren.
3. Schrittweise durch die Schleife gehen (Step over) und pruefen, ob `summe` sich bei jedem Durchlauf korrekt aendert. Falls nicht: Logikfehler in der Berechnung identifizieren (z.B. Zuweisung statt Addition).

## Aufgabe 7
- **Repository:** Projektverzeichnis mit vollstaendiger Aenderungshistorie.
- **Commit:** Gespeicherter Satz von Aenderungen mit einer beschreibenden Nachricht.
- **Branch:** Paralleler Entwicklungszweig, in dem unabhaengig gearbeitet werden kann.
- **Merge:** Zusammenfuehren zweier Branches (z.B. Feature-Branch in main).
- **Pull Request:** Anfrage an das Team, einen Branch zu ueberpruefen (Code Review) und in einen anderen Branch zu mergen.

## Aufgabe 8
Wenn beide Entwickler unterschiedliche Stellen in `login.js` geaendert haben, kann Git die Aenderungen automatisch zusammenfuehren (Auto-Merge). Wenn beide dieselbe Zeile geaendert haben, entsteht ein **Merge-Konflikt**. Git markiert die betroffenen Stellen mit Konfliktmarkierungen (`<<<<<<<`, `=======`, `>>>>>>>`). Die Entwickler muessen den Konflikt manuell loesen, indem sie die gewuenschte Version auswaehlen oder beide Aenderungen kombinieren, und anschliessend committen.

## Aufgabe 9
- a) Unit-Test → **JUnit** (Java), **pytest** (Python), **NUnit** (C#)
- b) GUI-Test → **Selenium**, **Cypress**, **Playwright**
- c) Lasttest → **JMeter**, **k6**, **Gatling**
- d) Statische Analyse → **SonarQube**, **ESLint**, **Checkstyle**

## Aufgabe 10
**Vorteile:**
1. Beschleunigte Entwicklung, da repetitiver Code automatisch generiert wird.
2. Weniger manuelle Fehler bei Standardaufgaben (z.B. Getter/Setter, Datenbankzugriff).

**Beispiel:** Ein ORM-Generator (z.B. Hibernate) erzeugt automatisch Java-Klassen aus Datenbanktabellen, inklusive Annotationen und Getter/Setter-Methoden.
