# Grundlagen: 3.1.06 – Standortuebergreifende Kommunikation

## IPsec (Internet Protocol Security)

**Definition:** IPsec ist eine Protokollsuite zur Absicherung der IP-Kommunikation auf OSI-Schicht 3. Es bietet Verschluesselung, Integritaetspruefung und Authentifizierung und wird hauptsaechlich fuer VPN-Verbindungen eingesetzt.

**Kernaussagen:**
- Arbeitet auf OSI-Schicht 3 (Vermittlungsschicht)
- Sichert die gesamte IP-Kommunikation (nicht nur einzelne Anwendungen)
- Zwei Protokolle: AH (Authentication Header) und ESP (Encapsulating Security Payload)
- Zwei Modi: Transportmodus und Tunnelmodus
- Schluesselaustausch ueber IKE (Internet Key Exchange)

### IPsec-Protokolle

| Protokoll | Funktion | Verschluesselung | Integritaet | Authentifizierung |
|-----------|----------|-------------------|-------------|-------------------|
| AH (Authentication Header) | Authentifizierung und Integritaet | Nein | Ja | Ja |
| ESP (Encapsulating Security Payload) | Verschluesselung + Authentifizierung | Ja | Ja | Ja |

→ **In der Praxis wird fast ausschliesslich ESP verwendet**, da ES auch Verschluesselung bietet.

### IPsec-Modi

| Modus | Beschreibung | Kapselung | Einsatz |
|-------|-------------|-----------|---------|
| Transportmodus | Nur die Nutzdaten (Payload) werden verschluesselt, IP-Header bleibt original | [IP-Header][ESP-Header][verschluesselte Payload] | Host-zu-Host (End-to-End) |
| Tunnelmodus | Gesamtes IP-Paket wird verschluesselt und in ein neues IP-Paket gekapselt | [Neuer IP-Header][ESP-Header][verschl. Original-IP-Paket] | Gateway-zu-Gateway (Site-to-Site VPN) |

### ASCII-Darstellung: IPsec-Modi

**Transportmodus:**
```
Original:     [IP-Header (Src→Dst)][TCP/UDP][Daten]
                                    ↓ ESP verschluesselt
IPsec:        [IP-Header (Src→Dst)][ESP-H][TCP/UDP][Daten][ESP-Trailer]

→ IP-Header bleibt unveraendert
→ Nur Payload ist geschuetzt
→ Quell- und Ziel-IP sind sichtbar
```

**Tunnelmodus:**
```
Original:     [IP-Header (Src→Dst)][TCP/UDP][Daten]
                     ↓ Gesamtes Paket wird verschluesselt
IPsec:        [Neuer IP-Header (GW-A→GW-B)][ESP-H][IP-Header][TCP/UDP][Daten][ESP-Tr]

→ Originales IP-Paket komplett verschluesselt
→ Neuer IP-Header fuer den Tunnel (Gateway-Adressen)
→ Quell- und Ziel-IP der Endgeraete sind verborgen
```

**Wichtige Begriffe:**
- **IKE (Internet Key Exchange)** – Protokoll zur Aushandlung der Sicherheitsparameter und Schluessel
- **SA (Security Association)** – Vereinbarung zwischen zwei Kommunikationspartnern ueber Sicherheitsparameter
- **SPI (Security Parameter Index)** – Identifiziert eine SA eindeutig
- **Perfect Forward Secrecy (PFS)** – Jede Sitzung nutzt eigene Schluessel, Kompromittierung eines Schluessels betrifft nicht andere Sitzungen

---

## Tunneling

**Definition:** Tunneling ist ein Verfahren, bei dem Datenpakete eines Protokolls in ein anderes Protokoll eingekapselt werden, um sie durch ein fremdes oder unsicheres Netzwerk zu transportieren.

**Kernaussagen:**
- Der aeussere Header dient dem Transport durch das oeffentliche Netz
- Der innere Header und die Nutzdaten sind geschuetzt (verschluesselt oder gekapselt)
- Tunneling ermoeglicht den Transport privater Adressen ueber das Internet
- Verschiedene Tunneling-Protokolle fuer verschiedene Einsatzzwecke

### Gaengige Tunneling-Protokolle

| Protokoll | OSI-Schicht | Verschluesselung | Beschreibung |
|-----------|-------------|-------------------|-------------|
| IPsec (ESP) | 3 | Ja (AES) | Standard fuer VPN, Site-to-Site und Remote Access |
| GRE (Generic Routing Encapsulation) | 3 | Nein | Kapselt beliebige Protokolle, oft mit IPsec kombiniert |
| L2TP (Layer 2 Tunneling Protocol) | 2 | Nein (benoetigt IPsec) | Kapselt Layer-2-Frames, oft mit IPsec fuer Verschluesselung |
| OpenVPN | 3–7 | Ja (TLS/SSL) | Open-Source-VPN-Loesung, flexibel, TCP oder UDP |
| WireGuard | 3 | Ja (ChaCha20) | Modernes, schlankes VPN-Protokoll, sehr performant |
| PPTP | 2 | Schwach (MPPE) | Veraltet, unsicher, nicht verwenden |
| SSL/TLS-VPN | 5–7 | Ja (TLS) | Browserbasiert, kein spezieller Client noetig |

