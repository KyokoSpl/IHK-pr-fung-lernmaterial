# Grundlagen: 3.1.01 – Schichtenmodelle benennen und zuordnen

## ARP (Address Resolution Protocol)

**Definition:** ARP ist ein Protokoll zur Aufloesung von IPv4-Adressen in MAC-Adressen innerhalb eines lokalen Netzwerks (LAN). Es arbeitet auf OSI-Schicht 2/3.

**Kernaussagen:**
- ARP sendet einen Broadcast an alle Geraete im LAN: "Wer hat IP x.x.x.x?"
- Das Geraet mit der gesuchten IP antwortet mit seiner MAC-Adresse (Unicast)
- Die Zuordnung wird im ARP-Cache gespeichert (temporaer)
- ARP funktioniert nur innerhalb eines Subnetzes
- Reverse ARP (RARP) macht das Gegenteil: MAC → IP (historisch)

**Wichtige Begriffe:**
- **ARP-Request** – Broadcast-Anfrage: "Wer hat diese IP?"
- **ARP-Reply** – Unicast-Antwort mit der MAC-Adresse
- **ARP-Cache** – temporaere Tabelle mit bekannten IP-MAC-Zuordnungen
- **ARP-Spoofing** – Angriff durch gefaelschte ARP-Antworten (Man-in-the-Middle)

**Erklaerung:** Wenn PC A (192.168.1.10) mit PC B (192.168.1.20) kommunizieren will, muss er dessen MAC-Adresse kennen. PC A prueft zuerst seinen ARP-Cache. Ist kein Eintrag vorhanden, sendet er einen ARP-Request als Broadcast. PC B erkennt seine IP und antwortet mit seiner MAC. PC A speichert die Zuordnung im Cache.

---

## IPv4 / IPv6

**Definition:** IP (Internet Protocol) ist das zentrale Protokoll der Vermittlungsschicht (OSI-Schicht 3). Es ermoeglicht die logische Adressierung und das Routing von Paketen ueber Netzwerkgrenzen hinweg.

### IPv4

**Kernaussagen:**
- 32-Bit-Adresse, dargestellt als vier Dezimalzahlen (Dotted Decimal Notation): z.B. 192.168.1.1
- Adressraum: ca. 4,3 Milliarden Adressen (2^32)
- Aufgeteilt in Netzanteil und Hostanteil (durch Subnetzmaske bestimmt)
- Subnetzmaske definiert die Grenze: z.B. 255.255.255.0 = /24

**Wichtige Adressbereiche:**

| Bereich | Netz | CIDR | Typ |
|---------|------|------|-----|
| Klasse A privat | 10.0.0.0 | /8 | Privat |
| Klasse B privat | 172.16.0.0 – 172.31.0.0 | /12 | Privat |
| Klasse C privat | 192.168.0.0 | /16 | Privat |
| Loopback | 127.0.0.0 | /8 | Lokal |
| APIPA | 169.254.0.0 | /16 | Automatisch (kein DHCP) |

**Subnetting-Grundlagen:**
- Subnetzmaske /24 = 255.255.255.0 → 256 Adressen, 254 nutzbar
- Subnetzmaske /25 = 255.255.255.128 → 128 Adressen, 126 nutzbar
- Formel nutzbare Hosts: 2^(32-Praefix) - 2 (Netz- und Broadcastadresse abziehen)

### IPv6

**Kernaussagen:**
- 128-Bit-Adresse, dargestellt als acht Gruppen zu je vier Hexadezimalziffern: z.B. 2001:0db8:85a3:0000:0000:8a2e:0370:7334
- Adressraum: 2^128 (praktisch unbegrenzt)
- Fuehrende Nullen koennen gekuerzt werden, aufeinanderfolgende Nullgruppen einmal durch :: ersetzt
- Kein Broadcast – stattdessen Multicast und Anycast
- Autokonfiguration (SLAAC) moeglich

