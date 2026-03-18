# Komplett: 3.4.04 – Objektorientierte Analyse- und Designverfahren

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.04
- **Thema:** Objektorientierte Analyse- und Designverfahren anwenden koennen

## Ziel

Du musst die Schritte der objektorientierten Analyse (OOA) und des objektorientierten Designs (OOD) kennen, Klassen aus Anforderungen ableiten und grundlegende Designprinzipien anwenden koennen.

## Grundlagen

### Objektorientierte Analyse (OOA)

**Definition:** Die OOA identifiziert aus den fachlichen Anforderungen (z.B. Lastenheft) die relevanten Objekte, Klassen, Attribute und Methoden des Systems.

**Vorgehen:**
1. **Anforderungen lesen** – Lastenheft, User Stories, Gespraechsprotokolle
2. **Substantive markieren** → Kandidaten fuer **Klassen** und **Attribute**
3. **Verben markieren** → Kandidaten fuer **Methoden**
4. **Beziehungen identifizieren** → Assoziationen, Kompositionen, Vererbung
5. **Erstes Klassendiagramm erstellen** → grobe Struktur

**Beispiel – Anforderungstext:**
> "Ein **Kunde** gibt eine **Bestellung** auf. Jede Bestellung enthaelt mehrere **Artikel**. Der Kunde hat einen **Namen** und eine **Adresse**. Artikel haben eine **Bezeichnung** und einen **Preis**."

**Ableitung:**

| Element | Typ | Quelle |
|---------|-----|--------|
| Kunde | Klasse | Substantiv |
| Bestellung | Klasse | Substantiv |
| Artikel | Klasse | Substantiv |
| Name, Adresse | Attribute von Kunde | Substantive (Eigenschaften) |
| Bezeichnung, Preis | Attribute von Artikel | Substantive (Eigenschaften) |
| aufgeben() | Methode von Kunde | Verb "gibt auf" |
| enthalten() | Beziehung Bestellung → Artikel | Verb "enthaelt" |

### CRC-Karten (Class-Responsibility-Collaboration)

**Definition:** CRC-Karten sind ein einfaches Werkzeug zur fruehen Identifikation von Klassen. Jede Karte beschreibt eine Klasse mit ihren Verantwortlichkeiten und Kooperationspartnern.

```
+----------------------------------+
|          KLASSE: Kunde           |
+----------------------------------+
| Verantwortlichkeiten:            |
| - Name und Adresse verwalten     |
| - Bestellung aufgeben            |
+----------------------------------+
| Kooperationen:                   |
| - Bestellung                     |
+----------------------------------+
```

```
+----------------------------------+
|       KLASSE: Bestellung         |
+----------------------------------+
| Verantwortlichkeiten:            |
| - Artikel verwalten              |
| - Gesamtpreis berechnen          |
| - Status aendern                 |
+----------------------------------+
| Kooperationen:                   |
| - Kunde, Artikel                 |
+----------------------------------+
```

### Objektorientiertes Design (OOD)

**Definition:** Das OOD verfeinert das OOA-Modell zur technischen Umsetzung: Klassen werden detailliert, Datentypen festgelegt, Sichtbarkeiten definiert und Entwurfsmuster angewendet.

**Schritte im OOD:**
1. OOA-Klassendiagramm verfeinern (Datentypen, Sichtbarkeiten)
2. Entwurfsmuster (Design Patterns) anwenden
3. Schnittstellen (Interfaces) definieren
4. Vererbungshierarchien optimieren
5. Sequenzdiagramme fuer wichtige Ablaeufe erstellen

**Sichtbarkeiten in UML:**

| Symbol | Bedeutung | Erklaerung |
|--------|-----------|-----------|
| + | public | Von ueberall zugreifbar |
| - | private | Nur innerhalb der eigenen Klasse |
| # | protected | Innerhalb der Klasse und in Unterklassen |
| ~ | package | Innerhalb des gleichen Pakets |

### SOLID-Prinzipien (Ueberblick)

| Buchstabe | Prinzip | Bedeutung |
|-----------|---------|-----------|
| S | Single Responsibility | Jede Klasse hat genau eine Aufgabe |
| O | Open/Closed | Offen fuer Erweiterung, geschlossen fuer Aenderung |
| L | Liskov Substitution | Unterklassen muessen die Oberklasse ersetzen koennen |
| I | Interface Segregation | Viele kleine Interfaces statt eines grossen |
| D | Dependency Inversion | Abhaengigkeiten auf Abstraktionen, nicht auf konkrete Klassen |

### OOP-Grundkonzepte

