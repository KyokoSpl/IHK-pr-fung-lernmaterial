# Grundlagen: 3.1.02 – Netzwerkkomponenten vergleichen und beschreiben

## Bridge

**Definition:** Eine Bridge ist ein Netzwerkgeraet auf OSI-Schicht 2 (Data Link Layer), das zwei Netzwerksegmente verbindet und den Datenverkehr anhand von MAC-Adressen filtert.

**Kernaussagen:**
- Arbeitet auf Schicht 2 (Data Link Layer)
- Trennt Kollisionsdomaenen, aber NICHT Broadcast-Domaenen
- Lernt MAC-Adressen und leitet Frames nur weiter, wenn noetig
- Wurde weitgehend durch Switches ersetzt
- Transparent Bridge: Geraete im Netzwerk merken nichts von der Bridge

**Wichtige Begriffe:**
- **Kollisionsdomaene** – Bereich, in dem Datenkollisionen auftreten koennen
- **Broadcast-Domaene** – Bereich, in dem Broadcast-Frames empfangen werden
- **Spanning Tree Protocol (STP)** – verhindert Schleifen bei redundanten Bridge-Verbindungen

**Erklaerung:** Eine Bridge arbeitet wie ein Switch mit nur zwei Ports. Sie empfaengt Frames, prueft die Ziel-MAC und entscheidet, ob der Frame ins andere Segment weitergeleitet werden muss. Heute wird der Begriff "Bridge" hauptsaechlich im WLAN-Kontext verwendet (Wireless Bridge verbindet zwei LANs drahtlos).

---

## Firewall

**Definition:** Eine Firewall ist ein Sicherheitssystem, das den Netzwerkverkehr zwischen vertrauenswuerdigen und nicht vertrauenswuerdigen Netzen anhand definierter Regeln kontrolliert.

**Kernaussagen:**
- Kann als Hardware-Appliance oder Software implementiert werden
- Regeln basieren auf: Quell-/Ziel-IP, Quell-/Ziel-Port, Protokoll, Richtung
- Grundprinzipien: Whitelist (nur Erlaubtes durchlassen) oder Blacklist (nur Verbotenes blockieren)
- Platzierung: Zwischen internem Netz und Internet, zwischen Netzwerksegmenten

### Firewall-Typen

| Typ | OSI-Schicht | Funktion | Merkmale |
|-----|------------|----------|----------|
| Paketfilter | 3–4 | Filtert anhand IP, Port, Protokoll | Schnell, aber kein Kontext |
| Stateful Inspection | 3–4 | Verfolgt Verbindungsstatus | Erkennt zusammengehoerige Pakete |
| Application Gateway (Proxy) | 7 | Analysiert Anwendungsdaten | Tiefe Inspektion, langsamer |
| Next-Generation Firewall (NGFW) | 3–7 | Kombination aller Typen | IDS/IPS, Deep Packet Inspection |

### Paketfilter vs. Stateful Inspection

| Kriterium | Paketfilter | Stateful Inspection |
|-----------|-------------|---------------------|
| Analyse | Einzelne Pakete isoliert | Pakete im Verbindungskontext |
| Zustandsinformation | Nein | Ja (State Table) |
| Rueckverkehr | Muss explizit erlaubt werden | Wird automatisch erlaubt |
| Performance | Sehr schnell | Etwas langsamer |
| Sicherheit | Grundlegend | Hoeher |
| Beispiel-Regel | "Erlaube TCP Port 443 von aussen" | "Erlaube Antwortpakete zu bestehenden Verbindungen" |

**Wichtige Begriffe:**
- **ACL (Access Control List)** – Regelliste zur Verkehrskontrolle
- **DMZ (Demilitarisierte Zone)** – Netzwerkbereich zwischen internem Netz und Internet fuer oeffentliche Server
- **NAT (Network Address Translation)** – oft in Firewalls integriert
- **IDS/IPS** – Intrusion Detection/Prevention System, erkennt und blockiert Angriffe
- **Deep Packet Inspection (DPI)** – Analyse des Dateninhalts (nicht nur Header)

**Erklaerung:** Ein einfacher Paketfilter prueft jedes Paket einzeln: Quell-IP, Ziel-IP, Port, Protokoll. Er weiss nicht, ob ein Paket zu einer bestehenden Verbindung gehoert. Eine Stateful Inspection Firewall merkt sich den Zustand von Verbindungen. Wenn ein interner Client eine HTTPS-Verbindung aufbaut, wird der Rueckverkehr automatisch zugelassen, ohne dass eine extra Regel noetig ist.

