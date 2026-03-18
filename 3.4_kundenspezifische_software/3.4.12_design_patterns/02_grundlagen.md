# Grundlagen: 3.4.12 – Architektur- und Design-Pattern anwenden

## Factory Pattern

**Definition:** Das Factory Pattern ist ein Erzeugungsmuster (Creational Pattern), bei dem eine Fabrikmethode die Instanziierung von Objekten uebernimmt. Der Client-Code kennt nur die abstrakte Schnittstelle, nicht die konkrete Klasse.

**UML-Diagramm (ASCII):**

```
+-------------------+          +---------------------+
|   Client          |          |  <<interface>>      |
|-------------------|          |  Produkt            |
| - fabrik: Fabrik  |--------->|---------------------|
|                   |          | + operation()       |
+-------------------+          +---------------------+
                                       ^    ^
                                       |    |
                          +------------+    +------------+
                          |                              |
                +-----------------+            +-----------------+
                | KonkretesA      |            | KonkretesB      |
                |-----------------|            |-----------------|
                | + operation()   |            | + operation()   |
                +-----------------+            +-----------------+

+-------------------+
|   Fabrik          |
|-------------------|
| + erstelle(typ)   |---> gibt KonkretesA oder KonkretesB zurueck
+-------------------+
```

**Pseudocode:**

```
KLASSE Fabrik
    METHODE erstelle(typ: String): Produkt
        WENN typ == "A" DANN
            RUECKGABE neues KonkretesA()
        SONST WENN typ == "B" DANN
            RUECKGABE neues KonkretesB()
        ENDE WENN
    ENDE METHODE
ENDE KLASSE

// Client-Code:
fabrik = neue Fabrik()
produkt = fabrik.erstelle("A")
produkt.operation()  // Client kennt nur die Schnittstelle
```

**Wann einsetzen:**
- Wenn der Client-Code nicht wissen soll, welche konkreten Klassen erzeugt werden
- Wenn neue Produkttypen ohne Aenderung des Client-Codes hinzugefuegt werden sollen

**Vorteile / Nachteile:**

| Vorteile | Nachteile |
|----------|-----------|
| Entkopplung von Erzeugung und Nutzung | Zusaetzliche Klassen erhoehen Komplexitaet |
| Neue Typen leicht ergaenzbar | Einfache Faelle werden unnoetig kompliziert |
| Zentraler Erzeugungspunkt | Fabrik kann bei vielen Typen unuebersichtlich werden |

---

## MVC (Model-View-Controller)

**Definition:** MVC ist ein Architektur-Pattern, das eine Anwendung in drei Schichten trennt: Model (Datenmodell und Geschaeftslogik), View (Benutzeroberflaeche) und Controller (Steuerung und Eingabeverarbeitung).

**UML-Diagramm (ASCII):**

```
+------------------+
|    Benutzer       |
+--------+---------+
         |
         v (Eingabe)
+--------+---------+
|   Controller      |
|-------------------|
| - verarbeitet     |
|   Benutzereingaben|
| - aktualisiert    |
|   das Model       |
+--------+---------+
    |           |
    v           v
+-------+  +-------+
| Model |  | View  |
|-------|  |-------|
| Daten |->| Zeigt |
| Logik |  | Daten |
+-------+  +-------+
```

**Ablauf:**
1. Benutzer interagiert mit der View (z.B. Klick auf Button)
2. Controller empfaengt die Eingabe und verarbeitet sie
3. Controller aktualisiert das Model (z.B. Daten aendern)
4. Model benachrichtigt die View ueber Aenderungen
5. View aktualisiert die Darstellung

**Pseudocode (Web-Beispiel):**

```
KLASSE ArtikelModel
    ATTRIBUT artikel: Liste
    METHODE holeAlle(): Liste
        RUECKGABE datenbankAbfrage("SELECT * FROM artikel")
    ENDE METHODE
ENDE KLASSE

KLASSE ArtikelView
    METHODE anzeigen(artikelListe: Liste)
        FUER JEDES a IN artikelListe
            ausgabe(a.name + " - " + a.preis + " EUR")
        ENDE FUER
    ENDE METHODE
ENDE KLASSE

KLASSE ArtikelController
    ATTRIBUT model: ArtikelModel
    ATTRIBUT view: ArtikelView
    METHODE index()
        daten = model.holeAlle()
        view.anzeigen(daten)
    ENDE METHODE
ENDE KLASSE
```

**Wann einsetzen:**
- Webanwendungen (z.B. Django, Spring MVC, ASP.NET MVC)
- Desktop-Anwendungen mit komplexer UI
- Wenn mehrere Views fuer dieselben Daten benoetigt werden

**Vorteile / Nachteile:**

| Vorteile | Nachteile |
|----------|-----------|
| Klare Trennung der Zustaendigkeiten | Hoeherer initialer Aufwand |
| View austauschbar ohne Logik-Aenderung | Kann bei kleinen Anwendungen ueberdimensioniert sein |
| Mehrere Views fuer ein Model moeglich | Kommunikation zwischen Schichten komplex |
| Parallele Entwicklung (Frontend/Backend) | Lernkurve fuer Einsteiger |

