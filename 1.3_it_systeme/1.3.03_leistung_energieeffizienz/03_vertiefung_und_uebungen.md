# Vertiefung und Uebungen: 1.3.03 – Leistungsfaehigkeit und Energieeffizienz

## Vertiefung

### Typische Pruefungsberechnungen

**Energiekosten:**
1. Leistung (W) × Betriebsstunden = Energie (Wh)
2. Wh / 1000 = kWh
3. kWh × Preis/kWh = Kosten

**Uebertragungszeit:**
1. Datengroesse in Bit umrechnen (Byte × 8)
2. Bit / Uebertragungsrate (bit/s) = Zeit in Sekunden

**Wirkungsgrad:**
- η = Nutzleistung / Zugefuehrte Leistung × 100
- Beispiel Netzteil: 400 W Nutzleistung, 500 W aus Steckdose → η = 80%

### HDD vs. SSD – Entscheidungshilfe

| Kriterium | HDD | SSD (SATA) | SSD (NVMe) |
|---|---|---|---|
| Lesen (seq.) | ~150 MB/s | ~550 MB/s | ~3.500 MB/s |
| Schreiben (seq.) | ~130 MB/s | ~520 MB/s | ~3.000 MB/s |
| Zugriffszeit | ~10 ms | ~0,1 ms | ~0,02 ms |
| Preis/GB | Guenstig | Mittel | Hoch |
| Einsatz | Archiv, Backup | Betriebssystem, Anwendungen | High-Performance |

### BIOS vs. UEFI

| Merkmal | BIOS | UEFI |
|---|---|---|
| Adressierung | 16-Bit | 32/64-Bit |
| Partitionstabelle | MBR (max. 2 TB) | GPT (max. 9,4 ZB) |
| Max. Partitionen | 4 primaer | 128 |
| Secure Boot | Nein | Ja |
| Oberflaeche | Textbasiert | Grafisch, Maus-Support |

### Typische Pruefungsaspekte
- Energiekostenberechnung fuer Server/Clients
- Uebertragungszeit fuer eine gegebene Dateigroesse und Bandbreite
- Vergleich HDD vs. SSD mit Begruendung
- BIOS/UEFI-Einstellungen benennen
- Dateisysteme dem Betriebssystem zuordnen

### Haeufige Fehler
- Bit und Byte verwechseln (Faktor 8!)
- Brutto- und Nettodatenrate nicht unterscheiden
- FAT32-Limit (4 GB) vergessen → Pruefungsklassiker
- Wirkungsgrad > 100% angeben (physikalisch unmoeglich)

---

## Uebungen

**Aufgabe 1:** Ein Unternehmen betreibt 20 Arbeitsplatz-PCs (je 200 W) und 2 Server (je 600 W). Alle laufen 10 Stunden pro Tag, 250 Arbeitstage im Jahr. Berechne die jaehrlichen Stromkosten bei 0,32 EUR/kWh.

**Aufgabe 2:** Eine Videodatei ist 4,5 GB gross. Kann sie auf einem USB-Stick mit FAT32-Dateisystem gespeichert werden? Begruende.

**Aufgabe 3:** Du sollst eine Datei von 1,6 GB ueber eine 100 Mbit/s-Leitung uebertragen. Berechne die theoretische Uebertragungszeit.

**Aufgabe 4:** Ein Netzteil nimmt 650 W auf und liefert 520 W an die Komponenten. Berechne den Wirkungsgrad.

**Aufgabe 5:** Nenne drei Unterschiede zwischen BIOS und UEFI.

**Aufgabe 6:** Welches Dateisystem waehlst du fuer eine Linux-Installation? Begruende.

---

## Loesungen

**Aufgabe 1:**
- PCs: 20 × 200 W × 10 h × 250 Tage = 10.000.000 Wh = 10.000 kWh
- Server: 2 × 600 W × 10 h × 250 Tage = 3.000.000 Wh = 3.000 kWh
- Gesamt: 13.000 kWh × 0,32 EUR = **4.160,00 EUR/Jahr**

**Aufgabe 2:** Nein. FAT32 hat ein Dateigroessenlimit von 4 GB. Die Datei ist 4,5 GB und somit zu gross. Loesung: USB-Stick mit NTFS oder exFAT formatieren.

**Aufgabe 3:**
- 1,6 GB = 1.600.000.000 Byte = 12.800.000.000 Bit
- 100 Mbit/s = 100.000.000 bit/s
- Zeit = 12.800.000.000 / 100.000.000 = **128 Sekunden ≈ 2 Min 8 Sek**

**Aufgabe 4:**
- η = 520 / 650 × 100 = **80%**

**Aufgabe 5:** (1) BIOS: 16-Bit / UEFI: 64-Bit. (2) BIOS: MBR (max. 2 TB) / UEFI: GPT (nahezu unbegrenzt). (3) BIOS: kein Secure Boot / UEFI: Secure Boot moeglich.

**Aufgabe 6:** ext4. Begruendung: Standard-Dateisystem fuer Linux, unterstuetzt grosse Dateien (bis 16 TB), Journaling fuer Datensicherheit, Berechtigungen (chmod/chown).
