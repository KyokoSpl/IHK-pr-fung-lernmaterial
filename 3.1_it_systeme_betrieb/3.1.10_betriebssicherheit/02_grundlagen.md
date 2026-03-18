# Grundlagen: 3.1.10 – Massnahmen zur Sicherstellung des Betriebes

## Elektrotechnisch: Unterbrechungsfreie Stromversorgung (USV)

**Definition:** Eine USV ist ein Geraet, das bei Stromausfall sofort die Stromversorgung uebernimmt und IT-Systeme vor Spannungsstoerungen schuetzt. Sie ermoeglicht ein kontrolliertes Herunterfahren oder ueberbrueckt den Ausfall bis ein Generator anlaeuft.

**Die drei USV-Klassen (nach IEC 62040-3):**

| Eigenschaft | VFD (Offline/Standby) | VI (Line-Interactive) | VFI (Online/Double-Conversion) |
|---|---|---|---|
| **Bezeichnung** | Voltage and Frequency Dependent | Voltage Independent | Voltage and Frequency Independent |
| **Umschaltzeit** | 2–10 ms | 2–4 ms | 0 ms (unterbrechungsfrei) |
| **Spannungsregelung** | Nein | Ja (AVR) | Ja (permanent) |
| **Frequenzregelung** | Nein | Nein | Ja |
| **Wirkungsgrad** | ca. 95–98 % | ca. 95–97 % | ca. 90–94 % |
| **Kosten** | Niedrig | Mittel | Hoch |
| **Einsatz** | Arbeitsplatz-PCs | Netzwerkgeraete, kleine Server | Serverschraenke, Rechenzentren |

```
VFD (Offline):
  Netz ---[Umschalter]---> Verbraucher
              |
           [Akku] ---> bei Ausfall

VI (Line-Interactive):
  Netz ---[AVR + Umschalter]---> Verbraucher
                |
             [Akku] ---> bei Ausfall

VFI (Online):
  Netz ---> [Gleichrichter] ---> [Akku] ---> [Wechselrichter] ---> Verbraucher
            (AC → DC)                        (DC → AC)
  → Verbraucher laeuft IMMER ueber den Wechselrichter
  → 0 ms Umschaltzeit, vollstaendige Entkopplung vom Netz
```

**Wichtige Begriffe:**
- **AVR (Automatic Voltage Regulation)** – automatische Spannungsanpassung bei Schwankungen
- **VA (Voltampere)** – Scheinleistung der USV
- **Watt** – Wirkleistung (typisch ca. 60–70 % der VA-Angabe)
- **Autonomiezeit** – Zeit, die die USV den Betrieb aufrechterhalten kann (abhaengig von Last und Akkukapazitaet)

---

## Hardwaretechnisch: RAID (Redundant Array of Independent Disks)

**Definition:** RAID ist ein Verfahren, bei dem mehrere Festplatten zu einem logischen Laufwerk zusammengefasst werden, um Ausfallsicherheit (Redundanz) und/oder Leistung zu steigern.

**RAID-Level im Ueberblick:**

| RAID | Mindest-Platten | Redundanz | Nutzbare Kapazitaet | Geschwindigkeit | Ausfall toleriert |
|---|---|---|---|---|---|
| RAID 0 | 2 | Keine | n * Plattengroesse | Sehr hoch (Striping) | 0 Platten |
| RAID 1 | 2 | Spiegelung | 1 * Plattengroesse | Lesen: hoch, Schreiben: normal | 1 Platte |
| RAID 5 | 3 | Paritaet (verteilt) | (n-1) * Plattengroesse | Lesen: hoch, Schreiben: mittel | 1 Platte |
| RAID 6 | 4 | Doppelte Paritaet | (n-2) * Plattengroesse | Lesen: hoch, Schreiben: langsamer | 2 Platten |
| RAID 10 | 4 | Spiegelung + Striping | n/2 * Plattengroesse | Sehr hoch | 1 pro Spiegel |

### Kapazitaetsberechnung:

```
RAID 0:  Kapazitaet = n * s          (n = Anzahl Platten, s = Groesse einer Platte)
RAID 1:  Kapazitaet = s              (nur die Haelfte nutzbar)
RAID 5:  Kapazitaet = (n - 1) * s
RAID 6:  Kapazitaet = (n - 2) * s
RAID 10: Kapazitaet = (n / 2) * s
```

### RAID-Level im Detail

**RAID 0 (Striping):**
- Daten werden auf alle Platten verteilt (gestreift)
- Maximale Geschwindigkeit, keine Redundanz
- Ausfall einer Platte = vollstaendiger Datenverlust
- Einsatz: Temporaere Daten, Video-Rendering

**RAID 1 (Mirroring):**
- Daten werden auf zwei Platten gespiegelt
- Volle Redundanz, aber nur 50 % der Kapazitaet nutzbar
- Einsatz: Betriebssystem-Laufwerke, kleine Server

**RAID 5 (Striping mit verteilter Paritaet):**
- Daten und Paritaetsinformationen werden auf alle Platten verteilt
- Eine Platte darf ausfallen, Daten werden aus Paritaet rekonstruiert
- Einsatz: Fileserver, NAS-Systeme

