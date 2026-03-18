# Beispiele: 3.1.08 – Anforderungen an die Verfuegbarkeit von Anwendungsdiensten

## Datenbanken

**Beispiel 1:** Ein Online-Shop nutzt eine MySQL-Datenbank als Backend. Der Shop generiert 500 Bestellungen pro Stunde. Bei einem Datenbankausfall koennen keine Bestellungen verarbeitet werden. → SLA von 99,99 % erforderlich, da jeder Ausfall direkt Umsatzverlust bedeutet. Massnahme: MySQL-Cluster mit Master-Master-Replikation und automatischem Failover.

**Beispiel 2:** Eine Firma betreibt eine interne Wissensdatenbank (Wiki) auf PostgreSQL. Die Nutzung findet nur waehrend der Buerozeiten statt (Mo–Fr, 8–18 Uhr). → SLA von 99,5 % reicht aus, da der Dienst nicht geschaeftskritisch ist und Wartung ausserhalb der Buerozeiten stattfinden kann.

---

## Echtzeitkommunikation

**Beispiel 1:** Ein Callcenter nutzt eine VoIP-Anlage (Asterisk) fuer den Kundenservice. 50 Agenten telefonieren gleichzeitig. Bei einem Ausfall erreichen Kunden niemanden. → SLA von 99,99 % noetig. Massnahmen: Redundante SIP-Trunks, QoS im Netzwerk (DSCP EF fuer Voice), zweiter Asterisk-Server im Failover.

**Beispiel 2:** Ein Unternehmen nutzt Microsoft Teams fuer interne Besprechungen. Die Kommunikation ist wichtig, aber Ausfaelle von wenigen Minuten sind tolerierbar. → SLA von 99,9 % (durch Microsoft im M365-Vertrag garantiert). Eigene Massnahme: Redundante Internetanbindung, damit der Cloud-Dienst erreichbar bleibt.

---

## Groupware

**Beispiel 1:** Eine Firma mit 200 Mitarbeitern nutzt Microsoft Exchange On-Premises. E-Mail und Kalender sind fuer den taeglichen Betrieb unverzichtbar. → SLA 99,9 %. Massnahme: Exchange DAG (Database Availability Group) mit zwei Servern an unterschiedlichen Standorten. Bei Ausfall von Server A uebernimmt Server B automatisch die Postfach-Datenbanken.

**Beispiel 2:** Ein kleines Buero mit 10 Mitarbeitern nutzt Nextcloud fuer Kalender und Dateien. → SLA 99 % ausreichend. Massnahme: Taegliches Backup der Nextcloud-Datenbank und der Dateien. Kein Cluster noetig, da Wiederherstellung innerhalb weniger Stunden akzeptabel ist.

---

## Mailserver

**Beispiel 1:** Ein Unternehmen betreibt einen eigenen Mailserver (Postfix + Dovecot). Die Domaene `firma.de` hat zwei MX-Records:

```
firma.de.   MX  10  mail1.firma.de.
firma.de.   MX  20  mail2.firma.de.
```

Bei Ausfall von `mail1` (Prioritaet 10) leiten sendende Server die E-Mails automatisch an `mail2` (Prioritaet 20) weiter. → Kein E-Mail-Verlust, nur verzoegerte Zustellung.

**Beispiel 2:** Eine Firma stellt fest, dass 30 % der eingehenden E-Mails als Spam klassifiziert werden. Massnahmen: SPF-Record im DNS setzen (`v=spf1 mx -all`), DKIM-Signatur aktivieren, DMARC-Policy definieren. Ergebnis: Reduzierte Spam-Quote und verbesserte Zustellbarkeit eigener E-Mails.

---

## Webserver

**Beispiel 1:** Ein E-Commerce-Unternehmen betreibt einen Webshop mit 10.000 Besuchern taeglich. Zur Weihnachtszeit verdreifacht sich der Traffic. Loesung:

```
Internet → Load Balancer (HAProxy)
              |
     +--------+--------+
     |        |        |
   Web-1   Web-2   Web-3
     |        |        |
     +--------+--------+
              |
         Datenbank-Cluster
```

Load-Balancing-Verfahren: Least Connections (da Anfragen unterschiedlich lange dauern). Bei Lastspitzen wird Web-4 automatisch hinzugeschaltet (Auto-Scaling).

**Beispiel 2:** Ein Nachrichtenportal nutzt ein CDN (Cloudflare), um statische Inhalte wie Bilder und CSS-Dateien ueber weltweit verteilte Server auszuliefern. Vorteil: Schnellere Ladezeiten, Entlastung des Origin-Servers, Schutz vor DDoS-Angriffen.

---

## Gesamtbeispiel: Verfuegbarkeitsberechnung

**Szenario:** Eine Webanwendung besteht aus drei Komponenten in Reihe:

| Komponente | Einzelverfuegbarkeit |
|---|---|
| Load Balancer | 99,99 % |
| Applikationsserver | 99,9 % |
| Datenbank | 99,9 % |

**Berechnung Gesamtverfuegbarkeit (seriell):**
```
V = 0,9999 * 0,999 * 0,999
V = 0,9979 = 99,79 %
Max. Ausfallzeit/Jahr = 8.760 h * (1 - 0,9979) = 18,4 Stunden
```

**Verbesserung durch Datenbank-Cluster (zwei DB-Server mit je 99,9 %):**
```
V_DB = 1 - (1 - 0,999)^2 = 1 - 0,000001 = 0,999999 = 99,9999 %
V_gesamt = 0,9999 * 0,999 * 0,999999 = 0,9989 = 99,89 %
Max. Ausfallzeit/Jahr = 8.760 * 0,0011 = 9,6 Stunden
```

→ Durch Redundanz bei der Datenbank wurde die Ausfallzeit nahezu halbiert.
