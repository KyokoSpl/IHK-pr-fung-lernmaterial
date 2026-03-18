# Vertiefung und Uebungen: 1.6.03 – Sicherheitskonzept nach BSI-Grundschutz

## Zusammenhang: Schutzbedarfsanalyse → Risikomatrix → Massnahmen

```
Schutzbedarfsfeststellung (1.6.02)
        ↓
Risikobewertung (Eintrittswahrscheinlichkeit × Schadenshoehe)
        ↓
Risikomatrix → Priorisierung
        ↓
Risikobehandlung (Vermeidung / Minderung / Uebertragung / Akzeptanz)
        ↓
BSI-Bausteine auswaehlen → Massnahmen umsetzen
        ↓
ISMS: Kontrolle und Verbesserung (PDCA)
```

## Vergleich: ISO 27001 vs. BSI-Grundschutz

| Kriterium | ISO 27001 | BSI IT-Grundschutz |
|---|---|---|
| **Herkunft** | International (ISO) | Deutschland (BSI) |
| **Ansatz** | Risikobasiert (individuell) | Massnahmenbasiert (Bausteine) |
| **Flexibilitaet** | Hoch (eigene Risikobewertung) | Strukturiert (vordefinierte Anforderungen) |
| **Zertifizierbar** | Ja | Ja (ISO 27001 auf Basis IT-Grundschutz) |
| **Aufwand** | Geringer (weniger Dokumentation) | Hoeher (detaillierte Bausteine) |

## Typische Pruefungsaspekte

1. **Risikomatrix erstellen:** Eintrittswahrscheinlichkeit × Schadenshoehe bewerten
2. **Schutzbedarfskategorien:** Normal/hoch/sehr hoch mit Begruendung zuordnen
3. **Risikobehandlung:** Vier Strategien benennen und Beispiele geben
4. **ISMS erklaeren:** Kernelemente und PDCA-Bezug
5. **BSI-Bausteine:** Anforderungsstufen (Basis/Standard/Erhoehter Schutzbedarf) kennen

## Haeufige Fehler

| Fehler | Richtig |
|---|---|
| ISMS = Software-Tool | ISMS ist ein Managementsystem (Prozesse, Rollen, Richtlinien) |
| Risikoakzeptanz = Risiko ignorieren | Risikoakzeptanz = bewusste, dokumentierte Entscheidung |
| Alle Risiken muessen eliminiert werden | Es gibt immer ein Restrisiko; Kosten-Nutzen-Abwaegung |
| BSI-Grundschutz ersetzt ISO 27001 | BSI-Grundschutz kann Grundlage fuer ISO 27001-Zertifizierung sein |

---

## Aufgabe 1: Risikomatrix
Ein Unternehmen identifiziert folgende Risiken. Trage sie in die Risikomatrix ein:
a) Festplattenausfall bei Server ohne Backup (Wahrscheinlichkeit: mittel, Schaden: hoch)
b) Stromausfall < 5 Min. (Wahrscheinlichkeit: hoch, Schaden: gering)
c) Ransomware-Angriff (Wahrscheinlichkeit: mittel, Schaden: hoch)
d) Fehlkonfiguration Firewall (Wahrscheinlichkeit: gering, Schaden: mittel)

## Aufgabe 2: Risikobehandlung
Ordne fuer jedes Risiko aus Aufgabe 1 eine passende Behandlungsstrategie zu und begruende.

## Aufgabe 3: Schutzbedarfskategorien
Ein Online-Haendler betreibt eine Webanwendung mit Kundendaten und Zahlungsinformationen. Leite den Schutzbedarf ab und begruende anhand der Schadensszenarien.

## Aufgabe 4: ISMS
Erklaere, warum ein ISMS nicht als einmaliges Projekt, sondern als kontinuierlicher Prozess verstanden werden muss. Nutze den PDCA-Zyklus.

---
---

## Loesung 1

| | Schaden gering | Schaden mittel | Schaden hoch |
|---|---|---|---|
| **W. hoch** | b) Stromausfall (Mittel) | – | – |
| **W. mittel** | – | – | a) Festplatte (Hoch), c) Ransomware (Hoch) |
| **W. gering** | – | d) Firewall (Gering) | – |

## Loesung 2
a) **Risikominderung** – RAID-System und regelmaessige Backups einrichten → Schadenshoehe sinkt
b) **Risikoakzeptanz** – Kurze Ausfaelle sind tolerierbar; ggf. USV als Minderung
c) **Risikominderung** – Virenschutz, E-Mail-Filter, Mitarbeiterschulung, Backup-Strategie
d) **Risikominderung** – Regelmaessige Firewall-Audits, Change-Management-Prozess

## Loesung 3

| Schutzziel | Kategorie | Begruendung |
|---|---|---|
| Vertraulichkeit | **Sehr hoch** | Zahlungsdaten (PCI-DSS), personenbezogene Daten → Gesetzesverstoss DSGVO |
| Integritaet | **Hoch** | Falsche Bestelldaten → Kundenbeschwerden, Finanzverlust |
| Verfuegbarkeit | **Sehr hoch** | Ausfall = kein Umsatz, Imageschaden, Kundenverlust |
| **Gesamt** | **Sehr hoch** | Maximumprinzip angewandt |

## Loesung 4
Ein ISMS muss kontinuierlich sein, da:
- **Plan:** Neue Bedrohungen (z.B. Zero-Day-Exploits) erfordern staendige Neubewertung der Risiken
- **Do:** Neue Massnahmen muessen implementiert und Mitarbeiter geschult werden
- **Check:** Audits und Penetrationstests decken Schwachstellen auf
- **Act:** Erkenntnisse fliessen in aktualisierte Richtlinien ein

Die Bedrohungslage aendert sich staendig → ohne kontinuierliche Anpassung veraltet das Sicherheitskonzept und wird wirkungslos.
