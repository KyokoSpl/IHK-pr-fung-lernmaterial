# Vertiefung und Uebungen: 3.1.06 – Standortuebergreifende Kommunikation

## Vertiefung

### IPsec Transportmodus vs. Tunnelmodus – Detailvergleich

| Kriterium | Transportmodus | Tunnelmodus |
|-----------|----------------|-------------|
| Verschluesselung | Nur Payload | Gesamtes original IP-Paket |
| IP-Header | Original bleibt erhalten | Neuer IP-Header (Gateway-Adressen) |
| Sichtbare IPs | Quell- und Ziel-IP der Endgeraete | Nur Gateway-IPs sichtbar |
| Overhead | Geringer | Hoeher (zusaetzlicher IP-Header) |
| Einsatz | Host-zu-Host (selten) | Gateway-zu-Gateway (Site-to-Site VPN) |
| Datenschutz | IP-Adressen der Endgeraete erkennbar | IP-Adressen verborgen |

### VPN-Protokolle im Vergleich

| Kriterium | IPsec | OpenVPN | WireGuard | L2TP/IPsec | SSL-VPN |
|-----------|-------|---------|-----------|------------|---------|
| OSI-Schicht | 3 | 3–7 | 3 | 2–3 | 5–7 |
| Verschluesselung | AES, 3DES | AES (via TLS) | ChaCha20, Curve25519 | AES (via IPsec) | AES (via TLS) |
| Transport | IP-Protokoll | TCP oder UDP | UDP | UDP (Port 1701) | TCP (Port 443) |
| Performance | Hoch | Mittel | Sehr hoch | Mittel | Mittel |
| Konfiguration | Komplex | Mittel | Einfach | Mittel | Einfach |
| NAT-Traversal | Problematisch (NAT-T noetig) | Kein Problem (TCP/UDP) | Kein Problem (UDP) | NAT-T noetig | Kein Problem (HTTPS-Port) |
| Vorteil | Standard, Site-to-Site | Flexibel, Open Source | Schnell, schlank | Weit verbreitet | Browserbasiert |
| Nachteil | Komplex, NAT-Probleme | Langsamer als WireGuard | Noch wenig Enterprise-Support | Doppelte Kapselung | Nur Remote Access |

### IPsec-Verbindungsaufbau (IKE Phase 1 + 2)

```
VPN-Gateway A                              VPN-Gateway B
      |                                          |
      |--- IKE Phase 1 (Main Mode) ------------->|
      |    Aushandlung: Verschluesselung,        |
      |    Hash, DH-Gruppe, Authentifizierung     |
      |<-- IKE SA steht (sicherer Kanal) --------|
      |                                          |
      |--- IKE Phase 2 (Quick Mode) ------------>|
      |    Aushandlung: IPsec-SA,                |
      |    ESP/AH, Schluessel fuer Datentunnel   |
      |<-- IPsec SA steht (Datentunnel) ---------|
      |                                          |
      |========= Verschluesselter Tunnel ========|
```

**Phase 1 (IKE SA):** Sicherer Verwaltungskanal wird aufgebaut. Beide Seiten tauschen Sicherheitsparameter aus und authentifizieren sich (Pre-Shared Key oder Zertifikat).

**Phase 2 (IPsec SA):** Ueber den sicheren Kanal aus Phase 1 werden die Parameter fuer den eigentlichen Datentunnel ausgehandelt (ESP, AES, Schluessel).

### Praxisszenario: Standortvernetzung

```
Standort Berlin                 Internet                Standort Muenchen
192.168.10.0/24                                          192.168.20.0/24
      |                                                       |
  [Switch]                                                [Switch]
      |                                                       |
  [Firewall/VPN-GW]======IPsec Tunnel======[Firewall/VPN-GW]
  Public: 203.0.113.10                      Public: 198.51.100.20
      |                                                       |
  [Router]---Internet---[Router]

Konfiguration:
- IPsec Tunnelmodus mit ESP (AES-256)
- IKE v2 mit Pre-Shared Key oder Zertifikaten
- PFS aktiviert (Diffie-Hellman Gruppe 14+)
- Crypto-ACL: 192.168.10.0/24 ↔ 192.168.20.0/24
```

