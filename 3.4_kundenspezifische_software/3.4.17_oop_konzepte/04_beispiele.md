# Beispiele: 3.4.17 – OOP-Methodenkonzepte anwenden

## Kapselung

**Beispiel 1:** Ein Onlineshop verwaltet Produkte. Der Lagerbestand darf nie negativ werden.

```
KLASSE Produkt
    PRIVAT name: String
    PRIVAT preis: Zahl
    PRIVAT lagerbestand: Zahl

    KONSTRUKTOR Produkt(name: String, preis: Zahl, bestand: Zahl)
        DIESER.name = name
        DIESER.preis = preis
        DIESER.lagerbestand = bestand
    ENDE KONSTRUKTOR

    OEFFENTLICH METHODE bestelle(menge: Zahl): Wahrheitswert
        WENN menge <= lagerbestand UND menge > 0 DANN
            lagerbestand = lagerbestand - menge
            RUECKGABE WAHR
        SONST
            ausgabe("Nicht genuegend auf Lager!")
            RUECKGABE FALSCH
        ENDE WENN
    ENDE METHODE

    OEFFENTLICH METHODE getLagerbestand(): Zahl
        RUECKGABE lagerbestand
    ENDE METHODE
ENDE KLASSE

// Verwendung:
laptop = neues Produkt("Laptop", 899.99, 10)
laptop.bestelle(3)         // OK, Bestand jetzt 7
laptop.bestelle(15)        // "Nicht genuegend auf Lager!"
```

→ Kapselung schuetzt den Lagerbestand vor ungueltigen Werten.

---

## Vererbung

**Beispiel 2:** Ein Unternehmen verwaltet verschiedene Mitarbeitertypen.

```
KLASSE Mitarbeiter
    GESCHUETZT name: String
    GESCHUETZT personalnummer: Zahl
    GESCHUETZT grundgehalt: Zahl

    METHODE berechneGehalt(): Zahl
        RUECKGABE grundgehalt
    ENDE METHODE

    METHODE info(): String
        RUECKGABE personalnummer + ": " + name
    ENDE METHODE
ENDE KLASSE

KLASSE Entwickler ERBT VON Mitarbeiter
    PRIVAT programmiersprache: String
    PRIVAT projektbonus: Zahl

    METHODE berechneGehalt(): Zahl       // ueberschrieben
        RUECKGABE grundgehalt + projektbonus
    ENDE METHODE
ENDE KLASSE

KLASSE Vertriebler ERBT VON Mitarbeiter
    PRIVAT provision: Zahl               // Prozentsatz
    PRIVAT umsatz: Zahl

    METHODE berechneGehalt(): Zahl       // ueberschrieben
        RUECKGABE grundgehalt + (umsatz * provision / 100)
    ENDE METHODE
ENDE KLASSE

// Polymorphe Verwendung:
mitarbeiter: Liste von Mitarbeiter = [
    neuer Entwickler("Anna", 1001, 4000, "Java", 500),
    neuer Vertriebler("Ben", 1002, 3000, 5, 20000)
]

FUER JEDES m IN mitarbeiter
    ausgabe(m.info() + " → Gehalt: " + m.berechneGehalt())
ENDE FUER
// Ausgabe:
// 1001: Anna → Gehalt: 4500
// 1002: Ben → Gehalt: 4000
```

→ Vererbung + Polymorphie: Jeder Mitarbeiter berechnet sein Gehalt unterschiedlich, aber alle werden ueber dieselbe Schnittstelle angesprochen.

---

## Interfaces

**Beispiel 3:** Ein Dokumentenmanagementsystem soll verschiedene Dokumenttypen exportieren koennen.

```
INTERFACE Exportierbar
    METHODE exportAlsPDF(): Datei
    METHODE exportAlsCSV(): Datei
ENDE INTERFACE

KLASSE Rechnung IMPLEMENTIERT Exportierbar
    ATTRIBUT rechnungsnummer: String
    ATTRIBUT positionen: Liste

    METHODE exportAlsPDF(): Datei
        // PDF mit Rechnungsdetails erzeugen
        RUECKGABE neuePDFDatei(rechnungsnummer, positionen)
    ENDE METHODE

    METHODE exportAlsCSV(): Datei
        // CSV mit Positionen erzeugen
        zeilen = ""
        FUER JEDES p IN positionen
            zeilen = zeilen + p.name + ";" + p.preis + "\n"
        ENDE FUER
        RUECKGABE neueCSVDatei(zeilen)
    ENDE METHODE
ENDE KLASSE

KLASSE Bericht IMPLEMENTIERT Exportierbar
    ATTRIBUT titel: String
    ATTRIBUT inhalt: String

    METHODE exportAlsPDF(): Datei
        RUECKGABE neuePDFDatei(titel, inhalt)
    ENDE METHODE

    METHODE exportAlsCSV(): Datei
        RUECKGABE neueCSVDatei(titel + ";" + inhalt)
    ENDE METHODE
ENDE KLASSE

// Verwendung mit Interface-Typ:
dokumente: Liste von Exportierbar = [neue Rechnung(...), neuer Bericht(...)]
FUER JEDES dok IN dokumente
    dok.exportAlsPDF()       // Jedes Dokument kann als PDF exportiert werden
ENDE FUER
```

