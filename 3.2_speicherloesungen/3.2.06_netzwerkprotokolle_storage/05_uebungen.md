# Uebungen: 3.2.06 – Netzwerkkomponenten und -protokolle beschreiben

## NAS und SAN

**Aufgabe 1:** Erklaere den Unterschied zwischen NAS und SAN. Gehe dabei auf die Speicherebene (File-Level vs. Block-Level), das Netzwerk und typische Einsatzszenarien ein.

**Aufgabe 2:** Ein Unternehmen moechte einen neuen Speicher fuer folgende Anforderungen beschaffen:
- 30 Mitarbeiter benoetigen Zugriff auf gemeinsame Projektordner
- Windows- und Linux-Clients im Einsatz
- Budget ist begrenzt
Welche Speicherloesung empfiehlst du? Begruende deine Entscheidung.

**Aufgabe 3:** Erklaere, warum ein SAN fuer eine Datenbankumgebung besser geeignet ist als ein NAS.

---

## Ethernet

**Aufgabe 4:** Nenne die Felder eines Ethernet-Frames und beschreibe kurz die Funktion jedes Feldes.

**Aufgabe 5:** Welchen Ethernet-Standard wuerdest du fuer folgende Szenarien empfehlen? Begruende jeweils kurz.
- a) Arbeitsplatzrechner im Buero
- b) Server-zu-Switch-Verbindung im Rechenzentrum
- c) Uplink zwischen zwei Gebaeuden (Entfernung: 800 m)

**Aufgabe 6:** Was sind Jumbo Frames? Nenne einen Vorteil und eine Voraussetzung fuer deren Einsatz.

---

## Speicherprotokolle

**Aufgabe 7:** Vergleiche Fibre Channel und iSCSI in einer Tabelle mit den Kriterien: Netzwerk, Kosten, Performance, typische Hardware.

**Aufgabe 8:** Erklaere den Unterschied zwischen SMB und NFS. In welcher Umgebung wird jeweils welches Protokoll bevorzugt?

**Aufgabe 9:** Was ist eine LUN? Erklaere den Begriff und nenne ein Beispiel fuer deren Einsatz.

**Aufgabe 10:** Ein Unternehmen plant ein iSCSI-SAN. Nenne fuenf Punkte, die bei der Netzwerkkonfiguration beachtet werden muessen.

---

## Kombinierte Aufgaben

**Aufgabe 11:** Ordne die folgenden Begriffe den Kategorien NAS oder SAN zu:
- a) LUN
- b) SMB-Freigabe
- c) Fibre Channel
- d) NFS-Export
- e) iSCSI-Target
- f) File-Level Storage

**Aufgabe 12:** Ein Systemadministrator soll eine Speicherloesung fuer ein Rechenzentrum planen, das 50 virtuelle Maschinen auf VMware vSphere hostet. Die Datenbank-VMs benoetigen sehr niedrige Latenz. Beschreibe deine Empfehlung und begruende sie.

---

---

# Loesungen

## Aufgabe 1
| Kriterium | NAS | SAN |
|-----------|-----|-----|
| Speicherebene | File-Level (Dateien und Ordner) | Block-Level (Bloecke und Sektoren) |
| Netzwerk | Bestehendes LAN (Ethernet) | Dediziertes Netzwerk (FC oder iSCSI) |
| Protokolle | SMB, NFS | Fibre Channel, iSCSI |
| Eignung | Dateifreigaben, Backup, KMU | Datenbanken, Virtualisierung, Hochleistung |

NAS: Der Client greift auf Dateien zu, das NAS verwaltet das Dateisystem. SAN: Der Server bekommt rohen Block-Speicher und erstellt sein eigenes Dateisystem darauf.

## Aufgabe 2
**NAS** ist die richtige Wahl. Begruendung:
- Guenstiger als SAN (kein dediziertes Netzwerk noetig)
- Einfache Einrichtung und Verwaltung
- Unterstuetzt sowohl SMB (Windows) als auch NFS (Linux) gleichzeitig
- Fuer Dateifreigaben optimiert
- RAID fuer Ausfallsicherheit konfigurierbar

## Aufgabe 3
Datenbanken benoetigen blockbasierten Zugriff mit niedriger Latenz und hohem IOPS (I/O-Operationen pro Sekunde). SAN bietet Block-Level-Storage ueber ein dediziertes Netzwerk, wodurch die Datenbank direkt auf Bloecke zugreift – wie bei einer lokalen Festplatte. NAS arbeitet auf Dateiebene, was zusaetzlichen Overhead durch das Dateisystem-Protokoll (SMB/NFS) erzeugt und die Latenz erhoeht.

## Aufgabe 4
| Feld | Funktion |
|------|----------|
| Praeambel (8 Byte) | Synchronisation der Geraete, enthaelt Start Frame Delimiter |
| Ziel-MAC (6 Byte) | MAC-Adresse des Empfaengers |
| Quell-MAC (6 Byte) | MAC-Adresse des Senders |
| Type/Length (2 Byte) | Gibt das uebergeordnete Protokoll an (z.B. 0x0800 = IPv4) |
| Payload (46–1500 Byte) | Die eigentlichen Nutzdaten |
| FCS (4 Byte) | Frame Check Sequence – CRC-Pruefsumme zur Fehlererkennung |

