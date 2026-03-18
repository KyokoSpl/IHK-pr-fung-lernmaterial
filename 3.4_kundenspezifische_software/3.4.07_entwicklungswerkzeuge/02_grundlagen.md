# Grundlagen: 3.4.07 – Software-Entwicklungswerkzeuge

## Compiler

**Definition:** Ein Compiler uebersetzt den gesamten Quellcode einer Programmiersprache in Maschinencode (native) oder Bytecode, bevor das Programm ausgefuehrt wird.

**Kernaussagen:**
- Gesamter Quellcode wird in einem Durchgang analysiert und uebersetzt
- Ergebnis: Objektdatei (.o, .obj) oder ausfuehrbares Programm
- Syntaxfehler und viele logische Fehler werden zur Compile-Zeit erkannt
- Ausfuehrung des kompilierten Programms ist schnell

**Compiler-Phasen:**

| Phase | Aufgabe |
|-------|---------|
| Lexikalische Analyse | Quellcode in Tokens zerlegen |
| Syntaxanalyse | Tokens auf grammatische Korrektheit pruefen |
| Semantische Analyse | Typpruefung, Variablendeklaration pruefen |
| Codeerzeugung | Maschinencode oder Bytecode generieren |
| Optimierung | Code fuer Performance oder Groesse optimieren |

**Beispiele:** gcc (C/C++), javac (Java → Bytecode), rustc (Rust)

---

## Debugger

**Definition:** Ein Debugger ist ein Werkzeug zur systematischen Fehlersuche in Programmen waehrend der Laufzeit.

**Kernaussagen:**
- Ermoeglicht das schrittweise Ausfuehren von Code (Step into, Step over, Step out)
- Breakpoints halten die Ausfuehrung an einer bestimmten Stelle an
- Variablen und deren Werte koennen zur Laufzeit inspiziert werden
- Call Stack zeigt die aktuelle Aufrufhierarchie

**Wichtige Debugger-Funktionen:**

| Funktion | Beschreibung |
|----------|-------------|
| Breakpoint | Haelt die Ausfuehrung an einer bestimmten Codezeile an |
| Step into | Springt in eine aufgerufene Funktion hinein |
| Step over | Fuehrt die aktuelle Zeile aus, ohne in Funktionen zu springen |
| Step out | Fuehrt den Rest der aktuellen Funktion aus und kehrt zum Aufrufer zurueck |
| Watch | Ueberwacht den Wert einer Variable dauerhaft |
| Call Stack | Zeigt die verschachtelte Aufruffolge der Funktionen |

**Beispiele:** gdb (C/C++), Debugger in IntelliJ/VS Code, Chrome DevTools (JavaScript)

---

## Editor

**Definition:** Ein Editor ist ein leichtgewichtiges Programm zum Erstellen und Bearbeiten von Quellcode-Dateien. Er bietet grundlegende Funktionen wie Syntaxhervorhebung, aber keine integrierten Build-/Debug-Tools.

**Kernaussagen:**
- Fokus auf Textbearbeitung, leichtgewichtig und schnell
- Durch Plugins/Erweiterungen individuell anpassbar
- Keine integrierte Kompilierung oder Debugging (ohne Erweiterungen)
- Fuer schnelle Aenderungen und einfache Aufgaben geeignet

**Beispiele:** Visual Studio Code (mit Erweiterungen nahe an IDE), Sublime Text, Vim, Nano, Notepad++

---

## IDE (Integrated Development Environment)

**Definition:** Eine IDE ist eine integrierte Entwicklungsumgebung, die Editor, Compiler/Interpreter, Debugger, Build-System, Versionsverwaltung und weitere Werkzeuge in einer Anwendung vereint.

**Typische IDE-Funktionen:**

| Funktion | Beschreibung |
|----------|-------------|
| Code-Editor | Syntaxhervorhebung, Autovervollstaendigung, Refactoring |
| Compiler/Build | Direktes Kompilieren und Erstellen des Projekts |
| Debugger | Integriertes Debugging mit Breakpoints und Variableninspection |
| Projektverwaltung | Ordnerstruktur, Dateinavigation, Suche |
| Versionsverwaltung | Git-Integration (Commit, Push, Pull, Diff) |
| Plugins | Erweiterbar durch Zusatzmodule |

