# Ueberblick und Grundlagen: 3.2.04 – Service- und Liefermodelle

## Einordnung

- **Pruefungsteil:** 3.2 – Inbetriebnehmen von Speicherloesungen
- **Thema-ID:** 3.2.04
- **Thema:** Verschiedene Service- und Liefermodelle benennen und bedarfsorientiert auswaehlen koennen

## Ziel

Du musst Cloud-Service-Modelle (SaaS, PaaS, IaaS) und Bereitstellungsmodelle (On Premises, Cloud, Hybrid) unterscheiden, vergleichen und fuer ein gegebenes Szenario die passende Loesung empfehlen koennen.

## Themenkreise im Ueberblick

| Nr. | Themenkreis | Schwerpunkt |
|-----|-------------|-------------|
| 1 | On Premises, Cloud | Liefermodelle, Bereitstellungsarten (Private, Public, Hybrid Cloud) |
| 2 | SaaS, IaaS, PaaS | Service-Modelle, Shared Responsibility, Vor-/Nachteile |

### Querverweise
- Thema 3.2.06: Netzwerkkomponenten und -protokolle (Anbindung an Cloud-Dienste)
- Thema 3.2.05: Daten heterogener Quellen zusammenfuehren (Cloud als Speicherort)
- Thema 1.4.07: Lizenzmodelle (SaaS-Lizenzen vs. On-Premises-Lizenzen)

---

## Grundlagen

### 1. Bereitstellungsmodelle: On Premises vs. Cloud

**Definition:** Ein Bereitstellungsmodell beschreibt, wo IT-Infrastruktur betrieben wird – im eigenen Rechenzentrum (On Premises) oder bei einem externen Anbieter (Cloud).

**Vergleich der Bereitstellungsmodelle:**

| Kriterium | On Premises | Public Cloud | Private Cloud | Hybrid Cloud |
|-----------|------------|-------------|--------------|-------------|
| Standort | Eigenes Rechenzentrum | Rechenzentrum des Anbieters | Eigenes oder dediziertes RZ | Kombination |
| Kontrolle | Vollstaendig | Gering (Anbieter verwaltet) | Hoch | Gemischt |
| Kosten (Anfang) | Hoch (Hardware, Aufbau) | Gering (Pay-as-you-go) | Mittel bis hoch | Mittel |
| Kosten (laufend) | Strom, Wartung, Personal | Nutzungsbasiert (OpEx) | Wartung + Betrieb | Variabel |
| Skalierbarkeit | Begrenzt (Hardware muss gekauft werden) | Sehr hoch (elastisch) | Begrenzt | Hoch |
| Datenschutz/Compliance | Volle Kontrolle | Abhaengig vom Anbieter/Standort | Hohe Kontrolle | Differenziert moeglich |
| Eignung | Hohe Sicherheitsanforderungen, stabile Last | Variable Last, schneller Start | Regulierte Branchen | Flexibilitaet + Kontrolle |

**Cloud-Bereitstellungsformen:**

| Form | Beschreibung | Beispiel |
|------|-------------|---------|
| **Public Cloud** | Ressourcen werden geteilt, oeffentlich verfuegbar | AWS, Microsoft Azure, Google Cloud |
| **Private Cloud** | Exklusiv fuer ein Unternehmen, eigene Infrastruktur | OpenStack im eigenen RZ, VMware vSphere |
| **Hybrid Cloud** | Kombination aus On Premises/Private Cloud und Public Cloud | Sensible Daten lokal, Lastspitzen in der Public Cloud |
| **Multi Cloud** | Nutzung mehrerer Public-Cloud-Anbieter | AWS fuer Compute, Azure fuer KI, Google fuer Analytics |

**Wichtige Begriffe:**
- **CapEx (Capital Expenditure)** – Investitionsausgaben (z.B. Serverkauf)
- **OpEx (Operational Expenditure)** – Betriebsausgaben (z.B. monatliche Cloud-Gebuehren)
- **Elastizitaet** – automatische Anpassung der Ressourcen an den Bedarf
- **Vendor Lock-in** – Abhaengigkeit von einem bestimmten Cloud-Anbieter

