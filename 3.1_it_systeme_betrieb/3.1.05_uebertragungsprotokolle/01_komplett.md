# Komplett: 3.1.05 – Uebertragungsprotokolle

## Einordnung

- **Pruefungsteil:** 3.1 – Betreiben von IT-Systemen (Netzwerktechnik)
- **Thema-ID:** 3.1.05
- **Thema:** Uebertragungsprotokolle erlaeutern und unterscheiden koennen

## Themenkreise

### 1. HTTP / HTTPS

**Definition:** HTTP (Hypertext Transfer Protocol) ist ein zustandsloses Anwendungsprotokoll fuer die Uebertragung von Webinhalten. HTTPS ist die verschluesselte Variante ueber TLS.

**Kernaussagen HTTP:**
- Arbeitet auf OSI-Schicht 7 (Application Layer), Port 80
- Request-Response-Modell: Client sendet Anfrage, Server antwortet
- Zustandslos: Jede Anfrage ist unabhaengig (Cookies/Sessions fuer Zustand)
- Textbasiertes Protokoll (Header im Klartext)
- Version HTTP/1.1, HTTP/2, HTTP/3 (ueber QUIC/UDP)

**HTTP-Methoden:**

| Methode | Beschreibung | Beispiel |
|---------|-------------|---------|
| GET | Daten vom Server abrufen | Webseite laden |
| POST | Daten an Server senden | Formular absenden |
| PUT | Ressource erstellen/ersetzen | Datei hochladen |
| DELETE | Ressource loeschen | Eintrag entfernen |
| PATCH | Ressource teilweise aendern | Einzelnes Feld aktualisieren |
| HEAD | Wie GET, aber nur Header | Verfuegbarkeit pruefen |

**HTTP-Statuscodes:**

| Code-Bereich | Bedeutung | Beispiele |
|-------------|-----------|-----------|
| 1xx | Informational | 100 Continue |
| 2xx | Erfolg | 200 OK, 201 Created |
| 3xx | Umleitung | 301 Moved Permanently, 302 Found |
| 4xx | Client-Fehler | 400 Bad Request, 403 Forbidden, 404 Not Found |
| 5xx | Server-Fehler | 500 Internal Server Error, 503 Service Unavailable |

**HTTPS (HTTP Secure):**
- Verschluesselte Variante von HTTP ueber TLS (Transport Layer Security)
- Port 443
- TLS-Handshake vor der HTTP-Kommunikation
- Zertifikatsbasierte Authentifizierung des Servers
- Schuetzt Vertraulichkeit (Verschluesselung), Integritaet (Pruefung) und Authentizitaet (Zertifikat)

**TLS-Handshake (vereinfacht):**

```
Client                           Server
  |                                |
  |-- ClientHello (unterstuetzte ->|   1. Client nennt TLS-Version, Cipher Suites
  |   Cipher Suites)               |
  |                                |
  |<- ServerHello, Zertifikat -----|   2. Server waehlt Cipher Suite, sendet Zertifikat
  |                                |
  |-- Zertifikat pruefen,       -->|   3. Client prueft Zertifikat, sendet Pre-Master-Secret
  |   Pre-Master-Secret            |      (verschluesselt mit Public Key des Servers)
  |                                |
  |<= Verschluesselter Kanal ====>|   4. Beide berechnen Session Key → Kommunikation verschluesselt
```

**Wichtige Begriffe:**
- **TLS** – Transport Layer Security, Nachfolger von SSL
- **Zertifikat** – Digitales Dokument zur Identitaetspruefung (X.509)
- **CA (Certificate Authority)** – Vertrauenswuerdige Stelle, die Zertifikate ausstellt
- **Cipher Suite** – Kombination aus Verschluesselungs-, Hash- und Schluesselaustausch-Algorithmen

---

### 2. TCP / UDP

**Definition:** TCP (Transmission Control Protocol) und UDP (User Datagram Protocol) sind die beiden zentralen Transportprotokolle auf OSI-Schicht 4.

