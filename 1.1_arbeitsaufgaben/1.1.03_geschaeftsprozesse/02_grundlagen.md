# Grundlagen: 1.1.03 – Arbeitsaufgaben im Rahmen von Geschaefts- und Leistungsprozessen

## Bearbeitungsstatus, z.B. mittels Ticketsystem

**Definition:** Ein Ticketsystem ist eine Software zur strukturierten Erfassung, Zuweisung, Nachverfolgung und Dokumentation von Arbeitsaufgaben, Stoerungen und Serviceanfragen.

**Kernaussagen:**
- Jede Aufgabe wird als **Ticket** erfasst mit eindeutiger ID
- Typische Statuswerte: Neu, In Bearbeitung, Wartend, Geloest, Geschlossen
- Priorisierung nach Dringlichkeit und Auswirkung
- Nachvollziehbarkeit: Wer hat wann was bearbeitet?
- Reporting: Auswertung von Bearbeitungszeiten, Haefigkeit von Stoerungen

**Wichtige Begriffe:**
- **Ticket** – Datensatz, der eine Aufgabe oder Stoerung beschreibt
- **Ticketstatus** – aktueller Bearbeitungsstand
- **Priorisierung** – Einstufung der Dringlichkeit (z.B. niedrig, mittel, hoch, kritisch)
- **SLA (Service Level Agreement)** – vertraglich vereinbarte Reaktions- und Loesungszeiten

**Erklaerung:** Ticketsysteme sind zentral fuer den IT-Betrieb. Sie sorgen dafuer, dass keine Anfrage verloren geht und die Bearbeitungsqualitaet messbar ist. Beispiele: JIRA, OTRS, Zendesk.

---

## Fehlermanagement

**Definition:** Fehlermanagement ist der systematische Prozess zur Erkennung, Dokumentation, Analyse und Behebung von Fehlern in IT-Systemen, Software oder Prozessen.

**Kernaussagen:**
- Fehler werden klassifiziert nach Schwere und Auswirkung
- Dokumentation jedes Fehlers: Beschreibung, Ursache, Loesung, Zeitpunkt
- Ziel: Fehler dauerhaft beseitigen, nicht nur Symptome behandeln
- Unterscheidung: **Workaround** (temporaere Loesung) vs. **Fix** (dauerhafte Loesung)

**Wichtige Begriffe:**
- **Bug** – Fehler in Software
- **Incident** – Stoerung im IT-Betrieb (siehe auch Stoerungsmanagement)
- **Root Cause Analysis** – Ursachenanalyse, um den eigentlichen Grund eines Fehlers zu finden
- **Known Error** – dokumentierter Fehler mit bekannter Ursache und Workaround

**Erklaerung:** Fehlermanagement haengt eng mit dem Qualitaetsmanagement zusammen (Thema 1.5.02, PDCA-Zyklus). Fehler, die nicht systematisch dokumentiert werden, treten wiederholt auf.

---

## KI-Unterstuetzung

**Definition:** KI-Unterstuetzung bezeichnet den Einsatz kuenstlicher Intelligenz zur Automatisierung, Analyse und Optimierung von Arbeitsaufgaben im IT-Bereich.

**Kernaussagen:**
- KI kann repetitive Aufgaben automatisieren (z.B. Ticket-Kategorisierung)
- Chatbots koennen Erstanfragen im Support beantworten
- Predictive Analytics: Vorhersage von Stoerungen durch Mustererkennung
- KI-gestuetzte Code-Analyse und Fehlererkennung

**Wichtige Begriffe:**
- **Chatbot** – automatisierter Gespraechspartner fuer Standardanfragen
- **Machine Learning** – Algorithmen, die aus Daten lernen
- **Predictive Maintenance** – vorausschauende Wartung durch Datenanalyse (siehe auch Thema 3.1.11)
- **Natural Language Processing (NLP)** – Verarbeitung natuerlicher Sprache

**Erklaerung:** KI ersetzt nicht den IT-Facharbeiter, sondern unterstuetzt bei Routineaufgaben. Fuer die Pruefung ist relevant, wo KI sinnvoll eingesetzt werden kann und wo ihre Grenzen liegen.

---

## Kundenkommunikation

