# Vertiefung und Uebungen: 3.1.09 – Risiken identifizieren, Massnahmen planen

## Vertiefung

### MTBF und Verfuegbarkeit – Zusammenhang

| Szenario | MTBF | MTTR | Verfuegbarkeit |
|---|---|---|---|
| Server ohne Ersatzteilvertrag | 50.000 h | 24 h | 50.000 / 50.024 = 99,95 % |
| Server mit 4h-Vor-Ort-Service | 50.000 h | 4 h | 50.000 / 50.004 = 99,99 % |
| Server mit Hot-Standby | 50.000 h | 0,5 h | 50.000 / 50.000,5 = 99,999 % |

→ Die MTTR hat einen deutlich groesseren Einfluss auf die Verfuegbarkeit als eine Verdopplung der MTBF.

### RPO und RTO im Vergleich

```
Zeitstrahl:
Letztes Backup                Ausfall                Wiederherstellung
     |                           |                          |
     |<---- RPO (Datenverlust) ->|<------ RTO (Downtime) -->|
     |                           |                          |
     v                           v                          v
  t = 0                      t = Ausfall              t = Recovery
```

**Pruefungsrelevante Zuordnung:**

| System | Typischer RPO | Typischer RTO |
|---|---|---|
| ERP-System | 1 Stunde | 4 Stunden |
| E-Mail-Server | 0–1 Stunde | 2 Stunden |
| Webshop | 0 (Echtzeit-Replikation) | 15 Minuten |
| Interne Wikis | 24 Stunden | 24 Stunden |
| Buchungssystem | 0 | 1 Stunde |

### PDCA im praktischen Risikomanagement

**Beispiel: Absicherung gegen Ransomware**

| Phase | Massnahme |
|---|---|
| **Plan** | Risikoanalyse: Ransomware als Top-Risiko identifiziert. Massnahme: Offline-Backups einfuehren, Mitarbeiterschulung planen |
| **Do** | 3-2-1-Backup-Regel umsetzen, Schulung durchfuehren, Endpoint-Protection installieren |
| **Check** | Nach 3 Monaten pruefen: Backup-Restore-Test erfolgreich? Phishing-Simulation: 15 % der Mitarbeiter klicken noch auf Fake-Links |
| **Act** | Backup-Konzept bestaetigt. Zusaetzliche Schulung fuer die 15 % anordnen. Phishing-Simulation kuenftig vierteljaehrlich |

### Haeufige Fehler
- MTBF als Garantiezeit missverstehen → MTBF ist ein statistischer Durchschnitt, kein Versprechen
- RPO und RTO verwechseln → RPO = Datenverlust (rueckwirkend), RTO = Wiederherstellungszeit (vorwaerts)
- PDCA als einmaligen Prozess sehen → PDCA ist ein Kreislauf, der sich staendig wiederholt
- Disaster-Recovery-Plan erstellen, aber nie testen → Ein ungetesteter Plan ist wertlos

### Typische Pruefungsaspekte
- MTBF und AFR berechnen
- Verfuegbarkeit aus MTBF und MTTR berechnen
- RPO und RTO fuer verschiedene Systeme festlegen und begruenden
- PDCA-Phasen einem konkreten Szenario zuordnen
- Bestandteile eines Disaster-Recovery-Plans benennen

---

## Uebungen

**Aufgabe 1:** Ein Server hat eine MTBF von 25.000 Stunden. Berechne die naeherungsweise AFR (Annualized Failure Rate).

**Aufgabe 2:** Ein System hat eine MTBF von 100.000 Stunden und eine MTTR von 2 Stunden. Berechne die Verfuegbarkeit in Prozent.

**Aufgabe 3:** Eine Festplatte hat eine MTBF von 1.000.000 Stunden. Ein Server hat 4 identische Festplatten.
a) Wie hoch ist die AFR einer einzelnen Festplatte?
b) Wie hoch ist die Wahrscheinlichkeit, dass **mindestens eine** der 4 Festplatten innerhalb eines Jahres ausfaellt? (Naeherung: AFR * Anzahl)

**Aufgabe 4:** Ordne die folgenden Szenarien den Begriffen RPO oder RTO zu:
- a) „Das ERP-System muss innerhalb von 4 Stunden wieder verfuegbar sein."
- b) „Es darf maximal 1 Stunde an Buchungsdaten verloren gehen."
- c) „Das Backup wird stuendlich erstellt."
- d) „Das Notfall-Handbuch sieht vor, den Datenbankserver in 30 Minuten neu aufzusetzen."

