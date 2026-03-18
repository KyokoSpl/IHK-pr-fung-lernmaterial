# Komplett: 3.4.19 – Bestehende Funktionen/Klassen erweitern

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.19
- **Thema:** Bestehende Funktionen/Klassen erweitern koennen

## Ziel

Du musst bestehenden Code (in allgemein verstaendlichem Pseudocode) lesen, verstehen und um neue Funktionalitaet erweitern koennen. In der Pruefung werden typischerweise Codeausschnitte gegeben, die du analysieren und durch Ergaenzungen oder Vererbung erweitern sollst.

## Themenkreise

| Nr. | Themenkreis | Schwerpunkt |
|-----|-------------|-------------|
| 1 | Code in allgemein verstaendlichem Pseudocode | Bestehenden Code lesen und erweitern |

---

## Grundlagen

### Bestehenden Code lesen und verstehen

**Vorgehensweise beim Lesen von Pseudocode:**
1. **Signatur analysieren:** Methodenname, Parameter, Rueckgabetyp
2. **Variablen identifizieren:** Was wird wo deklariert und verwendet?
3. **Kontrollfluss nachvollziehen:** Verzweigungen, Schleifen, Rueckgaben
4. **Trace durchfuehren:** Schrittweise Ausfuehrung mit konkreten Werten
5. **Zweck zusammenfassen:** Was macht die Methode insgesamt?

**Beispiel – Code analysieren:**

```
KLASSE Warenkorb
    PRIVAT artikel: Liste von Artikel

    METHODE gesamtpreis(): Zahl
        summe = 0
        FUER JEDES a IN artikel
            summe = summe + a.preis
        ENDE FUER
        RUECKGABE summe
    ENDE METHODE
ENDE KLASSE
```

Analyse:
- Klasse `Warenkorb` mit einer privaten Liste von Artikeln
- Methode `gesamtpreis()` summiert alle Artikelpreise auf
- Rueckgabe: Gesamtsumme als Zahl

### Erweiterung durch neue Methoden

Die einfachste Art, eine Klasse zu erweitern, ist das Hinzufuegen neuer Methoden:

```
KLASSE Warenkorb
    PRIVAT artikel: Liste von Artikel

    METHODE gesamtpreis(): Zahl
        summe = 0
        FUER JEDES a IN artikel
            summe = summe + a.preis
        ENDE FUER
        RUECKGABE summe
    ENDE METHODE

    // NEU: Methode hinzugefuegt
    METHODE anzahlArtikel(): Zahl
        RUECKGABE laenge(artikel)
    ENDE METHODE

    // NEU: Methode mit Logik
    METHODE gesamtpreisMitRabatt(rabattProzent: Zahl): Zahl
        gesamt = gesamtpreis()
        rabatt = gesamt * rabattProzent / 100
        RUECKGABE gesamt - rabatt
    ENDE METHODE

    // NEU: Artikel hinzufuegen mit Validierung
    METHODE hinzufuegen(neuerArtikel: Artikel): Wahrheitswert
        WENN neuerArtikel != NULL UND neuerArtikel.preis > 0 DANN
            artikel.hinzufuegen(neuerArtikel)
            RUECKGABE WAHR
        SONST
            RUECKGABE FALSCH
        ENDE WENN
    ENDE METHODE
ENDE KLASSE
```

### Erweiterung durch Vererbung

Wenn die bestehende Klasse nicht veraendert werden soll (z.B. fremde Bibliothek), wird Vererbung genutzt:

```
// Bestehende Klasse (nicht aendern!)
KLASSE Warenkorb
    GESCHUETZT artikel: Liste von Artikel

    METHODE gesamtpreis(): Zahl
        summe = 0
        FUER JEDES a IN artikel
            summe = summe + a.preis
        ENDE FUER
        RUECKGABE summe
    ENDE METHODE
ENDE KLASSE

// Erweiterte Klasse durch Vererbung
KLASSE PremiumWarenkorb ERBT VON Warenkorb
    PRIVAT rabattProzent: Zahl = 10

    METHODE gesamtpreis(): Zahl             // ueberschrieben
        basisPreis = super.gesamtpreis()    // Elternmethode aufrufen
        rabatt = basisPreis * rabattProzent / 100
        RUECKGABE basisPreis - rabatt
    ENDE METHODE

    METHODE getTeilsumme(kategorie: String): Zahl   // neue Methode
        summe = 0
        FUER JEDES a IN artikel
            WENN a.kategorie == kategorie DANN
                summe = summe + a.preis
            ENDE FUER
        RUECKGABE summe
    ENDE METHODE
ENDE KLASSE
```

### Erweiterung durch Interface-Implementierung

