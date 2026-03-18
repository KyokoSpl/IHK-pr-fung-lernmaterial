# Grundlagen: 1.4.01 – IT-Systeme konzeptionieren, konfigurieren, testen, dokumentieren

## Bedarfsanalyse

**Definition:** Systematische Ermittlung der Anforderungen an ein IT-System vor dessen Beschaffung oder Entwicklung.

**Kernaussagen:**
- Ist-Analyse: Aktuellen Zustand dokumentieren (Hardware, Software, Prozesse)
- Soll-Zustand: Gewuenschte Funktionalitaet, Leistung, Kapazitaet definieren
- Stakeholder einbeziehen: Anwender, IT-Abteilung, Geschaeftsfuehrung
- Rahmenbedingungen: Budget, Zeitrahmen, Kompatibilitaet, Datenschutz
- Methoden: Interviews, Frageboegen, Beobachtung, Dokumentenanalyse

**Wichtige Begriffe:**
- **Ist-Analyse** – Erfassung des aktuellen Zustands
- **Soll-Konzept** – Beschreibung des Zielzustands
- **Stakeholder** – Alle Personen/Gruppen mit Interesse am Projekt

**Erklaerung:** Die Bedarfsanalyse bildet die Grundlage fuer das Lastenheft und steht am Anfang jedes IT-Projekts. Ohne saubere Bedarfsanalyse drohen Fehlbeschaffungen.

---

## Installation und Einrichtung von Systemen

**Definition:** Praktische Taetigkeiten zur Inbetriebnahme eines IT-Systems – von der Hardware-Konfiguration bis zur Netzwerkeinbindung.

**Kernaussagen:**

### Betriebssystem-Installation
- Installationsmedium: USB, PXE-Boot, Image-basiert
- Partitionierung: Aufteilung der Festplatte in logische Bereiche
  - MBR (max. 4 primaere Partitionen, max. 2 TB)
  - GPT (max. 128 Partitionen, >2 TB)
- Formatierung: Dateisystem anlegen (NTFS, ext4, APFS)

### BIOS/UEFI-Einstellungen
- Boot-Reihenfolge festlegen
- Secure Boot aktivieren/deaktivieren
- Virtualisierung (VT-x) aktivieren
- TPM-Modul aktivieren (fuer BitLocker, Windows 11)

### Netzwerkanbindung
- **IPv4-Konfiguration:** IP-Adresse, Subnetzmaske, Gateway, DNS
- **IPv6-Konfiguration:** Autokonfiguration (SLAAC) oder manuell
- **DHCP vs. statisch:** DHCP fuer Clients, statisch fuer Server
- **WLAN:** SSID, Sicherheitsprotokoll (WPA2/WPA3), Pre-shared Key oder 802.1X

### Remote-Desktop
- RDP (Remote Desktop Protocol): Windows-Standard, Port 3389
- VNC: Plattformuebergreifend
- SSH: Kommandozeile, verschluesselt, Port 22
- TeamViewer/AnyDesk: Einfache Fernwartung

### KI-Software
- Lokal installierte KI-Tools (z.B. Copilot, lokale LLMs)
- Cloud-basierte KI-Dienste (z.B. ChatGPT, Azure AI)
- Datenschutzaspekte bei KI-Nutzung beachten

---

## Lasten- und Pflichtenheft

**Definition:** Zentrale Dokumente der Anforderungsdokumentation in IT-Projekten.

### Lastenheft (Erstellung: Auftraggeber)

| Aspekt | Beschreibung |
|---|---|
| Zweck | Beschreibt das „Was" – Anforderungen aus Kundensicht |
| Urheber | Auftraggeber (Kunde) |
| Inhalt | Ausgangssituation, Zielsetzung, funktionale Anforderungen, nicht-funktionale Anforderungen, Rahmenbedingungen |

### Pflichtenheft (Erstellung: Auftragnehmer)

| Aspekt | Beschreibung |
|---|---|
| Zweck | Beschreibt das „Wie" – Umsetzungskonzept |
| Urheber | Auftragnehmer (Dienstleister) |
| Inhalt | Technische Loesung, Architektur, Zeitplan, Testkonzept, Abnahmekriterien |

**Wichtige Begriffe:**
- **Funktionale Anforderung** – Was das System tun soll (z.B. „Benutzer kann sich einloggen")
- **Nicht-funktionale Anforderung** – Qualitaetsmerkmale (z.B. Antwortzeit < 2 Sekunden)
- **Abnahmekriterien** – Messbare Bedingungen fuer die erfolgreiche Uebergabe

**Erklaerung:** Pruefungsklassiker: Lastenheft vs. Pflichtenheft unterscheiden. Merkhilfe: **Lastenheft = Kundenwunsch (Was)**, **Pflichtenheft = Umsetzungsplan (Wie)**.

## Querverweise
- → 3.4.01 (Lasten-/Pflichtenheft detailliert)
- → 1.1.01 (Projektplanung, SMART-Ziele)
- → 1.4.05 (Konsolenbefehle fuer Konfiguration)
