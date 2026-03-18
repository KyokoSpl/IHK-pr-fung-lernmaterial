# Grundlagen: 3.1.08 – Anforderungen an die Verfuegbarkeit von Anwendungsdiensten

## Verfuegbarkeit – Allgemeine Grundlagen

**Definition:** Die Verfuegbarkeit eines IT-Dienstes gibt an, zu welchem Anteil der vereinbarten Betriebszeit der Dienst tatsaechlich nutzbar ist. Sie wird in Prozent angegeben und ist zentraler Bestandteil von Service Level Agreements (SLAs).

**Formel:**

```
Verfuegbarkeit (%) = (Gesamtzeit - Ausfallzeit) / Gesamtzeit * 100
```

**Verfuegbarkeitsklassen (Neuner-Regel):**

| Verfuegbarkeit | Max. Ausfallzeit/Jahr | Max. Ausfallzeit/Monat | Bezeichnung |
|---|---|---|---|
| 99,0 % | 3,65 Tage | 7,31 Stunden | Standard |
| 99,9 % | 8,76 Stunden | 43,8 Minuten | Erhoehte Verfuegbarkeit |
| 99,99 % | 52,6 Minuten | 4,38 Minuten | Hohe Verfuegbarkeit |
| 99,999 % | 5,26 Minuten | 26,3 Sekunden | Hoechste Verfuegbarkeit |

**Wichtige Begriffe:**
- **SLA (Service Level Agreement)** – vertragliche Vereinbarung ueber Qualitaet und Verfuegbarkeit eines Dienstes
- **Uptime** – Zeit, in der ein Dienst verfuegbar ist
- **Downtime** – Zeit, in der ein Dienst nicht verfuegbar ist
- **Planned Downtime** – geplante Wartungsfenster (zaehlt je nach SLA nicht als Ausfall)
- **Single Point of Failure (SPoF)** – eine einzelne Komponente, deren Ausfall den gesamten Dienst lahmlegt

---

## Datenbanken

**Definition:** Ein Datenbankmanagementsystem (DBMS) verwaltet strukturierte Daten und stellt sie Anwendungen ueber Abfragen (z.B. SQL) bereit.

**Kernaussagen:**
- Datenbanken sind oft die kritischste Komponente einer Anwendung
- Typische DBMS: MySQL/MariaDB, PostgreSQL, Microsoft SQL Server, Oracle
- Ausfaelle fuehren zu Datenverlust oder Anwendungsstillstand

**Verfuegbarkeitsmassnahmen:**

| Massnahme | Beschreibung |
|---|---|
| Replikation | Daten werden auf mehrere Server kopiert (Master-Slave, Master-Master) |
| Clustering | Mehrere Datenbankserver arbeiten als ein logisches System (z.B. Galera Cluster) |
| Failover | Automatischer Wechsel auf einen Standby-Server bei Ausfall |
| Connection Pooling | Verwaltung von Datenbankverbindungen zur Lastoptimierung |
| Regelnmaessige Backups | Sicherung der Daten fuer Wiederherstellung bei Datenverlust |

**Wichtige Begriffe:**
- **Replikation** – Synchrone oder asynchrone Kopie der Datenbank auf einen zweiten Server
- **Failover** – Automatisches Umschalten auf ein Ersatzsystem
- **Cluster** – Verbund mehrerer Server, die als ein System arbeiten
- **ACID** – Atomicity, Consistency, Isolation, Durability (Transaktionssicherheit)

---

## Echtzeitkommunikation

**Definition:** Echtzeitkommunikation umfasst Dienste, bei denen Daten sofort uebertragen und verarbeitet werden muessen (z.B. VoIP, Videokonferenzen, Chat).

**Kernaussagen:**
- Erfordert geringe Latenz (< 150 ms fuer VoIP) und minimalen Paketverlust (< 1 %)
- Protokolle: SIP, RTP, WebRTC, H.323
- Beispiele: Microsoft Teams, Zoom, Cisco Webex, Asterisk (PBX)

**Anforderungen:**

| Anforderung | Wert / Beschreibung |
|---|---|
| Latenz | < 150 ms (One-Way) |
| Jitter | < 30 ms |
| Paketverlust | < 1 % |
| Bandbreite | Abhaengig vom Codec (z.B. G.711 = 64 kbit/s pro Richtung) |
| QoS | Quality of Service muss im Netzwerk konfiguriert sein |

**Wichtige Begriffe:**
- **QoS (Quality of Service)** – Priorisierung von Netzwerkverkehr fuer zeitkritische Daten
- **SIP (Session Initiation Protocol)** – Signalisierungsprotokoll fuer VoIP
- **Jitter** – Schwankung der Paketlaufzeit
- **RTP (Real-Time Transport Protocol)** – Transportprotokoll fuer Audio/Video
- **PBX (Private Branch Exchange)** – Telefonanlage

---

## Groupware

