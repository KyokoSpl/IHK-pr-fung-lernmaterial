# Vertiefung und Uebungen: 3.1.10 – Massnahmen zur Sicherstellung des Betriebes

## Vertiefung

### USV-Typen im Vergleich – Entscheidungshilfe

| Kriterium | VFD (Offline) | VI (Line-Interactive) | VFI (Online) |
|---|---|---|---|
| Schutz vor Stromausfall | Ja (mit Umschaltzeit) | Ja (mit kurzer Umschaltzeit) | Ja (unterbrechungsfrei) |
| Schutz vor Ueberspannung | Begrenzt | Ja (AVR) | Ja (vollstaendig) |
| Schutz vor Frequenzschwankung | Nein | Nein | Ja |
| Schutz vor Spannungsschwankung | Nein | Ja (AVR) | Ja |
| Empfehlung | Arbeitsplatz-PC | Switch, kleiner Server | Serverraum, Rechenzentrum |

### RAID-Level – Kapazitaetsberechnung mit Zahlen

**Beispiel: 6 Festplatten mit je 2 TB**

| RAID | Berechnung | Nutzbare Kapazitaet | Redundanz |
|---|---|---|---|
| RAID 0 | 6 * 2 TB | 12 TB | Keine |
| RAID 1 | 1 * 2 TB | 2 TB | 1 Platte (Spiegel) |
| RAID 5 | (6-1) * 2 TB | 10 TB | 1 Platte |
| RAID 6 | (6-2) * 2 TB | 8 TB | 2 Platten |
| RAID 10 | (6/2) * 2 TB | 6 TB | 1 je Spiegel |

### RAID – Haeufige Pruefungsfragen

| Frage | Antwort |
|---|---|
| Welcher RAID-Level bietet keine Redundanz? | RAID 0 |
| Welcher RAID-Level hat die beste Schreibperformance + Redundanz? | RAID 10 |
| Wie viele Platten duerfen bei RAID 5 ausfallen? | Genau 1 |
| Was ist ein Hot Spare? | Ersatzplatte, die automatisch bei Ausfall einspringt |
| Ist RAID ein Ersatz fuer Backups? | **Nein!** RAID schuetzt vor Hardwareausfall, nicht vor versehentlichem Loeschen, Malware oder logischen Fehlern |

### Backup-Typen – Detailvergleich mit Beispiel

**Szenario:** 100 GB Daten am Montag. Taeglich aendern sich 10 GB.

| Tag | Vollbackup | Inkrementell | Differenziell |
|---|---|---|---|
| Mo (Voll) | 100 GB | 100 GB | 100 GB |
| Di | 100 GB | 10 GB | 10 GB |
| Mi | 100 GB | 10 GB | 20 GB |
| Do | 100 GB | 10 GB | 30 GB |
| Fr | 100 GB | 10 GB | 40 GB |
| **Gesamt** | **500 GB** | **140 GB** | **200 GB** |
| **Restore Fr** | 1 Backup | 5 Backups | 2 Backups |

### Zusammenspiel der Massnahmen

```
               Risiko                    Massnahme
  +----------------------------+   +----------------------------+
  | Stromausfall               | → | USV (VFI fuer Server)      |
  +----------------------------+   +----------------------------+
  | Festplattendefekt          | → | RAID (5, 6 oder 10)        |
  +----------------------------+   +----------------------------+
  | Datenverlust (Loeschen,    | → | Backup (3-2-1-Regel)       |
  |  Ransomware, Fehler)       |   |                            |
  +----------------------------+   +----------------------------+
  | Kompletter Serverausfall   | → | Redundanter Server/Cluster |
  +----------------------------+   +----------------------------+
  | Standortausfall (Brand)    | → | Offsite-Backup / Hot Site  |
  +----------------------------+   +----------------------------+
```

### Typische Pruefungsaspekte
- USV-Typ fuer ein Szenario empfehlen und begruenden
- RAID-Level auswahlen und Kapazitaet berechnen
- Backup-Strategie fuer ein Unternehmen planen (Typ, Intervall, Medium)
- 3-2-1-Regel erklaeren und anwenden
- Unterschied RAID vs. Backup erklaeren

### Haeufige Fehler
- RAID als Backup-Ersatz betrachten → RAID schuetzt nur vor Plattenausfall
- VFD und VFI verwechseln → VFD = einfachste USV, VFI = beste USV
- Inkrementell und Differenziell verwechseln → Inkrementell: seit letztem Backup (egal welcher Typ); Differenziell: seit letztem Vollbackup
- Restore-Aufwand nicht beruecksichtigen → Inkrementell spart Speicher, braucht aber alle Teile fuer Restore

---

## Uebungen

**Aufgabe 1:** Ein Serverraum soll eine USV erhalten. Die Server duerfen keine Unterbrechung der Stromversorgung erleben, auch nicht fuer Millisekunden. Welchen USV-Typ empfiehlst du? Begruende.

**Aufgabe 2:** Ein Unternehmen baut einen Fileserver mit 8 Festplatten zu je 4 TB auf. Berechne die nutzbare Kapazitaet fuer RAID 5, RAID 6 und RAID 10.

