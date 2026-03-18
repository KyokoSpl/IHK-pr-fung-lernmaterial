# Beispiele: 3.4.09 – UML-Diagramme erstellen

## Beispiel 1: Klassendiagramm aus Anforderungstext

**Anforderungstext:**
> "Eine Bibliothek verwaltet Buecher und Mitglieder. Jedes Buch hat eine ISBN, einen Titel und einen Autor. Mitglieder haben eine Mitgliedsnummer und einen Namen. Ein Mitglied kann mehrere Buecher ausleihen. Jede Ausleihe hat ein Ausleihdatum und ein Rueckgabedatum."

**Ableitung:**

| Element | Typ | Attribute | Methoden |
|---------|-----|-----------|----------|
| Buch | Klasse | - isbn: String, - titel: String, - autor: String | + getDetails(): String |
| Mitglied | Klasse | - mitgliedsNr: int, - name: String | + ausleihen(Buch): void |
| Ausleihe | Klasse (Assoziationsklasse) | - ausleihdatum: Date, - rueckgabedatum: Date | + berechneGebuehr(): double |

**Beziehungen:**
- Mitglied 1 ─── * Ausleihe (ein Mitglied hat 0..* Ausleihen)
- Ausleihe * ─── 1 Buch (jede Ausleihe bezieht sich auf genau ein Buch)

**Klassendiagramm:**

```
+-------------------+         +------------------+
|    Mitglied       |  1   *  |    Ausleihe      |
+-------------------+---------+------------------+
| - mitgliedsNr: int|         | - ausleihdatum:  |
| - name: String    |         |   Date           |
+-------------------+         | - rueckgabedatum:|
| + ausleihen()     |         |   Date           |
+-------------------+         +------------------+
                              | + berechne-      |
                              |   Gebuehr()      |
                              +--------+---------+
                                       | *     1
                              +--------v---------+
                              |      Buch        |
                              +------------------+
                              | - isbn: String   |
                              | - titel: String  |
                              | - autor: String  |
                              +------------------+
                              | + getDetails()   |
                              +------------------+
```

---

## Beispiel 2: Zustandsdiagramm – Supportticket

**Anforderungstext:**
> "Ein Supportticket wird erstellt und ist dann 'offen'. Ein Mitarbeiter nimmt es an, dann ist es 'in Bearbeitung'. Der Mitarbeiter kann es als 'geloest' markieren. Der Kunde bestaetigt die Loesung, dann wird es 'geschlossen'. Wenn der Kunde die Loesung ablehnt, geht es zurueck zu 'in Bearbeitung'."

**Zustandsdiagramm:**

```
   (●)
    |
    | erstellen()
    v
+--------+   annehmen()    +--------------+
| Offen  |---------------->| In           |
+--------+                 | Bearbeitung  |
                           +--------------+
                                |       ^
                  loesen()      |       | ablehnen()
                                v       |
                           +----------+-+
                           | Geloest    |
                           +------------+
                                |
                  bestaetigen() |
                                v
                           +------------+
                           | Geschlossen|
                           +------------+
                                |
                                v
                               (◉)
```

**Transitionen:**

| Von | Nach | Ereignis | Bedingung |
|-----|------|---------|-----------|
| (Start) | Offen | erstellen() | – |
| Offen | In Bearbeitung | annehmen() | [Mitarbeiter verfuegbar] |
| In Bearbeitung | Geloest | loesen() | – |
| Geloest | Geschlossen | bestaetigen() | [Kunde zufrieden] |
| Geloest | In Bearbeitung | ablehnen() | [Loesung unzureichend] |

---

## Beispiel 3: Anwendungsfalldiagramm – Lernplattform

**Anforderungstext:**
> "Schueler koennen Kurse anzeigen und sich fuer Kurse anmelden. Fuer die Anmeldung muessen sie sich vorher einloggen. Optional koennen sie bei der Anmeldung einen Rabattcode eingeben. Lehrer koennen Kurse erstellen und Teilnehmerlisten einsehen. Der Administrator verwaltet die Benutzerkonten."

