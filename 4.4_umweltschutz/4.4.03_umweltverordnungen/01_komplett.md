# Komplett: 4.4.03 – Oeffentliche Systeme und Verordnungen/Gesetze

## Einordnung

- **Pruefungsteil:** 4.4 – Umweltschutz
- **Thema-ID:** 4.4.03
- **Thema:** Oeffentliche Systeme und Verordnungen/Gesetze

## Ziel

Du musst die wichtigsten Umweltgesetze und Verordnungen kennen, die fuer IT-Betriebe relevant sind. Dazu gehoeren Immissionsschutzregelungen, Abfallrecht und das Verpackungsgesetz mit dem Dualen System.

## Themenkreise

| Nr | Themenkreis | Schwerpunkt |
|----|------------|-------------|
| 1 | Immissionsschutzgesetz / Technische Anleitungen | BImSchG, TA Laerm, TA Luft, TA Abfall |
| 2 | Teilnahme am Dualen System | VerpackG, Verpackungsentsorgung, Gruener Punkt |

## Querverweise

- Thema 4.4.01: Umweltbelastungen (ElektroG, Recycling)
- Thema 4.4.02: Umgang mit Abfaellen (KrWG, Entsorgungspflichten)
- Thema 4.4.06: Abfallvermeidung (Kreislaufwirtschaft, Abfallhierarchie)
- Thema 4.4.07: Rechtsfolgen bei Nichteinhaltung (Bussgelder, Strafrecht)

---

## Grundlagen

### Hierarchie des Umweltrechts

```
EU-Recht (Richtlinien, Verordnungen)
    |
    v
Bundesgesetze (BImSchG, KrWG, ElektroG, VerpackG)
    |
    v
Rechtsverordnungen (BImSchV, GewAbfV, AVV)
    |
    v
Technische Anleitungen (TA Laerm, TA Luft)
    |
    v
Normen und Standards (DIN, ISO)
```

### Bundes-Immissionsschutzgesetz (BImSchG)

**Definition:** Das BImSchG schuetzt Menschen, Tiere, Pflanzen, Boden, Wasser und die Atmosphaere vor schaedlichen Umwelteinwirkungen (Immissionen) durch Anlagen, Verkehr und Produkte.

**Kernaussagen:**
- **Immissionen** sind Einwirkungen auf die Umwelt: Luftverunreinigungen, Geraeusche, Erschuetterungen, Licht, Waerme, Strahlung
- Betreiber genehmigungsbeduerftiger Anlagen muessen den Stand der Technik einhalten
- Fuer IT-Betriebe vor allem relevant bei: Laerm von Klimaanlagen, Notstromaggregaten und Kuehlsystemen

**Wichtige Begriffe:**

| Begriff | Erklaerung |
|---------|-----------|
| Immission | Einwirkung von Schadstoffen/Laerm auf die Umgebung |
| Emission | Ausstoss von Schadstoffen/Laerm an der Quelle |
| BImSchV | Bundes-Immissionsschutzverordnungen – konkretisieren das BImSchG |
| Stand der Technik | Fortschrittlichste verfuegbare Technologie zur Emissionsminderung |

---

### TA Laerm (Technische Anleitung zum Schutz gegen Laerm)

**Definition:** Die TA Laerm ist eine Verwaltungsvorschrift, die Immissionsrichtwerte fuer Geraeuschemissionen von Anlagen festlegt.

**Kernaussagen:**
- Richtwerte abhaengig vom Gebietstyp und der Tageszeit
- Gilt fuer genehmigungsbeduerftige und nicht-genehmigungsbeduerftige Anlagen
- In IT-Betrieben relevant fuer: Klimaanlagen, Kuehlsysteme, Notstromaggregate, USV-Anlagen

**Immissionsrichtwerte (Auswahl):**

| Gebietstyp | Tags (6–22 Uhr) | Nachts (22–6 Uhr) |
|------------|-----------------|-------------------|
| Industriegebiet | 70 dB(A) | 70 dB(A) |
| Gewerbegebiet | 65 dB(A) | 50 dB(A) |
| Mischgebiet | 60 dB(A) | 45 dB(A) |
| Allgemeines Wohngebiet | 55 dB(A) | 40 dB(A) |
| Reines Wohngebiet | 50 dB(A) | 35 dB(A) |

**Erklaerung:** Ein Rechenzentrum in einem Gewerbegebiet darf tags maximal 65 dB(A) und nachts maximal 50 dB(A) an der naechsten Wohnbebauung verursachen. Werden die Werte ueberschritten, koennen Betriebseinschraenkungen oder Auflagen folgen.

---

### TA Luft (Technische Anleitung zur Reinhaltung der Luft)

**Definition:** Die TA Luft legt Immissions- und Emissionswerte fuer Luftschadstoffe fest und konkretisiert das BImSchG.

**Kernaussagen:**
- Regelt Grenzwerte fuer Staub, Stickoxide, Schwefeldioxid und andere Schadstoffe
- Fuer IT-Betriebe relevant bei: Notstromaggregaten (Diesel) und Loetarbeiten in der Hardwarefertigung
- Pflicht zur Emissionsminderung nach dem Stand der Technik

