# Vertiefung: 3.1.03 – Netzwerkkonzepte benennen und charakterisieren

## Netzwerktypen – Vertiefung

### Detaillierter Vergleich

| Kriterium | LAN | MAN | WAN | GAN |
|-----------|-----|-----|-----|-----|
| Ausdehnung | Gebaeude/Campus | Stadt/Region | Land/Kontinent | Weltweit |
| Betreiber | Eigene IT | Meist Provider | Provider | Mehrere Provider |
| Datenrate | 1–10 Gbit/s | 100 Mbit/s–10 Gbit/s | 10 Mbit/s–1 Gbit/s | Variabel |
| Latenz | Sehr gering | Gering | Mittel | Hoch |
| Kosten | Gering (eigene Infrastruktur) | Mittel | Hoch (Leitungsmiete) | Sehr hoch |
| Fehlerrate | Niedrig | Niedrig | Hoeher | Hoeher |
| Beispiel | Buero-LAN | Stadtnetz | Filialvernetzung | Internet |

---

## Netzwerktopologien – Vertiefung

### ASCII-Darstellungen

**Stern-Topologie:**
```
        [PC-A]
          |
[PC-B]--[Switch]--[PC-C]
          |
        [PC-D]
```

**Bus-Topologie:**
```
[PC-A]---[PC-B]---[PC-C]---[PC-D]
|====================================|
          gemeinsames Kabel
```

**Ring-Topologie:**
```
[PC-A] → [PC-B]
  ↑          ↓
[PC-D] ← [PC-C]
```

**Mesh-Topologie (Vollvermascht):**
```
[A]------[B]
|\ \    / /|
| \ \  / / |
|  \ \/ /  |
|   \/\/   |
|   /\/\   |
|  / /\ \  |
| / /  \ \ |
|/ /    \ \|
[C]------[D]
```

### Physische vs. logische Topologie

| Aspekt | Physische Topologie | Logische Topologie |
|--------|--------------------|--------------------|
| Definition | Tatsaechliche Kabelverbindungen | Datenfluss im Netzwerk |
| Beispiel | Sternfoermige Verkabelung zum Switch | Logisch wie ein Bus oder Ring |
| Token Ring | Physisch: Stern (am MAU) | Logisch: Ring (Token wird weitergereicht) |
| Ethernet | Physisch: Stern (am Switch) | Logisch: Bus (Broadcast-Prinzip) |

---

## WLAN-Sicherheit – Vertiefung

### WPA2 vs. WPA3

| Kriterium | WPA2 | WPA3 |
|-----------|------|------|
| Verschluesselung | AES-CCMP (128 Bit) | AES-GCMP (128/192 Bit) |
| Schluesselaustausch | 4-Way-Handshake (PSK) | SAE (Simultaneous Authentication of Equals) |
| Offline-Woerterbuch-Angriff | Moeglich (Handshake abfangen) | Nicht moeglich (SAE schuetzt) |
| Forward Secrecy | Nein | Ja (jede Sitzung eigener Schluessel) |
| Offene Netze | Unverschluesselt | OWE (Opportunistic Wireless Encryption) |
| Status | Noch akzeptabel | Empfohlener Standard |

### WLAN-Sicherheitsmassnahmen im Ueberblick

| Massnahme | Wirksamkeit | Erlaeuterung |
|-----------|-------------|--------------|
| WPA2/WPA3-Verschluesselung | Hoch | Muss aktiviert sein |
| 802.1X + RADIUS | Sehr hoch | Enterprise-Authentifizierung, individuelle Zugangsdaten |
| MAC-Filterung | Gering | Kann durch MAC-Spoofing umgangen werden |
| SSID verbergen | Sehr gering | SSID kann mit Tools trotzdem ausgelesen werden |
| Gastnetz (eigenes VLAN) | Hoch | Trennung von Gast- und Firmenverkehr |
| Kanalwahl optimieren | Mittel | Weniger Interferenzen, stabilere Verbindung |

---

## Strukturierte Verkabelung – Vertiefung

### Detailliertes Ebenenmodell

```
                     [Standortverteiler (SV)]
                      Campus Backbone (Primaer)
                      Glasfaser Singlemode
                      Zwischen Gebaeuden
                            |
              [Gebaeudeverkabelung (GV)]
               Building Backbone (Sekundaer)
               Glasfaser Multimode
               Zwischen Stockwerken
                            |
               [Etagenverteiler (EV)]
                Horizontal Cabling (Tertiaer)
                Kupfer Cat6a / Cat7
                Max. 90 m Installationskabel
                + 5 m Patchkabel Switch-seitig
                + 5 m Patchkabel Endgeraet-seitig
                = 100 m Gesamtlaenge
                            |
                      [Datendose]
                            |
                         [PC]
```

### Kabelkategorien fuer die Pruefung

| Kategorie | Max. Frequenz | Max. Datenrate | Einsatz |
|-----------|--------------|----------------|---------|
| Cat 5 | 100 MHz | 100 Mbit/s | Fast Ethernet (veraltet) |
| Cat 5e | 100 MHz | 1 Gbit/s | Gigabit Ethernet |
| Cat 6 | 250 MHz | 1 Gbit/s (10G bis 55 m) | Gigabit Ethernet |
| Cat 6a | 500 MHz | 10 Gbit/s | 10-Gigabit Ethernet |
| Cat 7 | 600 MHz | 10 Gbit/s | 10-Gigabit Ethernet (geschirmt) |
| Cat 8 | 2000 MHz | 25/40 Gbit/s | Rechenzentrum |

