# 3.3.02 – Beispiele: Planen mit geeigneten Modellen

## Beispiel 1: ERM → Relationales Modell (Bibliothek)

### Szenario
Eine Bibliothek verwaltet Buecher und Mitglieder. Mitglieder koennen Buecher ausleihen. Ein Buch kann von mehreren Mitgliedern (nacheinander) ausgeliehen werden, ein Mitglied kann mehrere Buecher gleichzeitig ausleihen.

### ERM

```
+------------+                              +------------+
|  Mitglied  |---n----< Ausleihe >----m----|   Buch     |
+------------+          +-------+           +------------+
| MitgliedNr |          | Datum |           | ISBN       |
| Name       |          | Rueck-|           | Titel      |
| Adresse    |          | gabe  |           | Autor      |
+------------+                              | Verlag     |
                                            +------------+
```

### Relationales Modell (nach Transformation)

```
Mitglied (MitgliedNr PK, Name, Adresse)
Buch (ISBN PK, Titel, Autor, Verlag)
Ausleihe (MitgliedNr FK, ISBN FK, Datum, Rueckgabedatum)
          PK = (MitgliedNr, ISBN, Datum)
```

**Erklaerung**: Die n:m-Beziehung wird durch die Zwischentabelle `Ausleihe` aufgeloest. Das `Datum` wird Teil des zusammengesetzten Primaerschluessels, damit das gleiche Buch vom gleichen Mitglied mehrfach (zu verschiedenen Zeiten) ausgeliehen werden kann.

---

## Beispiel 2: Klassendiagramm (Online-Shop)

### Szenario
Ein Online-Shop verwaltet Kunden, Bestellungen und Produkte. Kunden koennen mehrere Bestellungen aufgeben. Jede Bestellung enthaelt mehrere Bestellpositionen. Es gibt physische und digitale Produkte.

```
+-------------------+          +-------------------+
|      Kunde        |          |    Bestellung     |
+-------------------+ 1    *  +-------------------+
| - kundenNr: int   |◇------->| - bestellNr: int  |
| - name: String    |         | - datum: Date     |
| - email: String   |         | - status: String  |
+-------------------+         +-------------------+
| + bestellen()     |         | + berechneTotal() |
| + stornieren()    |         | + stornieren()    |
+-------------------+         +-------------------+
                                      |
                                      | 1..*
                                      v
                              +-------------------+
                              | Bestellposition   |
                              +-------------------+
                              | - menge: int      |
                              | - einzelpreis: double|
                              +-------------------+
                              | + getGesamt(): double|
                              +-------------------+
                                      |
                                      | *    1
                                      v
                              +-------------------+
                              |    Produkt        |
                              +-------------------+
                              | - produktNr: int  |
                              | - name: String    |
                              | - preis: double   |
                              +-------------------+
                              | + getDetails()    |
                              +-------------------+
                                     △
                                    / \
                   +----------------+ +------------------+
                   | PhysischesProdukt| | DigitalesProdukt |
                   +----------------+ +------------------+
                   | - gewicht: double| | - dateigroesse: long|
                   | - lagerort: String| | - downloadURL: String|
                   +----------------+ +------------------+
                   | + versenden()  | | + bereitstellen()|
                   +----------------+ +------------------+
```

**Erklaerung**:
- Kunde ◇→ Bestellung: **Aggregation** (Bestellung kann auch ohne Kunde-Objekt existieren, z.B. Gastbestellung)
- Bestellung → Bestellposition: **Komposition** wuerde auch passen (Position existiert nicht ohne Bestellung)
- Produkt → PhysischesProdukt / DigitalesProdukt: **Vererbung**

---

## Beispiel 3: Sequenzdiagramm (Onlinekauf)

### Szenario
Ein Kunde kauft einen Artikel im Online-Shop. Das System prueft den Bestand, erstellt die Bestellung und versendet eine Bestaetigung.

