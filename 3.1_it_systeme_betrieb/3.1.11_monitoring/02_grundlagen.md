# Grundlagen: 3.1.11 – Monitoringsysteme anwenden und Ergebnisse interpretieren

## Festlegen der Monitoringdaten

**Definition:** Monitoringdaten sind Kenngroessen (Metriken), die den Zustand und die Leistung von IT-Systemen beschreiben. Sie werden kontinuierlich erfasst und ausgewertet.

**Typische Monitoringdaten:**

| Kategorie | Metriken | Bedeutung |
|---|---|---|
| CPU | Auslastung (%), Load Average | Rechenleistung des Systems |
| RAM | Belegung (%), Swap-Nutzung | Arbeitsspeicher-Auslastung |
| Festplatte | Belegung (%), IOPS, Latenz | Speicherplatz und Geschwindigkeit |
| Netzwerk | Bandbreite (bit/s), Paketverlust, Latenz | Netzwerkauslastung und Qualitaet |
| Dienste | Verfuegbarkeit (up/down), Antwortzeit | Funktionsfaehigkeit einzelner Services |
| Logs | Fehlermeldungen, Warnungen | Hinweise auf Probleme |
| Hardware | Temperatur, Lueftergeschwindigkeit, Spannung | Physischer Zustand der Hardware |

**Wichtige Begriffe:**
- **Metrik** – einzelne messbare Groesse (z.B. CPU-Auslastung in %)
- **Polling** – Aktives Abfragen von Werten in regelmaessigen Intervallen
- **Trapping** – Geraet sendet bei Ereignis selbststaendig eine Nachricht (z.B. SNMP Trap)
- **Agent** – Software auf dem ueberwachten System, die Daten sammelt und sendet
- **Agentless** – Ueberwachung ohne installierte Software (z.B. ueber SNMP, WMI)

**Gaengige Monitoring-Tools:**

| Tool | Typ | Besonderheit |
|---|---|---|
| Nagios | Open Source | Klassiker, Plugin-basiert, Check-basiert |
| Zabbix | Open Source | Umfangreich, agentenbasiert und agentless |
| PRTG | Kommerziell | Einfache Einrichtung, Sensor-basiert |
| Prometheus + Grafana | Open Source | Metriken + Visualisierung, Cloud-nativ |
| Checkmk | Open Source / Kommerziell | Basiert auf Nagios, automatische Erkennung |
| Icinga | Open Source | Nagios-Fork, modernere Architektur |

---

## Festlegen von Schwellwerten

**Definition:** Ein Schwellwert (Threshold) ist ein definierter Grenzwert, bei dessen Ueber- oder Unterschreitung eine Warnung (Warning) oder ein kritischer Alarm (Critical) ausgeloest wird.

**Typische Schwellwerte:**

| Ressource | OK | Warning | Critical |
|---|---|---|---|
| CPU-Auslastung | < 70 % | 70–90 % | > 90 % |
| RAM-Belegung | < 80 % | 80–90 % | > 90 % |
| Festplattenbelegung | < 80 % | 80–90 % | > 95 % |
| Swap-Nutzung | < 10 % | 10–50 % | > 50 % |
| Netzwerk-Paketverlust | < 1 % | 1–5 % | > 5 % |
| Antwortzeit (Ping) | < 50 ms | 50–200 ms | > 200 ms |
| CPU-Temperatur | < 60 °C | 60–80 °C | > 80 °C |

**Kernaussagen:**
- Schwellwerte muessen an die jeweilige Umgebung angepasst werden
- Zu enge Schwellwerte fuehren zu Fehlalarmen (Alert Fatigue)
- Zu weite Schwellwerte lassen echte Probleme unerkannt
- Schwellwerte sollten auf Basis von Erfahrungswerten und Baselines festgelegt werden
- Hysterese: Der Alarm wird erst zurueckgesetzt, wenn der Wert deutlich unter den Schwellwert faellt

**Wichtige Begriffe:**
- **Baseline** – Normalzustand eines Systems, als Referenz fuer Schwellwerte
- **Alert Fatigue** – Ermuedung durch zu viele (falsche) Alarme
- **Hysterese** – Verzoegerung bei der Ruecksetzung eines Alarms zur Vermeidung von Flatter-Alarmen

---

## Predictive Maintenance

**Definition:** Vorausschauende Wartung (Predictive Maintenance) nutzt Monitoring-Daten und Trendanalysen, um den Ausfall von Komponenten vorauszusagen und praeventiv zu handeln.

**Kernaussagen:**
- Basiert auf historischen Daten und Trends (z.B. steigende Festplatten-Temperatur)
- Ziel: Ungeplante Ausfaelle vermeiden, Wartung zum optimalen Zeitpunkt durchfuehren
- Typisches Beispiel: S.M.A.R.T.-Werte einer Festplatte zeigen zunehmende Sektorfehler → Festplatte tauschen, bevor sie komplett ausfaellt

**Vergleich Wartungsstrategien:**

| Strategie | Beschreibung | Beispiel |
|---|---|---|
| Reaktive Wartung | Erst handeln, wenn etwas kaputt ist | Festplatte tauschen nach Ausfall |
| Praeventive Wartung | Regelmaessig warten nach Zeitplan | Festplatten alle 3 Jahre tauschen |
| Predictive Maintenance | Warten, wenn Daten einen Ausfall vorhersagen | Tausch bei steigenden S.M.A.R.T.-Fehlern |

---

## Ressourcenengpaesse

