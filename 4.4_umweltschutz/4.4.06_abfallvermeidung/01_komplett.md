# Komplett: 4.4.06 – Abfallvermeidung und -reduzierung

## Einordnung

- **Pruefungsteil:** 4.4 – Umweltschutz
- **Thema-ID:** 4.4.06
- **Thema:** Abfallvermeidung und -reduzierung

## Ziel

Du musst das Konzept der Kreislaufwirtschaft und die Abfallhierarchie kennen und auf IT-Betriebe anwenden koennen. Digitalisierung als Werkzeug zur Abfallreduzierung ist ein zentraler Pruefungsaspekt.

## Themenkreise

KEIN THEMENKREIS ANGEGEBEN – Inhalt ergibt sich aus dem Pruefungskatalog-Thema.

## Querverweise

- Thema 4.4.01: Umweltbelastungen (Green IT, Recycling)
- Thema 4.4.02: Umgang mit Abfaellen (Erfassung, Entsorgung)
- Thema 4.4.03: Oeffentliche Systeme (KrWG, Abfallhierarchie)
- Thema 4.4.05: Umweltschonende Ressourcennutzung (papierloses Buero)

---

## Grundlagen

### Kreislaufwirtschaft

**Definition:** Die Kreislaufwirtschaft (Circular Economy) ist ein Wirtschaftsmodell, bei dem Produkte, Materialien und Ressourcen so lange wie moeglich im Kreislauf gehalten werden. Ziel ist die Minimierung von Abfall und Rohstoffverbrauch.

**Kernaussagen:**
- Gegenteil der **Linearwirtschaft** (Produzieren → Nutzen → Wegwerfen)
- Gesetzliche Grundlage in Deutschland: **Kreislaufwirtschaftsgesetz (KrWG)**
- Zentrales Prinzip: Abfall ist Rohstoff fuer neue Produkte
- Die EU verfolgt mit dem **Circular Economy Action Plan** (2020) eine umfassende Strategie

**Kreislaufwirtschaft vs. Linearwirtschaft:**

```
Linearwirtschaft (Take-Make-Dispose):

  Rohstoffe → Herstellung → Nutzung → Abfall (Deponie/Verbrennung)


Kreislaufwirtschaft (Circular Economy):

  Rohstoffe → Herstellung → Nutzung ─┐
       ^                               |
       |    Wiederverwendung ←─────────┤
       |                               |
       └─── Recycling ←───────────────┘
```

### Abfallhierarchie nach KrWG (§6)

**Definition:** Die Abfallhierarchie legt die Rangfolge der Massnahmen im Umgang mit Abfaellen fest. Vermeidung hat hoechste Prioritaet, Beseitigung die niedrigste.

**Fuenf Stufen:**

| Rang | Stufe | Beschreibung | IT-Beispiel |
|------|-------|-------------|-------------|
| 1 | **Vermeidung** | Abfall gar nicht erst entstehen lassen | Papierloses Buero, Cloud statt physischer Datentraeger |
| 2 | **Vorbereitung zur Wiederverwendung** | Produkt pruefen, reinigen, reparieren | Refurbishment von Notebooks, Reparatur statt Neukauf |
| 3 | **Recycling** | Rohstoffe aus Abfall zurueckgewinnen | Kupfer aus Kabeln, Gold aus Leiterplatten |
| 4 | **Sonstige Verwertung** | Energetische oder stoffliche Verwertung | Verbrennung mit Energierueckgewinnung |
| 5 | **Beseitigung** | Endgueltige Entsorgung | Deponie (letzte Option) |

**Merksatz:** **V**eronika **W**ill **R**ote **V**eilchen **B**ringen  
(Vermeidung → Wiederverwendung → Recycling → Verwertung → Beseitigung)

---

### Abfallvermeidung im IT-Betrieb

**Massnahmen nach Bereichen:**

