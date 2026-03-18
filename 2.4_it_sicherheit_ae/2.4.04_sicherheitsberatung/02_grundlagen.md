# Grundlagen: 2.4.04 – Kunden zur IT-Sicherheit beraten

## Bedrohungsszenarien

**Definition:** Bedrohungsszenarien beschreiben typische Angriffsarten auf IT-Systeme, die als Grundlage fuer die Sicherheitsberatung dienen.

### Man-in-the-Middle (MITM)

**Funktionsweise:** Der Angreifer schaltet sich unbemerkt zwischen zwei Kommunikationspartner und kann Daten mitlesen oder manipulieren.

| Aspekt | Detail |
|---|---|
| Angriffsvektor | Netzwerk (WLAN, LAN) |
| Ziel | Abhoeren, Datenmanipulation |
| Betroffenes Schutzziel | Vertraulichkeit, Integritaet |
| Gegenmassnahme | TLS/HTTPS, VPN, Zertifikatspruefung |
| Beispiel | Angreifer im oeffentlichen WLAN faengt Login-Daten ab |

### SQL-Injection

**Funktionsweise:** Schadcode wird ueber Eingabefelder in SQL-Abfragen eingeschleust, um Datenbanken auszulesen oder zu manipulieren.

| Aspekt | Detail |
|---|---|
| Angriffsvektor | Webanwendung (Formular, URL) |
| Ziel | Datenbankinhalte lesen/aendern/loeschen |
| Betroffenes Schutzziel | Vertraulichkeit, Integritaet |
| Gegenmassnahme | Prepared Statements, Input Validation, WAF |
| Beispiel | `' OR 1=1 --` im Login-Feld umgeht Authentifizierung |

### DDoS-Attacke (Distributed Denial of Service)

**Funktionsweise:** Tausende kompromittierte Geraete (Botnet) senden gleichzeitig Anfragen an ein Ziel und ueberlasten es.

| Aspekt | Detail |
|---|---|
| Angriffsvektor | Netzwerk (Volumetric, Application Layer) |
| Ziel | Dienst/System lahmlegen |
| Betroffenes Schutzziel | Verfuegbarkeit |
| Gegenmassnahme | DDoS-Mitigation, CDN, Rate Limiting, Redundanz |
| Beispiel | Onlineshop wird durch Millionen Anfragen unerreichbar |

### Weitere Bedrohungen (Ueberblick)

| Bedrohung | Beschreibung | Gegenmassnahme |
|---|---|---|
| Cross-Site Scripting (XSS) | Schadcode in Webseite einschleusen | Output Encoding, CSP |
| Brute Force | Systematisches Ausprobieren von Passwoertern | Account-Lockout, MFA |
| Social Engineering | Manipulation von Personen | Awareness-Schulungen |
| Malware | Viren, Wuermer, Trojaner | Virenscanner, EDR |
| Zero-Day-Exploit | Ausnutzen unbekannter Schwachstellen | Patch-Management, IDS/IPS |

---

## Private Haushalte

**Definition:** Beratung von Privatpersonen zur Absicherung ihres digitalen Umfelds (Heimnetzwerk, Geraete, Online-Konten).

**Beratungsschwerpunkte:**

| Bereich | Empfehlung |
|---|---|
| WLAN-Sicherheit | WPA3 verwenden, SSID aendern, starkes Passwort, Gastnetz einrichten |
| Router-Konfiguration | Firmware aktuell halten, Fernzugriff deaktivieren, Standard-Passwort aendern |
| Passwortschutz | Mind. 12 Zeichen, Passwort-Manager nutzen, keine Wiederverwendung |
| MFA | Wo moeglich aktivieren (E-Mail, Banking, Social Media) |
| Datensicherung | Regelmaessige Backups auf externe Festplatte oder Cloud |
| Virenscanner | Aktueller Virenscanner, Betriebssystem-Updates |
| Phishing-Schutz | E-Mails kritisch pruefen, Links pruefen, keine Anhaenge oeffnen |
| Kinderschutz | Kindersicherung am Router, App-Kontrolle, Medienbildung |

---

## Qualitaetsanforderungen

**Definition:** An IT-Sicherheitsloesungen werden definierte Qualitaetsanforderungen gestellt, die bei der Beratung beruecksichtigt werden muessen.

| Anforderung | Beschreibung |
|---|---|
| Verfuegbarkeit | System muss im definierten Zeitrahmen erreichbar sein (SLA: z.B. 99,9%) |
| Performance | Sicherheitsloesung darf Systemleistung nicht unangemessen beeintraechtigen |
| Skalierbarkeit | Loesung muss mit wachsenden Anforderungen mitwachsen koennen |
| Kompatibilitaet | Integration in bestehende IT-Infrastruktur muss moeglich sein |
| Benutzerfreundlichkeit | Loesung muss fuer Nutzer handhabbar sein (sonst wird sie umgangen) |
| Wartbarkeit | Updates, Patches und Konfigurationsaenderungen muessen einfach moeglich sein |

---

## Rahmenbedingungen

**Definition:** Bei jeder IT-Sicherheitsberatung muessen vier Kategorien von Rahmenbedingungen beruecksichtigt werden.

