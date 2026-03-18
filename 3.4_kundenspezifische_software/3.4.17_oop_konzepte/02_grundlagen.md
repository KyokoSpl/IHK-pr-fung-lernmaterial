# Grundlagen: 3.4.17 – OOP-Methodenkonzepte anwenden

## Allgemeine Fehlerbehandlung

**Definition:** Fehlerbehandlung (Exception Handling) ist ein Mechanismus, der Laufzeitfehler abfaengt und kontrolliert verarbeitet, damit das Programm nicht unkontrolliert abstuerzt.

**Kernaussagen:**
- **try:** Codeblock, in dem Fehler auftreten koennen
- **catch:** Codeblock, der den Fehler auffaengt und behandelt
- **finally:** Codeblock, der immer ausgefuehrt wird (z.B. Ressourcen freigeben)
- **throw:** Explizites Ausloesen einer Exception

**Pseudocode:**

```
VERSUCHE
    datei = oeffne("daten.csv")
    inhalt = datei.lese()
FANGE FehlerTyp DateiNichtGefunden
    ausgabe("Datei wurde nicht gefunden!")
FANGE FehlerTyp Lesefehler
    ausgabe("Datei konnte nicht gelesen werden!")
ABSCHLIESSEND
    WENN datei != NULL DANN
        datei.schliesse()
    ENDE WENN
ENDE VERSUCHE
```

**Wichtige Begriffe:**
- **Exception** – Ausnahmefehler, der zur Laufzeit auftritt
- **Checked Exception** – muss behandelt werden (z.B. Dateizugriff)
- **Unchecked Exception** – Programmierfehler (z.B. NullPointer, Division durch 0)
- **Stack Trace** – Fehlermeldung mit Aufrufkette, zeigt wo der Fehler auftrat

**Erklaerung:** Ohne Fehlerbehandlung stuerzt ein Programm bei Laufzeitfehlern ab. Mit try-catch wird der Fehler abgefangen und eine sinnvolle Reaktion ausgeloest (Fehlermeldung, Wiederholung, Standardwert).

---

## Interfaces

**Definition:** Ein Interface (Schnittstelle) definiert eine Menge von Methodensignaturen, die eine implementierende Klasse umsetzen MUSS. Ein Interface enthaelt keinen eigenen Code (keine Implementierung).

**Pseudocode:**

```
INTERFACE Druckbar
    METHODE drucke(): nichts
ENDE INTERFACE

KLASSE Rechnung IMPLEMENTIERT Druckbar
    ATTRIBUT betrag: Zahl

    METHODE drucke()
        ausgabe("Rechnung: " + betrag + " EUR")
    ENDE METHODE
ENDE KLASSE

KLASSE Lieferschein IMPLEMENTIERT Druckbar
    ATTRIBUT artikelListe: Liste

    METHODE drucke()
        ausgabe("Lieferschein mit " + laenge(artikelListe) + " Artikeln")
    ENDE METHODE
ENDE KLASSE
```

**Interface vs. abstrakte Klasse:**

| Kriterium | Interface | Abstrakte Klasse |
|-----------|-----------|-----------------|
| Implementierung | Keine (nur Signaturen) | Kann Methoden mit Code enthalten |
| Mehrfachvererbung | Ja (Klasse kann mehrere Interfaces implementieren) | Nein (nur eine Elternklasse) |
| Attribute | Keine (nur Konstanten) | Ja |
| Konstruktor | Nein | Ja |
| Einsatz | Vertrag/Schnittstelle definieren | Gemeinsame Basis mit Teilimplementierung |

**UML-Notation:**

```
+-------------------+       +-------------------+
| <<interface>>     |       | <<abstract>>      |
| Druckbar          |       | Dokument          |
|-------------------|       |-------------------|
|                   |       | # titel: String   |
|-------------------|       |-------------------|
| + drucke(): void  |       | + drucke(): void  |  (abstrakt)
+-------------------+       | + speichere()     |  (implementiert)
        ^                   +-------------------+
        |                            ^
  implementiert                   erbt von
        |                            |
+-------------------+       +-------------------+
| Rechnung          |       | Rechnung          |
|-------------------|       |-------------------|
| + drucke(): void  |       | + drucke(): void  |
+-------------------+       +-------------------+
```

**Wichtige Begriffe:**
- **Schnittstellenvertrag** – Interface legt fest, was implementiert werden muss
- **Lose Kopplung** – Client-Code arbeitet nur gegen das Interface, nicht gegen die konkrete Klasse
- **Dependency Injection** – Abhaengigkeiten werden als Interfaces uebergeben

---

## Kapselung

**Definition:** Kapselung (Encapsulation) bedeutet, dass die internen Daten eines Objekts vor direktem Zugriff von aussen geschuetzt werden. Der Zugriff erfolgt ausschliesslich ueber definierte Methoden (Getter/Setter).

**Zugriffsmodifikatoren:**

| Modifikator | Sichtbarkeit | UML-Symbol |
|-------------|-------------|------------|
| public | Ueberall sichtbar | + |
| private | Nur innerhalb der eigenen Klasse | - |
| protected | Eigene Klasse + Unterklassen | # |
| package/internal | Innerhalb des Pakets/Moduls | ~ |

**Pseudocode:**

