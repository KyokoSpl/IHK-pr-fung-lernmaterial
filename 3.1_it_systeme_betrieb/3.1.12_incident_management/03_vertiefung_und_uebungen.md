# Vertiefung und Uebungen: 3.1.12 – Monitoringergebnisse analysieren und korrektive Massnahmen

## Vertiefung

### Incident Management – Detaillierter Ablauf

```
  Nutzer meldet Stoerung        Monitoring erkennt Stoerung
         |                                |
         +----------------+---------------+
                          |
                          v
               +----------+----------+
               | Ticket erstellen    |
               | (ID, Beschreibung,  |
               |  Kategorie, Zeit)   |
               +----------+----------+
                          |
                          v
               +----------+----------+
               | Klassifizierung     |
               | Impact + Urgency    |
               | → Prioritaet (P1–P5)|
               +----------+----------+
                          |
                          v
               +----------+----------+
               | Known Error?        |
               | → Ja: Workaround   |
               | → Nein: Diagnose   |
               +----------+----------+
                          |
            +-------------+-------------+
            |                           |
      Geloest?                   Nicht geloest?
            |                           |
            v                           v
   +--------+--------+        +--------+--------+
   | Ticket schliessen|        | Eskalation      |
   | Nutzer informieren|       | (funktional/    |
   +------------------+        |  hierarchisch)  |
                               +--------+--------+
                                        |
                                   (Naechste Stufe)
```

### Incident vs. Problem vs. Change

| Begriff | Definition | Beispiel |
|---|---|---|
| **Incident** | Ungeplante Unterbrechung eines Dienstes | Server nicht erreichbar |
| **Problem** | Ursache fuer einen oder mehrere Incidents | Defekte Netzwerkkarte im Server |
| **Change** | Geplante Aenderung an der IT-Infrastruktur | Netzwerkkarte austauschen |

→ Ablauf: Incident wird erkannt → Workaround (schnelle Loesung) → Problem Management (Ursache finden) → Change Management (dauerhafte Loesung implementieren)

### SLA-Einhaltung pruefen – Praxisbeispiel

**Szenario:** SLA fuer E-Mail-Server: Verfuegbarkeit 99,9 % pro Monat, Reaktionszeit P1: 15 min, Loesungszeit P1: 2 h.

**Vorfaelle im Monat Maerz (30 Tage):**

| Ticket | Prioritaet | Reaktionszeit | Loesungszeit | Ausfallzeit |
|---|---|---|---|---|
| INC-0042 | P1 | 10 min | 1 h 45 min | 1 h 45 min |
| INC-0056 | P2 | 25 min | 3 h | 0 (Workaround) |
| INC-0071 | P1 | 20 min | 2 h 30 min | 2 h 30 min |

**Auswertung:**
```
Gesamte Ausfallzeit: 1 h 45 min + 2 h 30 min = 4 h 15 min = 255 min
Gesamtzeit im Monat: 30 * 24 * 60 = 43.200 min
Verfuegbarkeit: (43.200 - 255) / 43.200 = 99,41 %
→ SLA (99,9 %) NICHT eingehalten!

INC-0042: Reaktionszeit 10 min (SLA 15 min) ✓, Loesungszeit 1:45 (SLA 2h) ✓
INC-0071: Reaktionszeit 20 min (SLA 15 min) ✗ VERLETZT, Loesungszeit 2:30 (SLA 2h) ✗ VERLETZT
```

### Support-Level im Detail

| Aspekt | 1st Level | 2nd Level | 3rd Level |
|---|---|---|---|
| Qualifikation | IT-Grundkenntnisse | Spezialist (z.B. Netzwerk, Server) | Entwickler / Hersteller |
| Werkzeuge | Ticketsystem, Remote-Desktop, FAQ | Admin-Tools, CLI, Monitoring | Quellcode, Debug-Tools, Labor |
| Typische Aufgaben | Passwort-Reset, Druckerproblem, Ticket-Weiterleitung | Firewall-Regel, AD-Konfiguration, Server-Analyse | Bugfix, Firmware-Update, Hardware-RMA |
| Loesungsrate | 60–70 % aller Tickets | 25–30 % | 5–10 % |
| Beispiel-Ticket | „Ich kann mich nicht anmelden" → Passwort zuruecksetzen | „VPN funktioniert nicht" → VPN-Gateway analysieren | „Software-Bug verursacht Absturz" → Entwickler analysiert Code |

### SOP – Beispiel: Server-Neustart

