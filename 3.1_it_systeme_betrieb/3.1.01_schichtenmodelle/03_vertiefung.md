# Vertiefung: 3.1.01 – Schichtenmodelle benennen und zuordnen

## OSI-Referenzmodell – Gesamtuebersicht

### Die 7 Schichten mit Protokollen und Dateneinheiten

| Schicht | Name | Funktion | Protokolle/Beispiele | Dateneinheit | Geraete |
|---------|------|----------|---------------------|--------------|---------|
| 7 | Application | Anwendungsdienste | HTTP, FTP, SMTP, DNS, DHCP | Daten | Gateway |
| 6 | Presentation | Datenformatierung, Verschluesselung | SSL/TLS, JPEG, ASCII | Daten | – |
| 5 | Session | Sitzungsverwaltung | NetBIOS, RPC | Daten | – |
| 4 | Transport | Ende-zu-Ende-Transport | TCP, UDP | Segment/Datagramm | – |
| 3 | Network | Logische Adressierung, Routing | IP, ICMP, ARP*, IPsec | Paket | Router |
| 2 | Data Link | Physische Adressierung, Frames | Ethernet, WLAN (802.11), PPP | Frame | Switch, Bridge |
| 1 | Physical | Bitstrom ueber Medium | Kabel, Glasfaser, Funk | Bit | Hub, Repeater |

*ARP arbeitet zwischen Schicht 2 und 3.

### TCP/IP-Modell im Vergleich

| TCP/IP-Schicht | Entspricht OSI | Protokolle |
|----------------|---------------|------------|
| 4 – Anwendung | 5, 6, 7 | HTTP, FTP, SMTP, DNS, DHCP |
| 3 – Transport | 4 | TCP, UDP |
| 2 – Internet | 3 | IP, ICMP, ARP |
| 1 – Netzzugang | 1, 2 | Ethernet, WLAN |

### ASCII-Darstellung: Datenkapselung

```
Anwendungsschicht:      [         Daten          ]
Transportschicht:   [TCP-Header][     Daten       ]  → Segment
Vermittlungsschicht:[IP-Header][TCP-H][  Daten    ]  → Paket
Sicherungsschicht: [Eth-H][IP-H][TCP-H][Daten][FCS]  → Frame
Bituebertragungs:   01010111010101010101010101010101  → Bits
```

---

## ARP-Prozess – Vertiefung

### Ablauf im Detail

```
PC-A (192.168.1.10, MAC: AA:AA:AA:AA:AA:AA)
    will PC-B (192.168.1.20) erreichen.

1. PC-A prueft ARP-Cache → kein Eintrag fuer 192.168.1.20

2. ARP-Request (Broadcast):
   [Src-MAC: AA:AA:AA:AA:AA:AA] [Dst-MAC: FF:FF:FF:FF:FF:FF]
   "Wer hat 192.168.1.20? Sage es 192.168.1.10"
   → Alle Geraete im LAN empfangen den Frame

3. PC-B (MAC: BB:BB:BB:BB:BB:BB) erkennt seine IP:
   ARP-Reply (Unicast):
   [Src-MAC: BB:BB:BB:BB:BB:BB] [Dst-MAC: AA:AA:AA:AA:AA:AA]
   "192.168.1.20 ist bei BB:BB:BB:BB:BB:BB"

4. PC-A speichert im ARP-Cache:
   192.168.1.20 → BB:BB:BB:BB:BB:BB

5. Kommunikation kann nun direkt erfolgen.
```

### Sicherheitsrisiko: ARP-Spoofing

- Angreifer sendet gefaelschte ARP-Replies mit eigener MAC
- Opfer speichert falsche Zuordnung im ARP-Cache
- Datenverkehr wird ueber den Angreifer umgeleitet (Man-in-the-Middle)
- Gegenmassnahmen: Dynamic ARP Inspection (DAI), statische ARP-Eintraege

---

## IPv4-Subnetting – Vertiefung

### Subnetting-Berechnungsschema

**Beispiel: 192.168.10.0/26**

1. Praefix /26 → 26 Bits Netzanteil, 6 Bits Hostanteil
2. Subnetzmaske: 255.255.255.192 (128+64 = 192)
3. Anzahl Hosts pro Subnetz: 2^6 - 2 = 62
4. Schrittweite: 256 - 192 = 64

Subnetze:

| Subnetz | Netzadresse | Erster Host | Letzter Host | Broadcast |
|---------|-------------|-------------|--------------|-----------|
| 1 | 192.168.10.0 | 192.168.10.1 | 192.168.10.62 | 192.168.10.63 |
| 2 | 192.168.10.64 | 192.168.10.65 | 192.168.10.126 | 192.168.10.127 |
| 3 | 192.168.10.128 | 192.168.10.129 | 192.168.10.190 | 192.168.10.191 |
| 4 | 192.168.10.192 | 192.168.10.193 | 192.168.10.254 | 192.168.10.255 |

### Haeufige Subnetzmasken

