# 3.3.04 – Vertiefung: Situationsgerechte Auswahl einer Programmiersprache

## Entscheidungsmatrix: Sprachwahl

Fuer die Pruefung ist es wichtig, eine **begruendete Empfehlung** abgeben zu koennen. Folgende Matrix hilft bei der Bewertung:

| Kriterium | Gewichtung | Sprache A | Sprache B | Sprache C |
|-----------|-----------|----------|----------|----------|
| Teamkompetenz | Hoch | ++ | + | - |
| Performance | Mittel | + | ++ | + |
| Portabilitaet | Mittel | ++ | - | ++ |
| Oekosystem/Bibliotheken | Hoch | ++ | + | ++ |
| Lernkurve | Niedrig | + | - | ++ |
| Arbeitsmarkt | Mittel | ++ | + | + |

**Bewertungsskala**: ++ sehr gut, + gut, o neutral, - schlecht, -- sehr schlecht

---

## Vergleichstabelle: Programmiersprachen nach Einsatzgebiet

| Einsatzgebiet | Empfohlene Sprachen | Begruendung |
|--------------|-------------------|-------------|
| Webanwendung (Backend) | Java, C#, Python, JavaScript (Node.js) | Frameworks, Skalierbarkeit, Oekosystem |
| Webanwendung (Frontend) | JavaScript, TypeScript | Browser-Standard, DOM-Manipulation |
| Mobile App (Android) | Kotlin, Java | Offiziell unterstuetzt, Android SDK |
| Mobile App (iOS) | Swift | Apple-Standard, Performance |
| Mobile App (Cross-Platform) | Flutter/Dart, React Native | Ein Code fuer beide Plattformen |
| Desktop-Anwendung | C#, Java, C++, Electron | GUI-Frameworks verfuegbar |
| Systemnahe Programmierung | C, C++, Rust | Direkter Hardwarezugriff, Performance |
| Data Science / KI | Python, R | NumPy, Pandas, TensorFlow, scikit-learn |
| Embedded / IoT | C, C++, MicroPython | Geringer Speicher, Hardwarenaehe |
| Automatisierung / Scripting | Python, Bash, PowerShell | Schnelle Entwicklung, Systemzugriff |

---

## Vertiefung: IDE-Funktionen im Entwicklungsalltag

### Debugging – Schritt fuer Schritt

| Aktion | Beschreibung | Tastenkombination (typisch) |
|--------|-------------|---------------------------|
| Breakpoint setzen | Haltepunkt in einer Zeile | Klick auf Zeilennummer |
| Step Over | Naechste Zeile ausfuehren (ohne in Methode zu springen) | F10 |
| Step Into | In die aufgerufene Methode springen | F11 |
| Step Out | Aus aktueller Methode zurueckkehren | Shift+F11 |
| Continue | Bis zum naechsten Breakpoint weiterlaufen | F5 |
| Watch | Variable beobachten | Variable zum Watch-Fenster hinzufuegen |
| Call Stack | Aufrufhierarchie anzeigen | Im Debug-Panel sichtbar |

### Refactoring-Optionen

| Refactoring | Beschreibung | Wann einsetzen? |
|-------------|-------------|-----------------|
| Rename | Symbol umbenennen (alle Referenzen) | Wenn ein Name unklar ist |
| Extract Method | Code-Block in eigene Methode auslagern | Bei langen Methoden |
| Extract Variable | Ausdruck in Variable speichern | Bei komplexen Ausdruecken |
| Inline | Variable/Methode wieder einsetzen | Bei ueberfluessigen Abstraktionen |
| Move | Klasse/Methode verschieben | Bei falscher Paketstruktur |

---

## Paradigmen und Sprachwahl

| Paradigma | Beschreibung | Sprachen |
|-----------|-------------|---------|
| Objektorientiert (OOP) | Klassen, Vererbung, Polymorphie | Java, C#, C++, Python |
| Funktional | Unveraenderliche Daten, Funktionen hoeherer Ordnung | Haskell, Scala, Elixir, (JS, Python teilw.) |
| Prozedural | Schritt-fuer-Schritt-Anweisungen | C, Pascal, COBOL |
| Skriptsprache | Schnelle Entwicklung, dynamisch typisiert | Python, JavaScript, Ruby, PHP |
| Deklarativ | WAS statt WIE beschreiben | SQL, HTML, CSS |

---

## Pruefungsaspekte

### Typische Fragestellungen

1. "Nennen Sie drei Vorteile einer IDE gegenueber einem einfachen Texteditor"
2. "Erklaeren Sie den Unterschied zwischen Framework und Bibliothek"
3. "Welche Programmiersprache wuerden Sie fuer folgendes Szenario empfehlen? Begruenden Sie."
4. "Was ist der Unterschied zwischen kompilierten und interpretierten Sprachen?"

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| IDE und Texteditor gleichsetzen | IDE hat Compiler, Debugger, VCS-Integration etc. |
| Framework und Bibliothek verwechseln | Framework = Inversion of Control, Bibliothek = man ruft auf |
| "Java ist langsam weil interpretiert" | Java nutzt JIT-Compilation, ist nicht rein interpretiert |
| "C++ ist immer die beste Wahl fuer Performance" | Stimmt oft, aber Entwicklungszeit ist laenger; Rust ist modern sicherer |
| Portabilitaet nur auf Betriebssysteme beziehen | Umfasst auch Geraete (Desktop, Mobile, Embedded) |
| Know-how-Faktor unterschaetzen | In der Praxis oft der wichtigste Entscheidungsfaktor |