```
SOP-ID:     SOP-003
Titel:      Geplanter Neustart eines Windows-Servers
Version:    1.2
Datum:      2026-01-15
Gueltig fuer: Alle Windows-Server im Rechenzentrum

VORAUSSETZUNGEN:
- Admin-Zugang zum Server (RDP oder Konsole)
- Genehmigter Change-Request im Ticketsystem
- Wartungsfenster kommuniziert an betroffene Nutzer

SCHRITTE:
1. Change-Ticket pruefen (Genehmigung vorhanden?)
2. Monitoring fuer den Server in Wartungsmodus setzen (Alarme unterdrücken)
3. Alle laufenden Dienste pruefen und dokumentieren
4. Nutzer informieren (5 Minuten vorher)
5. Server herunterfahren (shutdown /s /t 60)
6. 2 Minuten warten
7. Server starten
8. Dienste pruefen: Alle Dienste gestartet? (services.msc)
9. Anwendungen testen (z.B. Webseite aufrufen, Datenbankverbindung pruefen)
10. Monitoring aus Wartungsmodus nehmen
11. Nutzer informieren (Server wieder verfuegbar)
12. Ticket abschliessen mit Dokumentation

VERIFIZIERUNG:
- Alle Dienste laufen (gruener Status im Monitoring)
- Anwendung ist erreichbar (HTTP 200)
- Keine Fehlermeldungen im Eventlog (letzte 15 Minuten)
```

### Typische Pruefungsaspekte
- Eskalationsstufen (funktional vs. hierarchisch) erklaeren
- Incident-Management-Ablauf nach ITIL beschreiben
- Prioritaetsmatrix (Impact x Urgency) anwenden
- SLA-Kennzahlen berechnen und SLA-Verletzung feststellen
- SOP-Aufbau beschreiben und Vorteile benennen
- Unterschied Incident/Problem/Change erklaeren

### Haeufige Fehler
- Incident und Problem verwechseln → Incident = Symptom, Problem = Ursache
- Reaktionszeit mit Loesungszeit verwechseln → Reaktionszeit = erste Rueckmeldung, nicht Loesung
- Eskalation als Versagen sehen → Eskalation ist ein normaler, geplanter Prozess
- SOPs erstellen, aber nie aktualisieren → Veraltete SOPs fuehren zu Fehlern
- Support-Level an Personen statt an Kompetenzen binden → Rollen koennen wechseln

---

## Uebungen

**Aufgabe 1:** Erklaere den Unterschied zwischen funktionaler und hierarchischer Eskalation. Nenne je ein Beispiel.

**Aufgabe 2:** Ein Nutzer meldet: „Ich kann keine E-Mails mehr senden." Der Admin prueft: Alle anderen Nutzer koennen E-Mails senden, der Mailserver laeuft normal.
- a) Ordne dem Vorfall eine Kategorie und Prioritaet zu (Auswirkung: gering, Dringlichkeit: mittel).
- b) Beschreibe die naechsten Schritte im Incident-Management-Prozess.

**Aufgabe 3:** Ein Unternehmen hat folgendes SLA: Verfuegbarkeit 99,9 % pro Monat, Reaktionszeit P1: 15 min, Loesungszeit P1: 4 h. Im April (30 Tage) gab es zwei P1-Incidents:
- INC-101: Reaktion nach 10 min, Loesung nach 3 h, Ausfallzeit 3 h
- INC-102: Reaktion nach 20 min, Loesung nach 5 h, Ausfallzeit 5 h

a) Wurde die Verfuegbarkeits-SLA eingehalten?
b) Welche SLA-Verstösse sind aufgetreten?

**Aufgabe 4:** Beschreibe die Rolle und Aufgaben des 1st, 2nd und 3rd Level Supports.

**Aufgabe 5:** Erklaere den Unterschied zwischen Incident, Problem und Change anhand eines Beispiels: Ein Druckerserver faellt wiederholt aus.

**Aufgabe 6:** Erstelle eine vereinfachte SOP (mindestens 6 Schritte) fuer die Aufgabe „Passwort eines Active-Directory-Nutzers zuruecksetzen".

**Aufgabe 7:** Was ist eine Prioritaetsmatrix? Erstelle eine Matrix mit den Achsen „Auswirkung" und „Dringlichkeit" (jeweils hoch/mittel/niedrig) und ordne Prioritaeten P1–P5 zu.

**Aufgabe 8:** Nenne vier typische Bestandteile einer SOP und erklaere, warum Versionskontrolle wichtig ist.

---
---

# Loesungen

## Aufgabe 1
- **Funktionale Eskalation:** Weiterleitung an eine hoeher qualifizierte Stelle mit mehr Fachwissen. Beispiel: Der 1st Level Support kann ein Netzwerkproblem nicht loesen und leitet das Ticket an den 2nd Level (Netzwerk-Admin) weiter.
- **Hierarchische Eskalation:** Weiterleitung an einen Vorgesetzten, z.B. weil ein SLA gefaehrdet ist. Beispiel: Ein P1-Incident ist nach 3 Stunden immer noch nicht geloest (SLA: 4 h). Der Teamleiter wird informiert, um zusaetzliche Ressourcen freizugeben.

## Aufgabe 2
a) Kategorie: **Software / E-Mail**. Auswirkung: gering (nur ein Nutzer betroffen). Dringlichkeit: mittel. → **Prioritaet P4 (Niedrig)**.

