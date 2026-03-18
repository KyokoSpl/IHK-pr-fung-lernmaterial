# Uebungen: 2.4.06 – Wirksamkeit und Effizienz der umgesetzten TOM pruefen

## Zutritts-, Zugangs- und Zugriffskontrolle

**Aufgabe 1:** Ordne die folgenden Massnahmen den Kategorien Zutrittskontrolle, Zugangskontrolle oder Zugriffskontrolle zu:
(a) Alarmanlage im Serverraum
(b) Passwortrichtlinie mit MFA
(c) Rollenbasiertes Berechtigungskonzept (RBAC)
(d) Besucherausweise am Empfang
(e) AES-256-Verschluesselung der Festplatte
(f) Bildschirmsperre nach 5 Minuten

**Aufgabe 2:** Erklaere den Unterschied zwischen Zutritts-, Zugangs- und Zugriffskontrolle mit je einem konkreten Beispiel aus einem Buerogebaeude.

---

## Log Management und SIEM

**Aufgabe 3:** Ein SIEM-System zeigt folgende Ereignisse:
- 03:22 Uhr: 150 fehlgeschlagene Login-Versuche auf einen Webserver (verschiedene Benutzernamen, gleiche IP)
- 03:25 Uhr: Erfolgreicher Login als „admin"
- 03:27 Uhr: Datenbank-Export (5 GB) gestartet

(a) Welche Art von Angriff liegt vermutlich vor?
(b) Welche Sofortmassnahmen sollten ergriffen werden?
(c) Welche TOM haette den Angriff verhindern oder erschweren koennen?

**Aufgabe 4:** Nenne vier verschiedene Log-Quellen in einem Unternehmen und erklaere, welche sicherheitsrelevanten Informationen jeweils erfasst werden.

---

## Compliance Reports

**Aufgabe 5:** Erklaere den Unterschied zwischen einem internen und einem externen Audit. Nenne je einen Vorteil.

**Aufgabe 6:** Ein Compliance Report zeigt, dass 30% der Mitarbeiter-PCs keine aktuelle Antivirus-Software haben. Welche Massnahmen schlaegest du vor? Nenne drei konkrete Schritte.

---

## Biometrie und Verschluesselung

**Aufgabe 7:** Ein Unternehmen erwaegt, Fingerabdruckscanner fuer den Zugang zum Serverraum einzufuehren. Nenne zwei Vorteile und zwei Bedenken (inkl. Datenschutz).

**Aufgabe 8:** Erklaere den Unterschied zwischen Schnellformatierung, Ueberschreiben und physischer Vernichtung von Datentraegern. Welche Methode empfiehlst du fuer eine Festplatte mit Kundendaten?

---

## Wirksamkeitspruefung

**Aufgabe 9:** Bei einer jaehrlichen Pruefung der TOM werden 8 verwaiste Benutzerkonten gefunden (Mitarbeiter haben das Unternehmen bereits vor Monaten verlassen). (a) Welche Zugriffskontroll-Massnahme wurde versaeumt? (b) Welches Risiko besteht? (c) Welchen Prozess sollte das Unternehmen einfuehren?

**Aufgabe 10:** Erstelle eine vereinfachte Berechtigungsmatrix fuer ein kleines Unternehmen mit den Rollen: Geschaeftsfuehrung, Entwickler, Personalabteilung und Praktikant. Die Ressourcen sind: Quellcode, Personalakten, Finanzdaten und E-Mail.

---
---

# Loesungen

## Aufgabe 1
(a) Alarmanlage → **Zutrittskontrolle** (schuetzt physischen Raum). (b) Passwortrichtlinie + MFA → **Zugangskontrolle** (schuetzt Login zum System). (c) RBAC → **Zugriffskontrolle** (regelt, wer auf welche Daten zugreifen darf). (d) Besucherausweise → **Zutrittskontrolle** (regelt physischen Zutritt). (e) AES-256-Verschluesselung → **Zugriffskontrolle** (schuetzt Daten vor unbefugtem Lesen). (f) Bildschirmsperre → **Zugangskontrolle** (verhindert unbefugten System-Zugang).

## Aufgabe 2
**Zutrittskontrolle:** Chipkarten-Zugang am Eingang des Buerogebaeudes – nur Mitarbeiter mit gueltigem Ausweis koennen das Gebaeude betreten. **Zugangskontrolle:** Passwort + MFA am Arbeitsplatz-PC – nur mit gueltigem Login kann das Betriebssystem gestartet werden. **Zugriffskontrolle:** Rollenbasierte Berechtigungen – ein Mitarbeiter der Buchhaltung hat Zugriff auf Finanzdaten, aber nicht auf Personalakten.

## Aufgabe 3
(a) **Brute-Force-Angriff** auf den Webserver (systematisches Durchprobieren von Benutzernamen/Passwoertern), gefolgt von **Datenexfiltration** nach erfolgreichem Login. (b) **Sofortmassnahmen:** IP-Adresse des Angreifers sperren, Admin-Konto deaktivieren, Passwort aendern, Datenbank-Export stoppen/pruefen, Server isolieren, Vorfall dokumentieren, IT-Sicherheitsbeauftragten informieren. (c) **TOM:** Account-Lockout nach 5 Fehlversuchen, MFA fuer Admin-Konten, Rate Limiting, keine Standard-Benutzernamen wie „admin", Web Application Firewall (WAF), Netzwerksegmentierung.

