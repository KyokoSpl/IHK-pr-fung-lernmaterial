# 3.3.02 – Uebungen: Planen mit geeigneten Modellen

## Aufgabe 1: ERM erstellen und transformieren

Ein Fitnessstudio verwaltet folgende Informationen:
- **Mitglieder** haben eine MitgliedsNr, Name, Geburtsdatum und Tarifart
- **Kurse** haben eine KursNr, Bezeichnung und maximale Teilnehmerzahl
- **Trainer** haben eine TrainerNr, Name und Qualifikation
- Ein Mitglied kann an mehreren Kursen teilnehmen, ein Kurs hat mehrere Mitglieder
- Jeder Kurs wird von genau einem Trainer geleitet, ein Trainer kann mehrere Kurse leiten

a) Zeichne das ERM mit Kardinalitaeten.
b) Ueberführe das ERM in ein relationales Datenbankmodell.
c) Welche Zwischentabelle(n) entstehen?

---

## Aufgabe 2: Klassendiagramm erstellen

Erstelle ein UML-Klassendiagramm fuer ein Fahrzeugvermietungs-System:
- Es gibt eine Klasse `Fahrzeug` mit Attributen: kennzeichen, marke, baujahr, tagesPreis
- Unterklassen: `PKW` (sitzplaetze), `LKW` (ladekapazitaet), `Motorrad` (hubraum)
- Eine Klasse `Kunde` mit: kundenNr, name, fuehrerscheinKlasse
- Eine Klasse `Mietvertrag` mit: vertragNr, startDatum, endDatum, gesamtPreis
- Ein Kunde kann mehrere Mietvertraege haben
- Ein Mietvertrag bezieht sich auf genau ein Fahrzeug

Beachte: Sichtbarkeit, Datentypen, Multiplizitaeten und Beziehungstypen angeben.

---

## Aufgabe 3: Diagramm-Typ zuordnen

Welches UML-Diagramm wuerdest du verwenden? Begruende kurz.

| Nr. | Situation | Diagramm? |
|-----|-----------|-----------|
| a) | Du willst zeigen, welche Zustaende eine Bestellung durchlaeuft | |
| b) | Du willst die Datenbankstruktur einer Anwendung planen | |
| c) | Du willst den Ablauf eines Reklamationsprozesses darstellen | |
| d) | Du willst zeigen, welche Akteure das System nutzen und wofuer | |
| e) | Du willst die Kommunikation zwischen Browser, Server und DB zeigen | |
| f) | Du willst die Vererbungshierarchie deiner Klassen darstellen | |

---

## Aufgabe 4: Sequenzdiagramm lesen

Gegeben ist folgendes Sequenzdiagramm. Beantworte die Fragen:

```
  Benutzer      GUI         Controller      Service       Repository
     |           |              |              |              |
     |--klick()->|              |              |              |
     |           |--request()-->|              |              |
     |           |              |--validate()  |              |
     |           |              |--process()--->|              |
     |           |              |              |--save()------>|
     |           |              |              |<--ok----------|
     |           |              |<--result------|              |
     |           |<--response---|              |              |
     |<--anzeige-|              |              |              |
```

a) Wie viele Objekte (Lebenslinien) sind beteiligt?
b) Welches Objekt speichert die Daten?
c) In welcher Reihenfolge werden die Nachrichten gesendet?
d) Welches Architekturmuster laesst sich erkennen?

---

## Aufgabe 5: ERM-Fehler finden

Finde die Fehler im folgenden relationalen Modell (es wurde aus einem ERM transformiert):

```
Szenario: Schueler besuchen Klassen. Lehrer unterrichten Faecher.
          Ein Lehrer unterrichtet in mehreren Klassen.

Schueler (Name, Vorname, Klasse, Klassenlehrer)
Lehrer (Name, Fach1, Fach2, Fach3)
Klasse (Bezeichnung, Raum)
```

---

## Aufgabe 6: Zustandsdiagramm erstellen (FI AE)

Erstelle ein Zustandsdiagramm fuer ein Ticket in einem Helpdesk-System:
- Moegliche Zustaende: Neu, Zugewiesen, In Bearbeitung, Wartend, Geloest, Geschlossen
- Transitionen:
  - Neu → Zugewiesen (wenn Mitarbeiter zugewiesen wird)
  - Zugewiesen → In Bearbeitung (wenn Mitarbeiter beginnt)
  - In Bearbeitung → Wartend (wenn auf Kundenrueckmeldung gewartet wird)
  - Wartend → In Bearbeitung (wenn Kunde antwortet)
  - In Bearbeitung → Geloest (wenn Loesung gefunden)
  - Geloest → Geschlossen (wenn Kunde bestaetigt)
  - Geloest → In Bearbeitung (wenn Kunde nicht zufrieden)

---
---

## Loesung Aufgabe 1

### a) ERM

```
+----------+          +------------+           +----------+
| Mitglied |---n--< nimmt teil >---m---| Kurs     |
+----------+         +------------+            +----------+
| MitglNr  |                                   | KursNr   |
| Name     |                                   | Bezeichn.|
| GebDat   |                                   | MaxTeiln.|
| Tarif    |                                   +----------+
+----------+                                       |
                                                   n
                                                   |
                                            < wird geleitet >
                                                   |
                                                   1
                                               +----------+
                                               | Trainer  |
                                               +----------+
                                               | TrainerNr|
                                               | Name     |
                                               | Qualifik.|
                                               +----------+
```

### b) Relationales Modell

