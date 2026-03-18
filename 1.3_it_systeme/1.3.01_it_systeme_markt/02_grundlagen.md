# Grundlagen: 1.3.01 – Marktgaengige IT-Systeme

## Branchensoftware

**Definition:** Branchensoftware ist speziell fuer die Anforderungen einer bestimmten Branche oder Geschaeftsprozesse entwickelte Software.

- **ERP (Enterprise Resource Planning):** Integrierte Verwaltung aller Geschaeftsprozesse (Einkauf, Produktion, Vertrieb, Finanzen). Beispiel: SAP, Microsoft Dynamics
- **SCM (Supply Chain Management):** Steuerung der Lieferkette vom Lieferanten bis zum Kunden
- **CRM (Customer Relationship Management):** Verwaltung von Kundenbeziehungen, Vertrieb und Marketing. Beispiel: Salesforce, HubSpot

---

## Cloudloesungen

**Definition:** Cloud-Dienste stellen IT-Ressourcen ueber das Internet bereit, ohne lokale Installation.

- **SaaS (Software as a Service):** Anwendung wird ueber den Browser genutzt. Beispiel: Microsoft 365, Google Workspace
- **DaaS (Desktop as a Service):** Virtueller Desktop wird aus der Cloud bereitgestellt. Der Nutzer greift per Thin Client oder Browser auf seinen Arbeitsplatz zu

**Abgrenzung:** Siehe auch Thema 3.2.04 (IaaS, PaaS, SaaS, On-Premises)

---

## Entwicklungssysteme

**Definition:** Werkzeuge zur Softwareentwicklung.

- **Compiler:** Uebersetzt Quellcode vollstaendig in Maschinencode (z.B. GCC, javac)
- **Interpreter:** Fuehrt Quellcode zeilenweise aus (z.B. Python-Interpreter)
- **Virtuelle Maschinen:** Fuehren Bytecode plattformunabhaengig aus (z.B. JVM)
- **Editoren:** Texteditoren fuer Code (z.B. VS Code, Vim)
- **Debugger:** Werkzeug zur Fehlersuche, erlaubt schrittweises Durchlaufen des Codes

**Querverweise:** Thema 1.4.06 (Compiler, Linker, Interpreter), Thema 3.4.07 (IDE, Debugger)

---

## Funktionale, oekonomische und oekologische Aspekte

| Aspekt | Beschreibung | Beispiel |
|--------|-------------|----------|
| **Ergonomie** | Benutzerfreundlichkeit, Bedienbarkeit | Ergonomische Tastatur, intuitive Software |
| **Leistungsparameter** | Geschwindigkeit, Kapazitaet, Durchsatz | CPU-Takt, RAM-Groesse, SSD-Geschwindigkeit |
| **Einmalige Kosten** | Anschaffung, Installation | Hardware-Kauf, Einrichtungskosten |
| **Laufende Kosten** | Wartung, Lizenzen, Strom | Monatliche Cloud-Gebuehren |
| **Nutzungsdauer** | Erwartete Lebensdauer des Systems | 3-5 Jahre fuer Business-PCs |
| **Energieverbrauch** | Stromverbrauch im Betrieb | Watt-Angabe, Energy Star |
| **Recyclingfaehigkeit** | Entsorgung und Wiederverwertung | WEEE-Richtlinie, Recycling-Label |

---

## Hardwareprodukte

**CPU:** Prozessor, fuehrt Berechnungen durch. Kenngroessen: Taktfrequenz, Kerne, Cache.
**Motherboard:** Hauptplatine, verbindet alle Komponenten.
**RAM:** Arbeitsspeicher, fluechtig, schneller Zugriff. Typen: DDR4, DDR5.
**Datenspeicher:** SSD (schnell, Flash-basiert), HDD (mechanisch, guenstiger pro GB).
**Netzteil:** Stromversorgung, Wirkungsgrad (80 PLUS Zertifizierung).
**Grafikkarte:** GPU fuer Bildausgabe, auch fuer KI-Berechnungen.
**Peripheriegeraete:** Monitor, Tastatur, Maus, Drucker, Scanner.
**Sensoren:** Temperatur, Bewegung, Licht – relevant fuer IoT.
**Netzwerkkomponenten:** WLAN-Router, Switch, Gateway, Access Point.

**Querverweise:** Thema 1.3.03 (Leistungsdaten), Thema 1.4.02 (Hardwareauswahl)

---

## KI-Software

Software, die kuenstliche Intelligenz nutzt: Spracherkennung, Bilderkennung, Textgenerierung, Datenanalyse. Beispiele: ChatGPT, TensorFlow, Copilot.

**Querverweise:** Thema 1.1.03 (KI-Unterstuetzung), Thema 1.4.03 (KI-Software als Auswahlkriterium)

---

## Softwareprodukte

- **Anwendungssoftware:** Programme fuer spezifische Aufgaben (Textverarbeitung, Bildbearbeitung, Browser)
- **Betriebssysteme:** Verwalten Hardware und stellen Schnittstelle bereit. Beispiele: Windows, Linux, macOS

---

## Standardsoftware

Vorgefertigte Software fuer allgemeine Aufgaben:
- **Office-Pakete:** Microsoft 365, LibreOffice
- **DBMS:** MySQL, PostgreSQL, Microsoft SQL Server
- **Browser:** Chrome, Firefox, Edge

Abgrenzung zu Individualsoftware: Standardsoftware ist fuer den breiten Markt, Individualsoftware wird kundenspezifisch entwickelt (siehe Thema 1.4.03).

---

## Systemsoftware

Software, die den Betrieb des Computers ermoeglicht: Betriebssysteme, Geraetetreiber, Firmware, Dienstprogramme (z.B. Dateisystemtools, Task-Manager).

---

## Virtuelle Desktops

- **Cloud-basiert (DaaS):** Desktop laeuft auf einem Server im Rechenzentrum, Zugriff ueber Netzwerk
- **Lokal (VDI):** Desktop laeuft auf einem lokalen Server, Zugriff ueber Thin Clients im LAN
- Vorteile: Zentrale Verwaltung, Sicherheit, ortsunabhaengiges Arbeiten
- Nachteile: Abhaengigkeit von Netzwerkverbindung, Latenz
