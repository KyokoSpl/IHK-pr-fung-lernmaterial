# Grundlagen: 2.4.05 – Tools zur Ueberpruefung von IT-Sicherheitsmassnahmen

## Device Security Check

**Definition:** Systematische Ueberpruefung von Endgeraeten (PCs, Laptops, Smartphones, Server) auf Einhaltung definierter Sicherheitsstandards.

**Pruefbereiche:**

| Pruefbereich | Was wird geprueft? | Tool/Methode |
|---|---|---|
| Patch-Status | Sind Betriebssystem und Software aktuell? | WSUS, SCCM, Patch-Management-Tools |
| Virenscanner | Ist Antivirus installiert und aktuell? | Endpoint-Protection-Konsole |
| Verschluesselung | Ist die Festplatte verschluesselt? | BitLocker, FileVault, LUKS |
| Firewall | Ist die lokale Firewall aktiv? | Windows Defender Firewall, iptables |
| Konfiguration | Entspricht die Konfiguration der Richtlinie? | Gruppenrichtlinien (GPO), MDM |
| USB-Ports | Sind nicht autorisierte Geraete gesperrt? | Device Control, GPO |
| Passwoerter | Erfuellt das Passwort die Richtlinie? | Active Directory Passwort-Policy |

**Mobile Device Management (MDM):**

| Funktion | Beschreibung |
|---|---|
| Geraeteregistrierung | Nur verwaltete Geraete erhalten Zugang |
| Konfigurationsprofile | WLAN, VPN, E-Mail automatisch konfigurieren |
| Compliance-Check | Pruefen, ob Geraet Richtlinien erfuellt (z.B. PIN, Verschluesselung) |
| Remote Wipe | Geraet bei Verlust aus der Ferne loeschen |
| App-Management | Nur freigegebene Apps erlauben |
| Beispiele | Microsoft Intune, VMware Workspace ONE, Jamf |

---

## Identity & Access Management (IAM)

**Definition:** IAM umfasst Prozesse und Technologien zur Verwaltung digitaler Identitaeten und deren Zugriffsrechte auf IT-Ressourcen.

**IAM-Kernfunktionen:**

| Funktion | Beschreibung |
|---|---|
| Authentifizierung | Identitaet verifizieren (Wer bist du?) |
| Autorisierung | Rechte pruefen (Was darfst du?) |
| Provisioning | Benutzerkonten erstellen, aendern, loeschen |
| De-Provisioning | Konten bei Austritt sofort deaktivieren |
| Single Sign-On (SSO) | Ein Login fuer mehrere Anwendungen |
| Multi-Faktor-Authentifizierung (MFA) | Zwei oder mehr Faktoren zur Verifizierung |
| Audit / Logging | Zugriffe protokollieren und auswerten |

**Zugriffsmodelle:**

| Modell | Beschreibung | Einsatz |
|---|---|---|
| RBAC (Role-Based Access Control) | Rechte werden Rollen zugewiesen, Nutzer erhalten Rollen | Standard in Unternehmen |
| DAC (Discretionary Access Control) | Eigentuemer bestimmt Zugriffsrechte | Dateisysteme (NTFS) |
| MAC (Mandatory Access Control) | Systemweite Regeln, nicht durch Nutzer aenderbar | Militaer, Regierung |
| ABAC (Attribute-Based Access Control) | Rechte basierend auf Attributen (Abteilung, Standort, Zeit) | Cloud, komplexe Umgebungen |

**Verzeichnisdienste:**

| Dienst | Beschreibung |
|---|---|
| Active Directory (AD) | Microsoft: Verzeichnisdienst fuer Windows-Domaenen |
| LDAP | Lightweight Directory Access Protocol – offener Standard |
| Azure AD / Entra ID | Cloud-basierter Verzeichnisdienst (Microsoft 365) |
| Kerberos | Authentifizierungsprotokoll in AD-Umgebungen |

---

## Penetrations-Test

**Definition:** Ein Penetrationstest (Pentest) ist ein kontrollierter, autorisierter Angriff auf IT-Systeme mit dem Ziel, Schwachstellen zu identifizieren, bevor echte Angreifer sie ausnutzen.

**Testtypen:**