b) Naechste Schritte:
1. Ticket erstellen mit Beschreibung, Nutzername, Fehlermeldung
2. Profil des Nutzers pruefen: Postfach voll? Sendebeschraenkung aktiv?
3. Outlook-Konfiguration pruefen: SMTP-Server korrekt? Passwort gueltig?
4. Testmail aus Webmail versenden → funktioniert? → Outlook-Problem
5. Ggf. Outlook-Profil neu anlegen oder Client-Einstellungen korrigieren
6. Loesung dokumentieren, Ticket schliessen, Nutzer informieren

## Aufgabe 3
a)
```
Gesamte Ausfallzeit: 3 h + 5 h = 8 h = 480 min
Gesamtzeit: 30 * 24 * 60 = 43.200 min
Verfuegbarkeit: (43.200 - 480) / 43.200 = 42.720 / 43.200 = 98,89 %
→ SLA (99,9 %) NICHT eingehalten (max. erlaubt: 43,2 min = 0,72 h)
```

b) SLA-Verstoesse:
- **INC-102 Reaktionszeit:** 20 min statt max. 15 min → **verletzt**
- **INC-102 Loesungszeit:** 5 h statt max. 4 h → **verletzt**
- **Verfuegbarkeit:** 98,89 % statt 99,9 % → **verletzt**
- INC-101: Reaktion (10 min < 15 min ✓) und Loesung (3 h < 4 h ✓) eingehalten

## Aufgabe 4
- **1st Level (Service Desk):** Nimmt Stoerungsmeldungen entgegen, erstellt Tickets, klassifiziert nach Prioritaet, loest Standardprobleme (Passwort-Reset, Druckerproblem), leitet komplexere Faelle weiter.
- **2nd Level (Fachteam):** Bearbeitet technisch anspruchsvollere Probleme (Server-Administration, Netzwerkkonfiguration, Firewall-Regeln). Analysiert tiefer, nutzt Admin-Tools und CLI.
- **3rd Level (Experten/Hersteller):** Behebt Probleme, die Spezialwissen oder Zugang zum Quellcode erfordern (Softwarefehler, Firmware-Bugs, Hardware-RMA). Oft externer Hersteller-Support.

## Aufgabe 5
1. **Incident:** Der Druckerserver ist nicht erreichbar. Nutzer koennen nicht drucken. → Sofort-Massnahme: Server neustarten (Workaround).
2. **Problem:** Die Ursache wird untersucht. Ergebnis: Ein Memory Leak im Druckertreiber fuehrt bei hoher Last zum Absturz. → Problem wird im Problem Management dokumentiert.
3. **Change:** Der Druckertreiber wird auf eine neue Version aktualisiert. → Change Request erstellen, genehmigen, Update im Wartungsfenster durchfuehren.

## Aufgabe 6
```
SOP: Passwort-Reset im Active Directory

1. Identitaet des Nutzers pruefen (Personalausweis, Rueckruf auf bekannte Nummer, 
   oder persoenliches Erscheinen)
2. Active Directory Benutzer und Computer oeffnen (dsa.msc)
3. Nutzerkonto suchen (nach Name oder Login)
4. Rechtsklick → Kennwort zuruecksetzen
5. Neues temporaeres Passwort setzen + Haken bei "Benutzer muss Kennwort bei 
   naechster Anmeldung aendern"
6. Temporaeres Passwort dem Nutzer sicher mitteilen (persoenlich oder telefonisch, 
   NICHT per E-Mail)
7. Ticket dokumentieren (wer, wann, warum)
8. Ticket schliessen
```

## Aufgabe 7

| | Dringlichkeit hoch | Dringlichkeit mittel | Dringlichkeit niedrig |
|---|---|---|---|
| **Auswirkung hoch** | P1 – Kritisch | P2 – Hoch | P3 – Mittel |
| **Auswirkung mittel** | P2 – Hoch | P3 – Mittel | P4 – Niedrig |
| **Auswirkung niedrig** | P3 – Mittel | P4 – Niedrig | P5 – Gering |

Die Prioritaet ergibt sich aus der Kombination von Auswirkung (wie viele Nutzer/Systeme betroffen) und Dringlichkeit (wie schnell muss reagiert werden).

## Aufgabe 8
Vier typische Bestandteile: (1) **Zweck** – Warum existiert die SOP? (2) **Voraussetzungen** – Was muss vorhanden sein? (3) **Schritte** – Nummerierte Anleitung. (4) **Verifizierung** – Wie wird der Erfolg geprueft?

**Versionskontrolle** ist wichtig, weil sich IT-Systeme aendern (Updates, neue Konfigurationen). Eine veraltete SOP kann zu Fehlern fuehren. Durch Versionsnummer und Datum ist nachvollziehbar, ob die SOP noch aktuell ist. Bei Aenderungen wird eine neue Version erstellt und die alte archiviert.
