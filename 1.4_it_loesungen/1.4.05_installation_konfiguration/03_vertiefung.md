# Vertiefung: 1.4.05 – Installation und Konfiguration

## Troubleshooting-Ablauf – Vertiefung

### Systematische Fehlersuche (Bottom-Up, OSI-basiert)

| Schritt | Aktion | Befehl |
|---|---|---|
| 1. Physisch (Schicht 1) | Kabel pruefen, LEDs, WLAN-Verbindung | Visuell, `ethtool eth0` |
| 2. Link (Schicht 2) | MAC/ARP pruefen | `arp -a` |
| 3. Netzwerk (Schicht 3) | IP-Konfiguration, Gateway | `ipconfig /all`, `ping Gateway` |
| 4. Transport (Schicht 4) | Port erreichbar? | `telnet host port`, `netstat` |
| 5. Anwendung (Schicht 7) | Dienst erreichbar? | `nslookup`, `curl`, Browser |

### Haefig gefragt: Befehlsvergleich Windows vs. Linux

| Szenario | Windows-Befehl | Linux-Befehl |
|---|---|---|
| Alle IPs anzeigen | `ipconfig /all` | `ip addr show` |
| DNS-Cache löschen | `ipconfig /flushdns` | `systemd-resolve --flush-caches` |
| Route zum Ziel | `tracert google.de` | `traceroute google.de` |
| Offene Verbindungen | `netstat -an` | `ss -tuln` |
| Ordnerinhalt rekursiv | `dir /s` | `ls -R` |
| Ordner loeschen | `rmdir /s /q ordner` | `rm -rf ordner` |

### Zusammenhang zu anderen Themen
- **Netzwerkdienste** (3.1.07): DHCP, DNS, Proxy → Wenn DNS nicht funktioniert, `nslookup` nutzen
- **Shell-Programmierung** (3.3.07): Befehle in Skripten automatisieren
- **Monitoring** (3.1.11): SNMP, Systemlastanalyse als Erweiterung des Troubleshootings

### Typische Pruefungsaspekte
- Befehl fuer beschriebenes Problem angeben
- Troubleshooting-Reihenfolge bestimmen
- Kommandozeilen-Ausgabe interpretieren
- Unterschied Windows/Linux-Befehle

### Haeufige Fehler
- `tracert` (Windows) und `traceroute` (Linux) verwechseln
- `ipconfig` auf Linux verwenden (korrekt: `ip a` oder `ifconfig`)
- DNS-Problem mit Ping auf IP loesen → Ping funktioniert, aber Namensaufloesung nicht