| Typ | Informationslage | Beschreibung |
|---|---|---|
| White Box | Vollstaendig (Quellcode, Architektur, Zugangsdaten) | Umfassendster Test, Tester kennt alles |
| Grey Box | Teilweise (z.B. Benutzerzugang, keine Admin-Rechte) | Realistisch fuer internen Angreifer |
| Black Box | Keine Vorinformationen | Simuliert externen Angreifer, realistisch |

**Pentest-Phasen:**

| Phase | Beschreibung |
|---|---|
| 1. Planung & Beauftragung | Scope definieren, rechtliche Genehmigung einholen |
| 2. Informationsbeschaffung | Reconnaissance: DNS, Portscan, OSINT |
| 3. Schwachstellenidentifikation | Automatisierte Scans + manuelle Pruefung |
| 4. Ausnutzung (Exploitation) | Schwachstellen aktiv ausnutzen (kontrolliert) |
| 5. Post-Exploitation | Rechteeskalation, Lateral Movement pruefen |
| 6. Reporting | Bericht mit Findings, Risikobewertung und Empfehlungen |

**Pentest-Tools (Beispiele):**

| Tool | Funktion |
|---|---|
| Kali Linux | Spezialisierte Linux-Distribution fuer Pentests |
| Metasploit | Framework fuer Exploitation und Post-Exploitation |
| Burp Suite | Proxy fuer Web-Application-Tests |
| Nmap | Netzwerk-Scanner (Ports, Dienste, OS-Erkennung) |
| Wireshark | Netzwerkprotokoll-Analyse |
| OWASP ZAP | Open-Source Web-Application-Scanner |

**Wichtig:** Pentests duerfen **nur mit schriftlicher Genehmigung** durchgefuehrt werden. Ungenehmigtes Testen ist strafbar (§ 202a-c StGB).

---

## Schwachstellenanalyse

**Definition:** Systematische, meist automatisierte Suche nach bekannten Sicherheitsluecken (Vulnerabilities) in IT-Systemen, Software und Konfigurationen.

**Unterschied Schwachstellenanalyse vs. Pentest:**

| Kriterium | Schwachstellenanalyse | Penetrationstest |
|---|---|---|
| Tiefe | Oberflaeche (bekannte Schwachstellen) | Tiefgehend (aktive Ausnutzung) |
| Automatisierung | Hoch (Scanner) | Gering (manuell + automatisiert) |
| Risiko | Gering (kein Eingriff) | Mittel (kontrollierter Angriff) |
| Haeufigkeit | Regelmaessig (woechentlich/monatlich) | Jaehrlich oder anlassbezogen |
| Kosten | Gering | Hoch (Spezialist noetig) |

**Schwachstellenquellen:**

| Quelle | Beschreibung |
|---|---|
| CVE (Common Vulnerabilities and Exposures) | Oeffentliche Datenbank bekannter Schwachstellen |
| CVSS (Common Vulnerability Scoring System) | Bewertungssystem fuer Schwere einer Schwachstelle (0-10) |
| NVD (National Vulnerability Database) | US-Datenbank mit CVE-Details und CVSS-Werten |
| BSI-Warnungen | Warnmeldungen und Empfehlungen des BSI |

**CVSS-Bewertung:**

| Score | Schweregrad |
|---|---|
| 0.0 | Keine |
| 0.1 – 3.9 | Niedrig |
| 4.0 – 6.9 | Mittel |
| 7.0 – 8.9 | Hoch |
| 9.0 – 10.0 | Kritisch |

**Tools fuer Schwachstellenanalyse:**

| Tool | Beschreibung |
|---|---|
| Nessus | Kommerzieller Schwachstellenscanner (Tenable) |
| OpenVAS | Open-Source-Schwachstellenscanner |
| Qualys | Cloud-basierter Scanner |
| Nikto | Webserver-Schwachstellenscanner |
| OWASP Dependency-Check | Prueft Abhaengigkeiten auf bekannte Schwachstellen |

## Querverweise
- → 1.6.04 (Sicherheitskonzept – Massnahmenplanung)
- → 2.4.04 (TOM, Risikoanalyse)
- → 2.4.06 (Wirksamkeit der TOM pruefen)
