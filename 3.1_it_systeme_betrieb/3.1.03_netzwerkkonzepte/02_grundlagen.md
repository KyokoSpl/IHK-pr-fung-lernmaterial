# Grundlagen: 3.1.03 – Netzwerkkonzepte benennen und charakterisieren

## Ausdehnung: LAN / WAN / MAN / GAN

**Definition:** Netzwerke werden nach ihrer geografischen Ausdehnung klassifiziert. Die Reichweite bestimmt Technologien, Uebertragungsraten und Kosten.

| Typ | Name | Ausdehnung | Beispiel | Typische Technologie |
|-----|------|-----------|----------|---------------------|
| PAN | Personal Area Network | < 10 m | Bluetooth-Geraete | Bluetooth, NFC |
| LAN | Local Area Network | Gebaeude/Campus | Buero-Netzwerk | Ethernet, WLAN |
| MAN | Metropolitan Area Network | Stadt/Region | Stadtnetz, Uni-Verbund | Glasfaser, Metro Ethernet |
| WAN | Wide Area Network | Laender/Kontinente | Unternehmens-WAN | MPLS, Glasfaser, Internet |
| GAN | Global Area Network | Weltweit | Internet | Internet, Seekabel, Satellit |

**Wichtige Begriffe:**
- **LAN** – Netzwerk in Eigenverantwortung (eigener Switch, eigener Router)
- **WAN** – Verbindung zwischen entfernten LANs, oft ueber Provider-Leitungen
- **Intranet** – Firmeninternes Netzwerk (LAN/WAN mit internen Diensten)
- **Extranet** – Erweiterung des Intranets fuer externe Partner

---

## Bluetooth

**Definition:** Bluetooth ist ein Kurzstreckenfunkstandard (IEEE 802.15.1) fuer den Datenaustausch zwischen Geraeten im PAN-Bereich.

**Kernaussagen:**
- Frequenz: 2,4 GHz ISM-Band
- Reichweite: je nach Klasse 1 m bis 100 m
- Versionen: Bluetooth 4.0 (BLE – Low Energy), 5.0 (erhoehte Reichweite und Datenrate)
- Einsatz: Headsets, Tastaturen, Maeuse, IoT-Sensoren, Smartwatches
- Kopplungsprozess: Pairing mit PIN oder automatisch (BLE)
- Bluetooth bildet ein Piconet (bis zu 7 aktive Geraete um einen Master)

**Wichtige Begriffe:**
- **BLE (Bluetooth Low Energy)** – Energiesparende Variante fuer IoT
- **Piconet** – Kleinstnetzwerk aus einem Master und bis zu 7 Slaves
- **Pairing** – Kopplungsprozess zweier Bluetooth-Geraete

---

## Datenuebertragungsrate

**Definition:** Die Datenuebertragungsrate gibt an, wie viele Bits pro Sekunde ueber ein Medium uebertragen werden koennen.

**Kernaussagen:**
- Einheit: bit/s (bps), kbit/s, Mbit/s, Gbit/s
- Achtung: 1 Byte = 8 Bit → 100 Mbit/s ≈ 12,5 MByte/s (theoretisch)
- Bruttodatenrate: Theoretisches Maximum (inklusive Header, Overhead)
- Nettodatenrate / Durchsatz: Tatsaechlich nutzbare Datenrate
- Latenz: Verzoegerung zusaetzlich zur Datenrate relevant

**Gaengige Netzwerkstandards:**

| Standard | Datenrate | Medium | Kategorie |
|----------|-----------|--------|-----------|
| Fast Ethernet (100BASE-TX) | 100 Mbit/s | Kupfer (Cat5) | LAN |
| Gigabit Ethernet (1000BASE-T) | 1 Gbit/s | Kupfer (Cat5e/Cat6) | LAN |
| 10-Gigabit Ethernet | 10 Gbit/s | Cat6a/Glasfaser | Backbone |
| WLAN 802.11n (Wi-Fi 4) | bis 600 Mbit/s | Funk 2,4/5 GHz | WLAN |
| WLAN 802.11ac (Wi-Fi 5) | bis 6,9 Gbit/s | Funk 5 GHz | WLAN |
| WLAN 802.11ax (Wi-Fi 6) | bis 9,6 Gbit/s | Funk 2,4/5/6 GHz | WLAN |

