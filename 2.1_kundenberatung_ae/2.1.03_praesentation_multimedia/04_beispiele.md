# Beispiele: 2.1.03 – Daten multimedial aufbereiten und praesentieren

## Beispiel 1: IT-Projektpraesentation

**Szenario:** Du praesentierst dem Kunden den Abschluss eines Netzwerk-Migrationsprojekts.

**Folienstruktur (CI-konform):**

| Folie | Inhalt | Visualisierung |
|---|---|---|
| 1 | Titel, Logo, Datum, Projektname | Corporate Design |
| 2 | Agenda (4-5 Punkte) | Aufzaehlung |
| 3 | Ausgangslage / Ist-Zustand | Netzwerkplan (vorher) |
| 4 | Ziele / Soll-Zustand | Netzwerkplan (nachher) |
| 5 | Umsetzung / Meilensteine | Gantt-Diagramm |
| 6 | Ergebnisse / KPIs | Saeulendiagramm (Vorher/Nachher) |
| 7 | Lessons Learned | Tabelle (Was gut / Was verbessern) |
| 8 | Naechste Schritte / Empfehlungen | Aufzaehlung |
| 9 | Fragen & Diskussion | Kontaktdaten |

---

## Beispiel 2: Tabellenkalkulation – Kostenvergleich

**Aufgabe:** Vergleich von drei Cloud-Anbietern fuer 50 Nutzer.

```
|   | A              | B          | C          | D          |
|---|----------------|------------|------------|------------|
| 1 | Kriterium      | Anbieter A | Anbieter B | Anbieter C |
| 2 | Preis/Nutzer   | 12,50 €    | 15,00 €    | 10,00 €    |
| 3 | Nutzeranzahl   | 50         | 50         | 50         |
| 4 | Monatlich      | =B2*B3     | =C2*C3     | =D2*D3     |
| 5 | Jaehrlich      | =B4*12     | =C4*12     | =D4*12     |
| 6 | Setup (einmal) | 500 €      | 0 €        | 250 €      |
| 7 | Gesamt 1. Jahr | =B5+B6     | =C5+C6     | =D5+D6     |
| 8 | Guenstigster   | =WENN(B7=MIN(B7:D7);"JA";"") | ... | ... |

Ergebnis:
B4 = 625 €   | C4 = 750 €   | D4 = 500 €
B5 = 7.500 € | C5 = 9.000 € | D5 = 6.000 €
B7 = 8.000 € | C7 = 9.000 € | D7 = 6.250 €
→ Anbieter C ist im 1. Jahr am guenstigsten
```

---

## Beispiel 3: Visualisierung Serverauslastung

**Daten:**

| Monat | CPU (%) | RAM (%) | Speicher (%) |
|---|---|---|---|
| Jan | 45 | 60 | 70 |
| Feb | 48 | 62 | 72 |
| Mär | 55 | 68 | 75 |
| Apr | 70 | 75 | 80 |
| Mai | 82 | 80 | 85 |
| Jun | 90 | 88 | 92 |

**Richtige Visualisierung:** Liniendiagramm mit drei Linien (CPU, RAM, Speicher).
- X-Achse: Monate
- Y-Achse: Prozent (0-100%)
- Schwellenwert bei 80% als gestrichelte Linie
- **Erkenntnis:** Alle Ressourcen naehern sich der Kapazitaetsgrenze → Handlungsbedarf

---

## Beispiel 4: Multimediale Aufbereitung Schulungsvideo

**Szenario:** Erstellen eines Schulungsvideos "Neues Ticketsystem bedienen".

**Produktionsplan:**

| Schritt | Tool | Ergebnis |
|---|---|---|
| 1. Drehbuch schreiben | Texteditor | Skript mit Szenen |
| 2. Bildschirmaufnahme | OBS Studio | Screencast der Bedienung |
| 3. Nachbearbeitung | DaVinci Resolve | Schnitt, Uebergaenge, Titel |
| 4. Untertitel | SubStation Alpha (.ass) | Barrierefreiheit |
| 5. Export | MP4 (H.264, 1080p) | Fertige Datei |
| 6. Bereitstellung | Intranet/LMS | Abrufbar fuer Mitarbeiter |
