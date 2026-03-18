# Uebungen: 3.1.11 – Monitoringsysteme anwenden und Ergebnisse interpretieren

## Monitoringdaten und Schwellwerte

**Aufgabe 1:** Ein Unternehmen moechte seinen neuen Linux-Webserver ueberwachen. Nenne mindestens sechs Metriken, die ueberwacht werden sollten, und ordne jeder Metrik eine Kategorie zu (CPU, RAM, Disk, Netzwerk, Dienst, Hardware).

**Aufgabe 2:** Definiere sinnvolle Schwellwerte (OK / Warning / Critical) fuer folgende Metriken:
- a) RAM-Belegung
- b) Festplattenbelegung
- c) CPU-Temperatur

**Aufgabe 3:** Erklaere, was „Alert Fatigue" ist und wie man sie vermeidet.

---

## SNMP

**Aufgabe 4:** Erklaere die vier SNMP-Operationen: GET, SET, GETNEXT, TRAP.

**Aufgabe 5:** Vergleiche SNMPv2c und SNMPv3. Warum sollte in produktiven Netzwerken SNMPv3 eingesetzt werden?

**Aufgabe 6:** Ein Switch sendet einen SNMP Trap mit der Meldung „linkDown" fuer Interface GigabitEthernet0/12. Nenne drei moegliche Ursachen und beschreibe, wie du systematisch vorgehst.

---

## S.M.A.R.T. und Predictive Maintenance

**Aufgabe 7:** Interpretiere die folgenden S.M.A.R.T.-Daten einer Festplatte:

```
ID# ATTRIBUTE_NAME          VALUE  WORST  THRESH  RAW_VALUE
  5 Reallocated_Sector_Ct    092    092    010     28
  9 Power_On_Hours            078    078    000     35000
194 Temperature_Celsius       058    040    000     42
197 Current_Pending_Sector    098    098    000     5
```

Wie bewertest du den Zustand der Festplatte? Was empfiehlst du?

**Aufgabe 8:** Erklaere den Unterschied zwischen reaktiver Wartung, praeventiver Wartung und Predictive Maintenance. Nenne fuer jede Strategie ein IT-Beispiel.

---

## Ressourcenengpaesse und Systemlast

**Aufgabe 9:** Ein Server zeigt folgende Werte:
```
CPU: 25 %
RAM: 45 %
Disk I/O: %util = 99 %, await = 120 ms
Netzwerk: 5 % Auslastung
```
Welche Ressource ist der Engpass? Nenne zwei Massnahmen zur Behebung.

**Aufgabe 10:** Ein Linux-Server mit 8 CPU-Kernen zeigt einen Load Average von 12.5, 10.2, 8.0. Interpretiere diese Werte. Wie ist der Trend?

**Aufgabe 11:** Nenne fuenf Linux-Befehle zur Systemanalyse und beschreibe jeweils, welche Information sie liefern.

---

## Monitoring-Tools

**Aufgabe 12:** Vergleiche Nagios und Zabbix in mindestens vier Aspekten (z.B. Lizenz, Agent, Auto-Discovery, Dashboard).

**Aufgabe 13:** Ein kleines Unternehmen (30 Server, 50 Switches) sucht ein Monitoring-Tool. Es soll kostenfrei sein, agentenbasiertes Monitoring unterstuetzen und ein integriertes Dashboard bieten. Welches Tool empfiehlst du? Begruende.

---
---

# Loesungen

## Aufgabe 1

| Metrik | Kategorie |
|---|---|
| CPU-Auslastung (%) | CPU |
| RAM-Belegung (%) | RAM |
| Swap-Nutzung | RAM |
| Festplattenbelegung (%) | Disk |
| Disk I/O Wait | Disk |
| HTTP-Antwortzeit / Statuscode | Dienst |
| Netzwerk-Bandbreite (ein/aus) | Netzwerk |
| CPU-Temperatur | Hardware |

## Aufgabe 2
a) RAM: OK < 80 %, Warning 80–90 %, Critical > 90 %
b) Festplatte: OK < 80 %, Warning 80–90 %, Critical > 95 %
c) CPU-Temperatur: OK < 60 °C, Warning 60–80 °C, Critical > 80 °C

## Aufgabe 3
**Alert Fatigue** ist die Ermuedung von Administratoren durch zu viele (oft falsche) Alarme. Wenn staendig Warnungen eintreffen, die keine echten Probleme sind, werden auch kritische Alarme uebersehen.
**Vermeidung:**
- Schwellwerte sorgfaeltig an Baselines anpassen
- Hysterese konfigurieren (Alarm erst zuruecksetzen, wenn Wert deutlich sinkt)
- Alarme priorisieren (Critical, Warning, Info)
- Nicht relevante Metriken deaktivieren

## Aufgabe 4
- **GET:** Manager fragt einen bestimmten Wert vom Agenten ab (z.B. CPU-Auslastung)
- **SET:** Manager setzt einen Wert auf dem Agenten (z.B. Interface-Beschreibung aendern)
- **GETNEXT:** Manager fragt den naechsten Wert in der MIB-Baumstruktur ab (zum Durchlaufen der MIB)
- **TRAP:** Agent sendet unaufgefordert eine Nachricht an den Manager bei einem Ereignis (z.B. Link-Down)

## Aufgabe 5

