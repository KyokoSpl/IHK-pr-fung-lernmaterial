# Grundlagen: 2.4.02 – Praeventive IT-Sicherheitsmassnahmen

## Massnahmen gegen Datendiebstahl

**Definition:** Datendiebstahl ist der unbefugte Zugriff auf vertrauliche Informationen mit dem Ziel, diese zu kopieren, weiterzugeben oder zu missbrauchen.

**Angriffsvektoren:**

| Angriffsvektor | Beschreibung | Beispiel |
|---|---|---|
| Netzwerkangriff | Abfangen von Daten im Netzwerk | Man-in-the-Middle, Sniffing |
| Physischer Zugriff | Direkter Zugang zum Geraet | USB-Stick, gestohlener Laptop |
| Insider-Bedrohung | Mitarbeiter mit boesen Absichten | Datenexfiltration per Cloud-Upload |
| Schwachstelle | Ausnutzen von Software-Luecken | SQL-Injection, Zero-Day-Exploit |
| Social Engineering | Manipulation von Personen | CEO-Fraud, Pretexting |

**Praeventive Massnahmen:**

| Massnahme | Beschreibung |
|---|---|
| Verschluesselung | Daten im Ruhezustand (AES-256) und bei Uebertragung (TLS 1.3) verschluesseln |
| Zugriffskontrolle (ACL) | Prinzip der minimalen Rechte (Least Privilege) anwenden |
| DLP (Data Loss Prevention) | Software erkennt und verhindert unerlaubten Datenabfluss |
| Firewall/IDS/IPS | Netzwerkverkehr ueberwachen und filtern |
| VPN | Verschluesselte Verbindung fuer Remote-Zugriff |
| USB-Port-Sperre | Physische Schnittstellen deaktivieren oder kontrollieren |
| Netzwerksegmentierung | Sensible Bereiche vom allgemeinen Netzwerk trennen |
| Protokollierung | Zugriffe auf sensible Daten loggen und auswerten |

---

## Massnahmen gegen Identitaetsdiebstahl (Phishing)

**Definition:** Phishing ist eine Form des Social Engineering, bei der Angreifer durch gefaelschte E-Mails, Webseiten oder Nachrichten vertrauliche Zugangsdaten oder persoenliche Informationen stehlen.

**Phishing-Varianten:**

| Variante | Beschreibung |
|---|---|
| E-Mail-Phishing | Massenhaft versandte gefaelschte E-Mails mit schadhaften Links |
| Spear-Phishing | Gezielter Angriff auf eine bestimmte Person oder Abteilung |
| CEO-Fraud / Whaling | Angreifer gibt sich als Geschaeftsfuehrung aus |
| Smishing | Phishing per SMS |
| Vishing | Phishing per Telefonanruf |
| Pharming | DNS-Manipulation leitet auf gefaelschte Webseite um |

**Praeventive Massnahmen:**

| Massnahme | Beschreibung |
|---|---|
| Security-Awareness-Schulung | Regeln fuer Mitarbeiter, Erkennung verdaechtiger E-Mails |
| Multi-Faktor-Authentifizierung (MFA) | Zweiter Faktor (z.B. TOTP, Hardware-Token) neben Passwort |
| E-Mail-Sicherheit | SPF, DKIM, DMARC zur Absenderverifizierung |
| Spamfilter | Automatische Erkennung und Quarantaene verdaechtiger Mails |
| Passworterstaerkung | Passwoerter: mind. 12 Zeichen, komplex, keine Wiederverwendung |
| Passwort-Manager | Sichere Speicherung und Generierung von Passwoertern |
| Linkpruefung | URL vor dem Klicken pruefen (Hover, Sandbox-Umgebung) |
| Reporting-Prozess | Mitarbeiter koennen verdaechtige E-Mails einfach melden |

**Erkennungsmerkmale von Phishing-Mails:**
- Unbekannter oder gefaelschter Absender
- Dringlichkeit / Zeitdruck („Ihr Konto wird gesperrt!")
- Rechtschreib- und Grammatikfehler
- Verdaechtige Links (URL pruefen!)
- Ungewoehnliche Anhaenge (.exe, .zip, .docm)
- Unpersoenliche Anrede

---

## Massnahmen gegen digitale Erpressung (Ransomware)

**Definition:** Ransomware ist Schadsoftware, die Dateien oder ganze Systeme verschluesselt und Loesegeld fuer die Entschluesselung fordert.

**Angriffskette (Kill Chain):**

| Phase | Beschreibung |
|---|---|
| 1. Infektion | Phishing-Mail, Drive-by-Download, RDP-Schwachstelle |
| 2. Ausfuehrung | Malware wird installiert, Rechte werden eskaliert |
| 3. Ausbreitung | Lateral Movement im Netzwerk |
| 4. Verschluesselung | Dateien werden verschluesselt, Backups geloescht |
| 5. Erpressung | Loesegeldforderung (oft in Kryptowaehrung) |

**Praeventive Massnahmen:**

| Massnahme | Beschreibung |
|---|---|
| Backup-Strategie | 3-2-1-Regel, offline/air-gapped Backup |
| Patch-Management | Betriebssysteme und Software zeitnah aktualisieren |
| Endpoint Detection & Response (EDR) | Verhaltensbasierte Erkennung von Schadsoftware |
| Netzwerksegmentierung | Ausbreitung (Lateral Movement) verhindern |
| Least Privilege | Nutzer nur minimale Rechte vergeben |
| Application Whitelisting | Nur freigegebene Programme ausfuehren lassen |
| RDP-Absicherung | RDP deaktivieren oder nur per VPN + MFA zugaenglich |
| E-Mail-Scanner | Anhaenge in Sandbox pruefen, Makros blockieren |
| Notfallplan | Incident-Response-Plan mit definierten Rollen und Ablaeufen |

**Wichtig:** Kein Loesegeld zahlen! (Empfehlung BSI) – Keine Garantie fuer Entschluesselung, foerdert kriminelles Geschaeftsmodell.

## Querverweise
- → 1.6.01 (Schutzziele: Vertraulichkeit, Integritaet, Verfuegbarkeit)
- → 2.4.01 (Schadenspotenziale bewerten)
- → 2.4.04 (Kundenberatung zur IT-Sicherheit)
