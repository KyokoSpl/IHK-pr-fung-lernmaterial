# Grundlagen: 2.4.06 – Wirksamkeit und Effizienz der umgesetzten TOM pruefen

## Compliance Reports

**Definition:** Compliance Reports sind strukturierte Berichte, die nachweisen, ob und inwieweit ein Unternehmen Sicherheitsrichtlinien, gesetzliche Vorgaben und Normen einhalt.

**Arten von Compliance Reports:**

| Report-Typ | Beschreibung | Regelwerk |
|---|---|---|
| Internes Audit | Selbstpruefung durch eigene IT-/Sicherheitsabteilung | Interne Richtlinien |
| Externes Audit | Pruefung durch unabhaengige Auditoren | ISO 27001, BSI IT-Grundschutz |
| Datenschutzbericht | Nachweis der DSGVO-Konformitaet | DSGVO Art. 5, 32 |
| SOC 2 Report | Nachweis fuer Cloud-Anbieter (Sicherheit, Verfuegbarkeit) | AICPA Trust Service Criteria |
| Penetrationstest-Bericht | Ergebnisse eines Pentests mit Findings | Individuell / OWASP |
| Schwachstellenbericht | Ergebnisse automatisierter Schwachstellenscans | CVE, CVSS |

**Inhalte eines Compliance Reports:**

| Abschnitt | Inhalt |
|---|---|
| Management Summary | Zusammenfassung fuer die Geschaeftsfuehrung |
| Pruefumfang (Scope) | Welche Systeme/Prozesse wurden geprueft? |
| Methodik | Welche Standards/Tools wurden verwendet? |
| Findings | Gefundene Abweichungen, Schwachstellen, Nichtkonformitaeten |
| Risikobewertung | Schweregrad der Findings (kritisch, hoch, mittel, niedrig) |
| Empfehlungen | Konkrete Massnahmen zur Behebung |
| Nachverfolgung | Fristen und Verantwortlichkeiten fuer die Umsetzung |

---

## Log Management

**Definition:** Systematische Erfassung, zentrale Speicherung, Auswertung und Archivierung von Protokolldaten (Logs) aus IT-Systemen.

**Log-Quellen:**

| Quelle | Beispiel-Eintraege |
|---|---|
| Betriebssystem | Login/Logout, Fehlermeldungen, Systemereignisse |
| Firewall | Blockierte/erlaubte Verbindungen, Regelverstoesse |
| Webserver | HTTP-Requests, Fehlercodes (403, 404, 500) |
| Datenbank | Abfragen, Aenderungen, fehlgeschlagene Logins |
| Anwendung | Benutzeraktionen, Fehlermeldungen, Transaktionen |
| Active Directory | Kontoaenderungen, Gruppenrichtlinien-Anwendung |
| VPN-Gateway | Verbindungsauf-/-abbau, IP-Adressen |

**SIEM (Security Information and Event Management):**

| Funktion | Beschreibung |
|---|---|
| Sammlung | Logs aus verschiedenen Quellen zentral zusammenfuehren |
| Korrelation | Zusammenhaenge zwischen Ereignissen erkennen |
| Alarmierung | Bei verdaechtigen Mustern automatisch alarmieren |
| Dashboard | Echtzeitueberblick ueber Sicherheitslage |
| Forensik | Nachtraegliche Analyse von Vorfaellen |
| Beispiele | Splunk, Elastic SIEM, IBM QRadar, Microsoft Sentinel |

**Aufbewahrungsfristen fuer Logs:**

| Regelwerk | Aufbewahrungsdauer | Beispiel |
|---|---|---|
| DSGVO | So kurz wie moeglich (Datensparsamkeit) | Zugriffslogs: 6 Monate |
| GoBD | 6-10 Jahre | Buchungsrelevante Daten |
| BSI IT-Grundschutz | Mind. 6 Monate empfohlen | Sicherheitsrelevante Logs |
| Branchenspezifisch | Variabel | Finanzbranche: bis 10 Jahre |

**Wichtig:** Logs koennen personenbezogene Daten enthalten (IP-Adressen, Benutzernamen) → DSGVO beachten!

---

## Zugangskontrolle

**Definition:** Massnahmen, die verhindern, dass unbefugte Personen Zugang zu IT-Systemen erhalten (Login an Computern, Servern, Anwendungen).

**Authentifizierungsverfahren:**

| Verfahren | Kategorie | Beschreibung | Sicherheit |
|---|---|---|---|
| Passwort | Wissen | Zeichenkette, die nur der Nutzer kennt | Mittel (abhaengig von Komplexitaet) |
| PIN | Wissen | Kurze Zahlenkombination | Gering (ohne weitere Faktoren) |
| Biometrie – Fingerabdruck | Biometrie | Fingerabdrucksensor | Hoch |
| Biometrie – Gesichtserkennung | Biometrie | Kamera + Algorithmus | Hoch (abhaengig von Technik) |
| Biometrie – Iris-Scan | Biometrie | Scan der Regenbogenhaut | Sehr hoch |
| Chipkarte / Smartcard | Besitz | Karte mit gespeichertem Zertifikat | Hoch (mit PIN: MFA) |
| Hardware-Token | Besitz | YubiKey, RSA SecurID | Hoch |
| TOTP (z.B. Authenticator App) | Besitz | Zeitbasierter Einmalcode | Hoch |
| Bildschirmsperre | Wissen/Biometrie | Automatische Sperre nach Inaktivitaet | Basis-Schutz |

