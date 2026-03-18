# Vertiefung und Uebungen: 3.1.02 – Netzwerkkomponenten vergleichen und beschreiben

## Vertiefung

### Gesamtvergleich aller Netzwerkkomponenten

| Kriterium | Bridge | Switch | Router | Firewall |
|-----------|--------|--------|--------|----------|
| OSI-Schicht | 2 | 2 (L3-Switch: 2+3) | 3 | 3–7 |
| Adressierung | MAC | MAC (+ IP bei L3) | IP | IP, Port, Protokoll |
| Trennt Kollisionsdomaene | Ja | Ja (pro Port) | Ja | Ja |
| Trennt Broadcast-Domaene | Nein | Nein (nur mit VLAN) | Ja | Ja |
| Hauptfunktion | Segmente verbinden | Frames weiterleiten | Pakete routen | Verkehr filtern |
| Typischer Einsatz | Legacy/WLAN-Bridge | LAN-Infrastruktur | WAN/Internet-Anbindung | Netzwerksicherheit |

### ASCII-Darstellung: Typische Netzwerktopologie

```
                        [Internet]
                            |
                       [Firewall]
                            |
                         [Router]
                        /        \
                 [Switch-1]    [Switch-2]
                /    |    \       |    \
            [PC-A] [PC-B] [PC-C] [Server-1] [Server-2]
            
            VLAN 10 (Buero)       VLAN 20 (Server)
```

### DMZ-Architektur mit Firewall

```
                [Internet]
                     |
              [Firewall (extern)]
                     |
                   [DMZ]
              Webserver, Mailserver
                     |
              [Firewall (intern)]
                     |
               [Internes LAN]
           PCs, Datenbankserver
```

Die DMZ (Demilitarisierte Zone) ist ein separates Netzwerksegment zwischen dem internen Netz und dem Internet. Oeffentlich erreichbare Server (Web, Mail) stehen in der DMZ. Selbst bei Kompromittierung eines DMZ-Servers ist das interne Netz durch die innere Firewall geschuetzt.

### Wann welche Komponente?

| Anforderung | Komponente | Begruendung |
|-------------|------------|-------------|
| Geraete im LAN verbinden | Switch | Dedizierte Bandbreite pro Port, MAC-basierte Weiterleitung |
| Zwei Netze verbinden | Router | IP-basiertes Routing zwischen Subnetzen |
| Internetzugang fuer LAN | Router + Firewall | Router fuer Routing/NAT, Firewall fuer Sicherheit |
| Oeffentliche Server schuetzen | Firewall + DMZ | Trennung von oeffentlichen und internen Diensten |
| VLANs routen | Layer-3-Switch | Inter-VLAN-Routing ohne externen Router |
| WLAN mit LAN verbinden | Wireless Bridge / AP | Kabellose Anbindung an das kabelgebundene Netz |
| Netzwerk vor Angriffen schuetzen | Firewall (Stateful/NGFW) | Regelbasierte Zugriffskontrolle |

### Typische Pruefungsaspekte

- Netzwerkkomponenten der korrekten OSI-Schicht zuordnen
- Funktionsweise von Switch, Router und Firewall beschreiben
- Szenario: Welche Komponente loest ein bestimmtes Problem?
- Unterschied Paketfilter vs. Stateful Inspection erklaeren
- DMZ-Konzept verstehen und erklaeren koennen
- Layer-2- vs. Layer-3-Switch unterscheiden

### Haeufige Fehler

- Switch und Hub verwechseln: Hub sendet an alle Ports (dumm), Switch leitet gezielt weiter (intelligent)
- Router und Switch vermischen: Switch = Schicht 2 (MAC), Router = Schicht 3 (IP)
- Firewall nur als "Paketfilter" beschreiben – Stateful Inspection und Application Layer fehlen
- Vergessen, dass ein Router Broadcast-Domaenen trennt (Switch ohne VLAN nicht)
- Layer-3-Switch mit Router gleichsetzen: L3-Switch routet VLANs, Router verbindet WAN-Strecken

---

## Uebungen