| Kategorie | Beschreibung | Beispiele |
|---|---|---|
| Technologisch | Vorhandene IT-Infrastruktur, Kompatibilitaet | Betriebssysteme, Netzwerktopologie, Cloud-Dienste |
| Organisatorisch | Unternehmensstruktur, Prozesse, Personal | Sicherheitsrichtlinien, Schulungen, Verantwortlichkeiten |
| Rechtlich | Gesetze, Verordnungen, Normen | DSGVO, BDSG, IT-Sicherheitsgesetz, KRITIS-Verordnung |
| Ethisch | Moralische Aspekte, Verhaeltnismaessigkeit | Mitarbeiterueberwachung, Datensparsamkeit, Transparenz |

---

## Risikoanalyse

**Definition:** Systematische Identifikation, Bewertung und Priorisierung von Risiken fuer die IT-Sicherheit.

**Vorgehensweise:**

| Schritt | Beschreibung |
|---|---|
| 1. Bedrohungen identifizieren | Welche Angriffe/Gefahren sind moeglich? |
| 2. Schwachstellen identifizieren | Wo ist das System verwundbar? |
| 3. Risiko bewerten | Risiko = Eintrittswahrscheinlichkeit × Schadenshoehe |
| 4. Risiko priorisieren | Kritische Risiken zuerst behandeln |
| 5. Massnahmen ableiten | Risiko vermeiden, vermindern, uebertragen oder akzeptieren |

**Risikobehandlung:**

| Strategie | Beschreibung | Beispiel |
|---|---|---|
| Vermeiden | Risikoquelle eliminieren | Unsicheren Dienst abschalten |
| Vermindern | Eintrittswahrscheinlichkeit/Schaden senken | Firewall, Backup |
| Uebertragen | Risiko an Dritte abgeben | Cyber-Versicherung |
| Akzeptieren | Risiko bewusst hinnehmen | Restrisiko nach Kosten-Nutzen-Analyse |

---

## Technisch-organisatorische Massnahmen (TOM)

**Definition:** Massnahmen gemaess DSGVO Art. 32 zum Schutz personenbezogener Daten – unterteilt in technische und organisatorische Massnahmen.

| Kategorie | Technische Massnahmen | Organisatorische Massnahmen |
|---|---|---|
| Zutrittskontrolle | Schliessanlage, Chipkarte, Video | Besucherregelung, Schluesselverwaltung |
| Zugangskontrolle | Passwort, Biometrie, MFA | Passwortrichtlinie, Bildschirmsperre |
| Zugriffskontrolle | Verschluesselung, Rollenkonzept | Berechtigungskonzept, Need-to-Know |
| Weitergabekontrolle | VPN, TLS, Festplattenverschluesselung | Regelung zur Datenweitergabe |
| Eingabekontrolle | Protokollierung von Aenderungen | Dokumentation der Datenverarbeitung |
| Verfuegbarkeitskontrolle | USV, RAID, Backup | Notfallplan, Brandschutz |
| Trennungskontrolle | Mandantentrennung, VLAN | Zweckbindung der Datenverarbeitung |

---

## Unternehmen (intern, extern)

**Definition:** Beratung von Unternehmen zu internen und externen IT-Sicherheitsbedrohungen.

**Interne Bedrohungen:**

| Bedrohung | Beschreibung | Massnahme |
|---|---|---|
| Insider-Angriff | Mitarbeiter mit boesen Absichten | Least Privilege, Logging, DLP |
| Bedienfehler | Versehentliches Loeschen/Fehlkonfiguration | Schulungen, 4-Augen-Prinzip |
| Schatten-IT | Nicht genehmigte Software/Cloud-Dienste | IT-Richtlinien, Geraeteverwaltung |
| Unzureichende Passwoerter | Schwache oder geteilte Passwoerter | Passwortrichtlinie, MFA |

**Externe Bedrohungen:**

| Bedrohung | Beschreibung | Massnahme |
|---|---|---|
| Cyberangriffe | Ransomware, Phishing, DDoS | Firewall, EDR, Awareness |
| Supply-Chain-Angriff | Schadsoftware ueber Zulieferer | Lieferantenaudits, SLA |
| Industriespionage | Diebstahl von Geschaeftsgeheimnissen | Verschluesselung, Zugang einschraenken |

---

## Oeffentliche Hand – Funktionale Anforderungen

**Definition:** Behoerden und oeffentliche Einrichtungen unterliegen besonderen Anforderungen an IT-Sicherheit (BSI-Standards, KRITIS).

| Anforderung | Beschreibung |
|---|---|
| BSI IT-Grundschutz | Pflicht fuer Bundesbehoerden, empfohlen fuer alle oeffentlichen Stellen |
| KRITIS-Verordnung | Betreiber kritischer Infrastrukturen muessen IT-Sicherheit nachweisen |
| NIS2-Richtlinie | EU-weite Anforderungen an Cybersicherheit (ab 2024) |
| EVB-IT | Ergaenzende Vertragsbedingungen fuer IT in der oeffentlichen Beschaffung |
| Vergaberecht | IT-Sicherheitsanforderungen in Ausschreibungen definieren |
| Geheimschutz | VS-NfD, Verschlusssachen bei sicherheitsrelevanten Projekten |

## Querverweise
- → 1.6.01–1.6.04 (IT-Sicherheit, Datenschutz, ISMS, Sicherheitskonzept)
- → 2.4.01 (Schadenspotenziale)
- → 2.4.02 (Praeventive Massnahmen)
- → 2.4.05 (Tools zur Ueberpruefung)
- → 2.4.06 (TOM pruefen)
