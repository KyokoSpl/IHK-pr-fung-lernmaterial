# Vertiefung und Uebungen: 2.2.02 – Algorithmen formulieren und Programme entwickeln

## Vertiefung

### Vergleich UML-Diagrammtypen

| Diagramm | Zeigt | Statisch/Dynamisch | Typischer Einsatz |
|---|---|---|---|
| Use-Case | Funktionalitaeten + Akteure | Statisch | Anforderungsanalyse |
| Klassendiagramm | Klassen, Attribute, Beziehungen | Statisch | Softwarearchitektur |
| Aktivitaetsdiagramm | Ablauf/Prozess | Dynamisch | Algorithmen, Workflows |
| Sequenzdiagramm | Nachrichtenaustausch ueber Zeit | Dynamisch | Schnittstellen, APIs |
| Zustandsdiagramm | Zustandswechsel eines Objekts | Dynamisch | Automaten, Protokolle |

### Beziehungen im Klassendiagramm

| Beziehung | Symbol | Bedeutung | Beispiel |
|---|---|---|---|
| Assoziation | ——— | Kennt-Beziehung | Kunde kennt Auftrag |
| Aggregation | ◇——— | Teil-Ganzes (lose) | Abteilung hat Mitarbeiter |
| Komposition | ◆——— | Teil-Ganzes (stark) | Rechnung hat Positionen |
| Vererbung | ——▷ | Ist-ein-Beziehung | PKW ist ein Fahrzeug |
| Implementierung | --▷ | Realisiert Interface | Klasse implementiert Interface |

### Haeufige Fehler in Pruefungen

| Fehler | Richtig |
|---|---|
| Use-Case zeigt Programmablauf | Use-Case zeigt WAS, nicht WIE |
| Klassendiagramm ohne Sichtbarkeit | +/-/# immer angeben |
| Aktivitaetsdiagramm ohne Start/Ende | Immer Start- und Endknoten |
| Pseudocode syntaxspezifisch | Allgemein verstaendlich schreiben |

---

## Uebungen

### Aufgabe 1: Pseudocode schreiben
Schreibe Pseudocode fuer folgende Aufgabe: Ein Programm liest Noten (1-6) ein, bis der Wert 0 eingegeben wird. Am Ende wird der Durchschnitt ausgegeben.

---
---

**Loesung Aufgabe 1:**
```
summe = 0
anzahl = 0
EINGABE: note
SOLANGE note != 0 TUE
    WENN note >= 1 UND note <= 6 DANN
        summe = summe + note
        anzahl = anzahl + 1
    SONST
        AUSGABE: "Ungueltige Note!"
    ENDE WENN
    EINGABE: note
ENDE SOLANGE
WENN anzahl > 0 DANN
    durchschnitt = summe / anzahl
    AUSGABE: "Durchschnitt: " + durchschnitt
SONST
    AUSGABE: "Keine Noten eingegeben."
ENDE WENN
```

---

### Aufgabe 2: Klassendiagramm erstellen
Erstelle ein UML-Klassendiagramm fuer ein einfaches Bibliothekssystem mit:
- Klasse „Buch" (Titel, Autor, ISBN, ausgeliehen)
- Klasse „Mitglied" (Name, Mitgliedsnummer)
- Ein Mitglied kann mehrere Buecher ausleihen

---
---

**Loesung Aufgabe 2:**
```
+-----------------------------+          +-------------------------+
|         Mitglied            |          |         Buch            |
+-----------------------------+          +-------------------------+
| - name: String              |          | - titel: String         |
| - mitgliedsnummer: int      |          | - autor: String         |
+-----------------------------+          | - isbn: String          |
| + ausleihen(b: Buch): void | 1    0..*| - ausgeliehen: boolean  |
| + zurueckgeben(b: Buch): void|--------| +-------------------------+
| + getName(): String         |  leiht  | + getTitel(): String    |
+-----------------------------+   aus   | + istVerfuegbar(): bool  |
                                        +-------------------------+
```
Kardinalitaet: 1 Mitglied leiht 0..* Buecher aus. Assoziation "leiht aus".

---

### Aufgabe 3: Softwareergonomie beurteilen
Ein Formular zur Kundendatenerfassung hat folgende Probleme:
- Pflichtfelder sind nicht gekennzeichnet
- Nach dem Absenden erscheint keine Bestaetigung
- Tab-Reihenfolge springt zufaellig zwischen Feldern
- Alle Fehlermeldungen erscheinen als rotes Ausrufezeichen ohne Text

Ordne jedes Problem einem Ergonomie-Grundsatz zu und nenne eine Loesung.

---
---

**Loesung Aufgabe 3:**
1. **Pflichtfelder nicht gekennzeichnet** → Selbstbeschreibungsfaehigkeit. Loesung: Pflichtfelder mit * markieren und Legende "* = Pflichtfeld" anzeigen.
2. **Keine Bestaetigung** → Erwartungskonformitaet. Loesung: Erfolgsmeldung "Daten gespeichert" nach Absenden anzeigen.
3. **Tab-Reihenfolge zufaellig** → Steuerbarkeit. Loesung: Tab-Index logisch setzen (oben links → unten rechts), Feld-Reihenfolge entspricht Leserichtung.
4. **Fehlermeldungen ohne Text** → Fehlertoleranz. Loesung: Textuelle Fehlermeldung neben jedem Feld ("Bitte geben Sie eine gueltige E-Mail ein"), nicht nur Icon.
