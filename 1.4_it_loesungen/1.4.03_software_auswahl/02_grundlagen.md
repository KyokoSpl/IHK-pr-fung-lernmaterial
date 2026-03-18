# Grundlagen: 1.4.03 – Bedarfsgerechte Auswahl von Software

## Anwendungssoftware

**Definition:** Software, die fuer bestimmte Aufgaben oder Geschaeftsprozesse eingesetzt wird.

**Kernaussagen:**
- **Office-Pakete:** Textverarbeitung, Tabellenkalkulation, Praesentation (MS Office, LibreOffice)
- **ERP-Systeme:** Enterprise Resource Planning – integrierte Unternehmenssoftware (SAP, Microsoft Dynamics)
- **Branchensoftware:** Spezifisch fuer eine Branche (z.B. Praxissoftware, CAD-Software)
- **Bildbearbeitung:** Photoshop, GIMP
- **Datenbanksoftware:** MySQL, PostgreSQL, Microsoft SQL Server

---

## Betriebssysteme

**Definition:** Systemsoftware, die Hardware verwaltet und die Grundlage fuer Anwendungssoftware bildet.

| Betriebssystem | Einsatz | Dateisystem | Besonderheit |
|---|---|---|---|
| Windows 10/11 | Desktop, Buero | NTFS | Weit verbreitet, Active Directory |
| Windows Server | Server | NTFS/ReFS | Domaene, Gruppenrichtlinien |
| Linux (Ubuntu, Debian) | Server, Entwicklung | ext4 | Open Source, stabil, anpassbar |
| macOS | Kreativbereich, Entwicklung | APFS | Apple-Hardware, Unix-Basis |
| Android/iOS | Mobile Geraete | ext4/APFS | Apps, Touch-Bedienung |

**Verwaltungsfunktionen:**
- Dateiverwaltung: Ordnerstruktur, Berechtigungen (ACL)
- Freigaben: SMB-Freigaben (Windows), NFS (Linux)
- Benutzerverwaltung: Lokale Konten, Domaenenkonten
- Prozessverwaltung: Task-Manager, Dienste

---

## Beurteilungskriterien

**Definition:** Masstaebe zur systematischen Bewertung von Software vor der Beschaffung.

| Kriterium | Beschreibung |
|---|---|
| Anpassbarkeit | Kann die Software an individuelle Beduerfnisse angepasst werden? |
| Wartbarkeit | Wie einfach sind Updates, Patches, Fehlerbehebungen? |
| Schnittstellen | Welche APIs, Import-/Exportformate stehen zur Verfuegung? |
| Portabilitaet | Laeuft die Software auf verschiedenen Plattformen? |
| Skalierbarkeit | Kann die Software mit wachsenden Anforderungen umgehen? |
| Benutzerfreundlichkeit | Intuitive Bedienung, Schulungsaufwand? |
| Sicherheit | Verschluesselung, Zugriffskontrolle, Updates? |
| Kosten | Lizenz, Betrieb, Schulung (→ TCO) |

---

## Integrierte Entwicklungsumgebung (IDE)

**Definition:** Software, die mehrere Entwicklungswerkzeuge in einer einheitlichen Oberflaeche buendelt.

**Bestandteile:**
- **Editor** – Quellcode schreiben mit Syntaxhervorhebung
- **Compiler/Interpreter** – Code uebersetzen/ausfuehren
- **Debugger** – Fehler finden (Breakpoints, Variableninspektion)
- **Versionsverwaltung** – Git-Integration
- **Build-Tools** – Automatisiertes Kompilieren und Paketieren

**Beispiele:** Visual Studio Code, IntelliJ IDEA, Eclipse, PyCharm

---

## KI-Software

**Definition:** Software, die auf kuenstlicher Intelligenz basiert und Aufgaben wie Sprachverarbeitung, Datenanalyse oder Automatisierung uebernimmt.

**Kernaussagen:**
- **Chatbots:** Kundenservice-Automatisierung (z.B. ChatGPT, Microsoft Copilot)
- **Datenanalyse:** Mustererkennung, Prognosen (z.B. TensorFlow, Azure ML)
- **Automatisierung:** RPA (Robotic Process Automation), Workflow-Optimierung
- **Datenschutz:** Verarbeitung personenbezogener Daten durch KI → DSGVO beachten
- Cloud vs. Lokal: Cloud-KI (flexibel, Datenschutzbedenken) vs. Lokale KI (Kontrolle, Ressourcenbedarf)

---

## Open Source

**Definition:** Software, deren Quellcode offen eingesehen, veraendert und weiterverbreitet werden darf.

**Kernaussagen:**
- Lizenzen: GPL (Copyleft), MIT (permissiv), Apache (permissiv, Patentschutz)
- Kostenlos nutzbar, aber ggf. kostenpflichtiger Support
- Vorteile: Transparenz, Community, keine Abhaengigkeit vom Hersteller
- Nachteile: Kein garantierter Support, Eigenverantwortung fuer Wartung
- Beispiele: Linux, LibreOffice, Firefox, GIMP, MySQL, Git

---

## Proprietaere Software

**Definition:** Software, deren Quellcode nicht einsehbar ist und deren Nutzung durch Lizenzbedingungen eingeschraenkt wird.

**Kernaussagen:**
- EULA (End User License Agreement) regelt Nutzungsrechte
- Kein Einblick in Quellcode, keine Modifikation erlaubt
- Vorteile: Professioneller Support, Schulungen, stabile Releases
- Nachteile: Herstellerabhaengigkeit (Vendor Lock-in), Lizenzkosten
- Beispiele: Microsoft Office, Adobe Creative Cloud, SAP

---

## Standard- oder Individualsoftware

**Definition:** Standardsoftware ist fuer den Massenmarkt entwickelt. Individualsoftware wird massgeschneidert fuer einen bestimmten Kunden erstellt.

| Kriterium | Standardsoftware | Individualsoftware |
|---|---|---|
| Kosten | Guenstiger (Massenprodukt) | Teurer (Einzelentwicklung) |
| Anpassung | Begrenzt (Konfiguration) | Voll anpassbar |
| Einfuehrungszeit | Kurz | Lang (Entwicklungszeit) |
| Wartung | Hersteller liefert Updates | Eigene/externe Wartung |
| Beispiel | SAP, Microsoft 365 | Individuelle CRM-Loesung |

## Querverweise
- → 1.4.04 (Lizenzmodelle: GPL, OEM, EULA)
- → 1.3.04 (Wirtschaftlichkeit: Lizenzkosten, TCO)
- → 3.3.04 (Auswahl Programmiersprache)
