# Vertiefung und Uebungen: 1.6.02 – Schutzbedarfsanalyse

## Vorgehensmodell Schutzbedarfsanalyse

```
1. Informationsverbund definieren
   (Welche Anwendungen, Systeme, Verbindungen, Raeume?)
        ↓
2. Schutzbedarfsfeststellung fuer Anwendungen
   (Pro Schutzziel: normal / hoch / sehr hoch)
        ↓
3. Vererbung auf IT-Systeme (Maximumprinzip)
        ↓
4. Vererbung auf Kommunikationsverbindungen
        ↓
5. Vererbung auf Raeume und Infrastruktur
        ↓
6. Dokumentation  →  Basis fuer Risikoanalyse und Massnahmenauswahl
```

## Maximumprinzip, Kumulationseffekt, Verteilungseffekt

| Prinzip | Erklaerung | Beispiel |
|---|---|---|
| **Maximumprinzip** | Hoechster Schutzbedarf einer Anwendung bestimmt den des Systems | Server mit ERP (sehr hoch) + Wiki (normal) → sehr hoch |
| **Kumulationseffekt** | Viele normale Anwendungen = hoeher in Summe | 20 Clients mit je „normal" → Server „hoch" wegen Gesamtauswirkung |
| **Verteilungseffekt** | Redundanz senkt Schutzbedarf des Einzelsystems | Cluster aus 3 Servern: einzeln „hoch" statt „sehr hoch" |

## Typische Pruefungsaspekte

1. **Schutzbedarfskategorien:** Normal/hoch/sehr hoch definieren
2. **Vererbungsprinzipien:** Maximum, Kumulation, Verteilung erklaeren
3. **Praxisfall:** Schutzbedarf fuer ein gegebenes Szenario bestimmen
4. **Reihenfolge:** Anwendungen → Systeme → Verbindungen → Raeume

## Haeufige Fehler

| Fehler | Richtig |
|---|---|
| Schutzbedarf nur fuer Server bestimmen | Alle Ebenen: Anwendungen, Systeme, Verbindungen, Raeume |
| Kumulationseffekt ignorieren | Viele kleine Anwendungen koennen zusammen hohen Bedarf ergeben |
| Schutzbedarf = Risikoanalyse | Schutzbedarfsanalyse ist Vorarbeit fuer die Risikoanalyse |

---

## Aufgabe 1: Schutzbedarfsfeststellung
Ein mittelstaendisches Unternehmen hat folgende Anwendungen. Bestimme fuer jede den Schutzbedarf pro Schutzziel:

a) Online-Shop (Kundendaten, Zahlungsdaten)
b) Interne Wissensdatenbank (keine personenbez. Daten)
c) Personalverwaltungssoftware (Gehaltsdaten)

## Aufgabe 2: Vererbung
Server-A hostet: Online-Shop (sehr hoch) und Wissensdatenbank (normal). Welchen Schutzbedarf hat Server-A? Begruende.

## Aufgabe 3: Kumulationseffekt
30 Arbeitsplatz-PCs mit jeweils normalem Schutzbedarf werden ueber einen zentralen Switch verbunden. Erklaere, warum der Switch einen hoeheren Schutzbedarf haben koennte.

## Aufgabe 4
Erstelle eine Schutzbedarfsanalyse fuer einen Serverraum. Beruecksichtige: Server (ERP), Netzwerk-Switch, Klimaanlage, USV.

---
---

## Loesung 1

| Anwendung | Vertraulichkeit | Integritaet | Verfuegbarkeit | Gesamt |
|---|---|---|---|---|
| Online-Shop | Sehr hoch (Zahlungsdaten) | Hoch (Bestelldaten korrekt) | Sehr hoch (Umsatz) | Sehr hoch |
| Wissensdatenbank | Normal | Normal | Normal | Normal |
| Personalverwaltung | Sehr hoch (Gehaltsdaten) | Hoch | Hoch | Sehr hoch |

## Loesung 2
Server-A hat Schutzbedarf **sehr hoch** (Maximumprinzip). Der Online-Shop mit „sehr hoch" bestimmt den Gesamtschutzbedarf des Servers, auch wenn die Wissensdatenbank nur „normal" hat.

## Loesung 3
Einzeln hat jeder PC normalen Schutzbedarf. Faellt der zentrale Switch jedoch aus, sind alle 30 Arbeitsplaetze betroffen (**Kumulationseffekt**). Der Gesamtschaden (30 Mitarbeiter koennen nicht arbeiten) rechtfertigt mindestens Schutzbedarf **hoch** fuer den Switch.

## Loesung 4

| Objekt | Vertraulichkeit | Integritaet | Verfuegbarkeit | Gesamt |
|---|---|---|---|---|
| Server (ERP) | Hoch | Hoch | Sehr hoch | Sehr hoch |
| Netzwerk-Switch | Hoch | Normal | Hoch | Hoch |
| Klimaanlage | Normal | Normal | Hoch | Hoch |
| USV | Normal | Normal | Sehr hoch | Sehr hoch |
| **Serverraum gesamt** | – | – | – | **Sehr hoch** |

Begruendung: Der Serverraum erbt den hoechsten Schutzbedarf seiner Objekte (Maximumprinzip).