| Konzept | Beschreibung |
|---------|-------------|
| Klasse | Bauplan fuer Objekte (Attribute + Methoden) |
| Objekt | Konkrete Instanz einer Klasse |
| Vererbung | Unterklasse uebernimmt Attribute/Methoden der Oberklasse |
| Polymorphismus | Gleiche Methode, unterschiedliches Verhalten je nach Klasse |
| Kapselung | Zugriff auf Attribute nur ueber Methoden (Getter/Setter) |
| Abstraktion | Nur relevante Eigenschaften modellieren |

---

## Vertiefung

### OOA vs. OOD im Vergleich

| Aspekt | OOA | OOD |
|--------|-----|-----|
| Ziel | Fachliche Modellierung (WAS) | Technische Modellierung (WIE) |
| Perspektive | Kundensicht / Fachbereich | Entwicklersicht |
| Ergebnis | Fachliches Klassendiagramm | Technisches Klassendiagramm |
| Datentypen | Noch nicht festgelegt | Konkret (String, int, Date) |
| Sichtbarkeiten | Noch nicht definiert | +, -, #, ~ |
| Design Patterns | Noch nicht angewendet | Werden eingesetzt |

### Typische Pruefungsaspekte
- Aus einem Anforderungstext Klassen, Attribute und Methoden ableiten
- CRC-Karten erstellen oder interpretieren
- OOA von OOD unterscheiden
- OOP-Grundkonzepte (Vererbung, Kapselung, Polymorphismus) erklaeren
- SOLID-Prinzipien im Grundsatz kennen

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| Adjektive als Klassen identifiziert | Adjektive sind meist Attribute, nicht Klassen |
| Zu viele Klassen erstellt | Nur fachlich relevante Entitaeten werden Klassen |
| OOA und OOD vermischt | OOA = fachlich (WAS), OOD = technisch (WIE) |
| Kapselung ignoriert | Attribute sollten private sein, Zugriff ueber Getter/Setter |
| Vererbung fuer alles verwendet | Komposition ist oft besser als Vererbung ("favor composition over inheritance") |

---

## Uebungen

**Aufgabe 1:** Lies den folgenden Anforderungstext und leite Klassen, Attribute und Methoden ab:
> "Ein Mitarbeiter erfasst Projekte im System. Jedes Projekt hat einen Namen, ein Startdatum und ein Budget. Einem Projekt koennen mehrere Aufgaben zugeordnet werden. Jede Aufgabe hat eine Beschreibung und einen Status (offen/erledigt). Der Mitarbeiter kann Aufgaben als erledigt markieren."

**Aufgabe 2:** Erstelle eine CRC-Karte fuer die Klasse "Projekt" aus Aufgabe 1.

**Aufgabe 3:** Erklaere den Unterschied zwischen Kapselung und Abstraktion in je zwei Saetzen.

---
---

# Loesungen

## Aufgabe 1

| Element | Typ | Quelle |
|---------|-----|--------|
| Mitarbeiter | Klasse | Substantiv |
| Projekt | Klasse | Substantiv |
| Aufgabe | Klasse | Substantiv |
| Name, Startdatum, Budget | Attribute von Projekt | Substantive |
| Beschreibung, Status | Attribute von Aufgabe | Substantive |
| erfassen() | Methode von Mitarbeiter | Verb "erfasst" |
| zuordnen() | Methode/Beziehung Projekt → Aufgabe | Verb "zugeordnet" |
| alsErledigtMarkieren() | Methode von Aufgabe (oder Mitarbeiter) | Verb "als erledigt markieren" |

**Beziehungen:**
- Mitarbeiter → Projekt: Assoziation (erfasst)
- Projekt → Aufgabe: Komposition/Aggregation (1:n)

## Aufgabe 2
```
+----------------------------------+
|        KLASSE: Projekt           |
+----------------------------------+
| Verantwortlichkeiten:            |
| - Name, Startdatum, Budget       |
|   verwalten                      |
| - Aufgaben zuordnen              |
| - Projektstatus ueberblicken     |
+----------------------------------+
| Kooperationen:                   |
| - Aufgabe, Mitarbeiter           |
+----------------------------------+
```

## Aufgabe 3
- **Kapselung:** Interne Daten einer Klasse werden vor direktem Zugriff geschuetzt (Attribute sind private). Der Zugriff erfolgt ueber definierte Methoden (Getter/Setter), sodass Aenderungen kontrolliert werden.
- **Abstraktion:** Nur die fuer das Problem relevanten Eigenschaften und Verhaltensweisen eines Objekts werden modelliert. Unwichtige Details werden ausgeblendet, um die Komplexitaet zu reduzieren.
