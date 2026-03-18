# Beispiele: 3.4.07 – Software-Entwicklungswerkzeuge

## Beispiel 1: Build-Prozess eines C-Programms

**Szenario:** Ein Entwickler schreibt ein C-Programm, das aus zwei Dateien besteht: `main.c` und `math_utils.c`. Die Datei `math_utils.c` stellt eine Funktion `addiere()` bereit, die in `main.c` aufgerufen wird.

**Ablauf:**

| Schritt | Werkzeug | Aktion | Ergebnis |
|---------|---------|--------|---------|
| 1 | Praeprocessor | `#include`-Anweisungen aufloesen | Erweiterter Quellcode |
| 2 | Compiler (gcc -c) | `main.c` → `main.o`, `math_utils.c` → `math_utils.o` | Objektdateien |
| 3 | Linker (gcc) | `main.o` + `math_utils.o` + Standardbibliothek → `programm` | Ausfuehrbare Datei |
| 4 | Ausfuehrung | `./programm` | Programmausgabe |

**Fehlerszenarien:**
- Syntaxfehler in `main.c` → **Compiler** meldet Fehler zur Compile-Zeit
- `addiere()` wird aufgerufen, aber `math_utils.o` nicht eingebunden → **Linker** meldet "undefined reference"
- Programm laeuft, berechnet aber falsch → **Debugger** zur Laufzeitanalyse

---

## Beispiel 2: Debugging einer Java-Anwendung

**Szenario:** Ein Java-Programm berechnet Rabatte fuer eine E-Commerce-Plattform. Bei Bestellungen ueber 100 EUR soll 10% Rabatt gewaehrt werden. Im Test zeigt sich, dass der Rabatt nie angewendet wird.

**Vorgehensweise mit Debugger (z.B. IntelliJ IDEA):**

| Schritt | Aktion | Ergebnis |
|---------|--------|---------|
| 1 | Breakpoint setzen in Zeile `if (bestellwert > 100)` | Ausfuehrung haelt an dieser Stelle an |
| 2 | Programm im Debug-Modus starten | Programm laeuft bis zum Breakpoint |
| 3 | Variable `bestellwert` inspizieren | Wert ist 100 (nicht > 100!) |
| 4 | Fehler erkannt | Bedingung muss `>=` statt `>` sein |
| 5 | Code korrigieren: `if (bestellwert >= 100)` | Rabatt wird korrekt angewendet |

**Erkenntnis:** Der Debugger zeigt den exakten Variablenwert zum Zeitpunkt der Ausfuehrung. Ohne Debugger haette man den Fehler nur durch erneute Code-Analyse oder umfangreiche Log-Ausgaben finden koennen.

---

## Beispiel 3: Versionsverwaltung mit Git im Team

**Szenario:** Drei Entwickler arbeiten an einem Webprojekt. Entwickler A implementiert die Login-Seite, Entwickler B den Warenkorb, Entwickler C die Benutzerverwaltung.

**Git-Workflow:**

```
main:     o---o---o---------------------------o---o---o  (Releases)
               \         \                   /   /
feature/login:  o---o---o  \            Merge   /
                            \              /   /
feature/warenkorb:           o---o---o---o    /
                                         \  /
feature/benutzerverwaltung:   o---o---o---o
```

| Schritt | Entwickler | Git-Befehl | Aktion |
|---------|-----------|-----------|--------|
| 1 | A | `git checkout -b feature/login` | Neuen Branch erstellen |
| 2 | A | `git commit -m "Login-Formular implementiert"` | Aenderungen lokal speichern |
| 3 | A | `git push origin feature/login` | Branch an Remote senden |
| 4 | A | Pull Request erstellen | Code Review durch Team |
| 5 | Team | `git merge feature/login` | Branch in main einfuegen |
| 6 | B, C | `git pull origin main` | Aktuelle main-Version holen |

**Merge-Konflikt-Szenario:** Entwickler A und B haben beide die Datei `header.html` geaendert. Beim Merge entsteht ein Konflikt. Loesung: Manuell die Aenderungen zusammenfuehren, dann committen.

---

## Beispiel 4: Unit-Tests mit JUnit

**Szenario:** Eine Java-Klasse `Rechner` soll getestet werden:

```
Klasse: Rechner
Methoden: addiere(int a, int b), dividiere(int a, int b)
```

**Testfaelle:**

| Testfall | Eingabe | Erwartetes Ergebnis | Beschreibung |
|----------|---------|-------------------|-------------|
| testAddiere | addiere(3, 4) | 7 | Normalfall: Addition positiver Zahlen |
| testAddiereNegativ | addiere(-3, 4) | 1 | Grenzfall: Negative Zahlen |
| testDividiere | dividiere(10, 2) | 5 | Normalfall: Division |
| testDividiereNull | dividiere(10, 0) | ArithmeticException | Fehlerfall: Division durch Null |

**Ergebnis:** Alle Tests gruen → Code funktioniert korrekt. Test `testDividiereNull` stellt sicher, dass die Fehlerbehandlung korrekt implementiert ist.

---

## Beispiel 5: Programmgenerator – ORM

**Szenario:** Aus einer Datenbanktabelle `kunden` soll automatisch eine Java-Klasse generiert werden.

**Datenbanktabelle:**

| Spalte | Typ | Constraint |
|--------|-----|-----------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT |
| name | VARCHAR(100) | NOT NULL |
| email | VARCHAR(150) | UNIQUE |
| erstellt_am | DATETIME | DEFAULT NOW() |

**Generierter Code (vereinfacht, Hibernate-Stil):**

```
@Entity
@Table(name = "kunden")
public class Kunde {
    @Id @GeneratedValue
    private int id;

    @Column(nullable = false)
    private String name;

    @Column(unique = true)
    private String email;

    private LocalDateTime erstelltAm;

    // Getter und Setter automatisch generiert
}
```

**Vorteil:** Keine manuelle Erstellung der Klasse noetig. Aenderungen an der Datenbank koennen automatisch in den Code uebernommen werden.