```
Trainer (TrainerNr PK, Name, Qualifikation)
Mitglied (MitgliedNr PK, Name, Geburtsdatum, Tarif)
Kurs (KursNr PK, Bezeichnung, MaxTeilnehmer, TrainerNr FK→Trainer)
Teilnahme (MitgliedNr FK→Mitglied, KursNr FK→Kurs)
           PK = (MitgliedNr, KursNr)
```

### c) Zwischentabelle
Die Tabelle **Teilnahme** entsteht als Zwischentabelle fuer die n:m-Beziehung zwischen Mitglied und Kurs. Die 1:n-Beziehung zwischen Trainer und Kurs wird durch den Fremdschluessel `TrainerNr` in der Tabelle `Kurs` abgebildet (keine Zwischentabelle noetig).

---

## Loesung Aufgabe 2

```
+---------------------+
|      Fahrzeug       |
+---------------------+
| - kennzeichen: String|
| - marke: String     |
| - baujahr: int      |
| - tagesPreis: double|
+---------------------+
| + berechneKosten(tage: int): double |
+---------------------+
        △
       /|\
      / | \
+--------+ +--------+ +----------+
|  PKW   | |  LKW   | | Motorrad |
+--------+ +--------+ +----------+
|- sitz-  ||- lade-  ||- hubraum:|
|  plaetze||  kapaz. ||  int     |
|  : int  ||  : double|          |
+--------+ +--------+ +----------+

+---------------------+        +---------------------+
|       Kunde         | 1    * |    Mietvertrag      |
+---------------------+◇------>+---------------------+
| - kundenNr: int     |       | - vertragNr: int    |
| - name: String      |       | - startDatum: Date  |
| - fuehrerschein-    |       | - endDatum: Date    |
|   Klasse: String    |       | - gesamtPreis: double|
+---------------------+       +---------------------+
| + mieten(): void    |       | + berechne(): double|
+---------------------+       +---------------------+
                                       | 1
                                       |
                                       | 1
                               +---------------------+
                               |      Fahrzeug       |
                               +---------------------+
```

---

## Loesung Aufgabe 3

| Nr. | Situation | Diagramm | Begruendung |
|-----|-----------|----------|-------------|
| a) | Zustaende einer Bestellung | **Zustandsdiagramm** | Zeigt Zustaende und Uebergaenge eines Objekts |
| b) | Datenbankstruktur | **ERM / Relationales Modell** | Zeigt Entitaeten, Attribute, Beziehungen |
| c) | Reklamationsprozess | **Aktivitaetsdiagramm** | Zeigt Ablauf mit Entscheidungen und Parallelitaet |
| d) | Akteure und Funktionen | **Anwendungsfalldiagramm** | Zeigt Akteure, Use Cases und Systemgrenzen |
| e) | Kommunikation Browser-Server-DB | **Sequenzdiagramm** | Zeigt zeitlichen Nachrichtenaustausch |
| f) | Vererbungshierarchie | **Klassendiagramm** | Zeigt Klassen und Vererbungsbeziehungen |

---

## Loesung Aufgabe 4

a) **5 Objekte**: Benutzer, GUI, Controller, Service, Repository
b) **Repository** speichert die Daten (save()-Aufruf)
c) Reihenfolge: klick() → request() → validate() → process() → save() → ok → result → response → anzeige
d) **Schichtenarchitektur** (Layered Architecture): GUI → Controller → Service → Repository. Entspricht dem typischen MVC/Drei-Schichten-Modell.

---

## Loesung Aufgabe 5

**Fehler im Modell**:

1. **Kein Primaerschluessel** bei Schueler – es fehlt z.B. eine SchuelerNr
2. **Kein Primaerschluessel** bei Lehrer – es fehlt z.B. eine LehrerNr
3. **Wiederholungsgruppe bei Lehrer**: Fach1, Fach2, Fach3 verletzt die **1. Normalform** → eigene Tabelle `Fach` und Zwischentabelle `LehrerFach`
4. **Klassenlehrer in Schueler**: Transitive Abhaengigkeit → Klassenlehrer gehoert zur Klasse, nicht zum Schueler (verletzt 3NF)
5. **Beziehung Lehrer-Klasse fehlt**: Es gibt keine Zuordnungstabelle fuer "Lehrer unterrichtet in Klasse"

**Korrektes Modell**:
```
Schueler (SchuelerNr PK, Name, Vorname, KlasseBezeichnung FK)
Klasse (Bezeichnung PK, Raum, KlassenlehrerNr FK→Lehrer)
Lehrer (LehrerNr PK, Name)
Fach (FachNr PK, Bezeichnung)
LehrerFach (LehrerNr FK, FachNr FK)  PK=(LehrerNr, FachNr)
Unterricht (LehrerNr FK, KlasseBezeichnung FK, FachNr FK)
```

---

## Loesung Aufgabe 6

```
    ●
    |  erstellt
    v
+--------+  Mitarbeiter zugewiesen  +------------+
|  Neu   |------------------------->| Zugewiesen |
+--------+                          +------------+
                                          |
                                          | Mitarbeiter beginnt
                                          v
                   Kunde antwortet  +--------------+
               +<-------------------| In Bearbeitg |<---------+
               |                    +--------------+           |
               v                      |          |             |
          +----------+    Loesung     |          | Kunde nicht |
          | Wartend  |    gefunden    |          | zufrieden   |
          +----------+               v          |             |
               |                +---------+     |             |
               | Kunde          | Geloest |-----+             |
               | antwortet      +---------+                   |
               |                     |                        |
               +---->In Bearbeitg    | Kunde bestaetigt       |
                                     v                        |
                              +------------+                  |
                              | Geschlossen|                  |
                              +------------+                  |
                                     |
                                     v
                                     ◉
```
