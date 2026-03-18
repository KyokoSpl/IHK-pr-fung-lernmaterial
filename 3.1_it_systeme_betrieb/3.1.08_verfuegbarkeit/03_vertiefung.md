# Vertiefung: 3.1.08 – Anforderungen an die Verfuegbarkeit von Anwendungsdiensten

## Verfuegbarkeitsberechnung – Vertiefung

### Berechnung der maximalen Ausfallzeit

```
Max. Ausfallzeit = Gesamtzeit * (1 - Verfuegbarkeit/100)
```

**Beispiel: 99,9 % Verfuegbarkeit pro Jahr**
```
Max. Ausfallzeit = 365 Tage * 24 h * (1 - 0,999)
                 = 8.760 h * 0,001
                 = 8,76 Stunden pro Jahr
```

**Beispiel: 99,9 % Verfuegbarkeit pro Monat (30 Tage)**
```
Max. Ausfallzeit = 30 * 24 h * 0,001
                 = 720 h * 0,001
                 = 0,72 h = 43,2 Minuten pro Monat
```

### Verfuegbarkeit bei Reihenschaltung (seriell)

Wenn mehrere Komponenten hintereinander geschaltet sind (jede muss funktionieren):

```
V_gesamt = V_1 * V_2 * ... * V_n
```

**Beispiel:** Webserver (99,9 %) → Applikationsserver (99,9 %) → Datenbank (99,9 %)
```
V_gesamt = 0,999 * 0,999 * 0,999 = 0,997 = 99,7 %
Max. Ausfallzeit/Jahr = 8.760 * 0,003 = 26,28 Stunden
```

### Verfuegbarkeit bei Parallelschaltung (redundant)

Wenn eine Komponente redundant vorhanden ist:

```
V_parallel = 1 - (1 - V_1) * (1 - V_2)
```

**Beispiel:** Zwei Webserver mit je 99,9 % im Cluster:
```
V_parallel = 1 - (1 - 0,999) * (1 - 0,999)
           = 1 - 0,001 * 0,001
           = 1 - 0,000001
           = 0,999999 = 99,9999 %
```

### Typische Pruefungsaspekte
- Verfuegbarkeit aus Ausfallzeiten berechnen
- Gesamtverfuegbarkeit bei seriell geschalteten Komponenten berechnen
- Auswirkung von Redundanz auf die Gesamtverfuegbarkeit erkennen

### Haeufige Fehler
- Verfuegbarkeiten addieren statt multiplizieren (bei serieller Schaltung)
- Geplante Wartung als Ausfall zaehlen, obwohl das SLA sie ausschliesst
- Verwechslung von Uptime und Verfuegbarkeit (Uptime = absolute Zeit, Verfuegbarkeit = Prozentwert)

---

## Diensttypen im Vergleich

| Kriterium | Datenbank | Echtzeitkomm. | Groupware | Mailserver | Webserver |
|---|---|---|---|---|---|
| Typische SLA | 99,99 % | 99,9 % | 99,9 % | 99,9 % | 99,9–99,99 % |
| Latenzempfindlich | Mittel | Sehr hoch | Gering | Gering | Mittel |
| Paketverlust kritisch | Ja | Sehr | Nein | Nein | Nein |
| Redundanz-Methode | Replikation, Cluster | Geo-Redundanz | DAG, Cluster | Backup-MX | Load Balancing |
| Protokolle | SQL (TCP) | SIP, RTP (UDP) | MAPI, CalDAV | SMTP, IMAP | HTTP/HTTPS |
| Typischer Port | 3306, 5432, 1433 | 5060 (SIP) | 443 | 25, 587, 993 | 80, 443 |

---

## Load Balancing – Vertiefung

### Verfahren im Vergleich

| Verfahren | Beschreibung | Einsatz |
|---|---|---|
| Round Robin | Anfragen abwechselnd an Server verteilen | Gleichmaessige Last, gleiche Server |
| Least Connections | Server mit wenigsten aktiven Verbindungen | Unterschiedliche Anfragedauer |
| IP Hash | Client-IP bestimmt den Zielserver | Session-Persistence noetig |
| Weighted Round Robin | Server mit Gewichtung (leistungsstaerker = mehr Last) | Heterogene Serverlandschaft |

### ASCII-Diagramm: Load Balancing

```
                         +------------------+
                         |   Load Balancer  |
                         | (z.B. HAProxy)   |
                         +--------+---------+
                                  |
                 +----------------+----------------+
                 |                |                |
           +-----+-----+  +-----+-----+  +------+----+
           | Webserver 1|  | Webserver 2|  | Webserver 3|
           |  (aktiv)   |  |  (aktiv)   |  |  (aktiv)   |
           +-----+------+  +-----+------+  +-----+-----+
                 |                |                |
                 +----------------+----------------+
                                  |
                         +--------+---------+
                         |    Datenbank     |
                         |   (Cluster)      |
                         +------------------+
```

---

## Clustering vs. Load Balancing

| Aspekt | Clustering | Load Balancing |
|---|---|---|
| Ziel | Hochverfuegbarkeit (Failover) | Lastverteilung |
| Funktionsweise | Server uebernimmt bei Ausfall | Anfragen werden verteilt |
| Typ | Aktiv-Passiv oder Aktiv-Aktiv | Immer Aktiv-Aktiv |
| Beispiel | Datenbank-Failover-Cluster | Webserver hinter HAProxy |
| Kombination | Oft mit Load Balancing kombiniert | Oft mit Clustering kombiniert |

### Aktiv-Passiv vs. Aktiv-Aktiv

```
Aktiv-Passiv:                    Aktiv-Aktiv:

  +--------+    +--------+        +--------+    +--------+
  | Server |    | Server |        | Server |    | Server |
  |   A    |    |   B    |        |   A    |    |   B    |
  | AKTIV  |    | STANDBY|        | AKTIV  |    | AKTIV  |
  +---+----+    +---+----+        +---+----+    +---+----+
      |              |                |              |
      +----- VIP ----+                +--- LB/VIP ---+
             |                               |
         Clients                         Clients
```

---

## SLA fuer verschiedene Diensttypen

### Typische SLA-Inhalte

| SLA-Bestandteil | Beschreibung |
|---|---|
| Verfuegbarkeit | z.B. 99,9 % pro Monat |
| Reaktionszeit | Maximale Zeit bis zur ersten Reaktion auf einen Vorfall |
| Wiederherstellungszeit | Maximale Zeit bis der Dienst wieder laeuft |
| Wartungsfenster | Geplante Zeiten fuer Updates (zaehlen oft nicht als Ausfall) |
| Eskalationsstufen | Wer wird wann informiert |
| Poenale/Gutschriften | Vertragsstrafen bei SLA-Verletzung |

### Typische Pruefungsaspekte
- SLA-Parameter einem Dienst zuordnen
- Begruenden, warum ein Dienst hohe/niedrige Verfuegbarkeit benoetigt
- Load-Balancing-Verfahren auswaehlen und begruenden
- Unterschied Clustering vs. Load Balancing erklaeren

### Haeufige Fehler
- Load Balancing und Clustering gleichsetzen – sie haben unterschiedliche Ziele
- SLA nur auf Verfuegbarkeit reduzieren – Reaktionszeit und Wiederherstellungszeit gehoeren dazu
- Vergessen, dass eine Kette nur so stark ist wie ihr schwaechstes Glied (serielle Verfuegbarkeit)
