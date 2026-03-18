# Grundlagen: 3.2.06 – Netzwerkkomponenten und -protokolle beschreiben

## 1. Ethernet

**Definition:** Ethernet ist die am weitesten verbreitete kabelgebundene Netzwerktechnologie fuer lokale Netzwerke (LAN). Es arbeitet auf OSI-Schicht 1 (Bitueberetragung) und Schicht 2 (Sicherungsschicht) und definiert den Zugriff auf das Uebertragungsmedium sowie den Rahmenaufbau.

**Ethernet-Standards und Geschwindigkeiten:**

| Standard | Bezeichnung | Geschwindigkeit | Medium | Max. Laenge |
|----------|------------|----------------|--------|-------------|
| 10BASE-T | Ethernet | 10 Mbit/s | Kupfer (Cat3+) | 100 m |
| 100BASE-TX | Fast Ethernet | 100 Mbit/s | Kupfer (Cat5+) | 100 m |
| 1000BASE-T | Gigabit Ethernet | 1 Gbit/s | Kupfer (Cat5e/Cat6) | 100 m |
| 10GBASE-T | 10-Gigabit Ethernet | 10 Gbit/s | Kupfer (Cat6a/Cat7) | 100 m |
| 1000BASE-SX | Gigabit Ethernet | 1 Gbit/s | Multimode-Glasfaser | 550 m |
| 10GBASE-SR | 10-Gigabit Ethernet | 10 Gbit/s | Multimode-Glasfaser | 300 m |
| 10GBASE-LR | 10-Gigabit Ethernet | 10 Gbit/s | Singlemode-Glasfaser | 10 km |

**Ethernet-Frame (vereinfacht):**

```
+----------+----------+------+------+---------+-----+
| Praeambel| Ziel-MAC | Src- | Type | Nutzdaten| FCS |
| 8 Byte   | 6 Byte   | MAC  | 2 B  | 46-1500 | 4 B |
|          |          | 6 B  |      | Byte    |     |
+----------+----------+------+------+---------+-----+
```

| Feld | Beschreibung |
|------|-------------|
| Praeambel | Synchronisation (inkl. Start Frame Delimiter) |
| Ziel-MAC | MAC-Adresse des Empfaengers |
| Quell-MAC (Src-MAC) | MAC-Adresse des Senders |
| Type/Length | Protokolltyp (z.B. 0x0800 = IPv4) oder Laenge |
| Nutzdaten (Payload) | Die eigentlichen Daten (46–1500 Byte) |
| FCS (Frame Check Sequence) | Pruefsumme zur Fehlererkennung (CRC) |

**Wichtige Begriffe:**
- **MAC-Adresse** – 48-Bit-Hardwareadresse (z.B. AA:BB:CC:DD:EE:FF)
- **MTU (Maximum Transmission Unit)** – maximale Nutzdatengroesse (Standard: 1500 Byte)
- **Jumbo Frame** – Ethernet-Frame mit erhoehter MTU (bis 9000 Byte), reduziert Overhead
- **CSMA/CD** – Zugriffsverfahren bei klassischem Ethernet (veraltet bei Vollduplex/Switches)

---

## 2. Fibre Channel (FC)

**Definition:** Fibre Channel ist eine Hochgeschwindigkeits-Netzwerktechnologie, die primaer fuer SAN-Umgebungen eingesetzt wird. Sie bietet dedizierte, verlustfreie Datenuebertragung mit sehr geringer Latenz.

**Fibre Channel Geschwindigkeiten:**

| Generation | Geschwindigkeit | Bezeichnung |
|-----------|----------------|-------------|
| 1 GFC | 1 Gbit/s | 1G Fibre Channel |
| 2 GFC | 2 Gbit/s | 2G Fibre Channel |
| 4 GFC | 4 Gbit/s | 4G Fibre Channel |
| 8 GFC | 8 Gbit/s | 8G Fibre Channel |
| 16 GFC | 16 Gbit/s | 16G Fibre Channel |
| 32 GFC | 32 Gbit/s | 32G Fibre Channel |

**FC-Topologien:**