**Wichtige Begriffe:**
- **Bandbreite** – Maximale Uebertragungskapazitaet eines Mediums
- **Durchsatz / Throughput** – Tatsaechlich uebertragene Datenrate
- **Latenz** – Verzoegerungszeit der Datenuebertragung
- **Overhead** – Zusaetzliche Daten durch Header und Protokolle

---

## Drahtlose Netzwerke: PAN / WLAN / Mesh

**Definition:** Drahtlose Netzwerke nutzen Funktechnologien anstelle von Kabeln zur Datenuebertragung.

### WLAN (Wireless LAN)

**Kernaussagen:**
- IEEE-Standard: 802.11 (a/b/g/n/ac/ax)
- Frequenzen: 2,4 GHz (groessere Reichweite) und 5 GHz (hoehere Datenrate)
- Infrastruktur-Modus: Access Point als zentrale Vermittlungsstelle
- Ad-hoc-Modus: Direkte Verbindung zwischen Geraeten
- SSID: Name des Funknetzwerks

### Mesh-Netzwerk

**Kernaussagen:**
- Vermaschtes Netzwerk: Jeder Knoten kann Daten weiterleiten
- Selbstheilend: Bei Ausfall eines Knotens wird automatisch ein alternativer Weg gewaehlt
- Einsatz: Grossflaechige WLAN-Abdeckung, IoT-Netzwerke
- Beispiel: WLAN-Mesh-Systeme fuer Wohnungen/Bueros

---

## Netzwerkplan

**Definition:** Ein Netzwerkplan dokumentiert die Struktur eines Netzwerks grafisch. Er dient der Planung, Administration und Fehlersuche.

**Kernaussagen:**
- **Physischer Netzwerkplan:** Zeigt tatsaechliche Geraete, Kabelwege, Raeume, Patchfelder
- **Logischer Netzwerkplan:** Zeigt IP-Adressen, Subnetze, VLANs, Routing-Wege
- Muss aktuell gehalten werden (Aenderungsmanagement)
- Werkzeuge: Visio, draw.io, PRTG, Netzwerkscanner

**Wichtige Begriffe:**
- **Dokumentation** – Netzwerkplaene sind Teil der IT-Dokumentation
- **Patchfeld** – Zentrale Anschlussleiste im Netzwerkschrank fuer strukturierte Verkabelung

---

## Netzwerktopologie

**Definition:** Eine Netzwerktopologie beschreibt die physische oder logische Anordnung von Geraeten und Verbindungen in einem Netzwerk.

| Topologie | Beschreibung | Vorteile | Nachteile |
|-----------|-------------|----------|-----------|
| Stern | Alle Geraete an zentralem Knoten (Switch/Hub) | Einfache Erweiterung, Ausfall eines Geraets betrifft nur dieses | Zentraler Knoten = Single Point of Failure |
| Bus | Alle Geraete an einem gemeinsamen Kabel | Guenstig, einfache Installation | Kollisionen, Kabelbruch = Totalausfall |
| Ring | Geraete in einer geschlossenen Schleife verbunden | Deterministischer Zugriff (Token) | Ausfall eines Geraets unterbricht den Ring |
| Mesh (Vollvermascht) | Jedes Geraet mit jedem verbunden | Hoechste Ausfallsicherheit, redundante Wege | Sehr viele Verbindungen, teuer |
| Mesh (Teilvermascht) | Wichtige Knoten mehrfach verbunden | Guter Kompromiss aus Redundanz und Kosten | Komplexere Planung |
| Baum | Hierarchische Sterntopologie | Skalierbar, strukturiert | Root-Knoten = Single Point of Failure |

**Erklaerung:** In der Praxis werden heute fast ausschliesslich Stern-Topologien verwendet (Switch im Zentrum). Backbone-Netze nutzen oft Teilvermaschung fuer Redundanz. Bus- und Ring-Topologien sind historisch relevant (Thin Ethernet, Token Ring).

---

## Sicherheit in Drahtlosnetzen

**Definition:** Sicherheitsmassnahmen zum Schutz von WLAN-Netzwerken vor unerlaubtem Zugriff und Abhoeren.

**Verschluesselungsverfahren:**

