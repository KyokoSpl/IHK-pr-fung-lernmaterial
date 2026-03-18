# Vertiefung und Uebungen: 1.4.01 – IT-Systeme konzeptionieren, konfigurieren, testen, dokumentieren

## Vertiefung

### Lastenheft vs. Pflichtenheft – Vergleich

| Kriterium | Lastenheft | Pflichtenheft |
|---|---|---|
| Ersteller | Auftraggeber | Auftragnehmer |
| Perspektive | Was soll erreicht werden? | Wie wird es umgesetzt? |
| Verbindlichkeit | Grundlage fuer Angebot | Grundlage fuer Vertrag |
| Detailgrad | Grob, fachlich | Detailliert, technisch |
| Zeitpunkt | Vor Ausschreibung | Nach Auftragsvergabe |

### IPv4-Adressierung – Wichtige Konzepte

| Klasse | Bereich | Privater Bereich | Subnetzmaske |
|---|---|---|---|
| A | 1.0.0.0 – 126.x.x.x | 10.0.0.0/8 | 255.0.0.0 |
| B | 128.0.0.0 – 191.x.x.x | 172.16.0.0/12 | 255.255.0.0 |
| C | 192.0.0.0 – 223.x.x.x | 192.168.0.0/16 | 255.255.255.0 |

### Typische Pruefungsaspekte
- Unterschied Lastenheft/Pflichtenheft benennen
- IP-Konfiguration: Zuordnung IP, Subnetzmaske, Gateway
- BIOS vs. UEFI (→ 1.3.03)
- Partitionierung MBR vs. GPT

### Haeufige Fehler
- Lastenheft und Pflichtenheft vertauschen
- DHCP-Server statt DNS-Server bei der Namensaufloesung angeben
- Subnetzmaske vergessen bei manueller IP-Konfiguration

---

## Uebungen

**Aufgabe 1:** Erklaere den Unterschied zwischen Lastenheft und Pflichtenheft in je einem Satz.

**Aufgabe 2:** Ein neuer Arbeitsplatz-PC soll eingerichtet werden. Nenne die 5 wichtigsten Schritte in der richtigen Reihenfolge.

**Aufgabe 3:** Ein Client soll die IP-Adresse 192.168.1.50 erhalten. Der Router hat die IP 192.168.1.1 und der DNS-Server 192.168.1.10. Welche vier Werte muessen am Client konfiguriert werden?

**Aufgabe 4:** Wann ist eine statische IP-Vergabe sinnvoller als DHCP? Nenne zwei Beispiele.

---

## Loesungen

**Aufgabe 1:** Lastenheft: Beschreibt die Anforderungen des Auftraggebers an das IT-System (Was soll erreicht werden?). Pflichtenheft: Beschreibt die technische Umsetzung durch den Auftragnehmer (Wie wird es realisiert?).

**Aufgabe 2:** (1) BIOS/UEFI konfigurieren (Boot-Reihenfolge). (2) Festplatte partitionieren und formatieren. (3) Betriebssystem installieren. (4) Netzwerkanbindung konfigurieren (IP/DHCP). (5) Software installieren und testen.

**Aufgabe 3:** IP-Adresse: 192.168.1.50, Subnetzmaske: 255.255.255.0, Standardgateway: 192.168.1.1, DNS-Server: 192.168.1.10.

**Aufgabe 4:** (1) Server – benoetigen feste IP fuer zuverlaessige Erreichbarkeit. (2) Drucker im Netzwerk – damit alle Clients den Drucker unter derselben IP finden.
