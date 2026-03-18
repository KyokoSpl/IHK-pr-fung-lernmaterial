# Grundlagen: 3.1.07 – Netzwerkrelevante Dienste

## DHCP (Dynamic Host Configuration Protocol)

**Definition:** DHCP ist ein Netzwerkprotokoll zur automatischen Vergabe von IP-Adressen und weiteren Netzwerkparametern an Clients. Es arbeitet auf OSI-Schicht 7 und nutzt UDP (Port 67 Server, Port 68 Client).

**Kernaussagen:**
- Zentrale, automatische IP-Adressvergabe im Netzwerk
- Vermeidet manuelle Konfiguration und IP-Adresskonflikte
- Vergibt neben der IP-Adresse auch: Subnetzmaske, Default Gateway, DNS-Server
- Adressen werden fuer eine bestimmte Zeit verliehen (Lease Time)
- DHCP-Server kann auf einem dedizierten Server, Router oder Firewall laufen

### Der DORA-Prozess

| Schritt | Name | Richtung | Typ | Beschreibung |
|---------|------|----------|-----|-------------|
| 1 | **D**iscover | Client → Netzwerk | Broadcast | Client sucht DHCP-Server (hat noch keine IP) |
| 2 | **O**ffer | Server → Client | Broadcast/Unicast | Server bietet eine IP-Adresse an |
| 3 | **R**equest | Client → Netzwerk | Broadcast | Client nimmt das Angebot an |
| 4 | **A**cknowledge | Server → Client | Broadcast/Unicast | Server bestaetigt die Zuweisung |

### ASCII-Darstellung: DORA-Prozess

```
Client (noch keine IP)              DHCP-Server (192.168.1.1)
  |                                        |
  |--- DHCP Discover (Broadcast) --------->|  "Gibt es einen DHCP-Server?"
  |    Src: 0.0.0.0, Dst: 255.255.255.255 |
  |                                        |
  |<-- DHCP Offer -------------------------|  "Hier, nimm 192.168.1.50"
  |    Angebotene IP: 192.168.1.50         |
  |    Subnetzmaske: 255.255.255.0         |
  |    Gateway: 192.168.1.1                |
  |    DNS: 192.168.1.1                    |
  |    Lease: 24 Stunden                   |
  |                                        |
  |--- DHCP Request (Broadcast) ---------->|  "Ich nehme 192.168.1.50"
  |                                        |
  |<-- DHCP Acknowledge -------------------|  "Bestaetigt, 192.168.1.50 ist deine"
  |                                        |
  |=== Client hat jetzt IP 192.168.1.50 ===|
```

### DHCP-Konfigurationsparameter

| Parameter | Beschreibung | Beispiel |
|-----------|-------------|---------|
| IP-Adressbereich (Pool/Scope) | Bereich vergebbarer Adressen | 192.168.1.50 – 192.168.1.200 |
| Subnetzmaske | Netz-/Hostanteil-Trennung | 255.255.255.0 (/24) |
| Default Gateway | Router-Adresse | 192.168.1.1 |
| DNS-Server | Namensaufloesung | 192.168.1.1 oder 8.8.8.8 |
| Lease Time | Gueltigkeitsdauer der Adresse | 86400 Sekunden (24 h) |
| DHCP-Reservierung | Feste IP fuer bestimmte MAC (statisches DHCP) | MAC AA:BB:CC:DD:EE:FF → 192.168.1.10 |

**Wichtige Begriffe:**
- **Lease** – Zeitlich begrenzte Zuweisung einer IP-Adresse
- **DHCP-Relay / IP-Helper** – Leitet DHCP-Broadcasts ueber Router hinweg an einen DHCP-Server in einem anderen Subnetz weiter
- **DHCP-Reservierung** – Feste IP-Zuweisung basierend auf der MAC-Adresse
- **APIPA** – Automatische IP (169.254.x.x), wenn kein DHCP-Server erreichbar ist