| Bereich | Massnahme | Erwartete Wirkung |
|---------|-----------|-------------------|
| Papier | Papierloses Buero (DMS, digitale Workflows) | Papierverbrauch um 80-90% reduzieren |
| Papier | Duplexdruck als Standard, Follow-Me-Print | 50% Papierersparnis, weniger Fehldrucke |
| Hardware | Lebensdauer verlaengern (Reparatur, Upgrade statt Neukauf) | Weniger Elektroschrott |
| Hardware | Thin Clients statt Desktop-PCs | Weniger Hardware, laengere Lebensdauer |
| Hardware | Leasing-Modelle mit Ruecknahme | Hersteller kuemmert sich um Wiederverwendung |
| Verpackung | Mehrwegverpackungen bei interner Logistik | Weniger Karton- und Folienabfall |
| Verpackung | Lieferanten auf reduzierte Verpackung ansprechen | Weniger Verpackungsabfall |
| Datentraeger | Cloud-Speicher statt physische Datentraeger | Keine physischen Medien zu entsorgen |
| Toner | Nachfuellbare Tonerkartuschen | Weniger Plastikabfall |
| Toner | Tonersparmodus nutzen | Laengere Lebensdauer der Kartusche |
| Allgemein | Schulung der Mitarbeiter zum Thema Abfallvermeidung | Bewusstsein schaffen, Verhalten aendern |

---

### Digitalisierung zur Abfallreduzierung

**Definition:** Digitalisierung kann zur Abfallreduzierung beitragen, indem physische Materialien durch digitale Loesungen ersetzt werden.

**Wichtige Konzepte:**

| Konzept | Beschreibung | Effekt auf Abfall |
|---------|-------------|-------------------|
| Dokumentenmanagementsystem (DMS) | Digitale Archivierung, Versionskontrolle, Suchfunktion | Papierarchive entfallen |
| Elektronische Signatur | Rechtsverbindliche digitale Unterschrift (eIDAS) | Vertraege muessen nicht gedruckt werden |
| Digitale Rechnungsstellung | E-Rechnung statt Papierrechnung | Papier- und Portoersparnis |
| Cloud Computing | Daten und Anwendungen in der Cloud | Weniger lokale Hardware und Datentraeger |
| Videokonferenzen | Meetings ohne Reise | Weniger Reiseabfall, weniger gedruckte Unterlagen |
| Digitale Notizen | Tablets/Apps statt Notizzettel | Weniger Papierabfall |

**Achtung – Rebound-Effekt:** Digitalisierung erzeugt auch Abfall und Energieverbrauch:
- Server und Netzwerkinfrastruktur haben eine begrenzte Lebensdauer
- Cloud-Dienste verbrauchen Strom (siehe PUE-Wert, Thema 4.4.01)
- Haeufigere Hardware-Erneuerungszyklen durch wachsende Anforderungen

---

## Vertiefung

### Circular Economy in der IT – Praktisches Modell

```
                    Design fuer Langlebigkeit
                    und Reparierbarkeit
                           |
                           v
    ┌──── Rohstoff-  ←── Recycling ←──┐
    |     gewinnung                     |
    v                                   |
  Herstellung                    Sammlung und
    |                            Zerlegung
    v                                   ^
  Vertrieb                              |
    |                                   |
    v                                   |
  Nutzung ──→ Reparatur ──→ Refurbishment
    |              ^              |
    |              |              v
    └──────── Upgrade ←── Wiederverkauf
```

### Vergleich: Linearwirtschaft vs. Kreislaufwirtschaft

| Aspekt | Linearwirtschaft | Kreislaufwirtschaft |
|--------|-----------------|-------------------|
| Rohstoffbedarf | Hoch (staendig neues Material) | Reduziert (Material im Kreislauf) |
| Abfallmenge | Hoch | Minimiert |
| Produktdesign | Kostenoptimiert | Langlebig, reparierbar, zerlegbar |
| Geschaeftsmodell | Verkauf | Leasing, Product-as-a-Service |
| Kosten langfristig | Steigend (Rohstoffknappheit) | Stabil (Wiederverwendung) |
| Umweltbelastung | Hoch | Gering |

