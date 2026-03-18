# Ueberblick: 3.4.12 – Architektur- und Design-Pattern anwenden

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.12
- **Thema:** Architektur- und Design-Pattern anwenden

## Ziel

Du musst gaengige Entwurfsmuster (Design Patterns) kennen, deren Aufbau in UML-Notation darstellen und begruenden koennen, wann welches Pattern eingesetzt wird. In der Pruefung werden typischerweise Szenarien beschrieben, zu denen das passende Pattern zugeordnet werden muss.

## Themenkreise im Ueberblick

### 1. Factory Pattern
Das Factory Pattern erzeugt Objekte, ohne die konkrete Klasse direkt im Client-Code festzulegen. Eine zentrale Fabrikmethode entscheidet anhand von Parametern, welches konkrete Objekt erstellt wird. Vorteil: Der Client-Code bleibt unabhaengig von konkreten Klassen.

### 2. MVC (Model-View-Controller)
MVC trennt eine Anwendung in drei Komponenten: Model (Daten/Logik), View (Darstellung) und Controller (Steuerung). Dieses Architektur-Pattern ist besonders wichtig fuer Webanwendungen und wird in der Pruefung haeufig abgefragt.

### 3. Observer Pattern
Das Observer Pattern definiert eine 1:n-Abhaengigkeit zwischen Objekten. Wenn sich der Zustand eines Objekts (Subject) aendert, werden alle abhaengigen Objekte (Observer) automatisch benachrichtigt. Typisch fuer Event-Systeme und GUI-Programmierung.

### 4. Singleton Pattern
Das Singleton Pattern stellt sicher, dass eine Klasse nur genau eine Instanz besitzt und bietet einen globalen Zugriffspunkt darauf. Einsatz z.B. fuer Datenbankverbindungen, Konfigurationsmanager oder Logger.

## Querverweise

- **Thema 3.4.17:** OOP-Methodenkonzepte (Vererbung, Polymorphie, Interfaces) – Grundlage fuer Design Patterns
- **Thema 3.4.02:** Vorgehensmodelle – Architektur-Patterns werden in der Entwurfsphase festgelegt
- **Thema 3.4.14:** Benutzeroberflaeche gestalten – MVC trennt UI von Logik