**Wichtige IPv6-Adressen:**

| Adresse | Bedeutung |
|---------|-----------|
| ::1 | Loopback |
| fe80::/10 | Link-Local (wie APIPA) |
| 2000::/3 | Global Unicast (oeffentlich) |
| fc00::/7 | Unique Local (privat) |
| ff00::/8 | Multicast |

**Wichtige Begriffe:**
- **Subnetzmaske** – trennt Netz- und Hostanteil einer IPv4-Adresse
- **CIDR-Notation** – Kurzschreibweise fuer die Subnetzmaske (z.B. /24)
- **NAT** – Network Address Translation, uebersetzt private in oeffentliche IP-Adressen
- **SLAAC** – Stateless Address Autoconfiguration (IPv6)

---

## MAC-Adressen

**Definition:** Die MAC-Adresse (Media Access Control) ist eine 48 Bit (6 Byte) lange, weltweit eindeutige Hardware-Adresse eines Netzwerkadapters. Sie arbeitet auf OSI-Schicht 2.

**Kernaussagen:**
- Darstellung: sechs Hexadezimal-Paare, z.B. AA:BB:CC:DD:EE:FF
- Erste 3 Bytes = OUI (Organizationally Unique Identifier) → identifiziert den Hersteller
- Letzte 3 Bytes = geraetespezifische Kennung
- Wird vom Hersteller fest vergeben (kann aber softwareseitig geaendert werden)
- Broadcast-MAC: FF:FF:FF:FF:FF:FF

**Wichtige Begriffe:**
- **OUI** – Herstellerkennung (erste 3 Bytes der MAC)
- **Unicast-MAC** – Adresse eines einzelnen Geraets
- **Broadcast-MAC** – FF:FF:FF:FF:FF:FF, erreicht alle Geraete im LAN
- **Multicast-MAC** – erreicht eine Gruppe von Geraeten

**Erklaerung:** Die MAC-Adresse wird fuer die Kommunikation innerhalb eines LANs benoetigt. Ein Switch leitet Frames anhand der MAC-Adressen weiter. Bei der Kommunikation ueber Router hinweg aendert sich die MAC-Adresse in jedem Hop, waehrend die IP-Adresse gleich bleibt.

---

## Routing

**Definition:** Routing ist der Prozess der Wegewahl fuer IP-Pakete zwischen verschiedenen Netzwerken. Es findet auf OSI-Schicht 3 statt und wird von Routern durchgefuehrt.

**Kernaussagen:**
- Router verbinden verschiedene Netzwerke und leiten Pakete anhand der Ziel-IP-Adresse weiter
- Die Routing-Tabelle enthaelt Informationen ueber bekannte Netze und den naechsten Hop
- Statisches Routing: Routen werden manuell konfiguriert
- Dynamisches Routing: Routen werden automatisch ueber Protokolle gelernt (z.B. OSPF, RIP, BGP)
- Default-Route (0.0.0.0/0): wird verwendet, wenn keine spezifische Route existiert

**Wichtige Begriffe:**
- **Routing-Tabelle** – Liste aller bekannten Routen mit Ziel, Metrik und Next Hop
- **Next Hop** – naechster Router auf dem Weg zum Ziel
- **Default Gateway** – Standardrouter fuer Pakete ausserhalb des eigenen Netzes
- **Metrik** – Bewertungszahl fuer die Guete eines Weges

**Erklaerung:** Wenn ein Host ein Paket an eine IP-Adresse ausserhalb seines Subnetzes sendet, schickt er es an sein Default Gateway (Router). Der Router prueft seine Routing-Tabelle und leitet das Paket an den naechsten Hop weiter, bis es das Zielnetz erreicht.

---

## Switching

**Definition:** Switching ist die Weiterleitung von Ethernet-Frames anhand von MAC-Adressen innerhalb eines LANs. Es arbeitet auf OSI-Schicht 2 und wird von Switches durchgefuehrt.

