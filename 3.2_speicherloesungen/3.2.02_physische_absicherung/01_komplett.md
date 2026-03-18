# Ueberblick und Grundlagen: 3.2.02 – Moeglichkeiten der physischen/hardwaretechnischen Absicherung

## Einordnung

- **Pruefungsteil:** 3.2 – Inbetriebnehmen von Speicherloesungen
- **Thema-ID:** 3.2.02
- **Thema:** Moeglichkeiten der physischen/hardwaretechnischen Absicherung benennen

## Ziel

Du musst physische Bedrohungen fuer IT-Infrastruktur kennen und geeignete Schutzmassnahmen benennen koennen. Der Schwerpunkt liegt auf Elementarrisiken und Zugangskontrollen fuer Gebaeude, Serverraeume und Serverschraenke.

## Themenkreise im Ueberblick

| Nr. | Themenkreis | Schwerpunkt |
|-----|-------------|-------------|
| 1 | Elementarrisiken (z.B. Feuer, Hochwasser) | Brandschutz, Wasserschutz, Klimatisierung, USV |
| 2 | Zugangskontrollen (z.B. Gebaeude, Serverraum, Schrank) | Physische Zutrittskontrollen auf mehreren Ebenen |

### Querverweise
- Thema 3.2.01: TOM – Zutritt, Zugang, Zugriff (Einordnung der Zutrittskontrollen)
- Thema 3.2.03: Softwaretechnische Absicherung (ergaenzende logische Schutzmassnahmen)
- Thema 3.1.01: IT-Sicherheitskonzepte und Risikoanalyse

---

## Grundlagen

### 1. Elementarrisiken

**Definition:** Elementarrisiken sind physische Gefahren, die IT-Infrastruktur zerstoeren oder deren Betrieb unterbrechen koennen. Sie werden auch als hoehere Gewalt oder Umgebungsrisiken bezeichnet.

**Kategorien von Elementarrisiken:**

| Risiko | Beschreibung | Schutzmassnahmen |
|--------|-------------|------------------|
| **Feuer/Brand** | Direkte Zerstoerung von Hardware und Datentraegern | Brandmeldeanlage, Gasloeschanlage (kein Wasser!), Brandabschnitte, feuerfeste Schraenke |
| **Wasser/Hochwasser** | Kurzschluesse, Korrosion, Datenverlust | Keine Server im Keller, Wassermelder, abgedichtete Kabeldurchfuehrungen |
| **Stromausfall** | Systemausfaelle, Datenverlust bei Schreibvorgaengen | USV (Unterbrechungsfreie Stromversorgung), Notstromaggregat, redundante Einspeisung |
| **Ueberhitzung** | Hardwaredefekte, verkuerzte Lebensdauer | Klimaanlage, Kalt-/Warmgang-Einhausung, Temperaturueberwachung |
| **Blitzschlag** | Ueberspannung, Zerstoerung elektronischer Bauteile | Blitzableiter, Ueberspannungsschutz, geschirmte Kabel |
| **Erdbeben/Sturm** | Mechanische Beschaedigung | Standortwahl, erdbebensichere Montage, redundante Standorte |
| **Staub/Schmutz** | Ueberhitzung durch verstopfte Luefter, Kurzschluesse | Staubfilter, regelmaessige Reinigung, geschlossene Schraenke |

**Wichtige Begriffe:**
- **USV (Unterbrechungsfreie Stromversorgung)** – ueberbrueckt kurze Stromausfaelle und ermoeglicht kontrolliertes Herunterfahren
- **Gasloeschanlage** – loescht Brand ohne Wasser (z.B. mit Argon oder Stickstoff), schuetzt empfindliche Hardware
- **Redundanz** – Vorhandensein von Ersatzsystemen oder -wegen bei Ausfall
- **Kalt-/Warmgang-Einhausung** – Trennung von kalter Zuluft und warmer Abluft im Rechenzentrum

**Erklaerung:** Im Serverraum wird niemals mit Wasser geloescht, da dies die Hardware zerstoert. Stattdessen kommen Gasloeschanlagen zum Einsatz, die den Sauerstoff verdraengen. Eine USV ueberbrueckt typischerweise 10–30 Minuten – genug Zeit fuer ein kontrolliertes Herunterfahren oder bis das Notstromaggregat anspringt.

