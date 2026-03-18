# Uebungen: 3.1.01 – Schichtenmodelle benennen und zuordnen

## OSI-Modell und Protokollzuordnung

**Aufgabe 1:** Nenne die sieben Schichten des OSI-Modells in der korrekten Reihenfolge (von unten nach oben) und gib jeweils die Dateneinheit an.

**Aufgabe 2:** Ordne die folgenden Protokolle der korrekten OSI-Schicht zu: HTTP, TCP, IP, Ethernet, UDP, ARP, FTP, ICMP, SMTP, DNS.

**Aufgabe 3:** Erklaere den Unterschied zwischen dem OSI-Modell (7 Schichten) und dem TCP/IP-Modell (4 Schichten). Welche OSI-Schichten werden im TCP/IP-Modell zusammengefasst?

**Aufgabe 4:** Beschreibe den Prozess der Datenkapselung: Was passiert mit den Daten, wenn sie von der Anwendungsschicht bis zur Bituebertragungs­schicht wandern?

---

## ARP

**Aufgabe 5:** Beschreibe den ARP-Prozess in vier Schritten: PC-A (192.168.1.10) will PC-B (192.168.1.20) erreichen und kennt dessen MAC-Adresse nicht.

**Aufgabe 6:** Was ist ARP-Spoofing und welche Gegenmassnahme kann auf einem Switch konfiguriert werden?

---

## IPv4 / IPv6

**Aufgabe 7:** Berechne fuer das Netz 192.168.50.0/27:
a) Die Subnetzmaske in Dezimalschreibweise
b) Die Anzahl nutzbarer Hosts pro Subnetz
c) Die Netzadressen aller Subnetze
d) Den Broadcastadresse des dritten Subnetzes

**Aufgabe 8:** In welchem Subnetz liegt die IP-Adresse 10.20.30.200 mit der Maske /28?
a) Netzadresse
b) Broadcastadresse
c) Erster und letzter nutzbarer Host

**Aufgabe 9:** Nenne drei wesentliche Unterschiede zwischen IPv4 und IPv6.

**Aufgabe 10:** Was ist eine APIPA-Adresse und wann wird sie vergeben?

---

## MAC-Adressen

**Aufgabe 11:** Erklaere den Aufbau einer MAC-Adresse. Was ist der OUI-Anteil?

**Aufgabe 12:** Warum aendert sich die MAC-Adresse eines Frames bei jedem Router-Hop, die IP-Adresse aber nicht?

---

## Routing und Switching

**Aufgabe 13:** Erklaere den Unterschied zwischen Routing und Switching. Nenne jeweils die OSI-Schicht, das verwendete Geraet und die Adressierungsart.

**Aufgabe 14:** Was ist eine Default-Route und wann wird sie verwendet? Gib die Netzadresse der Default-Route an.

**Aufgabe 15:** Beschreibe, wie ein Switch seine MAC-Adresstabelle aufbaut. Was passiert, wenn die Ziel-MAC unbekannt ist?

---

## TCP / UDP

**Aufgabe 16:** Beschreibe den TCP-3-Way-Handshake in drei Schritten.

**Aufgabe 17:** Nenne fuenf Anwendungsprotokolle mit dem jeweiligen Transportprotokoll (TCP oder UDP) und der Portnummer.

**Aufgabe 18:** Ein Unternehmen plant einen VoIP-Dienst. Welches Transportprotokoll sollte verwendet werden? Begruende.

**Aufgabe 19:** Erklaere, warum DNS sowohl TCP als auch UDP verwendet.

---
---

# Loesungen

## Aufgabe 1
1. Schicht 1 – Bituebertragungs­schicht (Physical): Bits
2. Schicht 2 – Sicherungsschicht (Data Link): Frames
3. Schicht 3 – Vermittlungsschicht (Network): Pakete
4. Schicht 4 – Transportschicht (Transport): Segmente (TCP) / Datagramme (UDP)
5. Schicht 5 – Sitzungsschicht (Session): Daten
6. Schicht 6 – Darstellungsschicht (Presentation): Daten
7. Schicht 7 – Anwendungsschicht (Application): Daten

