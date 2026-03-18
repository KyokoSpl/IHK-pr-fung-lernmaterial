# Komplett: 3.4.06 – Konzepte von Programmiersprachen

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.06
- **Thema:** Konzepte von Programmiersprachen kennen und exemplarisch Programmiersprachen nennen koennen

## Ziel

Du musst die grundlegenden Programmierparadigmen und Sprachkonzepte kennen, beispielhafte Sprachen zuordnen und die Unterschiede zwischen kompilierten und interpretierten sowie stark und schwach typisierten Sprachen erklaeren koennen.

## Grundlagen

### Programmierparadigmen

**Definition:** Ein Programmierparadigma ist ein grundlegender Stil oder Ansatz der Programmierung, der bestimmt, wie Probleme strukturiert und geloest werden.

| Paradigma | Beschreibung | Beispielsprachen |
|-----------|-------------|-----------------|
| Imperativ | Programm als Folge von Anweisungen, die den Zustand aendern | C, Pascal, BASIC |
| Prozedural | Imperativ mit Strukturierung durch Prozeduren/Funktionen | C, Pascal, COBOL |
| Objektorientiert (OOP) | Strukturierung durch Klassen und Objekte (Kapselung, Vererbung, Polymorphismus) | Java, C#, Python, C++ |
| Funktional | Programme als Auswertung mathematischer Funktionen, keine Seiteneffekte | Haskell, Erlang, Lisp, F# |
| Logisch | Programme als Menge logischer Regeln und Fakten, Abfragen werden inferiert | Prolog |
| Deklarativ | Beschreibt WAS berechnet werden soll, nicht WIE | SQL, HTML, CSS |

**Wichtige Begriffe:**
- **Multiparadigmen-Sprache** – Sprache, die mehrere Paradigmen unterstuetzt (z.B. Python: OOP + funktional + imperativ)
- **Seiteneffekt** – Eine Funktion veraendert Zustand ausserhalb ihres Gueltigkeitsbereichs
- **Zustandslosigkeit** – Funktionales Paradigma: Keine veraenderbaren Variablen

### Imperativ vs. Deklarativ

| Aspekt | Imperativ | Deklarativ |
|--------|----------|-----------|
| Fokus | WIE (Schritte zum Ziel) | WAS (gewuenschtes Ergebnis) |
| Kontrolle | Programmierer steuert Ablauf | System bestimmt Ablauf |
| Beispiel | Schleife zum Filtern einer Liste | SQL-Abfrage: SELECT ... WHERE |
| Zustand | Veraenderbar (mutable) | Oft unveraenderlich (immutable) |

### OOP-Konzepte (Zusammenfassung)

| Konzept | Beschreibung |
|---------|-------------|
| Klasse | Bauplan fuer Objekte mit Attributen und Methoden |
| Objekt | Konkrete Instanz einer Klasse |
| Kapselung | Zugriff auf Attribute nur ueber Getter/Setter |
| Vererbung | Unterklasse erbt von Oberklasse |
| Polymorphismus | Gleiche Methode, unterschiedliches Verhalten |
| Abstraktion | Nur relevante Details modellieren |

### Funktionale Programmierung (Zusammenfassung)

| Konzept | Beschreibung |
|---------|-------------|
| Reine Funktionen | Gleiche Eingabe → gleiche Ausgabe, keine Seiteneffekte |
| Unveraenderlichkeit (Immutability) | Variablen werden nicht veraendert, sondern neue erstellt |
| Hoehere Funktionen | Funktionen als Parameter oder Rueckgabewert |
| Rekursion | Statt Schleifen wird Rekursion verwendet |
| Lambda-Ausdruecke | Anonyme Funktionen (z.B. `x -> x * 2`) |

---

### Kompiliert vs. Interpretiert

**Definition:** Programmiersprachen unterscheiden sich darin, wie Quellcode in ausfuehrbaren Code uebersetzt wird.

| Aspekt | Kompiliert | Interpretiert |
|--------|-----------|--------------|
| Uebersetzung | Gesamter Quellcode wird vor der Ausfuehrung in Maschinencode uebersetzt | Quellcode wird zeilenweise zur Laufzeit uebersetzt |
| Ausfuehrung | Direkt vom Betriebssystem (schnell) | Durch Interpreter (langsamer) |
| Fehlererkennung | Zur Compile-Zeit (frueh) | Zur Laufzeit (spaet) |
| Beispielsprachen | C, C++, Rust, Go | Python, JavaScript, PHP, Ruby |
| Portabilitaet | Plattformabhaengig (Neukompilierung noetig) | Plattformunabhaengig (Interpreter noetig) |

**Sonderfall: Bytecode-Sprachen**
Java und C# werden in Bytecode kompiliert, der auf einer virtuellen Maschine (JVM bzw. CLR) interpretiert/JIT-kompiliert wird. → Mischform.