| Aspekt | SNMPv2c | SNMPv3 |
|---|---|---|
| Authentifizierung | Community String (Klartext) | Benutzername + Passwort (MD5/SHA) |
| Verschluesselung | Keine | Ja (AES/DES) |
| Sicherheitsniveau | Gering | Hoch |

In produktiven Netzwerken sollte SNMPv3 eingesetzt werden, weil der Community String bei v2c im Klartext uebertragen wird. Ein Angreifer koennte den String abfangen und damit Netzwerkgeraete auslesen oder konfigurieren.

## Aufgabe 6
**Moegliche Ursachen:**
1. Kabel defekt oder nicht eingesteckt
2. Gegensprechstelle (z.B. Server, Access Point) ausgeschaltet oder defekt
3. Port am Switch administrativ deaktiviert oder fehlkonfiguriert

**Systematisches Vorgehen:**
1. Im Monitoring pruefen, welches Geraet an GigabitEthernet0/12 angeschlossen ist (Dokumentation/CMDB)
2. Vor Ort pruefen: Kabel eingesteckt? Link-LED am Switch und Gegensprechstelle?
3. Kabel testen oder tauschen
4. Falls Kabel OK: Gegensprechstelle pruefen (Neustart, NIC-Status)
5. Switch-Port pruefen: `show interface GigabitEthernet0/12` (Errors, Administrativer Status)

## Aufgabe 7
- **Reallocated_Sector_Ct: RAW = 28** → 28 Sektoren wurden bereits als defekt markiert und ersetzt. Das ist ein Warnsignal.
- **Power_On_Hours: RAW = 35.000** → ca. 4 Jahre Betriebszeit. Die Platte hat ein hohes Alter.
- **Temperature: 42 °C** → Im normalen Bereich.
- **Current_Pending_Sector: RAW = 5** → 5 Sektoren warten auf Ueberpruefung. Weiteres Warnsignal.

**Bewertung:** Festplatte zeigt deutliche Verschleisserscheinungen. Empfehlung: **Sofortiger Tausch** im naechsten Wartungsfenster. Daten vorher sichern (falls nicht durch RAID geschuetzt).

## Aufgabe 8
- **Reaktive Wartung:** Erst handeln, wenn ein Ausfall eintritt. Beispiel: Server-Festplatte faellt aus → erst dann Ersatz beschaffen.
- **Praeventive Wartung:** Regelmaessige Wartung nach Zeitplan. Beispiel: Alle 3 Jahre werden Festplatten getauscht, unabhaengig vom Zustand.
- **Predictive Maintenance:** Wartung basierend auf Monitoring-Daten und Trends. Beispiel: S.M.A.R.T.-Werte zeigen steigende Sektorfehler → Platte wird vor dem Ausfall getauscht.

## Aufgabe 9
**Engpass: Disk I/O** (%util = 99 %, das Laufwerk arbeitet am Limit). CPU und RAM sind kaum ausgelastet, Netzwerk ist frei.
**Massnahmen:**
1. HDDs durch SSDs ersetzen (deutlich hoehere IOPS)
2. RAID-Level optimieren (z.B. von RAID 5 auf RAID 10 fuer bessere Schreibperformance)

Weitere Option: Pruefen, welcher Prozess die I/O verursacht (iotop), ggf. Datenbankabfragen optimieren.

## Aufgabe 10
- Load Average: 12.5 (1 min), 10.2 (5 min), 8.0 (15 min) bei 8 Kernen
- **Interpretation:** Alle drei Werte liegen ueber der Kernanzahl (8) → Server ist ueberlastet
- **Trend:** Der 1-Minuten-Wert (12,5) ist hoeher als der 15-Minuten-Wert (8,0) → die Last **steigt aktuell** an. Sofortige Analyse mit `top` oder `htop` noetig.

## Aufgabe 11

| Befehl | Information |
|---|---|
| top / htop | CPU- und RAM-Auslastung pro Prozess in Echtzeit |
| free -m | RAM- und Swap-Belegung in Megabyte |
| df -h | Festplattenbelegung pro Dateisystem |
| iostat -x | Disk-I/O-Statistiken (Auslastung, Warteschlange, Latenz) |
| uptime | Betriebszeit und Load Average (1, 5, 15 Minuten) |

## Aufgabe 12

| Aspekt | Nagios | Zabbix |
|---|---|---|
| Lizenz | Open Source (Core) | Open Source |
| Agent | Plugin-basiert (extern) | Eigener Agent (Zabbix Agent) |
| Auto-Discovery | Nicht nativ (Plugin) | Ja (integriert) |
| Dashboard | Einfach, veraltet | Modern, anpassbar |
| SNMP-Support | Ja (Plugin) | Ja (nativ) |
| Skalierung | Mittel (erfordert Add-ons) | Gut (Proxies fuer verteiltes Monitoring) |

## Aufgabe 13
**Empfehlung: Zabbix.** Begruendung:
1. **Kostenfrei** (Open Source, keine Lizenzkosten)
2. **Agentenbasiertes Monitoring** mit eigenem Zabbix-Agent fuer detaillierte Server-Ueberwachung
3. **Integriertes Dashboard** mit anpassbaren Graphen und Karten
4. **Auto-Discovery** fuer die 50 Switches (SNMP-basiert)
5. Gut skalierbar fuer 30 Server + 50 Switches