| Topologie | Beschreibung | Einsatz |
|-----------|-------------|---------|
| Point-to-Point | Direkte Verbindung zwischen zwei Geraeten | Einfache Setups |
| Arbitrated Loop (FC-AL) | Ringfoermige Verbindung, geteilte Bandbreite | Aeltere Systeme |
| Switched Fabric | Sternfoermig ueber FC-Switches, volle Bandbreite | Standard in modernen SANs |

**Wichtige Begriffe:**
- **FC-Switch** – verbindet FC-Geraete in einer Switched-Fabric-Topologie
- **HBA (Host Bus Adapter)** – Netzwerkkarte fuer Fibre Channel (Gegenstueck zur NIC)
- **WWPN (World Wide Port Name)** – eindeutige Kennung eines FC-Ports (wie MAC-Adresse bei Ethernet)
- **Zoning** – Zugriffskontrolle im FC-SAN, legt fest, welche Geraete miteinander kommunizieren duerfen

---

## 3. NAS (Network Attached Storage)

**Definition:** Ein NAS ist ein Speichergeraet, das ueber das bestehende Netzwerk (LAN/Ethernet) dateibasiert Speicherplatz bereitstellt. Es arbeitet auf Dateiebene (File-Level) und wird ueber Protokolle wie SMB oder NFS angesprochen.

**Kernaussagen:**
- NAS ist ein eigenstaendiges Geraet mit eigenem Betriebssystem (z.B. Synology DSM, QNAP QTS, TrueNAS)
- Zugriff ueber Standard-Netzwerkprotokolle (SMB, NFS, FTP, HTTP)
- Einfache Einrichtung und Verwaltung (Weboberflaeche)
- Eignet sich fuer gemeinsame Dateiablage, Backup, Medienstreaming

**NAS-Architektur:**

```
[Client A] ---|
[Client B] ---+--- [Ethernet-Switch] --- [NAS-Geraet]
[Client C] ---|                          (Dateifreigaben)
```

**Wichtige Begriffe:**
- **File-Level Storage** – Zugriff auf Dateiebene (Dateien und Ordner)
- **RAID** – Redundante Festplattenanordnung im NAS (z.B. RAID 1, RAID 5)
- **SMB/NFS** – Protokolle fuer den Dateizugriff auf dem NAS

---

## 4. NFS (Network File System)

**Definition:** NFS ist ein Netzwerkprotokoll fuer die Freigabe von Dateien und Verzeichnissen in Unix/Linux-Umgebungen. Es ermoeglicht das Einbinden (Mounten) entfernter Verzeichnisse als waeren sie lokal.

**Kernaussagen:**
- Entwickelt von Sun Microsystems
- Aktuelle Version: NFSv4 (mit verbesserter Sicherheit und Firewall-Freundlichkeit)
- Typisch fuer Linux/Unix-Umgebungen und gemischte Netzwerke
- Zugriff ueber TCP (Port 2049 bei NFSv4)
- Authentifizierung ueber Kerberos moeglich (NFSv4)

**NFS-Versionen:**

| Version | Merkmal |
|---------|---------|
| NFSv3 | Zustandsloses Protokoll, mehrere Ports, keine native Verschluesselung |
| NFSv4 | Zustandsbehaftet, einzelner Port (2049), Kerberos-Authentifizierung, ACL-Unterstuetzung |

**Wichtige Begriffe:**
- **Mount** – Einbinden eines NFS-Exports in das lokale Dateisystem
- **Export** – ein freigegebenes Verzeichnis auf dem NFS-Server
- **Kerberos** – Authentifizierungsprotokoll fuer sichere NFS-Verbindungen

---

## 5. SAN (Storage Area Network)

**Definition:** Ein SAN ist ein dediziertes Netzwerk, das Server mit Speichersystemen verbindet. Es arbeitet auf Blockebene (Block-Level) und stellt Speicher so bereit, als waere es eine lokal angeschlossene Festplatte.

**Kernaussagen:**
- Eigenes, separates Netzwerk (nicht ueber das LAN)
- Blockbasierter Zugriff (Betriebssystem sieht ein lokales Laufwerk)
- Hohe Performance und niedrige Latenz
- Protokolle: Fibre Channel (FC) oder iSCSI
- Typisch fuer Datenbanken, Virtualisierung, grosse Speichersysteme

