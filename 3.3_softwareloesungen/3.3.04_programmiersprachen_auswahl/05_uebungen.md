# 3.3.04 – Uebungen: Situationsgerechte Auswahl einer Programmiersprache

## Aufgabe 1: Framework oder Bibliothek?

Ordne zu: Framework (F) oder Bibliothek (B)?

| Nr. | Technologie | F oder B? |
|-----|-------------|-----------|
| a) | Angular (JavaScript) | |
| b) | jQuery (JavaScript) | |
| c) | Django (Python) | |
| d) | NumPy (Python) | |
| e) | Spring Boot (Java) | |
| f) | Gson (Java) | |
| g) | React (JavaScript) | |
| h) | Flask (Python) | |

---

## Aufgabe 2: Sprachwahl begruenden

Fuer welches Szenario wuerdest du welche Sprache empfehlen? Begruende jeweils kurz.

a) Eine Hochschule moechte ein Verwaltungssystem fuer Studierende entwickeln. Das IT-Team hat Java-Erfahrung, das System soll auf Linux-Servern laufen und langfristig wartbar sein.

b) Ein Data-Science-Team soll ein Machine-Learning-Modell zur Bilderkennung entwickeln.

c) Ein Dienstleister moechte ein einfaches Skript, das taeglich Logdateien analysiert und per E-Mail einen Report versendet.

d) Ein Spieleentwickler will ein performantes 3D-Spiel fuer PC entwickeln.

---

## Aufgabe 3: IDE-Funktionen benennen

Erklaere die folgenden IDE-Funktionen und deren Nutzen:

a) IntelliSense / Code-Completion
b) Breakpoint
c) Call Stack
d) Refactoring: "Extract Method"
e) Versionskontroll-Integration

---

## Aufgabe 4: Compiled vs. Interpreted

Ergaenze die Tabelle:

| Merkmal | Compiled | Interpreted |
|---------|----------|-------------|
| Uebersetzungszeitpunkt | | |
| Ausfuehrungsgeschwindigkeit | | |
| Fehlerentdeckung | | |
| Portabilitaet | | |
| Beispielsprachen | | |

---

## Aufgabe 5: Entscheidungsmatrix erstellen

Ein Unternehmen plant die Entwicklung einer internen Zeiterfassungs-Web-App. Folgende Rahmenbedingungen:
- Team: 2 Entwickler (erfahren in C# und JavaScript)
- Anforderung: Web-basiert, responsive, Anbindung an bestehende SQL-Server-Datenbank
- Budget: mittel
- Zeitrahmen: 4 Monate

Erstelle eine Entscheidungsmatrix und empfehle eine Technologie-Kombination.

---
---

## Loesung Aufgabe 1

| Nr. | Technologie | Typ | Begruendung |
|-----|-------------|-----|-------------|
| a) | Angular | **Framework** | Gibt Architektur vor (Module, Components, Services), IoC |
| b) | jQuery | **Bibliothek** | Hilfsunktionen fuer DOM-Manipulation, du rufst auf |
| c) | Django | **Framework** | MVT-Architektur vorgegeben, URL-Routing |
| d) | NumPy | **Bibliothek** | Mathematische Funktionen, die du aufrufst |
| e) | Spring Boot | **Framework** | IoC-Container, Dependency Injection, Anwendungsstruktur |
| f) | Gson | **Bibliothek** | JSON-Serialisierung, die du aufrufst |
| g) | React | **Bibliothek** (offiziell) | Wird oft als Framework behandelt, ist aber eine UI-Bibliothek |
| h) | Flask | **(Micro-)Framework** | Gibt Routing/Request-Handling vor, aber minimale Struktur |

---

## Loesung Aufgabe 2

a) **Java mit Spring Boot**: Team hat Java-Erfahrung (Know-how), plattformunabhaengig dank JVM (Linux-kompatibel), Spring Boot bietet Enterprise-Features, gute Wartbarkeit durch strenge Typisierung.

