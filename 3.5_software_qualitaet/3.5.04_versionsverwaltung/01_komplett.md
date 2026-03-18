# Ueberblick und Grundlagen: 3.5.04 – Debugging

## Einordnung

- **Pruefungsteil:** 3.5 – Sicherstellen der Qualitaet von Softwareanwendungen
- **Thema-ID:** 3.5.04
- **Thema:** Fehlermeldungen analysieren und systematisch debuggen koennen

## Themenkreise

### 1. Fehlermeldungen analysieren

**Definition:** Debugging ist der systematische Prozess zum Erkennen, Lokalisieren und Beheben von Fehlern (Bugs) in Software. Es umfasst das Analysieren von Fehlermeldungen, das Nachvollziehen des Programmablaufs und den Einsatz spezialisierter Werkzeuge.

**Kernaussagen:**
- Debugging ist ein wesentlicher Teil der Softwareentwicklung
- Systematisches Vorgehen ist effizienter als "Trial and Error"
- Fehler koennen in verschiedenen Phasen auftreten (Kompilierung, Laufzeit, Logik)
- Gute Fehlermeldungen und Logging erleichtern das Debugging erheblich
- Debugging-Faehigkeiten sind pruefungsrelevant und praxisentscheidend

---

## Fehlerarten

**Definition:** Fehler in Software lassen sich nach dem Zeitpunkt ihres Auftretens und ihrer Ursache klassifizieren.

| Fehlerart | Zeitpunkt | Ursache | Beispiel |
|---|---|---|---|
| **Syntaxfehler** | Kompilierung / Interpretation | Verstoss gegen die Sprachgrammatik | Fehlende Klammer: `if (x > 5` |
| **Laufzeitfehler (Runtime Error)** | Ausfuehrung | Ungueltiger Zustand zur Laufzeit | Division durch Null, NullPointerException |
| **Logischer Fehler** | Ausfuehrung | Code laeuft fehlerfrei, liefert aber falsches Ergebnis | Berechnung: `preis * 1.19` statt `preis * 0.19` fuer MwSt-Anteil |
| **Semantischer Fehler** | Ausfuehrung | Code tut nicht, was beabsichtigt war | `<` statt `<=` in einer Schleifenbedingung |
| **Ressourcenfehler** | Ausfuehrung | Speicher, Datei, Netzwerk nicht verfuegbar | OutOfMemoryError, FileNotFoundException |

**Erklaerung:** In der Pruefung wird oft ein Codefragment gezeigt, in dem du den Fehlertyp identifizieren und die Ursache erklaeren sollst. Syntaxfehler erkennt der Compiler, logische Fehler sind am schwierigsten zu finden.

---

## Stack Traces lesen und verstehen

**Definition:** Ein Stack Trace (Stapelverfolgung) ist eine Liste der Methodenaufrufe, die zum Zeitpunkt eines Fehlers aktiv waren. Er wird bei einer nicht behandelten Exception ausgegeben.

**Aufbau eines Stack Trace:**

```
Exception in thread "main" java.lang.NullPointerException
    at com.shop.OrderService.calculateTotal(OrderService.java:42)
    at com.shop.OrderController.submitOrder(OrderController.java:28)
    at com.shop.Main.main(Main.java:15)
```

**Leserichtung und Interpretation:**

| Zeile | Bedeutung |
|---|---|
| Zeile 1 | **Fehlertyp:** NullPointerException |
| Zeile 2 (oberste) | **Fehlerort:** Methode `calculateTotal` in Datei `OrderService.java`, Zeile 42 → hier ist der Fehler aufgetreten |
| Zeile 3 | `submitOrder` hat `calculateTotal` aufgerufen |
| Zeile 4 (unterste) | `main` hat `submitOrder` aufgerufen → Einstiegspunkt |

**Leseregel:** Von oben nach unten lesen. Die **oberste Zeile nach dem Fehlertyp** zeigt den genauen Fehlerort. Die weiteren Zeilen zeigen die Aufrufkette (Call Stack).

**Haeufige Exceptions und ihre Ursachen:**