**RAID 6 (wie RAID 5, doppelte Paritaet):**
- Zwei Platten koennen gleichzeitig ausfallen
- Einsatz: Grosse Arrays, wo Rebuild-Zeiten lang sind

**RAID 10 (RAID 1+0):**
- Kombination: Erst spiegeln (RAID 1), dann stripen (RAID 0)
- Hohe Geschwindigkeit und Redundanz
- Einsatz: Datenbankserver, geschaeftskritische Anwendungen

```
RAID 5 mit 4 Platten:

  Platte 1    Platte 2    Platte 3    Platte 4
  +--------+  +--------+  +--------+  +--------+
  | Daten  |  | Daten  |  | Daten  |  |Paritaet|  ← Paritaet
  | Block1 |  | Block2 |  | Block3 |  |  P1    |    rotiert
  +--------+  +--------+  +--------+  +--------+    ueber alle
  | Daten  |  | Daten  |  |Paritaet|  | Daten  |    Platten
  | Block4 |  | Block5 |  |  P2    |  | Block6 |
  +--------+  +--------+  +--------+  +--------+
  | Daten  |  |Paritaet|  | Daten  |  | Daten  |
  | Block7 |  |  P3    |  | Block8 |  | Block9 |
  +--------+  +--------+  +--------+  +--------+

  Nutzbare Kapazitaet: (4-1) * s = 3 * s
```

**Wichtige Begriffe:**
- **Striping** – Daten werden in Bloecke aufgeteilt und auf mehrere Platten verteilt
- **Mirroring** – Daten werden 1:1 auf eine zweite Platte kopiert
- **Paritaet** – Pruefsumme, aus der fehlende Daten rekonstruiert werden koennen
- **Rebuild** – Wiederherstellung der Daten auf einer Ersatzplatte nach einem Ausfall
- **Hot Spare** – Ersatzfestplatte, die automatisch bei einem Ausfall einspringt

---

## Softwaretechnisch: Backups

**Definition:** Ein Backup ist eine Sicherungskopie von Daten, die im Falle eines Datenverlusts zur Wiederherstellung verwendet werden kann.

**Backup-Typen im Vergleich:**

| Typ | Beschreibung | Speicherbedarf | Backup-Dauer | Restore-Dauer |
|---|---|---|---|---|
| Vollbackup | Alle Daten werden gesichert | Hoch | Lang | Schnell (1 Backup) |
| Inkrementelles Backup | Nur Aenderungen seit dem letzten Backup (egal welcher Typ) | Niedrig | Kurz | Lang (Voll + alle Inkremente) |
| Differenzielles Backup | Nur Aenderungen seit dem letzten Vollbackup | Mittel (wachsend) | Mittel | Mittel (Voll + letztes Diff.) |

```
Woche: Mo(Voll)  Di        Mi        Do        Fr

Inkrementell:
  Mo: [Voll]
  Di: [Aend. seit Mo]
  Mi: [Aend. seit Di]         ← nur seit letztem Backup
  Do: [Aend. seit Mi]
  Fr: [Aend. seit Do]
  Restore Fr: Mo + Di + Mi + Do + Fr (alle noetig!)

Differenziell:
  Mo: [Voll]
  Di: [Aend. seit Mo]
  Mi: [Aend. seit Mo]         ← immer seit Vollbackup
  Do: [Aend. seit Mo]
  Fr: [Aend. seit Mo]
  Restore Fr: Mo + Fr (nur Voll + letztes Diff.)
```

### 3-2-1-Regel

```
  3 Kopien der Daten (Original + 2 Sicherungen)
  2 verschiedene Medientypen (z.B. Festplatte + Band/Cloud)
  1 Kopie an einem externen Standort (Offsite)
```

| Regel | Erklaerung | Beispiel |
|---|---|---|
| 3 Kopien | Original + 2 Backups | Daten auf Server + NAS + Cloud |
| 2 Medien | Unterschiedliche Speichermedien | Festplatte + LTO-Band |
| 1 Offsite | Mindestens eine Kopie raeumlich getrennt | Cloud-Backup oder Bandlagerung in anderem Gebaeude |

**Weitere Backup-Konzepte:**

| Konzept | Beschreibung |
|---|---|
| Generationenprinzip (GVS) | Grossvater-Vater-Sohn: Tages-, Wochen- und Monatsbackups |
| Snapshot | Momentaufnahme eines Dateisystems (z.B. ZFS, VMware) |
| Image-Backup | Sicherung eines gesamten Laufwerks oder einer VM |
| Cold Backup | Backup bei heruntergefahrenem System (konsistenter Zustand) |
| Hot Backup | Backup im laufenden Betrieb (erfordert spezielle Software) |

**Wichtige Begriffe:**
- **Retention (Aufbewahrungsfrist)** – Wie lange werden Backups aufbewahrt?
- **RPO** – Maximaler Datenverlust bestimmt das Backup-Intervall (→ Thema 3.1.09)
- **Restore-Test** – Regelmaessige Pruefung, ob Backups tatsaechlich wiederherstellbar sind
- **Archiv-Bit** – Dateiattribut, das anzeigt, ob eine Datei seit dem letzten Backup geaendert wurde
