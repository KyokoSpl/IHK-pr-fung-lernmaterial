# Vertiefung und Uebungen: 3.1.07 – Netzwerkrelevante Dienste

## Vertiefung

### DHCP – Vertiefung

#### Lease-Erneuerung

```
Lease Time: 24 Stunden

Nach 50 % (12 h): Client versucht, Lease beim gleichen Server zu verlaengern (Unicast)
  → Server bestaetigt → Lease-Timer wird zurueckgesetzt

Nach 87,5 % (21 h): Falls der erste Versuch scheitert: Client sendet erneut (Broadcast)
  → Jeder DHCP-Server kann antworten

Nach 100 %: Lease laeuft ab
  → Client verliert IP-Adresse und startet neuen DORA-Prozess
```

#### DHCP-Relay (IP-Helper)

```
[LAN A: 192.168.10.0/24]        [LAN B: 192.168.20.0/24]
      |                                |
   [Switch]                        [DHCP-Server]
      |                                |
   [Router mit DHCP-Relay]-------------|
   
Problem: DHCP Discover ist ein Broadcast und wird vom Router nicht weitergeleitet.
Loesung: DHCP-Relay auf dem Router konfigurieren.
  → Router nimmt DHCP-Broadcast aus LAN A entgegen
  → Router leitet ihn als Unicast an den DHCP-Server in LAN B weiter
  → DHCP-Server antwortet an den Router
  → Router gibt die Antwort an den Client in LAN A zurueck
```

#### Haeufige DHCP-Probleme

| Problem | Ursache | Loesung |
|---------|---------|---------|
| Client erhaelt 169.254.x.x | DHCP-Server nicht erreichbar | Server pruefen, Netzwerk pruefen |
| IP-Adresskonflikt | Doppelte IP-Vergabe | Pool pruefen, Reservierungen pruefen |
| Falsches Gateway/DNS | Falsche DHCP-Konfiguration | DHCP-Scope-Optionen pruefen |
| Rogue DHCP-Server | Unbefugter DHCP-Server im Netz | DHCP-Snooping auf dem Switch aktivieren |

---

### DNS – Vertiefung

#### DNS-Abfragetypen im Detail

| Abfragetyp | Beschreibung |
|------------|-------------|
| Rekursiv | Client erwartet eine vollstaendige Antwort. Der gefragte Server muss die Aufloesung komplett durchfuehren. Typisch: Client → lokaler DNS-Server. |
| Iterativ | Gefragter Server liefert die beste bekannte Antwort oder einen Verweis auf den naechsten Server. Typisch: DNS-Server untereinander. |
| Reverse Lookup | IP-Adresse → Hostname. Nutzt PTR-Records in der in-addr.arpa-Zone. |

#### DNS-Dienstaufloesung – Vollstaendiges Beispiel

**Anfrage: www.ihk-berlin.de**

```
1. Client prueft lokalen DNS-Cache → kein Eintrag
2. Client prueft hosts-Datei → kein Eintrag
3. Client fragt konfigurierten DNS-Server (z.B. 192.168.1.1) [rekursiv]
4. DNS-Server prueft eigenen Cache → kein Eintrag
5. DNS-Server fragt Root-Server (z.B. a.root-servers.net) [iterativ]
   → Antwort: "Frag den .de-Nameserver (z.B. a.nic.de)"
6. DNS-Server fragt .de-Nameserver [iterativ]
   → Antwort: "Frag den Nameserver von ihk-berlin.de (z.B. ns1.ihk-berlin.de)"
7. DNS-Server fragt ns1.ihk-berlin.de [iterativ]
   → Antwort: "www.ihk-berlin.de = 185.xx.xx.xx" (A-Record)
8. DNS-Server cached das Ergebnis (TTL z.B. 3600 s) und antwortet dem Client
9. Client cached das Ergebnis und verbindet sich mit 185.xx.xx.xx
```

#### nslookup / dig – Diagnose-Befehle

```
# Forward Lookup (Name → IP)
nslookup www.firma.de
dig www.firma.de A

# Reverse Lookup (IP → Name)
nslookup 93.184.216.34
dig -x 93.184.216.34

# MX-Record abfragen
nslookup -type=MX firma.de
dig firma.de MX

# Bestimmten DNS-Server befragen
nslookup www.firma.de 8.8.8.8
dig @8.8.8.8 www.firma.de
```