| Exception | Ursache | Typische Loesung |
|---|---|---|
| NullPointerException | Zugriff auf ein Objekt, das `null` ist | Null-Check vor Zugriff |
| ArrayIndexOutOfBoundsException | Zugriff auf Array-Index ausserhalb des gueltigen Bereichs | Index pruefen, Schleifenbedingung korrigieren |
| NumberFormatException | String kann nicht in Zahl umgewandelt werden | Eingabevalidierung vor Konvertierung |
| FileNotFoundException | Datei existiert nicht am angegebenen Pfad | Pfad pruefen, Existenz vor Zugriff pruefen |
| StackOverflowError | Unendliche Rekursion | Abbruchbedingung der Rekursion pruefen |
| ClassCastException | Ungueltiger Typ-Cast | instanceof-Pruefung vor Cast |
| ConcurrentModificationException | Aenderung einer Collection waehrend Iteration | Iterator verwenden oder CopyOnWriteArrayList |

---

## Systematischer Debugging-Ansatz

**Vorgehensweise in 6 Schritten:**

```
1. Fehler reproduzieren
        |
        v
2. Fehlermeldung / Stack Trace lesen
        |
        v
3. Hypothese aufstellen (Was koennte die Ursache sein?)
        |
        v
4. Hypothese testen (Breakpoint, Logging, Variablen pruefen)
        |
        v
5. Fehler beheben
        |
        v
6. Regressionstest (Funktioniert alles andere noch?)
```

**Details zu den Schritten:**

| Schritt | Beschreibung | Tipp |
|---|---|---|
| 1. Reproduzieren | Fehler mit denselben Eingaben/Bedingungen nachstellen | Exakte Schritte dokumentieren |
| 2. Fehlermeldung lesen | Stack Trace, Konsolenausgabe, Logfiles analysieren | Von oben nach unten lesen |
| 3. Hypothese bilden | Moegliche Ursache eingrenzen (welche Methode, welche Variable?) | "Was hat sich zuletzt geaendert?" |
| 4. Hypothese testen | Debugger einsetzen, Logging ergaenzen, Variablenwerte pruefen | Schrittweise (Step Over/Into) |
| 5. Fehler beheben | Ursache beseitigen, nicht nur Symptom kaschieren | Root Cause, nicht Workaround |
| 6. Regressionstest | Sicherstellen, dass der Fix keine neuen Fehler einfuehrt | Automatisierte Tests ausfuehren |

---

## Debugger-Werkzeuge

**Definition:** Ein Debugger ist ein Werkzeug, mit dem der Programmablauf kontrolliert angehalten, schrittweise durchlaufen und der Zustand von Variablen inspiziert werden kann.

**Zentrale Debugger-Funktionen:**

| Funktion | Beschreibung |
|---|---|
| **Breakpoint** | Haltepunkt im Code – Programm stoppt an dieser Stelle |
| **Conditional Breakpoint** | Breakpoint, der nur bei erfuellter Bedingung ausloest (z.B. `i == 42`) |
| **Step Over (F10)** | Naechste Zeile ausfuehren, ohne in Methodenaufrufe hineinzuspringen |
| **Step Into (F11)** | In den naechsten Methodenaufruf hineinspringen |
| **Step Out** | Aktuelle Methode bis zum Ende ausfuehren und zurueckkehren |
| **Watch** | Variable ueberwachen – Wert wird bei jedem Schritt angezeigt |
| **Call Stack** | Zeigt die aktuelle Aufrufhierarchie (welche Methode hat welche aufgerufen?) |
| **Evaluate Expression** | Ausdruck im aktuellen Kontext auswerten (z.B. `array.length`) |

**Gaengige Debugger:**

| Umgebung | Debugger |
|---|---|
| Java | IntelliJ IDEA Debugger, Eclipse Debugger |
| Python | pdb, VS Code Debugger, PyCharm Debugger |
| JavaScript | Browser DevTools (Chrome, Firefox), VS Code Debugger |
| C# | Visual Studio Debugger |

---

## Logging

**Definition:** Logging ist das systematische Aufzeichnen von Ereignissen und Zustaenden waehrend der Programmausfuehrung. Im Gegensatz zum Debugger laeuft Logging auch im Produktivbetrieb.

**Logging-Level:**

| Level | Bedeutung | Beispiel |
|---|---|---|
| **TRACE** | Sehr detaillierte Informationen (nur Entwicklung) | "Entering method calculateTotal with params: [42, 3.99]" |
| **DEBUG** | Debugging-Informationen (Entwicklung/Test) | "User ID: 42, Cart items: 3" |
| **INFO** | Allgemeine Informationen ueber den Programmablauf | "Order #1234 successfully placed" |
| **WARN** | Hinweis auf moegliches Problem, Programm laeuft weiter | "Database connection pool running low (90% used)" |
| **ERROR** | Fehler aufgetreten, Funktion konnte nicht ausgefuehrt werden | "Failed to send confirmation email: SMTP connection refused" |
| **FATAL** | Kritischer Fehler, Programm kann nicht weiterlaufen | "Database unreachable – application shutting down" |