**Aufgabe 1:** Ordne die folgenden Netzwerkkomponenten der korrekten OSI-Schicht zu: Hub, Switch, Router, Bridge, Firewall (Paketfilter), Repeater.

**Aufgabe 2:** Beschreibe den Unterschied zwischen einer Kollisionsdomaene und einer Broadcast-Domaene. Welche Geraete trennen welche Domaene?

**Aufgabe 3:** Ein Unternehmen hat ein flaches Netzwerk mit 200 PCs an einem Switch. Es kommt zu Broadcast-Storms. Welche zwei Massnahmen koennen helfen?

**Aufgabe 4:** Erklaere den Unterschied zwischen einem Paketfilter und einer Stateful Inspection Firewall. Nenne jeweils ein Beispiel fuer eine Regel.

**Aufgabe 5:** Zeichne eine einfache Netzwerktopologie mit DMZ: Welche Komponenten werden benoetigt und wo stehen sie?

**Aufgabe 6:** Ein kleines Buero hat drei Abteilungen (Verwaltung, Entwicklung, Gaeste), die auf einem Switch getrennt werden sollen. Welche Technologie wird eingesetzt? Wie koennen die Abteilungen trotzdem miteinander kommunizieren?

**Aufgabe 7:** Erklaere, warum ein Layer-3-Switch in einem Netzwerk mit vielen VLANs sinnvoller sein kann als ein externer Router.

---

## Loesungen

**Aufgabe 1:**
- Schicht 1 (Physical): Hub, Repeater
- Schicht 2 (Data Link): Switch, Bridge
- Schicht 3 (Network): Router
- Schicht 3–4: Firewall (Paketfilter)

**Aufgabe 2:**
- Kollisionsdomaene: Bereich, in dem zwei gleichzeitig sendende Geraete eine Kollision verursachen. Wird getrennt durch: Switch, Bridge, Router.
- Broadcast-Domaene: Bereich, in dem ein Broadcast-Frame alle Geraete erreicht. Wird getrennt durch: Router (und Layer-2-Switch mit VLANs).

**Aufgabe 3:**
1. VLANs einrichten: Logische Segmentierung reduziert die Broadcast-Domaene. Jedes VLAN bildet eine eigene Broadcast-Domaene.
2. Router oder Layer-3-Switch einsetzen: Trennt Broadcast-Domaenen physisch auf Schicht 3.

**Aufgabe 4:**
- Paketfilter: Prueft jedes Paket einzeln anhand von IP, Port und Protokoll. Beispiel-Regel: "Erlaube eingehenden TCP-Verkehr auf Port 443 von jeder Quelle zum Webserver 10.0.1.5."
- Stateful Inspection: Merkt sich den Zustand von Verbindungen in einer State Table. Beispiel-Regel: "Erlaube Antwortpakete (ESTABLISHED, RELATED) zu intern initiierten Verbindungen automatisch."

**Aufgabe 5:**
```
[Internet] → [Externe Firewall] → [DMZ-Switch] (Webserver, Mailserver) → [Interne Firewall] → [LAN-Switch] (PCs, Datenbankserver)
```
Benoetigt: 2 Firewalls (oder eine mit 3 Interfaces), 2 Switches, eine DMZ fuer oeffentliche Dienste.

**Aufgabe 6:**
VLANs werden auf dem Switch konfiguriert: VLAN 10 (Verwaltung), VLAN 20 (Entwicklung), VLAN 30 (Gaeste). Damit die VLANs miteinander kommunizieren koennen, wird ein Router oder Layer-3-Switch fuer Inter-VLAN-Routing benoetigt. Alternativ: Router-on-a-Stick mit Subinterfaces.

**Aufgabe 7:**
Ein Layer-3-Switch routet VLAN-Verkehr direkt in Hardware (ASIC-basiert), was deutlich schneller ist als ein externer Router, der den Verkehr ueber ein einzelnes Interface verarbeiten muss (Router-on-a-Stick). Bei vielen VLANs und hohem Inter-VLAN-Traffic wird der Router zum Engpass. Der L3-Switch bietet Wire-Speed-Routing zwischen VLANs.