---

### 2. Zugangskontrollen (Gebaeude, Serverraum, Schrank)

**Definition:** Physische Zugangskontrollen (im Sinne von Zutrittskontrollen) schuetzen IT-Infrastruktur durch stufenweise Absicherung auf mehreren Ebenen.

**Zonenkonzept:**

```
+------------------------------------------+
|  Zone 1: GELAENDE                        |
|  Zaun, Tor, Pfoertner, Kamera            |
|  +------------------------------------+  |
|  |  Zone 2: GEBAEUDE                  |  |
|  |  Schliessanlage, Chipkarte, Empfang|  |
|  |  +------------------------------+  |  |
|  |  |  Zone 3: SERVERRAUM          |  |  |
|  |  |  Biometrie, PIN, Protokoll   |  |  |
|  |  |  +------------------------+  |  |  |
|  |  |  |  Zone 4: SERVERSCHRANK |  |  |  |
|  |  |  |  Schloss, Sensor,      |  |  |  |
|  |  |  |  Zugriffsprotokoll     |  |  |  |
|  |  |  +------------------------+  |  |  |
|  |  +------------------------------+  |  |
|  +------------------------------------+  |
+------------------------------------------+
```

**Massnahmen nach Zone:**

| Zone | Objekt | Massnahmen |
|------|--------|-----------|
| Zone 1 | Gelaende | Zaun, Tor, Pfoertner, Aussenbeleuchtung, Videoueberwachung |
| Zone 2 | Gebaeude | Schliessanlage, Chipkarten, Empfang mit Besucherprotokoll |
| Zone 3 | Serverraum | Biometrischer Zugang, PIN-Code, Protokollierung aller Zutritte, Einbruchmeldeanlage |
| Zone 4 | Serverschrank | Schloss (Schluessel/Code), Tueroffnungssensor, Kamera |

**Anforderungen an einen Serverraum:**

| Kriterium | Anforderung |
|-----------|-------------|
| Lage | Nicht im Keller (Hochwassergefahr), nicht im Dachgeschoss (Hitze), keine Aussenfenster |
| Klimatisierung | Temperatur 18–24 °C, Luftfeuchtigkeit 40–60 % |
| Brandschutz | Gasloeschanlage, Rauchmelder, Brandschutztueren, feuerfeste Waende |
| Stromversorgung | Redundante Einspeisung, USV, Notstromaggregat |
| Zutrittskontrolle | Biometrie oder Chipkarte + PIN, Protokollierung |
| Ueberwachung | Temperatur-/Feuchtigkeitssensoren, Wassermelder, Kamera |

**Wichtige Begriffe:**
- **Zonenkonzept** – stufenweise Absicherung vom Gelaende bis zum Serverschrank
- **Biometrische Authentifizierung** – Identifikation anhand koerperlicher Merkmale (Fingerabdruck, Iris)
- **Brandabschnitt** – baulich abgetrennter Bereich, der die Ausbreitung von Feuer verhindert
- **Kensington Lock** – mechanische Diebstahlsicherung fuer Laptops und Geraete

---

## Vertiefung

### USV-Typen im Vergleich

| Typ | Bezeichnung | Funktionsweise | Umschaltzeit | Eignung |
|-----|-------------|---------------|-------------|---------|
| Offline/Standby | VFD | Schaltet bei Stromausfall auf Batterie um | 5–12 ms | Arbeitsplaetze |
| Line-Interactive | VI | Regelung ueber Autotransformator | 2–4 ms | Kleine Server |
| Online/Doppelwandler | VFI | Dauerhafte Versorgung ueber Batterie und Wechselrichter | 0 ms | Serverraeume, Rechenzentren |

### Pruefungsrelevante Szenarien

**Szenario 1:** Ein Unternehmen plant einen neuen Serverraum. Welche Anforderungen muessen erfuellt sein?
→ Klimatisierung, Brandschutz (Gasloeschanlage), USV + Notstrom, Zutrittskontrolle, Wassermelder, keine Fenster, nicht im Keller.