## Aufgabe 2
- Schicht 7 (Application): HTTP, FTP, SMTP, DNS
- Schicht 4 (Transport): TCP, UDP
- Schicht 3 (Network): IP, ICMP
- Schicht 2/3: ARP (arbeitet zwischen beiden Schichten)
- Schicht 2 (Data Link): Ethernet

## Aufgabe 3
Das OSI-Modell hat 7 Schichten, das TCP/IP-Modell hat 4. Im TCP/IP-Modell werden zusammengefasst:
- OSI-Schichten 5, 6, 7 → TCP/IP-Schicht 4 (Anwendung)
- OSI-Schicht 4 → TCP/IP-Schicht 3 (Transport)
- OSI-Schicht 3 → TCP/IP-Schicht 2 (Internet)
- OSI-Schichten 1, 2 → TCP/IP-Schicht 1 (Netzzugang)

## Aufgabe 4
Die Daten werden beim Durchlaufen der Schichten jeweils mit einem Header versehen (Kapselung):
1. Anwendungsschicht: Nutzdaten entstehen
2. Transportschicht: TCP/UDP-Header wird hinzugefuegt → Segment/Datagramm
3. Vermittlungsschicht: IP-Header wird hinzugefuegt → Paket
4. Sicherungsschicht: Ethernet-Header und Trailer (FCS) werden hinzugefuegt → Frame
5. Bituebertragungsschicht: Frame wird als Bitfolge ueber das Medium gesendet

## Aufgabe 5
1. PC-A prueft seinen ARP-Cache: kein Eintrag fuer 192.168.1.20 vorhanden
2. PC-A sendet einen ARP-Request als Broadcast (Ziel-MAC: FF:FF:FF:FF:FF:FF): "Wer hat 192.168.1.20?"
3. PC-B erkennt seine IP und antwortet mit einem ARP-Reply (Unicast) an PC-A: "192.168.1.20 hat MAC BB:BB:BB:BB:BB:BB"
4. PC-A speichert die Zuordnung 192.168.1.20 → BB:BB:BB:BB:BB:BB im ARP-Cache

## Aufgabe 6
ARP-Spoofing ist ein Angriff, bei dem ein Angreifer gefaelschte ARP-Replies sendet, um seinen eigenen MAC-Eintrag fuer eine fremde IP in den ARP-Cache des Opfers einzuschleusen. Dadurch wird der Datenverkehr ueber den Angreifer umgeleitet (Man-in-the-Middle). Gegenmassnahme auf dem Switch: Dynamic ARP Inspection (DAI), die ARP-Pakete gegen die DHCP-Snooping-Datenbank validiert.

## Aufgabe 7
a) /27 → 255.255.255.224 (128+64+32 = 224)
b) 2^(32-27) - 2 = 2^5 - 2 = 30 nutzbare Hosts
c) Schrittweite: 256 - 224 = 32. Subnetze: 192.168.50.0, 192.168.50.32, 192.168.50.64, 192.168.50.96, 192.168.50.128, 192.168.50.160, 192.168.50.192, 192.168.50.224
d) Drittes Subnetz = 192.168.50.64/27 → Broadcast: 192.168.50.95

## Aufgabe 8
/28 → Schrittweite: 256 - 240 = 16. 200 / 16 = 12 Rest 8 → 12 * 16 = 192
a) Netzadresse: 10.20.30.192
b) Broadcastadresse: 10.20.30.207 (192 + 16 - 1)
c) Erster Host: 10.20.30.193, Letzter Host: 10.20.30.206

## Aufgabe 9
1. Adresslaenge: IPv4 = 32 Bit (ca. 4,3 Mrd. Adressen), IPv6 = 128 Bit (praktisch unbegrenzt)
2. Darstellung: IPv4 = Dezimal mit Punkten (192.168.1.1), IPv6 = Hexadezimal mit Doppelpunkten (2001:db8::1)
3. Broadcast: IPv4 hat Broadcast, IPv6 verwendet stattdessen Multicast und Anycast