**Erklaerung:** Ohne DHCP muesste jeder PC manuell konfiguriert werden (IP, Maske, Gateway, DNS). Bei 200 PCs waere das fehleranfaellig und zeitaufwaendig. DHCP automatisiert diesen Prozess und reduziert Konfigurationsfehler.

---

## DNS (Domain Name System)

**Definition:** DNS ist ein hierarchisches, verteiltes Namenssystem, das Domainnamen (z.B. www.example.de) in IP-Adressen (z.B. 93.184.216.34) auflöst. Es arbeitet auf OSI-Schicht 7 und nutzt UDP/TCP Port 53.

**Kernaussagen:**
- Menschen merken sich Namen, Computer arbeiten mit IP-Adressen
- DNS uebersetzt in beide Richtungen: Name → IP (Forward Lookup) und IP → Name (Reverse Lookup)
- Hierarchisch aufgebaut: Root → TLD → SLD → Subdomains
- Verteiltes System: Kein einzelner Server kennt alle Eintraege
- Zwischenspeicherung (Caching) beschleunigt Anfragen

### DNS-Hierarchie

```
                        [Root-Server (.)]
                       /        |        \
                [.de]        [.com]      [.org]       ← Top-Level-Domains (TLD)
               /     \         |
        [example.de] [firma.de]  [google.com]         ← Second-Level-Domains (SLD)
           |
    [www.example.de]  [mail.example.de]               ← Subdomains / Hostnames
```

### DNS-Aufloesung (Rekursiv + Iterativ)

```
[Client-PC]                [Lokaler DNS-Server]        [Root]  [TLD .de]  [Autoritativ]
     |                            |                      |         |           |
     |-- "www.firma.de?" -------->|                      |         |           |
     |   (rekursive Anfrage)      |                      |         |           |
     |                            |-- "www.firma.de?" -->|         |           |
     |                            |<- "Frag .de-Server" -|         |           |
     |                            |                                |           |
     |                            |-- "www.firma.de?" ------------>|           |
     |                            |<- "Frag ns.firma.de" ----------|           |
     |                            |                                            |
     |                            |-- "www.firma.de?" ------------------------>|
     |                            |<- "93.184.216.34" -------------------------|
     |                            |                                            |
     |<- "93.184.216.34" ---------|                                            |
     |   (Antwort + Caching)      |                                            |
```

**Rekursive Anfrage:** Client fragt seinen DNS-Server und erwartet eine vollstaendige Antwort (der DNS-Server kuemmert sich um alles).

**Iterative Anfrage:** DNS-Server fragt andere Server und erhaelt jeweils Verweise auf den naechstzustaendigen Server.

### DNS-Record-Typen

| Record-Typ | Funktion | Beispiel |
|------------|----------|---------|
| A | Hostname → IPv4-Adresse | www.firma.de → 93.184.216.34 |
| AAAA | Hostname → IPv6-Adresse | www.firma.de → 2001:db8::1 |
| MX | Mail-Server fuer eine Domain | firma.de → mail.firma.de (Prioritaet 10) |
| CNAME | Alias fuer einen anderen Hostnamen | blog.firma.de → www.firma.de |
| NS | Zustaendiger Nameserver fuer eine Zone | firma.de → ns1.provider.de |
| PTR | IP-Adresse → Hostname (Reverse Lookup) | 34.216.184.93 → www.firma.de |
| SOA | Start of Authority, Metadaten der Zone | Primaerer NS, Serial, TTL |
| TXT | Texteintraege (SPF, DKIM, Verifikation) | v=spf1 include:_spf.google.com |
| SRV | Dienst-Lokalisierung | _sip._tcp.firma.de → sip.firma.de:5060 |

**Wichtige Begriffe:**
- **Zone** – Verwaltungsbereich eines DNS-Servers (z.B. firma.de)
- **Forward Lookup** – Name → IP-Adresse
- **Reverse Lookup** – IP-Adresse → Name (PTR-Record, in-addr.arpa)
- **TTL (Time to Live)** – Wie lange ein DNS-Eintrag gecacht werden darf
- **DNS-Forwarder** – Leitet Anfragen an externe DNS-Server weiter
- **DNS-Cache** – Zwischenspeicher fuer bereits aufgeloeste Namen