**Szenario 2:** Bei einem Stromausfall fallen alle Server aus. Welche Massnahme haette das verhindern koennen?
→ USV (Online-Typ fuer unterbrechungsfreie Versorgung) + Notstromaggregat fuer Langzeitversorgung.

### Typische Pruefungsaspekte
- Elementarrisiken benennen und passende Schutzmassnahmen zuordnen
- Anforderungen an einen Serverraum auflisten
- Zonenkonzept erklaeren
- USV-Typen unterscheiden

### Haeufige Fehler
- Wasserloeschanlage im Serverraum vorschlagen → Es muss eine **Gasloeschanlage** sein
- USV mit Notstromaggregat verwechseln: USV ueberbrueckt Sekunden bis Minuten, Notstromaggregat fuer Stunden
- Serverraum im Keller planen → Hochwassergefahr!
- Klimatisierung vergessen → Server produzieren viel Abwaerme, Ueberhitzung fuehrt zu Ausfaellen

---

## Uebungen

**Aufgabe 1:** Nenne fuenf Elementarrisiken und jeweils eine passende Schutzmassnahme.

**Aufgabe 2:** Erklaere das Zonenkonzept und nenne fuer jede Zone eine typische Schutzmassnahme.

**Aufgabe 3:** Welche Anforderungen muss ein professioneller Serverraum hinsichtlich Lage, Klimatisierung und Brandschutz erfuellen?

**Aufgabe 4:** Ein Unternehmen moechte eine USV fuer den Serverraum anschaffen. Erklaere den Unterschied zwischen Offline-USV und Online-USV. Welche ist fuer den Serverraum geeignet?

**Aufgabe 5:** Warum darf ein Serverraum keine Fenster haben und nicht im Keller liegen? Nenne jeweils die Begruendung.

---
---

# Loesungen

## Aufgabe 1

| Elementarrisiko | Schutzmassnahme |
|-----------------|-----------------|
| Feuer/Brand | Gasloeschanlage, Rauchmelder |
| Wasser/Hochwasser | Wassermelder, Server nicht im Keller |
| Stromausfall | USV + Notstromaggregat |
| Ueberhitzung | Klimaanlage, Kalt-/Warmgang-Einhausung |
| Blitzschlag | Ueberspannungsschutz, Blitzableiter |

## Aufgabe 2
Das Zonenkonzept beschreibt die stufenweise physische Absicherung von aussen nach innen:
- **Zone 1 (Gelaende):** Zaun und Videoueberwachung
- **Zone 2 (Gebaeude):** Chipkarten-Schliessanlage
- **Zone 3 (Serverraum):** Biometrischer Zugang mit Protokollierung
- **Zone 4 (Serverschrank):** Schloss mit Tueroffnungssensor

## Aufgabe 3
- **Lage:** Nicht im Keller (Hochwasser), nicht im Dachgeschoss (Hitze), keine Aussenfenster (Einbruch, Sonneneinstrahlung)
- **Klimatisierung:** Temperatur 18–24 °C, Luftfeuchtigkeit 40–60 %, Kalt-/Warmgang-Trennung
- **Brandschutz:** Gasloeschanlage (kein Wasser!), Rauchmelder, Brandschutztueren, feuerfeste Waende

## Aufgabe 4
- **Offline-USV:** Schaltet erst bei Stromausfall auf Batterie um. Umschaltzeit 5–12 ms. Guenstig, aber fuer Server ungeeignet, da die Unterbrechung zu Datenverlust fuehren kann.
- **Online-USV (Doppelwandler):** Versorgt die Geraete dauerhaft ueber Batterie und Wechselrichter. Umschaltzeit 0 ms. Fuer Serverraeume geeignet, da keine Unterbrechung auftritt.

## Aufgabe 5
- **Keine Fenster:** Fenster ermoeglichen Einbruch, Sonneneinstrahlung fuehrt zu Aufheizung, Fenster sind Schwachstellen im Brandschutz.
- **Nicht im Keller:** Hochwasser- und Ueberschwemmungsgefahr. Eindringendes Wasser zerstoert Hardware und Datentraeger. Wasserrohrbrueche treten im Keller haeufiger auf.