## Aufgabe 4
(1) **Firewall-Logs:** Blockierte und erlaubte Verbindungen, Quell- und Ziel-IP, Ports, Protokolle – erkennt Angriffsversuche von aussen. (2) **Active-Directory-Logs:** Benutzeranmeldungen, Kontoaenderungen, Gruppenmitgliedschaften – erkennt unbefugte Kontoaenderungen. (3) **Webserver-Logs:** HTTP-Requests, Statuscodes (403, 404), IP-Adressen – erkennt Schwachstellen-Scans und Angriffsversuche. (4) **Datenbank-Logs:** Abfragen, Aenderungen, fehlgeschlagene Zugriffe – erkennt SQL-Injection und unbefugte Datenabfragen.

## Aufgabe 5
**Internes Audit:** Wird von der eigenen IT-/Sicherheitsabteilung durchgefuehrt. Vorteil: Schnell durchfuehrbar, kostenguenstig, internes Know-how. **Externes Audit:** Wird von unabhaengigen, zertifizierten Auditoren durchgefuehrt (z.B. fuer ISO 27001). Vorteil: Objektiv und unvoreingenommen, anerkanntes Zertifikat, hoehere Glaubwuerdigkeit gegenueber Kunden und Partnern.

## Aufgabe 6
(1) **Automatisiertes Deployment:** Antivirussoftware ueber Softwareverteilung (SCCM, Intune) zentral auf allen PCs installieren und aktualisieren. (2) **Compliance-Richtlinie:** PCs ohne aktuelle AV-Software automatisch sperren (Conditional Access / NAC – Network Access Control). (3) **Monitoring:** Regelmaessigen Compliance-Scan einrichten, der den AV-Status woechentlich prueft und nicht-konforme Geraete meldet.

## Aufgabe 7
**Vorteile:** (1) Hohe Sicherheit – Fingerabdruck ist einzigartig und schwer zu faelschen. (2) Komfort – kein Passwort/Chipkarte noetig, schnelle Authentifizierung. **Bedenken:** (1) **Datenschutz (DSGVO Art. 9):** Biometrische Daten sind besondere Kategorien personenbezogener Daten – Einwilligung oder betriebliche Erforderlichkeit noetig, strenge Schutzmassnahmen fuer die gespeicherten Daten. (2) **Faelschbarkeit:** Fingerabdruecke koennen mit Attrappen nachgebildet werden – nicht als alleiniger Faktor verwenden (besser als Teil von MFA: Fingerabdruck + PIN).

## Aufgabe 8
**Schnellformatierung:** Loescht nur das Dateisystem/Inhaltsverzeichnis, die eigentlichen Daten bleiben auf dem Datentraeger erhalten und koennen mit Recovery-Tools wiederhergestellt werden. **Unsicher.** **Ueberschreiben:** Alle Sektoren des Datentraegers werden ein- oder mehrfach mit Zufallsdaten ueberschrieben. Wiederherstellung ist praktisch nicht moeglich. **Sicher** (1-3 Durchgaenge genuegen, z.B. mit DBAN). **Physische Vernichtung:** Datentraeger wird mechanisch zerstoert (Shredder) oder entmagnetisiert (Degausser). **Hoechste Sicherheit.** **Empfehlung fuer Kundendaten:** Mindestens Ueberschreiben (3 Durchgaenge). Bei sensiblen Daten (Gesundheit, Finanzen): physische Vernichtung mit Vernichtungsprotokoll.

## Aufgabe 9
(a) **De-Provisioning** wurde versaeumt – die Benutzerkonten haetten bei Austritt der Mitarbeiter sofort deaktiviert/geloescht werden muessen. (b) **Risiken:** Ehemalige Mitarbeiter koennten weiterhin auf Firmendaten zugreifen. Die verwaisten Konten koennten von Angreifern uebernommen werden (kein aktiver Nutzer bemerkt verdaechtige Aktivitaeten). (c) **Prozess:** Automatisierter Off-Boarding-Prozess: HR meldet Austritt → IT sperrt am letzten Arbeitstag alle Konten, entzieht Zugriffsrechte, zieht Hardware ein. Quartalsweiser IAM-Audit (Abgleich HR-Liste mit AD-Konten).

## Aufgabe 10

| Rolle | Quellcode | Personalakten | Finanzdaten | E-Mail |
|---|---|---|---|---|
| Geschaeftsfuehrung | Lesen | Lesen | Lesen/Schreiben | Vollzugriff |
| Entwickler | Lesen/Schreiben | Kein Zugriff | Kein Zugriff | Vollzugriff |
| Personalabteilung | Kein Zugriff | Lesen/Schreiben | Kein Zugriff | Vollzugriff |
| Praktikant | Lesen (nur Projekt) | Kein Zugriff | Kein Zugriff | Lesen/Senden |

Begruendung: Need-to-Know und Least Privilege – jede Rolle erhaelt nur die Rechte, die fuer ihre Aufgaben erforderlich sind.
