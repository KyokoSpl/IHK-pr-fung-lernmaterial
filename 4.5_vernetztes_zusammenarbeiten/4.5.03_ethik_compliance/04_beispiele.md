# 4.5.03 – Ethische Aspekte und Compliance-Regelungen: Beispiele

## Beispiel 1: KI-Bias im Recruiting-Tool

### Szenario

Die **HireTech GmbH** entwickelt ein KI-basiertes Bewerbungstool fuer IT-Unternehmen. Das Tool filtert Bewerbungen automatisch vor und erstellt ein Ranking der Kandidaten.

### Problem

Nach 6 Monaten Einsatz zeigt die Auswertung:
- 85% der empfohlenen Kandidaten sind maennlich
- Bewerber mit nicht-deutschen Namen werden 30% seltener empfohlen
- Bewerber ueber 50 Jahre werden systematisch niedriger bewertet

### Analyse

| Bias-Art | Ursache | Auswirkung |
|----------|---------|------------|
| Historischer Bias | Trainingsdaten basieren auf bisherigen Einstellungen (ueberwiegend maennlich) | Frauen werden benachteiligt |
| Repraesentations-Bias | Wenig Bewerber mit nicht-deutschen Namen in Trainingsdaten | Ethnische Diskriminierung |
| Proxy-Bias | Alter korreliert mit Technologie-Schlagworten im Lebenslauf | Altersdiskriminierung |

### Rechtliche Bewertung

| Aspekt | Bewertung |
|--------|-----------|
| AGG-Verstoss | Ja – Diskriminierung nach Geschlecht, ethnischer Herkunft, Alter |
| DSGVO Art. 22 | Automatisierte Einzelentscheidung – Betroffene haben Recht auf menschliche Ueberpruefung |
| Haftung | Unternehmen, das Tool einsetzt, haftet (nicht nur Hersteller) |
| EU AI Act | Hochrisiko-KI-System – besondere Anforderungen an Transparenz und Fairness |

### Loesungsmassnahmen

| Massnahme | Umsetzung |
|-----------|-----------|
| Daten-Audit | Trainingsdaten auf Repraesentativitaet pruefen und bereinigen |
| Fairness-Metriken | Gleichmaessige Empfehlungsrate ueber Geschlecht, Alter, Herkunft |
| Human in the Loop | Menschliche Endentscheidung bei jeder Bewerbung |
| Erklaerbare KI | Transparente Kriterien fuer Ranking offenlegen |
| Regelmaessiges Monitoring | Quartalsweise Bias-Analyse |
| Diverse Entwicklerteams | Verschiedene Perspektiven in der Entwicklung |

---

## Beispiel 2: Compliance-Verstoss und Whistleblowing

### Szenario

Entwickler Jonas arbeitet bei der **SecureData AG** (200 Mitarbeiter). Bei der Arbeit an einem Kundenprojekt entdeckt er, dass personenbezogene Kundendaten unverschluesselt auf einem oeffentlich zugaenglichen Server gespeichert werden. Sein Teamleiter sagt: "Das war schon immer so, lass das."

### Analyse

| Aspekt | Bewertung |
|--------|-----------|
| DSGVO-Verstoss | Ja – Art. 5 Abs. 1 lit. f (Integritaet und Vertraulichkeit) |
| Art. 32 DSGVO | Technische und organisatorische Massnahmen fehlen (Verschluesselung) |
| Meldepflicht (Art. 33) | Bei Datenpanne: 72h-Frist an Aufsichtsbehoerde |
| Bussgeld | Bis zu 20 Mio. EUR oder 4% des Jahresumsatzes |
| Teamleiter-Verhalten | Compliance-Verstoss durch Unterlassen |

### Jonas' Optionen nach HinSchG

| Option | Beschreibung | Empfehlung |
|--------|-------------|------------|
| 1. Interne Meldung | Meldung an interne Meldestelle / Compliance-Officer | Bevorzugt – gibt dem Unternehmen Chance zur Korrektur |
| 2. Eskalation | Wenn interne Meldung erfolglos: Meldung an Datenschutzbehoerde | Wenn nach 3 Monaten keine Reaktion |
| 3. Offenlegung | Oeffentlich machen (z.B. Presse) | Nur als letztes Mittel |

### Korrekter Ablauf

| Schritt | Handlung |
|---------|----------|
| 1 | Jonas dokumentiert den Befund (Screenshots, Logs) |
| 2 | Meldung an interne Meldestelle / Compliance-Officer / DSB |
| 3 | Eingangsbestaetigung innerhalb von 7 Tagen |
| 4 | Untersuchung durch Compliance-Abteilung |
| 5 | Rueckmeldung an Jonas innerhalb von 3 Monaten |
| 6 | Sofort-Massnahme: Server absichern, Daten verschluesseln |
| 7 | Langfristig: Prozesse anpassen, Schulungen durchfuehren |

### Jonas' Schutz

- Keine Kuendigung wegen der Meldung (Beweislastumkehr)
- Keine Versetzung, Degradierung oder Mobbing
- Vertraulichkeit seiner Identitaet wird gewahrt

