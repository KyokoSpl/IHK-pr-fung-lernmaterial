# Vertiefung und Uebungen: 4.4.05 – Umweltschonende Ressourcennutzung

## Vertiefung

### Nachhaltige Beschaffung – Entscheidungsmatrix

Bei der Beschaffung von IT-Hardware koennen Umweltkriterien in eine **gewichtete Nutzwertanalyse** integriert werden:

| Kriterium | Gewichtung | Produkt A | Produkt B | Produkt C |
|-----------|-----------|----------|----------|----------|
| Preis | 30% | 8 Pkt. | 9 Pkt. | 6 Pkt. |
| Leistung | 25% | 9 Pkt. | 7 Pkt. | 8 Pkt. |
| Energieeffizienz | 20% | 6 Pkt. | 8 Pkt. | 9 Pkt. |
| Reparierbarkeit | 15% | 5 Pkt. | 7 Pkt. | 9 Pkt. |
| Oeko-Label | 10% | 4 Pkt. | 8 Pkt. | 10 Pkt. |

Berechnung gewichteter Gesamtwert:
- A: 0,3×8 + 0,25×9 + 0,2×6 + 0,15×5 + 0,1×4 = 2,4 + 2,25 + 1,2 + 0,75 + 0,4 = **7,00**
- B: 0,3×9 + 0,25×7 + 0,2×8 + 0,15×7 + 0,1×8 = 2,7 + 1,75 + 1,6 + 1,05 + 0,8 = **7,90**
- C: 0,3×6 + 0,25×8 + 0,2×9 + 0,15×9 + 0,1×10 = 1,8 + 2,0 + 1,8 + 1,35 + 1,0 = **7,95**

→ Produkt C gewinnt knapp trotz hoeheren Preises – die Nachhaltigkeit macht den Unterschied.

### Vergleich: Oeko-Labels fuer IT

| Aspekt | Blauer Engel | Energy Star | EPEAT | TCO Certified |
|--------|-------------|-------------|-------|---------------|
| Herkunft | Deutschland | USA/EU | USA (global) | Schweden |
| Fokus | Gesamter Lebenszyklus | Energieeffizienz | Lebenszyklus-Bewertung | Ergonomie + Umwelt |
| Stufen | Ja/Nein | Ja/Nein | Gold/Silber/Bronze | Ja/Nein |
| IT-Produkte | Drucker, Computer, Monitore | Computer, Monitore, Drucker | Computer, Monitore, Server | Monitore, Notebooks |
| Soziale Kriterien | Nein | Nein | Ja (ab 2019) | Ja |
| Kosten fuer Hersteller | Gering | Gering | Mittel | Hoch |

### Papierloses Buero – Umsetzungsschritte

```
Ist-Analyse             Digitalisierung         Prozessoptimierung
    |                        |                        |
    v                        v                        v
Papierverbrauch     Dokumentenmanagement-     Digitale Unterschriften
erfassen            system (DMS) einfuehren   (eIDAS-konform)
    |                        |                        |
    v                        v                        v
Hauptverbraucher    Scan-Workflows            Digitale Formulare
identifizieren      einrichten                und Workflows
    |                        |                        |
    v                        v                        v
Ziele definieren    Cloud-Speicher /          Follow-Me-Print
(z.B. -50%)         SharePoint nutzen         fuer Restbedarf
```

### Energiebilanz: Oekostrom vs. konventioneller Strom

Beispielrechnung fuer ein kleines Rechenzentrum (100 kW IT-Last, PUE 1,5):

```
Jaehrlicher Gesamtverbrauch = 100 kW × 1,5 (PUE) × 8.760 h = 1.314.000 kWh

CO2 bei konventionellem Strommix (DE: ca. 400 g/kWh):
1.314.000 × 0,4 kg = 525.600 kg = 525,6 t CO2/Jahr

CO2 bei Oekostrom (Windenergie: ca. 15 g/kWh):
1.314.000 × 0,015 kg = 19.710 kg = 19,7 t CO2/Jahr

Einsparung: 525,6 - 19,7 = 505,9 t CO2/Jahr (96% Reduktion)
```

