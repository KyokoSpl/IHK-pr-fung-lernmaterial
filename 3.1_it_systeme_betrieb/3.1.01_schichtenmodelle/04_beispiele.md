# Beispiele: 3.1.01 – Schichtenmodelle benennen und zuordnen

## ARP in der Praxis

**Beispiel 1:** Ein Mitarbeiter startet seinen PC und oeffnet den Browser. Der PC muss zuerst mit dem Default Gateway (Router, 192.168.1.1) kommunizieren. Da der ARP-Cache nach dem Neustart leer ist, sendet der PC einen ARP-Broadcast: "Wer hat 192.168.1.1?" Der Router antwortet mit seiner MAC-Adresse. Erst danach kann der PC Pakete an den Router senden. → **ARP ist Voraussetzung fuer jede IP-Kommunikation im LAN.**

**Beispiel 2:** Ein Administrator tippt in der Kommandozeile `arp -a` und sieht folgende Eintraege:

```
192.168.1.1      00-1A-2B-3C-4D-5E   dynamisch
192.168.1.50     AA-BB-CC-DD-EE-FF   dynamisch
```

Die Eintraege zeigen, dass der PC bereits mit dem Router (.1) und einem weiteren Geraet (.50) kommuniziert hat. → **Der ARP-Cache beschleunigt die Kommunikation, da keine erneuten Broadcasts noetig sind.**

---

## IPv4-Subnetting in der Praxis

**Beispiel 1 – Netzplanung:** Ein Unternehmen hat das Netz 172.16.0.0/16 und benoetigt vier Subnetze fuer die Abteilungen Entwicklung, Vertrieb, Verwaltung und Gaeste.

Loesung mit /18:
- Subnetz 1 (Entwicklung): 172.16.0.0/18 → Hosts: 172.16.0.1 – 172.16.63.254
- Subnetz 2 (Vertrieb): 172.16.64.0/18 → Hosts: 172.16.64.1 – 172.16.127.254
- Subnetz 3 (Verwaltung): 172.16.128.0/18 → Hosts: 172.16.128.1 – 172.16.191.254
- Subnetz 4 (Gaeste): 172.16.192.0/18 → Hosts: 172.16.192.1 – 172.16.255.254

Jedes Subnetz bietet 2^14 - 2 = 16.382 nutzbare Adressen.

**Beispiel 2 – Pruefungsaufgabe:** Gegeben: IP 192.168.5.130, Subnetzmaske /25 (255.255.255.128)

Berechnung:
1. /25 → Hostanteil: 7 Bit → 2^7 = 128 Adressen, 126 nutzbar
2. Schrittweite: 128
3. 130 liegt im Bereich 128–255
4. Netzadresse: 192.168.5.128
5. Broadcast: 192.168.5.255
6. Erster Host: 192.168.5.129
7. Letzter Host: 192.168.5.254

→ Die IP 192.168.5.130 ist der **zweite nutzbare Host** im Subnetz 192.168.5.128/25.

---

## MAC-Adressen in der Praxis

**Beispiel 1:** Ein Netzwerkadministrator analysiert mit Wireshark einen Ethernet-Frame:

```
Destination MAC: FF:FF:FF:FF:FF:FF  (Broadcast)
Source MAC:      00:1A:2B:3C:4D:5E
EtherType:       0x0806 (ARP)
```

Analyse: Der Frame ist ein ARP-Request (Broadcast). Die Source-MAC beginnt mit 00:1A:2B – das ist ein Hersteller-OUI, das einem bestimmten Netzwerkkartenhersteller zugeordnet ist. → **Die MAC-Adresse ermoeglicht die Identifikation des Geraets und Herstellers.**

**Beispiel 2:** Ein Administrator konfiguriert einen MAC-Filter auf dem WLAN-Access-Point. Nur die MAC-Adressen der Firmengeraete duerfen sich verbinden. Allerdings: MAC-Adressen koennen gefaelscht werden (MAC-Spoofing). → **MAC-Filterung ist keine ausreichende Sicherheitsmassnahme, nur eine ergaenzende.**

---

## Routing in der Praxis

**Beispiel 1:** Ein PC im Netz 192.168.1.0/24 will den Webserver 203.0.113.50 erreichen.

```
PC (192.168.1.10) → Default Gateway (192.168.1.1)
    Router prueft Routing-Tabelle:
    - 192.168.1.0/24  → direkt verbunden (Interface eth0)
    - 10.0.0.0/8      → next hop 10.0.0.1 (Interface eth1)
    - 0.0.0.0/0       → next hop 10.0.0.254 (Default Route)
    → 203.0.113.50 passt zu keiner spezifischen Route
    → Default Route wird verwendet → Paket geht an 10.0.0.254
```

→ **Die Default Route ist der "Ausgang" fuer alle unbekannten Ziele.**

**Beispiel 2 – Statisches vs. dynamisches Routing:**
- Kleines Buero mit einem Router und einer Internetverbindung: Statische Default-Route genuegt (`0.0.0.0/0 via ISP-Gateway`)
- Grosses Unternehmen mit 20 Standorten und redundanten Verbindungen: Dynamisches Routing mit OSPF, da sich Routen bei Ausfaellen automatisch anpassen

→ **Statisches Routing = einfach, manuell, fuer kleine Netze. Dynamisches Routing = automatisch, flexibel, fuer komplexe Netze.**

---

## Switching in der Praxis

**Beispiel 1:** Ein neuer Switch wird in Betrieb genommen. Die MAC-Adresstabelle ist leer.

```
1. PC-A (Port 1) sendet Frame an PC-B
   → Switch lernt: MAC-A = Port 1
   → Ziel-MAC-B unbekannt → Flooding an alle Ports (ausser Port 1)

2. PC-B (Port 3) antwortet
   → Switch lernt: MAC-B = Port 3
   → Ziel-MAC-A bekannt (Port 1) → Frame nur an Port 1

3. Naechster Frame von PC-A an PC-B:
   → MAC-B bekannt (Port 3) → Frame nur an Port 3 (kein Flooding mehr)
```

→ **Ein Switch lernt durch den Datenverkehr und wird mit der Zeit effizienter.**

---

## TCP vs. UDP in der Praxis

**Beispiel 1 – TCP:** Ein Nutzer laedt eine 50 MB grosse Datei per FTP herunter. TCP stellt sicher, dass alle Pakete ankommen und in der richtigen Reihenfolge zusammengesetzt werden. Geht ein Paket verloren, fordert TCP es erneut an. → **TCP garantiert Vollstaendigkeit, daher ideal fuer Dateiuebertragung.**

**Beispiel 2 – UDP:** Ein Mitarbeiter fuehrt eine VoIP-Konferenz. Geht ein Sprachpaket verloren, wuerde eine Neuanforderung (wie bei TCP) zu Verzoegerungen fuehren. Stattdessen wird das fehlende Paket uebersprungen – ein kurzes Knacken ist besser als eine Verzoegerung. → **UDP ist ideal fuer Echtzeitkommunikation.**

**Beispiel 3 – DNS:** Eine DNS-Anfrage nutzt standardmaessig UDP (Port 53), da die Anfrage klein ist und schnell gehen soll. Ist die Antwort groesser als 512 Bytes (z.B. bei Zonentransfers), wechselt DNS zu TCP. → **Manche Protokolle nutzen beide Transportprotokolle je nach Situation.**
