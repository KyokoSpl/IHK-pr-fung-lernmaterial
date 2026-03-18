# Beispiele: 3.1.03 – Netzwerkkonzepte benennen und charakterisieren

## Netzwerktypen in der Praxis

**Beispiel 1 – LAN:** Ein Unternehmen hat ein Buerogebaeude mit 50 Arbeitsplaetzen. Alle PCs sind ueber Switches verbunden und nutzen das Netz 192.168.1.0/24. Der Fileserver und Drucker stehen im selben Gebaeude. → **LAN**, da lokal begrenzt, eigene Infrastruktur, hohe Datenrate.

**Beispiel 2 – WAN:** Dasselbe Unternehmen hat eine Filiale in einer anderen Stadt. Die beiden Standorte werden ueber eine gemietete MPLS-Leitung des Providers verbunden. → **WAN**, da stadtuebergreifend, Provider-Infrastruktur.

**Beispiel 3 – MAN:** Eine Universitaet verbindet drei Campusstandorte innerhalb einer Stadt ueber Glasfaserleitungen des staedtischen Netzbetreibers. → **MAN**, da staedte­uebergreifend (innerhalb einer Stadt), Provider-Infrastruktur.

---

## Netzwerktopologien in der Praxis

**Beispiel 1 – Sterntopologie:** In einem Buero sind 20 PCs ueber einen zentralen Switch verbunden. Ein PC faellt aus → alle anderen arbeiten weiter. Der Switch faellt aus → alle PCs verlieren die Verbindung. → Typische **Stern-Topologie** mit Switch als Single Point of Failure.

**Beispiel 2 – Mesh im Backbone:** Ein Rechenzentrum hat vier Core-Switches. Jeder Switch ist mit jedem anderen verbunden. Faellt ein Switch aus, existieren alternative Wege. → **Teilvermaschte Topologie** fuer Redundanz im Backbone.

---

## VLAN in der Praxis

**Beispiel 1:** Ein mittelstaendisches Unternehmen hat drei Abteilungen: Verwaltung, Entwicklung, Vertrieb. Alle nutzen denselben physischen Switch. Der Administrator konfiguriert:

```
VLAN 10 (Verwaltung):  Port 1-8   → 192.168.10.0/24
VLAN 20 (Entwicklung): Port 9-16  → 192.168.20.0/24
VLAN 30 (Vertrieb):    Port 17-24 → 192.168.30.0/24
```

Ergebnis: Die Verwaltung kann nicht auf Entwicklungs-PCs zugreifen und umgekehrt. Broadcast-Pakete bleiben innerhalb des jeweiligen VLANs. → **Sicherheit und Performance verbessert ohne zusaetzliche Hardware.**

**Beispiel 2 – Gastnetztrennung:** Ein Hotel bietet Gaesten WLAN an. Das Gast-WLAN ist in VLAN 99 isoliert. Gaeste koennen ins Internet, haben aber keinen Zugriff auf das Hotelverwaltungsnetz (VLAN 10). → **VLAN trennt Gastverkehr vom produktiven Netz.**

---

## Strukturierte Verkabelung in der Praxis

**Beispiel 1:** Ein neues Buerogebaeude mit drei Stockwerken wird verkabelt:

```
Keller:
  Standortverteiler (SV) mit Glasfaseranschluss zum Nachbargebaeude
  → Primaerverkabelung: Singlemode-Glasfaser, 500 m

Jedes Stockwerk:
  Gebaeudeverteilerschrank (GV) im Technikraum
  → Sekundaerverkabelung: Multimode-Glasfaser vom Keller, je 30 m

Bueros:
  Etagenverteiler (EV) = Patchfeld + Switch
  → Tertiaerverkabelung: Cat6a-Kupferkabel zu den Datendosen, max. 90 m
  → Patchkabel: je 3 m Switch-seitig und Arbeitsplatz-seitig
```

