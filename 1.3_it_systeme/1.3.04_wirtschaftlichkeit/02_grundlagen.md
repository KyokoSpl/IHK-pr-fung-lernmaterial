# Grundlagen: 1.3.04 – Wirtschaftlichkeit von IT-Systemen

## Anschaffungskosten

**Definition:** Einmalige Kosten, die beim Erwerb eines IT-Systems anfallen.

**Kernaussagen:**
- Hardwarekosten (Server, Clients, Netzwerkkomponenten)
- Softwarekosten (Lizenzen, Betriebssystem)
- Installations- und Konfigurationskosten
- Schulungskosten fuer Mitarbeiter
- Projektkosten (Planung, Beratung)

**Erklaerung:** Anschaffungskosten sind nicht gleich Gesamtkosten. Fuer eine vollstaendige wirtschaftliche Bewertung muessen auch Betriebs- und Finanzierungskosten beruecksichtigt werden (Total Cost of Ownership – TCO).

---

## Betriebskosten

**Definition:** Laufende Kosten, die waehrend der Nutzungsdauer eines IT-Systems anfallen.

**Kernaussagen:**
- Stromkosten (siehe 1.3.03: Leistung × Zeit × Preis)
- Wartung und Support (intern oder extern, SLA)
- Verbrauchsmaterial (Toner, Papier, Kabel)
- Raumkosten (Serverraum, Klimatisierung)
- Personal (Administration, Helpdesk)
- Updates und Upgrades

**Wichtige Begriffe:**
- **TCO (Total Cost of Ownership)** – Gesamtkosten ueber die Lebensdauer
- **OPEX (Operational Expenditure)** – Betriebsausgaben (laufend)
- **CAPEX (Capital Expenditure)** – Investitionsausgaben (einmalig)

---

## Einfacher Kostenvergleich (Leasing, Kauf, Finanzierung, Pay-per-Use)

**Definition:** Vergleich verschiedener Beschaffungsmodelle ueber einen definierten Zeitraum zur Ermittlung der guenstigsten Option.

**Kernaussagen:**

| Modell | Beschreibung | Vorteil | Nachteil |
|---|---|---|---|
| Kauf | Einmalige Zahlung, Eigentum | Kein Zinszuschlag, volle Kontrolle | Hohe Anfangsinvestition |
| Leasing | Monatliche Rate, kein Eigentum | Liquiditaet geschont, aktueller Stand | Teurer insgesamt, kein Eigentum |
| Finanzierung (Kredit) | Ratenzahlung + Zinsen, Eigentum | Eigentum, Liquiditaet teilweise geschont | Zinskosten |
| Pay-per-Use | Zahlung nach Nutzung | Flexibel, keine Anfangskosten | Schwer kalkulierbar, abhaengig |

**Berechnungsbeispiel:**
- Kauf: 12.000 EUR einmalig
- Leasing: 400 EUR/Monat × 36 Monate = 14.400 EUR
- Finanzierung: 12.000 EUR + 8% Zinsen auf 3 Jahre ≈ 13.440 EUR
→ Kauf ist am guenstigsten, aber bindet Kapital

---

## Finanzierungskosten

**Definition:** Kosten, die durch die Art der Kapitalbeschaffung entstehen (Zinsen, Gebuehren).

**Kernaussagen:**
- Kreditfinanzierung: Zinsen als zusaetzliche Kosten
- Leasingfinanzierung: Zinsanteil in Rate enthalten
- Eigenfinanzierung: Keine Zinskosten, aber Opportunitaetskosten (entgangene Anlagerendite)
- Foerderungen: Staatliche Zuschuesse oder Steuervorteile bei bestimmten Investitionen

---

## Lizenzkosten

**Definition:** Kosten fuer das Recht zur Nutzung von Software.

**Kernaussagen:**

| Modell | Beschreibung | Beispiel |
|---|---|---|
| Einmalkauf (perpetual) | Einmalige Zahlung, dauerhafte Nutzung | Microsoft Office 2021 |
| Abo/Subscription | Monatliche/jaehrliche Zahlung | Microsoft 365, Adobe CC |
| Open Source | Kostenfrei (ggf. Support kostenpflichtig) | LibreOffice, Linux |
| OEM | An Hardware gebunden | Windows mit Laptop |
| Concurrent/Floating | Begrenzte Gleichzeitnutzung | CAD-Software |
| Named User | Pro benanntem Benutzer | Datenbanklizenzen |

