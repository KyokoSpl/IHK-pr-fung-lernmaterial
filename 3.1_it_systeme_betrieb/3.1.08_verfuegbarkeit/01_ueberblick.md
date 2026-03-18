# Ueberblick: 3.1.08 – Anforderungen an die Verfuegbarkeit von Anwendungsdiensten

## Einordnung

- **Pruefungsteil:** 3.1 – Betreiben von IT-Systemen
- **Thema-ID:** 3.1.08
- **Thema:** Anforderungen an die Verfuegbarkeit verschiedener Anwendungsdienste kennen und bewerten koennen

## Ziel

Du musst wissen, welche Verfuegbarkeitsanforderungen verschiedene Anwendungsdienste (Datenbanken, Mailserver, Webserver etc.) haben. Dazu gehoeren SLA-Definitionen, Verfuegbarkeitsberechnung, Lastverteilung und Clustering-Konzepte.

## Themenkreise im Ueberblick

### 1. Datenbanken
Datenbanksysteme (z.B. MySQL, PostgreSQL, MS SQL Server, Oracle) stellen zentrale Dienste fuer Anwendungen bereit. Ihre Verfuegbarkeit ist geschaeftskritisch, da Ausfaelle direkt den Betrieb betreffen. Konzepte wie Replikation, Clustering und Failover sichern die Hochverfuegbarkeit.

### 2. Echtzeitkommunikation
Dienste wie VoIP (z.B. SIP, Teams), Videokonferenzen und Instant Messaging erfordern geringe Latenz und hohe Verfuegbarkeit. Ausfaelle beeintraechtigen die Zusammenarbeit unmittelbar. QoS-Massnahmen und redundante Infrastruktur sind essenziell.

### 3. Groupware
Groupware-Systeme (z.B. Microsoft Exchange/Outlook, Nextcloud, Lotus Notes) buendeln E-Mail, Kalender, Kontakte und Aufgaben. Sie sind zentrale Werkzeuge der Buero-Kommunikation und muessen hohe Verfuegbarkeit bieten.

### 4. Mailserver
Mailserver (z.B. Postfix, Exchange, Dovecot) verarbeiten den E-Mail-Verkehr. Ausfaelle fuehren zu Kommunikationsstoerungen. Redundante MX-Records, Spamfilter-Integration und Backup-MX-Server sind pruefungsrelevant.

### 5. Webserver
Webserver (z.B. Apache, Nginx, IIS) stellen Webanwendungen und Webseiten bereit. Fuer oeffentlich erreichbare Dienste (E-Commerce, Kundenportale) gelten besonders hohe Verfuegbarkeitsanforderungen. Load Balancing und Content Delivery Networks (CDN) sind gaengige Massnahmen.

## Querverweise
- → 3.1.09 (Risiken identifizieren, MTBF/AFR)
- → 3.1.10 (Massnahmen zur Sicherstellung: RAID, USV, Backups)
- → 3.1.11 (Monitoring von Diensten und Systemen)
- → 3.1.12 (Incident Management, SLA, Eskalation)
- → 3.1.07 (Netzwerkrelevante Dienste: DNS, DHCP)