**SAN-Architektur:**

```
[Server 1] ---(HBA)---+
                       |--- [FC-Switch] --- [Storage Array]
[Server 2] ---(HBA)---+                    (LUNs / Volumes)
                       |
[Server 3] ---(HBA)---+
```

**Wichtige Begriffe:**
- **Block-Level Storage** – Zugriff auf Blockebene (Sektoren, Bloecke), kein Dateisystem auf Speicherseite
- **LUN (Logical Unit Number)** – logische Speichereinheit im SAN, vom Server als Festplatte gesehen
- **Storage Array** – zentrales Speichersystem mit vielen Festplatten (z.B. NetApp, Dell EMC)
- **Fabric** – das Netzwerk aus FC-Switches, das Server und Storage verbindet

---

## 6. SMB (Server Message Block)

**Definition:** SMB (Server Message Block) ist ein Netzwerkprotokoll fuer die Freigabe von Dateien, Druckern und anderen Ressourcen in Windows-Netzwerken. Die aktuelle Version heisst SMB3.

**Kernaussagen:**
- Standard-Protokoll fuer Dateifreigaben in Windows-Umgebungen
- Auch bekannt als CIFS (Common Internet File System, aeltere Bezeichnung)
- SMB3 unterstuetzt Verschluesselung, Multichannel und verbesserte Performance
- Zugriff ueber TCP Port 445
- Auch unter Linux nutzbar (ueber Samba-Server)

**SMB-Versionen:**

| Version | Eingefuehrt mit | Neuerungen |
|---------|----------------|-----------|
| SMB 1.0 | Windows 2000 | Grundfunktionen (veraltet, unsicher!) |
| SMB 2.0 | Windows Vista | Verbesserte Performance, weniger Befehle |
| SMB 2.1 | Windows 7 | Leasing-Mechanismus, Energiesparen |
| SMB 3.0 | Windows 8 / Server 2012 | Verschluesselung, Multichannel, SMB Direct |
| SMB 3.1.1 | Windows 10 / Server 2016 | Preauthentication Integrity, AES-128-GCM |

**Wichtige Begriffe:**
- **CIFS** – aelterer Name fuer SMB (Common Internet File System)
- **Samba** – Open-Source-Implementierung von SMB fuer Linux/Unix
- **SMB Direct** – RDMA-basierter Datentransfer fuer hohe Performance (z.B. in Hyper-V)
- **Multichannel** – Nutzung mehrerer Netzwerkverbindungen gleichzeitig

---

## 7. iSCSI (Internet Small Computer Systems Interface)

**Definition:** iSCSI ist ein Protokoll, das SCSI-Befehle ueber TCP/IP-Netzwerke (Ethernet) uebertraegt. Es ermoeglicht blockbasierten Speicherzugriff ueber das bestehende Ethernet-Netzwerk – als guenstigere Alternative zu Fibre Channel.

**Kernaussagen:**
- Uebertraegt SCSI-Befehle in TCP/IP-Paketen
- Nutzt Standard-Ethernet-Infrastruktur (1 GbE, 10 GbE, 25 GbE)
- Guenstigere Alternative zu Fibre Channel SAN
- Server sieht den iSCSI-Speicher als lokale Festplatte (wie bei FC-SAN)
- Port: TCP 3260

**iSCSI-Komponenten:**

| Komponente | Beschreibung |
|------------|-------------|
| **iSCSI Initiator** | Software oder Hardware auf dem Server, der den Speicher nutzt |
| **iSCSI Target** | Der Speicher, der die LUNs bereitstellt (Storage-System) |
| **LUN** | Logische Speichereinheit, die dem Server praesentiert wird |
| **IQN (iSCSI Qualified Name)** | Eindeutige Kennung fuer Initiator und Target |

**Wichtige Begriffe:**
- **SCSI** – Bussystem fuer den Datenaustausch mit Speichergeraeten
- **Initiator** – der Client, der auf den Speicher zugreift
- **Target** – der Server/das System, das Speicher bereitstellt
- **TOE (TCP Offload Engine)** – Hardwarebeschleunigung fuer iSCSI auf der Netzwerkkarte
