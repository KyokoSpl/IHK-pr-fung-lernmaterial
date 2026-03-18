# Beispiele: 3.2.06 – Netzwerkkomponenten und -protokolle beschreiben

## NAS vs. SAN – Praxisszenarien

**Beispiel 1 – NAS:** Ein kleines Architekturbüro mit 15 Mitarbeitern benoetigt einen zentralen Speicher fuer CAD-Zeichnungen und Projektdokumente. Alle Rechner sind ueber Gigabit-Ethernet verbunden. → **NAS** ist die richtige Wahl: Einfache Einrichtung, Zugriff ueber SMB (Windows) oder NFS (Linux), guenstig, RAID 5 fuer Ausfallsicherheit. Ein Synology- oder QNAP-NAS reicht aus.

**Beispiel 2 – SAN:** Ein Unternehmen betreibt eine VMware-vSphere-Umgebung mit 20 virtuellen Maschinen und einer Oracle-Datenbank. Hohe I/O-Performance und niedrige Latenz sind entscheidend. → **SAN** (Fibre Channel oder iSCSI): Blockbasierter Zugriff, dediziertes Netzwerk, Storage Array mit redundanten Controllern. Die VMs koennen per vMotion zwischen Hosts verschoben werden, da alle Hosts auf den gleichen SAN-Speicher zugreifen.

**Beispiel 3 – iSCSI statt FC:** Ein mittelstaendisches Unternehmen moechte ein SAN einrichten, hat aber kein Budget fuer eine separate Fibre-Channel-Infrastruktur. Die vorhandene 10-GbE-Ethernet-Infrastruktur soll genutzt werden. → **iSCSI-SAN**: Blockbasierter Zugriff ueber bestehendes 10-GbE-Netzwerk. Empfohlen: Jumbo Frames aktivieren, dediziertes VLAN fuer iSCSI-Traffic, TOE-Netzwerkkarten fuer CPU-Entlastung.

---

## Ethernet in der Praxis

**Beispiel 4 – Netzwerkplanung:** Ein Unternehmen plant die Verkabelung eines neuen Bueros. 50 Arbeitsplaetze, ein Serverraum mit 5 Servern, ein NAS und eine Internet-Anbindung.

| Bereich | Verkabelung | Geschwindigkeit |
|---------|-------------|----------------|
| Arbeitsplaetze → Switch | Cat6a (Kupfer) | 1 Gbit/s (1000BASE-T) |
| Server → Core-Switch | Cat6a oder Glasfaser | 10 Gbit/s (10GBASE-T oder 10GBASE-SR) |
| Switch → Switch (Uplink) | Glasfaser (Multimode) | 10 Gbit/s (10GBASE-SR) |
| NAS → Switch | Cat6a | 10 Gbit/s (10GBASE-T) |

**Beispiel 5 – Ethernet-Frame:** Ein Client (MAC: AA:BB:CC:11:22:33) sendet eine HTTP-Anfrage an einen Server (MAC: DD:EE:FF:44:55:66).

```
+----------+-------------------+-------------------+--------+----------+-----+
| Praeambel| Ziel-MAC          | Quell-MAC         | Type   | Payload  | FCS |
| 8 Byte   | DD:EE:FF:44:55:66 | AA:BB:CC:11:22:33 | 0x0800 | HTTP-    | CRC |
|          |                   |                   | (IPv4) | Daten    |     |
+----------+-------------------+-------------------+--------+----------+-----+
```

---

## SMB und NFS in der Praxis

**Beispiel 6 – SMB-Freigabe:** Ein Windows-Dateiserver stellt den Ordner "Projekte" fuer die Abteilung Entwicklung bereit:
- Freigabename: `\\fileserver\Projekte`
- Zugriff: Nur Mitglieder der AD-Gruppe "Entwicklung"
- Berechtigung: Lesen und Schreiben
- Protokoll: SMB3 mit Verschluesselung

**Beispiel 7 – NFS-Export:** Ein Linux-Server stellt `/srv/daten` fuer alle Server im Subnetz bereit:
- Export: `/srv/daten 192.168.1.0/24(rw,sync,no_subtree_check)`
- Client-Mount: `mount -t nfs server:/srv/daten /mnt/daten`
- Protokoll: NFSv4 mit Kerberos-Authentifizierung

**Beispiel 8 – Gemischte Umgebung:** Ein Unternehmen hat sowohl Windows- als auch Linux-Clients. Das NAS stellt Freigaben ueber beide Protokolle bereit:

| Protokoll | Clients | Freigabepfad |
|-----------|---------|-------------|
| SMB | Windows-PCs | `\\nas01\gemeinsam` |
| NFS | Linux-Server | `nas01:/volume1/gemeinsam` |

---

## SAN und Fibre Channel in der Praxis

**Beispiel 9 – FC-SAN Setup:** Ein Rechenzentrum betreibt ein Fibre-Channel-SAN:

```
[ESXi Host 1] ---(HBA)---+
                          |--- [FC-Switch A] ---+--- [Storage Array]
[ESXi Host 2] ---(HBA)---+                     |    (Dell EMC Unity)
                          |                     |
[ESXi Host 3] ---(HBA)---+--- [FC-Switch B] ---+    LUN 1: Datenbank
                                                     LUN 2: VMs
                                                     LUN 3: Backup
```

- Topologie: Switched Fabric (redundant ueber zwei FC-Switches)
- Geschwindigkeit: 32 GFC
- Zoning: Host 1 sieht nur LUN 1 und LUN 2, Host 3 sieht nur LUN 3

**Beispiel 10 – iSCSI-Konfiguration:**

| Komponente | Konfiguration |
|------------|--------------|
| iSCSI Target | Storage: TrueNAS, IQN: iqn.2024-01.com.firma:storage01 |
| iSCSI Initiator | Server: Windows Server, IQN: iqn.2024-01.com.firma:server01 |
| Netzwerk | 10 GbE, VLAN 100 (dediziert fuer iSCSI), Jumbo Frames (MTU 9000) |
| LUN | 500 GB, formatiert als NTFS durch den Server |
| Multipath | Zwei Netzwerkpfade fuer Redundanz und Load Balancing |
