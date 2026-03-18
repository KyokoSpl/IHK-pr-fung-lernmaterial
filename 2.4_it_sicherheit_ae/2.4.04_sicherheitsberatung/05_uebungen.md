# Uebungen: 2.4.04 – Kunden zur IT-Sicherheit beraten

## Bedrohungsszenarien

**Aufgabe 1:** Erklaere den Ablauf einer SQL-Injection anhand eines Login-Formulars. Welche Eingabe koennte ein Angreifer nutzen? Nenne zwei Gegenmassnahmen.

**Aufgabe 2:** Ein Onlineshop ist durch einen DDoS-Angriff 6 Stunden nicht erreichbar. Welches Schutzziel ist verletzt? Nenne drei technische Gegenmassnahmen.

---

## Risikoanalyse

**Aufgabe 3:** Fuehre eine vereinfachte Risikoanalyse fuer folgendes Szenario durch: Ein Handwerksbetrieb (15 Mitarbeiter) nutzt ein NAS fuer alle Firmendokumente. Es gibt kein Backup. Zwei Mitarbeiter nutzen private Smartphones fuer Firmen-E-Mails (BYOD). Erstelle eine Risikotabelle mit mindestens drei Risiken (Asset, Bedrohung, Wahrscheinlichkeit, Schaden, Massnahme).

**Aufgabe 4:** Nenne die vier Strategien zur Risikobehandlung und gib je ein Beispiel aus dem IT-Bereich.

---

## Kundengruppen

**Aufgabe 5:** Ein Verein mit 200 Mitgliedern moechte eine Mitglieder-Datenbank betreiben. Welche drei datenschutzrechtlichen Anforderungen musst du in der Beratung ansprechen?

**Aufgabe 6:** Vergleiche die IT-Sicherheitsberatung fuer (a) einen privaten Haushalt und (b) eine Behoerde anhand von drei Kriterien (z.B. Budget, Regulierung, Massnahmen).

---

## TOM

**Aufgabe 7:** Ordne die folgenden Massnahmen den TOM-Kategorien zu: (a) Chipkarte am Eingang, (b) AES-256-Verschluesselung, (c) Passwortrichtlinie mit MFA, (d) VPN fuer Homeoffice, (e) RAID 6 im Server.

**Aufgabe 8:** Ein Kunde fragt: „Reicht eine Firewall als IT-Sicherheitsmassnahme?" Verfasse eine begruendete Antwort mit Verweis auf das Defense-in-Depth-Prinzip.

---

## Rahmenbedingungen

**Aufgabe 9:** Nenne je ein Beispiel fuer eine technologische, organisatorische, rechtliche und ethische Rahmenbedingung bei der Einfuehrung einer Videoabsicherung in einem Buerogebaeude.

**Aufgabe 10:** Ein Unternehmen plant, KI-basierte Verhaltensanalyse zur Erkennung von Insider-Bedrohungen einzusetzen. Nenne zwei ethische Bedenken und erklaere, wie diese adressiert werden koennen.

---
---

# Loesungen

## Aufgabe 1
**Ablauf:** Das Login-Formular sendet Benutzername und Passwort an den Server. Dort wird eine SQL-Abfrage erstellt: `SELECT * FROM users WHERE name='EINGABE' AND pw='EINGABE'`. Der Angreifer gibt als Benutzername ein: `' OR 1=1 --`. Dadurch wird die Bedingung immer wahr, und der Angreifer erhaelt Zugang. **Gegenmassnahmen:** (1) Prepared Statements / Parameterized Queries – Eingabe wird als Daten behandelt, nicht als SQL-Code. (2) Input Validation – nur erlaubte Zeichen akzeptieren (Whitelist).

## Aufgabe 2
**Verletztes Schutzziel:** Verfuegbarkeit. **Gegenmassnahmen:** (1) DDoS-Mitigation-Dienst (z.B. Cloudflare, AWS Shield). (2) Content Delivery Network (CDN) zur Lastverteilung. (3) Rate Limiting – Anzahl der Anfragen pro IP begrenzen. Zusaetzlich: Redundante Infrastruktur, Notfallplan.

## Aufgabe 3

| Asset | Bedrohung | Wahrscheinlichkeit | Schaden | Risiko | Massnahme |
|---|---|---|---|---|---|
| NAS (Firmendokumente) | Ransomware/Hardwaredefekt | Hoch | Sehr hoch | Kritisch | 3-2-1-Backup einfuehren |
| Smartphones (BYOD) | Datenverlust bei Verlust/Diebstahl | Mittel | Hoch | Hoch | MDM-Loesung, Remote Wipe |
| E-Mail-Zugang | Phishing | Hoch | Mittel | Hoch | MFA aktivieren, Awareness-Schulung |

