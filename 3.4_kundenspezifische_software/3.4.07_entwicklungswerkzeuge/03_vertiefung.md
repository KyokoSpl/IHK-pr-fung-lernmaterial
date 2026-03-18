# Vertiefung: 3.4.07 – Software-Entwicklungswerkzeuge

## Der Build-Prozess im Detail

Der Build-Prozess beschreibt die Schritte vom Quellcode zum ausfuehrbaren Programm:

```
  Quellcode (.c, .java, ...)
        |
        v
  +------------+
  | Praeprozes- |   (nur C/C++: #include, #define aufloesen)
  | sor         |
  +------------+
        |
        v
  +------------+
  | Compiler   |   Quellcode → Objektcode (.o, .obj) oder Bytecode (.class)
  +------------+
        |
        v
  +------------+
  | Linker     |   Objektdateien + Bibliotheken → ausfuehrbares Programm
  +------------+
        |
        v
  Programm (.exe, ELF, .jar)
        |
        v
  +------------+
  | Laufzeit-  |   Ausfuehrung (ggf. durch JVM, CLR, Interpreter)
  | umgebung   |
  +------------+
```

### Vergleich: Compiler vs. Interpreter (Vertiefung)

| Aspekt | Compiler | Interpreter |
|--------|---------|------------|
| Uebersetzungszeitpunkt | Vor der Ausfuehrung (einmalig) | Zur Laufzeit (bei jedem Start) |
| Ergebnis | Maschinencode / Bytecode | Kein persistenter Code |
| Ausfuehrungsgeschwindigkeit | Schnell (nativer Code) | Langsamer |
| Fehlererkennung | Compile-Zeit (frueh) | Laufzeit (spaet) |
| Speicherverbrauch | Nur Programm noetig | Interpreter + Quellcode noetig |
| Typische Sprachen | C, C++, Rust, Go | Python, JavaScript, PHP |
| JIT-Kompilierung | Kein Bedarf | Oft eingesetzt (V8, PyPy) |

### IDE-Funktionen im Detail

| Funktion | Beschreibung | Pruefungsrelevanz |
|----------|-------------|------------------|
| Syntax Highlighting | Farbliche Hervorhebung der Sprachstruktur | Erleichtert Lesbarkeit |
| Autovervollstaendigung | Vorschlaege beim Tippen (IntelliSense) | Reduziert Tippfehler, beschleunigt |
| Refactoring | Automatisches Umbenennen, Extrahieren von Methoden | Code-Qualitaet verbessern |
| Code Navigation | Springe zur Definition, finde alle Verwendungen | Grosse Codebasen navigieren |
| Integrierter Terminal | Kommandozeile in der IDE | Build- und Skript-Ausfuehrung |
| Linting | Echtzeit-Pruefung auf Stilregeln und Fehler | Code-Standards einhalten |

### Git-Workflow: Feature-Branch

```
main:       o---o---o-----------o---o  (Merge)
                     \         /
feature:              o---o---o
                              ^
                          Pull Request
```

1. Neuen Branch erstellen: `git checkout -b feature/login`
2. Aenderungen committen: `git add . && git commit -m "Login implementiert"`
3. Branch pushen: `git push origin feature/login`
4. Pull Request erstellen → Code Review
5. Merge in main: `git merge feature/login`

### Typische Pruefungsaspekte
- Compiler von Interpreter unterscheiden und Beispiele nennen
- Build-Prozess (Compiler → Linker → Programm) beschreiben
- Statisches vs. dynamisches Linken erklaeren
- IDE vs. Editor unterscheiden
- Debugger-Funktionen (Breakpoint, Step into/over/out, Watch) benennen
- Git-Grundbegriffe (Commit, Branch, Merge, Pull Request) definieren
- Teststufen (Unit, Integration, System, Abnahme) den Werkzeugen zuordnen

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| Compiler und Interpreter verwechselt | Compiler: vor Ausfuehrung, Interpreter: zur Laufzeit |
| Linker vergessen im Build-Prozess | Compiler erzeugt Objektdateien, Linker erzeugt Programm |
| IDE und Editor gleichgesetzt | IDE = integrierte Umgebung mit Build+Debug; Editor = Textbearbeitung |
| Git Commit mit Git Push verwechselt | Commit = lokal speichern; Push = an Remote senden |
| Statische Analyse als Test zur Laufzeit verstanden | Statische Analyse prueft Code OHNE Ausfuehrung |
| Programmgenerator als Compiler bezeichnet | Generator erzeugt Quellcode; Compiler uebersetzt Quellcode |