```
KLASSE Konto
    PRIVAT kontostand: Zahl

    OEFFENTLICH METHODE getKontostand(): Zahl
        RUECKGABE kontostand
    ENDE METHODE

    OEFFENTLICH METHODE einzahlen(betrag: Zahl)
        WENN betrag > 0 DANN
            kontostand = kontostand + betrag
        SONST
            ausgabe("Ungültiger Betrag!")
        ENDE WENN
    ENDE METHODE

    OEFFENTLICH METHODE abheben(betrag: Zahl): Wahrheitswert
        WENN betrag > 0 UND betrag <= kontostand DANN
            kontostand = kontostand - betrag
            RUECKGABE WAHR
        SONST
            ausgabe("Nicht genuegend Guthaben!")
            RUECKGABE FALSCH
        ENDE WENN
    ENDE METHODE
ENDE KLASSE
```

**UML-Darstellung:**

```
+------------------------------+
|          Konto               |
|------------------------------|
| - kontostand: double         |
|------------------------------|
| + getKontostand(): double    |
| + einzahlen(betrag: double)  |
| + abheben(betrag: double)    |
+------------------------------+
```

**Erklaerung:** Durch Kapselung wird sichergestellt, dass der Kontostand nicht direkt auf einen negativen Wert gesetzt werden kann. Nur ueber die Methoden einzahlen() und abheben() – die eine Validierung durchfuehren – kann der Wert veraendert werden.

---

## Polymorphie

**Definition:** Polymorphie (Vielgestaltigkeit) bedeutet, dass Objekte verschiedener Klassen ueber eine gemeinsame Schnittstelle angesprochen werden koennen und sich unterschiedlich verhalten.

**Zwei Arten:**

| Art | Name | Beschreibung | Beispiel |
|-----|------|-------------|----------|
| Ueberladen | Overloading | Gleicher Methodenname, verschiedene Parameter | `berechne(a)` und `berechne(a, b)` |
| Ueberschreiben | Overriding | Kindklasse ueberschreibt Methode der Elternklasse | `Hund.sprechen()` statt `Tier.sprechen()` |

**Pseudocode – Ueberschreiben (Overriding):**

```
KLASSE Tier
    METHODE sprechen(): String
        RUECKGABE "..."
    ENDE METHODE
ENDE KLASSE

KLASSE Hund ERBT VON Tier
    METHODE sprechen(): String       // ueberschreibt Tier.sprechen()
        RUECKGABE "Wau!"
    ENDE METHODE
ENDE KLASSE

KLASSE Katze ERBT VON Tier
    METHODE sprechen(): String       // ueberschreibt Tier.sprechen()
        RUECKGABE "Miau!"
    ENDE METHODE
ENDE KLASSE

// Polymorphe Verwendung:
tiere: Liste von Tier = [neuer Hund(), neue Katze()]
FUER JEDES t IN tiere
    ausgabe(t.sprechen())            // "Wau!", "Miau!"
ENDE FUER
```

**Pseudocode – Ueberladen (Overloading):**

```
KLASSE Rechner
    METHODE addiere(a: Zahl, b: Zahl): Zahl
        RUECKGABE a + b
    ENDE METHODE

    METHODE addiere(a: Zahl, b: Zahl, c: Zahl): Zahl   // ueberladene Methode
        RUECKGABE a + b + c
    ENDE METHODE
ENDE KLASSE
```

---

## Vererbung

**Definition:** Vererbung (Inheritance) ermoeglicht es, dass eine Klasse (Kindklasse/Unterklasse) Attribute und Methoden einer anderen Klasse (Elternklasse/Oberklasse) uebernimmt und erweitert.

**Pseudocode:**

```
KLASSE Fahrzeug                         // Elternklasse
    GESCHUETZT marke: String
    GESCHUETZT baujahr: Zahl

    METHODE beschreibung(): String
        RUECKGABE marke + " (" + baujahr + ")"
    ENDE METHODE
ENDE KLASSE

KLASSE PKW ERBT VON Fahrzeug           // Kindklasse
    PRIVAT anzahlSitze: Zahl

    METHODE beschreibung(): String      // ueberschrieben
        RUECKGABE marke + " (" + baujahr + "), " + anzahlSitze + " Sitze"
    ENDE METHODE
ENDE KLASSE

KLASSE LKW ERBT VON Fahrzeug           // Kindklasse
    PRIVAT ladekapazitaet: Zahl         // in Tonnen

    METHODE beschreibung(): String      // ueberschrieben
        RUECKGABE marke + " (" + baujahr + "), " + ladekapazitaet + " t"
    ENDE METHODE
ENDE KLASSE
```

**UML-Darstellung:**

```
+----------------------------+
|       Fahrzeug             |
|----------------------------|
| # marke: String            |
| # baujahr: int             |
|----------------------------|
| + beschreibung(): String   |
+----------------------------+
         ^            ^
         |            |
    erbt von      erbt von
         |            |
+----------------+  +--------------------+
|     PKW        |  |       LKW          |
|----------------|  |--------------------|
| - anzahlSitze  |  | - ladekapazitaet   |
|----------------|  |--------------------|
| + beschreibung |  | + beschreibung()   |
+----------------+  +--------------------+
```

**Wichtige Begriffe:**
- **Oberklasse (Superklasse)** – Klasse, von der geerbt wird
- **Unterklasse (Subklasse)** – Klasse, die erbt
- **super** – Zugriff auf Methoden/Konstruktor der Oberklasse
- **Ist-ein-Beziehung** – PKW ist ein Fahrzeug (Vererbung)
- **Hat-ein-Beziehung** – Fahrzeug hat einen Motor (Komposition, keine Vererbung)

**Erklaerung:** Durch Vererbung muessen gemeinsame Attribute (marke, baujahr) und Methoden nur einmal in der Elternklasse definiert werden. Kindklassen fuegen spezifische Attribute hinzu und koennen Methoden ueberschreiben.
