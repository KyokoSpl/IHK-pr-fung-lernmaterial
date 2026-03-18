# 3.3.04 – Grundlagen: Situationsgerechte Auswahl einer Programmiersprache

## TK 1: Einsatz von IDE

### Definition
**IDE** = Integrated Development Environment – eine integrierte Entwicklungsumgebung, die mehrere Werkzeuge zur Softwareentwicklung in einer Anwendung vereint.

### Kernfunktionen einer IDE

| Funktion | Beschreibung | Beispiel |
|----------|-------------|---------|
| **Code-Editor** | Syntaxhervorhebung, Einrueckung, Zeilennummern | Farbige Darstellung von Schluesselwoertern |
| **Code-Vervollstaendigung** | Automatische Vorschlaege (IntelliSense/Autocomplete) | Methoden einer Klasse werden vorgeschlagen |
| **Compiler/Interpreter** | Code uebersetzen und ausfuehren | Build-Button, Run-Konfiguration |
| **Debugger** | Schrittweises Ausfuehren, Breakpoints, Variablen inspizieren | Breakpoint in Zeile 42 setzen |
| **Versionskontrolle** | Git-Integration (Commit, Push, Pull, Diff) | Aenderungen direkt in der IDE committen |
| **Refactoring** | Automatisches Umbenennen, Extrahieren von Methoden | "Rename Symbol" aendert alle Referenzen |
| **Projektmanagement** | Dateiverwaltung, Build-System-Integration | Maven, Gradle, npm Integration |
| **Terminal** | Eingebaute Kommandozeile | Befehle ohne IDE-Wechsel ausfuehren |
| **Plugins/Erweiterungen** | Zusaetzliche Funktionen installierbar | Linter, Formatter, Sprachunterstuetzung |
| **Testing** | Testausfuehrung und -ergebnisse | Unit-Tests direkt ausfuehren |

### Verbreitete IDEs

| IDE | Sprachen | Besonderheit |
|-----|----------|-------------|
| Visual Studio Code | Viele (per Plugins) | Leichtgewichtig, kostenlos, erweiterbar |
| IntelliJ IDEA | Java, Kotlin | Starke Java-Unterstuetzung, JetBrains |
| Eclipse | Java, C++ | Open Source, Plugin-Oekosystem |
| Visual Studio | C#, .NET, C++ | Microsoft-Oekosystem, umfangreich |
| PyCharm | Python | Spezialisiert auf Python, JetBrains |
| Xcode | Swift, Objective-C | Apple-Entwicklung (iOS, macOS) |
| Android Studio | Java, Kotlin | Android-Entwicklung, basiert auf IntelliJ |

---

## TK 2: Framework vs. Bibliothek

### Definitionen

| Merkmal | Bibliothek (Library) | Framework |
|---------|---------------------|-----------|
| **Definition** | Sammlung von Funktionen/Klassen, die man aufruft | Gibt die Architektur vor und ruft DEINEN Code auf |
| **Kontrolle** | DU rufst die Bibliothek auf | Das FRAMEWORK ruft deinen Code auf |
| **Prinzip** | "Don't call us, we call you" gilt NICHT | **Inversion of Control** – Framework steuert den Ablauf |
| **Austauschbarkeit** | Leicht austauschbar | Praegt die gesamte Anwendungsstruktur |
| **Beispiel** | Lodash (JS), NumPy (Python), Gson (Java) | Spring (Java), Angular (JS), Django (Python) |

### Inversion of Control (IoC)

```
Bibliothek:
  Dein Code ─────ruft auf────→ Bibliothek
  (Du hast die Kontrolle)

Framework:
  Framework ─────ruft auf────→ Dein Code
  (Framework hat die Kontrolle)
```

### Auswahlkriterien fuer Frameworks/Bibliotheken

| Kriterium | Frage |
|-----------|-------|
| Community/Support | Wie gross ist die Community? Gibt es Dokumentation? |
| Aktualitaet | Wird das Projekt aktiv weiterentwickelt? |
| Lizenz | Open Source? Kommerzielle Einschraenkungen? |
| Lernkurve | Wie schnell kann das Team produktiv werden? |
| Performance | Welchen Overhead bringt das Framework mit? |
| Kompatibilitaet | Passt es zu bestehenden Technologien? |