### Beispiel: Lebenszyklus eines Notebooks

**Lineares Modell:**
Herstellung → 3 Jahre Nutzung → Entsorgung als E-Waste

**Kreislaufmodell:**
Herstellung (modulares Design) → 3 Jahre Erstnutzung → Upgrade (SSD, RAM) → 2 Jahre Zweitnutzung → Refurbishment → 2 Jahre Drittnutzung → Recycling (Rohstoffrueckgewinnung) → Herstellung neuer Produkte

→ Statt 3 Jahre Lebensdauer: **7+ Jahre Nutzung**

### Typische Pruefungsaspekte

- Abfallhierarchie in der richtigen Reihenfolge benennen und auf IT beziehen
- Massnahmen zur Abfallvermeidung im IT-Betrieb vorschlagen
- Kreislaufwirtschaft erklaeren und von Linearwirtschaft abgrenzen
- Digitalisierung als Werkzeug zur Abfallreduzierung beschreiben
- Rebound-Effekt der Digitalisierung erkennen

### Haeufige Fehler

| Fehler | Richtigstellung |
|--------|----------------|
| Recycling steht an erster Stelle der Abfallhierarchie | Vermeidung steht an erster Stelle (§6 KrWG) |
| Kreislaufwirtschaft = Recycling | Kreislaufwirtschaft umfasst den gesamten Lebenszyklus, nicht nur die Entsorgungsphase |
| Digitalisierung erzeugt keinen Abfall | Auch digitale Infrastruktur hat einen Lebenszyklus und erzeugt Abfall |
| Papierloses Buero ist nicht realisierbar | Viele Unternehmen haben den Papierverbrauch um 80-90% gesenkt |
| Abfallvermeidung ist nur eine Kostenfrage | Abfallvermeidung ist gesetzlich priorisiert (KrWG) und oekologisch notwendig |

---

## Uebungen

**Aufgabe 1:** Nenne die fuenf Stufen der Abfallhierarchie nach KrWG und ordne jeder Stufe eine IT-spezifische Massnahme zu.

**Aufgabe 2:** Ein IT-Unternehmen mit 50 Mitarbeitern verbraucht jaehrlich 500.000 Blatt Papier. Entwickle einen Plan zur Reduktion des Papierverbrauchs um mindestens 70%. Nenne konkrete Massnahmen.

**Aufgabe 3:** Erklaere den Unterschied zwischen Kreislaufwirtschaft und Linearwirtschaft. Warum ist die Kreislaufwirtschaft speziell fuer die IT-Branche relevant?

**Aufgabe 4:** Ein Notebook-Hersteller moechte sein Produkt nach dem Prinzip der Kreislaufwirtschaft gestalten. Welche Design-Entscheidungen sollte er treffen?

**Aufgabe 5:** Erklaere anhand eines IT-Beispiels, warum Digitalisierung nicht automatisch zu weniger Abfall fuehrt (Rebound-Effekt).

---
---

# Loesungen

## Aufgabe 1
1. **Vermeidung:** Papierloses Buero einfuehren – digitale Workflows statt Ausdrucke
2. **Vorbereitung zur Wiederverwendung:** Refurbishment alter Notebooks – pruefen, reparieren, aufbereiten fuer Wiederverkauf
3. **Recycling:** Alte Netzwerkkabel sammeln und Kupfer zurueckgewinnen
4. **Sonstige Verwertung:** Nicht recycelbare Kunststoffgehaeuse energetisch verwerten (Verbrennung mit Energierueckgewinnung)
5. **Beseitigung:** Deponierung nicht verwertbarer Reste (letzte Option, moeglichst vermeiden)

## Aufgabe 2
**Ziel:** Reduktion von 500.000 auf maximal 150.000 Blatt (−70%)

