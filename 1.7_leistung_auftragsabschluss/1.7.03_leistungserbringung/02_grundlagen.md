# Grundlagen: 1.7.03 – Umsetzungsvarianten der Leistungserbringung

## Kundenvorgaben bei der Leistungserbringung

| Vorgabe | Beschreibung | Beispiel |
|---|---|---|
| **Termin** | Liefer-/Fertigstellungszeitpunkt | Rollout bis 01.04. |
| **Erfuellungsort** | Wo wird die Leistung erbracht? | Vor Ort beim Kunden / Remote |
| **Technische Voraussetzungen** | Betriebssystem, Hersteller, Infrastruktur | „Nur Windows 11", „Cisco-Hardware" |
| **Budget** | Finanzrahmen fuer die Leistung | Max. 50.000 EUR |

**Wichtig:** Alle Vorgaben muessen im Vertrag/Lastenheft dokumentiert sein. Abweichungen erfordern Abstimmung (Change Request).

---

## Leistungserbringung: Vor Ort vs. Remote

| Kriterium | Vor Ort | Remote |
|---|---|---|
| **Zugang** | Physisch beim Kunden | Ueber VPN/Fernwartung |
| **Kommunikation** | Direkt, persoenlich | Videokonferenz, Chat, Telefon |
| **Reaktionszeit** | Anfahrt noetig | Sofort moeglich |
| **Kosten** | Hoeher (Reise, Zeit) | Geringer |
| **Geeignet fuer** | Hardware-Installation, Schulung | Software-Support, Konfiguration |
| **Sicherheit** | Physischer Zugang zu Systemen | Abhaengig von Netzwerkzugang |

**Hybridmodell:** Kombination aus Vor-Ort und Remote – z.B. Hardware vor Ort installieren, Software remote konfigurieren.

---

## Ticketsystem

**Definition:** Software zur strukturierten Erfassung, Verfolgung und Bearbeitung von Service-Anfragen und Stoerungen.

**Typischer Ticket-Lebenszyklus:**
```
Neu → Zugewiesen → In Bearbeitung → Warte auf Kunde → Geloest → Geschlossen
```

**Ticket-Inhalte:**

| Feld | Beschreibung |
|---|---|
| Ticket-ID | Eindeutige Nummer |
| Ersteller | Wer hat das Ticket eroeffnet? |
| Kategorie | Stoerung, Anfrage, Change |
| Prioritaet | Kritisch, Hoch, Mittel, Niedrig |
| Beschreibung | Detaillierte Problembeschreibung |
| Zugewiesen an | Bearbeiter/Team |
| Status | Aktueller Stand |
| Loesung | Dokumentierte Loesung |

**Vorteile:**
- Nachvollziehbarkeit aller Anfragen
- SLA-Ueberwachung (Reaktions-/Loesungszeiten)
- Wissensdatenbank aus geloesten Tickets
- Reporting und Statistik (haeufigste Stoerungen)

**Bekannte Systeme:** JIRA, OTRS, Zendesk, ServiceNow, Redmine
