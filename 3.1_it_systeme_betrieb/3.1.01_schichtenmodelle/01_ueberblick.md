# Ueberblick: 3.1.01 – Schichtenmodelle benennen und zuordnen

## Einordnung

- **Pruefungsteil:** 3.1 – Betreiben von IT-Systemen (Netzwerktechnik)
- **Thema-ID:** 3.1.01
- **Thema:** Schichtenmodelle benennen und zuordnen koennen

## Ziel

Du musst das OSI-Referenzmodell und das TCP/IP-Modell kennen, Protokolle den richtigen Schichten zuordnen koennen und die Funktionsweise grundlegender Netzwerkprotokolle (ARP, IP, TCP, UDP, MAC) verstehen.

## Themenkreise im Ueberblick

### 1. ARP (Address Resolution Protocol)
ARP dient der Zuordnung von IP-Adressen zu MAC-Adressen innerhalb eines lokalen Netzwerks. Es arbeitet auf Schicht 2 (Data Link Layer) und ist essenziell fuer die Kommunikation im LAN.

### 2. IPv4 / IPv6
IPv4 verwendet 32-Bit-Adressen (ca. 4,3 Milliarden), IPv6 verwendet 128-Bit-Adressen. Beide arbeiten auf Schicht 3 (Vermittlungsschicht) und sind fuer die logische Adressierung und das Routing zustaendig. Subnetting ist ein zentrales Pruefungsthema bei IPv4.

### 3. MAC-Adressen
Die MAC-Adresse (Media Access Control) ist eine hardwarebasierte, 48 Bit lange Adresse, die auf Schicht 2 arbeitet. Sie identifiziert Netzwerkgeraete eindeutig innerhalb eines lokalen Netzwerks.

### 4. Routing
Routing ist der Prozess der Wegewahl fuer Datenpakete zwischen verschiedenen Netzwerken. Es findet auf Schicht 3 statt und wird von Routern durchgefuehrt. Statisches und dynamisches Routing sind zu unterscheiden.

### 5. Switching
Switching bezeichnet die Weiterleitung von Frames anhand von MAC-Adressen innerhalb eines LANs. Es arbeitet auf Schicht 2 und wird von Switches durchgefuehrt. Die MAC-Adresstabelle ist das zentrale Element.

### 6. TCP / UDP
TCP (Transmission Control Protocol) und UDP (User Datagram Protocol) arbeiten auf Schicht 4 (Transportschicht). TCP ist verbindungsorientiert und zuverlaessig, UDP ist verbindungslos und schneller. Die Wahl des Protokolls haengt vom Anwendungsfall ab.

## Querverweise
- → 3.1.02 (Netzwerkkomponenten: Router, Switch)
- → 3.1.03 (Netzwerkkonzepte: VLAN, Topologien)
- → 3.1.05 (Uebertragungsprotokolle: HTTP, HTTPS, TCP/UDP)
- → 3.1.07 (Netzwerkrelevante Dienste: DHCP, DNS)
