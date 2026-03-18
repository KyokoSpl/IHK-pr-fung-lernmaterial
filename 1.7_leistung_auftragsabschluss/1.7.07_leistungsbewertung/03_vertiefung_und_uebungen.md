# Vertiefung und Uebungen: 1.7.07 – Leistungsbewertung und Nachkalkulation

## Vertiefung

### Zusammenhang der Themenkreise

```
Projektabschluss
       |
       v
+-----------------+     +-------------------+
| Nachkalkulation |---->| Soll-Ist-Vergleich|
| (Kosten)        |     | (Abweichungen)    |
+-----------------+     +-------------------+
       |                        |
       v                        v
+------------------+    +--------------------+
| Lessons Learned  |<---| Ursachenanalyse    |
| (Reflexion)      |    | (Warum Abweichung?)|
+------------------+    +--------------------+
       |
       v
+------------------------+
| Nachfolgeauftraege     |
| (Cross-/Upselling,    |
|  Wartung, Erweiterung) |
+------------------------+
```

### Vergleich: Vor- vs. Nachkalkulation

| Merkmal | Vorkalkulation | Nachkalkulation |
|---|---|---|
| Zeitpunkt | Vor Projektstart | Nach Projektabschluss |
| Datenbasis | Schaetzungen, Erfahrungswerte | Tatsaechliche Kosten |
| Zweck | Angebotserstellung, Budget | Erfolgskontrolle, Erfahrung |
| Genauigkeit | Unsicher (Prognose) | Exakt (reale Daten) |
| Ergebnis | Geplanter Deckungsbeitrag | Tatsaechlicher Deckungsbeitrag |

### Deckungsbeitragsrechnung (vereinfacht)

```
  Umsatz (Auftragswert)          100.000 €
- Variable Kosten (Ist)           79.500 €
= Deckungsbeitrag                 20.500 €
- Fixkosten-Anteil (zugeordnet)   15.000 €
= Gewinn / Verlust                 5.500 €
```

### Typische Pruefungsaspekte

- Abweichungen berechnen (absolut und relativ)
- Ursachen fuer Kostenabweichungen benennen
- Massnahmen aus Lessons Learned ableiten
- Cross-Selling vs. Upselling unterscheiden
- Bedeutung der Kundenzufriedenheit fuer Folgeauftraege

### Haeufige Fehler in Pruefungen

| Fehler | Richtig |
|---|---|
| Nachkalkulation nur als Kostenliste | Immer Soll-Ist-Vergleich durchfuehren |
| Lessons Learned nur negativ | Auch positive Erfahrungen dokumentieren |
| Nachfolgeauftraege vergessen | Aktiv aus Projekterkenntnissen generieren |
| Abweichung nur absolut angeben | Immer auch prozentual berechnen |

---

## Uebungen

### Aufgabe 1: Nachkalkulation berechnen
Ein IT-Projekt wurde wie folgt kalkuliert und abgerechnet:

| Position | Soll | Ist |
|---|---|---|
| Personalkosten (160h x 80€) | 12.800 € | 14.400 € (180h x 80€) |
| Hardware | 3.500 € | 3.200 € |
| Softwarelizenzen | 2.000 € | 2.500 € |
| Reisekosten | 500 € | 800 € |

a) Berechne die Gesamtabweichung (absolut und prozentual).
b) Welche Position hat die groesste relative Abweichung?
c) Nenne zwei moegliche Ursachen fuer die Personalkostenabweichung.

---
---

**Loesung Aufgabe 1:**
a) Soll gesamt: 18.800 € | Ist gesamt: 20.900 € → Abweichung: +2.100 € (+11,2%)
b) Reisekosten: +300 € von 500 € = +60% relative Abweichung (groesste)
c) Moegliche Ursachen: (1) Umfang wurde unterschaetzt, mehr Stunden noetig. (2) Nachtraegliche Aenderungswuensche des Kunden (Scope Creep).

---

### Aufgabe 2: Soll-Ist-Vergleich Zeitplan
Fuer ein Webprojekt waren folgende Meilensteine geplant:

| Meilenstein | Soll (Woche) | Ist (Woche) |
|---|---|---|
| Anforderungsanalyse | 2 | 2 |
| Design/Prototyp | 4 | 5 |
| Implementierung | 8 | 11 |
| Test | 10 | 13 |
| Go-Live | 12 | 14 |

a) In welcher Phase ist die groesste Verzoegerung entstanden?
b) Welche Auswirkung hatte die Verzoegerung auf die Folgephasen?
c) Formuliere eine Lessons-Learned-Empfehlung.

---
---

**Loesung Aufgabe 2:**
a) Implementierung: Geplant 4 Wochen (Woche 4-8), tatsaechlich 6 Wochen (Woche 5-11) → 2 Wochen Verzoegerung allein in dieser Phase.
b) Die Verzoegerung der Implementierung hat sich auf Test und Go-Live durchgeschlagen (Kaskadeneffekt). Insgesamt 2 Wochen Verzoegerung gegenueber dem Plan.
c) Empfehlung: "Fuer Implementierungsphasen sollten kuenftig groessere Zeitpuffer eingeplant werden. Ab 50% Phasenfortschritt sollte ein Zwischenreview stattfinden, um frueh Verzoegerungen zu erkennen."

---

### Aufgabe 3: Nachfolgeauftraege generieren
Ein IT-Dienstleister hat fuer eine Steuerberatungskanzlei ein lokales Netzwerk mit 15 Arbeitsplaetzen eingerichtet. Waehrend des Projekts fielen folgende Punkte auf:
- Die bestehende Backup-Loesung ist veraltet
- Mitarbeiter wuenschen sich Homeoffice-Moeglichkeit
- Der Server hat nur noch 20% freien Speicherplatz

a) Nenne drei moegliche Nachfolgeauftraege.
b) Erklaere den Unterschied zwischen Cross-Selling und Upselling anhand dieses Beispiels.

---
---

**Loesung Aufgabe 3:**
a) (1) Backup-Konzept modernisieren (z.B. Cloud-Backup, NAS mit 3-2-1-Regel). (2) VPN-Loesung fuer Homeoffice einrichten. (3) Server-Storage erweitern oder Cloud-Migration planen.
b) Cross-Selling: Dem Kunden ein anderes/ergaenzendes Produkt verkaufen (z.B. zusaetzlich eine VPN-Loesung zum Netzwerk). Upselling: Dem Kunden eine hoeherwertige Variante des bestehenden Produkts verkaufen (z.B. groesseren Server statt Speichererweiterung, Premium-Backup statt Basis-Backup).
