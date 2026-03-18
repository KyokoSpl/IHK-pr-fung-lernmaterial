# Vertiefung: 3.2.06 – Netzwerkkomponenten und -protokolle beschreiben

## NAS vs. SAN – Detaillierter Vergleich

| Kriterium | NAS | SAN |
|-----------|-----|-----|
| Speicherebene | File-Level (Dateien/Ordner) | Block-Level (Bloecke/Sektoren) |
| Netzwerk | Bestehendes LAN (Ethernet) | Dediziertes Netzwerk (FC oder iSCSI) |
| Protokoll | SMB, NFS | Fibre Channel, iSCSI |
| Performance | Gut (abhaengig vom LAN) | Sehr hoch (dediziert, niedrige Latenz) |
| Kosten | Gering bis mittel | Hoch (eigenes Netz, FC-Hardware) |
| Komplexitaet | Gering (Plug & Play) | Hoch (eigene Infrastruktur, Zoning) |
| Eignung | Dateifreigaben, Backup, KMU | Datenbanken, Virtualisierung, Grossunternehmen |
| Dateisystem | NAS verwaltet das Dateisystem | Server verwaltet das Dateisystem auf der LUN |
| Skalierbarkeit | Begrenzt (einzelnes Geraet) | Hoch (Storage Arrays, Erweiterung moeglich) |

## Block-Level vs. File-Level Storage

```
FILE-LEVEL (NAS):                    BLOCK-LEVEL (SAN):

Client                               Client
  |                                     |
  v                                     v
[SMB/NFS-Anfrage]                    [SCSI/iSCSI-Befehl]
  |                                     |
  v                                     v
NAS-Dateisystem                      Server-Dateisystem
(NAS verwaltet)                      (Server verwaltet)
  |                                     |
  v                                     v
Festplatten im NAS                   LUN im Storage Array
```

**Erklaerung:** Bei NAS fragt der Client nach einer Datei ("Gib mir /daten/bericht.pdf"). Das NAS verwaltet das Dateisystem. Bei SAN bekommt der Server einen Block-Speicher praesentiert und erstellt darauf sein eigenes Dateisystem – wie bei einer lokalen Festplatte.

---

## Fibre Channel vs. iSCSI

| Kriterium | Fibre Channel | iSCSI |
|-----------|-------------|-------|
| Netzwerk | Eigenes FC-Netzwerk | Bestehendes Ethernet |
| Geschwindigkeit | 8/16/32 Gbit/s | 1/10/25/100 Gbit/s (Ethernet) |
| Latenz | Sehr niedrig | Niedrig (hoeher als FC) |
| Hardware | FC-Switches, HBA (teuer) | Standard-Ethernet-Switches, NIC (guenstig) |
| Kosten | Hoch | Gering bis mittel |
| Komplexitaet | Hoch (eigenes Netzwerk, Zoning) | Mittel (nutzt bestehendes Netz) |
| Zuverlaessigkeit | Verlustfreies Protokoll | Abhaengig von Netzwerkkonfiguration |
| Eignung | Hochleistungs-SANs, Rechenzentren | KMU, Budget-SANs, Virtualisierung |

---

## SMB vs. NFS

| Kriterium | SMB | NFS |
|-----------|-----|-----|
| Herkunft | Microsoft | Sun Microsystems (Unix/Linux) |
| Betriebssystem | Windows (primaer), Linux (Samba) | Linux/Unix (primaer), Windows (Services for NFS) |
| Port | TCP 445 | TCP 2049 (NFSv4) |
| Authentifizierung | Active Directory, NTLM | Kerberos (NFSv4), Host-basiert (NFSv3) |
| Verschluesselung | SMB3: Ja (nativ) | NFSv4: ueber Kerberos |
| Typischer Einsatz | Windows-Dateifreigaben, Drucker | Linux-Dateifreigaben, NAS-Systeme |

---

## Speicherprotokolle im OSI-Modell

```
OSI-Schicht:    Ethernet        FC              iSCSI           SMB/NFS
+-----------+
| 7 Anwend. |                                                   SMB, NFS
| 6 Darstl. |
| 5 Sitzung |                                   iSCSI
| 4 Transp. |                                   TCP
| 3 Vermittl|                   FC-3            IP
| 2 Sicher. |   Ethernet       FC-2
| 1 Bituebert|  Ethernet       FC-0/FC-1
+-----------+
```

---

## Ethernet-Varianten fuer Speichernetzwerke

| Technologie | Geschwindigkeit | Einsatz |
|-------------|----------------|---------|
| 1 GbE | 1 Gbit/s | NAS, kleines iSCSI |
| 10 GbE | 10 Gbit/s | iSCSI-SAN, leistungsfaehiges NAS |
| 25 GbE | 25 Gbit/s | Moderne Server, iSCSI-SAN |
| 40/100 GbE | 40/100 Gbit/s | Backbone, Hochleistungs-Storage |

### Jumbo Frames im Speichernetzwerk
- Standard-MTU: 1500 Byte → Standard-Ethernet
- Jumbo Frames: MTU bis 9000 Byte
- Reduziert CPU-Last und Overhead bei grossen Datenuebertragungen
- Alle Geraete im Pfad muessen Jumbo Frames unterstuetzen
- Besonders wichtig fuer iSCSI-Netzwerke

---

## Typische Pruefungsaspekte
- NAS vs. SAN unterscheiden (File-Level vs. Block-Level)
- Fibre Channel vs. iSCSI vergleichen
- SMB vs. NFS: Wann wird welches Protokoll eingesetzt?
- Ethernet-Frame-Aufbau beschreiben
- Begriffe: LUN, HBA, WWPN, IQN erklaeren
- Speicherprotokoll fuer ein Szenario empfehlen

## Haeufige Fehler
- NAS und SAN verwechseln: NAS = dateibasiert ueber LAN, SAN = blockbasiert ueber dediziertes Netz
- iSCSI ist KEIN Fibre Channel ueber Ethernet – es ist SCSI ueber TCP/IP
- SMB 1.0 als aktuell bezeichnen → SMB 1.0 ist veraltet und ein Sicherheitsrisiko (WannaCry nutzte SMB1)
- Vergessen, dass bei SAN der SERVER das Dateisystem verwaltet, nicht das Storage Array
- Fibre Channel wird faelschlicherweise nur mit Glasfaser assoziiert → FC kann auch ueber Kupfer laufen