**Akteure und Use Cases:**

| Akteur | Use Cases |
|--------|----------|
| Schueler | Kurse anzeigen, Kursanmeldung, Login |
| Lehrer | Kurse erstellen, Teilnehmerliste einsehen |
| Administrator | Benutzer verwalten |

**Beziehungen:**
- "Kursanmeldung" <<include>> "Login" (Anmeldung erfordert immer Login)
- "Kursanmeldung" <<extend>> "Rabattcode eingeben" (optional)

**Diagramm:**

```
+--------------------------------------------------+
|              Lernplattform (System)              |
|                                                  |
|  (Kurse anzeigen)                                |
|                                                  |
|  (Kursanmeldung)----<<include>>--->(Login)       |
|       |                                          |
|       +---<<extend>>--->(Rabattcode eingeben)    |
|                                                  |
|  (Kurse erstellen)                               |
|                                                  |
|  (Teilnehmerliste einsehen)                      |
|                                                  |
|  (Benutzer verwalten)                            |
+--------------------------------------------------+
  |        |              |              |
Schueler Schueler      Lehrer     Administrator

Zuordnung:
- Schueler: Kurse anzeigen, Kursanmeldung
- Lehrer: Kurse erstellen, Teilnehmerliste einsehen
- Administrator: Benutzer verwalten
```

---

## Beispiel 4: Sequenzdiagramm – Artikelbestellung

**Szenario:** Ein Kunde bestellt einen Artikel im Online-Shop. Das System prueft den Lagerbestand, erstellt die Bestellung und sendet eine Bestaetigungsmail.

```
  Kunde      Webshop       Lager        Bestell-      Mail-
              (UI)        service       service       service
    |            |            |            |            |
    | 1: bestelle|            |            |            |
    |  (artikelId)|           |            |            |
    |----------->|            |            |            |
    |            | 2: pruefeBestand        |            |
    |            |   (artikelId)           |            |
    |            |----------->|            |            |
    |            |            |            |            |
    |            | 3: verfuegbar: true     |            |
    |            |<-----------|            |            |
    |            |            |            |            |
    |            | 4: erstelleBestellung   |            |
    |            |   (kunde, artikel)      |            |
    |            |------------------------>|            |
    |            |            |            |            |
    |            | 5: bestellNr: 1234      |            |
    |            |<------------------------|            |
    |            |            |            |            |
    |            | 6: sendeBestaetigung    |            |
    |            |   (kunde, bestellNr)    |            |
    |            |----------------------------------->  |
    |            |            |            |            |
    | 7: "Bestellung|         |            |            |
    |   bestaetigt" |         |            |            |
    |<-----------|            |            |            |
```

---

## Beispiel 5: Aktivitaetsdiagramm – Kundenregistrierung

**Szenario:** Ein Neukunde registriert sich auf einer Plattform. Das System prueft die Eingaben und sendet eine Bestaetigungsmail.

```
        (●) Start
         |
+--------v---------+
| Registrierungs-  |
| formular oeffnen |
+--------+---------+
         |
+--------v---------+
| Daten eingeben   |
| (Name, E-Mail,   |
|  Passwort)       |
+--------+---------+
         |
+--------v---------+
| Eingaben pruefen |
+--------+---------+
         |
      <◇>
     /    \
 [valide] [invalide]
    |         |
    |    +----v----------+
    |    | Fehlermeldung  |
    |    | anzeigen       |
    |    +----+-----------+
    |         |
    |         +------> (zurueck zu "Daten eingeben")
    |
+---v--------------+
| Konto erstellen  |
+---+--------------+
    |
    ═══ (Fork: Parallelisierung)
   / \
  v   v
+--------+  +------------------+
| E-Mail |  | Willkommensseite |
| senden |  | anzeigen         |
+--------+  +------------------+
  \   /
   ═══ (Join)
    |
   (◉) Ende
```
