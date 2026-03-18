# Vertiefung und Uebungen: 3.4.12 – Architektur- und Design-Pattern anwenden

## Vertiefung

### Uebersicht: Pattern-Kategorien

| Kategorie | Pattern | Zweck |
|-----------|---------|-------|
| Erzeugungsmuster | Factory, Singleton | Wie werden Objekte erzeugt? |
| Strukturmuster | MVC, Adapter, Decorator | Wie sind Klassen/Objekte zusammengesetzt? |
| Verhaltensmuster | Observer, Strategy | Wie kommunizieren Objekte? |

### Vergleich der vier Patterns

| Kriterium | Factory | MVC | Observer | Singleton |
|-----------|---------|-----|----------|-----------|
| Kategorie | Erzeugung | Architektur | Verhalten | Erzeugung |
| Zweck | Objekte ueber Fabrik erzeugen | UI, Logik, Steuerung trennen | Auf Aenderungen reagieren | Genau eine Instanz |
| Kopplung | Lose (Client ↔ Produkt) | Lose (Model ↔ View) | Lose (Subject ↔ Observer) | Eng (globaler Zugriff) |
| Komplexitaet | Mittel | Hoch | Mittel | Gering |
| Pruefungsrelevanz | Hoch | Sehr hoch | Hoch | Hoch |

### MVC in Webanwendungen – Detailablauf

```
+----------+    HTTP-Request     +-----------+
| Browser  | ------------------> | Controller|
+----------+                     +-----------+
                                   |       |
                             liest |       | aktualisiert
                                   v       v
                              +-----------+
                              |   Model   |
                              | (Datenbank|
                              |  + Logik) |
                              +-----------+
                                   |
                              liefert Daten
                                   |
                                   v
                              +-----------+    HTTP-Response     +----------+
                              |   View    | ------------------> | Browser  |
                              | (Template)|                     +----------+
                              +-----------+
```

**Konkretes Web-Beispiel:**
1. Benutzer ruft URL `/artikel/liste` auf
2. **Controller** `ArtikelController.index()` wird aufgerufen
3. Controller fragt **Model** `Artikel.holeAlle()` ab
4. Model fuehrt SQL-Abfrage aus, gibt Ergebnis zurueck
5. Controller uebergibt Daten an **View** `artikel_liste.html`
6. View rendert HTML mit den Artikeldaten
7. HTML wird an den Browser zurueckgesendet

### Factory Pattern – Erweitertes Beispiel

Situation: Ein Grafikprogramm erzeugt verschiedene Formen (Kreis, Rechteck, Dreieck). Neue Formen sollen spaeter ergaenzt werden koennen, ohne den bestehenden Code zu aendern.

```
FormFabrik.erstelle("Kreis")     --> neuer Kreis()
FormFabrik.erstelle("Rechteck")  --> neues Rechteck()
FormFabrik.erstelle("Dreieck")   --> neues Dreieck()
```

→ Neue Form "Ellipse" hinzufuegen: Nur die Fabrik erweitern, kein Client-Code aendert sich.

### Observer Pattern – Praxisbeispiel Newsletter

```
Subject: Newsletter-System
Observer: Abonnent_A, Abonnent_B, Abonnent_C

newsletter.registriere(Abonnent_A)
newsletter.registriere(Abonnent_B)
newsletter.veroeffentliche("Neue Version 2.0 verfuegbar!")
--> Abonnent_A erhaelt Nachricht
--> Abonnent_B erhaelt Nachricht
--> Abonnent_C erhaelt KEINE Nachricht (nicht registriert)
```

### Typische Pruefungsaspekte
- Szenario lesen und passendes Pattern zuordnen koennen
- UML-Klassendiagramm eines Patterns erkennen oder zeichnen
- Vor- und Nachteile eines Patterns benennen
- MVC-Schichten in einem gegebenen Code-Beispiel identifizieren
- Singleton: Warum privater Konstruktor? → Verhindert externe Instanziierung

### Haeufige Fehler
- MVC: View und Controller verwechseln – View zeigt nur an, Controller verarbeitet Eingaben
- Singleton wird als "globale Variable" missverstanden – es ist ein kontrollierter Zugriff
- Factory wird mit dem Konstruktor verwechselt – die Fabrik kapselt die Entscheidung, WELCHES Objekt erzeugt wird
- Observer: Vergessen, Observer abzumelden → Speicherlecks / unerwuenschte Benachrichtigungen

---

## Uebungen

**Aufgabe 1:** Ordne die folgenden Szenarien dem passenden Design Pattern zu (Factory, MVC, Observer, Singleton):
- a) Eine Webanwendung trennt die HTML-Ausgabe von der Datenbankabfrage und der URL-Verarbeitung.
- b) Ein Logging-System stellt sicher, dass alle Module dieselbe Log-Instanz verwenden.
- c) Ein Online-Shop benachrichtigt registrierte Kunden automatisch, wenn ein Produkt wieder verfuegbar ist.
- d) Ein Dokumentenmanagementsystem erzeugt je nach Dateityp (.pdf, .docx, .csv) das passende Parser-Objekt.