| Standard | Verschluesselung | Sicherheit | Status |
|----------|-----------------|------------|--------|
| WEP | RC4 (40/104 Bit) | Sehr unsicher | Veraltet, nicht verwenden |
| WPA | TKIP (RC4-basiert) | Unsicher | Veraltet |
| WPA2 | AES-CCMP (128 Bit) | Sicher | Aktueller Standard |
| WPA3 | AES-GCMP, SAE | Sehr sicher | Neuester Standard |

**Weitere Sicherheitsmassnahmen:**
- SSID verbergen (Hidden SSID) – erschwert das Auffinden, kein echter Schutz
- MAC-Filterung – nur bekannte MAC-Adressen duerfen sich verbinden (kann umgangen werden)
- 802.1X-Authentifizierung – Enterprise-WLAN mit RADIUS-Server
- Gastnetz trennen – Gaeste erhalten eigenes VLAN ohne Zugriff aufs Firmennetz

**Wichtige Begriffe:**
- **WPA2-Personal (PSK)** – Vorab geteilter Schluessel (Pre-Shared Key), fuer kleine Netze
- **WPA2-Enterprise (802.1X)** – Individuelle Authentifizierung ueber RADIUS, fuer Unternehmen
- **SAE (Simultaneous Authentication of Equals)** – Schluesselaustausch in WPA3, schuetzt vor Offline-Woerterbuch-Angriffen
- **KRACK** – Known Reinstallation Attack, Schwachstelle in WPA2 (durch Updates behoben)

---

## Sicherheitskonzepte

**Definition:** Uebergeordnete Strategien zum Schutz von Netzwerken vor Bedrohungen.

**Kernaussagen:**
- **Defense in Depth:** Mehrere Sicherheitsschichten (Firewall + IDS + Segmentierung + Endpoint Security)
- **Netzwerksegmentierung:** Aufteilung in Zonen (z.B. Server-VLAN, Client-VLAN, Gast-VLAN)
- **DMZ:** Demilitarisierte Zone fuer oeffentliche Dienste (Webserver, Mailserver)
- **Zero Trust:** Kein implizites Vertrauen, jede Anfrage wird verifiziert
- **Least Privilege:** Nur minimale noetige Rechte zuweisen
- **Haertung (Hardening):** Deaktivieren unnoetig Dienste, sichere Konfiguration

---

## Strukturierte Verkabelung

**Definition:** Normgerechter, hierarchischer Aufbau der Netzwerkverkabelung in Gebaeuden und Standorten nach EN 50173 / ISO 11801.

**Drei Ebenen:**

| Ebene | Name | Bereich | Typisches Medium | Laenge |
|-------|------|---------|-------------------|--------|
| Primaer | Gelaendeverkabelung (Campus Backbone) | Gebaeude zu Gebaeude | Glasfaser (Singlemode) | bis mehrere km |
| Sekundaer | Gebaeudeverkabelung (Building Backbone) | Stockwerk zu Stockwerk | Glasfaser (Multimode) | bis 500 m |
| Tertiaer | Etagenverkabelung (Horizontal Cabling) | Verteilerschrank zu Arbeitsplatz | Kupfer (Cat6/6a/7) | max. 90 m + 10 m Patchkabel |

### ASCII-Darstellung: Strukturierte Verkabelung

```
    [Gebaeude A]                              [Gebaeude B]
         |                                         |
    [Standortverteiler (SV)]---Primaer (Glas)---[Standortverteiler (SV)]
         |                                         |
    [Gebaeudev. (GV)]---Sekundaer (Glas)---[Gebaeudev. (GV)]
         |                                         |
    [Etagenv. (EV)]---Tertiaer (Kupfer)---[Datendose am Arbeitsplatz]
```

**Wichtige Begriffe:**
- **Patchfeld** – Anschlussfeld im Verteilerschrank
- **Patchkabel** – Flexibles Kabel von Patchfeld zu Switch oder von Datendose zu PC
- **Cat5e / Cat6 / Cat6a / Cat7** – Kupferkabelkategorien (Cat6a fuer 10 Gbit/s)
- **Singlemode-Glasfaser** – Fuer grosse Distanzen (ein Lichtmodus)
- **Multimode-Glasfaser** – Fuer kuerzere Distanzen (mehrere Lichtmodi)

---

## VLAN (Virtual LAN)

