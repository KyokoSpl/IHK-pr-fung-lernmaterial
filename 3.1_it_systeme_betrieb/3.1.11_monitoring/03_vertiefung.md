# Vertiefung: 3.1.11 – Monitoringsysteme anwenden und Ergebnisse interpretieren

## Monitoring-Architektur

### Aufbau eines typischen Monitoring-Systems

```
+---------------------------------------------------+
|                Monitoring-Server                   |
|  (z.B. Zabbix, Nagios, PRTG, Checkmk)            |
|                                                   |
|  +----------+  +-----------+  +----------------+  |
|  | Datenbank|  | Alerting  |  | Web-Dashboard  |  |
|  | (Metriken)|  |(Mail/SMS) |  | (Visualisierung)|  |
|  +----------+  +-----------+  +----------------+  |
+------------------------+-------------------------+
                         |
          +--------------+--------------+
          |              |              |
    +-----+----+  +------+-----+  +----+------+
    | Agent    |  | SNMP-Query |  | Agentless |
    | (Server) |  | (Switch)   |  | (WMI/SSH) |
    +----------+  +------------+  +-----------+
```

### Agentenbasiert vs. Agentless

| Aspekt | Agentenbasiert | Agentless |
|---|---|---|
| Installation | Agent auf jedem Host noetig | Keine Installation auf dem Host |
| Detailtiefe | Hoch (OS-interne Metriken) | Begrenzt (nur zugaengliche Daten) |
| Protokoll | Proprietaer (z.B. Zabbix Agent) | SNMP, WMI, SSH |
| Last auf dem Host | Gering | Keine (Abfrage vom Server) |
| Eignung | Server, VMs | Switches, Router, Drucker |

---

## SNMP – Vertiefung

### MIB-Baumstruktur (vereinfacht)

```
iso (1)
 └── org (3)
      └── dod (6)
           └── internet (1)
                ├── mgmt (2)
                │    └── mib-2 (1)
                │         ├── system (1)     → .1.3.6.1.2.1.1
                │         ├── interfaces (2) → .1.3.6.1.2.1.2
                │         ├── ip (4)         → .1.3.6.1.2.1.4
                │         └── tcp (6)        → .1.3.6.1.2.1.6
                └── private (4)
                     └── enterprises (1)     → Herstellerspezifisch
```

### SNMP-Kommunikation

```
  SNMP Manager                     SNMP Agent
  (Monitoring)                     (Switch/Server)
       |                                |
       |--- GET (.1.3.6.1.2.1.1.3) --->|  (Anfrage: sysUpTime)
       |<-- Response (45 days) ---------|  (Antwort)
       |                                |
       |<-- TRAP (linkDown) ------------|  (Spontane Meldung)
       |                                |
```

### Typische Pruefungsaspekte SNMP
- SNMP-Versionen und deren Sicherheitsunterschiede benennen
- OID-Struktur verstehen
- Unterschied GET vs. TRAP erklaeren
- Warum SNMPv3 bevorzugt wird (Verschluesselung + Authentifizierung)

---

## S.M.A.R.T. – Vertiefung

### Interpretation von S.M.A.R.T.-Werten

**Beispiel-Ausgabe (smartctl):**
```
ID# ATTRIBUTE_NAME          VALUE  WORST  THRESH  RAW_VALUE
  5 Reallocated_Sector_Ct    100    100    010     0
  9 Power_On_Hours            85     85    000     13200
194 Temperature_Celsius       065    045    000     35
197 Current_Pending_Sector    100    100    000     0
198 Offline_Uncorrectable     100    100    000     0
```

**Interpretation:**
- VALUE: Aktueller normalisierter Wert (100 = gut, sinkt bei Verschlechterung)
- WORST: Schlechtester jemals gemessener Wert
- THRESH: Schwellwert – wird VALUE < THRESH, gilt das Attribut als kritisch
- RAW_VALUE: Roher Messwert (z.B. Temperatur in °C, Stunden, Sektoranzahl)

**Warnsignale:**
- Reallocated_Sector_Ct > 0 → Platte hat bereits defekte Sektoren ersetzt
- Current_Pending_Sector > 0 → Sektoren warten auf Ueberpruefung/Ersatz
- Temperatur > 50 °C → Kuehlung pruefen