| CIDR | Maske | Hosts | Subnetze (bei /24-Ausgangsnetz) |
|------|-------|-------|---------------------------------|
| /24 | 255.255.255.0 | 254 | 1 |
| /25 | 255.255.255.128 | 126 | 2 |
| /26 | 255.255.255.192 | 62 | 4 |
| /27 | 255.255.255.224 | 30 | 8 |
| /28 | 255.255.255.240 | 14 | 16 |
| /29 | 255.255.255.248 | 6 | 32 |
| /30 | 255.255.255.252 | 2 | 64 |

---

## Routing vs. Switching – Vertiefung

### Detaillierter Vergleich

| Kriterium | Switching | Routing |
|-----------|-----------|---------|
| OSI-Schicht | 2 (Data Link) | 3 (Network) |
| Adressierung | MAC-Adresse | IP-Adresse |
| Geraet | Switch | Router |
| Reichweite | Innerhalb eines LANs | Zwischen verschiedenen Netzen |
| Tabelle | MAC-Adresstabelle (CAM) | Routing-Tabelle |
| Broadcast | Wird weitergeleitet | Wird blockiert (Broadcast-Domaene) |
| Geschwindigkeit | Sehr schnell (Hardware-basiert) | Langsamer (Software-Entscheidung) |
| VLAN-faehig | Ja (Tagged VLANs) | Ja (Inter-VLAN-Routing) |

### Paketfluss durch ein Netzwerk (ASCII)

```
[PC-A] --Frame--> [Switch] --Frame--> [Router] --neuer Frame--> [Switch] --Frame--> [PC-B]
LAN 1 (192.168.1.0/24)                                    LAN 2 (192.168.2.0/24)

Frame im LAN 1:  Src-MAC=PC-A, Dst-MAC=Router (LAN1-Interface)
                 Src-IP=PC-A,  Dst-IP=PC-B

Frame im LAN 2:  Src-MAC=Router (LAN2-Interface), Dst-MAC=PC-B
                 Src-IP=PC-A,  Dst-IP=PC-B
                 → IP-Adressen bleiben gleich, MAC-Adressen aendern sich!
```

---

## TCP vs. UDP – Vertiefung

### TCP 3-Way-Handshake (ASCII)

```
Client                    Server
  |                         |
  |--- SYN (seq=100) ----->|      1. Verbindungsanfrage
  |                         |
  |<-- SYN-ACK ------------|      2. Bestaetigung + eigene Anfrage
  |    (seq=300, ack=101)   |
  |                         |
  |--- ACK (ack=301) ----->|      3. Bestaetigung
  |                         |
  |===== Verbindung steht ==|
```

### TCP Verbindungsabbau (4-Way-Teardown)

```
Client                    Server
  |--- FIN --------------->|      1. Client will beenden
  |<-- ACK ----------------|      2. Server bestaetigt
  |<-- FIN ----------------|      3. Server will auch beenden
  |--- ACK --------------->|      4. Client bestaetigt
```

### Wichtige Portnummern fuer die Pruefung

| Port | Protokoll | Dienst | Transport |
|------|-----------|--------|-----------|
| 20/21 | FTP | Dateiuebertragung | TCP |
| 22 | SSH | Sichere Shell | TCP |
| 23 | Telnet | Unsichere Shell | TCP |
| 25 | SMTP | E-Mail-Versand | TCP |
| 53 | DNS | Namensaufloesung | TCP/UDP |
| 67/68 | DHCP | IP-Vergabe | UDP |
| 80 | HTTP | Webseiten | TCP |
| 110 | POP3 | E-Mail-Abruf | TCP |
| 143 | IMAP | E-Mail-Abruf | TCP |
| 443 | HTTPS | Webseiten (verschluesselt) | TCP |
| 3389 | RDP | Remote Desktop | TCP |

---

## Typische Pruefungsaspekte

- Protokolle den OSI-Schichten zuordnen koennen
- Unterschied zwischen OSI-Modell (7 Schichten) und TCP/IP-Modell (4 Schichten) erklaeren
- Datenkapselung beschreiben: Daten → Segment → Paket → Frame → Bits
- Subnetting-Aufgaben rechnen (Netzadresse, Broadcast, nutzbare Hosts)
- TCP vs. UDP: Wann wird welches Protokoll eingesetzt?
- ARP-Ablauf beschreiben koennen
- MAC vs. IP: Wann aendert sich was bei der Uebertragung?

## Haeufige Fehler

- ARP wird faelschlicherweise nur Schicht 3 zugeordnet – es arbeitet zwischen Schicht 2 und 3
- Verwechslung: IP-Adresse aendert sich beim Routing NICHT, MAC-Adressen aendern sich bei jedem Hop
- Subnetting: Netzadresse und Broadcast vergessen abzuziehen (nutzbare Hosts = 2^n - 2)
- UDP wird als "schlecht" bewertet – es ist fuer bestimmte Anwendungen (Echtzeit) die bessere Wahl
- OSI-Modell und TCP/IP-Modell werden verwechselt: OSI hat 7, TCP/IP hat 4 Schichten
