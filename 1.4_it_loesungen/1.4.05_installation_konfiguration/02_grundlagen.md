# Grundlagen: 1.4.05 – Installation und Konfiguration

## Anpassung von Software

**Definition:** Konfiguration und Parametrierung von Software, um sie an die Beduerfnisse der Nutzer und des Unternehmens anzupassen.

**Kernaussagen:**
- **Konfiguration:** Einstellungen ueber GUI oder Konfigurationsdateien (z.B. INI, XML, YAML)
- **Parametrierung:** Anpassung durch Setzen von Parametern (z.B. Datenbankverbindung, Sprache)
- **Personalisierung:** Nutzerspezifische Einstellungen (z.B. Desktop, Startseite)
- Gruppenrichtlinien (GPO) fuer unternehmensweite Konfiguration
- Automatisierte Softwareverteilung (z.B. SCCM, PDQ Deploy, Ansible)

---

## Arbeiten mit der Kommandozeile

**Definition:** Textbasierte Schnittstelle zur Steuerung eines Betriebssystems durch Eingabe von Befehlen.

**Befehlssyntax:**
```
befehl [optionen] [parameter]
```
- **Befehl:** Auszufuehrende Aktion (z.B. `dir`, `ls`)
- **Optionen/Flags:** Modifizieren das Verhalten (z.B. `-l`, `/s`)
- **Parameter:** Ziel der Aktion (z.B. Dateiname, Pfad)

**Shells:**
- **Windows:** CMD (Command Prompt), PowerShell
- **Linux/macOS:** Bash, Zsh, Fish

---

## Installation und Konfiguration der Hardware

**Definition:** Physische und logische Einrichtung von Hardware-Komponenten.

**Kernaussagen:**
- Einbau von Komponenten (RAM, SSD, Grafikkarte)
- Treiber installieren (automatisch via OS oder manuell vom Hersteller)
- Peripherie anbinden: Drucker, Scanner, Monitor (USB, HDMI, DisplayPort)
- Firmware-Updates (z.B. BIOS/UEFI-Update)
- Geraetemanager (Windows): Status pruefen, Treiber aktualisieren

---

## Installation und Konfiguration des Betriebssystems

**Definition:** Einrichtung des Betriebssystems und Grundkonfiguration fuer den produktiven Einsatz.

**Kernaussagen:**
- Installationsmedium: USB-Stick, PXE-Boot, Image (WDS, MDT)
- Partitionierung und Formatierung (→ 1.3.03)
- Windows-Aktivierung (Lizenzschluessel, KMS-Server)
- Updates installieren (Windows Update, apt update/upgrade)
- Dienste konfigurieren (z.B. Druckdienst, Remotedesktop)
- Benutzerverwaltung: Lokale Konten, Domaene

---

## Konfiguration, Test und Troubleshooting von Netzwerkverbindungen

**Definition:** Einrichtung und Fehlerbehebung von Netzwerkverbindungen.

**Kernaussagen:**
- **IP-Konfiguration:** IPv4/IPv6, Subnetzmaske, Gateway, DNS
- **DHCP:** Automatische IP-Vergabe durch DHCP-Server
- **WLAN:** SSID, Sicherheit (WPA2/WPA3), Pre-shared Key vs. 802.1X Enterprise
- **VPN:** Sicherer Remotezugang zum Firmennetz (→ 3.1.06)

**Troubleshooting-Methodik:**
1. Physische Verbindung pruefen (Kabel, LED)
2. IP-Konfiguration pruefen (`ipconfig`, `ip a`)
3. Lokale Konnektivitaet testen (`ping 127.0.0.1`, `ping Gateway`)
4. Externe Konnektivitaet testen (`ping 8.8.8.8`)
5. Namensaufloesung testen (`nslookup`)
6. Routing pruefen (`traceroute`, `tracert`)

---

## Konsolenbefehle fuer Dateioperationen und Netzwerk-Troubleshooting

### Dateioperationen

| Aktion | Windows (CMD) | Linux (Bash) |
|---|---|---|
| Verzeichnis anzeigen | `dir` | `ls -la` |
| Ordner erstellen | `mkdir ordner` | `mkdir ordner` |
| Datei kopieren | `copy quelle ziel` | `cp quelle ziel` |
| Datei loeschen | `del datei` | `rm datei` |
| Datei verschieben | `move quelle ziel` | `mv quelle ziel` |
| Berechtigungen aendern | `icacls` | `chmod 755 datei` |

### Netzwerk-Troubleshooting

| Aktion | Windows | Linux |
|---|---|---|
| IP-Konfiguration anzeigen | `ipconfig /all` | `ip a` oder `ifconfig` |
| Erreichbarkeit testen | `ping 192.168.1.1` | `ping 192.168.1.1` |
| Route verfolgen | `tracert ziel` | `traceroute ziel` |
| DNS-Abfrage | `nslookup domain` | `nslookup domain` |
| ARP-Tabelle anzeigen | `arp -a` | `arp -a` |
| Offene Ports anzeigen | `netstat -an` | `ss -tuln` |
| DHCP erneuern | `ipconfig /release` + `/renew` | `dhclient -r` + `dhclient` |
| DNS-Cache leeren | `ipconfig /flushdns` | `systemd-resolve --flush-caches` |
| Routing-Tabelle | `route print` | `ip route` |

### Wichtige Aliase und Zusatzbefehle (Linux)
- `alias` – Kurzbefehl definieren
- `iproute2` – Modernes Netzwerk-Tool-Paket (ersetzt ifconfig, route, arp)

## Querverweise
- → 1.4.01 (BIOS/UEFI, Partitionierung)
- → 3.1.07 (DHCP, DNS, Proxy im Detail)
- → 3.3.07 (Shell-Programmierung, Scripting)
