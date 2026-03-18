# Komplett: 3.4.08 – Einsatzmoeglichkeiten von Programmiersprachen

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.08
- **Thema:** Einsatzmoeglichkeiten von Programmiersprachen kennen

## Ziel

Du musst wissen, welche Programmiersprachen in welchen Anwendungsbereichen typischerweise eingesetzt werden, und begruenden koennen, warum eine bestimmte Sprache fuer ein Einsatzgebiet geeignet ist.

## Grundlagen

### Sprachkategorien nach Einsatzgebiet

| Einsatzgebiet | Typische Sprachen | Begruendung |
|--------------|-------------------|-------------|
| Webentwicklung (Frontend) | JavaScript, TypeScript, HTML/CSS | Laufen im Browser, DOM-Manipulation, Frameworks (React, Angular, Vue) |
| Webentwicklung (Backend) | Java, Python, PHP, C#, Node.js (JavaScript), Go, Ruby | Serverseitige Logik, Datenbankzugriff, API-Bereitstellung |
| Mobile Entwicklung (nativ) | Swift (iOS), Kotlin/Java (Android) | Plattformspezifisch, voller Zugriff auf Geraete-APIs |
| Mobile Entwicklung (cross-platform) | Dart (Flutter), JavaScript (React Native) | Eine Codebasis fuer iOS + Android |
| Desktop-Anwendungen | C#/.NET (Windows), Java (plattformuebergreifend), C++ (Qt), Python (Tkinter) | GUI-Frameworks, Betriebssystemintegration |
| Embedded / Systemprogrammierung | C, C++, Rust | Hardwarenahe, niedriger Speicherverbrauch, deterministische Ausfuehrung |
| Data Science / KI | Python, R, Julia | Umfangreiche Bibliotheken (NumPy, Pandas, TensorFlow, scikit-learn) |
| Spieleentwicklung | C++ (Unreal Engine), C# (Unity) | Performance, Engine-Unterstuetzung |
| Datenbanken / Abfragen | SQL | Standardsprache fuer relationale Datenbanken |
| DevOps / Scripting | Bash, Python, PowerShell | Automatisierung, Systemadministration |
| Blockchain / Smart Contracts | Solidity | Ethereum-basierte Smart Contracts |

### Populaere Sprachen und ihre Staerken

| Sprache | Staerken | Haupteinsatz |
|---------|---------|-------------|
| Java | Plattformunabhaengig (JVM), grosses Oekosystem, Enterprise-tauglich | Backend, Android, Enterprise |
| Python | Einfache Syntax, riesiges Bibliotheks-Oekosystem, schnell prototypbar | Data Science, Web (Django/Flask), Scripting |
| JavaScript | Einzige Sprache im Browser, Full-Stack mit Node.js | Web (Frontend + Backend) |
| C# | Enge Integration mit Microsoft/.NET, vielseitig | Desktop (Windows), Web (ASP.NET), Spiele (Unity) |
| C / C++ | Maximale Performance, Hardwarenaehe | Embedded, Betriebssysteme, Spiele |
| TypeScript | Statische Typisierung fuer JavaScript, bessere Wartbarkeit | Grosse Webprojekte |
| Go | Einfach, schnell, hervorragende Nebenlaeufigkeit | Cloud, Microservices, DevOps-Tools |
| Rust | Speichersicherheit ohne Garbage Collector, Performance | System, Embedded, sicherheitskritisch |
| PHP | Weit verbreitet im Web, grosse Community (WordPress, Laravel) | Webentwicklung |
| Kotlin | Moderne Java-Alternative, offiziell fuer Android | Android, Backend (Spring) |

---

## Vertiefung

### Polyglot Programming

**Definition:** Polyglot Programming bedeutet, dass in einem Projekt mehrere Programmiersprachen eingesetzt werden, jeweils dort, wo sie am besten geeignet sind.

**Beispiel – E-Commerce-Plattform:**

| Komponente | Sprache | Begruendung |
|-----------|---------|-------------|
| Frontend (Webshop) | TypeScript (React) | Moderne UI, Typsicherheit |
| Backend (API) | Java (Spring Boot) | Enterprise-tauglich, stabil |
| Datenanalyse | Python (Pandas) | Beste Bibliotheken fuer Datenauswertung |
| Datenbank | SQL (PostgreSQL) | Standard fuer relationale Abfragen |
| DevOps / CI/CD | Bash + Python | Automatisierungsskripte |
| Mobile App | Kotlin (Android) / Swift (iOS) | Native Performance |

