# Uebungen: 2.1.03 – Daten multimedial aufbereiten und praesentieren

## Aufgabe 1: Diagrammtyp waehlen
Welches Diagramm eignet sich jeweils am besten? Begruende kurz.
a) Monatliche IT-Supportanfragen ueber ein Jahr
b) Verteilung der Betriebssysteme im Unternehmen (Windows, Linux, macOS)
c) Vergleich der Anschaffungskosten von 5 Notebooks
d) Projektfortschritt mit Meilensteinen und Zeitraum

---
---

**Loesung Aufgabe 1:**
a) **Liniendiagramm** – Zeitreihe, Trend erkennbar (steigend/fallend/saisonal).
b) **Kreisdiagramm** – Anteile am Ganzen (3 Kategorien, summieren sich auf 100%).
c) **Balken-/Saeulendiagramm** – Vergleich diskreter Werte (5 Produkte).
d) **Gantt-Diagramm** – Zeitplanung mit Start-/Enddaten und Abhaengigkeiten.

---

## Aufgabe 2: Excel-Formeln
Gegeben ist folgende Tabelle:

| | A | B | C |
|---|---|---|---|
| 1 | Mitarbeiter | Stunden | Stundensatz |
| 2 | Mueller | 160 | 45 € |
| 3 | Schmidt | 140 | 50 € |
| 4 | Weber | 180 | 42 € |

a) Schreibe eine Formel fuer die Personalkosten von Mueller (Zelle D2).
b) Schreibe eine Formel fuer die Gesamtpersonalkosten (Zelle D5).
c) Schreibe eine Formel fuer die durchschnittlichen Stunden (Zelle B5).
d) Schreibe eine Formel, die in E2 "Ueberstunden" ausgibt, wenn B2 > 160, sonst "Normal".

---
---

**Loesung Aufgabe 2:**
a) `=B2*C2` → 160 * 45 = 7.200 €
b) `=SUMME(D2:D4)` → 7.200 + 7.000 + 7.560 = 21.760 €
c) `=MITTELWERT(B2:B4)` → (160 + 140 + 180) / 3 = 160
d) `=WENN(B2>160;"Ueberstunden";"Normal")` → "Normal" (160 ist nicht > 160)

---

## Aufgabe 3: CI-konforme Praesentation
Ein Unternehmen hat folgende CI-Vorgaben:
- Primaerfarbe: #003366 (Dunkelblau)
- Sekundaerfarbe: #FF9900 (Orange)
- Schriftart: Arial
- Logo: Oben rechts auf jeder Folie

Ein Mitarbeiter erstellt eine Praesentation mit Comic Sans, bunten Hintergruenden und ohne Logo.
a) Nenne drei konkrete Verstoesse gegen die CI.
b) Erklaere, warum Corporate Design bei Praesentationen wichtig ist.

---
---

**Loesung Aufgabe 3:**
a) (1) Falsche Schriftart: Comic Sans statt Arial. (2) Fehlendes Logo oben rechts. (3) Bunte Hintergruende statt der definierten Unternehmensfarben Dunkelblau/Orange.
b) Corporate Design sorgt fuer einen professionellen, einheitlichen Auftritt gegenueber Kunden. Es staerkt die Wiedererkennung und Glaubwuerdigkeit des Unternehmens. Kunden verbinden konsistentes Design mit Zuverlaessigkeit und Kompetenz.

---

## Aufgabe 4: Praesentationstechnik
Du sollst einem Kunden die Ergebnisse eines IT-Sicherheitsaudits praesentieren. Die Praesentation dauert 15 Minuten.
a) Erstelle eine sinnvolle Folienstruktur (6-8 Folien mit Stichworten).
b) Nenne zwei Regeln fuer einen guten Foliensatz.
c) Welche Visualisierung eignet sich fuer die Darstellung gefundener Schwachstellen nach Schweregrad?

---
---

**Loesung Aufgabe 4:**
a)
1. **Titel:** IT-Sicherheitsaudit – Ergebnisse [Datum, Kundenname]
2. **Agenda:** Ziel, Methodik, Ergebnisse, Empfehlungen
3. **Methodik:** Pruefbereiche (Netzwerk, Server, Endgeraete, Prozesse)
4. **Ergebnis-Uebersicht:** Gesamtbewertung, Anzahl Schwachstellen nach Schweregrad
5. **Kritische Schwachstellen:** Top 3 mit Beschreibung und Risiko
6. **Empfehlungen:** Priorisierte Massnahmenliste
7. **Zeitplan:** Vorgeschlagene Umsetzungsreihenfolge
8. **Naechste Schritte / Fragen**

b) (1) Maximal 6 Stichpunkte pro Folie, keine ganzen Saetze. (2) Eine Kernaussage pro Folie – nicht ueberladen.

c) **Gestapeltes Saeulendiagramm** oder **Balkendiagramm** mit Farbkodierung: Rot = kritisch, Orange = hoch, Gelb = mittel, Gruen = niedrig. Alternativ: Tabelle mit Ampelfarben.
