# Vertiefung und Uebungen: 2.4.05 – Tools zur Ueberpruefung von IT-Sicherheitsmassnahmen

## Vertiefung

### Vergleich der Pruefmethoden

| Kriterium | Device Security Check | IAM-Audit | Pentest | Schwachstellenanalyse |
|---|---|---|---|---|
| Fokus | Endgeraete | Identitaeten/Rechte | Gesamtsystem | Bekannte Schwachstellen |
| Tiefe | Konfiguration | Prozesse + Technik | Sehr tief (Exploitation) | Oberflaechlich (Scan) |
| Automatisierung | Hoch (MDM) | Mittel | Gering (manuell) | Hoch (Scanner) |
| Haeufigkeit | Kontinuierlich | Quartalsweise | Jaehrlich | Woechentlich/monatlich |
| Kosten | Teil der MDM-Lizenz | Mittel | Hoch | Gering–mittel |
| Ergebnis | Compliance-Status | Berechtigungsreport | Angriffsbericht | Schwachstellenliste |

### Zusammenwirken der Tools

```
+--------------------------------------------------+
|          IT-Sicherheitsueberpruefung              |
+--------------------------------------------------+
|                                                    |
|  Kontinuierlich        Regelmaessig   Anlassbezogen|
|  +--------------+      +----------+   +---------+ |
|  | Device       |      | Schwach- |   | Pene-   | |
|  | Security     |      | stellen- |   | trations-| |
|  | Check        |      | analyse  |   | test    | |
|  | (MDM)        |      | (Scanner)|   | (manuell)| |
|  +------+-------+      +-----+----+   +----+----+ |
|         |                     |              |      |
|         +----------+----------+--------------+      |
|                    |                                 |
|              +-----+------+                          |
|              | IAM-Audit  |                          |
|              | (Rechte    |                          |
|              |  pruefen)  |                          |
|              +-----+------+                          |
|                    |                                 |
|              +-----+------+                          |
|              | Reporting  |                          |
|              | & Massn.   |                          |
|              +------------+                          |
+--------------------------------------------------+
```

### Pentest-Phasen im Detail

```
+-------------------+
| 1. Planung        |  Scope, Regeln, Genehmigung
| (Rules of         |  (Was darf getestet werden?)
|  Engagement)      |
+--------+----------+
         |
         v
+--------+----------+
| 2. Reconnaissance |  Passive: OSINT, DNS, Whois
| (Informations-    |  Aktive: Nmap, Portscan
|  beschaffung)     |
+--------+----------+
         |
         v
+--------+----------+
| 3. Schwachstellen |  Scanner (Nessus, OpenVAS)
| identifizieren    |  + manuelle Analyse
+--------+----------+
         |
         v
+--------+----------+
| 4. Exploitation   |  Metasploit, Burp Suite
| (Ausnutzen)       |  SQL-Injection, XSS testen
+--------+----------+
         |
         v
+--------+----------+
| 5. Post-Exploita- |  Rechteeskalation?
| tion              |  Lateral Movement?
+--------+----------+
         |
         v
+--------+----------+
| 6. Reporting      |  Findings + Risikobewertung
|                   |  + Empfehlungen
+-------------------+
```

### IAM-Lifecycle

```
Eintritt           Wechsel            Austritt
+----------+       +----------+       +----------+
| Provisi- |       | Aendern  |       | De-Provi-|
| oning    |------>| (Rolle   |------>| sioning  |
| (Konto   |       |  wechselt|       | (Konto   |
|  anlegen)|       |  → Rechte|       |  sperren/|
|          |       |  anpassen|       |  loeschen|
+----------+       +----------+       +----------+
     |                  |                   |
     +------------------+-------------------+
                        |
                  +-----+------+
                  | Audit      |
                  | (Rechte    |
                  |  pruefen)  |
                  +------------+
```

### CVSS-Score Beispiele

| Schwachstelle | CVSS-Score | Schweregrad | Massnahme |
|---|---|---|---|
| Remote Code Execution (RCE) | 9.8 | Kritisch | Sofort patchen |
| SQL-Injection (authentifiziert) | 7.5 | Hoch | Kurzfristig beheben |
| Cross-Site Scripting (reflected) | 6.1 | Mittel | Im naechsten Release |
| Informationsleck (Versionsnummer) | 3.1 | Niedrig | Bei Gelegenheit |

### Typische Pruefungsaspekte
- Unterschied Schwachstellenanalyse vs. Penetrationstest benennen
- Pentest-Typen (White/Grey/Black Box) zuordnen koennen
- IAM-Begriffe erklaeren (SSO, RBAC, Provisioning, De-Provisioning)
- CVE und CVSS erklaeren koennen
- Device Security Check: Was wird geprueft? Tools benennen
- Rechtliche Grundlage fuer Pentests kennen (schriftliche Genehmigung)

### Haeufige Fehler
- Schwachstellenanalyse = Pentest → Schwachstellenanalyse findet nur bekannte Luecken, Pentest nutzt sie aus
- Black-Box-Test = besser als White Box → Beide haben Vor-/Nachteile, White Box ist gruendlicher
- IAM = nur Passwort-Reset → IAM umfasst den gesamten Identitaets-Lebenszyklus
- CVSS 10 = garantierter Angriff → CVSS bewertet die Schwere, nicht die Eintrittswahrscheinlichkeit
- Pentest ohne Genehmigung = erlaubt wenn intern → Immer schriftliche Genehmigung noetig (StGB)