→ **Normgerechte Verkabelung nach EN 50173 garantiert Zukunftssicherheit und einfache Wartung.**

---

## WLAN-Sicherheit in der Praxis

**Beispiel 1 – WPA2-Enterprise:** Ein Unternehmen mit 200 Mitarbeitern nutzt WLAN. Jeder Mitarbeiter authentifiziert sich mit seinem Active-Directory-Konto ueber 802.1X. Der WLAN-Access-Point leitet die Anmeldedaten an den RADIUS-Server weiter, der sie gegen das Active Directory prueft. → **WPA2-Enterprise bietet individuelle Authentifizierung statt eines gemeinsamen Passwortes.**

**Beispiel 2 – Unsicheres WLAN:** Ein kleines Cafe bietet offenes WLAN ohne Verschluesselung. Ein Angreifer kann mit einem Sniffer (z.B. Wireshark) den gesamten Datenverkehr mitlesen. → **Ohne WPA2/WPA3 ist jede WLAN-Kommunikation abhoerbar.** WPA3 mit OWE wuerde selbst offene Netze verschluesseln.

---

## VPN in der Praxis

**Beispiel 1 – Homeoffice (End-to-Site):** Ein Mitarbeiter arbeitet von zu Hause. Er startet den VPN-Client auf seinem Laptop, authentifiziert sich mit Benutzername, Passwort und einem zweiten Faktor (Token). Der VPN-Tunnel wird zum Firmen-VPN-Gateway aufgebaut. Der Mitarbeiter kann nun auf interne Ressourcen (Fileserver, Intranet) zugreifen, als waere er im Buero. → **End-to-Site-VPN fuer Remote-Access.**

**Beispiel 2 – Filialanbindung (Site-to-Site):** Zwei Unternehmensstandorte in verschiedenen Staedten werden ueber einen IPsec-Tunnel verbunden. Die Router an beiden Standorten bauen den Tunnel automatisch auf. Mitarbeiter an Standort A koennen auf Server an Standort B zugreifen, ohne VPN-Client. → **Site-to-Site-VPN fuer permanente Standortvernetzung.**

---

## Zugriffskontrolle in der Praxis

**Beispiel 1 – RADIUS:** Ein Unternehmen nutzt 802.1X fuer die WLAN-Authentifizierung. Wenn ein neuer Mitarbeiter sein Notebook mit dem WLAN verbindet, wird er aufgefordert, seine Domaenen-Zugangsdaten einzugeben. Der Access Point sendet die Daten an den RADIUS-Server (z.B. Microsoft NPS), der sie gegen das Active Directory prueft. Bei Erfolg wird der Mitarbeiter in das richtige VLAN geschaltet (z.B. VLAN 20 fuer Entwicklung). → **RADIUS ermoeglicht individuelle Authentifizierung und dynamische VLAN-Zuweisung.**

**Beispiel 2 – Kerberos:** Ein Mitarbeiter meldet sich morgens an seinem Windows-PC an. Der Domain Controller (KDC) stellt ein TGT aus. Als der Mitarbeiter den Fileserver oeffnet, wird automatisch ein Service Ticket angefordert und prasentiert – ohne erneute Passworteingabe. → **Kerberos ermoeglicht Single Sign-On: Ein Login fuer alle Dienste.**

---

## Bluetooth in der Praxis

**Beispiel 1:** Ein Mitarbeiter verbindet sein Bluetooth-Headset mit dem Firmen-Smartphone. Reichweite: ca. 10 m. Die Kopplungs erfolgt ueber einen PIN (Pairing). → **Bluetooth PAN fuer Peripheriegeraete.**

**Beispiel 2:** Ein IoT-Sensor ueberwacht die Raumtemperatur und sendet die Daten per Bluetooth Low Energy (BLE) an ein Gateway. BLE verbraucht wenig Energie und eignet sich fuer batteriebetriebene Geraete. → **BLE fuer IoT-Anwendungen.**