#### Haeufige DNS-Probleme

| Problem | Symptom | Ursache | Loesung |
|---------|---------|---------|---------|
| Name wird nicht aufgeloest | "Server nicht gefunden" | DNS-Server falsch konfiguriert oder nicht erreichbar | DNS-Konfiguration pruefen (ipconfig /all) |
| Alte IP wird zurueckgegeben | Website nicht erreichbar nach Serverumzug | DNS-Cache enthaelt veralteten Eintrag | Cache leeren: ipconfig /flushdns |
| Interne Namen funktionieren nicht | Intern: Fehler, Extern: OK | Interner DNS-Server nicht als primaer konfiguriert | DNS-Reihenfolge pruefen, Split DNS konfigurieren |

---

### Proxy – Vertiefung

#### Forward Proxy – Typische Konfiguration

```
Unternehmensnetz:

[PCs] → [Forward Proxy (Squid)] → [Firewall] → [Internet]
                |
          URL-Filter:
          - Social Media → blockiert
          - Streaming → blockiert
          - Malware-Sites → blockiert
          
          Caching:
          - Windows Updates → einmal laden, lokal verteilen
          - Haeufig besuchte Sites → schneller Zugriff
          
          Logging:
          - Wer hat wann welche Seite aufgerufen?
```

#### Reverse Proxy – Typische Konfiguration

```
Internet → [Reverse Proxy (nginx)] → [Webserver 1: Shop]
                    |               → [Webserver 2: Blog]
                    |               → [Webserver 3: API]
                    
Funktionen:
- SSL-Terminierung: HTTPS-Entschluesselung am Proxy, intern HTTP
- Load Balancing: Anfragen auf mehrere Server verteilen
- Caching: Statische Inhalte (Bilder, CSS) zwischenspeichern
- WAF: Schutz vor SQL Injection, XSS, CSRF
- URL-basiertes Routing: /shop → Server 1, /blog → Server 2
```

#### Proxy-Vergleich

| Kriterium | Forward Proxy | Reverse Proxy | Transparenter Proxy |
|-----------|--------------|---------------|---------------------|
| Wer nutzt ihn? | Interne Clients | Externe Clients | Interne Clients |
| Wofuer? | Internetzugang kontrollieren | Server schuetzen | Wie Forward, ohne Konfiguration |
| Client-Konfiguration | Ja (Browser/System) | Nein | Nein |
| Beispiel-Software | Squid, McAfee Web Gateway | nginx, HAProxy, Traefik | Squid (transparent mode) |
| Typischer Port | 3128, 8080 | 80, 443 | 80, 443 |

---

### Zusammenspiel: DHCP + DNS in der Praxis

```
1. PC wird eingeschaltet
2. PC hat keine IP → DHCP Discover (Broadcast)
3. DHCP-Server antwortet mit:
   - IP: 192.168.1.50
   - Maske: 255.255.255.0
   - Gateway: 192.168.1.1
   - DNS-Server: 192.168.1.1

4. PC oeffnet Browser → www.firma.de
5. PC fragt DNS-Server 192.168.1.1: "Was ist die IP von www.firma.de?"
6. DNS-Server antwortet: "93.184.216.34"
7. PC baut HTTP-Verbindung zu 93.184.216.34 auf (evtl. ueber Proxy)

→ DHCP liefert dem PC die Adresse des DNS-Servers
→ DNS loest den Domainnamen in eine IP-Adresse auf
→ Proxy kann als Vermittler dazwischengeschaltet sein
```

---

### Typische Pruefungsaspekte

- DORA-Prozess vollstaendig beschreiben (alle vier Schritte)
- DNS-Hierarchie erklaeren (Root → TLD → SLD → Hostname)
- DNS-Record-Typen kennen und zuordnen (A, AAAA, MX, CNAME, NS, PTR)
- Unterschied Forward Proxy vs. Reverse Proxy
- DHCP-Relay erklaeren (warum wird es benoetigt?)
- DNS-Aufloesung rekursiv vs. iterativ
- Fehlerszenario: Was pruefen, wenn ein Client keine IP erhaelt?

### Haeufige Fehler

