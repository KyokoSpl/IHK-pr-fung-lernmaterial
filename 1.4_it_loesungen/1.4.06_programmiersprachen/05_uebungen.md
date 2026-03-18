# Uebungen: 1.4.06 – Programmiersprachen

## Variablen und Datentypen

**Aufgabe 1:** Ordne die folgenden Werte den passenden Datentypen zu: `42`, `"Hallo"`, `true`, `3.14`, `'A'`.

**Aufgabe 2:** Erklaere den Unterschied zwischen einem Array und einer Liste.

---

## Kontrollstrukturen

**Aufgabe 3:** Schreibe Pseudocode fuer eine Funktion, die prueft, ob eine Zahl durch 3 UND durch 5 teilbar ist. Ausgabe: „FizzBuzz", nur durch 3: „Fizz", nur durch 5: „Buzz", sonst die Zahl.

**Aufgabe 4:** Welche Schleifenart (for, while, do-while) ist jeweils geeignet?
- a) Alle Elemente eines Arrays durchlaufen
- b) Benutzereingabe solange wiederholen, bis sie gueltig ist
- c) Menu-Anzeige: Mindestens einmal anzeigen, dann wiederholen bei Wunsch

---

## OOP

**Aufgabe 5:** Erklaere die Begriffe: Klasse, Objekt, Attribut, Methode – jeweils in einem Satz.

**Aufgabe 6:** Was bedeutet Kapselung (Encapsulation) in der OOP? Warum werden Attribute oft `private` gesetzt?

---

## Compiler, Interpreter, Debugging

**Aufgabe 7:** Nenne zwei Vorteile eines Compilers und zwei eines Interpreters.

**Aufgabe 8:** Ordne die folgenden Fehler der korrekten Fehlerart zu (Syntaxfehler, Laufzeitfehler, Logikfehler):
- a) Fehlende schliessende Klammer
- b) Berechnung ergibt falsches Ergebnis
- c) Zugriff auf ein nicht existierendes Array-Element
- d) Semikolon vergessen

---

---

# Loesungen

## Aufgabe 1
`42` → Integer, `"Hallo"` → String, `true` → Boolean, `3.14` → Float/Double, `'A'` → Char.

## Aufgabe 2
Array: Feste Groesse, gleicher Datentyp, direkter Indexzugriff. Liste: Dynamische Groesse, kann wachsen/schrumpfen, verschiedene Implementierungen (ArrayList, LinkedList).

## Aufgabe 3
```
FUNKTION fizzBuzz(zahl: Integer)
    WENN zahl MODULO 3 == 0 UND zahl MODULO 5 == 0 DANN
        AUSGABE "FizzBuzz"
    SONST WENN zahl MODULO 3 == 0 DANN
        AUSGABE "Fizz"
    SONST WENN zahl MODULO 5 == 0 DANN
        AUSGABE "Buzz"
    SONST
        AUSGABE zahl
    ENDE WENN
ENDE FUNKTION
```

## Aufgabe 4
a) `for`-Schleife (bekannte Anzahl). b) `while`-Schleife (Bedingung vor Ausfuehrung pruefen). c) `do-while`-Schleife (mindestens 1 Durchlauf garantiert).

## Aufgabe 5
Klasse: Bauplan/Vorlage fuer Objekte mit definierten Attributen und Methoden. Objekt: Konkrete Instanz einer Klasse mit eigenen Attributwerten. Attribut: Eigenschaft/Variable eines Objekts (z.B. Name, Alter). Methode: Funktion, die zum Objekt gehoert und dessen Verhalten beschreibt.

## Aufgabe 6
Kapselung bedeutet, dass die internen Daten (Attribute) eines Objekts vor direktem Zugriff von aussen geschuetzt werden. Attribute werden `private` gesetzt, weil der Zugriff nur ueber kontrollierte Methoden (Getter/Setter) erfolgen soll → Datenkonsistenz, Validierung, spaeteren Aenderungen ohne Auswirkung auf externe Nutzung.

## Aufgabe 7
Compiler: (1) Schnellere Ausfuehrung (vorkompiliert). (2) Fehler werden vor Ausfuehrung erkannt. Interpreter: (1) Sofortige Ausfuehrung ohne Kompilierungsschritt. (2) Plattformunabhaengig (solange Interpreter vorhanden).

## Aufgabe 8
a) Syntaxfehler – verletzt Sprachregeln. b) Logikfehler – Programm laeuft, Ergebnis falsch. c) Laufzeitfehler – ArrayIndexOutOfBounds zur Laufzeit. d) Syntaxfehler – verletzt Sprachregeln.