```
// Bestehendes Interface
INTERFACE Druckbar
    METHODE drucke()
ENDE INTERFACE

// Bestehende Klasse erweitern, um Interface zu implementieren
KLASSE Warenkorb IMPLEMENTIERT Druckbar
    PRIVAT artikel: Liste von Artikel

    METHODE gesamtpreis(): Zahl
        // ... wie bisher
    ENDE METHODE

    // NEU: Interface-Methode implementiert
    METHODE drucke()
        ausgabe("=== Warenkorb ===")
        FUER JEDES a IN artikel
            ausgabe(a.name + ": " + a.preis + " EUR")
        ENDE FUER
        ausgabe("Gesamt: " + gesamtpreis() + " EUR")
    ENDE METHODE
ENDE KLASSE
```

---

## Vertiefung

### Strategien fuer Code-Erweiterung

| Strategie | Wann einsetzen | Vorteil |
|-----------|---------------|---------|
| Neue Methode hinzufuegen | Einfache Erweiterung, Klasse darf geaendert werden | Einfachste Loesung |
| Vererbung | Klasse soll nicht veraendert werden (Open-Closed-Prinzip) | Bestehender Code bleibt unberuehrt |
| Interface implementieren | Neue Faehigkeit hinzufuegen | Lose Kopplung, polymorphe Nutzung |
| Komposition | "Hat-ein"-Beziehung statt "Ist-ein" | Flexibler als Vererbung |

### Open-Closed-Prinzip (OCP)

**Definition:** Klassen sollen **offen fuer Erweiterung**, aber **geschlossen fuer Modifikation** sein. Das bedeutet: Neue Funktionalitaet wird durch Erweiterung (Vererbung, Interfaces) hinzugefuegt, ohne bestehenden Code zu aendern.

```
// SCHLECHT: Bestehende Methode aendern
KLASSE Rechner
    METHODE berechne(typ: String, a: Zahl, b: Zahl): Zahl
        WENN typ == "addiere" DANN
            RUECKGABE a + b
        SONST WENN typ == "subtrahiere" DANN
            RUECKGABE a - b
        // Fuer neue Operation muss DIESE Methode geaendert werden!
        ENDE WENN
    ENDE METHODE
ENDE KLASSE

// GUT: Erweiterbar ohne Aenderung
INTERFACE Operation
    METHODE ausfuehren(a: Zahl, b: Zahl): Zahl
ENDE INTERFACE

KLASSE Addition IMPLEMENTIERT Operation
    METHODE ausfuehren(a: Zahl, b: Zahl): Zahl
        RUECKGABE a + b
    ENDE METHODE
ENDE KLASSE

// Neue Operation hinzufuegen: Nur neue Klasse erstellen!
KLASSE Multiplikation IMPLEMENTIERT Operation
    METHODE ausfuehren(a: Zahl, b: Zahl): Zahl
        RUECKGABE a * b
    ENDE METHODE
ENDE KLASSE
```

### Pseudocode-Konventionen fuer die Pruefung (Wiederholung)

| Element | Schreibweise |
|---------|-------------|
| Neue Klasse | `KLASSE Name` ... `ENDE KLASSE` |
| Vererbung | `KLASSE Kind ERBT VON Eltern` |
| Interface | `KLASSE X IMPLEMENTIERT Y` |
| Elternmethode aufrufen | `super.methode()` |
| Neues Objekt | `neues Klassenname(parameter)` |
| Methode ueberschreiben | Gleicher Name und gleiche Signatur in Kindklasse |

### Typische Pruefungsaspekte
- Gegebenen Pseudocode lesen und Zweck beschreiben
- Fehlende Methode ergaenzen (Lueckentext)
- Klasse durch Vererbung erweitern
- Bestehende Methode ueberschreiben
- Trace: Schrittweise Ausfuehrung mit konkreten Werten

### Haeufige Fehler
- `super`-Aufruf vergessen: Kindklasse ueberschreibt Methode komplett statt sie zu erweitern
- Zugriffsmodifikator falsch: `private` in Elternklasse → Kindklasse kann nicht darauf zugreifen (muss `protected` sein)
- Rueckgabetyp bei Ueberschreiben geaendert → muss gleich bleiben
- Bestehenden Code aendern statt erweitern → verletzt Open-Closed-Prinzip

---

## Uebungen

**Aufgabe 1:** Analysiere den folgenden Pseudocode. Was gibt die Methode zurueck, wenn die Liste `[4, 7, 2, 9, 1]` uebergeben wird?

```
METHODE mystery(zahlen: Liste): Zahl
    ergebnis = zahlen[0]
    FUER i VON 1 BIS laenge(zahlen) - 1
        WENN zahlen[i] < ergebnis DANN
            ergebnis = zahlen[i]
        ENDE WENN
    ENDE FUER
    RUECKGABE ergebnis
ENDE METHODE
```

**Aufgabe 2:** Gegeben ist die Klasse `Konto`. Erweitere sie um:
- Eine Methode `ueberweise(zielKonto: Konto, betrag: Zahl)`, die den Betrag vom eigenen Konto abbucht und dem Zielkonto gutschreibt.
- Fehlerbehandlung fuer unzureichendes Guthaben.