**Kernaussagen:**
- Ein Switch lernt MAC-Adressen durch Beobachten eingehender Frames (Source-MAC → Port)
- Die MAC-Adresstabelle (CAM-Table) ordnet MAC-Adressen den Ports zu
- Bekannte Ziel-MAC → Frame wird nur an den richtigen Port gesendet (Unicast)
- Unbekannte Ziel-MAC → Frame wird an alle Ports gesendet (Flooding)
- Broadcast-Frames werden an alle Ports weitergeleitet

**Wichtige Begriffe:**
- **MAC-Adresstabelle / CAM-Table** – Zuordnung von MAC zu Port
- **Flooding** – Weiterleitung an alle Ports bei unbekannter Ziel-MAC
- **Store-and-Forward** – Frame wird komplett empfangen und geprueft vor Weiterleitung
- **Cut-Through** – Frame wird sofort nach Lesen der Ziel-MAC weitergeleitet (schneller, keine Fehlerkorrektur)

**Erklaerung:** Ein Switch arbeitet intelligenter als ein Hub. Waehrend ein Hub alle Frames an alle Ports sendet, leitet ein Switch Frames gezielt weiter. Dadurch werden Kollisionen vermieden und die Bandbreite besser genutzt.

---

## TCP / UDP

**Definition:** TCP und UDP sind Transportprotokolle auf OSI-Schicht 4. Sie steuern den Datentransport zwischen Anwendungen auf verschiedenen Hosts.

### TCP (Transmission Control Protocol)

**Kernaussagen:**
- Verbindungsorientiert: Verbindung wird vor Datenaustausch aufgebaut (3-Way-Handshake)
- Zuverlaessig: Empfangsbestaetigungen (ACK), Neuuebertragung bei Verlust
- Reihenfolge wird garantiert (Sequenznummern)
- Flusskontrolle und Staukontrolle (Congestion Control)
- Hoehere Latenz durch Overhead

**3-Way-Handshake:**
1. Client → Server: SYN
2. Server → Client: SYN-ACK
3. Client → Server: ACK

### UDP (User Datagram Protocol)

**Kernaussagen:**
- Verbindungslos: Kein Verbindungsaufbau, Daten werden direkt gesendet
- Unzuverlaessig: Keine Empfangsbestaetigungen, kein Neuversand
- Keine Reihenfolgegarantie
- Geringer Overhead → schneller als TCP
- Geeignet fuer Echtzeitanwendungen

**Vergleich TCP vs. UDP:**

| Kriterium | TCP | UDP |
|-----------|-----|-----|
| Verbindung | Verbindungsorientiert | Verbindungslos |
| Zuverlaessigkeit | Ja (ACK, Retransmission) | Nein |
| Reihenfolge | Garantiert | Nicht garantiert |
| Geschwindigkeit | Langsamer (Overhead) | Schneller |
| Typische Anwendung | HTTP, FTP, E-Mail, SSH | DNS, DHCP, VoIP, Streaming |

**Wichtige Begriffe:**
- **Port** – logische Adresse einer Anwendung (0–65535)
- **Well-Known Ports** – 0–1023, z.B. HTTP=80, HTTPS=443, SSH=22, FTP=21, DNS=53
- **Socket** – Kombination aus IP-Adresse und Port (z.B. 192.168.1.1:443)
- **Segment** – Dateneinheit auf Schicht 4 (TCP)
- **Datagramm** – Dateneinheit auf Schicht 4 (UDP)

**Erklaerung:** TCP wird gewaehlt, wenn alle Daten vollstaendig und in korrekter Reihenfolge ankommen muessen (z.B. Dateiuebertragung). UDP wird gewaehlt, wenn Geschwindigkeit wichtiger ist als Vollstaendigkeit (z.B. Videostreaming – ein verlorenes Paket erzeugt nur kurzes Ruckeln).