---

## Uebungen

**Aufgabe 1:** Erklaere den Unterschied zwischen einer Schwachstellenanalyse und einem Penetrationstest anhand von drei Kriterien.

**Aufgabe 2:** Ein Unternehmen plant einen Pentest fuer seinen Onlineshop. Der Tester erhaelt nur die URL des Shops, keine weiteren Informationen. (a) Welcher Testtyp liegt vor? (b) Nenne zwei Vorteile und einen Nachteil dieses Testtyps.

**Aufgabe 3:** Ein Schwachstellenscanner meldet eine Luecke mit CVSS-Score 9.2. (a) Welchem Schweregrad entspricht das? (b) Welche Massnahme sollte sofort ergriffen werden? (c) Wo findest du Details zur Schwachstelle?

**Aufgabe 4:** In einem Unternehmen verlassen drei Mitarbeiter die Firma. Zwei Wochen spaeter stellt die IT fest, dass deren Konten noch aktiv sind. (a) Welches IAM-Problem liegt vor? (b) Welcher Prozess fehlt? (c) Welches Risiko besteht?

**Aufgabe 5:** Ein MDM-System meldet, dass 15 von 100 Firmen-Smartphones kein aktuelles Betriebssystem haben und bei 8 Geraeten die Festplattenverschluesselung deaktiviert ist. Welche Massnahmen empfiehlst du?

**Aufgabe 6:** Ordne die folgenden Tools der passenden Pruefmethode zu: (a) Nessus, (b) Microsoft Intune, (c) Metasploit, (d) Azure AD, (e) OpenVAS, (f) Burp Suite.

---
---

# Loesungen

## Aufgabe 1

| Kriterium | Schwachstellenanalyse | Penetrationstest |
|---|---|---|
| Tiefe | Oberflaeche – findet bekannte Schwachstellen | Tiefgehend – nutzt Schwachstellen aktiv aus |
| Methode | Automatisiert (Scanner) | Manuell + automatisiert (Spezialist) |
| Haeufigkeit | Regelmaessig (woechentlich/monatlich) | Selten (jaehrlich oder anlassbezogen) |

## Aufgabe 2
(a) **Black-Box-Test** – der Tester hat keine Vorinformationen ausser der URL. (b) **Vorteile:** (1) Realistisch – simuliert einen echten externen Angreifer. (2) Unvoreingenommen – Tester entdeckt Schwachstellen ohne Vorwissen. **Nachteil:** Weniger gruendlich – versteckte Schwachstellen (z.B. im Backend-Code) werden moeglicherweise nicht gefunden, da dem Tester der Quellcode fehlt.

## Aufgabe 3
(a) **Kritisch** (Score 9.0–10.0). (b) **Sofort patchen** oder den betroffenen Dienst voruebergehend abschalten, bis ein Patch verfuegbar ist. Ggf. Workaround anwenden und Vorfall an IT-Sicherheitsbeauftragten melden. (c) Details in der **CVE-Datenbank** (cve.org) oder der **NVD (National Vulnerability Database)**, alternativ BSI-Warnmeldungen.

## Aufgabe 4
(a) **Verwaiste Konten (Orphaned Accounts):** Benutzerkonten sind noch aktiv, obwohl die Mitarbeiter das Unternehmen verlassen haben. (b) **De-Provisioning-Prozess** fehlt: Bei Austritt muss das Benutzerkonto sofort deaktiviert/geloescht und alle Zugriffsrechte entzogen werden. (c) **Risiken:** Ehemalige Mitarbeiter koennten weiterhin auf Firmendaten zugreifen. Die Konten koennten von Angreifern uebernommen werden (kein aktiver Nutzer ueberwacht die Aktivitaet).

## Aufgabe 5
(1) **Erzwungenes Update:** Ueber das MDM-System ein Update-Fenster erzwingen. Bei Nichtbefolgung innerhalb einer Frist: Sperre des E-Mail/VPN-Zugangs. (2) **Compliance-Richtlinie:** Geraete ohne Verschluesselung als „nicht konform" markieren, Zugang zu Firmendaten automatisch sperren (Conditional Access). (3) **Nachfassen:** Betroffene Nutzer benachrichtigen, Schulung zur Geraetesicherheit. (4) **Langfristig:** Automatische Compliance-Checks im MDM konfigurieren, die Zugang nur bei erfuellten Kriterien erlauben.

## Aufgabe 6
(a) Nessus → **Schwachstellenanalyse** (Vulnerability Scanner). (b) Microsoft Intune → **Device Security Check** (MDM-System). (c) Metasploit → **Penetrationstest** (Exploitation Framework). (d) Azure AD → **Identity & Access Management** (Cloud-Verzeichnisdienst). (e) OpenVAS → **Schwachstellenanalyse** (Open-Source-Scanner). (f) Burp Suite → **Penetrationstest** (Web-Application-Proxy).
