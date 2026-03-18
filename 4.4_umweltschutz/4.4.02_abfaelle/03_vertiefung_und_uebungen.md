# Vertiefung und Uebungen: 4.4.02 – Umgang mit Abfaellen

## Vertiefung

### Entsorgungswege im IT-Betrieb – Uebersicht

| Abfallart | Entsorgungsweg | Rechtsgrundlage |
|-----------|---------------|-----------------|
| Tonerkartuschen (leer) | Rueckgabe an Hersteller oder Recycling-Dienstleister | VerpackG, ElektroG |
| Tonerkartuschen (mit Restinhalt) | Gefaehrlicher Abfall → zertifizierter Entsorger | GefStoffV, KrWG |
| USV-Batterien | Rueckgabe an Hersteller/Vertreiber | BattG |
| Monitore/Bildschirme | Kommunale Sammelstelle oder Herstellerruecknahme | ElektroG |
| Festplatten mit Daten | Datenvernichtung (DIN 66399) + Elektroschrott-Recycling | DSGVO, ElektroG |
| Netzwerkkabel | Kabelschrott → Kupfer-Recycling | KrWG |
| Leiterplatten | Elektroschrott → Edelmetallrueckgewinnung | ElektroG |
| Verpackungen | Gelber Sack/Tonne oder Duales System | VerpackG |

### DIN 66399 – Zuordnung Schutzklasse zu Sicherheitsstufe

```
Schutzklasse 1 (normal)      → Sicherheitsstufen 1, 2, 3
Schutzklasse 2 (hoch)        → Sicherheitsstufen 3, 4, 5
Schutzklasse 3 (sehr hoch)   → Sicherheitsstufen 5, 6, 7
```

**Pruefungsrelevant:** Die Mindest-Sicherheitsstufe fuer personenbezogene Daten (DSGVO) ist in der Regel **Stufe 3** (Schutzklasse 2).

### Vergleich: Loeschen vs. Vernichten

| Aspekt | Softwarebasiertes Loeschen | Physische Vernichtung |
|--------|---------------------------|----------------------|
| Methode | Ueberschreiben mit Zufallsdaten | Schreddern, Degaussing, Schmelzen |
| Datenwiederherstellung | Ab 1x Ueberschreiben praktisch unmoeglich (HDDs) | Vollstaendig ausgeschlossen |
| Geraet wiederverwendbar | Ja | Nein |
| Geeignet fuer SSDs | Eingeschraenkt (Wear Leveling) | Ja |
| Nachweis | Loeschprotokoll | Vernichtungsprotokoll |
| Kosten | Gering | Mittel bis hoch |

### WEEE-Kategorien fuer IT-Geraete

Die EU-WEEE-Richtlinie (umgesetzt durch ElektroG) teilt Elektrogeraete in Kategorien ein:

| Kategorie | Beispiele aus der IT |
|-----------|---------------------|
| 1 – Waermeuebertraeger | Serverschrank-Kuehlung (bestimmte Typen) |
| 2 – Bildschirme/Monitore | LCD-Monitore, CRT-Monitore, Laptops |
| 3 – Lampen | Hintergrundbeleuchtung (aeltere Displays) |
| 4 – Grossgeraete | Serverschraenke, grosse USV-Anlagen |
| 5 – Kleingeraete | Router, Switches, Tastaturen, Maeuse |
| 6 – Kleine IT-/Telekommunikationsgeraete | Smartphones, Tablets, USB-Sticks |

### Typische Pruefungsaspekte

- Zuordnung von IT-Abfaellen zum korrekten Entsorgungsweg
- DIN 66399: Schutzklasse und Sicherheitsstufe bestimmen
- Unterschied zwischen gefaehrlichem und nicht-gefaehrlichem Abfall
- Dokumentationspflichten (Registerpflicht, Entsorgungsnachweis)
- Zusammenhang Datenschutz und Datentraegerentsorgung

### Haeufige Fehler

| Fehler | Richtigstellung |
|--------|----------------|
| Formatieren genuegt zur sicheren Datenloeschung | Formatieren entfernt nur das Inhaltsverzeichnis – Daten sind wiederherstellbar |
| Alle IT-Abfaelle sind gefaehrlicher Abfall | Nur bestimmte Abfaelle (z.B. Batterien, Toner mit Restinhalt) gelten als gefaehrlich |
| Kabel koennen im Restmuell entsorgt werden | Kabel enthalten Kupfer und gehoeren zum Recycling |
| SSDs koennen durch Ueberschreiben sicher geloescht werden | Wegen Wear Leveling ist physische Vernichtung sicherer fuer SSDs |
| Entsorgungsnachweis ist freiwillig | Fuer gefaehrliche Abfaelle ist der Entsorgungsnachweis Pflicht |

