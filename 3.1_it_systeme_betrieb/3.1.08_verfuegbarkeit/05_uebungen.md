# Uebungen: 3.1.08 – Anforderungen an die Verfuegbarkeit von Anwendungsdiensten

## Verfuegbarkeitsberechnung

**Aufgabe 1:** Ein Server hat eine zugesicherte Verfuegbarkeit von 99,9 % pro Jahr. Berechne die maximal zulaessige Ausfallzeit in Stunden pro Jahr.

**Aufgabe 2:** Eine Webanwendung besteht aus folgenden seriell geschalteten Komponenten:
- Firewall: 99,99 %
- Webserver: 99,9 %
- Applikationsserver: 99,9 %
- Datenbankserver: 99,5 %

Berechne die Gesamtverfuegbarkeit und die maximale Ausfallzeit pro Jahr.

**Aufgabe 3:** Der Datenbankserver aus Aufgabe 2 wird durch einen Cluster aus zwei identischen Servern (je 99,5 %) ersetzt. Berechne die neue Verfuegbarkeit des Datenbank-Clusters und die neue Gesamtverfuegbarkeit.

---

## Diensttypen und Anforderungen

**Aufgabe 4:** Ordne die folgenden Anforderungen dem passenden Diensttyp zu (Datenbank, Echtzeitkommunikation, Groupware, Mailserver, Webserver):
- a) Latenz unter 150 ms, QoS erforderlich
- b) MX-Records muessen redundant konfiguriert sein
- c) Content Delivery Network zur Lastverteilung
- d) ACID-Transaktionen muessen gewaehrleistet sein
- e) CalDAV und ActiveSync fuer mobile Zugriffe

**Aufgabe 5:** Ein Unternehmen plant die Einfuehrung eines VoIP-Systems fuer 100 Mitarbeiter. Nenne drei Voraussetzungen, die das Netzwerk erfuellen muss, damit die Sprachqualitaet gewaehrleistet ist.

**Aufgabe 6:** Erklaere den Unterschied zwischen einem Backup-MX-Server und einem Mailserver-Cluster. Wann wird welche Loesung eingesetzt?

---

## Load Balancing und Clustering

**Aufgabe 7:** Erklaere den Unterschied zwischen Aktiv-Passiv- und Aktiv-Aktiv-Clustering. Nenne fuer jedes Verfahren ein Einsatzbeispiel.

**Aufgabe 8:** Ein Online-Shop hat drei Webserver hinter einem Load Balancer. Waehrend einer Marketingaktion verdoppelt sich die Last. Welches Load-Balancing-Verfahren ist hier sinnvoll und warum?

**Aufgabe 9:** Erklaere, warum ein Load Balancer selbst ein Single Point of Failure sein kann. Welche Massnahme loest dieses Problem?

---

## SLA und Praxis

**Aufgabe 10:** Ein Cloud-Anbieter garantiert eine Verfuegbarkeit von 99,95 % pro Monat. Berechne die maximal zulaessige Ausfallzeit in Minuten pro Monat (30 Tage).

**Aufgabe 11:** Nenne fuenf typische Bestandteile eines SLA.

**Aufgabe 12:** Ein Unternehmen stellt fest, dass sein Webshop im letzten Monat insgesamt 90 Minuten nicht erreichbar war. Der Monat hatte 30 Tage. Berechne die tatsaechliche Verfuegbarkeit. Wurde das SLA von 99,9 % eingehalten?

---
---

# Loesungen

## Aufgabe 1
```
Max. Ausfallzeit = 8.760 h * (1 - 0,999) = 8.760 * 0,001 = 8,76 Stunden/Jahr
```

## Aufgabe 2
```
V = 0,9999 * 0,999 * 0,999 * 0,995
V = 0,9999 * 0,999 * 0,999 * 0,995
V = 0,9929 = 99,29 %
Max. Ausfallzeit = 8.760 * (1 - 0,9929) = 8.760 * 0,0071 = 62,2 Stunden/Jahr
```

## Aufgabe 3
```
V_DB_Cluster = 1 - (1 - 0,995)^2 = 1 - (0,005)^2 = 1 - 0,000025 = 0,999975 = 99,9975 %
V_gesamt = 0,9999 * 0,999 * 0,999 * 0,999975
V_gesamt = 0,9979 = 99,79 %
Max. Ausfallzeit = 8.760 * 0,0021 = 18,4 Stunden/Jahr
```
→ Durch den DB-Cluster sank die Ausfallzeit von 62,2 auf 18,4 Stunden/Jahr.

