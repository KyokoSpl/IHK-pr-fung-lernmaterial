# Grundlagen: 1.4.06 – Programmiersprachen kennen, einordnen, unterscheiden

## Variablen, Datentypen und -strukturen

**Definition:** Variablen sind benannte Speicherplaetze fuer Daten. Datentypen bestimmen, welche Werte gespeichert werden koennen.

**Grundlegende Datentypen:**

| Datentyp | Beschreibung | Beispiel |
|---|---|---|
| Integer (int) | Ganzzahl | 42, -7 |
| Float/Double | Gleitkommazahl | 3.14, -0.5 |
| Boolean (bool) | Wahrheitswert | true, false |
| Char | Einzelnes Zeichen | 'A', '9' |
| String | Zeichenkette | "Hallo Welt" |

**Datenstrukturen:**
- **Array** – Geordnete Sammlung gleicher Datentypen, feste Groesse
- **Liste** – Dynamische Sammlung, variable Groesse
- **Dictionary/Map** – Schluessel-Wert-Paare
- **Stack** – LIFO (Last In, First Out)
- **Queue** – FIFO (First In, First Out)

---

## Kontrollstrukturen

**Definition:** Anweisungen, die den Ablauf eines Programms steuern.

### Verzweigungen
- **if/else:** Bedingte Ausfuehrung
- **switch/case:** Mehrfachverzweigung basierend auf einem Wert

### Schleifen
- **for:** Zaehlschleife (bekannte Anzahl Durchlaeufe)
- **while:** Kopfgesteuerte Schleife (Bedingung vor Ausfuehrung)
- **do-while:** Fussgesteuerte Schleife (mind. 1 Durchlauf)

**Pseudocode-Beispiel:**
```
FUER i VON 1 BIS 10
    WENN i MODULO 2 == 0 DANN
        AUSGABE i + " ist gerade"
    ENDE WENN
ENDE FUER
```

---

## Prozeduren und Funktionen

**Definition:** Wiederverwendbare Code-Bloecke, die eine bestimmte Aufgabe erledigen.

| Merkmal | Prozedur | Funktion |
|---|---|---|
| Rueckgabewert | Nein (void) | Ja (return) |
| Zweck | Ausfuehren einer Aktion | Berechnen und Zurueckgeben eines Werts |
| Beispiel | `druckeBeleg()` | `berechneNetto(brutto, mwst)` |

**Parameter:**
- **Uebergabeparameter** – Werte, die der Funktion mitgegeben werden
- **Rueckgabewert** – Ergebnis der Funktion

---

## Prozedurale vs. objektorientierte Herangehensweise

| Merkmal | Prozedural | Objektorientiert (OOP) |
|---|---|---|
| Struktur | Funktionen/Prozeduren | Klassen und Objekte |
| Daten | Global oder lokal | Gekapselt in Objekten |
| Wiederverwendung | Durch Funktionsaufrufe | Durch Vererbung/Komposition |
| Beispiele | C, Pascal, Bash | Java, Python, C#, C++ |
| Eignung | Kleine/einfache Programme | Komplexe, wartbare Software |

---

## Klassen, Attribute, Objekte, Methoden, Sichtbarkeit

**Definition:** Grundkonzepte der OOP – eine Klasse ist ein Bauplan, ein Objekt eine konkrete Instanz.

**Kernbegriffe:**
- **Klasse:** Bauplan/Vorlage (z.B. `Kunde`)
- **Objekt:** Instanz einer Klasse (z.B. `kunde1 = new Kunde()`)
- **Attribute:** Eigenschaften (z.B. `name`, `kundennummer`)
- **Methoden:** Funktionen einer Klasse (z.B. `getKundendaten()`)

**Sichtbarkeit (Zugriffsmodifikatoren):**

| Modifikator | Zugriff |
|---|---|
| `public (+)` | Von ueberall |
| `private (-)` | Nur innerhalb der Klasse |
| `protected (#)` | Klasse + Unterklassen |

---

## Compiler, Linker, Interpreter

**Definition:** Werkzeuge zur Uebersetzung von Quellcode in ausfuehrbaren Code.

| Werkzeug | Funktion | Zeitpunkt |
|---|---|---|
| **Compiler** | Uebersetzt gesamten Quellcode in Maschinencode | Vor Ausfuehrung |
| **Linker** | Verbindet kompilierte Module und Bibliotheken | Nach Kompilierung |
| **Interpreter** | Uebersetzt und fuehrt zeilenweise aus | Waehrend Ausfuehrung |

**Vergleich Compiler vs. Interpreter:**

| Aspekt | Compiler | Interpreter |
|---|---|---|
| Geschwindigkeit | Schnell (vorkompiliert) | Langsamer (Laufzeit-Uebersetzung) |
| Fehlererkennung | Vor Ausfuehrung (Kompilierzeit) | Waehrend Ausfuehrung |
| Ausgabe | Ausfuehrbare Datei (.exe) | Keine eigenstaendige Datei |
| Beispiele | C, C++, Java (Bytecode) | Python, JavaScript, PHP |

---

## Debugging, formale und inhaltliche Fehler

**Definition:** Fehlersuche und -behebung im Quellcode.

**Fehlerarten:**

| Fehlerart | Beschreibung | Beispiel |
|---|---|---|
| **Syntaxfehler (formal)** | Verletzt Sprachregeln | Fehlende Klammer, Semikolon |
| **Laufzeitfehler** | Tritt waehrend Ausfuehrung auf | Division durch Null, Null-Pointer |
| **Logikfehler (inhaltlich)** | Programm laeuft, Ergebnis falsch | Falsche Formel, falsche Bedingung |

**Debugging-Methoden:**
- **Breakpoint:** Haltepunkt, Programm stoppt an definierter Stelle
- **Variableninspektion:** Werte waehrend Ausfuehrung pruefen
- **Schrittweises Ausfuehren (Step Over/Into):** Zeile fuer Zeile durchgehen
- **Konsolenausgabe:** `print()`/`console.log()` zur schnellen Fehlersuche

---

## Bibliotheken und Frameworks

**Definition:** Vorgefertigte Code-Sammlungen zur Wiederverwendung.

| Merkmal | Bibliothek (Library) | Framework |
|---|---|---|
| Steuerung | Du rufst die Bibliothek auf | Das Framework ruft deinen Code auf |
| Prinzip | Werkzeugkasten | Geruest/Rahmen |
| Flexibilitaet | Hoch (du entscheidest wann/wo) | Eingeschraenkt (du folgst Regeln) |
| Beispiele | NumPy, jQuery, Gson | Django, Spring, Angular, React |

---

## Skriptsprachen

**Definition:** Interpretierte Sprachen, die haeufig fuer Automatisierung, Systemadministration und schnelle Aufgaben eingesetzt werden.

**Kernaussagen:**
- Werden zur Laufzeit interpretiert (kein Kompilieren noetig)
- Kurze Entwicklungszyklen, gut fuer Prototypen
- **Shell-Skript:** Bash, PowerShell – Systemautomatisierung
- **Python:** Vielseitig – Scripting, Web, KI, Datenanalyse
- **JavaScript:** Web (Client + Server mit Node.js)

## Querverweise
- → 1.4.07 (UML, Pseudocode, Schreibtischtest)
- → 3.3.05 (Algorithmen in Programmiersprache)
- → 3.4.06 (Programmiersprachen-Konzepte)
- → 3.4.17 (OOP-Konzepte: Vererbung, Polymorphie, Interfaces)