## Aufgabe 10
APIPA (Automatic Private IP Addressing) vergibt Adressen im Bereich 169.254.0.0/16. Sie wird automatisch vergeben, wenn ein Geraet per DHCP keine IP-Adresse erhaelt (DHCP-Server nicht erreichbar). Mit APIPA kann nur im lokalen Netz kommuniziert werden, kein Internetzugang.

## Aufgabe 11
Eine MAC-Adresse ist 48 Bit (6 Byte) lang, dargestellt als sechs Hexadezimal-Paare (z.B. AA:BB:CC:DD:EE:FF). Die ersten 3 Bytes (AA:BB:CC) sind der OUI (Organizationally Unique Identifier) und identifizieren den Hersteller der Netzwerkkarte. Die letzten 3 Bytes sind die geraetespezifische Kennung.

## Aufgabe 12
Die MAC-Adresse ist nur fuer die Kommunikation innerhalb eines lokalen Netzwerks (Hop-zu-Hop) zustaendig. An jedem Router wird der Frame entpackt, das IP-Paket ausgelesen und ein neuer Frame mit den MAC-Adressen des aktuellen und naechsten Hops erstellt. Die IP-Adresse hingegen bleibt als Ende-zu-Ende-Adresse (Quelle und Ziel) ueber alle Hops hinweg unveraendert.

## Aufgabe 13
- Switching: OSI-Schicht 2, Geraet = Switch, Adressierung = MAC-Adresse, innerhalb eines LANs
- Routing: OSI-Schicht 3, Geraet = Router, Adressierung = IP-Adresse, zwischen verschiedenen Netzen

## Aufgabe 14
Die Default-Route (0.0.0.0/0) ist ein Eintrag in der Routing-Tabelle, der alle Pakete auffaengt, fuer die keine spezifischere Route existiert. Sie wird verwendet, um Pakete mit unbekanntem Zielnetz an einen bestimmten Next-Hop (z.B. den Internet-Router) weiterzuleiten.

## Aufgabe 15
Ein Switch lernt MAC-Adressen, indem er bei jedem eingehenden Frame die Quell-MAC-Adresse dem Eingangsport zuordnet und in die MAC-Adresstabelle (CAM-Table) eintraegt. Ist die Ziel-MAC-Adresse unbekannt (kein Eintrag in der Tabelle), fuehrt der Switch ein Flooding durch: Der Frame wird an alle Ports weitergeleitet (ausser dem Eingangsport).

## Aufgabe 16
1. SYN: Der Client sendet ein SYN-Paket an den Server (Verbindungsanfrage mit initialer Sequenznummer)
2. SYN-ACK: Der Server antwortet mit SYN-ACK (bestaetigt die Anfrage und sendet eigene Sequenznummer)
3. ACK: Der Client bestaetigt mit ACK → Verbindung ist aufgebaut, Daten koennen uebertragen werden

## Aufgabe 17
1. HTTP – TCP – Port 80
2. HTTPS – TCP – Port 443
3. DNS – UDP (und TCP) – Port 53
4. DHCP – UDP – Port 67/68
5. FTP – TCP – Port 20/21

## Aufgabe 18
UDP, da VoIP eine Echtzeitanwendung ist. Verzoegerungen durch Verbindungsaufbau und Neuuebertragungen (wie bei TCP) wuerden die Sprachqualitaet stark beeintraechtigen. Ein verlorenes Paket wird uebersprungen statt neu angefordert – kurze Aussetzer sind akzeptabler als Verzoegerungen.

## Aufgabe 19
DNS-Anfragen nutzen standardmaessig UDP (Port 53), da die Anfragen klein sind und schnell gehen sollen (kein Verbindungsaufbau noetig). TCP wird verwendet, wenn die Antwort groesser als 512 Bytes ist oder bei Zonentransfers zwischen DNS-Servern, bei denen Zuverlaessigkeit wichtiger ist als Geschwindigkeit.