**Best Practices fuer Logging:**
- Im Produktivbetrieb: Level INFO oder hoeher
- In Entwicklung/Test: Level DEBUG oder TRACE
- Keine sensiblen Daten loggen (Passwoerter, Kreditkarten, personenbezogene Daten)
- Strukturierte Logs verwenden (JSON-Format fuer automatisierte Auswertung)
- Kontextinformationen mitloggen (Zeitstempel, User-ID, Request-ID)

---

## Typische Pruefungsaspekte

- Fehlerart anhand eines Codefragments identifizieren
- Stack Trace lesen und den Fehlerort benennen
- Systematische Debugging-Schritte beschreiben
- Debugger-Funktionen (Breakpoint, Step Over/Into, Watch) erklaeren
- Logging-Level kennen und einordnen koennen
- Unterschied Syntaxfehler vs. Laufzeitfehler vs. logischer Fehler

## Haeufige Fehler

| Fehler | Richtigstellung |
|---|---|
| Logische Fehler werden vom Compiler erkannt | Nein – der Compiler erkennt nur Syntaxfehler. Logische Fehler liefern falsche Ergebnisse ohne Fehlermeldung |
| `System.out.println` ist ausreichend fuer Debugging | Fuer schnelle Checks ok, aber ein Debugger (Breakpoints, Watch) ist systematischer und effizienter |
| Stack Trace von unten nach oben lesen | Nein – von oben nach unten. Die oberste Zeile zeigt den Fehlerort |
| Debugging ist nur etwas fuer Anfaenger | Nein – Debugging ist eine professionelle Kernkompetenz in der Softwareentwicklung |
| Logging im Produktivbetrieb auf DEBUG stellen | Nein – zu viele Logdaten, Performanceprobleme. Produktiv: INFO oder hoeher |

---

## Beispiele

### Beispiel 1: Stack Trace analysieren

**Szenario:** Ein Webshop wirft folgenden Fehler:

```
java.lang.NullPointerException
    at com.shop.CartService.getItemPrice(CartService.java:35)
    at com.shop.CartService.calculateTotal(CartService.java:22)
    at com.shop.CheckoutController.checkout(CheckoutController.java:48)
```

**Analyse:**
1. **Fehlertyp:** NullPointerException → Ein Objekt ist `null`, auf das zugegriffen wird
2. **Fehlerort:** `CartService.java`, Zeile 35, Methode `getItemPrice`
3. **Aufrufkette:** `checkout()` → `calculateTotal()` → `getItemPrice()` → Fehler
4. **Hypothese:** In Zeile 35 wird auf ein Produkt zugegriffen, das nicht existiert (z.B. Produkt wurde geloescht, ist aber noch im Warenkorb)
5. **Loesung:** Null-Check vor dem Zugriff auf den Artikelpreis

---

### Beispiel 2: Logischer Fehler finden

**Szenario:** Eine Funktion soll den Durchschnitt eines Arrays berechnen, liefert aber falsche Ergebnisse.

```
FUNKTION berechneDurchschnitt(werte):
    summe = 0
    FUER i = 0 BIS werte.laenge - 1:
        summe = summe + werte[i]
    ENDE FUER
    RUECKGABE summe / werte.laenge - 1    // <-- Fehler!
ENDE FUNKTION
```

**Debugging mit Watch:**
- Eingabe: `[10, 20, 30]` → Erwartetes Ergebnis: 20
- Watch auf `summe`: nach Schleife = 60 ✓
- Watch auf `werte.laenge`: 3 ✓
- Ergebnis: 60 / 3 - 1 = 19 (statt 20)

**Fehler:** Operatorpraezedenz – Division wird vor Subtraktion ausgefuehrt. Es muesste `summe / (werte.laenge)` heissen. Die `- 1` gehoert nicht zur Berechnung des Durchschnitts. Korrekt:

```
RUECKGABE summe / werte.laenge
```

---

### Beispiel 3: Systematisches Debugging mit Breakpoints

**Szenario:** Eine Webanwendung zeigt nach dem Login eine leere Seite statt des Dashboards.

**Schritt-fuer-Schritt:**