**IT-Relevanz:**

| Quelle | Relevante Emission | Massnahme |
|--------|-------------------|-----------|
| Diesel-Notstromaggregate | Stickoxide, Feinstaub, CO₂ | Abgasfilter, Betriebsstundenbegrenzung |
| Loetarbeiten (Hardwarewerkstatt) | Loetdaempfe, Flussmittel | Absauganlage, Lueftung |
| Serverraum-Kuehlung | Kaeltemittel bei Leckage (F-Gase) | Dichtheitspruefung, kaeltemittelarme Systeme |

---

### Kreislaufwirtschaftsgesetz (KrWG)

**Definition:** Das KrWG ist das zentrale Abfallgesetz in Deutschland. Es regelt die Vermeidung, Verwertung und Beseitigung von Abfaellen und setzt die EU-Abfallrahmenrichtlinie um.

**Kernaussagen:**
- Legt die **Abfallhierarchie** gesetzlich fest (5-stufig)
- Erzeuger und Besitzer von Abfaellen sind zu ordnungsgemaesser Entsorgung verpflichtet
- Gefaehrliche Abfaelle unterliegen strengeren Nachweispflichten

**Abfallhierarchie nach §6 KrWG:**

| Rang | Stufe | Beschreibung | IT-Beispiel |
|------|-------|-------------|-------------|
| 1 | Vermeidung | Abfall gar nicht erst entstehen lassen | Papierloses Buero, langlebige Hardware |
| 2 | Wiederverwendung | Produkt erneut fuer gleichen Zweck nutzen | Refurbishment von Notebooks |
| 3 | Recycling | Rohstoffe zurueckgewinnen | Kupfer aus Kabeln, Gold aus Leiterplatten |
| 4 | Sonstige Verwertung | Energetische Verwertung | Verbrennung mit Energierueckgewinnung |
| 5 | Beseitigung | Endgueltige Entsorgung (Deponie) | Letzte Option – moeglichst vermeiden |

---

### Verpackungsgesetz (VerpackG) und Duales System

**Definition:** Das VerpackG regelt die Verantwortung von Herstellern und Vertreibern fuer die Entsorgung von Verpackungen. Das Duale System (z.B. Gruener Punkt) organisiert die Sammlung und Verwertung.

**Kernaussagen:**
- Hersteller, die Verpackungen in Verkehr bringen, muessen sich an einem **dualen System** beteiligen
- Registrierung bei der **Zentralen Stelle Verpackungsregister (LUCID)** ist Pflicht
- Systembeteiligungspflichtig sind: Verkaufsverpackungen, Umverpackungen, Versandverpackungen
- IT-Haendler, die Hardware versenden, muessen ihre Verpackungen lizenzieren

**Wichtige Begriffe:**

| Begriff | Erklaerung |
|---------|-----------|
| Duales System | Privatwirtschaftlich organisierte Verpackungsentsorgung parallel zur kommunalen Entsorgung |
| Gruener Punkt | Bekanntestes Zeichen des Dualen Systems (heute: Der Gruene Punkt – DSD GmbH) |
| LUCID | Zentrale Stelle Verpackungsregister – Registrierungspflicht fuer alle Erstinverkehrbringer |
| Systembeteiligungspflicht | Pflicht, Verpackungen bei einem dualen System zu lizenzieren |
| EPR | Extended Producer Responsibility – erweiterte Herstellerverantwortung |

**IT-Relevanz:**
- IT-Haendler, die Hardware in Kartons versenden → Versandverpackungen sind systembeteiligungspflichtig
- Softwareunternehmen mit physischem Datentraeger in Verpackung → systembeteiligungspflichtig
- Reine Dienstleister ohne Verpackungsversand → normalerweise nicht betroffen

---

## Vertiefung

### Zusammenspiel der Gesetze

```
                    KrWG
                 (Abfallrecht)
                /      |       \
               /       |        \
          ElektroG   GewAbfV   VerpackG
         (E-Schrott) (Gewerbe-  (Verpackungen)
                      abfall)
              \        |        /
               \       |       /
                Betrieb / IT-Unternehmen
                       |
                  BImSchG + TA Laerm/Luft
                  (Laerm, Emissionen)
```

### Vergleich: Wichtige Umweltgesetze

| Gesetz | Schutzgut | IT-Relevanz | Sanktionen |
|--------|-----------|-------------|------------|
| BImSchG | Luft, Laermschutz | Klimaanlagen, Notstromgeneratoren | Bussgeld bis 50.000 EUR, Betriebsuntersagung |
| KrWG | Abfallvermeidung/-verwertung | Alle Abfallarten im IT-Betrieb | Bussgeld bis 100.000 EUR |
| ElektroG | Elektroschrott-Recycling | Hardware-Entsorgung/-Ruecknahme | Bussgeld bis 100.000 EUR |
| VerpackG | Verpackungsentsorgung | Versand von IT-Hardware | Bussgeld bis 200.000 EUR, Vertriebsverbot |
| BattG | Batterieentsorgung | USV-Batterien, Akkus | Bussgeld bis 100.000 EUR |

