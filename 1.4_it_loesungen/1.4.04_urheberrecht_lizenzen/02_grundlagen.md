# Grundlagen: 1.4.04 – Urheberrechtsgesetz und Lizenzmodelle

## Grundlagen des Schutzes der Urheber

**Definition:** Das Urheberrechtsgesetz (UrhG) schuetzt die geistigen Schoepfungen von Urhebern. Software wird als literarisches Werk behandelt und ist automatisch ab Entstehung geschuetzt.

**Kernaussagen:**
- Urheber ist die natuerliche Person, die das Werk geschaffen hat
- Urheberrecht entsteht automatisch (keine Registrierung noetig)
- Software ist nach §69a UrhG geschuetzt
- Verwertungsrechte: Vervielfaeltigung, Verbreitung, oeffentliche Zugaenglichmachung
- Nutzungsrechte koennen uebertragen werden (Lizenz), das Urheberrecht selbst nicht
- Schutzdauer: 70 Jahre nach Tod des Urhebers

**Wichtige Begriffe:**
- **Urheberrecht** – Schutzrecht des Schöpfers (unveräusserlich)
- **Nutzungsrecht/Lizenz** – Erlaubnis, ein Werk zu nutzen (uebertragbar)
- **Verwertungsrecht** – Recht, wirtschaftlichen Nutzen aus dem Werk zu ziehen
- **Raubkopie** – Unerlaubte Vervielfaeltigung geschuetzter Software

**Erklaerung:** Auch wenn ein Arbeitnehmer Software im Rahmen seiner Arbeit erstellt, bleibt er Urheber. Die Verwertungsrechte gehen jedoch in der Regel an den Arbeitgeber ueber (§69b UrhG).

---

## Lizenzarten

**Definition:** Lizenzen regeln die Bedingungen, unter denen Software genutzt werden darf.

| Lizenzart | Beschreibung | Eigentuemer |
|---|---|---|
| **EULA** | End User License Agreement – Endbenutzer-Lizenzvertrag fuer proprietaere Software | Hersteller behaelt alle Rechte |
| **OEM** | Original Equipment Manufacturer – Lizenz an Hardware gebunden | Hardware-Kaeufer |
| **GNU GPL** | General Public License – Copyleft, Quellcode muss offenbleiben | Community |
| **MIT** | Permissiv – fast alles erlaubt, auch proprietaere Nutzung | Frei |
| **Apache** | Permissiv + Patentschutz | Frei |
| **Creative Commons** | Fuer Werke (Texte, Bilder), verschiedene Abstufungen | Urheber waehlt |

### EULA im Detail
- Typisch fuer Microsoft, Adobe, SAP
- Regelt: Anzahl Installationen, Weitergabe, Nutzungszweck
- Zustimmung bei Installation erforderlich
- Verstoss = Lizenzrechtsverletzung

### OEM-Lizenz im Detail
- An bestimmte Hardware (z.B. PC, Laptop) gekoppelt
- Guenstiger als Retail-Lizenz
- Nicht uebertragbar auf andere Hardware
- Beispiel: Windows auf vorinstalliertem Laptop

### GNU GPL im Detail
- Copyleft-Prinzip: Abgeleitete Werke muessen ebenfalls unter GPL stehen
- Quellcode muss bei Verbreitung offengelegt werden
- Kommerzielle Nutzung erlaubt, aber Quellcode bleibt offen
- Beispiel: Linux-Kernel, WordPress

---

## Pay-per-Use

**Definition:** Abrechnungsmodell, bei dem nur die tatsaechliche Nutzung berechnet wird – keine festen Lizenzgebuehren.

**Kernaussagen:**
- Typisch fuer Cloud-Dienste (AWS, Azure, Google Cloud)
- Abrechnung nach: Rechenzeit, Speichervolumen, API-Aufrufe, Transaktionen
- Vorteile: Keine Vorabkosten, Skalierbarkeit, flexible Nutzung
- Nachteile: Schwer kalkulierbar, bei hoher Nutzung teuer
- Beispiel: AWS EC2 (pro Betriebsstunde), Azure Blob (pro GB gespeichert)

**Erklaerung:** In der Pruefung werden haeufig Kostenvergleiche gefordert: Wann lohnt sich Pay-per-Use vs. Flat-Rate vs. Lizenzkauf? Entscheidend ist das Nutzungsvolumen.

## Querverweise
- → 1.4.03 (Open Source, proprietaere Software)
- → 1.3.04 (Kostenvergleich, Finanzierungsmodelle)
- → 1.7.01 (Lizenzvertrag als Vertragsart)