### Tunneling-Prinzip (ASCII)

```
[PC-A im LAN A] → [VPN-Gateway A] ====Tunnel==== [VPN-Gateway B] → [PC-B im LAN B]
  192.168.1.10      203.0.113.1     INTERNET     198.51.100.1       192.168.2.20

Paket von PC-A an PC-B:
  Inneres Paket: [Src: 192.168.1.10 → Dst: 192.168.2.20][Daten]
  Aeusseres Paket: [Src: 203.0.113.1 → Dst: 198.51.100.1][ESP][Inneres Paket verschl.]

→ Im Internet sieht man nur die Gateway-Adressen
→ Die privaten IPs sind verschluesselt im Tunnel verborgen
```

**Erklaerung:** Tunneling ist vergleichbar mit einem Brief in einem Brief: Der innere Brief (Daten mit privaten Adressen) wird in einen aeusseren Umschlag (mit oeffentlichen Adressen) gesteckt. Die Post (Internet) befördert nur den aeusseren Umschlag. Am Ziel wird der aeussere Umschlag entfernt und der innere Brief zugestellt.

---

## VPN-Modelle

**Definition:** VPN-Modelle beschreiben die verschiedenen Verbindungsarten, ueber die verschluesselte Tunnel aufgebaut werden.

### Die drei VPN-Modelle

| Modell | Beschreibung | Initiator | Typischer Einsatz |
|--------|-------------|-----------|-------------------|
| Site-to-Site | Zwei Netzwerke werden ueber einen permanenten Tunnel verbunden | Router/Firewall beider Standorte | Filialvernetzung |
| End-to-Site (Remote Access) | Ein einzelner Client verbindet sich mit dem Firmennetz | VPN-Client auf dem Endgeraet | Homeoffice, Aussendienst |
| End-to-End | Verschluesselte Verbindung direkt zwischen zwei Endgeraeten | Beide Endgeraete | Spezialanwendungen, SSH-Tunnel |

### Site-to-Site VPN

```
[LAN Standort A]           [Internet]           [LAN Standort B]
192.168.1.0/24                                   192.168.2.0/24
      |                                               |
[VPN-Gateway A] =========IPsec Tunnel========= [VPN-Gateway B]
 203.0.113.1                                    198.51.100.1

- Tunnel wird automatisch zwischen den Gateways aufgebaut
- Clients bemerken den Tunnel nicht (transparent)
- Permanente Verbindung (Always-On)
- Typisches Protokoll: IPsec im Tunnelmodus
```

### End-to-Site VPN (Remote Access)

```
[Homeoffice-Laptop]                            [Firmennetz]
      |                                         192.168.1.0/24
      |                                              |
[VPN-Client] ========VPN-Tunnel======== [VPN-Gateway/Firewall]
  (dynamische IP)                          203.0.113.1

- Mitarbeiter startet VPN-Client und authentifiziert sich
- Laptop erhaelt eine IP-Adresse aus dem Firmennetz (z.B. 192.168.1.200)
- Zugriff auf interne Ressourcen wie im Buero
- Typische Protokolle: IPsec, OpenVPN, WireGuard, SSL-VPN
```

### End-to-End VPN

```
[PC-A] =========verschluesselter Tunnel========= [PC-B]

- Direkte Ende-zu-Ende-Verschluesselung
- Kein Gateway noetig (beide Endgeraete haben VPN-Software)
- Beispiel: SSH-Tunnel, Peer-to-Peer-VPN
- Seltener in der Praxis
```

**Wichtige Begriffe:**
- **VPN-Gateway** – Router oder Firewall, der den VPN-Tunnel terminiert
- **VPN-Client** – Software auf dem Endgeraet (z.B. OpenVPN, Cisco AnyConnect)
- **Split Tunneling** – Nur Firmenverkehr ueber VPN, privater Traffic direkt ins Internet
- **Full Tunneling** – Gesamter Traffic ueber VPN (sicherer, aber langsamer)
- **Multi-Factor Authentication (MFA)** – Zusaetzliche Authentifizierung (z.B. Token, SMS) neben Passwort

**Erklaerung:** Site-to-Site-VPNs ersetzen teure Standleitungen durch guenstige Internet-Anbindungen. End-to-Site-VPNs sind seit der Zunahme von Homeoffice essentiell. Die Wahl des VPN-Protokolls haengt von den Anforderungen ab: IPsec fuer Site-to-Site, OpenVPN/WireGuard fuer Remote Access, SSL-VPN fuer browserbasierte Loesungen.