```
C/C++:     Quellcode  -->  Compiler  -->  Maschinencode  -->  Ausfuehrung
Python:    Quellcode  -->  Interpreter  ---------------------->  Ausfuehrung
Java:      Quellcode  -->  Compiler  -->  Bytecode  -->  JVM  -->  Ausfuehrung
```

### Stark vs. Schwach Typisiert

| Aspekt | Stark typisiert | Schwach typisiert |
|--------|----------------|------------------|
| Typumwandlung | Explizit durch Programmierer | Automatisch (implizit) |
| Typsicherheit | Hoch (Fehler werden frueh erkannt) | Niedrig (unerwartete Umwandlungen) |
| Beispiel | Java, C#, Haskell | JavaScript, PHP |

**Zusaetzlich: Statisch vs. Dynamisch Typisiert**

| Aspekt | Statisch typisiert | Dynamisch typisiert |
|--------|-------------------|-------------------|
| Typfestlegung | Zur Compile-Zeit | Zur Laufzeit |
| Variablentyp | Muss deklariert werden | Wird automatisch ermittelt |
| Beispiel | Java, C, C++ | Python, JavaScript, Ruby |

---

## Vertiefung

### Uebersicht: Paradigma + Typisierung + Ausfuehrung

| Sprache | Paradigma | Typisierung | Ausfuehrung |
|---------|----------|------------|------------|
| C | Prozedural | Statisch, schwach | Kompiliert |
| Java | OOP (Multiparadigma) | Statisch, stark | Bytecode (JVM) |
| Python | Multiparadigma | Dynamisch, stark | Interpretiert |
| JavaScript | Multiparadigma | Dynamisch, schwach | Interpretiert (JIT) |
| C# | OOP (Multiparadigma) | Statisch, stark | Bytecode (CLR) |
| Haskell | Funktional | Statisch, stark | Kompiliert |
| PHP | Prozedural/OOP | Dynamisch, schwach | Interpretiert |
| Prolog | Logisch | Dynamisch | Interpretiert |

### Typische Pruefungsaspekte
- Paradigmen benennen und Beispielsprachen zuordnen
- Kompiliert vs. interpretiert erklaeren und Sprachen zuordnen
- Stark vs. schwach typisiert unterscheiden
- OOP-Grundkonzepte erklaeren (Vererbung, Kapselung, Polymorphismus)
- Funktionale Konzepte (reine Funktionen, Immutability) kennen

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| Java als interpretiert bezeichnet | Java wird kompiliert (Bytecode), dann von der JVM ausgefuehrt |
| Python als schwach typisiert | Python ist stark, aber dynamisch typisiert |
| Deklarativ = funktional | Deklarativ ist der Oberbegriff; funktional und logisch sind Unterkategorien |
| OOP nur als "Vererbung" verstanden | OOP umfasst Kapselung, Vererbung, Polymorphismus und Abstraktion |

---

## Uebungen

**Aufgabe 1:** Ordne die folgenden Sprachen dem passenden Hauptparadigma zu: C, Haskell, Java, Prolog, SQL.

**Aufgabe 2:** Erklaere den Unterschied zwischen kompilierten und interpretierten Sprachen. Nenne je zwei Beispiele.

**Aufgabe 3:** Warum ist Python "stark, aber dynamisch typisiert"? Erklaere mit einem kurzen Beispiel.

**Aufgabe 4:** Was ist eine Multiparadigmen-Sprache? Nenne ein Beispiel und begruende, welche Paradigmen sie unterstuetzt.

---
---

# Loesungen

## Aufgabe 1
- C → Prozedural (imperativ)
- Haskell → Funktional
- Java → Objektorientiert (Multiparadigma)
- Prolog → Logisch
- SQL → Deklarativ

## Aufgabe 2
- **Kompiliert:** Der gesamte Quellcode wird vor der Ausfuehrung in Maschinencode uebersetzt. Vorteil: schnellere Ausfuehrung. Beispiele: C, C++.
- **Interpretiert:** Der Quellcode wird zeilenweise zur Laufzeit uebersetzt und ausgefuehrt. Vorteil: plattformunabhaengig. Beispiele: Python, JavaScript.

## Aufgabe 3
Python erfordert, dass Typen kompatibel sind (stark typisiert): `"5" + 3` fuehrt zu einem Fehler (kein automatisches Umwandeln). Aber der Typ einer Variable wird erst zur Laufzeit bestimmt (dynamisch typisiert): `x = 5` – kein Typ muss deklariert werden, und spaeter kann `x = "Hallo"` zugewiesen werden.

## Aufgabe 4
Eine Multiparadigmen-Sprache unterstuetzt mehrere Programmierparadigmen. Beispiel: **Python** – unterstuetzt imperative Programmierung (Schleifen, Zuweisungen), objektorientierte Programmierung (Klassen, Vererbung) und funktionale Programmierung (Lambda, map, filter, list comprehension).