| Schritt | Aktion | Ergebnis |
|---|---|---|
| 1. Reproduzieren | Login mit Testbenutzer "admin" / "test123" | Leere Seite nach Login |
| 2. Fehlermeldung | Browser-Konsole pruefen | Keine Fehlermeldung sichtbar |
| 3. Server-Logs pruefen | Log-Level auf DEBUG setzen | "User 'admin' logged in, loading dashboard data..." |
| 4. Breakpoint setzen | In `DashboardController.loadData()`, Zeile 15 | Variable `userData` ist `null` |
| 5. Step Into | In `UserRepository.findByUsername("admin")` | SQL-Query liefert kein Ergebnis |
| 6. Ursache | Datenbankschema wurde migriert, Username-Spalte heisst jetzt `user_name` statt `username` | Query sucht in falscher Spalte |
| 7. Fix | SQL-Query anpassen: `WHERE user_name = ?` | Dashboard wird korrekt geladen |
| 8. Regressionstest | Alle Login-bezogenen Tests ausfuehren | Alle Tests bestanden |

---

## Uebungen

**Aufgabe 1:** Gegeben ist folgender Stack Trace. Bestimme den Fehlertyp, den Fehlerort und beschreibe eine moegliche Ursache.
```
java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 5
    at com.app.DataProcessor.processRow(DataProcessor.java:67)
    at com.app.DataProcessor.processAll(DataProcessor.java:31)
    at com.app.Main.main(Main.java:12)
```

**Aufgabe 2:** Erklaere den Unterschied zwischen einem Breakpoint und einem Conditional Breakpoint. Nenne ein Szenario, in dem ein Conditional Breakpoint sinnvoll ist.

**Aufgabe 3:** Ein Programm berechnet den Gesamtpreis falsch. Beschreibe dein systematisches Vorgehen zum Debuggen in mindestens 5 Schritten.

---
---

# Loesungen

## Aufgabe 1

- **Fehlertyp:** ArrayIndexOutOfBoundsException (Laufzeitfehler)
- **Fehlerort:** `DataProcessor.java`, Zeile 67, Methode `processRow`
- **Beschreibung:** Es wird versucht, auf den Index 5 eines Arrays zuzugreifen, das nur 5 Elemente hat (Indizes 0–4). Index 5 ist ausserhalb des gueltigen Bereichs.
- **Moegliche Ursache:** Die Schleife zaehlt bis `<= array.length` statt `< array.length` (Off-by-One-Fehler). Oder ein hartcodierter Index wird verwendet, der bei bestimmten Daten zu gross ist.
- **Loesung:** Schleifenbedingung auf `< array.length` aendern oder Index vor Zugriff pruefen.

## Aufgabe 2

- **Breakpoint:** Das Programm wird bei jedem Durchlauf an dieser Stelle angehalten. Beispiel: Breakpoint in Zeile 42 → Programm stoppt immer in Zeile 42.
- **Conditional Breakpoint:** Das Programm wird nur angehalten, wenn eine bestimmte Bedingung erfuellt ist. Beispiel: Breakpoint in Zeile 42 mit Bedingung `i == 999` → Programm stoppt nur, wenn die Variable `i` den Wert 999 hat.
- **Szenario:** Eine Schleife durchlaeuft 1000 Datensaetze, aber nur bei Datensatz 999 tritt ein Fehler auf. Mit einem normalen Breakpoint muesste man 999 Mal "Continue" druecken. Mit einem Conditional Breakpoint (`i == 999`) stoppt das Programm direkt beim problematischen Durchlauf.

## Aufgabe 3

1. **Fehler reproduzieren:** Konkreten Testfall erstellen (z.B. 3 Artikel mit bekannten Preisen, erwartetes Ergebnis manuell berechnen).
2. **Fehlermeldung pruefen:** Konsolenausgabe und Logfiles auf Exceptions oder Warnungen pruefen.
3. **Hypothese aufstellen:** "Die Berechnung koennte bei der Mehrwertsteuer oder beim Rabatt falsch sein."
4. **Breakpoint setzen:** In der Methode `berechneGesamtpreis()` einen Breakpoint setzen und Watch auf die relevanten Variablen (Einzelpreise, Summe, MwSt, Rabatt).
5. **Schrittweise durchgehen:** Mit Step Over/Step Into den Programmablauf verfolgen und die Variablenwerte bei jedem Schritt pruefen.
6. **Fehlerursache identifizieren:** Z.B. "MwSt wird auf den bereits rabattierten Preis und nochmal auf den Originalpreis berechnet."
7. **Fehler beheben:** Berechnung korrigieren.
8. **Regressionstest:** Alle bestehenden Tests ausfuehren, um sicherzustellen, dass der Fix keine Seiteneffekte hat.