## Aufgabe 4
(1) **Vermeiden:** Einen unsicheren FTP-Server abschalten und durch SFTP ersetzen. (2) **Vermindern:** Firewall und EDR installieren, um die Eintrittswahrscheinlichkeit von Angriffen zu senken. (3) **Uebertragen:** Cyber-Versicherung abschliessen, die Schaeden durch Ransomware abdeckt. (4) **Akzeptieren:** Das Restrisiko eines sehr unwahrscheinlichen Meteoriteneinschlags wird bewusst akzeptiert.

## Aufgabe 5
(1) **Rechtsgrundlage:** Verarbeitung der Mitgliederdaten benoetigt eine Rechtsgrundlage (Art. 6 DSGVO), z.B. Vertragserfuellung (Mitgliedschaft) oder Einwilligung. (2) **Datensparsamkeit:** Nur die Daten erheben, die fuer die Vereinsverwaltung noetig sind (Name, Kontakt, Beitragsstatus). (3) **TOM:** Technisch-organisatorische Massnahmen zum Schutz der Daten (Zugangskontrolle zur Datenbank, Verschluesselung, Backup, Berechtigungskonzept).

## Aufgabe 6

| Kriterium | Privater Haushalt | Behoerde |
|---|---|---|
| Budget | Gering (100-500 EUR) | Haushaltsmittel, groesseres Budget |
| Regulierung | Allgemeine DSGVO | BSI IT-Grundschutz, KRITIS, NIS2, Vergaberecht |
| Massnahmen | Router-Sicherheit, Virenscanner, Passwort-Manager | ISMS, IT-Grundschutz-Zertifizierung, EDR, SIEM |

## Aufgabe 7
(a) Chipkarte am Eingang → **Zutrittskontrolle** (physischer Zutritt zum Gebaeude). (b) AES-256-Verschluesselung → **Zugriffskontrolle** (Schutz der Daten vor unbefugtem Zugriff). (c) Passwortrichtlinie mit MFA → **Zugangskontrolle** (Zugang zum IT-System). (d) VPN fuer Homeoffice → **Weitergabekontrolle** (sichere Datenuebertragung). (e) RAID 6 im Server → **Verfuegbarkeitskontrolle** (Schutz vor Datenverlust bei Festplattenausfall).

## Aufgabe 8
Nein, eine Firewall allein reicht nicht. Das **Defense-in-Depth-Prinzip** (Verteidigung in der Tiefe) besagt, dass mehrere unabhaengige Sicherheitsschichten noetig sind. Wenn eine Schicht versagt, schuetzen die anderen. Neben der Firewall braucht man: Virenscanner/EDR, Patch-Management, MFA, Zugriffskontrolle (Least Privilege), Backup-Strategie, Awareness-Schulungen und einen Incident-Response-Plan. Die Firewall schuetzt nur den Netzwerkperimeter – interne Bedrohungen, Phishing und physische Angriffe werden nicht abgedeckt.

## Aufgabe 9
**Technologisch:** Kameraaufloesung, Speicherkapazitaet, Netzwerkanbindung. **Organisatorisch:** Regelung, wer Zugriff auf die Aufnahmen hat, Aufbewahrungsdauer. **Rechtlich:** DSGVO (Datenschutz-Folgenabschaetzung noetig), Kennzeichnungspflicht (Hinweisschilder), Betriebsratsvereinbarung. **Ethisch:** Verhaeltnismaessigkeit (keine Ueberwachung von Pausen-/Toilettenraeumen), Transparenz gegenueber Mitarbeitern.

## Aufgabe 10
**Ethische Bedenken:** (1) **Privatsphaere:** Verhaltensanalyse wertet das Verhalten aller Mitarbeiter aus, auch unverdaechtiger – Eingriff in Persoenlichkeitsrechte. (2) **Diskriminierung/Bias:** KI koennte bestimmte Verhaltensweisen falsch als verdaechtig einstufen (z.B. Nachtarbeit = verdaechtig). **Adressierung:** (1) Transparente Information der Mitarbeiter (Betriebsvereinbarung), Datenschutz-Folgenabschaetzung, nur anonymisierte Auswertung. (2) Regelmaessige Pruefung der KI auf Bias, Entscheidungen nicht vollautomatisch treffen (Mensch-im-Loop-Prinzip).