```
  Kunde       WebShop      Lagersystem    Zahlungsdienst   E-Mail-Service
    |            |              |               |               |
    |--waehle -->|              |               |               |
    |  Artikel   |              |               |               |
    |            |--pruefeBestand()-->           |               |
    |            |              |               |               |
    |            |<--verfuegbar-|               |               |
    |            |              |               |               |
    |--bestelle->|              |               |               |
    |            |--reserviere()-->              |               |
    |            |              |               |               |
    |            |--bezahle()---+-------------->|               |
    |            |              |               |               |
    |            |<--Zahlungsbestaetigung-------|               |
    |            |              |               |               |
    |            |--erstelleBestellung()        |               |
    |            |              |               |               |
    |            |--sendeBestaetigung()--+------+-------------->|
    |            |              |               |               |
    |<---Bestaetigung (E-Mail)--+------+-------+---------------|
    |            |              |               |               |
```

---

## Beispiel 4: Aktivitaetsdiagramm (Reklamationsprozess)

### Szenario
Ein Kunde reklamiert ein Produkt. Der Prozess umfasst Pruefung und Entscheidung.

```
         ●
         |
  [Reklamation eingehen]
         |
  [Reklamation erfassen]
         |
  ═══════════════════  (Fork - parallele Aktivitaeten)
     |              |
[Ware pruefen]  [Kaufbeleg pruefen]
     |              |
  ═══════════════════  (Join)
         |
        ◇ Berechtigt?
       / \
     ja    nein
     /       \
    ◇         [Ablehnung
   / \         mitteilen]
 Reparatur     |
 moeglich?     ◉
  /    \
ja      nein
/        \
[Ware    [Erstattung
reparieren] veranlassen]
  \        /
   \      /
[Kunde informieren]
      |
      ◉
```

---

## Beispiel 5: Zustandsdiagramm (Benutzerkonto)

### Szenario
Ein Benutzerkonto durchlaeuft verschiedene Zustaende von der Registrierung bis zur Loeschung.

```
    ●
    |  registriert
    v
+-------------+  E-Mail bestaetigt   +-----------+
| Registriert |--------------------->|  Aktiv    |
+-------------+                      +-----------+
    |                                  |       |
    | Timeout (48h)        3x falsches |       | Benutzer
    | ohne Bestaetigung     Passwort   |       | loescht Konto
    v                                  v       |
+-----------+                    +-----------+ |
| Abgelaufen|                    | Gesperrt  | |
+-----------+                    +-----------+ |
                                   |           |
                         Admin     |           |
                         entsperrt |           |
                                   v           v
                              +-----------+  +-----------+
                              |  Aktiv    |  | Geloescht |
                              +-----------+  +-----------+
                                                   |
                                                   v
                                                   ◉
```

---

## Beispiel 6: Mockup-Beschreibung (Login-Seite)

```
+--------------------------------------------------+
|  LOGO        Firmenname         [DE|EN]          |
+--------------------------------------------------+
|                                                  |
|              +---------------------------+       |
|              |       ANMELDUNG           |       |
|              +---------------------------+       |
|              |                           |       |
|              | E-Mail:                   |       |
|              | [________________________]|       |
|              |                           |       |
|              | Passwort:                 |       |
|              | [________________________]|       |
|              |                           |       |
|              | [ ] Angemeldet bleiben    |       |
|              |                           |       |
|              | [====== ANMELDEN ======] |       |
|              |                           |       |
|              | Passwort vergessen?       |       |
|              | Noch kein Konto?          |       |
|              |   → Registrieren          |       |
|              +---------------------------+       |
|                                                  |
+--------------------------------------------------+
|  Impressum | Datenschutz | Kontakt              |
+--------------------------------------------------+
```

**Anmerkungen zum Mockup**:
- Eingabefelder fuer E-Mail und Passwort
- Checkbox "Angemeldet bleiben"
- Button "Anmelden" prominent hervorgehoben
- Links: Passwort vergessen, Registrierung
- Sprachumschaltung oben rechts