---

## Observer Pattern

**Definition:** Das Observer Pattern definiert eine 1:n-Abhaengigkeit. Ein Subject (Subjekt) verwaltet eine Liste von Observern (Beobachtern) und benachrichtigt diese automatisch bei Zustandsaenderungen.

**UML-Diagramm (ASCII):**

```
+----------------------+          +---------------------+
|  <<interface>>       |          |  <<interface>>      |
|  Subject             |          |  Observer           |
|----------------------|          |---------------------|
| + registriere(o)     |<>----->>| + aktualisiere()    |
| + entferne(o)        |          +---------------------+
| + benachrichtige()   |                  ^    ^
+----------------------+                  |    |
         ^                    +-----------+    +----------+
         |                    |                           |
+--------+-----------+  +-----+--------+    +-----+--------+
| KonkretesSubject   |  | ObserverA    |    | ObserverB    |
|--------------------|  |--------------|    |--------------|
| - zustand          |  | + aktuali-   |    | + aktuali-   |
| + getZustand()     |  |   siere()    |    |   siere()    |
| + setZustand()     |  +--------------+    +--------------+
+--------------------+
```

**Pseudocode:**

```
KLASSE TemperaturSensor   // Subject
    ATTRIBUT observer: Liste
    ATTRIBUT temperatur: Zahl

    METHODE registriere(o: Observer)
        observer.hinzufuegen(o)
    ENDE METHODE

    METHODE benachrichtige()
        FUER JEDES o IN observer
            o.aktualisiere(temperatur)
        ENDE FUER
    ENDE METHODE

    METHODE setTemperatur(wert: Zahl)
        temperatur = wert
        benachrichtige()
    ENDE METHODE
ENDE KLASSE

KLASSE DisplayAnzeige   // Observer
    METHODE aktualisiere(temperatur: Zahl)
        ausgabe("Aktuelle Temperatur: " + temperatur + " Grad")
    ENDE METHODE
ENDE KLASSE

// Verwendung:
sensor = neuer TemperaturSensor()
display = neue DisplayAnzeige()
sensor.registriere(display)
sensor.setTemperatur(22.5)  // Display wird automatisch aktualisiert
```

**Wann einsetzen:**
- Event-Systeme (z.B. GUI-Button-Klicks)
- Publish-Subscribe-Mechanismen
- Wenn mehrere Komponenten auf Aenderungen reagieren muessen

**Vorteile / Nachteile:**

| Vorteile | Nachteile |
|----------|-----------|
| Lose Kopplung zwischen Subject und Observer | Reihenfolge der Benachrichtigung nicht garantiert |
| Neue Observer ohne Aenderung am Subject | Kann zu unerwarteten Kettenreaktionen fuehren |
| Dynamisches An-/Abmelden moeglich | Speicherlecks bei nicht entfernten Observern |

---

## Singleton Pattern

**Definition:** Das Singleton Pattern stellt sicher, dass eine Klasse nur genau eine Instanz besitzt. Es bietet einen globalen Zugriffspunkt auf diese Instanz ueber eine statische Methode.

**UML-Diagramm (ASCII):**

```
+---------------------------+
|       Singleton           |
|---------------------------|
| - instanz: Singleton      |  (statisch, privat)
|---------------------------|
| - Singleton()             |  (privater Konstruktor)
| + gibInstanz(): Singleton |  (statisch, oeffentlich)
| + operation()             |
+---------------------------+
```

**Pseudocode:**

```
KLASSE Datenbankverbindung
    STATISCH PRIVAT instanz: Datenbankverbindung = NULL

    PRIVAT KONSTRUKTOR Datenbankverbindung()
        // Verbindung herstellen
    ENDE KONSTRUKTOR

    STATISCH METHODE gibInstanz(): Datenbankverbindung
        WENN instanz == NULL DANN
            instanz = neue Datenbankverbindung()
        ENDE WENN
        RUECKGABE instanz
    ENDE METHODE

    METHODE abfrage(sql: String): Ergebnis
        // SQL ausfuehren und Ergebnis zurueckgeben
    ENDE METHODE
ENDE KLASSE

// Verwendung:
db = Datenbankverbindung.gibInstanz()
db.abfrage("SELECT * FROM kunden")
```

**Wann einsetzen:**
- Datenbankverbindungen (Connection Pool)
- Konfigurationsmanager
- Logger / Logging-System
- Druckerwarteschlange (Spooler)

**Vorteile / Nachteile:**

| Vorteile | Nachteile |
|----------|-----------|
| Genau eine Instanz garantiert | Globaler Zustand → schwer testbar |
| Kontrollierter Zugriff | Kann Multithreading-Probleme verursachen |
| Lazy Initialization moeglich | Wird oft ueberstrapaziert (Anti-Pattern-Gefahr) |
| Ressourcen werden gespart | Versteckte Abhaengigkeiten im Code |