Massnahmen:
1. **DMS einfuehren:** Alle internen Dokumente digital archivieren und verteilen (Ersparnis: ca. 150.000 Blatt)
2. **Digitale Rechnungsstellung:** E-Rechnungen statt Papierrechnungen (Ersparnis: ca. 50.000 Blatt)
3. **Duplexdruck als Standard:** Alle Drucker auf beidseitigen Druck konfigurieren (Ersparnis: ca. 75.000 Blatt)
4. **Follow-Me-Print:** Druckauftraege nur bei Authentifizierung am Drucker ausfuehren → Fehldrucke eliminieren (Ersparnis: ca. 30.000 Blatt)
5. **Digitale Signaturen:** Vertraege und Freigaben elektronisch unterschreiben (Ersparnis: ca. 20.000 Blatt)
6. **Tablet/Notebook in Meetings:** Keine gedruckten Meeting-Unterlagen mehr (Ersparnis: ca. 25.000 Blatt)

Gesamt: ca. 350.000 Blatt Ersparnis = 70% Reduktion

## Aufgabe 3
**Linearwirtschaft:** Rohstoffe werden abgebaut, zu Produkten verarbeitet, genutzt und dann als Abfall entsorgt. Es handelt sich um einen einseitigen Fluss von Ressourcen.

**Kreislaufwirtschaft:** Produkte und Materialien werden so lange wie moeglich im Kreislauf gehalten. Nach der Nutzung werden Produkte repariert, wiederverwendet oder ihre Rohstoffe zurueckgewonnen.

**Relevanz fuer die IT-Branche:**
- IT-Hardware enthaelt wertvolle und knappe Rohstoffe (Seltene Erden, Gold, Kobalt)
- Der Abbau dieser Rohstoffe ist umweltschaedlich und sozial problematisch
- Durch Refurbishment, Recycling und modulares Design koennen Rohstoffe laenger genutzt werden
- Schnelle Innovationszyklen in der IT fuehren zu viel E-Waste → Kreislaufwirtschaft als Gegenkonzept

## Aufgabe 4
Design-Entscheidungen fuer Kreislaufwirtschaft:
1. **Modularer Aufbau:** RAM, SSD, Akku, Display einzeln austauschbar
2. **Standardisierte Schrauben:** Keine Speziallwerkzeuge oder verklebten Teile
3. **Langlebige Materialien:** Aluminium-Gehaeuse statt kurzlebigem Plastik
4. **Software-Support:** Mindestens 5–7 Jahre Updates und Sicherheitspatches
5. **Reparaturanleitungen:** Oeffentlich zugaengliche Reparaturhandbuecher und Ersatzteile
6. **Recyclingfaehige Materialien:** Leicht trennbare, sortenreine Kunststoffe und Metalle
7. **Ruecknahmeprogramm:** Hersteller nimmt alte Geraete zurueck und fuehrt sie dem Refurbishment oder Recycling zu

## Aufgabe 5
**Beispiel: Einfuehrung eines Dokumentenmanagementsystems (DMS)**

Direkt: Das DMS ersetzt Papierausdrucke – der Papierverbrauch sinkt um 80%.

**Rebound-Effekte:**
- Die Mitarbeiter drucken trotzdem, weil sie Dokumente "zur Sicherheit" ausdrucken (Verhaltens-Rebound)
- Durch die einfache Verfuegbarkeit werden mehr Dokumente erstellt als zuvor (Effizienz-Rebound)
- Das DMS laeuft auf Servern, die Strom verbrauchen – bei wachsendem Datenvolumen steigt der Energieverbrauch
- Fuer das DMS werden neue Server, Speicher und Netzwerkkomponenten beschafft, die irgendwann selbst Abfall werden

→ Die Nettobilanz ist trotzdem positiv, aber der Effekt ist geringer als erwartet. Deshalb muessen Vermeidungsstrategien auch im digitalen Bereich greifen (z.B. Datensparsamkeit, regelmaessiges Loeschen nicht mehr benoetigter Daten).