**Beispiele:** IntelliJ IDEA (Java), Visual Studio (C#/.NET), Eclipse (Java), PyCharm (Python), Android Studio (Android)

### Editor vs. IDE

| Kriterium | Editor | IDE |
|-----------|--------|-----|
| Umfang | Leichtgewichtig | Umfangreich |
| Funktionen | Hauptsaechlich Textbearbeitung | Editor + Build + Debug + Tools |
| Ressourcenverbrauch | Gering | Hoch |
| Einarbeitungszeit | Kurz | Laenger |
| Eignung | Schnelle Aenderungen, Scripting | Grosse Projekte, komplexe Entwicklung |

---

## Interpreter

**Definition:** Ein Interpreter fuehrt den Quellcode zeilenweise zur Laufzeit aus, ohne ihn vorher vollstaendig in Maschinencode zu uebersetzen.

**Kernaussagen:**
- Code wird sofort ausgefuehrt, kein separater Kompilierungsschritt
- Fehler werden erst zur Laufzeit erkannt (bei Erreichen der fehlerhaften Zeile)
- Langsamere Ausfuehrung als kompilierter Code
- Plattformunabhaengig (Interpreter muss auf Zielsystem vorhanden sein)

**Beispiele:** Python-Interpreter (CPython), Node.js (JavaScript), PHP-Interpreter, Ruby-Interpreter

---

## Linker

**Definition:** Ein Linker verbindet mehrere kompilierte Objektdateien (.o, .obj) und Bibliotheken zu einem einzigen ausfuehrbaren Programm.

**Kernaussagen:**
- Loest externe Referenzen auf (z.B. Funktionsaufrufe zwischen Dateien)
- Bindet statische Bibliotheken ein (.a, .lib)
- Verweist auf dynamische Bibliotheken (.so, .dll)
- Erzeugt das finale ausfuehrbare Programm (.exe, ELF)

**Statisch vs. Dynamisch Linken:**

| Aspekt | Statisch | Dynamisch |
|--------|---------|-----------|
| Bibliothek wird | in die Programmdatei kopiert | zur Laufzeit geladen |
| Dateigroesse | Groesser | Kleiner |
| Abhaengigkeit | Keine (eigenstaendig) | Bibliothek muss auf System vorhanden sein |
| Update | Neukompilierung noetig | Bibliothek austauschen genuegt |
| Beispiel-Dateien | .a (Linux), .lib (Windows) | .so (Linux), .dll (Windows) |

---

## Programmgenerator

**Definition:** Ein Programmgenerator erzeugt automatisch Quellcode aus Modellen, Vorlagen, Schemata oder grafischen Beschreibungen.

**Kernaussagen:**
- Beschleunigt die Entwicklung durch automatische Codeerzeugung
- Reduziert manuelle Fehler bei repetitiven Aufgaben
- Einsatz bei ORM (Datenbankklassen), GUI-Builder, API-Stubs

**Beispiele:**

| Typ | Beschreibung | Beispiel |
|-----|-------------|---------|
| ORM-Generator | Erzeugt Datenbankzugriffsklassen aus Tabellendefinitionen | Entity Framework, Hibernate |
| GUI-Builder | Erzeugt GUI-Code aus grafischem Layout | JavaFX Scene Builder, Qt Designer |
| API-Generator | Erzeugt Server-/Client-Code aus API-Spezifikation | Swagger/OpenAPI Codegen |
| Scaffolding | Erzeugt Grundgeruest fuer ein Projekt | Rails Scaffold, Angular CLI |

---

## Testsoftware

**Definition:** Testsoftware automatisiert die Ueberpruefung von Softwarequalitaet durch verschiedene Teststufen und -methoden.

**Testarten und Werkzeuge:**

| Testart | Beschreibung | Beispiel-Tools |
|---------|-------------|---------------|
| Unit-Test | Test einzelner Funktionen/Klassen | JUnit (Java), pytest (Python), NUnit (C#) |
| Integrationstest | Test des Zusammenspiels mehrerer Komponenten | Testcontainers, Spring Test |
| GUI-Test | Automatisiertes Testen der Benutzeroberflaeche | Selenium, Cypress, Playwright |
| Lasttest | Testen der Performance unter hoher Belastung | JMeter, k6, Gatling |
| Statische Analyse | Quellcode-Pruefung ohne Ausfuehrung (Code-Qualitaet) | SonarQube, ESLint, Checkstyle |

---

## Versionsverwaltung

**Definition:** Versionsverwaltungssysteme protokollieren alle Aenderungen am Quellcode, ermoeglichen paralleles Arbeiten und das Zuruecksetzen auf fruehere Versionen.

**Kernaussagen:**
- Git ist der De-facto-Standard fuer Versionsverwaltung
- Jede Aenderung wird als Commit mit Nachricht gespeichert
- Branching ermoeglicht paralleles Arbeiten an Features
- Merging fuehrt Branches wieder zusammen

**Wichtige Git-Begriffe:**

| Begriff | Beschreibung |
|---------|-------------|
| Repository | Projektverzeichnis mit vollstaendiger Historie |
| Commit | Gespeicherter Satz von Aenderungen mit Nachricht |
| Branch | Paralleler Entwicklungszweig |
| Merge | Zusammenfuehren zweier Branches |
| Pull Request | Anfrage zum Zusammenfuehren eines Branches (Code Review) |
| Clone | Kopie eines Remote-Repositories auf den lokalen Rechner |
| Push / Pull | Aenderungen zum/vom Remote-Repository senden/holen |

**Beispiele:** Git (+ GitHub, GitLab, Bitbucket), Subversion (SVN), Mercurial