## Aufgabe 5
a) **1000BASE-T (Gigabit Ethernet):** 1 Gbit/s ueber Cat5e/Cat6 reicht fuer Bueroarbeitsplaetze aus, kostenguenstig.
b) **10GBASE-T oder 10GBASE-SR (10 Gigabit Ethernet):** Server benoetigen hohe Bandbreite fuer viele gleichzeitige Zugriffe. 10 GbE ist Standard im Rechenzentrum.
c) **10GBASE-LR (10 GbE ueber Singlemode-Glasfaser):** Reichweite bis 10 km, geeignet fuer die 800 m Entfernung zwischen den Gebaeuden. Multimode (10GBASE-SR, max. 300 m) reicht nicht aus.

## Aufgabe 6
Jumbo Frames sind Ethernet-Frames mit einer erhoehten MTU von bis zu 9000 Byte (Standard: 1500 Byte). **Vorteil:** Weniger Frames fuer die gleiche Datenmenge, dadurch weniger Overhead und geringere CPU-Last – besonders wichtig bei iSCSI-Netzwerken. **Voraussetzung:** Alle Geraete im Netzwerkpfad (Switches, NICs, Server) muessen Jumbo Frames unterstuetzen und auf die gleiche MTU konfiguriert sein.

## Aufgabe 7
| Kriterium | Fibre Channel | iSCSI |
|-----------|-------------|-------|
| Netzwerk | Eigenes FC-Netzwerk (dediziert) | Bestehendes Ethernet-Netzwerk |
| Kosten | Hoch (FC-Switches, HBAs) | Gering bis mittel (Standard-Hardware) |
| Performance | Sehr hoch, sehr niedrige Latenz | Hoch (abhaengig von Ethernet-Geschwindigkeit) |
| Typische Hardware | FC-Switch, HBA, FC-Kabel | Ethernet-Switch, NIC (ggf. TOE), Cat6a/Glasfaser |

## Aufgabe 8
- **SMB:** Standard-Protokoll fuer Dateifreigaben in **Windows-Umgebungen**. Nutzt Port 445/TCP. Authentifizierung ueber Active Directory. Unter Linux ueber Samba nutzbar.
- **NFS:** Standard-Protokoll fuer Dateifreigaben in **Linux/Unix-Umgebungen**. Nutzt Port 2049/TCP (NFSv4). Authentifizierung ueber Kerberos (NFSv4). Unter Windows ueber "Services for NFS" nutzbar.

## Aufgabe 9
Eine **LUN (Logical Unit Number)** ist eine logische Speichereinheit innerhalb eines SAN-Storage-Arrays. Sie wird einem oder mehreren Servern zugewiesen. Fuer den Server erscheint die LUN wie eine lokale Festplatte, auf der er ein Dateisystem erstellt. Beispiel: Ein Storage Array stellt eine 500 GB LUN bereit, die einem Windows Server zugewiesen wird. Der Server formatiert die LUN mit NTFS und speichert dort Datenbankdateien.

## Aufgabe 10
1. **Dediziertes VLAN:** iSCSI-Traffic in ein separates VLAN isolieren
2. **Jumbo Frames:** MTU auf 9000 Byte setzen (auf allen beteiligten Geraeten)
3. **Redundanz/Multipath:** Zwei unabhaengige Netzwerkpfade fuer Ausfallsicherheit (MPIO)
4. **Bandbreite:** Mindestens 10 GbE fuer ausreichende Performance
5. **Quality of Service (QoS):** Priorisierung des iSCSI-Traffics gegenueber anderem Netzwerkverkehr

## Aufgabe 11
- a) LUN → **SAN** (logische Speichereinheit auf Block-Ebene)
- b) SMB-Freigabe → **NAS** (dateibasierter Zugriff)
- c) Fibre Channel → **SAN** (Protokoll fuer blockbasierten Zugriff)
- d) NFS-Export → **NAS** (dateibasierter Zugriff)
- e) iSCSI-Target → **SAN** (blockbasierter Zugriff ueber Ethernet)
- f) File-Level Storage → **NAS** (Zugriff auf Dateiebene)

## Aufgabe 12
Empfehlung: **Fibre-Channel-SAN** mit redundanter Switched-Fabric-Topologie.

Begruendung:
- 50 VMs benoetigen hohe gleichzeitige I/O-Leistung → SAN bietet blockbasierten Zugriff mit hoher Performance
- Datenbank-VMs benoetigen sehr niedrige Latenz → Fibre Channel bietet die niedrigste Latenz aller Speicherprotokolle
- VMware vSphere nutzt Shared Storage fuer vMotion und HA → alle Hosts muessen auf den gleichen Speicher zugreifen, was nur mit SAN effizient moeglich ist
- Redundanz: Zwei FC-Switches (Fabric A und B) mit je zwei HBA-Ports pro Host fuer Ausfallsicherheit (Multipath)
- LUNs: Separate LUNs fuer Datenbank-VMs (auf schnellen SSDs) und Anwendungs-VMs (auf HDDs/Hybrid)