**Aufgabe 2:** Zeichne das UML-Klassendiagramm (als ASCII oder Skizze) fuer ein Singleton-Pattern am Beispiel eines Konfigurationsmanagers. Benenne alle Attribute und Methoden.

**Aufgabe 3:** Erklaere, warum der Konstruktor beim Singleton-Pattern privat sein muss. Was wuerde passieren, wenn er oeffentlich waere?

**Aufgabe 4:** Nenne drei Vorteile des MVC-Patterns und erklaere, warum es besonders fuer Webanwendungen geeignet ist.

**Aufgabe 5:** Ein Unternehmen entwickelt eine Wetterstation. Mehrere Anzeigegeraete (Display, App, Webseite) sollen automatisch aktualisiert werden, wenn sich die Messwerte aendern. Welches Pattern ist geeignet? Beschreibe den Ablauf in Pseudocode.

**Aufgabe 6:** Erklaere den Unterschied zwischen Erzeugungsmuster, Strukturmuster und Verhaltensmuster. Ordne Factory, MVC, Observer und Singleton zu.

---
---

# Loesungen

## Aufgabe 1
- a) **MVC** – HTML-Ausgabe = View, Datenbankabfrage = Model, URL-Verarbeitung = Controller
- b) **Singleton** – Genau eine Instanz des Loggers fuer alle Module
- c) **Observer** – Kunden sind Observer, Produkt ist Subject, Benachrichtigung bei Zustandsaenderung
- d) **Factory** – Fabrikmethode entscheidet anhand des Dateityps, welches Parser-Objekt erzeugt wird

## Aufgabe 2

```
+----------------------------------+
|     KonfigurationsManager        |
|----------------------------------|
| - instanz: KonfigurationsManager |  (statisch, privat)
| - einstellungen: Map             |
|----------------------------------|
| - KonfigurationsManager()        |  (privater Konstruktor)
| + gibInstanz(): KonfigManager    |  (statisch)
| + ladeEinstellung(key): String   |
| + setzeEinstellung(key, value)   |
+----------------------------------+
```

## Aufgabe 3
Der Konstruktor muss privat sein, damit kein externer Code mit `neues KonfigurationsManager()` eine zweite Instanz erzeugen kann. Die einzige Moeglichkeit, eine Instanz zu erhalten, ist ueber die statische Methode `gibInstanz()`, die prueft, ob bereits eine Instanz existiert. Waere der Konstruktor oeffentlich, koennten beliebig viele Instanzen erzeugt werden – das Singleton-Prinzip waere verletzt.

## Aufgabe 4
1. **Trennung der Zustaendigkeiten:** Frontend-Entwickler koennen die View aendern, ohne die Geschaeftslogik im Model zu beruehren.
2. **Wiederverwendbarkeit:** Dasselbe Model kann mit verschiedenen Views genutzt werden (z.B. HTML-Seite und REST-API).
3. **Testbarkeit:** Model und Controller koennen unabhaengig von der View getestet werden (Unit-Tests).
Fuer Webanwendungen geeignet, weil: HTTP-Requests natuerlich auf Controller abgebildet werden, Templates als Views dienen und die Datenbank das Model darstellt. Frameworks wie Django, Spring MVC und ASP.NET nutzen dieses Prinzip.

## Aufgabe 5
Geeignetes Pattern: **Observer**

```
KLASSE WetterStation                // Subject
    ATTRIBUT observer: Liste
    ATTRIBUT temperatur: Zahl
    ATTRIBUT luftfeuchtigkeit: Zahl

    METHODE registriere(o: Observer)
        observer.hinzufuegen(o)
    ENDE METHODE

    METHODE benachrichtige()
        FUER JEDES o IN observer
            o.aktualisiere(temperatur, luftfeuchtigkeit)
        ENDE FUER
    ENDE METHODE

    METHODE messwertGeaendert(temp, feuchte)
        temperatur = temp
        luftfeuchtigkeit = feuchte
        benachrichtige()
    ENDE METHODE
ENDE KLASSE

KLASSE DisplayAnzeige              // Observer
    METHODE aktualisiere(temp, feuchte)
        ausgabe("Display: " + temp + "°C, " + feuchte + "%")
    ENDE METHODE
ENDE KLASSE

// Verwendung:
station = neue WetterStation()
display = neue DisplayAnzeige()
app = neue AppAnzeige()
station.registriere(display)
station.registriere(app)
station.messwertGeaendert(23.5, 65)
// --> Beide Anzeigen werden automatisch aktualisiert
```

## Aufgabe 6
- **Erzeugungsmuster:** Betreffen die Art, wie Objekte erzeugt werden. → Factory, Singleton
- **Strukturmuster:** Betreffen die Zusammensetzung von Klassen und Objekten. → MVC (Architektur-Pattern, wird oft auch als Strukturmuster eingeordnet)
- **Verhaltensmuster:** Betreffen die Kommunikation und Interaktion zwischen Objekten. → Observer

Hinweis: MVC wird in der Literatur teils als Architekturmuster (uebergeordnet zu Design Patterns) eingeordnet. In der IHK-Pruefung wird es zusammen mit Design Patterns abgefragt.