**Passwortrichtlinie (Best Practice):**

| Kriterium | Empfehlung |
|---|---|
| Mindestlaenge | 12 Zeichen (BSI: mind. 8, besser 12+) |
| Komplexitaet | Gross-/Kleinbuchstaben, Zahlen, Sonderzeichen |
| Wiederverwendung | Verboten (jedes System eigenes Passwort) |
| Aenderungsintervall | Nicht mehr erzwungen (BSI 2024), nur bei Verdacht |
| Sperrung | Nach 5 Fehlversuchen fuer 15 Minuten sperren |
| MFA | Wo moeglich aktivieren |

---

## Zugriffskontrolle

**Definition:** Massnahmen, die sicherstellen, dass nur berechtigte Personen auf bestimmte Daten und Ressourcen zugreifen koennen.

**Berechtigungskonzept:**

| Element | Beschreibung |
|---|---|
| Berechtigungsmatrix | Tabelle: Wer darf auf welche Daten/Ressourcen zugreifen? |
| Rollenkonzept (RBAC) | Rechte werden Rollen zugewiesen, Nutzer erhalten Rollen |
| Need-to-Know-Prinzip | Zugriff nur auf Daten, die fuer die Aufgabe noetig sind |
| Least Privilege | Minimale Berechtigungen, die fuer die Arbeit erforderlich sind |
| 4-Augen-Prinzip | Kritische Aktionen erfordern Freigabe durch zweite Person |

**Verschluesselung von Datentraegern:**

| Methode | Beschreibung | Einsatz |
|---|---|---|
| BitLocker | Microsoft-Verschluesselung fuer Windows-Laufwerke | Laptops, Desktops |
| FileVault | Apple-Verschluesselung fuer macOS | MacBooks |
| LUKS | Linux-Festplattenverschluesselung | Linux-Server, Desktops |
| VeraCrypt | Plattformuebergreifend, Open Source | USB-Sticks, Container |
| Hardwareverschluesselung | Verschluesselung im Laufwerk (SED) | Enterprise-SSDs |

**Sichere Datentraegerloeschung:**

| Methode | Beschreibung | Sicherheit |
|---|---|---|
| Formatieren (Schnell) | Nur Dateisystem-Eintraege loeschen | Unsicher (Daten wiederherstellbar) |
| Ueberschreiben | Alle Sektoren mit Zufallsdaten ueberschreiben | Sicher (1-3 Durchgaenge genuegen) |
| Kryptografisches Loeschen | Schluessel vernichten (bei verschluesselten Laufwerken) | Sehr sicher, schnell |
| Physische Vernichtung | Shredder, Degausser | Hoechste Sicherheit |

---

## Zutrittskontrolle

**Definition:** Massnahmen, die unbefugten physischen Zutritt zu Raeumen und Gebaeuden mit IT-Infrastruktur verhindern.

**Zutrittskontrollmassnahmen:**

| Massnahme | Beschreibung | Einsatzbereich |
|---|---|---|
| Alarmanlage | Erkennt unbefugten Zutritt, loest Alarm aus | Serverraum, Rechenzentrum |
| Videoueberwachung | Kameras zeichnen Zutritts-/Oeffentlichkeitsbereiche auf | Eingang, Flure, Serverraum |
| Schliesssystem | Mechanisch oder elektronisch (Chipkarte, PIN) | Alle Raeume |
| Besucherausweise | Besucher erhalten sichtbaren Ausweis mit Gueltigkeitsdauer | Empfang, Besuchermanagement |
| Vereinzelungsanlage | Schleuse/Drehkreuz – nur eine Person pro Zutritt | Rechenzentrum, Hochsicherheit |
| Sicherheitspersonal | Pfoertner, Wachschutz | Empfang, Kontrollpunkte |
| Zutrittsprotokolle | Wer hat wann welchen Raum betreten? | Elektronische Schliesssysteme |

**Zonierung (Sicherheitszonen):**

| Zone | Beschreibung | Beispiel | Zutrittskontrolle |
|---|---|---|---|
| Oeffentlich | Frei zugaenglich | Empfangsbereich, Lobby | Keine |
| Intern | Nur Mitarbeiter | Bueros, Besprechungsraeume | Chipkarte |
| Eingeschraenkt | Nur autorisiertes Personal | Serverraum, Archiv | Chipkarte + PIN |
| Hochsicherheit | Streng kontrolliert | Rechenzentrum, Tresorraum | Biometrie + Chipkarte + Protokoll |

## Querverweise
- → 1.6.01 (Schutzziele: CIA)
- → 1.6.02 (DSGVO, TOM-Pflicht Art. 32)
- → 2.4.04 (TOM in der Kundenberatung)
- → 2.4.05 (Tools zur Ueberpruefung)
