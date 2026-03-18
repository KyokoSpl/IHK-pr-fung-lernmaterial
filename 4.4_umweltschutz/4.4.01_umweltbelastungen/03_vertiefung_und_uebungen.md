# Vertiefung und Uebungen: 4.4.01 – Umweltbelastungen wahrnehmen und vermeiden helfen

## Vertiefung

### Green IT – Massnahmen im Ueberblick

| Bereich | Massnahme | Wirkung |
|---------|-----------|---------|
| Arbeitsplatz | Energiesparmodus aktivieren, Monitor abschalten | Stromverbrauch senken |
| Arbeitsplatz | Thin Clients statt Desktop-PCs | Bis zu 80% weniger Energieverbrauch am Arbeitsplatz |
| Drucken | Duplexdruck, Follow-Me-Print | Papierverbrauch und Fehldrucke reduzieren |
| Beschaffung | Energy-Star-/EPEAT-zertifizierte Geraete | Energieeffiziente Hardware |
| Rechenzentrum | Virtualisierung, Konsolidierung | Weniger physische Server, geringerer Energieverbrauch |
| Rechenzentrum | Free Cooling, Warmgang-/Kaltgang-Einhausung | Kuehlenergie reduzieren |
| Entsorgung | Refurbishment, zertifiziertes Recycling | Ressourcenschonung, weniger E-Waste |

### PUE-Wert – Einordnung

```
PUE-Wert     Bewertung
-----------  -----------------------
1,0          Ideal (theoretisches Maximum)
1,0 – 1,2   Sehr effizient (moderne Rechenzentren)
1,2 – 1,5   Gut (State of the Art)
1,5 – 2,0   Verbesserungspotenzial
> 2,0        Ineffizient
```

### Vergleich: Speichermedien vs. Printmedien

| Kriterium | Digitale Speicherung | Printmedien |
|-----------|---------------------|-------------|
| Ressourcenverbrauch | Strom, Speichermedien | Papier, Toner, Tinte |
| Umweltbelastung Herstellung | Energieintensiv (Server, Cloud) | Holzverarbeitung, Chemikalien |
| Langzeitarchivierung | Abhaengig von Technik und Format | Langlebig bei richtiger Lagerung |
| Zugriff | Schnell, ortsunabhaengig | Physisch gebunden |
| Entsorgung | Datentraegervernichtung noetig | Altpapier-Recycling |

### Typische Pruefungsaspekte

- Massnahmen zur Reduzierung des Energieverbrauchs in IT-Betrieben benennen
- PUE-Wert berechnen und interpretieren
- Vorteile von Virtualisierung fuer den Umweltschutz erklaeren
- Unterschied zwischen Vermeidung und Verwertung von IT-Abfaellen
- Pflichten nach ElektroG kennen (Herstellerruecknahme, Sammelstellen)

### Haeufige Fehler

| Fehler | Richtigstellung |
|--------|----------------|
| Green IT bezieht sich nur auf Recycling | Green IT umfasst den gesamten Lebenszyklus: Beschaffung, Nutzung, Entsorgung |
| PUE = 2,0 bedeutet doppelt so effizient | PUE = 2,0 bedeutet: 50% der Energie geht fuer Infrastruktur (Kuehlung etc.) drauf |
| USV-Batterien koennen im Restmuell entsorgt werden | USV-Batterien sind Sondermuell und muessen fachgerecht entsorgt werden |
| Digitalisierung ist immer umweltfreundlicher als Drucken | Digitale Infrastruktur verbraucht ebenfalls Energie – Gesamtbilanz betrachten |
| ElektroG gilt nur fuer Privatkunden | ElektroG gilt fuer alle Endnutzer – auch Unternehmen koennen Altgeraete zurueckgeben |

---

## Uebungen

**Aufgabe 1:** Ein Rechenzentrum verbraucht jaehrlich 800.000 kWh Gesamtenergie. Davon entfallen 500.000 kWh auf die IT-Geraete. Berechne den PUE-Wert und bewerte das Ergebnis.

**Aufgabe 2:** Nenne fuenf konkrete Massnahmen, mit denen ein IT-Systemhaus seinen Energieverbrauch senken kann. Ordne jede Massnahme einem Bereich zu (Arbeitsplatz, Rechenzentrum, Beschaffung).

