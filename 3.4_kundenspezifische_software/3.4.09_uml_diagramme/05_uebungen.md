# Uebungen: 3.4.09 – UML-Diagramme erstellen

## Klassendiagramm

**Aufgabe 1:** Leite aus folgendem Text ein Klassendiagramm ab (Klassen, Attribute, Methoden, Beziehungen mit Kardinalitaeten):
> "Ein Fitnessstudio verwaltet Mitglieder und Kurse. Jedes Mitglied hat eine Mitgliedsnummer, einen Namen und ein Geburtsdatum. Kurse haben eine Bezeichnung, einen Wochentag und eine Uhrzeit. Ein Mitglied kann sich fuer mehrere Kurse anmelden, und ein Kurs hat mehrere Teilnehmer. Jede Anmeldung speichert das Datum."

**Aufgabe 2:** Erklaere den Unterschied zwischen Aggregation und Komposition. Gib je ein Beispiel.

---

## Anwendungsfalldiagramm

**Aufgabe 3:** Erstelle ein Anwendungsfalldiagramm fuer folgendes Szenario:
> "In einem Ticketsystem koennen Kunden Tickets erstellen und den Status einsehen. Supportmitarbeiter bearbeiten Tickets und koennen Tickets eskalieren. Fuer die Bearbeitung ist ein Login erforderlich. Optional kann ein Ticket mit einem Screenshot versehen werden."

Identifiziere: Akteure, Use Cases, include- und extend-Beziehungen.

---

## Zustandsdiagramm

**Aufgabe 4:** Zeichne ein Zustandsdiagramm fuer eine Ampel mit den Zustaenden: Rot, Rot-Gelb, Gruen, Gelb. Definiere die Transitionen.

---

## Sequenzdiagramm

**Aufgabe 5:** Zeichne ein Sequenzdiagramm fuer folgenden Ablauf:
> "Ein Benutzer ruft eine Produktseite im Browser auf. Der Browser sendet eine Anfrage an den Webserver. Der Webserver fragt die Produktdaten aus der Datenbank ab. Die Datenbank liefert die Daten zurueck. Der Webserver sendet die HTML-Seite an den Browser."

---

## Aktivitaetsdiagramm

**Aufgabe 6:** Zeichne ein Aktivitaetsdiagramm fuer den Ablauf "Passwort zuruecksetzen":
> "Der Benutzer klickt auf 'Passwort vergessen', gibt seine E-Mail ein, das System prueft ob die E-Mail existiert. Falls ja, wird ein Reset-Link per E-Mail gesendet. Falls nein, wird eine Fehlermeldung angezeigt."

---
---

# Loesungen

## Aufgabe 1

**Klassen, Attribute, Methoden:**

| Klasse | Attribute | Methoden |
|--------|-----------|----------|
| Mitglied | - mitgliedsNr: int, - name: String, - geburtsdatum: Date | + anmelden(Kurs): void |
| Kurs | - bezeichnung: String, - wochentag: String, - uhrzeit: Time | + getTeilnehmer(): List |
| Anmeldung | - datum: Date | – |

**Beziehungen:**
- Mitglied * ─── * Kurs (n:m-Beziehung, aufgeloest durch Assoziationsklasse Anmeldung)
- Mitglied 1 ─── * Anmeldung
- Anmeldung * ─── 1 Kurs

**Klassendiagramm:**

```
+-------------------+       +------------------+       +-------------------+
|    Mitglied       | 1   * |   Anmeldung      | *   1 |      Kurs         |
+-------------------+-------+------------------+-------+-------------------+
| - mitgliedsNr: int|       | - datum: Date    |       | - bezeichnung:    |
| - name: String    |       +------------------+       |   String          |
| - geburtsdatum:   |                                  | - wochentag: String|
|   Date            |                                  | - uhrzeit: Time   |
+-------------------+                                  +-------------------+
| + anmelden()      |                                  | + getTeilnehmer() |
+-------------------+                                  +-------------------+
```

## Aufgabe 2
- **Aggregation (◇):** "Hat-ein"-Beziehung, bei der das Teil auch ohne das Ganze existieren kann. Beispiel: Abteilung ◇── Mitarbeiter. Wird die Abteilung aufgeloest, existieren die Mitarbeiter weiterhin.
- **Komposition (◆):** "Besteht-aus"-Beziehung, bei der das Teil nicht ohne das Ganze existieren kann. Beispiel: Haus ◆── Raum. Wird das Haus abgerissen, existieren die Raeume nicht mehr.

## Aufgabe 3

**Akteure:** Kunde, Supportmitarbeiter
**Use Cases:** Ticket erstellen, Status einsehen, Ticket bearbeiten, Ticket eskalieren, Login, Screenshot anhaengen

**Beziehungen:**
- "Ticket bearbeiten" <<include>> "Login" (immer erforderlich)
- "Ticket erstellen" <<extend>> "Screenshot anhaengen" (optional)

```
+-------------------------------------------+
|          Ticketsystem (System)            |
|                                           |
|  (Ticket erstellen)                       |
|       |---<<extend>>-->(Screenshot        |
|       |                 anhaengen)        |
|  (Status einsehen)                        |
|  (Ticket bearbeiten)--<<include>>-->(Login)|
|  (Ticket eskalieren)                      |
+-------------------------------------------+
  |          |
Kunde    Supportmitarbeiter

Zuordnung:
- Kunde: Ticket erstellen, Status einsehen
- Supportmitarbeiter: Ticket bearbeiten, Ticket eskalieren
```

## Aufgabe 4

```
   (●)
    |
    v
+-------+  timer    +-----------+  timer   +-------+  timer   +-------+
|  Rot  |---------->| Rot-Gelb  |--------->| Gruen |--------->| Gelb  |
+-------+           +-----------+          +-------+          +-------+
    ^                                                             |
    |                         timer                               |
    +-------------------------------------------------------------+
```

Transitionen:
- Rot → Rot-Gelb (timer abgelaufen)
- Rot-Gelb → Gruen (timer abgelaufen)
- Gruen → Gelb (timer abgelaufen)
- Gelb → Rot (timer abgelaufen)
→ Zyklischer Ablauf (kein Endzustand, da Ampel dauerhaft laeuft)

## Aufgabe 5

```
  Benutzer        Browser         Webserver       Datenbank
     |               |               |               |
     | 1: URL eingeben|               |               |
     |-------------->|               |               |
     |               | 2: GET /produkt/123            |
     |               |-------------->|               |
     |               |               | 3: SELECT *   |
     |               |               | FROM produkte |
     |               |               | WHERE id=123  |
     |               |               |-------------->|
     |               |               |               |
     |               |               | 4: Produktdaten|
     |               |               |<--------------|
     |               |               |               |
     |               | 5: HTML-Seite |               |
     |               |<--------------|               |
     |               |               |               |
     | 6: Seite anzeigen              |               |
     |<--------------|               |               |
```

## Aufgabe 6

```
        (●) Start
         |
+--------v--------------+
| "Passwort vergessen"  |
| klicken               |
+--------+--------------+
         |
+--------v--------------+
| E-Mail-Adresse        |
| eingeben              |
+--------+--------------+
         |
+--------v--------------+
| E-Mail in Datenbank   |
| pruefen               |
+--------+--------------+
         |
      <◇>
     /    \
[existiert] [existiert nicht]
    |              |
+---v----------+  +---v-----------+
| Reset-Link   |  | Fehlermeldung |
| per E-Mail   |  | anzeigen      |
| senden       |  +---+-----------+
+---+----------+      |
    |                  |
    +------+------+----+
           |
          (◉) Ende
```