**Erklaerung:** Wenn du www.firma.de im Browser eingibst, fragt dein PC zuerst seinen konfigurierten DNS-Server (z.B. vom DHCP erhalten). Dieser prueft seinen Cache. Findet er keinen Eintrag, startet er eine iterative Abfrage ueber Root → TLD → autoritativen Server. Das Ergebnis wird zwischengespeichert (Caching), damit die naechste Anfrage schneller beantwortet wird.

---

## Proxy

**Definition:** Ein Proxy-Server ist ein Vermittler zwischen Client und Zielserver. Er nimmt Anfragen entgegen, leitet sie weiter und gibt die Antwort an den Client zurueck.

**Kernaussagen:**
- Arbeitet auf OSI-Schicht 7 (Application Layer)
- Kann Inhalte zwischenspeichern (Caching) → schnellerer Zugriff, weniger Bandbreite
- Kann den Zugriff auf bestimmte Websites blockieren (URL-Filter)
- Kann Anonymitaet bieten (Zielserver sieht nur die Proxy-IP)
- Zwei Haupttypen: Forward Proxy und Reverse Proxy

### Forward Proxy vs. Reverse Proxy

| Kriterium | Forward Proxy | Reverse Proxy |
|-----------|--------------|---------------|
| Position | Vor den Clients (im LAN) | Vor den Servern (in der DMZ) |
| Zweck | Clients kontrollieren/schuetzen | Server schuetzen/lastverteilen |
| Sicht | Server sieht nur den Proxy | Client sieht nur den Proxy |
| Typische Funktion | URL-Filter, Caching, Logging | Load Balancing, SSL-Terminierung, WAF |
| Beispiel | Squid Proxy im Firmennetz | nginx als Reverse Proxy vor Webservern |

### ASCII-Darstellung

**Forward Proxy:**
```
[Client-PC] → [Forward Proxy] → [Internet / Webserver]
                  ↑
         URL-Filter, Cache,
         Logging, Anonymisierung
         
→ Client muss Proxy als Gateway nutzen (manuell oder transparent)
→ Server sieht nur die IP des Proxys
```

**Reverse Proxy:**
```
[Internet / Client] → [Reverse Proxy] → [Webserver 1]
                           ↓           → [Webserver 2]
                     Load Balancing,    → [Webserver 3]
                     SSL-Terminierung,
                     WAF, Caching

→ Client weiss nicht, welcher Server antwortet
→ Reverse Proxy verteilt Last und schuetzt die Backend-Server
```

### Transparenter Proxy

**Kernaussagen:**
- Client muss keinen Proxy konfigurieren
- Der Netzwerkverkehr wird ueber Routing-Regeln automatisch zum Proxy umgeleitet
- Vorteil: Kein Konfigurationsaufwand auf den Clients
- Nachteil: HTTPS-Verkehr kann ohne Aufbrechen der Verschluesselung (SSL Inspection) nicht gefiltert werden

**Wichtige Begriffe:**
- **Caching** – Zwischenspeicherung haeufig angefragter Inhalte
- **URL-Filter / Content-Filter** – Blockierung bestimmter Websites oder Kategorien
- **SSL-Terminierung** – Reverse Proxy entschluesselt HTTPS und leitet intern unverschluesselt weiter
- **Load Balancing** – Verteilung der Anfragen auf mehrere Backend-Server
- **WAF (Web Application Firewall)** – Schutz vor Angriffen auf Webanwendungen (SQL Injection, XSS)

**Erklaerung:** In Unternehmen wird oft ein Forward Proxy eingesetzt, um den Internetzugang der Mitarbeiter zu kontrollieren (z.B. Social Media blockieren, Bandbreite sparen durch Caching). Ein Reverse Proxy steht vor den eigenen Webservern und verteilt die Last, terminiert SSL und schuetzt vor Angriffen.