---

## Beispiel 3: Barrierefreiheit bei einer Web-Anwendung

### Szenario

Die **WebAccess GmbH** entwickelt ein Online-Portal fuer eine Behoerde. Das Portal muss nach BITV 2.0 barrierefrei sein. Beim Audit werden folgende Maengel festgestellt:

### Maengelfeststellung

| Problem | WCAG-Prinzip | Konformitaetsstufe | Betroffene Gruppe |
|---------|-------------|-------------------|-------------------|
| Bilder ohne Alternativtexte | Wahrnehmbar (1.1.1) | A | Blinde (Screenreader) |
| Formulare nicht per Tastatur bedienbar | Bedienbar (2.1.1) | A | Motorisch eingeschraenkte Nutzer |
| Kontrastverhaealtnis < 4.5:1 | Wahrnehmbar (1.4.3) | AA | Sehbehinderte |
| Videos ohne Untertitel | Wahrnehmbar (1.2.2) | A | Gehoerlose / Schwerhoerige |
| Keine Fehlerhinweise in Formularen | Verstaendlich (3.3.1) | A | Kognitive Einschraenkungen |
| Keine Skip-Navigation | Bedienbar (2.4.1) | A | Screenreader-Nutzer |
| Bewegte Inhalte nicht pausierbar | Bedienbar (2.2.2) | A | Epilepsie, Konzentration |

### Korrekturmassnahmen

| Problem | Loesung | Aufwand |
|---------|---------|---------|
| Fehlende Alt-Texte | Alle Bilder mit aussagekraeftigen alt-Attributen versehen | Niedrig |
| Tastaturnavigation | Tab-Reihenfolge korrigieren, Focus-Styles hinzufuegen | Mittel |
| Kontrast | Farbschema anpassen, Contrast-Checker einsetzen | Niedrig |
| Untertitel | Captions fuer alle Videos erstellen | Mittel |
| Fehlerhinweise | ARIA-Attribute und sichtbare Fehlermeldungen | Niedrig |
| Skip-Navigation | Skip-Link am Seitenanfang einbauen | Niedrig |
| Bewegte Inhalte | Pause-Button fuer Animationen und Videos | Niedrig |

### Technische Umsetzung (Beispiel Alt-Text)

```
FALSCH:
<img src="dashboard.png">
<img src="dashboard.png" alt="Bild">
<img src="dashboard.png" alt="dashboard.png">

RICHTIG:
<img src="dashboard.png" alt="Dashboard-Uebersicht mit
Kennzahlen zu offenen Tickets, Bearbeitungszeit und
Kundenzufriedenheit">

DEKORATIVES BILD (kein Informationsgehalt):
<img src="zierlinie.png" alt="">
```

---

## Beispiel 4: Nachhaltige IT-Beschaffung

### Szenario

Die **EcoTech GmbH** (150 Mitarbeiter) moechte 50 neue Arbeitsplatz-PCs beschaffen. Die IT-Leitung soll eine nachhaltige Entscheidung treffen.

### Vergleich der Optionen

| Kriterium | Option A: Neue Standard-PCs | Option B: Refurbished Business-PCs | Option C: Thin Clients + Cloud |
|-----------|---------------------------|-----------------------------------|-------------------------------|
| Anschaffungskosten | 800 EUR/Stueck | 400 EUR/Stueck | 300 EUR/Stueck + Cloud-Kosten |
| Energieverbrauch | 150 W | 120 W (aeltere, aber effiziente HW) | 15 W + Serverenergie |
| Lebensdauer | 5 Jahre | 3-4 Jahre | 7+ Jahre (wenig Verschleiss) |
| CO2-Fussabdruck (Herstellung) | Hoch (neue Produktion) | Gering (Wiederverwendung) | Mittel |
| Reparierbarkeit | Mittel | Gut (Standard-Komponenten) | Gering (kaum Teile) |
| Leistung | Hoch | Mittel-Hoch | Abhaengig von Server/Cloud |
| Elektroschrott | In 5 Jahren | Verzoegert Entsorgung | Minimal |
| Nachhaltigkeitsbewertung | ★★☆☆☆ | ★★★★☆ | ★★★★★ (bei Oekostrom) |

### Empfehlung

| Nutzungsprofil | Empfohlene Option | Begruendung |
|----------------|-------------------|-------------|
| Entwickler (hohe Rechenleistung) | Option A mit Eco-Label | Leistung erforderlich, auf Blue Angel achten |
| Sachbearbeiter (Office, Web) | Option B oder C | Ausreichende Leistung, nachhaltig |
| Besprechungsraeume | Option C | Geringer Energieverbrauch, zentrale Verwaltung |

### Beachtenswerte Umweltlabel

| Label | Bedeutung |
|-------|-----------|
| Blauer Engel | Deutsches Umweltzeichen – strenge Kriterien |
| Energy Star | Energieeffizienz (international) |
| EPEAT | Electronic Product Environmental Assessment Tool |
| TCO Certified | Nachhaltigkeit und Ergonomie (Schweden) |
| EU Ecolabel | Europaeisches Umweltzeichen |