**Aufgabe 3:** Erklaere, warum USV-Anlagen ein spezifisches Umweltrisiko darstellen. Welche gesetzliche Regelung greift bei der Entsorgung?

**Aufgabe 4:** Ein Unternehmen moechte 200 alte Notebooks entsorgen. Beschreibe den korrekten Entsorgungsweg unter Beruecksichtigung des ElektroG.

**Aufgabe 5:** Erklaere den Unterschied zwischen Refurbishment und Recycling. Welche Variante ist aus Umweltsicht vorzuziehen und warum?

**Aufgabe 6:** Nenne drei Vorteile der Virtualisierung im Hinblick auf den Umweltschutz.

---
---

# Loesungen

## Aufgabe 1
PUE = 800.000 kWh / 500.000 kWh = **1,6**

Bewertung: Der Wert liegt im Bereich "Verbesserungspotenzial" (1,5–2,0). Fuer jede kWh IT-Nutzung werden zusaetzlich 0,6 kWh fuer Infrastruktur (Kuehlung, USV, Beleuchtung) verbraucht. Massnahmen wie Free Cooling oder Kaltgang-/Warmgang-Einhausung koennten den Wert verbessern.

## Aufgabe 2
1. **Arbeitsplatz:** Energiesparmodi auf allen Arbeitsplatz-PCs aktivieren (automatischer Standby nach 10 Minuten)
2. **Arbeitsplatz:** Thin Clients statt herkoemmlicher Desktop-PCs einsetzen
3. **Rechenzentrum:** Server durch Virtualisierung konsolidieren – weniger physische Hardware
4. **Rechenzentrum:** Free Cooling nutzen – Aussenluft statt Klimaanlage in kuehlen Monaten
5. **Beschaffung:** Nur Geraete mit Energy-Star- oder EPEAT-Zertifizierung einkaufen

## Aufgabe 3
USV-Anlagen enthalten Blei-Saeure- oder Lithium-Ionen-Batterien. Diese sind Sondermuell, da sie Schwermetalle (Blei) und andere umweltgefaehrdende Stoffe enthalten. Bei unsachgemaesser Entsorgung koennen Schadstoffe in Boden und Grundwasser gelangen. Die Entsorgung ist im **Batteriegesetz (BattG)** geregelt. Hersteller und Vertreiber sind zur Ruecknahme verpflichtet. Zusaetzlich greift das **ElektroG** fuer die USV-Anlage als Gesamtgeraet.

## Aufgabe 4
1. **Datensicherheit:** Zunaechst alle Datentraeger sicher loeschen oder physisch vernichten (DIN 66399)
2. **Rueckgabe an Hersteller:** Pruefen, ob der Hersteller ein Ruecknahmeprogramm anbietet (Pflicht nach ElektroG)
3. **Kommunale Sammelstelle:** Alternativ Abgabe bei der oertlichen Sammelstelle (kostenfrei)
4. **Zertifizierter Entsorger:** Beauftragung eines zertifizierten Entsorgungsunternehmens mit Entsorgungsnachweis
5. **Refurbishment pruefen:** Vor Entsorgung pruefen, ob Geraete noch aufgearbeitet und weiterverwendet werden koennen

## Aufgabe 5
- **Refurbishment:** Gebrauchte Hardware wird geprueft, repariert, gereinigt und fuer den Wiederverkauf aufbereitet. Das Geraet bleibt als Ganzes erhalten.
- **Recycling:** Hardware wird zerlegt, Rohstoffe (Gold, Kupfer, Seltene Erden) werden zurueckgewonnen. Das Geraet wird dabei zerstoert.

Refurbishment ist aus Umweltsicht vorzuziehen, weil es der Wiederverwendung in der Abfallhierarchie entspricht (Stufe 2) und somit hoeherwertig ist als Recycling (Stufe 3). Es spart die Energie und Ressourcen, die fuer die Herstellung eines neuen Geraets noetig waeren.

## Aufgabe 6
1. **Weniger physische Server:** Mehrere virtuelle Maschinen laufen auf einem physischen Server → weniger Hardware, weniger Energieverbrauch
2. **Geringerer Kuehlbedarf:** Weniger Geraete erzeugen weniger Abwaerme → Kuehlenergie sinkt
3. **Bessere Ressourcenauslastung:** Physische Server werden oft nur zu 10-20% ausgelastet; Virtualisierung steigert die Auslastung auf 60-80% → effizienterer Betrieb