**Definition:** Ein Ressourcenengpass (Bottleneck) liegt vor, wenn eine einzelne Ressource die Gesamtleistung eines Systems begrenzt, obwohl andere Ressourcen nicht ausgelastet sind.

**Typische Engpaesse und Symptome:**

| Ressource | Symptom | Pruefung |
|---|---|---|
| CPU | Hohe Auslastung (>90 %), langsame Antworten | top, htop, Task-Manager |
| RAM | Swap-Nutzung hoch, System wird langsam | free -m, vmstat |
| Festplatte (I/O) | Hohe Warteschlange, langsame Lese-/Schreibzugriffe | iostat, iotop |
| Netzwerk | Hohe Latenz, Paketverlust, Bandbreite am Limit | iftop, netstat, nload |

**Kernaussagen:**
- Ein Engpass kann nur durch Ueberwachung aller Ressourcen identifiziert werden
- Die Behebung eines Engpasses kann einen neuen Engpass an anderer Stelle sichtbar machen
- Systematische Analyse: Erst messen, dann optimieren

---

## SNMP / S.M.A.R.T.

### SNMP (Simple Network Management Protocol)

**Definition:** SNMP ist ein Netzwerkprotokoll zur Ueberwachung und Verwaltung von Netzwerkgeraeten (Switches, Router, Server, Drucker). Es arbeitet auf Schicht 7 (Anwendungsschicht) und nutzt UDP Port 161 (Abfragen) und Port 162 (Traps).

**Komponenten:**

| Komponente | Beschreibung |
|---|---|
| SNMP Manager | Zentrale Ueberwachungsstation (z.B. Zabbix, Nagios) |
| SNMP Agent | Software auf dem ueberwachten Geraet |
| MIB (Management Information Base) | Datenbank mit allen abfragbaren Werten (strukturiert als Baumstruktur) |
| OID (Object Identifier) | Eindeutige Kennung fuer jeden Wert in der MIB |

**SNMP-Versionen:**

| Version | Sicherheit | Authentifizierung | Verschluesselung |
|---|---|---|---|
| SNMPv1 | Gering | Community String (Klartext) | Nein |
| SNMPv2c | Gering | Community String (Klartext) | Nein |
| SNMPv3 | Hoch | Benutzername + Passwort | Ja (AES/DES) |

**SNMP-Operationen:**
- **GET** – Wert abfragen
- **SET** – Wert aendern
- **GETNEXT** – Naechsten Wert in der MIB abfragen
- **TRAP** – Geraet sendet unaufgefordert eine Benachrichtigung

**Beispiel OID:**
```
.1.3.6.1.2.1.1.1.0  → sysDescr (Systembeschreibung)
.1.3.6.1.2.1.1.3.0  → sysUpTime (Betriebszeit)
.1.3.6.1.2.1.2.2    → ifTable (Netzwerkschnittstellen)
```

### S.M.A.R.T. (Self-Monitoring, Analysis and Reporting Technology)

**Definition:** S.M.A.R.T. ist ein Ueberwachungssystem, das in Festplatten (HDD/SSD) eingebaut ist. Es erfasst interne Zustandsdaten und warnt vor moeglichen Ausfaellen.

**Wichtige S.M.A.R.T.-Attribute:**

| ID | Attribut | Beschreibung | Kritisch? |
|---|---|---|---|
| 5 | Reallocated Sectors Count | Anzahl ersetzter defekter Sektoren | Ja |
| 9 | Power-On Hours | Gesamtbetriebsstunden | Info |
| 10 | Spin Retry Count | Fehlgeschlagene Anlaufversuche (HDD) | Ja |
| 187 | Reported Uncorrectable Errors | Nicht korrigierbare Fehler | Ja |
| 194 | Temperature | Betriebstemperatur in °C | Warnung |
| 197 | Current Pending Sectors | Sektoren, die auf Umverteilung warten | Ja |
| 198 | Offline Uncorrectable | Sektoren, die auch offline nicht reparierbar sind | Ja |

**Werkzeuge:** smartctl (Linux), CrystalDiskInfo (Windows), Monitoring-Plugins

---

## Systemlastanalyse

**Definition:** Die Systemlastanalyse bewertet die Auslastung von CPU, RAM, Festplatte und Netzwerk ueber einen bestimmten Zeitraum. Sie dient der Kapazitaetsplanung und Fehlererkennung.

**Linux-Befehle fuer Systemanalyse:**

| Befehl | Funktion |
|---|---|
| top / htop | CPU- und RAM-Auslastung in Echtzeit |
| free -m | Speicherauslastung (RAM + Swap) |
| df -h | Festplattenbelegung |
| iostat | Festplatten-I/O-Statistiken |
| vmstat | Virtuelle Speicher-Statistiken |
| sar | Systemaktivitaet (historisch, aus sysstat-Paket) |
| uptime | Load Average (1, 5, 15 Minuten) |
| iftop / nload | Netzwerkbandbreite in Echtzeit |

**Load Average (Linux):**
```
$ uptime
 14:23:05 up 45 days,  load average: 1.50, 2.10, 1.80
                                       |     |     |
                                     1 min  5 min  15 min
```
- Load Average = Durchschnittliche Anzahl von Prozessen, die auf CPU-Zeit warten
- Faustregel: Load Average sollte **nicht dauerhaft ueber der Anzahl der CPU-Kerne** liegen
- Beispiel: 4-Kern-Server → Load Average dauerhaft > 4 = Ueberlastung