- DHCP und DNS verwechseln: DHCP = IP-Vergabe, DNS = Namensaufloesung
- DORA-Reihenfolge falsch: Es ist immer Discover → Offer → Request → Acknowledge
- Vergessen, dass DHCP ueber Broadcast funktioniert und daher DHCP-Relay benoetigt wird, wenn der Server in einem anderen Subnetz steht
- Forward Proxy und Reverse Proxy verwechseln: Forward = fuer Clients, Reverse = fuer Server
- DNS als "eine einzige Datenbank" beschreiben – es ist ein verteiltes, hierarchisches System
- MX-Record mit A-Record verwechseln: MX zeigt auf den Mailserver, A loest den Namen in eine IP auf

---

## Uebungen

**Aufgabe 1:** Beschreibe den DORA-Prozess in vier Schritten. Was passiert, wenn kein DHCP-Server erreichbar ist?

**Aufgabe 2:** Ein DHCP-Server vergibt Adressen im Bereich 192.168.1.100 – 192.168.1.200. Ein Drucker soll immer die IP 192.168.1.10 erhalten. Wie wird das konfiguriert?

**Aufgabe 3:** Im Netzwerk gibt es zwei Subnetze (192.168.1.0/24 und 192.168.2.0/24), aber nur einen DHCP-Server in Subnetz 1. Wie erhalten die Clients in Subnetz 2 ihre IP-Adressen?

**Aufgabe 4:** Erklaere die DNS-Hierarchie anhand der Domain "shop.firma.de". Welche DNS-Server werden bei der Aufloesung nacheinander gefragt?

**Aufgabe 5:** Ordne die folgenden DNS-Record-Typen ihrer Funktion zu: A, AAAA, MX, CNAME, NS, PTR.
a) Hostname → IPv4-Adresse
b) Alias fuer einen anderen Hostnamen
c) Zustaendiger Mailserver
d) Hostname → IPv6-Adresse
e) IP-Adresse → Hostname
f) Zustaendiger Nameserver

**Aufgabe 6:** Was ist der Unterschied zwischen einer rekursiven und einer iterativen DNS-Anfrage?

**Aufgabe 7:** Erklaere den Unterschied zwischen Forward Proxy und Reverse Proxy. Nenne jeweils zwei typische Funktionen.

**Aufgabe 8:** Ein Mitarbeiter meldet: "Ich kann keine Webseiten oeffnen, aber ich kann IP-Adressen anpingen." Was ist die wahrscheinliche Ursache?

**Aufgabe 9:** Warum wird in Unternehmen oft ein eigener DNS-Server betrieben statt nur den DNS des Providers zu nutzen?

**Aufgabe 10:** Ein Unternehmen moechte den Internetzugang der Mitarbeiter kontrollieren (bestimmte Seiten blockieren, Nutzung protokollieren) und gleichzeitig Bandbreite sparen. Welche Loesung empfiehlst du?

---
---

# Loesungen

## Aufgabe 1
1. **Discover:** Client sendet einen Broadcast ins Netzwerk, um einen DHCP-Server zu finden (Client hat noch keine IP, sendet von 0.0.0.0 an 255.255.255.255).
2. **Offer:** Der DHCP-Server antwortet mit einem Angebot: IP-Adresse, Subnetzmaske, Gateway, DNS-Server und Lease-Dauer.
3. **Request:** Der Client nimmt das Angebot an und sendet einen Broadcast (Request), um den Server zu informieren.
4. **Acknowledge:** Der Server bestaetigt die Zuweisung. Der Client uebernimmt die Konfiguration.

Wenn kein DHCP-Server erreichbar ist, erhaelt der Client eine APIPA-Adresse (169.254.x.x /16). Damit kann er nur mit anderen APIPA-Geraeten im selben Subnetz kommunizieren, hat aber keinen Internetzugang und kein funktionierendes Routing.

## Aufgabe 2
Ueber eine DHCP-Reservierung (auch statisches DHCP genannt). Die MAC-Adresse des Druckers wird im DHCP-Server hinterlegt und fest der IP 192.168.1.10 zugeordnet. Immer wenn der Drucker eine IP anfragt, erhaelt er 192.168.1.10. Die IP liegt bewusst ausserhalb des dynamischen Pools (100–200), um Konflikte zu vermeiden.