b) **Python**: Dominantes Oekosystem fuer ML/AI (TensorFlow, PyTorch, scikit-learn, NumPy, Pandas), grosse Community, Jupyter Notebooks fuer explorative Analyse.

c) **Python oder Bash**: Python fuer komplexere Logik (Regex, E-Mail-Versand mit smtplib), Bash fuer einfache Textverarbeitung (grep, awk). Schnelle Entwicklung, keine Kompilierung noetig.

d) **C++ mit Unreal Engine oder C# mit Unity**: C++ fuer maximale Performance (Unreal Engine), C# mit Unity als zugaenglichere Alternative. Direkter Hardwarezugriff und Grafikoptimierung noetig.

---

## Loesung Aufgabe 3

a) **IntelliSense**: Zeigt beim Tippen automatisch passende Methoden, Attribute und Parameter an. **Nutzen**: Schnellere Entwicklung, weniger Tippfehler, Dokumentation direkt sichtbar.

b) **Breakpoint**: Haltepunkt im Code, an dem die Programmausfuehrung pausiert. **Nutzen**: Variablenwerte zur Laufzeit pruefen, Programmfluss verstehen, Fehler lokalisieren.

c) **Call Stack**: Zeigt die Verschachtelung der Methodenaufrufe zum aktuellen Zeitpunkt. **Nutzen**: Nachvollziehen, welche Methode welche andere aufgerufen hat, Fehlerursachen in tiefen Aufrufketten finden.

d) **Extract Method**: Markierter Code-Block wird in eine eigene Methode verschoben, der urspruengliche Block durch den Methodenaufruf ersetzt. **Nutzen**: Kuerzere Methoden, bessere Lesbarkeit, Wiederverwendbarkeit.

e) **Versionskontroll-Integration**: Git direkt in der IDE nutzen (Commits, Branches, Diffs, Merge). **Nutzen**: Kein Wechsel zur Kommandozeile noetig, visuelle Darstellung von Aenderungen, einfacheres Konfliktmanagement.

---

## Loesung Aufgabe 4

| Merkmal | Compiled | Interpreted |
|---------|----------|-------------|
| Uebersetzungszeitpunkt | Vor der Ausfuehrung | Waehrend der Ausfuehrung |
| Ausfuehrungsgeschwindigkeit | Schnell (Maschinencode) | Langsamer (zeilenweise interpretiert) |
| Fehlerentdeckung | Zur Compile-Zeit (Syntaxfehler, Typfehler) | Zur Laufzeit |
| Portabilitaet | Gering (plattformspezifischer Binary) | Hoch (Interpreter auf jeder Plattform) |
| Beispielsprachen | C, C++, Rust, Go | Python, Ruby, PHP, JavaScript |

---

## Loesung Aufgabe 5

### Entscheidungsmatrix

| Kriterium | Gewicht | C# + ASP.NET + React | C# + Blazor | Node.js + React |
|-----------|---------|---------------------|-------------|-----------------|
| Teamkompetenz (C#, JS) | 30% | ++ (beides bekannt) | + (nur C#) | + (nur JS) |
| SQL-Server-Anbindung | 20% | ++ (Entity Framework) | ++ (EF) | + (moeglich, weniger nativ) |
| Zeitrahmen (4 Monate) | 25% | + (zwei Technologien) | ++ (ein Oekosystem) | + (zwei Technologien) |
| Web/Responsive | 15% | ++ (React) | + (Blazor CSS) | ++ (React) |
| Langfristige Wartbarkeit | 10% | ++ | ++ | + |

**Empfehlung**: **C# + ASP.NET Core (Backend) + React (Frontend)**
- Backend: ASP.NET Core nutzt die C#-Erfahrung des Teams und hat native SQL-Server-Integration via Entity Framework
- Frontend: React nutzt die JavaScript-Erfahrung
- Alternative: Blazor, wenn das Team lieber komplett in C# arbeitet