## Aufgabe 4
- a) **Echtzeitkommunikation** (VoIP-Anforderungen)
- b) **Mailserver** (MX-Records sind DNS-Eintraege fuer E-Mail-Routing)
- c) **Webserver** (CDN dient der Auslieferung von Webinhalten)
- d) **Datenbank** (ACID = Transaktionssicherheit)
- e) **Groupware** (Kalender- und Kontaktsynchronisation)

## Aufgabe 5
1. **QoS konfiguriert:** Sprachpakete muessen priorisiert werden (DSCP EF = Expedited Forwarding)
2. **Ausreichende Bandbreite:** Pro Gespraech ca. 100 kbit/s (je nach Codec), fuer 100 Nutzer muss genuegend Bandbreite reserviert sein
3. **Geringe Latenz und Jitter:** Netzwerk muss Latenz < 150 ms und Jitter < 30 ms gewaehrleisten (PoE-faehige Switches, keine ueberlasteten Links)

## Aufgabe 6
- **Backup-MX:** Ein zweiter Mailserver, der E-Mails annimmt, wenn der primaere Server nicht erreichbar ist. Die E-Mails werden zwischengespeichert und spaeter an den primaeren Server weitergeleitet. Einfache Redundanz, keine sofortige Zustellung an Nutzer.
- **Mailserver-Cluster:** Mehrere Server arbeiten als ein System. E-Mails sind sofort auf allen Knoten verfuegbar. Beispiel: Exchange DAG. Aufwendiger, aber hoehere Verfuegbarkeit.
- **Einsatz:** Backup-MX fuer kleine Umgebungen mit tolerierbarer Verzoegerung. Cluster fuer Unternehmen mit hohen Verfuegbarkeitsanforderungen.

## Aufgabe 7
- **Aktiv-Passiv:** Ein Server arbeitet, der zweite wartet im Standby. Bei Ausfall uebernimmt der passive Server. Beispiel: Datenbank-Failover-Cluster (SQL Server Always On mit sekundaerem Replikat).
- **Aktiv-Aktiv:** Beide Server arbeiten gleichzeitig und teilen sich die Last. Bei Ausfall eines Servers uebernimmt der andere die gesamte Last. Beispiel: Zwei Webserver hinter einem Load Balancer.

## Aufgabe 8
**Least Connections** ist sinnvoll, da bei erhoehter Last die Anfragen an den Server mit den wenigsten aktiven Verbindungen geleitet werden. So wird verhindert, dass ein bereits stark belasteter Server weitere Anfragen erhaelt. Alternativ: Weighted Round Robin, falls die Server unterschiedliche Leistung haben.

## Aufgabe 9
Ein einzelner Load Balancer ist ein Single Point of Failure – faellt er aus, ist keiner der Backend-Server erreichbar. Loesung: **Redundanter Load Balancer** im Aktiv-Passiv- oder Aktiv-Aktiv-Modus mit einer virtuellen IP-Adresse (VIP), z.B. ueber VRRP (Virtual Router Redundancy Protocol) oder keepalived.

## Aufgabe 10
```
Max. Ausfallzeit = 30 * 24 * 60 * (1 - 0,9995)
                 = 43.200 min * 0,0005
                 = 21,6 Minuten/Monat
```

## Aufgabe 11
1. Verfuegbarkeit (z.B. 99,9 %)
2. Reaktionszeit (z.B. 30 Minuten)
3. Wiederherstellungszeit (z.B. 4 Stunden)
4. Wartungsfenster (z.B. Sonntag 02:00–06:00 Uhr)
5. Poenale/Vertragsstrafen bei Nichteinhaltung

## Aufgabe 12
```
Gesamtzeit = 30 * 24 * 60 = 43.200 Minuten
Ausfallzeit = 90 Minuten
Verfuegbarkeit = (43.200 - 90) / 43.200 * 100 = 43.110 / 43.200 * 100 = 99,79 %
```
Das SLA von 99,9 % wurde **nicht eingehalten** (erlaubt waeren max. 43,2 Minuten Ausfall).