```
KLASSE Konto
    PRIVAT kontostand: Zahl
    OEFFENTLICH METHODE getKontostand(): Zahl
        RUECKGABE kontostand
    ENDE METHODE
    OEFFENTLICH METHODE einzahlen(betrag: Zahl)
        WENN betrag > 0 DANN
            kontostand = kontostand + betrag
        ENDE WENN
    ENDE METHODE
    OEFFENTLICH METHODE abheben(betrag: Zahl): Wahrheitswert
        WENN betrag > 0 UND betrag <= kontostand DANN
            kontostand = kontostand - betrag
            RUECKGABE WAHR
        SONST
            RUECKGABE FALSCH
        ENDE WENN
    ENDE METHODE
ENDE KLASSE
```

**Aufgabe 3:** Erstelle eine Kindklasse `Sparkonto` die von `Konto` erbt und:
- Ein Attribut `zinssatz` hat
- Eine Methode `zinsenBerechnen()`, die Zinsen auf den aktuellen Kontostand gutschreibt
- Die Methode `abheben()` ueberschreibt: Abheben nur moeglich, wenn Mindestguthaben von 100 EUR verbleibt

**Aufgabe 4:** Was bedeutet das Open-Closed-Prinzip? Erklaere es mit eigenen Worten und gib ein Beispiel.

**Aufgabe 5:** Fuehre einen Trace fuer folgenden Code durch. Was wird ausgegeben?

```
KLASSE Zaehler
    PRIVAT wert: Zahl = 0
    METHODE erhoehe()
        wert = wert + 1
    ENDE METHODE
    METHODE verdopple()
        wert = wert * 2
    ENDE METHODE
    METHODE getWert(): Zahl
        RUECKGABE wert
    ENDE METHODE
ENDE KLASSE

z = neuer Zaehler()
z.erhoehe()
z.erhoehe()
z.verdopple()
z.erhoehe()
ausgabe(z.getWert())
```

---
---

# Loesungen

## Aufgabe 1
Die Methode findet das **Minimum** in der Liste.

Trace mit `[4, 7, 2, 9, 1]`:
- ergebnis = 4
- i=1: 7 < 4? Nein → ergebnis = 4
- i=2: 2 < 4? Ja → ergebnis = 2
- i=3: 9 < 2? Nein → ergebnis = 2
- i=4: 1 < 2? Ja → ergebnis = 1

Rueckgabe: **1**

## Aufgabe 2

```
OEFFENTLICH METHODE ueberweise(zielKonto: Konto, betrag: Zahl): Wahrheitswert
    WENN betrag <= 0 DANN
        ausgabe("Ungueltiger Betrag!")
        RUECKGABE FALSCH
    ENDE WENN
    WENN abheben(betrag) DANN
        zielKonto.einzahlen(betrag)
        RUECKGABE WAHR
    SONST
        ausgabe("Nicht genuegend Guthaben!")
        RUECKGABE FALSCH
    ENDE WENN
ENDE METHODE
```

## Aufgabe 3

```
KLASSE Sparkonto ERBT VON Konto
    PRIVAT zinssatz: Zahl        // z.B. 2.5 fuer 2,5%

    KONSTRUKTOR Sparkonto(startGuthaben: Zahl, zins: Zahl)
        super.einzahlen(startGuthaben)
        zinssatz = zins
    ENDE KONSTRUKTOR

    METHODE zinsenBerechnen()
        zinsen = getKontostand() * zinssatz / 100
        einzahlen(zinsen)
    ENDE METHODE

    METHODE abheben(betrag: Zahl): Wahrheitswert       // ueberschrieben
        WENN getKontostand() - betrag >= 100 DANN
            RUECKGABE super.abheben(betrag)
        SONST
            ausgabe("Mindestguthaben von 100 EUR muss verbleiben!")
            RUECKGABE FALSCH
        ENDE WENN
    ENDE METHODE
ENDE KLASSE
```

## Aufgabe 4
Das Open-Closed-Prinzip besagt, dass Klassen **offen fuer Erweiterung** (neue Funktionalitaet kann hinzugefuegt werden) und **geschlossen fuer Modifikation** (bestehender Code muss nicht geaendert werden) sein sollen. Beispiel: Statt eine switch-Anweisung fuer neue Zahlungsarten zu erweitern, wird ein Interface `Zahlungsart` definiert. Neue Zahlungsarten (Kreditkarte, PayPal, Rechnung) implementieren das Interface, ohne bestehenden Code zu aendern.

## Aufgabe 5
Trace:
- `z = neuer Zaehler()` → wert = 0
- `z.erhoehe()` → wert = 0 + 1 = 1
- `z.erhoehe()` → wert = 1 + 1 = 2
- `z.verdopple()` → wert = 2 * 2 = 4
- `z.erhoehe()` → wert = 4 + 1 = 5

Ausgabe: **5**