---

## Uebungen

**Aufgabe 1:** Ein IT-Dienstleister tauscht bei einem Kunden 50 Festplatten aus. Die alten Festplatten enthalten personenbezogene Kundendaten (Schutzklasse 2). Welche Sicherheitsstufe nach DIN 66399 ist mindestens erforderlich? Welche Vernichtungsmethode empfiehlst du?

**Aufgabe 2:** Ordne die folgenden Abfaelle dem korrekten Entsorgungsweg zu:
- a) Leere Tonerkartuschen
- b) Defekte USV-Batterie (Blei-Saeure)
- c) Alte Cat5-Netzwerkkabel
- d) Kaputter LCD-Monitor
- e) Kartonverpackung eines neuen Servers

**Aufgabe 3:** Erklaere den Unterschied zwischen Registerpflicht und Entsorgungsnachweis. Fuer welche Abfallart ist der Entsorgungsnachweis zwingend erforderlich?

**Aufgabe 4:** Warum reicht softwarebasiertes Ueberschreiben bei SSDs nicht zuverlaessig aus? Welche Alternative gibt es?

**Aufgabe 5:** Ein Unternehmen lagert seit zwei Jahren defekte Monitore und alte Server in einem Kellerraum. Welche Probleme ergeben sich? Welche gesetzlichen Pflichten werden moeglicherweise verletzt?

---
---

# Loesungen

## Aufgabe 1
Bei Schutzklasse 2 (hoher Schutzbedarf – personenbezogene Daten) ist mindestens **Sicherheitsstufe 3** (besser Stufe 4 oder 5) erforderlich. Empfohlene Methode: **Physisches Schreddern** der Festplatten, da dies den Nachweis der unwiederbringlichen Vernichtung erleichtert. Alternativ: Softwarebasiertes Ueberschreiben mit mindestens einem Durchgang (bei HDDs) + Loeschprotokoll und anschliessendes Recycling.

## Aufgabe 2
- a) **Leere Tonerkartuschen:** Rueckgabe an Hersteller (Ruecknahmeprogramm) oder Recycling-Dienstleister fuer Tonerkartuschen
- b) **Defekte USV-Batterie:** Gefaehrlicher Abfall → Rueckgabe an den Vertreiber/Hersteller (BattG) oder Entsorgung ueber zertifizierten Entsorgungsfachbetrieb mit Begleitschein
- c) **Alte Netzwerkkabel:** Kabelschrott → Recyclingbetrieb (Kupferrueckgewinnung)
- d) **Kaputter LCD-Monitor:** Elektroschrott → kommunale Sammelstelle oder Herstellerruecknahme (ElektroG)
- e) **Kartonverpackung:** Verpackungsabfall → Altpapier/gelber Sack (VerpackG, Duales System)

## Aufgabe 3
- **Registerpflicht (§49 KrWG):** Alle Erzeuger, Befoerderer und Entsorger muessen Art, Menge, Herkunft und Verbleib von Abfaellen dokumentieren. Gilt fuer alle Abfaelle.
- **Entsorgungsnachweis:** Belegt den konkreten Entsorgungsweg im Voraus (Vorab-Genehmigung der Entsorgungsanlage). Ist zwingend erforderlich fuer **gefaehrliche Abfaelle** (z.B. Batterien mit Schwermetallen, Toner mit Restinhalt).

## Aufgabe 4
SSDs verwenden **Wear Leveling**, d.h. Daten werden nicht immer an derselben physischen Stelle gespeichert. Beim softwarebasierten Ueberschreiben koennen daher Datenfragmente in nicht adressierbaren Bereichen (Reserve-Bloecken) verbleiben. **Alternative:** Physische Vernichtung (Schreddern) oder Nutzung des herstellerspezifischen **Secure Erase**-Befehls (ATA Secure Erase), der alle Speicherzellen einschliesslich Reserve-Bloecke zuruecksetzt.

## Aufgabe 5
**Probleme:**
- Gefahr von Schadstofffreisetzung (Quecksilber in alten Monitoren, Blei in Loetverbindungen)
- Keine ordnungsgemaesse Entsorgung – Verstoss gegen **ElektroG** (Pflicht zur zeitnahen Entsorgung)
- Verstoss gegen **Registerpflicht** (§49 KrWG) – Abfaelle muessen erfasst und dokumentiert werden
- Moeglicherweise Verstoss gegen die **GewAbfV** (Pflicht zur getrennten Sammlung)
- Bei Datentraegern in den Servern: moeglicherweise **DSGVO-Verstoss**, wenn personenbezogene Daten nicht geloescht wurden
- **Brandgefahr** durch unsachgemaesse Lagerung von Lithium-Akkus