### Split Tunneling vs. Full Tunneling

```
Full Tunneling:
[Laptop] --alle Pakete--> [VPN-Tunnel] --> [Firmen-Gateway] --> [Internet]
                                                              --> [Firmennetz]
→ Alles geht ueber den Tunnel, auch privater Traffic
→ Vorteil: Sicherheit (Firm-Firewall filtert alles)
→ Nachteil: Hoeherer Bandbreitenbedarf am Gateway

Split Tunneling:
[Laptop] --Firmen-Traffic--> [VPN-Tunnel] --> [Firmennetz]
         --Privat-Traffic--> [Internet direkt]
→ Nur Firmenverkehr geht durch den Tunnel
→ Vorteil: Weniger Last am Gateway, schnellerer Internetzugang
→ Nachteil: Client ist gleichzeitig im Internet und im LAN exponiert
```

### Typische Pruefungsaspekte

- IPsec Transportmodus vs. Tunnelmodus erklaeren und vergleichen
- Site-to-Site vs. End-to-Site VPN unterscheiden und Szenarien zuordnen
- Tunneling-Prinzip beschreiben (Kapselung, innerer/aeusserer Header)
- VPN-Protokolle benennen und grundlegende Eigenschaften kennen
- Split vs. Full Tunneling: Vor- und Nachteile
- IKE Phase 1 und Phase 2 grob beschreiben koennen

### Haeufige Fehler

- IPsec Transportmodus wird als "unsicher" bezeichnet – er ist verschluesselt, aber die IP-Adressen sind sichtbar
- L2TP wird als eigenstaendig verschluesselt behandelt – L2TP hat KEINE Verschluesselung, benoetigt IPsec
- PPTP wird empfohlen – PPTP ist veraltet und unsicher, nicht verwenden
- VPN wird mit Anonymisierung gleichgesetzt – VPN verschluesselt den Tunnel, anonymisiert aber nicht automatisch
- Tunnelmodus und Transportmodus werden verwechselt: Tunnel = ganzes Paket, Transport = nur Payload

---

## Uebungen

**Aufgabe 1:** Erklaere den Unterschied zwischen IPsec-Transportmodus und IPsec-Tunnelmodus. Welcher wird fuer Site-to-Site-VPN verwendet?

**Aufgabe 2:** Ein Unternehmen hat den Hauptsitz in Hamburg und eine Filiale in Leipzig. Beide Standorte sollen dauerhaft vernetzt werden. Beschreibe die VPN-Loesung: VPN-Modell, Protokoll, Modus und welche Geraete benoetigt werden.

**Aufgabe 3:** Ein Aussendienst-Mitarbeiter muss von seinem Laptop im Hotel auf den Firmen-Fileserver zugreifen. Welches VPN-Modell und welches Protokoll schlage vor? Begruende.

**Aufgabe 4:** Erklaere das Tunneling-Prinzip. Was passiert mit den IP-Adressen im Tunnelmodus?

**Aufgabe 5:** Vergleiche OpenVPN und WireGuard hinsichtlich Performance, Konfigurationsaufwand und Transportprotokoll.

**Aufgabe 6:** Was ist der Unterschied zwischen Split Tunneling und Full Tunneling? Nenne jeweils einen Vorteil und ein Risiko.

**Aufgabe 7:** Warum hat L2TP alleine keine Verschluesselung und mit welchem Protokoll wird es typischerweise kombiniert?

---

## Loesungen