**Erklaerung:** In der Pruefung werden haeufig Lizenzkosten-Vergleiche gefordert: Was kostet Abo vs. Einmalkauf ueber 3 oder 5 Jahre?

---

## Nutzwertanalyse

**Definition:** Systematische Methode zur Bewertung und Rangfolge von Alternativen anhand gewichteter Kriterien.

**Vorgehen:**
1. Kriterien festlegen (z.B. Preis, Leistung, Support, Erweiterbarkeit)
2. Gewichtung vergeben (in % oder Punkten, Summe = 100%)
3. Alternativen je Kriterium bewerten (z.B. 1-10)
4. Gewichtete Punktzahl berechnen (Gewicht × Bewertung)
5. Summe bilden → Hoechste Summe = Empfehlung

**Beispiel:**

| Kriterium | Gewicht | Angebot A | Gew. A | Angebot B | Gew. B |
|---|---|---|---|---|---|
| Preis | 40% | 8 | 3,2 | 6 | 2,4 |
| Leistung | 30% | 7 | 2,1 | 9 | 2,7 |
| Support | 20% | 5 | 1,0 | 8 | 1,6 |
| Erweiterbarkeit | 10% | 6 | 0,6 | 7 | 0,7 |
| **Summe** | **100%** | | **6,9** | | **7,4** |

→ Angebot B ist die bessere Wahl trotz hoeherem Preis.

---

## Preis-Leistungs-Verhaeltnis

**Definition:** Bewertung, wie viel Leistung/Qualitaet man fuer den gezahlten Preis erhaelt.

**Kernaussagen:**
- Nicht immer ist das guenstigste Angebot das beste
- Nicht immer ist das teuerste das leistungsfaehigste
- Beruecksichtigung von TCO (Folgekosten!)
- Qualitative Aspekte einbeziehen (Zuverlaessigkeit, Support)

---

## Qualitativer und quantitativer Angebotsvergleich

**Definition:** Systematischer Vergleich von Angeboten anhand messbarer und nicht messbarer Kriterien.

**Quantitativ (messbar):**
- Angebotspreis (brutto/netto)
- Lieferzeit
- Zahlungsbedingungen (Skonto, Zahlungsziel)
- Garantiedauer

**Qualitativ (nicht messbar):**
- Reputation des Anbieters
- Servicequalitaet
- Referenzen
- Standort/Erreichbarkeit
- Nachhaltigkeit

**Berechnungsbeispiel Skonto:**
- Angebotspreis: 10.000 EUR netto
- Skonto: 2% bei Zahlung innerhalb 10 Tagen
- Ersparnis: 10.000 × 0,02 = 200 EUR → Zahlbetrag: 9.800 EUR

---

## Variable und fixe Kosten

**Definition:** Fixkosten bleiben unabhaengig von der Auslastung konstant, variable Kosten aendern sich proportional zur Nutzung.

| Kostenart | Beispiel IT | Verhalten |
|---|---|---|
| Fix | Servermiete, Lizenzen (Abo), Personal | Konstant |
| Variabel | Strom (nutzungsabhaengig), Cloud-Traffic, Druckkosten | Steigt mit Nutzung |

**Break-Even-Berechnung (Kauf vs. Cloud):**
- On-Premises: 50.000 EUR Fixkosten + 200 EUR/Monat variabel
- Cloud: 1.500 EUR/Monat rein variabel
- Break-Even: 50.000 / (1.500 - 200) = 38,5 Monate
→ Ab 39 Monaten ist On-Premises guenstiger

---

## Wertschoepfung

**Definition:** Der Mehrwert, den ein Unternehmen durch seine Taetigkeit schafft. Differenz zwischen dem Wert der Outputs und dem Wert der Inputs.

**Kernaussagen:**
- Wertschoepfung = Umsatz – Vorleistungen
- IT-Abteilung als interne Wertschoepfung (Produktivitaetssteigerung)
- IT-Dienstleister als externe Wertschoepfung (Verkauf von Services)
- Wertschoepfungskette nach Porter: Primaere und unterstuetzende Aktivitaeten