### Glasfaser: Singlemode vs. Multimode

| Kriterium | Singlemode (SM) | Multimode (MM) |
|-----------|-----------------|----------------|
| Kerndurchmesser | 9 µm | 50 oder 62,5 µm |
| Lichtquelle | Laser | LED oder VCSEL |
| Reichweite | bis ca. 80 km | bis ca. 500 m (OM3/OM4) |
| Datenrate | Sehr hoch (100+ Gbit/s) | Hoch (10–100 Gbit/s) |
| Kosten | Teurer (Laser, Spleissen) | Guenstiger |
| Einsatz | Primaerverkabelung, WAN | Sekundaerverkabelung, Rechenzentrum |

---

## VLAN – Vertiefung

### VLAN-Konfigurationsbeispiel

```
Switch-Ports:
Port 1-10:  VLAN 10 (Verwaltung)    → 192.168.10.0/24
Port 11-20: VLAN 20 (Entwicklung)   → 192.168.20.0/24
Port 21-24: VLAN 30 (Gaeste)        → 192.168.30.0/24
Port 48:    Trunk (zu Router/L3-Switch) → Alle VLANs

Ohne Router/L3-Switch:
VLAN 10 ←✗→ VLAN 20 (keine Kommunikation moeglich)

Mit Inter-VLAN-Routing (L3-Switch oder Router-on-a-Stick):
VLAN 10 ←✓→ VLAN 20 (Routing ueber Schicht 3)
```

### 802.1Q VLAN-Tagging

```
Normaler Ethernet-Frame:
[Dst-MAC][Src-MAC][Type][Daten][FCS]

802.1Q Tagged Frame:
[Dst-MAC][Src-MAC][802.1Q Tag (4 Bytes)][Type][Daten][FCS]
                   └→ VLAN-ID (12 Bit = 0–4095)
```

### Vorteile von VLANs

| Vorteil | Erklaerung |
|---------|-----------|
| Sicherheit | Abteilungen logisch getrennt, Zugriff ueber Firewall-Regeln |
| Performance | Reduzierte Broadcast-Domaene weniger Broadcast-Verkehr |
| Flexibilitaet | Umzug eines PCs = VLAN-Zuweisung aendern, kein Umverkabeln |
| Kosten | Ein physischer Switch statt mehrere getrennte Switches |
| Verwaltung | Zentrale Konfiguration ueber Switch-Management |

---

## RADIUS und Kerberos – Vertiefung

### RADIUS-Ablauf (802.1X WLAN-Authentifizierung)

```
[Client/Supplicant] → [Access Point/Authenticator] → [RADIUS-Server]
        |                        |                         |
        |-- EAP-Request ------->|                         |
        |                       |-- Access-Request ------>|
        |                       |                         |-- prueft Credentials
        |                       |<-- Access-Accept -------|   (gegen AD/LDAP)
        |<-- EAP-Success -------|                         |
        |                                                 |
        |===== WLAN-Zugang gewaehrt =====================|
```

### Kerberos-Ablauf (vereinfacht)

```
[Client]                    [KDC (Key Distribution Center)]        [Dienst/Server]
   |                                    |                                |
   |-- 1. Anmeldung (User/Pass) ------>|                                |
   |<-- 2. TGT (Ticket Granting Ticket)|                                |
   |                                    |                                |
   |-- 3. TGT + Dienstanfrage -------->|                                |
   |<-- 4. Service Ticket --------------|                                |
   |                                                                     |
   |-- 5. Service Ticket ------------------------------------------------>|
   |<-- 6. Zugriff gewaehrt ---------------------------------------------|
```

### RADIUS vs. Kerberos

| Kriterium | RADIUS | Kerberos |
|-----------|--------|----------|
| Einsatz | WLAN, VPN, Netzwerkzugang | Windows-Domaene, SSO |
| Authentifizierung | Benutzername/Passwort (EAP) | Ticket-basiert |
| Single Sign-On | Nein (jede Anmeldung einzeln) | Ja (TGT fuer alle Dienste) |
| Typischer Server | RADIUS-Server (z.B. FreeRADIUS, NPS) | Domain Controller (KDC) |
| Port | 1812/1813 | 88 |

---

## Typische Pruefungsaspekte

- Netzwerktypen (LAN/MAN/WAN) anhand von Szenarien zuordnen
- Topologien zeichnen und Vor-/Nachteile benennen
- WPA2 vs. WPA3: Unterschiede kennen
- VLAN-Konzept erklaeren und Vorteile benennen
- Strukturierte Verkabelung: Drei Ebenen und Kabeltypen
- RADIUS vs. Kerberos: Wann wird was eingesetzt?
- Unterschied physische vs. logische Topologie

## Haeufige Fehler

- LAN und WLAN verwechseln: WLAN ist eine drahtlose Variante eines LANs
- VLAN mit VPN verwechseln: VLAN = lokale Segmentierung, VPN = verschluesselte Verbindung ueber Internet
- SSID verbergen als "sicher" bezeichnen – es ist kein Sicherheitsmerkmal
- MAC-Filter als ausreichende Sicherheit bewerten – MAC-Adressen koennen einfach gefaelscht werden
- Tertiaerverkabelung als 100 m angeben – 90 m ist das Installationskabel, 10 m sind Patchkabel
- Kerberos mit RADIUS verwechseln: Kerberos = Ticket-basiert/SSO, RADIUS = WLAN/VPN-Authentifizierung