### Auswahlkriterien fuer die Praxis

| Kriterium | Frage |
|-----------|-------|
| Einsatzgebiet | Web, Mobile, Desktop, Embedded? |
| Performance-Anforderung | Echtzeit? Hoher Durchsatz? |
| Plattform | Windows, Linux, macOS, Browser, Smartphone? |
| Team-Know-how | Welche Sprachen beherrscht das Team? |
| Oekosystem | Gibt es passende Frameworks und Bibliotheken? |
| Community | Wie gross ist die Community fuer Support und Dokumentation? |
| Wartbarkeit | Ist der Code langfristig lesbar und wartbar? |
| Lizenz/Kosten | Open Source oder kommerziell? |

### Typische Pruefungsaspekte
- Sprache einem Einsatzgebiet zuordnen (z.B. "Fuer Mobile-Entwicklung auf Android → Kotlin")
- Begruendung, warum eine bestimmte Sprache fuer ein Szenario geeignet ist
- Unterschied Frontend vs. Backend benennen und passende Sprachen nennen
- Polyglot Programming als Konzept erklaeren

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| JavaScript nur als Frontend-Sprache genannt | JavaScript laeuft auch serverseitig (Node.js) |
| Python als langsam und ungeeignet abgestempelt | Python ist ideal fuer Prototyping, Data Science und Scripting; Performance-kritische Teile koennen in C/C++ ausgelagert werden |
| C# nur mit Windows assoziiert | C# laeuft mit .NET Core/8 auch auf Linux und macOS |
| SQL als Programmiersprache behandelt | SQL ist eine deklarative Abfragesprache, kein Allzweck-Programmiersprache |
| HTML/CSS als Programmiersprache bezeichnet | HTML ist eine Auszeichnungssprache, CSS eine Stilsprache |

---

## Uebungen

**Aufgabe 1:** Ordne die folgenden Szenarien der jeweils am besten geeigneten Sprache zu und begruende:
- a) Entwicklung einer nativen Android-App
- b) Datenanalyse grosser CSV-Dateien
- c) Programmierung eines Mikrocontrollers
- d) Erstellung einer modernen Single-Page-Webanwendung

**Aufgabe 2:** Was bedeutet "Polyglot Programming"? Nenne ein Beispiel, in dem drei verschiedene Sprachen in einem Projekt sinnvoll eingesetzt werden.

**Aufgabe 3:** Nenne drei Kriterien, die bei der Auswahl einer Programmiersprache fuer ein neues Projekt beruecksichtigt werden sollten. Erklaere jedes Kriterium in einem Satz.

---
---

# Loesungen

## Aufgabe 1
- a) **Kotlin** – Offiziell von Google fuer Android empfohlen, moderne Syntax, volle Android-API-Unterstuetzung.
- b) **Python** – Bibliotheken wie Pandas und NumPy sind speziell fuer Datenanalyse optimiert; einfache Syntax fuer schnelle Prototypen.
- c) **C** – Hardwarenahe Programmierung, geringer Speicherverbrauch, deterministische Ausfuehrung, Standardsprache fuer Embedded-Systeme.
- d) **JavaScript/TypeScript** – Einzige Sprache, die nativ im Browser laeuft; Frameworks wie React, Angular oder Vue ermoeglichen moderne SPAs.

## Aufgabe 2
Polyglot Programming bedeutet, in einem Projekt mehrere Programmiersprachen einzusetzen, jeweils dort, wo sie die beste Loesung bieten. Beispiel: Ein Webshop nutzt TypeScript (React) fuer das Frontend, Java (Spring Boot) fuer das Backend und Python fuer die Datenanalyse der Verkaufszahlen.

## Aufgabe 3
1. **Einsatzgebiet:** Die Sprache muss zum geplanten Anwendungsbereich passen (z.B. Web, Mobile, Embedded).
2. **Team-Know-how:** Das Entwicklungsteam sollte die Sprache bereits beherrschen oder schnell erlernen koennen, um Produktivitaet und Qualitaet sicherzustellen.
3. **Oekosystem:** Es muessen passende Frameworks, Bibliotheken und Tools verfuegbar sein, um nicht alles von Grund auf entwickeln zu muessen.