**Aufgabe 1:**
- **Transportmodus:** Nur die Nutzdaten (Payload) werden verschluesselt. Der originale IP-Header bleibt erhalten. Die Quell- und Ziel-IP der Endgeraete sind sichtbar. Einsatz: Host-zu-Host-Kommunikation.
- **Tunnelmodus:** Das gesamte originale IP-Paket wird verschluesselt und in ein neues Paket mit neuem IP-Header gekapselt. Nur die Gateway-Adressen sind sichtbar. Einsatz: Site-to-Site-VPN.
→ Fuer Site-to-Site-VPN wird der **Tunnelmodus** verwendet.

**Aufgabe 2:**
- VPN-Modell: Site-to-Site VPN
- Protokoll: IPsec (ESP) im Tunnelmodus
- Modus: Tunnelmodus (Gateway-zu-Gateway)
- Geraete: Je ein VPN-faehiger Router oder eine Firewall an beiden Standorten (z.B. pfSense, Cisco ASA). Beide Gateways benoetigen eine oeffentliche IP-Adresse und eine Internetanbindung.
- Der Tunnel wird automatisch zwischen den Gateways aufgebaut. Clients an beiden Standorten koennen transparent ueber den Tunnel kommunizieren.

**Aufgabe 3:**
- VPN-Modell: End-to-Site (Remote Access)
- Protokoll: OpenVPN oder WireGuard (alternativ: SSL-VPN wenn nur Webzugriff noetig)
- Begruendung: Der Mitarbeiter nutzt einen VPN-Client auf dem Laptop, der sich mit dem VPN-Gateway der Firma verbindet. OpenVPN/WireGuard arbeiten ueber UDP und haben wenig Probleme mit NAT und Firewalls in Hotels. Authentifizierung ueber Benutzername + Zertifikat + MFA fuer maximale Sicherheit.

**Aufgabe 4:**
Tunneling kapselt ein Datenpaket (inneres Paket) in ein anderes Paket (aeusseres Paket) ein. Im IPsec-Tunnelmodus wird das gesamte originale IP-Paket verschluesselt und als Nutzdaten in ein neues IP-Paket eingesetzt. Der neue (aeussere) IP-Header enthaelt die Adressen der VPN-Gateways. Die originalen (inneren) IP-Adressen der Endgeraete sind verschluesselt und damit im Internet nicht sichtbar.

**Aufgabe 5:**
| Kriterium | OpenVPN | WireGuard |
|-----------|---------|-----------|
| Performance | Mittel (Userspace, TLS-Overhead) | Sehr hoch (Kernel-Integration, schlankes Protokoll) |
| Konfiguration | Mittel (viele Optionen, Zertifikate) | Einfach (wenige Zeilen Konfiguration) |
| Transport | TCP oder UDP (wahlweise) | Nur UDP |
| Verbreitung | Sehr weit verbreitet, ausgereift | Neuer, zunehmend adoptiert |

**Aufgabe 6:**
- **Split Tunneling:** Nur Firmenverkehr geht ueber den VPN-Tunnel, privater Traffic direkt ins Internet. Vorteil: Weniger Last am VPN-Gateway, schnellerer privater Internetzugang. Risiko: Der Client ist gleichzeitig mit dem Internet und dem Firmennetz verbunden – Malware koennte ueber den Client ins Firmennetz gelangen.
- **Full Tunneling:** Gesamter Traffic geht ueber den VPN-Tunnel. Vorteil: Alle Daten werden durch die Unternehmens-Firewall gefiltert. Risiko: Hoeherer Bandbreitenbedarf am VPN-Gateway, langsamerer Internetzugang fuer den Nutzer.

**Aufgabe 7:**
L2TP (Layer 2 Tunneling Protocol) kapselt Layer-2-Frames und erstellt einen Tunnel, bietet aber selbst keine Verschluesselung und keine Integritaetspruefung der Daten. Daher wird L2TP typischerweise mit IPsec kombiniert (L2TP/IPsec). IPsec uebernimmt die Verschluesselung (ESP), waehrend L2TP die Tunnelung bereitstellt.
