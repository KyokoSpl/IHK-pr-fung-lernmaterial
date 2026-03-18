# Grundlagen: 1.3.03 – Leistungsfaehigkeit und Energieeffizienz von IT-Systemen

## Barrierefreier Zugriff auf IT-Systeme

**Definition:** Barrierefreiheit bedeutet, dass IT-Systeme und Webseiten so gestaltet sind, dass sie von Menschen mit koerperlichen oder kognitiven Einschraenkungen nutzbar sind.

**Kernaussagen:**
- **Visuelle Anpassungen:** Schriftgroesse, Kontrast, Farbschemata, Zoom
- **Screenreader:** Liest Bildschirminhalte vor (z.B. NVDA, JAWS)
- **Sprachsteuerung:** Bedienung per Stimme (z.B. Cortana, Siri)
- **Tastaturnavigation:** Vollstaendige Bedienbarkeit ohne Maus
- **Untertitel/Gebaerdensprache:** Fuer Audio-/Videoinhalte
- Normen: WCAG 2.1 (Web Content Accessibility Guidelines), BITV 2.0

**Wichtige Begriffe:**
- **WCAG** – Web Content Accessibility Guidelines (internationale Richtlinie)
- **BITV** – Barrierefreie-Informationstechnik-Verordnung (deutsches Recht)
- **Screenreader** – Software, die Bildschirminhalte vorliest
- **Alt-Text** – Alternativtext fuer Bilder (fuer Screenreader)

**Erklaerung:** In der Pruefung kann nach konkreten Massnahmen zur Barrierefreiheit am Arbeitsplatz gefragt werden: groesserer Monitor, breitere Tastatur, Lautsprecher/Mikrofon, angepasste Software-Einstellungen.

---

## Guetesiegel fuer Energieeffizienz

**Definition:** Zertifikate und Labels, die die Energieeffizienz und Umweltvertraeglichkeit von IT-Geraeten kennzeichnen.

**Kernaussagen:**

| Siegel | Fokus |
|---|---|
| Energy Star | Energieverbrauch (v.a. Standby) |
| Blauer Engel | Umweltvertraeglichkeit gesamt |
| TCO Certified | Ergonomie + Umwelt + Energie |
| EU-Energielabel | Energieeffizienzklasse (A-G) |
| EPEAT | Lebenszyklus-Umweltbewertung |

**Wichtige Begriffe:**
- **Energy Star** – US-Programm, international anerkannt
- **TCO** – Schwedisches Zertifikat fuer Bildschirme und IT-Geraete
- **EPEAT** – Electronic Product Environmental Assessment Tool

**Erklaerung:** Fuer die Pruefung muessen die wichtigsten Siegel benannt und deren Fokus beschrieben werden koennen. Haeufig wird nach der oekologischen Bewertung von IT-Anschaffungen gefragt.

---

## Kenngroessen zu Strom, Spannung, Leistung, Energie

**Definition:** Grundlegende elektrische Groessen, die fuer die Beurteilung von IT-Systemen relevant sind.

**Kernaussagen und Formeln:**

| Groesse | Formelzeichen | Einheit | Formel |
|---|---|---|---|
| Spannung | U | Volt (V) | U = R × I |
| Stromstaerke | I | Ampere (A) | I = U / R |
| Widerstand | R | Ohm (Ω) | R = U / I |
| Leistung | P | Watt (W) | P = U × I |
| Energie | E/W | Wattstunden (Wh) | E = P × t |
| Wirkungsgrad | η | % | η = P_ab / P_zu × 100 |

**Berechnungsbeispiel Energiekosten:**
- Server: P = 500 W, Laufzeit = 24h/Tag, 365 Tage
- Jahresverbrauch: 500 W × 24h × 365 = 4.380.000 Wh = 4.380 kWh
- Kosten bei 0,30 EUR/kWh: 4.380 × 0,30 = 1.314,00 EUR/Jahr