**Definition:** Groupware-Systeme sind Software-Plattformen, die die Zusammenarbeit in Teams unterstuetzen. Sie integrieren E-Mail, Kalender, Kontakte, Aufgaben und oft auch Dokumentenmanagement.

**Kernaussagen:**
- Typische Systeme: Microsoft Exchange/Outlook, Nextcloud, Google Workspace
- Zugriff ueber verschiedene Clients: Desktop, Web, Mobile
- Protokolle: MAPI, EWS, CalDAV, CardDAV, ActiveSync

**Verfuegbarkeitsanforderungen:**

| Aspekt | Anforderung |
|---|---|
| Typische SLA | 99,9 % (bis 8,76 h Ausfall/Jahr) |
| Zugriffsarten | Desktop-Client, Webmail, Mobile (ActiveSync) |
| Datensicherheit | Verschluesselte Uebertragung (TLS), serverseitige Verschluesselung |
| Redundanz | Database Availability Group (DAG) bei Exchange |
| Backup | Regelmaessige Postfach-Sicherung |

**Wichtige Begriffe:**
- **DAG (Database Availability Group)** – Exchange-Cluster fuer Hochverfuegbarkeit
- **ActiveSync** – Protokoll zur Synchronisation von E-Mail, Kalender und Kontakten mit Mobilgeraeten
- **CalDAV/CardDAV** – Standards fuer Kalender- und Kontaktsynchronisation

---

## Mailserver

**Definition:** Ein Mailserver empfaengt, speichert und versendet E-Mails. Er besteht typischerweise aus einem MTA (Mail Transfer Agent) und einem MDA (Mail Delivery Agent).

**Kernaussagen:**
- Versand: SMTP (Port 25/587)
- Empfang: IMAP (Port 993) oder POP3 (Port 995) – jeweils verschluesselt
- MX-Records im DNS bestimmen, welcher Server fuer eine Domaene E-Mails empfaengt
- Backup-MX: Zweiter MX-Record mit niedrigerer Prioritaet als Fallback

**Serverkomponenten:**

| Komponente | Funktion | Beispiel |
|---|---|---|
| MTA (Mail Transfer Agent) | E-Mails senden und empfangen | Postfix, Sendmail, Exim |
| MDA (Mail Delivery Agent) | E-Mails in Postfaecher zustellen | Dovecot, Cyrus |
| MUA (Mail User Agent) | E-Mail-Client des Nutzers | Thunderbird, Outlook |
| Spamfilter | Unerwuenschte Mails filtern | SpamAssassin, rspamd |

**Verfuegbarkeitsmassnahmen:**
- Redundante MX-Records (Backup-MX-Server)
- Replikation der Mailbox-Datenbank
- TLS-Verschluesselung fuer sichere Uebertragung
- Greylisting und SPF/DKIM/DMARC gegen Spam und Spoofing

**Wichtige Begriffe:**
- **MX-Record** – DNS-Eintrag, der den zustaendigen Mailserver fuer eine Domaene angibt
- **Backup-MX** – Ersatz-Mailserver, der E-Mails annimmt, wenn der primaere Server ausfaellt
- **SPF/DKIM/DMARC** – Mechanismen zur Authentifizierung von E-Mails

---

## Webserver

**Definition:** Ein Webserver liefert Webseiten und Webanwendungen ueber HTTP/HTTPS an Clients (Browser) aus.

**Kernaussagen:**
- Typische Webserver: Apache HTTP Server, Nginx, Microsoft IIS
- HTTPS mit TLS-Zertifikaten fuer verschluesselte Verbindungen
- Bei oeffentlichen Diensten (E-Commerce, SaaS) besonders hohe Anforderungen

**Verfuegbarkeitsmassnahmen:**

| Massnahme | Beschreibung |
|---|---|
| Load Balancing | Verteilung der Anfragen auf mehrere Server (z.B. HAProxy, Nginx) |
| Clustering | Mehrere Webserver als Verbund |
| CDN (Content Delivery Network) | Statische Inhalte ueber verteilte Server weltweit ausliefern (z.B. Cloudflare) |
| Auto-Scaling | Automatisches Hinzufuegen von Servern bei Lastspitzen (Cloud) |
| Health Checks | Regelmaessige Pruefung, ob der Webserver antwortet |
| Reverse Proxy | Vorgeschalteter Proxy fuer Lastverteilung und Caching |

**Wichtige Begriffe:**
- **Load Balancer** – Verteilt eingehende Anfragen auf mehrere Backend-Server
- **CDN** – Netzwerk aus verteilten Servern zur schnellen Auslieferung von Inhalten
- **Reverse Proxy** – Proxy, der Anfragen entgegennimmt und an Backend-Server weiterleitet
- **Health Check** – Automatische Pruefung, ob ein Server ordnungsgemaess arbeitet
- **SSL/TLS-Zertifikat** – Digitales Zertifikat fuer verschluesselte HTTPS-Verbindungen