**Definition:** Kundenkommunikation umfasst alle Interaktionen zwischen IT-Dienstleister und Kunde im Rahmen von Auftraegen, Stoerungen und Serviceanfragen.

**Kernaussagen:**
- Professionell, sachlich und loesungsorientiert kommunizieren
- Kunden ueber Status, Fortschritt und Loesungen informieren
- Fachsprache fuer Kunden verstaendlich uebersetzen
- Verschiedene Kanaele: Telefon, E-Mail, Ticketsystem, persoenlich

**Wichtige Begriffe:**
- **Statusmeldung** – Information ueber den aktuellen Bearbeitungsstand
- **Eskalation** – Weiterleitung an hoehere Supportebene bei nicht loessbaren Problemen
- **Erwartungsmanagement** – Realistische Zusagen treffen und einhalten

**Erklaerung:** Gute Kundenkommunikation erhoht die Zufriedenheit und reduziert Rueckfragen. Siehe auch Thema 1.2.03 (Kommunikationsmodelle) und Thema 4.5.02 (IT-Schutzziele bei Kommunikation).

---

## Stoerungs-Management

**Definition:** Stoerungsmanagement (Incident Management) ist der Prozess zur schnellen Wiederherstellung des normalen IT-Betriebs nach einer Stoerung.

**Kernaussagen:**
- Ziel: Schnellstmoegliche Wiederherstellung des Dienstes
- Nicht Ursachenbeseitigung, sondern Betriebsaufnahme hat Prioritaet
- Stoerungen werden nach Schweregrad klassifiziert
- Dokumentation jeder Stoerung im Ticketsystem

**Ablauf:**
1. Erkennung und Erfassung der Stoerung
2. Klassifizierung und Priorisierung
3. Diagnose (Erstanalyse)
4. Eskalation (falls noetig)
5. Loesung und Wiederherstellung
6. Dokumentation und Abschluss

**Wichtige Begriffe:**
- **Incident** – ungeplante Unterbrechung eines IT-Service
- **Workaround** – temporaere Umgehung des Problems
- **Eskalation** – Weiterleitung an hoeheres Supportlevel
- **Major Incident** – schwerwiegende Stoerung mit grosser Auswirkung

**Erklaerung:** Stoerungsmanagement ist ein ITIL-Prozess. Es unterscheidet sich vom **Problem Management**, das die dauerhafte Ursachenbeseitigung zum Ziel hat. Siehe auch Thema 3.1.12 (Incident Management, SLA).

---

## Support- und Serviceanfragen (First-, Second- und Thirdlevelsupport)

**Definition:** Der IT-Support ist in drei Ebenen (Levels) organisiert, die sich in Kompetenz und Aufgabenbereich unterscheiden.

**Kernaussagen:**

### First-Level-Support (1st Level)
- Erste Anlaufstelle fuer alle Anfragen
- Aufgaben: Ticket-Erfassung, Standardloesungen anwenden, einfache Probleme loesen
- Beispiel: Passwort zuruecksetzen, Druckerproblem loesen

### Second-Level-Support (2nd Level)
- Bearbeitet komplexere technische Probleme
- Aufgaben: Detailanalyse, spezialisierte Fehlerbehebung
- Beispiel: Netzwerkproblem diagnostizieren, Softwarekonfiguration anpassen

### Third-Level-Support (3rd Level)
- Hoechste Eskalationsstufe, oft Experten oder Hersteller
- Aufgaben: Grundlegende Problemloesung, Entwicklung von Patches, Architekturanpassungen
- Beispiel: Herstellersupport fuer Softwarefehler, Infrastrukturumgestaltung

**Wichtige Begriffe:**
- **Eskalationsstufe** – Uebergang zwischen den Supportleveln
- **Single Point of Contact (SPOC)** – zentrale Anlaufstelle (meist 1st Level)
- **Wissensdatenbank** – Sammlung von Loesungen fuer bekannte Probleme

**Erklaerung:** Nicht jede Anfrage durchlaeuft alle Levels. Die meisten Anfragen werden im First-Level geloest. Die Eskalation erfolgt nur, wenn das aktuelle Level das Problem nicht loesen kann. Siehe auch Thema 3.1.12 (Service Level 1-3, Eskalationsstufen).
