# Komplett: 1.4.08 – Grundlagen relationaler Datenbanken / ER-Modelle

## Einordnung
- **Abschnitt:** 1.4 – Auftragsumgebung
- **Thema:** Grundlagen von relationalen Datenbanken kennen und anwenden koennen
- **Themenkreis:** Einfache ER-Modelle

## Ziel
Grundlegendes Verstaendnis fuer Entity-Relationship-Modelle (ER-Modelle) als Werkzeug zur Datenmodellierung.

---

## Definition
Ein **ER-Modell** (Entity-Relationship-Modell) ist eine grafische Darstellung von Daten und deren Beziehungen zueinander. Es dient als Grundlage fuer den Entwurf relationaler Datenbanken.

## Kernbegriffe

| Begriff | Erklaerung | Beispiel |
|---|---|---|
| **Entitaet (Entity)** | Ein real existierendes oder abstraktes Objekt | Kunde, Produkt, Bestellung |
| **Attribut** | Eigenschaft einer Entitaet | Kundenname, Preis, Datum |
| **Primaerschluessel (PK)** | Eindeutiges Identifikationsmerkmal | KundenNr, ProduktID |
| **Beziehung (Relationship)** | Verbindung zwischen Entitaeten | Kunde *bestellt* Produkt |
| **Kardinalitaet** | Anzahlverhaeltnis der Beziehung | 1:1, 1:n, n:m |

## Kardinalitaeten

| Typ | Bedeutung | Beispiel |
|---|---|---|
| **1:1** | Genau eine Zuordnung | Person ↔ Personalausweis |
| **1:n** | Eins zu viele | Abteilung → Mitarbeiter |
| **n:m** | Viele zu viele | Schueler ↔ Kurse |

## ER-Diagramm: Notation

```
┌─────────────┐         ┌─────────────────┐         ┌──────────────┐
│   Kunde     │ 1     n │   Bestellung    │ n     m │   Produkt    │
├─────────────┤─────────├─────────────────┤─────────├──────────────┤
│ *KundenNr   │         │ *BestellNr      │         │ *ProduktID   │
│  Name       │         │  Datum          │         │  Bezeichnung │
│  Email      │         │  Gesamtbetrag   │         │  Preis       │
└─────────────┘         └─────────────────┘         └──────────────┘
```

- * = Primaerschluessel (PK)
- Linien zeigen Beziehungen
- Kardinalitaeten stehen an den Enden

## Vom ER-Modell zur Tabelle

**Regel 1:n:** Der Primaerschluessel der 1-Seite wird als Fremdschluessel in die n-Seite uebernommen.

**Regel n:m:** Es entsteht eine Zwischentabelle (Assoziationstabelle) mit den Primaerschluesseln beider Entitaeten.

**Beispiel: Bestellung_Produkt (Zwischentabelle):**

| BestellNr (FK) | ProduktID (FK) | Menge |
|---|---|---|
| 1001 | P01 | 3 |
| 1001 | P03 | 1 |
| 1002 | P01 | 2 |

## Referenzielle Integritaet
- Jeder Fremdschluessel muss auf einen existierenden Primaerschluessel verweisen
- **Aktualisierungsweitergabe:** Aendert sich ein PK, werden alle FK automatisch angepasst
- **Loeschweitergabe:** Wird ein Datensatz geloescht, werden abhaengige Datensaetze ebenfalls geloescht (CASCADE) oder die Loeschung wird verhindert (RESTRICT)

## Querverweise
- → 2.2.03 (Datenbanken modellieren: SQL, Normalisierung, Anomalien)
- → 3.4.10 (Datenmodelle erstellen: ER-Modell, Relationales Modell)
- → 3.4.11 (Normalisierung: 1. bis 3. Normalform)

---

## Uebungen

### Aufgabe 1
Erstelle ein ER-Modell fuer folgendes Szenario:
- Ein **Verlag** hat mehrere **Autoren**
- Ein **Autor** kann mehrere **Buecher** schreiben
- Ein **Buch** kann von mehreren Autoren geschrieben werden
- Jedes Buch hat eine ISBN, einen Titel und ein Erscheinungsjahr

### Aufgabe 2
Welche Kardinalitaet liegt vor?
a) Ehepartner ↔ Ehepartner
b) Klasse → Schueler
c) Student ↔ Vorlesung

### Aufgabe 3
Gegeben ist folgendes ER-Modell. Erstelle daraus die Tabellenstruktur mit PK und FK:
- Entitaet **Abteilung** (AbtNr, Name)
- Entitaet **Mitarbeiter** (MitNr, Name, Gehalt)
- Beziehung: Eine Abteilung hat mehrere Mitarbeiter (1:n)

---
---

### Loesung 1
```
┌──────────┐       ┌──────────┐       ┌──────────┐
│  Verlag  │ 1   n │  Autor   │ n   m │   Buch   │
├──────────┤───────├──────────┤───────├──────────┤
│ *VerlagID│       │ *AutorID │       │ *ISBN    │
│  Name    │       │  Name    │       │  Titel   │
│  Ort     │       │  Geburt  │       │  Jahr    │
└──────────┘       └──────────┘       └──────────┘

Zwischentabelle: Autor_Buch
│ AutorID (FK) │ ISBN (FK) │
```

### Loesung 2
a) 1:1
b) 1:n
c) n:m

### Loesung 3
**Tabelle Abteilung:**
| AbtNr (PK) | Name |
|---|---|
| 1 | Entwicklung |
| 2 | Vertrieb |

**Tabelle Mitarbeiter:**
| MitNr (PK) | Name | Gehalt | AbtNr (FK) |
|---|---|---|---|
| 101 | Mueller | 3500 | 1 |
| 102 | Schmidt | 3200 | 1 |
| 103 | Weber | 3800 | 2 |

→ Der FK `AbtNr` in Mitarbeiter verweist auf PK `AbtNr` in Abteilung (1:n Regel).
