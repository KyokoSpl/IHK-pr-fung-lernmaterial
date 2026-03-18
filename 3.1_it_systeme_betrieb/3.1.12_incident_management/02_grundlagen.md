# Grundlagen: 3.1.12 – Monitoringergebnisse analysieren und korrektive Massnahmen

## Eskalationsstufen

**Definition:** Eskalation ist die stufenweise Weiterleitung eines Vorfalls (Incident) an hoeher qualifizierte oder autorisierte Stellen, wenn eine Loesung auf der aktuellen Stufe nicht moeglich ist.

**Arten der Eskalation:**

| Art | Beschreibung | Beispiel |
|---|---|---|
| Funktionale Eskalation | Weiterleitung an Spezialisten mit tieferem Fachwissen | 1st Level → 2nd Level → 3rd Level |
| Hierarchische Eskalation | Weiterleitung an Vorgesetzte/Management | Admin → Teamleiter → IT-Leiter → Geschaeftsfuehrung |

**Typischer Eskalationspfad:**

```
Vorfall erkannt (Monitoring/Anruf/Ticket)
         |
         v
  +------+-------+
  | 1st Level    |  Annahme, Klassifizierung, Standardloesungen
  | (Service Desk)|  Loesung innerhalb von 30 min?
  +------+-------+
         | Nein
         v
  +------+-------+
  | 2nd Level    |  Tiefgehende Analyse, Spezialwissen
  | (Fachteam)   |  Loesung innerhalb von 2 h?
  +------+-------+
         | Nein
         v
  +------+-------+
  | 3rd Level    |  Hersteller, Entwickler, externe Experten
  | (Experten)   |  Loesung ggf. ueber Tage/Wochen
  +------+-------+
         |
    (Parallel: hierarchische Eskalation bei SLA-Gefaehrdung)
```

**Wichtige Begriffe:**
- **Funktionale Eskalation** – Weiterleitung an Spezialisten (vertikal im Fachwissen)
- **Hierarchische Eskalation** – Weiterleitung an Vorgesetzte (vertikal in der Hierarchie)
- **Eskalationszeit** – Maximale Zeit, bevor auf die naechste Stufe eskaliert wird

---

## Incident Management (Ticketsystem)

**Definition:** Incident Management ist ein ITIL-Prozess mit dem Ziel, den normalen Betrieb eines IT-Dienstes so schnell wie moeglich wiederherzustellen und die Auswirkungen auf das Geschaeft zu minimieren.

**ITIL-Definition:**
- **Incident (Stoerung):** Ungeplante Unterbrechung oder Qualitaetsminderung eines IT-Dienstes
- **Problem:** Ursache fuer einen oder mehrere Incidents (wird im Problem Management behandelt)
- **Change:** Geplante Aenderung an der IT-Infrastruktur

**Incident-Management-Prozess:**

| Schritt | Beschreibung |
|---|---|
| 1. Erfassung | Stoerung wird erkannt (Monitoring, Anruf, E-Mail) und im Ticketsystem dokumentiert |
| 2. Klassifizierung | Kategorie (Hardware, Software, Netzwerk) und Prioritaet festlegen |
| 3. Priorisierung | Basierend auf Auswirkung (Impact) und Dringlichkeit (Urgency) |
| 4. Diagnose | Ursache ermitteln, ggf. bekannte Fehler (Known Errors) pruefen |
| 5. Loesung | Workaround oder dauerhafte Behebung |
| 6. Abschluss | Ticket schliessen, Dokumentation abschliessen, Nutzer informieren |

**Prioritaetsmatrix:**

| | Dringlichkeit hoch | Dringlichkeit mittel | Dringlichkeit niedrig |
|---|---|---|---|
| **Auswirkung hoch** | P1 – Kritisch | P2 – Hoch | P3 – Mittel |
| **Auswirkung mittel** | P2 – Hoch | P3 – Mittel | P4 – Niedrig |
| **Auswirkung niedrig** | P3 – Mittel | P4 – Niedrig | P5 – Gering |

**Typische Ticketsysteme:**

| System | Typ | Besonderheit |
|---|---|---|
| OTRS / Znuny | Open Source | ITIL-konform, weit verbreitet |
| Jira Service Management | Kommerziell | Integration mit Jira (Entwicklung) |
| GLPI | Open Source | IT-Asset-Management + Ticketing |
| ServiceNow | Kommerziell (Cloud) | Enterprise-ITSM, sehr umfangreich |
| osTicket | Open Source | Einfach, fuer kleine Teams |

**Wichtige Begriffe:**
- **Ticket** – Datensatz, der einen Vorfall dokumentiert (Nummer, Beschreibung, Status, Prioritaet)
- **Impact** – Auswirkung der Stoerung (wie viele Nutzer/Systeme betroffen?)
- **Urgency** – Dringlichkeit (wie schnell muss reagiert werden?)
- **Workaround** – Provisorische Loesung, die den Betrieb wiederherstellt
- **Known Error** – Bekannte Fehlerursache mit dokumentiertem Workaround
- **CMDB (Configuration Management Database)** – Datenbank aller IT-Komponenten und deren Beziehungen