**Definition:** Ein VLAN ist eine logische Segmentierung eines physischen Netzwerks auf OSI-Schicht 2, die Broadcast-Domaenen trennt, ohne physisch getrennte Switches zu benoetigen.

**Kernaussagen:**
- Ports eines Switches werden einem VLAN zugeordnet
- Geraete in verschiedenen VLANs koennen ohne Router/L3-Switch NICHT kommunizieren
- Jedes VLAN bildet eine eigene Broadcast-Domaene
- Trunk-Ports transportieren mehrere VLANs ueber ein Kabel (802.1Q-Tagging)
- Vorteile: Sicherheit, Performance, Flexibilitaet

**VLAN-Typen:**
- **Port-basiertes VLAN:** Switch-Port wird einem VLAN fest zugeordnet (gaengigste Methode)
- **Tagged VLAN (802.1Q):** VLAN-ID wird im Ethernet-Frame markiert (fuer Trunks)
- **Untagged / Native VLAN:** Frames ohne VLAN-Tag gehoeren zum Native VLAN

**Wichtige Begriffe:**
- **Access Port** – Port gehoert zu genau einem VLAN (fuer Endgeraete)
- **Trunk Port** – Port transportiert mehrere VLANs (zwischen Switches oder zum Router)
- **802.1Q** – Standard fuer VLAN-Tagging im Ethernet-Frame
- **Inter-VLAN-Routing** – Routing zwischen VLANs ueber L3-Switch oder Router

---

## VPN (Virtual Private Network)

**Definition:** Ein VPN stellt eine verschluesselte Verbindung ueber ein oeffentliches Netzwerk (Internet) her, sodass Daten sicher uebertragen werden.

**Kernaussagen:**
- Erzeugt einen verschluesselten "Tunnel" durch das Internet
- Schutzziele: Vertraulichkeit, Integritaet, Authentizitaet
- Zwei Haupttypen: Site-to-Site und End-to-Site (Remote Access)

**VPN-Typen:**

| Typ | Beschreibung | Einsatz |
|-----|-------------|---------|
| Site-to-Site | Verbindung zweier Standort-Netzwerke | Filialen anbinden |
| End-to-Site (Remote Access) | Einzelner Client verbindet sich mit Firmennetz | Homeoffice, Aussendienst |
| End-to-End | Direkte Verschluesselung zwischen zwei Endgeraeten | Spezialanwendungen |

**Wichtige Begriffe:**
- **Tunnel** – Verschluesselte Verbindung durch ein oeffentliches Netz
- **Split Tunneling** – Nur Firmendaten gehen ueber VPN, privater Traffic direkt ins Internet
- **Full Tunneling** – Gesamter Traffic geht ueber VPN

---

## Zugriffskontrolle im Netzwerk (RADIUS, Kerberos)

**Definition:** Protokolle und Verfahren zur Authentifizierung, Autorisierung und Abrechnung (AAA) im Netzwerk.

### RADIUS (Remote Authentication Dial-In User Service)

**Kernaussagen:**
- AAA-Protokoll: Authentication, Authorization, Accounting
- Zentraler Authentifizierungsserver fuer WLAN (802.1X), VPN und Netzwerkzugang
- Client (z.B. WLAN-Access-Point) leitet Anmeldedaten an RADIUS-Server weiter
- RADIUS prueft Credentials gegen Verzeichnisdienst (z.B. Active Directory)
- Port: 1812 (Authentication), 1813 (Accounting)

### Kerberos

**Kernaussagen:**
- Authentifizierungsprotokoll fuer Netzwerke (Standard in Windows-Domaenen / Active Directory)
- Ticket-basiert: Nach der Anmeldung erhaelt der Benutzer ein Ticket Granting Ticket (TGT)
- Single Sign-On: Ein Login genuegt fuer den Zugriff auf verschiedene Dienste
- Zeitstempel verhindern Replay-Angriffe (Uhrsynchronisation erforderlich)
- Port: 88

**Wichtige Begriffe:**
- **AAA** – Authentication (wer?), Authorization (was darf?), Accounting (was wurde gemacht?)
- **802.1X** – Standard fuer portbasierte Netzwerkzugriffskontrolle
- **TGT (Ticket Granting Ticket)** – Kerberos-Ticket fuer den Zugang zu weiteren Diensten
- **KDC (Key Distribution Center)** – Zentraler Kerberos-Server