→ Das Interface `Exportierbar` stellt sicher, dass alle Dokumenttypen die gleichen Export-Methoden besitzen.

---

## Fehlerbehandlung

**Beispiel 4:** Ein Taschenrechner-Programm soll Division durch Null und ungueltige Eingaben abfangen.

```
KLASSE Taschenrechner
    METHODE dividiere(a: Zahl, b: Zahl): Zahl
        WENN b == 0 DANN
            WIRF neuen Fehler("Division durch Null!")
        ENDE WENN
        RUECKGABE a / b
    ENDE METHODE
ENDE KLASSE

// Verwendung mit Fehlerbehandlung:
rechner = neuer Taschenrechner()

VERSUCHE
    ergebnis = rechner.dividiere(10, 0)
    ausgabe("Ergebnis: " + ergebnis)
FANGE FehlerTyp Rechenfehler als fehler
    ausgabe("Fehler: " + fehler.nachricht)     // "Fehler: Division durch Null!"
ABSCHLIESSEND
    ausgabe("Berechnung abgeschlossen.")
ENDE VERSUCHE
```

→ Ohne try-catch wuerde das Programm abstuerzen. Mit try-catch wird der Fehler abgefangen und das Programm laeuft weiter.

---

## Polymorphie – Ueberladen

**Beispiel 5:** Eine Klasse `Logger` bietet verschiedene Log-Methoden an.

```
KLASSE Logger
    METHODE log(nachricht: String)
        ausgabe("[INFO] " + nachricht)
    ENDE METHODE

    METHODE log(nachricht: String, level: String)       // ueberladene Methode
        ausgabe("[" + level + "] " + nachricht)
    ENDE METHODE

    METHODE log(nachricht: String, level: String, zeitstempel: Datum)
        ausgabe("[" + level + " " + zeitstempel + "] " + nachricht)
    ENDE METHODE
ENDE KLASSE

// Verwendung:
logger = neuer Logger()
logger.log("Server gestartet")                          // [INFO] Server gestartet
logger.log("Verbindung fehlgeschlagen", "ERROR")        // [ERROR] Verbindung fehlgeschlagen
logger.log("Backup erstellt", "INFO", aktuelleDatum())  // [INFO 2026-03-17] Backup erstellt
```

→ Gleicher Methodenname, aber verschiedene Parameteranzahl. Der Compiler waehlt die passende Methode anhand der Parameter.

---

## Gesamtbeispiel: Tierverwaltung (alle Konzepte)

```
INTERFACE Impfbar
    METHODE impfen(impfstoff: String)
ENDE INTERFACE

KLASSE Tier
    GESCHUETZT name: String
    GESCHUETZT alter: Zahl

    METHODE laut(): String
        RUECKGABE "..."
    ENDE METHODE
ENDE KLASSE

KLASSE Hund ERBT VON Tier IMPLEMENTIERT Impfbar
    PRIVAT rasse: String

    METHODE laut(): String                    // Overriding (Polymorphie)
        RUECKGABE "Wau!"
    ENDE METHODE

    METHODE impfen(impfstoff: String)         // Interface-Implementierung
        ausgabe(name + " erhaelt Impfung: " + impfstoff)
    ENDE METHODE
ENDE KLASSE

// Verwendung:
VERSUCHE
    hund = neuer Hund("Bello", 3, "Labrador")
    ausgabe(hund.laut())                     // Polymorphie: "Wau!"
    hund.impfen("Tollwut")                   // Interface: "Bello erhaelt Impfung: Tollwut"
FANGE FehlerTyp Exception als e
    ausgabe("Fehler: " + e.nachricht)        // Fehlerbehandlung
ENDE VERSUCHE
```