## Aufgabe 3
Ueber einen DHCP-Relay-Agent (IP-Helper) auf dem Router zwischen den Subnetzen. Der Router in Subnetz 2 nimmt den DHCP-Broadcast des Clients entgegen und leitet ihn als Unicast an den DHCP-Server in Subnetz 1 weiter. Der Server antwortet dem Router, der die Antwort an den Client in Subnetz 2 zurueckgibt. Auf dem DHCP-Server muss ein separater Scope fuer 192.168.2.0/24 angelegt sein.

## Aufgabe 4
Domain: shop.firma.de
DNS-Hierarchie (von oben nach unten):
1. **Root-Server (.)** – Kennt die Nameserver fuer alle TLDs
2. **TLD-Server (.de)** – Kennt die Nameserver fuer alle .de-Domains
3. **Autoritativer Server (firma.de)** – Kennt alle Records fuer firma.de, inklusive shop.firma.de

Aufloesung: Client → lokaler DNS → Root ("frag .de") → .de-NS ("frag ns.firma.de") → ns.firma.de ("shop.firma.de = 10.0.1.50")

## Aufgabe 5
a) A – Hostname → IPv4-Adresse
b) CNAME – Alias fuer einen anderen Hostnamen
c) MX – Zustaendiger Mailserver
d) AAAA – Hostname → IPv6-Adresse
e) PTR – IP-Adresse → Hostname (Reverse Lookup)
f) NS – Zustaendiger Nameserver

## Aufgabe 6
- **Rekursive Anfrage:** Der Client erwartet eine vollstaendige Antwort. Der gefragte DNS-Server muss die Aufloesung komplett durchfuehren und das Ergebnis zurueckliefern. Typisch: Client → lokaler DNS-Server.
- **Iterative Anfrage:** Der gefragte DNS-Server liefert die beste bekannte Antwort oder verweist auf den naechsten zustaendigen Server. Der anfragende Server muss selbst weiter fragen. Typisch: Lokaler DNS-Server fragt Root → TLD → autoritativen Server.

## Aufgabe 7
- **Forward Proxy:** Steht zwischen internen Clients und dem Internet. Funktionen: (1) URL-Filterung (Zugriff auf bestimmte Seiten blockieren), (2) Caching (haeufig abgerufene Inhalte zwischenspeichern).
- **Reverse Proxy:** Steht zwischen dem Internet und den eigenen Servern. Funktionen: (1) Load Balancing (Anfragen auf mehrere Server verteilen), (2) SSL-Terminierung (HTTPS am Proxy entschluesseln, intern HTTP weiterleiten).

## Aufgabe 8
Wahrscheinliche Ursache: DNS-Problem. Der Client hat eine funktionierende IP-Konfiguration (daher kann er IP-Adressen anpingen), aber die Namensaufloesung funktioniert nicht (daher keine Webseiten). Moegliche Ursachen: DNS-Server nicht erreichbar, DNS-Server falsch konfiguriert, DNS-Server ausgefallen. Pruefung: `nslookup www.google.de` → schlaegt fehl. Loesung: DNS-Konfiguration pruefen (ipconfig /all), alternativen DNS testen (z.B. 8.8.8.8).

## Aufgabe 9
Gruende fuer einen eigenen DNS-Server:
1. **Interne Namensaufloesung:** Interne Hostnamen (z.B. fileserver.firma.local) koennen nur von einem internen DNS aufgeloest werden.
2. **Active Directory:** Windows-Domaenen benoetigen DNS zwingend fuer die Diensterkennung (SRV-Records).
3. **Schnellere Aufloesung:** Lokaler Cache beschleunigt wiederholte Anfragen.
4. **Kontrolle:** Eigene DNS-Eintraege verwalten, Split DNS fuer interne/externe Aufloesung.

## Aufgabe 10
Forward Proxy (z.B. Squid) mit URL-Filter und Caching-Funktion. Der Proxy blockiert unerwuenschte Websites (Social Media, Streaming, Malware), protokolliert die Nutzung und cached haeufig abgerufene Inhalte (z.B. Windows Updates), sodass sie nur einmal aus dem Internet geladen werden muessen. Zusaetzlich kann der Proxy als transparenter Proxy konfiguriert werden, damit keine Client-Konfiguration noetig ist.