---

### 2. Service-Modelle: SaaS, IaaS, PaaS

**Definition:** Cloud-Service-Modelle beschreiben, welche Verantwortlichkeiten beim Anbieter und welche beim Kunden liegen.

**Die drei Service-Modelle:**

| Modell | Ausgeschrieben | Beschreibung | Beispiel |
|--------|---------------|-------------|---------|
| **IaaS** | Infrastructure as a Service | Anbieter stellt Infrastruktur bereit (VMs, Netzwerk, Storage). Kunde verwaltet OS, Middleware, Anwendungen | AWS EC2, Azure VMs, Google Compute Engine |
| **PaaS** | Platform as a Service | Anbieter stellt Plattform bereit (OS, Middleware, Laufzeitumgebung). Kunde entwickelt und deployt Anwendungen | Azure App Service, Google App Engine, Heroku |
| **SaaS** | Software as a Service | Anbieter stellt fertige Anwendung bereit. Kunde nutzt sie ueber den Browser | Microsoft 365, Salesforce, Google Workspace |

**Shared Responsibility Model (Geteilte Verantwortung):**

```
Verantwortung:         On Prem    IaaS     PaaS     SaaS
+-----------------+
| Anwendung       |   Kunde    Kunde    Kunde    Anbieter
| Daten           |   Kunde    Kunde    Kunde    Kunde*
| Laufzeitumgebung|   Kunde    Kunde    Anbieter Anbieter
| Middleware      |   Kunde    Kunde    Anbieter Anbieter
| Betriebssystem  |   Kunde    Kunde    Anbieter Anbieter
| Virtualisierung |   Kunde    Anbieter Anbieter Anbieter
| Server/Hardware |   Kunde    Anbieter Anbieter Anbieter
| Netzwerk        |   Kunde    Anbieter Anbieter Anbieter
| Rechenzentrum   |   Kunde    Anbieter Anbieter Anbieter
+-----------------+
(*Daten bleiben immer in der Verantwortung des Kunden)
```

**Wichtige Begriffe:**
- **Shared Responsibility** – geteilte Verantwortung zwischen Anbieter und Kunde
- **Pay-as-you-go** – Bezahlung nach tatsaechlicher Nutzung
- **Mandantenfaehigkeit (Multi-Tenancy)** – mehrere Kunden teilen sich eine Infrastruktur, logisch getrennt
- **SLA (Service Level Agreement)** – vertragliche Zusicherung von Verfuegbarkeit und Leistung

---

## Vertiefung

### Entscheidungsmatrix: On Premises vs. Cloud

| Anforderung | Empfehlung |
|-------------|-----------|
| Hoechste Datenschutzanforderungen (z.B. Gesundheitsdaten) | On Premises oder Private Cloud |
| Schnelle Skalierung bei unvorhersehbarer Last | Public Cloud (IaaS oder PaaS) |
| Standardsoftware ohne Anpassung (z.B. E-Mail, Office) | SaaS |
| Individuelle Anwendungsentwicklung | PaaS |
| Volle Kontrolle ueber Hardware und Software | On Premises |
| Kostenoptimierung bei stark schwankender Auslastung | Public Cloud (Pay-as-you-go) |
| Sensible Daten lokal, Lastspitzen in der Cloud | Hybrid Cloud |

### Pizza-Analogie fuer Service-Modelle

| | On Premises | IaaS | PaaS | SaaS |
|---|---|---|---|---|
| **Pizza-Analogie** | Selbst gemacht (Teig, Belag, Ofen, alles selbst) | Ofen + Kuechengeraete gestellt, Teig + Belag selbst | Fertiger Teig + Ofen gestellt, Belag selbst | Pizza wird geliefert (fertig) |

### Typische Pruefungsaspekte
- Service-Modelle (SaaS, PaaS, IaaS) erklaeren und unterscheiden
- Shared Responsibility Matrix lesen und anwenden
- Szenario: Welches Modell fuer welchen Anwendungsfall?
- Vor- und Nachteile von On Premises vs. Cloud benennen
- CapEx vs. OpEx im Cloud-Kontext erklaeren

