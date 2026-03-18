# Beispiele: 3.1.11 – Monitoringsysteme anwenden und Ergebnisse interpretieren

## Festlegen von Monitoringdaten

**Beispiel 1:** Ein Unternehmen betreibt einen Webshop auf einem Linux-Server. Der Admin richtet Zabbix ein und definiert folgende Monitoringdaten:

| Metrik | Intervall | Begruendung |
|---|---|---|
| CPU-Auslastung | 60 s | Erkennung von Lastspitzen |
| RAM-Belegung | 60 s | Warnung vor Speichermangel |
| Festplattenbelegung | 300 s | Warnung vor vollem Speicher |
| HTTP-Antwortzeit | 30 s | Erkennung von Performance-Problemen |
| HTTP-Statuscode | 30 s | Erkennung von Ausfaellen (503, 500) |
| Festplatten-S.M.A.R.T. | 3600 s | Fruehwarnung vor Defekt |

→ Die Auswahl orientiert sich an den geschaeftskritischen Anforderungen des Webshops.

**Beispiel 2:** Ein Admin ueberwacht 20 Netzwerk-Switches per SNMP. Er fragt folgende OIDs ab:
- ifOperStatus (Schnittstelle up/down)
- ifInOctets / ifOutOctets (Datenverkehr pro Interface)
- sysUpTime (Laufzeit des Switches)

→ Bei einem Link-Down wird automatisch ein SNMP Trap an den Monitoring-Server gesendet.

---

## Schwellwerte

**Beispiel 1:** Der Admin setzt folgende Schwellwerte fuer den Webshop-Server:

```
CPU:
  OK:       < 70 %
  Warning:  70–90 %
  Critical: > 90 %

Festplatte:
  OK:       < 80 %
  Warning:  80–90 %
  Critical: > 95 %
```

Am Freitag Nachmittag steigt die CPU-Auslastung durch eine Marketing-Aktion auf 85 %. Zabbix sendet eine **Warning-Mail** an den Admin. Der Admin prueft die Ursache und stellt fest, dass PHP-Prozesse durch erhoehten Traffic mehr CPU benoetigen. → Keine sofortige Massnahme noetig, aber der Admin plant fuer die naechste Aktion einen zweiten Webserver.

**Beispiel 2:** Die Festplattenbelegung eines Logservers steigt von 60 % auf 88 % innerhalb von 3 Tagen. Schwellwert: Warning bei 80 %. Der Admin erhaelt eine Warnung und entdeckt, dass ein Dienst ueberdimensionierte Log-Dateien schreibt. Massnahme: Log-Rotation aktivieren und alte Logs archivieren.

---

## Predictive Maintenance

**Beispiel 1:** Der Monitoring-Server zeigt fuer eine Festplatte im RAID-5-Array folgende S.M.A.R.T.-Entwicklung:

```
Woche 1: Reallocated Sectors = 0
Woche 4: Reallocated Sectors = 3
Woche 8: Reallocated Sectors = 12
Woche 12: Reallocated Sectors = 47
```

→ Die Anzahl der ersetzten Sektoren steigt exponentiell. Obwohl die Platte noch funktioniert, plant der Admin den proaktiven Tausch. Waehrend der naechsten Wartungsperiode wird die Platte ersetzt und das RAID rebuildet sich ohne Datenverlust.

**Beispiel 2:** Monitoring zeigt, dass die CPU-Temperatur eines Servers in den letzten 6 Monaten langsam von 45 °C auf 62 °C gestiegen ist. Der Admin prueft den Server und findet einen verstopften Luefter. Reinigung senkt die Temperatur auf 42 °C. → Predictive Maintenance hat einen moeglichen Hitzeschaden verhindert.

---

## Ressourcenengpaesse

**Beispiel 1:** Ein Datenbankserver reagiert seit zwei Tagen langsam. Der Admin analysiert:

```
$ top
  PID  USER   %CPU  %MEM  COMMAND
  3451 mysql  15.2  92.3  mysqld
  ...

$ free -m
              total    used    free    shared  buff/cache   available
Mem:          8192     7850     50      120     292          120
Swap:         4096     3200     896
```

→ **RAM-Engpass**: MySQL belegt 92 % des RAMs, 3,2 GB Swap werden genutzt. Swap ist langsam (Festplatte statt RAM). Loesung: RAM von 8 GB auf 16 GB erweitern oder MySQL-Konfiguration optimieren (innodb_buffer_pool_size reduzieren).

**Beispiel 2:** Ein Fileserver ist langsam beim Kopieren grosser Dateien. Analyse:

```
$ iostat -x 1
Device   %util  avgqu-sz  await  r/s   w/s
sda      98.5   12.3      85.2   120   340
```

→ **Disk-I/O-Engpass**: %util bei 98,5 % (Festplatte arbeitet am Limit). Hohe Warteschlange (avgqu-sz = 12,3). Loesung: SSDs einsetzen oder RAID-Level optimieren (z.B. RAID 10 statt RAID 5).

---

## SNMP-Monitoring

**Beispiel 1:** Ein Admin richtet SNMP-Monitoring fuer einen Cisco-Switch in Zabbix ein:

1. Am Switch: SNMP-Community konfigurieren
   ```
   snmp-server community LeseZugriff ro
   ```
2. In Zabbix: Host anlegen, SNMP-Interface konfigurieren
3. Template „Cisco Switch SNMP" zuweisen → Automatisches Monitoring aller Interfaces

Ergebnis: Zabbix zeigt pro Interface den Datenverkehr, Status (up/down) und Fehler.

**Beispiel 2:** Ein Switch sendet einen SNMP Trap „linkDown" an den Monitoring-Server. Der Admin sieht im Dashboard:

```
[2026-03-17 09:15:23] CRITICAL: Switch-EG-01 - Interface GigabitEthernet0/5 - linkDown
```

→ Der Admin prueft vor Ort: Das Patchkabel ist defekt. Austausch des Kabels → Interface geht wieder auf „up".

---

## Systemlastanalyse

**Beispiel 1:** Ein 4-Kern-Linux-Server zeigt folgende Load Average:

```
$ uptime
 10:30:00 up 120 days, load average: 6.50, 5.80, 4.20
```

→ Load Average von 6,5 bei 4 Kernen = **Ueberlastung** (Faustregel: Load sollte < Anzahl Kerne sein). Der Trend steigt (1-min > 5-min > 15-min). Sofortige Analyse noetig:
- `top` zeigt: Ein Java-Prozess belegt 3 CPU-Kerne → Anwendungsfehler (Memory Leak fuehrt zu Garbage Collection).
- Loesung: Java-Anwendung neustarten, Speichereinstellungen anpassen.

**Beispiel 2:** Der Admin erstellt einen monatlichen Kapazitaetsbericht fuer den Fileserver:

```
Monat     Belegung   Zuwachs   Prognose: Voll in
Januar    2.4 TB     +120 GB   -
Februar   2.5 TB     +100 GB   -
Maerz     2.6 TB     +100 GB   ca. 14 Monate (bei 4 TB Kapazitaet)
```

→ Basierend auf der Trendanalyse muss in ca. 12 Monaten entweder Speicher erweitert oder alte Daten archiviert werden. → Kapazitaetsplanung einleiten.