**TCP – Detaillierte Merkmale:**
- Verbindungsorientiert: 3-Way-Handshake vor Datenueberragung
- Zuverlaessig: Sequenznummern, Acknowledgements, Retransmission
- Flusskontrolle: Sliding Window reguliert die Datenrate
- Staukontrolle: Slow Start, Congestion Avoidance
- Segmentierung: Grosse Datenmengen werden in Segmente zerlegt
- Vollduplex: Bidirektionale Kommunikation gleichzeitig

**TCP 3-Way-Handshake:**

```
Client                    Server
  |                         |
  |--- SYN (seq=x) ------->|   1. Verbindungsanfrage
  |                         |
  |<-- SYN-ACK ------------|   2. Bestaetigung + Gegenanfrage
  |    (seq=y, ack=x+1)    |
  |                         |
  |--- ACK (ack=y+1) ----->|   3. Bestaetigung → Verbindung steht
  |                         |
```

**TCP 4-Way-Teardown:**

```
Client                    Server
  |--- FIN --------------->|   1. Client moechte beenden
  |<-- ACK ----------------|   2. Server bestaetigt
  |<-- FIN ----------------|   3. Server moechte auch beenden
  |--- ACK --------------->|   4. Client bestaetigt → Verbindung beendet
```

**UDP – Detaillierte Merkmale:**
- Verbindungslos: Kein Handshake, Daten werden sofort gesendet
- Unzuverlaessig: Kein ACK, keine Neuuebertragung
- Keine Reihenfolge: Pakete koennen in beliebiger Reihenfolge ankommen
- Minimaler Header: 8 Bytes (TCP: 20+ Bytes)
- Schneller: Kein Overhead durch Verbindungsmanagement
- Broadcast/Multicast moeglich (TCP nicht)

### Vergleich TCP vs. UDP

| Kriterium | TCP | UDP |
|-----------|-----|-----|
| Verbindungsaufbau | Ja (3-Way-Handshake) | Nein |
| Zuverlaessigkeit | Ja (ACK, Retransmission) | Nein |
| Reihenfolge | Garantiert (Sequenznummern) | Nicht garantiert |
| Flusskontrolle | Ja (Sliding Window) | Nein |
| Header-Groesse | 20+ Bytes | 8 Bytes |
| Geschwindigkeit | Langsamer | Schneller |
| Broadcast/Multicast | Nein | Ja |
| Duplex | Vollduplex | Simplex/Duplex |

### Wichtige Portnummern

| Port | Protokoll | Transport | Beschreibung |
|------|-----------|-----------|-------------|
| 20/21 | FTP | TCP | Dateiuebertragung (Daten/Steuerung) |
| 22 | SSH/SCP/SFTP | TCP | Sichere Shell / Dateiuebertragung |
| 23 | Telnet | TCP | Unsichere Fernsteuerung |
| 25 | SMTP | TCP | E-Mail-Versand |
| 53 | DNS | TCP/UDP | Namensaufloesung |
| 67/68 | DHCP | UDP | IP-Adressvergabe |
| 80 | HTTP | TCP | Webseiten (unverschluesselt) |
| 110 | POP3 | TCP | E-Mail-Abruf |
| 143 | IMAP | TCP | E-Mail-Abruf |
| 443 | HTTPS | TCP | Webseiten (verschluesselt) |
| 3389 | RDP | TCP | Remote Desktop |

---

## Typische Pruefungsaspekte

- HTTP-Methoden kennen und Szenarien zuordnen koennen
- Unterschied HTTP vs. HTTPS erklaeren (TLS, Zertifikate)
- TCP-Handshake beschreiben koennen
- TCP vs. UDP: Wann welches Protokoll?
- Portnummern gaengiger Dienste kennen
- HTTP-Statuscodes interpretieren koennen

## Haeufige Fehler

- HTTPS wird als "eigenes Protokoll" beschrieben – es ist HTTP ueber TLS
- SSL und TLS werden verwechselt: SSL ist veraltet, TLS ist der aktuelle Standard
- TCP wird als "besser" als UDP bewertet – beide haben ihre Berechtigung
- HTTP/2 und HTTP/3 werden ignoriert: HTTP/3 nutzt QUIC (basiert auf UDP, nicht TCP!)
- Portnummer 443 wird HTTP statt HTTPS zugeordnet