---

## Router

**Definition:** Ein Router ist ein Netzwerkgeraet auf OSI-Schicht 3 (Vermittlungsschicht), das IP-Pakete zwischen verschiedenen Netzwerken weiterleitet und als Grenze zwischen Broadcast-Domaenen dient.

**Kernaussagen:**
- Arbeitet auf Schicht 3 (Network Layer)
- Leitet Pakete anhand der Ziel-IP-Adresse und der Routing-Tabelle weiter
- Trennt Broadcast-Domaenen (Broadcasts werden NICHT weitergeleitet)
- Kann NAT durchfuehren (private → oeffentliche IP)
- Verbindet unterschiedliche Netzwerke (z.B. LAN mit WAN/Internet)
- Unterstuetzt statisches und dynamisches Routing

**Wichtige Begriffe:**
- **Routing-Tabelle** – Enthaelt Zielnetze, Metriken und Next-Hop-Informationen
- **Default Gateway** – Router-Adresse, an die Pakete fuer unbekannte Ziele gesendet werden
- **NAT/PAT** – Uebersetzung privater in oeffentliche Adressen (Port-basiert)
- **ACL** – Zugriffslisten auf dem Router zur Paketfilterung

**Erklaerung:** Jedes Geraet im LAN hat ein Default Gateway konfiguriert (meist die Router-IP). Wenn ein Paket an ein Ziel ausserhalb des eigenen Subnetzes gesendet wird, schickt das Geraet es an den Router. Der Router entpackt den Frame, liest die Ziel-IP, schaut in die Routing-Tabelle und erstellt einen neuen Frame fuer das naechste Netzwerksegment.

---

## Switch

**Definition:** Ein Switch ist ein Netzwerkgeraet auf OSI-Schicht 2 (Data Link Layer), das Ethernet-Frames anhand von MAC-Adressen gezielt an den richtigen Port weiterleitet.

**Kernaussagen:**
- Arbeitet auf Schicht 2 (Data Link Layer), Layer-3-Switches zusaetzlich auf Schicht 3
- Jeder Port bildet eine eigene Kollisionsdomaene (Full Duplex moeglich)
- MAC-Adresstabelle (CAM-Table) ordnet MAC-Adressen den Ports zu
- Unbekannte Ziel-MAC → Flooding (Frame an alle Ports)
- Unterstuetzt VLANs zur logischen Segmentierung

### Switch vs. Hub

| Kriterium | Switch | Hub |
|-----------|--------|-----|
| OSI-Schicht | 2 | 1 |
| Adressierung | MAC-basiert | Keine (alle Ports) |
| Kollisionsdomaene | Pro Port eine | Eine fuer alle Ports |
| Duplex | Full Duplex | Half Duplex |
| Bandbreite | Dediziert pro Port | Geteilt |
| Intelligenz | Lernt MAC-Adressen | Keine |

### Layer-2-Switch vs. Layer-3-Switch

| Kriterium | Layer-2-Switch | Layer-3-Switch |
|-----------|----------------|----------------|
| OSI-Schicht | 2 | 2 und 3 |
| Weiterleitung | MAC-Adresse | MAC und IP-Adresse |
| Routing-Faehigkeit | Nein | Ja (Inter-VLAN-Routing) |
| Einsatz | Einfache LANs | Grosse Netze mit VLANs |
| Preis | Guenstiger | Teurer |

**Wichtige Begriffe:**
- **CAM-Table** – Content Addressable Memory Tabelle (MAC-Port-Zuordnung)
- **VLAN** – Virtual LAN, logische Segmentierung auf dem Switch
- **Trunk-Port** – Port, der mehrere VLANs transportiert (802.1Q-Tagging)
- **PoE (Power over Ethernet)** – Stromversorgung ueber das Netzwerkkabel

**Erklaerung:** Ein Switch ist das zentrale Geraet im LAN. Er verbindet alle Endgeraete und Server. Durch die MAC-basierte Weiterleitung werden Frames gezielt zugestellt, was die Netzwerkleistung gegenueber einem Hub erheblich verbessert. In groesseren Netzen werden VLANs auf dem Switch konfiguriert, um Abteilungen logisch zu trennen.