### Typische Pruefungsaspekte

- Oeko-Labels benennen und deren Bedeutung erklaeren
- Kriterien fuer nachhaltige IT-Beschaffung aufzaehlen
- Vorteile von Oekostrom fuer Rechenzentren quantifizieren
- Massnahmen zum sparsamen Umgang mit Betriebsstoffen
- GHS-Kennzeichnung und Sicherheitsdatenblaetter erklaeren
- Nutzwertanalyse mit Umweltkriterien durchfuehren

### Haeufige Fehler

| Fehler | Richtigstellung |
|--------|----------------|
| Energy Star bewertet den gesamten Lebenszyklus | Energy Star bewertet primaer die Energieeffizienz im Betrieb |
| Blauer Engel ist ein EU-Label | Blauer Engel ist ein deutsches Umweltzeichen (RAL gGmbH) |
| Oekostrom ist immer teurer | Oekostromtarife sind oft preislich konkurrenzfaehig mit konventionellem Strom |
| Papierloses Buero spart nur Papier | Es spart auch Toner, Druckerenergie, Lagerplatz und Entsorgungskosten |
| Nachhaltige Beschaffung ist nur eine Frage des Labels | Auch Langlebigkeit, Reparierbarkeit und TCO muessen beruecksichtigt werden |
| Das LkSG betrifft nur produzierende Unternehmen | Auch IT-Dienstleister, die Hardware beschaffen, koennen betroffen sein |

---

## Uebungen

**Aufgabe 1:** Ein Unternehmen moechte 100 neue Monitore beschaffen. Nenne fuenf Kriterien, die bei einer umweltschonenden Beschaffung beruecksichtigt werden sollten.

**Aufgabe 2:** Erklaere den Unterschied zwischen den Labels Blauer Engel, Energy Star und EPEAT. Fuer welche Kaufentscheidung eignet sich welches Label am besten?

**Aufgabe 3:** Ein Rechenzentrum verbraucht 2.000.000 kWh pro Jahr. Berechne die CO2-Einsparung, wenn von konventionellem Strom (420 g CO2/kWh) auf Oekostrom (20 g CO2/kWh) umgestellt wird.

**Aufgabe 4:** Nenne vier konkrete Massnahmen fuer ein papierloses Buero in einem IT-Unternehmen.

**Aufgabe 5:** Ein IT-Techniker findet im Lager einen Kanister Reinigungsmittel ohne Kennzeichnung neben USV-Batterien. Welche Probleme bestehen und welche Vorschriften werden verletzt?

**Aufgabe 6:** Erstelle eine vereinfachte Nutzwertanalyse fuer zwei Drucker:
- Drucker A: 200 EUR, 500 W, kein Oeko-Label, nicht nachfuellbar
- Drucker B: 280 EUR, 300 W, Blauer Engel, nachfuellbare Kartuschen
Verwende die Kriterien Preis (30%), Energieverbrauch (25%), Oeko-Label (20%), Nachhaltigkeit (25%).

---
---

# Loesungen

## Aufgabe 1
1. **Energieeffizienz:** Geringer Stromverbrauch im Betrieb und Standby (Energy-Star-Zertifizierung)
2. **Oeko-Labels:** Monitors mit Blauem Engel oder TCO Certified bevorzugen
3. **Langlebigkeit:** Mindestens 5 Jahre Herstellergarantie und Ersatzteilversorgung
4. **Schadstoffe:** Quecksilberfrei, halogenfreie Flammschutzmittel, RoHS-konform
5. **Recyclingfaehigkeit:** Leicht zerlegbar, recycelbare Materialien (Aluminium, Glas)

