# Grundlagen: 1.6.02 – Schutzbedarfsanalyse nach BSI-Grundschutz

## Schutzbedarfskategorien (BSI)

| Kategorie | Beschreibung | Schadenauswirkung |
|---|---|---|
| **Normal** | Begrenzte/ueberschaubare Schaeden | Schadensauswirkungen sind begrenzt und ueberschaubar |
| **Hoch** | Schaeden koennen betraechtlich sein | Erhebliche finanzielle/rechtliche Folgen |
| **Sehr hoch** | Schaeden koennen existenzbedrohend sein | Gefahr fuer Leib/Leben oder Existenz des Unternehmens |

## Schutzbedarfsanalyse fuer Anwendungen

**Definition:** Bewertung, welchen Schutzbedarf eine Software-Anwendung hinsichtlich der Schutzziele (Vertraulichkeit, Integritaet, Verfuegbarkeit) hat.

**Vorgehen:**
1. Alle Anwendungen erfassen (z.B. ERP, CRM, E-Mail, Datenbank)
2. Fuer jede Anwendung: Welche Daten werden verarbeitet?
3. Bewertung pro Schutzziel anhand der Schadensszenarien
4. Hoechstes Einzelergebnis = Gesamtschutzbedarf der Anwendung

**Beispiel:**

| Anwendung | Vertraulichkeit | Integritaet | Verfuegbarkeit | Gesamt |
|---|---|---|---|---|
| E-Mail | Normal | Normal | Hoch | **Hoch** |
| ERP-System | Hoch | Hoch | Sehr hoch | **Sehr hoch** |
| Intranet-Wiki | Normal | Normal | Normal | **Normal** |
| Personalverwaltung | Sehr hoch | Hoch | Hoch | **Sehr hoch** |

---

## Schutzbedarfsanalyse fuer IT-Systeme

**Definition:** IT-Systeme erben den Schutzbedarf der Anwendungen, die auf ihnen laufen.

**Maximumprinzip:** Das IT-System erhaelt den hoechsten Schutzbedarf aller darauf laufenden Anwendungen.

**Kumulationseffekt:** Mehrere Anwendungen mit normalem Schutzbedarf koennen zusammen einen hoeheren Schutzbedarf ergeben (wenn der Ausfall aller zusammen gravierend waere).

**Verteilungseffekt:** Wenn eine Anwendung auf mehrere redundante Systeme verteilt ist, kann der Schutzbedarf des einzelnen Systems sinken.

**Beispiel:**

| IT-System | Anwendungen darauf | Schutzbedarf |
|---|---|---|
| Server-01 | ERP, Datenbank | Sehr hoch (Maximum) |
| Client-PC | E-Mail, Browser | Hoch |
| Backup-Server | Backup-Software | Hoch (Verfuegbarkeit) |

---

## Schutzbedarfsanalyse fuer Kommunikationsverbindungen

**Definition:** Bewertung der Netzwerkverbindungen hinsichtlich Vertraulichkeit und Integritaet der uebertragenen Daten.

**Bewertungskriterien:**
- Welche Daten werden uebertragen?
- Intern oder extern (Internet)?
- Verschluesselt oder unverschluesselt?
- Physisch geschuetzt oder offen zugaenglich?

**Beispiel:**

| Verbindung | Daten | Schutzbedarf |
|---|---|---|
| LAN (intern, geswitched) | Allgemeine Burodaten | Normal |
| VPN (Homeoffice → Firma) | Geschaeftsdaten | Hoch |
| WLAN (Gaestenetz) | Internetzugang | Normal |
| Anbindung Rechenzentrum | Alle Unternehmensdaten | Sehr hoch |

---

## Schutzbedarfsanalyse fuer Raeume und Infrastruktur

**Definition:** Physische Sicherheitsbewertung der Raeumlichkeiten und technischen Infrastruktur.

**Zu bewertende Objekte:**
- Serverraeume
- Buroraeume
- Verteilerraeume / Netzwerkschraenke
- Archivrueme
- Haustechnik (Klimaanlage, USV)

**Beispiel:**

| Raum/Infrastruktur | Begruendung | Schutzbedarf |
|---|---|---|
| Serverraum | Alle zentralen Systeme | Sehr hoch |
| Buero Buchhaltung | Finanzdaten | Hoch |
| Empfangsbereich | Keine sensiblen Daten | Normal |
| Verteilerraum 2. OG | Netzwerk-Switches | Hoch |
| Klimaanlage Serverraum | Betrieb der Server | Hoch |