### Typische Pruefungsaspekte

- Zuordnung von Umweltproblemen zum korrekten Gesetz
- Abfallhierarchie nach KrWG in der richtigen Reihenfolge benennen
- Erklaerung des Dualen Systems und der Systembeteiligungspflicht
- TA-Laerm-Werte fuer verschiedene Gebietstypen kennen
- Wissen, wann ein IT-Unternehmen vom VerpackG betroffen ist

### Haeufige Fehler

| Fehler | Richtigstellung |
|--------|----------------|
| TA Laerm ist ein Gesetz | TA Laerm ist eine Verwaltungsvorschrift zum BImSchG |
| Das KrWG gilt nur fuer Industriebetriebe | Das KrWG gilt fuer alle Abfallerzeuger, auch Bueros und IT-Betriebe |
| Gruener Punkt bedeutet, dass die Verpackung recycelt wird | Der Gruene Punkt zeigt nur die Beteiligung am Dualen System an |
| Nur Hersteller muessen sich bei LUCID registrieren | Auch Importeure und Online-Haendler sind Erstinverkehrbringer |
| VerpackG betrifft keine Softwareunternehmen | Wer physische Produkte in Verpackungen versendet, ist betroffen |

---

## Uebungen

**Aufgabe 1:** Ein IT-Systemhaus betreibt ein kleines Rechenzentrum in einem Mischgebiet. Die Klimaanlage erzeugt nachts 48 dB(A) an der naechsten Wohnbebauung. Liegt ein Verstoss gegen die TA Laerm vor? Begruende.

**Aufgabe 2:** Nenne die fuenf Stufen der Abfallhierarchie nach KrWG in der richtigen Reihenfolge. Gib zu jeder Stufe ein IT-Beispiel.

**Aufgabe 3:** Ein Online-Shop verkauft gebrauchte, aufbereitete Notebooks und versendet diese in Kartons. Welche Pflichten ergeben sich aus dem VerpackG?

**Aufgabe 4:** Erklaere den Unterschied zwischen Emission und Immission anhand eines Beispiels aus dem IT-Bereich.

**Aufgabe 5:** Ordne die folgenden Situationen dem jeweils zutreffenden Gesetz zu:
- a) Entsorgung alter Monitore
- b) Laerm durch ein Notstromaggregat
- c) Versand von Notebooks in Kartonverpackung
- d) Entsorgung von USV-Akkus
- e) Getrennte Sammlung von Tonerkartuschen im Buero

---
---

# Loesungen

## Aufgabe 1
**Ja, es liegt ein Verstoss vor.** Der Immissionsrichtwert der TA Laerm fuer ein Mischgebiet betraegt nachts (22–6 Uhr) **45 dB(A)**. Mit 48 dB(A) wird der Grenzwert um 3 dB(A) ueberschritten. Das IT-Systemhaus muss Massnahmen ergreifen, z.B. leisere Klimatechnik, Schalldaemmung oder Einschraenkung des Nachtbetriebs.

## Aufgabe 2
1. **Vermeidung:** Papierloses Buero – keine Ausdrucke erzeugen
2. **Wiederverwendung:** Refurbishment – alte Notebooks aufbereiten und weitergeben
3. **Recycling:** Kupfer aus alten Netzwerkkabeln zurueckgewinnen
4. **Sonstige Verwertung:** Nicht recycelbare Kunststoffteile energetisch verwerten (Verbrennung mit Energierueckgewinnung)
5. **Beseitigung:** Deponierung von nicht verwertbaren Reststoffen (letzte Option)

## Aufgabe 3
Pflichten nach VerpackG:
1. **Registrierung bei LUCID** (Zentrale Stelle Verpackungsregister) als Erstinverkehrbringer
2. **Systembeteiligung:** Lizenzierung der Versandverpackungen (Kartons, Fuellmaterial, Klebeband) bei einem dualen System
3. **Datenmeldung:** Jaehrliche Meldung der in Verkehr gebrachten Verpackungsmengen an LUCID und an das duale System
4. **Kennzeichnung** der Verpackungsmaterialien zur korrekten Entsorgung

## Aufgabe 4
- **Emission:** Der Ausstoss an der Quelle. Beispiel: Ein Diesel-Notstromaggregat im Rechenzentrum stoesst Stickoxide aus dem Auspuff aus → **Emission** am Aggregat.
- **Immission:** Die Einwirkung auf die Umgebung. Beispiel: Die Stickoxide aus dem Aggregat erreichen die umliegende Wohnbebauung und beeintraechtigen die Luftqualitaet → **Immission** beim Empfaenger.

## Aufgabe 5
- a) Entsorgung alter Monitore → **ElektroG** (Elektro- und Elektronikgeraetegesetz)
- b) Laerm durch Notstromaggregat → **BImSchG** / **TA Laerm**
- c) Versand von Notebooks in Kartons → **VerpackG** (Verpackungsgesetz)
- d) Entsorgung von USV-Akkus → **BattG** (Batteriegesetz)
- e) Getrennte Sammlung von Tonerkartuschen → **GewAbfV** (Gewerbeabfallverordnung) / **KrWG**