**Aufgabe 5:** Erstelle eine Mini-Risikoanalyse fuer das folgende Szenario: Ein Unternehmen betreibt einen einzelnen Datenbankserver ohne Redundanz. Benenne mindestens drei Risiken und je eine Gegenmassnahme.

**Aufgabe 6:** Erklaere die vier Phasen des PDCA-Zyklus anhand des folgenden Szenarios: Der Admin stellt fest, dass die serverseitige Festplattenauslastung regelmaessig ueber 90 % steigt.

**Aufgabe 7:** Erklaere den Unterschied zwischen Cold Site, Warm Site und Hot Site. Ordne jeweils einen typischen RTO-Wert zu.

**Aufgabe 8:** Warum ist ein regelmaessiger Test des Disaster-Recovery-Plans wichtig? Nenne drei Gruende.

---
---

# Loesungen

## Aufgabe 1
```
AFR ≈ 8.760 / 25.000 * 100 = 35,04 %
```
→ Mit ca. 35 % Ausfallwahrscheinlichkeit pro Jahr ist diese Komponente nicht besonders zuverlaessig.

## Aufgabe 2
```
Verfuegbarkeit = MTBF / (MTBF + MTTR) = 100.000 / (100.000 + 2) = 100.000 / 100.002 = 99,998 %
```

## Aufgabe 3
a)
```
AFR ≈ 8.760 / 1.000.000 * 100 = 0,876 %
```
b)
```
Wahrscheinlichkeit (Naeherung) = 4 * 0,876 % = 3,504 %
```
→ Bei 4 Festplatten steigt die Wahrscheinlichkeit, dass mindestens eine ausfaellt, auf ca. 3,5 % pro Jahr. Deshalb ist RAID als Absicherung notwendig (→ Thema 3.1.10).

## Aufgabe 4
- a) **RTO** (Maximale Wiederherstellungszeit)
- b) **RPO** (Maximaler tolerierbarer Datenverlust)
- c) **RPO** (Das Backup-Intervall bestimmt den maximalen Datenverlust)
- d) **RTO** (Geplante Wiederherstellungszeit)

## Aufgabe 5

| Risiko | Beschreibung | Gegenmassnahme |
|---|---|---|
| Hardwareausfall | Festplatte oder Netzteil defekt → Datenverlust, Ausfall | RAID-System (z.B. RAID 1 oder RAID 5) einsetzen |
| Kein Backup | Datenbank nur auf einem Server → kein Recovery moeglich | Taegliches Backup auf externen Speicher (3-2-1-Regel) |
| Single Point of Failure | Nur ein Server → kompletter Ausfall bei jedem Problem | Zweiten Server als Failover einrichten (Replikation) |
| Stromausfall | Unerwarteter Shutdown → Datenbankkorruption | USV (unterbrechungsfreie Stromversorgung) installieren |

## Aufgabe 6
- **Plan:** Analyse: Festplattenauslastung steigt regelmaessig ueber 90 %. Ursache: Log-Dateien wachsen unkontrolliert. Massnahme: Log-Rotation einrichten und aeltere Daten archivieren.
- **Do:** Log-Rotation mit logrotate konfigurieren (taegliche Rotation, Aufbewahrung 30 Tage). Aeltere Logs auf NAS archivieren.
- **Check:** Nach 4 Wochen pruefen: Festplattenauslastung liegt konstant bei 60 %. Keine Engpaesse mehr.
- **Act:** Massnahme wirksam. Log-Rotation als Standard fuer alle Server uebernehmen. Monitoring-Schwellwert auf 80 % setzen als Fruehwarnung.

## Aufgabe 7

| Typ | Beschreibung | Typischer RTO |
|---|---|---|
| **Cold Site** | Leerer Raum mit Strom und Netzwerk. Hardware muss erst beschafft und installiert werden. | Tage bis Wochen |
| **Warm Site** | Hardware vorhanden, aber Daten muessen aus Backups eingespielt werden. | Stunden bis 1–2 Tage |
| **Hot Site** | Vollstaendig gespiegelte Infrastruktur, Echtzeit-Replikation. Sofort einsatzbereit. | Minuten bis wenige Stunden |

## Aufgabe 8
1. **Fehler im Plan aufdecken:** Nur durch Tests zeigt sich, ob die Dokumentation vollstaendig und korrekt ist.
2. **Wiederherstellungszeit pruefen:** Nur ein realer Test zeigt, ob der RTO eingehalten werden kann.
3. **Mitarbeiter schulen:** Im Ernstfall muessen alle Beteiligten wissen, was zu tun ist. Regelmaessige Tests schuetzen vor Unsicherheit und Fehlern unter Druck.