**Wichtige Begriffe:**
- **Wirkungsgrad (η)** – Verhaeltnis Nutzleistung zu zugefuehrter Leistung
- **PUE (Power Usage Effectiveness)** – Kennzahl fuer Rechenzentren (Gesamt-Energie / IT-Energie)
- **TDP (Thermal Design Power)** – Max. Waermeabgabe einer CPU

---

## Kenngroessen zu Uebertragungsraten und Datenmengen

**Definition:** Kennwerte fuer die Geschwindigkeit und das Volumen von Datenuebertragungen.

**Kernaussagen:**
- **Bit vs. Byte:** 1 Byte = 8 Bit
- **Uebertragungsrate:** bit/s (bps), kbit/s, Mbit/s, Gbit/s
- **Speicherkapazitaet:** Byte, KB, MB, GB, TB (Basis 1000 oder 1024)

**Umrechnungstabelle:**

| Einheit | Dezimal (SI) | Binaer (IEC) |
|---|---|---|
| Kilo | 1.000 | 1.024 (KiB) |
| Mega | 1.000.000 | 1.048.576 (MiB) |
| Giga | 1.000.000.000 | 1.073.741.824 (GiB) |

**Berechnungsbeispiel Uebertragungszeit:**
- Datei: 2 GB = 2.000.000.000 Byte = 16.000.000.000 Bit
- Leitung: 100 Mbit/s = 100.000.000 bit/s
- Zeit: 16.000.000.000 / 100.000.000 = 160 Sekunden = 2 Min 40 Sek

**Wichtige Begriffe:**
- **Bruttodatenrate** – Theoretische Maximalrate inkl. Overhead
- **Nettodatenrate** – Tatsaechliche Nutzrate nach Abzug von Overhead
- **Latenz** – Verzoegerung einer Uebertragung (ms)

---

## Leistungsdaten und Funktionsumfang von Hardware

**Definition:** Spezifikationen von Hardware-Komponenten, die die Leistungsfaehigkeit eines IT-Systems bestimmen.

**Kernaussagen:**

### CPU
- Taktfrequenz (GHz), Kerne, Threads
- Cache (L1, L2, L3)
- Architektur (x86, x64, ARM)

### RAM
- Kapazitaet (GB), Typ (DDR4, DDR5)
- Taktfrequenz (MHz)
- Dual Channel fuer hoehere Bandbreite

### Datenspeicher

| Typ | Vorteil | Nachteil |
|---|---|---|
| HDD | Guenstig, hohe Kapazitaet | Langsam, mechanisch, stossempfindlich |
| SSD (SATA) | Schneller als HDD, lautlos | Teurer als HDD |
| SSD (NVMe) | Sehr schnell (PCIe-Anbindung) | Am teuersten |

### Dateisysteme

| Dateisystem | Betriebssystem | Max. Dateigroesse |
|---|---|---|
| FAT32 | Windows/Linux/Mac | 4 GB |
| NTFS | Windows | 16 TB |
| APFS | macOS | Praktisch unbegrenzt |
| ext4 | Linux | 16 TB |

### BIOS/UEFI
- **BIOS** – Basic Input/Output System (aelter, 16-Bit, MBR)
- **UEFI** – Unified Extensible Firmware Interface (modern, 64-Bit, GPT, Secure Boot)
- Einstellungen: Boot-Reihenfolge, Virtualisierung, TPM, Secure Boot

### Netzwerk
- Ethernet-Standards: 100BASE-TX (100 Mbit/s), 1000BASE-T (1 Gbit/s), 10GBASE-T (10 Gbit/s)
- WLAN-Standards: 802.11n (Wi-Fi 4), 802.11ac (Wi-Fi 5), 802.11ax (Wi-Fi 6)
- LWL (Lichtwellenleiter): Singlemode (lange Strecken), Multimode (kurze Strecken)

## Querverweise
- → 1.3.04 (Wirtschaftlichkeit: Kosten pro Leistung)
- → 1.4.01 (Installation/Konfiguration: BIOS, Partitionierung)
- → 1.4.02 (Hardwareauswahl nach Bedarf)
- → 3.1.03 (Netzwerktopologien, WLAN-Standards)