---

## SLA / Service Level 1–3

**Definition:** Ein Service Level Agreement (SLA) ist eine vertragliche Vereinbarung zwischen IT-Dienstleister und Kunde ueber die Qualitaet und Verfuegbarkeit eines Dienstes.

**Support-Stufen:**

| Stufe | Bezeichnung | Aufgaben | Personal |
|---|---|---|---|
| 1st Level | Service Desk / Helpdesk | Annahme, Klassifizierung, Standardloesungen (z.B. Passwort-Reset) | IT-Support-Mitarbeiter |
| 2nd Level | Fachteam | Tiefgehende technische Analyse, Konfiguration, Administration | Systemadministratoren, Netzwerk-Admins |
| 3rd Level | Experten / Hersteller | Entwicklung, Patches, Hardwaretausch, Root-Cause-Analyse | Entwickler, Hersteller-Support |

**SLA-Kennzahlen:**

| Kennzahl | Definition | Beispiel |
|---|---|---|
| Verfuegbarkeit | Prozentualer Anteil der Uptime | 99,9 % |
| Reaktionszeit | Max. Zeit bis zur ersten Reaktion | P1: 15 min, P2: 1 h |
| Loesungszeit | Max. Zeit bis zur Wiederherstellung | P1: 2 h, P2: 8 h |
| Servicezeit | Zeitfenster, in dem Support geleistet wird | Mo–Fr 8–18 Uhr oder 24/7 |

**Typische SLA-Zeiten nach Prioritaet:**

| Prioritaet | Reaktionszeit | Loesungszeit | Beispiel |
|---|---|---|---|
| P1 – Kritisch | 15 Minuten | 2 Stunden | Server komplett ausgefallen, 200 Nutzer betroffen |
| P2 – Hoch | 30 Minuten | 4 Stunden | E-Mail-System fuer eine Abteilung gestoert |
| P3 – Mittel | 2 Stunden | 8 Stunden | Drucker einer Etage defekt |
| P4 – Niedrig | 4 Stunden | 2 Arbeitstage | Einzelner Monitor flackert |

**Wichtige Begriffe:**
- **Reaktionszeit** – Zeit bis zur ersten qualifizierten Rueckmeldung (nicht Loesung!)
- **Loesungszeit** – Zeit bis der Dienst wiederhergestellt ist
- **Servicezeit** – Zeitfenster, in dem das SLA gilt (z.B. 8x5 oder 24x7)
- **OLA (Operational Level Agreement)** – Interne Vereinbarung zwischen IT-Teams
- **UC (Underpinning Contract)** – Vertrag mit externem Dienstleister, der das SLA unterstuetzt

---

## Standard Operation Procedures (SOP)

**Definition:** Eine SOP ist eine dokumentierte, Schritt-fuer-Schritt-Anleitung fuer wiederkehrende IT-Aufgaben. Sie stellt sicher, dass Aufgaben unabhaengig von der Person einheitlich, korrekt und effizient ausgefuehrt werden.

**Typische SOPs in der IT:**

| SOP | Inhalt |
|---|---|
| Server-Neustart | Reihenfolge der Dienste, Pruefung nach Neustart |
| Passwort-Reset | Identitaetspruefung, Aendern im AD, Nutzer informieren |
| Backup-Restore | Auswahl des Backups, Rueckspielen, Verifizierung |
| Patching | Zeitfenster, Reihenfolge, Rollback-Plan |
| Onboarding neuer Mitarbeiter | Konto anlegen, Berechtigungen, Hardware ausgeben |
| Netzwerk-Port-Freischaltung | Antrag pruefen, Switch konfigurieren, dokumentieren |

**Aufbau einer SOP:**

| Abschnitt | Inhalt |
|---|---|
| Titel | Name der Prozedur |
| Zweck | Warum existiert diese SOP? |
| Geltungsbereich | Fuer welche Systeme/Situationen gilt sie? |
| Voraussetzungen | Was muss vorhanden sein? (Zugaenge, Tools) |
| Schritte | Nummerierte Schritt-fuer-Schritt-Anleitung |
| Verifizierung | Wie wird geprueft, ob die Aufgabe erfolgreich war? |
| Verantwortlich | Wer fuehrt die SOP aus? |
| Version / Datum | Versionskontrolle der Dokumentation |

**Wichtige Begriffe:**
- **Runbook** – Sammlung von SOPs fuer den IT-Betrieb
- **Playbook** – Ahnlich wie Runbook, oft im Security-Kontext (Incident Response)
- **Checkliste** – Vereinfachte SOP als Pruefliste (Abhakliste)