### Predictive Maintenance mit S.M.A.R.T.

```
    Zeitverlauf →
    
    Reallocated Sectors:
    |
 50 |                                          *** AUSFALL
    |                                     ****
    |                                ****
 20 |                          *****
    |                   ******
    |            ******
  5 |      *****
    | ****
  0 |**
    +-----------------------------------------> Zeit
    t0                                      t_ausfall
    
    → Trend zeigt steigende defekte Sektoren
    → Tausch empfohlen, BEVOR der Wert kritisch wird
```

---

## Schwellwerte – Vertiefung

### Schwellwert-Typen

| Typ | Beschreibung | Beispiel |
|---|---|---|
| Statischer Schwellwert | Fester Grenzwert | CPU > 90 % = Critical |
| Dynamischer Schwellwert | Basiert auf Baseline/Trend | CPU 30 % ueber Tagesdurchschnitt |
| Rate of Change | Schnelle Aenderung | Festplatte verliert 5 % Kapazitaet/Stunde |

### Alarmierung – Eskalation

```
Schwellwert ueberschritten
         |
         v
    +----+----+
    | Warning |  → E-Mail an Admin
    +---------+
         |
    (Wert steigt weiter)
         |
         v
    +----+-----+
    | Critical |  → SMS + E-Mail an Team
    +----------+
         |
    (keine Reaktion in 30 min)
         |
         v
    +----+--------+
    | Eskalation  |  → Teamleiter / Rufbereitschaft
    +-------------+
```

---

## Systemlastanalyse – Vertiefung

### Engpass-Analyse: Systematisches Vorgehen

```
1. Symptom identifizieren
   (z.B. Anwendung reagiert langsam)
         |
         v
2. CPU pruefen
   (top / htop)
   CPU < 80 %? → Kein CPU-Engpass → weiter
         |
         v
3. RAM pruefen
   (free -m)
   Swap-Nutzung hoch? → RAM-Engpass → RAM erweitern
         |
         v
4. Disk I/O pruefen
   (iostat / iotop)
   Hohe Wait-Zeiten? → I/O-Engpass → SSD einsetzen / RAID optimieren
         |
         v
5. Netzwerk pruefen
   (iftop / netstat)
   Bandbreite am Limit? → Netzwerk-Engpass → Uplink erweitern
```

### Vergleichstabelle: Monitoring-Tools

| Feature | Nagios | Zabbix | PRTG | Prometheus |
|---|---|---|---|---|
| Lizenz | Open Source | Open Source | Kommerziell | Open Source |
| Agent | Plugin-basiert | Ja (Zabbix Agent) | SNMP/Sensor | Exporter |
| Auto-Discovery | Nein (Plugin) | Ja | Ja | Nein |
| Alerting | Ja | Ja | Ja | Ja (Alertmanager) |
| Dashboard | Einfach | Gut | Sehr gut | Grafana (separat) |
| Skalierung | Mittel | Gut | Gut | Sehr gut (Cloud) |
| Typischer Einsatz | Klassische IT | Mittlere bis grosse IT | KMU | Cloud/Container |

### Typische Pruefungsaspekte
- Monitoring-Architektur erklaeren (Agent vs. Agentless)
- S.M.A.R.T.-Werte interpretieren und Handlungsempfehlung geben
- Schwellwerte fuer verschiedene Ressourcen festlegen und begruenden
- Systematisch einen Engpass identifizieren
- SNMP-Versionen vergleichen

### Haeufige Fehler
- S.M.A.R.T.-Werte ignorieren → fruehzeitiges Warnsignal fuer Festplattenausfall
- Schwellwerte ohne Baseline festlegen → fuehrt zu Fehlalarmen oder verpassten Problemen
- SNMPv1/v2c in produktiven Netzen → Community String im Klartext = Sicherheitsrisiko
- Nur CPU ueberwachen → Engpass kann auch bei RAM, Disk oder Netzwerk liegen
- Monitoring einrichten, aber Alarme nicht bearbeiten → Monitoring ist wertlos ohne Reaktion