### Haeufige Fehler
- IaaS und PaaS verwechseln: Bei IaaS verwaltet der Kunde das OS, bei PaaS nicht
- "Cloud ist immer guenstiger" → Falsch! Bei stabiler, hoher Last kann On Premises kosteneffizienter sein
- Datenschutz wird vergessen → Cloud-Anbieter muss DSGVO-konform sein (Serverstandort beachten!)
- SaaS wird mit einer lokal installierten Software verwechselt → SaaS laeuft im Browser beim Anbieter

---

## Uebungen

**Aufgabe 1:** Erklaere die drei Cloud-Service-Modelle (SaaS, PaaS, IaaS) jeweils in einem Satz und nenne ein Beispiel.

**Aufgabe 2:** Ein mittelstaendisches Unternehmen moechte seine E-Mail-Loesung modernisieren. Aktuell betreibt es einen eigenen Exchange-Server. Welches Cloud-Service-Modell wuerdest du empfehlen? Begruende.

**Aufgabe 3:** Erstelle eine Tabelle, die zeigt, wer (Anbieter oder Kunde) bei IaaS, PaaS und SaaS fuer folgende Bereiche verantwortlich ist: Rechenzentrum, Betriebssystem, Anwendung, Daten.

**Aufgabe 4:** Was ist der Unterschied zwischen CapEx und OpEx? Ordne zu: Serverkauf, monatliche Cloud-Gebuehr, Notstromaggregat, SaaS-Lizenz.

**Aufgabe 5:** Nenne drei Vorteile und drei Nachteile der Public Cloud gegenueber On Premises.

---
---

# Loesungen

## Aufgabe 1
- **IaaS (Infrastructure as a Service):** Der Anbieter stellt virtuelle Infrastruktur (VMs, Netzwerk, Storage) bereit, der Kunde verwaltet OS und Anwendungen. Beispiel: AWS EC2.
- **PaaS (Platform as a Service):** Der Anbieter stellt eine Entwicklungsplattform bereit (inkl. OS und Laufzeitumgebung), der Kunde entwickelt und deployt seine Anwendungen. Beispiel: Heroku.
- **SaaS (Software as a Service):** Der Anbieter stellt eine fertige Anwendung bereit, die der Kunde ueber den Browser nutzt. Beispiel: Microsoft 365.

## Aufgabe 2
**SaaS** (z.B. Microsoft 365 / Exchange Online). Begruendung: E-Mail ist eine Standardanwendung ohne individuelle Anpassung. SaaS erfordert keinen eigenen Server, keine Wartung, automatische Updates. Der Anbieter kuemmert sich um Betrieb, Sicherheit und Verfuegbarkeit. Kosten sind planbar (monatliche Lizenz pro Nutzer).

## Aufgabe 3

| Bereich | IaaS | PaaS | SaaS |
|---------|------|------|------|
| Rechenzentrum | Anbieter | Anbieter | Anbieter |
| Betriebssystem | Kunde | Anbieter | Anbieter |
| Anwendung | Kunde | Kunde | Anbieter |
| Daten | Kunde | Kunde | Kunde |

## Aufgabe 4
- **CapEx (Capital Expenditure):** Einmalige Investitionsausgaben. Beispiele: Serverkauf, Notstromaggregat.
- **OpEx (Operational Expenditure):** Laufende Betriebsausgaben. Beispiele: Monatliche Cloud-Gebuehr, SaaS-Lizenz.

## Aufgabe 5
**Vorteile der Public Cloud:**
1. Hohe Skalierbarkeit (Ressourcen bei Bedarf hinzubuchen)
2. Geringe Anfangsinvestition (kein Hardwarekauf, OpEx statt CapEx)
3. Schnelle Bereitstellung (VMs in Minuten statt Wochen)

**Nachteile der Public Cloud:**
1. Abhaengigkeit vom Anbieter (Vendor Lock-in)
2. Datenschutzbedenken (Daten auf fremden Servern, DSGVO-Konformitaet pruefen)
3. Laufende Kosten koennen bei stabiler Last hoeher sein als On Premises