## Aufgabe 2
- **Blauer Engel:** Deutsches Umweltzeichen, bewertet den gesamten Lebenszyklus (Herstellung, Nutzung, Entsorgung). Am besten geeignet fuer eine umfassende Bewertung mit Fokus auf den deutschen Markt.
- **Energy Star:** Fokussiert auf Energieeffizienz im Betrieb und Standby. Am besten geeignet, wenn Stromverbrauch das Hauptkriterium ist.
- **EPEAT:** Bewertet Lebenszyklus-Aspekte mit Abstufungen (Gold/Silber/Bronze) und beruecksichtigt auch soziale Kriterien. Am besten geeignet fuer eine differenzierte, internationale Bewertung.

## Aufgabe 3
CO2 bei konventionellem Strom: 2.000.000 kWh × 420 g/kWh = 840.000 kg = **840 t CO2/Jahr**
CO2 bei Oekostrom: 2.000.000 kWh × 20 g/kWh = 40.000 kg = **40 t CO2/Jahr**
**Einsparung: 840 - 40 = 800 t CO2/Jahr (ca. 95% Reduktion)**

## Aufgabe 4
1. **Dokumentenmanagementsystem (DMS)** einfuehren fuer digitale Archivierung und Versionskontrolle
2. **Digitale Unterschriften** (qualifizierte elektronische Signatur nach eIDAS) fuer Vertraege und Freigaben
3. **Digitale Formulare** und Workflows (z.B. Urlaubsantraege, Bestellfreigaben) statt Papierformulare
4. **Follow-Me-Print-System** einrichten – Druckauftraege nur ausfuehren, wenn der Nutzer am Drucker authentifiziert → Fehldrucke vermeiden

## Aufgabe 5
**Probleme:**
1. **Fehlende GHS-Kennzeichnung:** Der Kanister ist nicht nach GHS gekennzeichnet → Verstoss gegen die **GefStoffV** (Gefahrstoffverordnung). Mitarbeiter koennen Gefahren nicht erkennen.
2. **Fehlendes Sicherheitsdatenblatt:** Ohne SDB ist unbekannt, welche Gefahren vom Reinigungsmittel ausgehen → Verstoss gegen **REACH-Verordnung** und GefStoffV.
3. **Gemeinsame Lagerung mit Batterien:** USV-Batterien sind gefaehrliche Abfaelle. Die gemeinsame Lagerung mit unbekannten Chemikalien kann zu gefaehrlichen Reaktionen fuehren → Verstoss gegen **Lagervorschriften** der GefStoffV und des BattG.
4. **Brandgefahr:** Lithium-Batterien in der Naehe von moeglicherweise entzuendbaren Substanzen.

## Aufgabe 6

| Kriterium | Gewichtung | Drucker A | Punkte A | Drucker B | Punkte B |
|-----------|-----------|----------|----------|----------|----------|
| Preis | 30% | 200 EUR (guenstiger) | 9 | 280 EUR | 6 |
| Energieverbrauch | 25% | 500 W | 4 | 300 W | 8 |
| Oeko-Label | 20% | Keines | 0 | Blauer Engel | 10 |
| Nachhaltigkeit | 25% | Nicht nachfuellbar | 3 | Nachfuellbar | 9 |

Gewichteter Gesamtwert:
- **Drucker A:** 0,3×9 + 0,25×4 + 0,2×0 + 0,25×3 = 2,7 + 1,0 + 0,0 + 0,75 = **4,45**
- **Drucker B:** 0,3×6 + 0,25×8 + 0,2×10 + 0,25×9 = 1,8 + 2,0 + 2,0 + 2,25 = **8,05**

**Ergebnis:** Drucker B ist trotz hoeheren Anschaffungspreises die deutlich bessere Wahl unter Beruecksichtigung von Umweltkriterien. Auch die laufenden Kosten (Energie, Toner) duereften niedriger sein.