**Aufgabe 3:** Ein Server mit RAID 5 aus 5 Festplatten (je 1 TB) hat einen Plattenausfall. Waehrend des Rebuilds faellt eine zweite Platte aus. Was passiert?

**Aufgabe 4:** Erklaere den Unterschied zwischen inkrementellem und differenziellem Backup. Ein Unternehmen macht am Sonntag ein Vollbackup. Am Mittwoch faellt der Server aus. Welche Backups werden fuer den Restore benoetigt bei:
- a) Inkrementeller Strategie
- b) Differenzieller Strategie

**Aufgabe 5:** Ein Unternehmen hat folgende Backup-Strategie: Woechentliches Vollbackup (Freitag Nacht), taegliches differenzielles Backup (Mo–Do). Der Server faellt am Donnerstag um 14 Uhr aus.
- a) Welche Backups werden fuer den Restore benoetigt?
- b) Wie viele Stunden Daten gehen maximal verloren (RPO)?

**Aufgabe 6:** Erklaere die 3-2-1-Backup-Regel. Ein kleines Unternehmen hat bisher nur ein taegliches Backup auf einer externen USB-Festplatte neben dem Server. Was fehlt?

**Aufgabe 7:** Warum ist RAID kein Ersatz fuer ein Backup? Nenne drei Szenarien, in denen RAID nicht schuetzt.

**Aufgabe 8:** Ordne die folgenden Massnahmen der richtigen Kategorie zu (elektrotechnisch, hardwaretechnisch, softwaretechnisch):
- a) LTO-Bandsicherung
- b) VFI-USV im Serverraum
- c) RAID-10-Konfiguration
- d) Generationenbackup (GVS)
- e) Redundantes Netzteil im Server
- f) Blitzschutzanlage

---
---

# Loesungen

## Aufgabe 1
**VFI (Online/Double-Conversion).** Begruendung: Nur VFI hat 0 ms Umschaltzeit, da der Verbraucher permanent ueber den Wechselrichter versorgt wird. VFD (2–10 ms) und VI (2–4 ms) haben Umschaltzeiten, die empfindliche Server stoeren koennen.

## Aufgabe 2
```
RAID 5:  (8-1) * 4 TB = 7 * 4 TB = 28 TB
RAID 6:  (8-2) * 4 TB = 6 * 4 TB = 24 TB
RAID 10: (8/2) * 4 TB = 4 * 4 TB = 16 TB
```

## Aufgabe 3
Bei RAID 5 darf nur **eine** Platte ausfallen. Faellt waehrend des Rebuilds eine zweite Platte aus, sind **alle Daten verloren** (Totalverlust). Deshalb wird fuer grosse Arrays RAID 6 empfohlen (toleriert 2 Ausfaelle) oder ein **Hot Spare** eingesetzt, der den Rebuild sofort startet.

## Aufgabe 4
- **Inkrementell:** Sonntag (Voll) + Montag (Inkr.) + Dienstag (Inkr.) + Mittwoch (Inkr.) = 4 Backups noetig.
- **Differenziell:** Sonntag (Voll) + Mittwoch (Diff.) = 2 Backups noetig.
- **Unterschied:** Inkrementell sichert nur Aenderungen seit dem letzten Backup (egal welcher Typ). Differenziell sichert alle Aenderungen seit dem letzten Vollbackup.

## Aufgabe 5
a) Restore: **Freitag-Vollbackup + Mittwoch-Differenzielles Backup** (letztes Diff. vor dem Ausfall).
b) Das letzte Backup war Mittwoch Nacht. Ausfall war Donnerstag 14 Uhr → **maximal ca. 14 Stunden Datenverlust** (RPO = 14 h). Daten von Donnerstag 00:00 bis 14:00 sind verloren.

## Aufgabe 6
Die 3-2-1-Regel: **3** Kopien, **2** verschiedene Medien, **1** Offsite.
- **Fehlt:** Nur 1 Backup-Kopie (statt 2) → zweites Backup noetig. Nur 1 Medientyp (USB-Festplatte) → zweites Medium (z.B. Cloud oder Band). Kein Offsite → USB-Festplatte steht neben dem Server, bei Brand sind Original und Backup betroffen. Loesung: Zusaetzliches Cloud-Backup oder Bandlagerung an externem Standort.

## Aufgabe 7
RAID ist kein Backup, weil:
1. **Versehentliches Loeschen:** RAID spiegelt das Loeschen sofort auf alle Platten.
2. **Ransomware:** Verschluesselte Daten werden auf alle RAID-Platten geschrieben.
3. **Controller-Defekt:** Ein defekter RAID-Controller kann das gesamte Array unlesbar machen.

Weitere Szenarien: Softwarefehler (korrupte Datenbank), Diebstahl des Servers, Brandschaden.

## Aufgabe 8
- a) LTO-Bandsicherung → **softwaretechnisch** (Backup-Strategie)
- b) VFI-USV → **elektrotechnisch**
- c) RAID-10 → **hardwaretechnisch**
- d) GVS → **softwaretechnisch** (Backup-Konzept)
- e) Redundantes Netzteil → **hardwaretechnisch**
- f) Blitzschutzanlage → **elektrotechnisch**