---

## Uebungen

**Aufgabe 1:** Erklaere den Unterschied zwischen HTTP und HTTPS. Welche Schutzziele werden durch HTTPS erreicht?

**Aufgabe 2:** Ordne die folgenden Szenarien der passenden HTTP-Methode zu:
a) Nutzer ruft eine Produktseite auf
b) Nutzer sendet ein Kontaktformular ab
c) Admin loescht einen Benutzereintrag ueber eine REST-API
d) System prueft, ob eine Ressource existiert (ohne Inhalt abzurufen)

**Aufgabe 3:** Beschreibe den TCP-3-Way-Handshake mit den drei Schritten und den verwendeten Flags.

**Aufgabe 4:** Nenne jeweils drei Anwendungen, die TCP bzw. UDP verwenden, und begruende die Wahl.

**Aufgabe 5:** Ein HTTP-Server antwortet mit Statuscode 403. Was bedeutet das? Nenne zwei moegliche Ursachen.

**Aufgabe 6:** Erklaere, warum HTTP/3 auf UDP statt TCP basiert. Welches Protokoll liegt zwischen HTTP/3 und UDP?

---
---

# Loesungen

## Aufgabe 1
HTTP uebertraegt Daten im Klartext (Port 80). HTTPS verschluesselt die Kommunikation mit TLS (Port 443). Schutzziele:
- **Vertraulichkeit:** Daten sind verschluesselt und koennen nicht mitgelesen werden
- **Integritaet:** Daten koennen nicht unbemerkt veraendert werden
- **Authentizitaet:** Das Server-Zertifikat bestaetigt die Identitaet des Servers

## Aufgabe 2
a) GET – Ressource abrufen
b) POST – Daten an Server senden
c) DELETE – Ressource loeschen
d) HEAD – Nur Header abrufen (wie GET ohne Body)

## Aufgabe 3
1. **SYN:** Client sendet ein SYN-Paket mit initialer Sequenznummer an den Server (Verbindungsanfrage)
2. **SYN-ACK:** Server antwortet mit SYN-ACK: bestaetigt die Anfrage (ACK) und sendet eigene Sequenznummer (SYN)
3. **ACK:** Client bestaetigt mit ACK. Die Verbindung ist aufgebaut und Daten koennen uebertragen werden.

## Aufgabe 4
TCP-Anwendungen (benoetigen Zuverlaessigkeit):
1. HTTP/HTTPS (Webseiten muessen vollstaendig laden)
2. FTP (Dateien muessen komplett und korrekt uebertragen werden)
3. SMTP (E-Mails duerfen nicht verloren gehen)

UDP-Anwendungen (benoetigen Geschwindigkeit):
1. VoIP (Echtzeitkommunikation, Verzoegerung schlimmer als Paketverlust)
2. DNS (Kleine Anfragen, schnelle Antwort gewuenscht)
3. DHCP (Broadcast-basiert, Client hat noch keine IP, keine TCP-Verbindung moeglich)

## Aufgabe 5
Statuscode 403 = Forbidden. Der Server hat die Anfrage verstanden, verweigert aber den Zugriff. Moegliche Ursachen:
1. Der Benutzer hat keine Berechtigung fuer die angeforderte Ressource (fehlende Rechte)
2. Der Zugriff ist durch eine IP-basierte Einschraenkung blockiert (z.B. Geoblocking, Firewall-Regel)

## Aufgabe 6
HTTP/3 basiert auf QUIC (Quick UDP Internet Connections), das ueber UDP laeuft. Grund: TCP hat das "Head-of-Line-Blocking"-Problem – wenn ein Paket verloren geht, muessen alle nachfolgenden Pakete warten. QUIC loest dieses Problem, indem Streams unabhaengig voneinander uebertragen werden. Verbindungsaufbau und TLS-Handshake geschehen in einem Schritt (0-RTT moeglich), was die Latenz reduziert.