---

## TK 3: Know-how / Fachkenntnis

### Auswirkung auf die Sprachwahl

| Faktor | Beschreibung |
|--------|-------------|
| Teamkompetenz | Welche Sprachen beherrscht das Team bereits? |
| Lernkurve | Wie lange dauert die Einarbeitung in eine neue Sprache? |
| Arbeitsmarkt | Sind Entwickler fuer diese Sprache verfuegbar? |
| Unternehmensstrategie | Standardisierung auf bestimmte Technologien? |
| Projektlaufzeit | Bei kurzer Laufzeit: bekannte Technologie bevorzugen |

**Faustregel**: Eine dem Team vertraute Sprache ist oft besser als die "perfekte" Sprache, die niemand beherrscht.

---

## TK 4: Performance / Speicherverbrauch

### Compiled vs. Interpreted

| Merkmal | Compiled (kompiliert) | Interpreted (interpretiert) | JIT-Compiled |
|---------|----------------------|---------------------------|-------------|
| Uebersetzung | Vor Ausfuehrung (Compiler) | Zur Laufzeit (Interpreter) | Zur Laufzeit (optimiert) |
| Geschwindigkeit | Schnell (Maschinencode) | Langsamer (zeilenweise) | Mittel bis schnell |
| Portabilitaet | Plattformabhaengig | Plattformunabhaengig | Plattformunabhaengig |
| Beispiele | C, C++, Rust, Go | Python, Ruby, PHP | Java (JVM), C# (.NET) |
| Fehlerentdeckung | Zur Compile-Zeit | Zur Laufzeit | Mischung |

```
Compiled:
  Quellcode ──→ Compiler ──→ Maschinencode ──→ Ausfuehrung
                               (plattformspezifisch)

Interpreted:
  Quellcode ──→ Interpreter ──→ Ausfuehrung
                (liest + fuehrt zeilenweise aus)

JIT (Java):
  Quellcode ──→ Compiler ──→ Bytecode ──→ JVM (JIT) ──→ Maschinencode
                             (plattformunabhaengig)
```

### Performance-Vergleich (allgemein)

| Sprache | Typ | Relative Geschwindigkeit | Speicherverbrauch |
|---------|-----|------------------------|------------------|
| C/C++ | Compiled | Sehr schnell | Gering (manuelle Verwaltung) |
| Rust | Compiled | Sehr schnell | Gering (Ownership-Modell) |
| Go | Compiled | Schnell | Gering |
| Java | JIT-Compiled | Schnell | Mittel (GC, JVM-Overhead) |
| C# | JIT-Compiled | Schnell | Mittel (GC, CLR-Overhead) |
| JavaScript | JIT (V8) | Mittel | Mittel |
| Python | Interpreted | Langsam | Mittel bis hoch |

---

## TK 5: Portabilitaet

### Definition
Faehigkeit, Software auf verschiedenen Plattformen (Betriebssysteme, Geraete) auszufuehren.

### Strategien fuer Portabilitaet

| Strategie | Beschreibung | Beispiel |
|-----------|-------------|---------|
| Plattformunabhaengige Sprache | Laeuft ueberall dank VM/Runtime | Java (JVM), C# (.NET Core) |
| Cross-Platform Framework | Ein Code, mehrere Plattformen | Flutter, React Native, Electron |
| Webbasiert | Laeuft im Browser | HTML/CSS/JS, Progressive Web Apps |
| Containerisierung | Anwendung + Abhaengigkeiten verpackt | Docker |
| Abstraktionsschichten | OS-spezifischer Code hinter Interfaces | Conditional Compilation |

### Plattformunabhaengigkeit nach Sprache

| Sprache | Portabilitaet | Erklaerung |
|---------|--------------|------------|
| Java | Hoch | "Write once, run anywhere" – JVM auf allen Plattformen |
| Python | Hoch | Interpreter fuer alle gaengigen OS verfuegbar |
| C# (.NET Core) | Hoch | Seit .NET Core plattformuebergreifend |
| JavaScript | Hoch | Laeuft in jedem Browser + Node.js |
| C/C++ | Niedrig | Muss fuer jede Plattform neu kompiliert werden |
| Swift | Niedrig | Primaer Apple-Oekosystem |
