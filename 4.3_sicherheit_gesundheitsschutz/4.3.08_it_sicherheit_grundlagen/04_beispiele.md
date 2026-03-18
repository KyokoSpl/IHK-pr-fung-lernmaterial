# Beispiele: 4.3.08 – Grundlagen der IT-Sicherheit kennen und umsetzen

## Beispiel 1: CIA-Triade in der Praxis

Ein mittelstaendisches Unternehmen betreibt einen Online-Shop. Ordne die folgenden Vorfaelle den verletzten Schutzzielen zu:

| Vorfall | Verletztes Schutzziel | Begruendung |
|---------|----------------------|-------------|
| Ein Hacker liest die Kreditkartendaten der Kunden aus | **Vertraulichkeit** | Unbefugter hat Zugriff auf vertrauliche Daten |
| Durch einen Softwarefehler werden Preise in der Datenbank falsch gespeichert | **Integritaet** | Daten sind nicht mehr korrekt/vollstaendig |
| Ein DDoS-Angriff legt den Online-Shop 6 Stunden lahm | **Verfuegbarkeit** | System ist nicht erreichbar |
| Ein Angreifer versendet E-Mails im Namen des Unternehmens (Spoofing) | **Authentizitaet** | Absender ist nicht der, der er vorgibt zu sein |

**Gegenmassnahmen:**

| Schutzziel | Massnahme |
|-----------|-----------|
| Vertraulichkeit | Datenbankverschluesselung, Zugriffskontrolle, Firewall, WAF |
| Integritaet | Pruefsummen, Transaktionslogging, Input-Validierung |
| Verfuegbarkeit | DDoS-Schutz, Redundanz, CDN, SLA mit Hosting-Anbieter |
| Authentizitaet | DKIM/SPF/DMARC fuer E-Mail, 2FA fuer Admin-Zugang |

---

## Beispiel 2: TOM fuer ein Softwareunternehmen

Ein Softwareunternehmen mit 50 Mitarbeitern verarbeitet personenbezogene Daten (Kundendaten, Mitarbeiterdaten). Der Datenschutzbeauftragte erstellt ein TOM-Verzeichnis:

| TOM-Kategorie | Konkrete Massnahme |
|---------------|-------------------|
| **Zutrittskontrolle** | Chipkarten-Zugang zum Gebaeude, Serverraum mit PIN-Code, Besucheranmeldung |
| **Zugangskontrolle** | Active Directory mit Passwortrichtlinie (min. 12 Zeichen), 2FA fuer VPN, automatische Bildschirmsperre nach 5 min |
| **Zugriffskontrolle** | Rollenbasiertes Berechtigungskonzept (RBAC), Admin-Rechte nur fuer IT-Abteilung, Need-to-know-Prinzip |
| **Weitergabekontrolle** | E-Mail-Verschluesselung (S/MIME), VPN fuer Homeoffice, HTTPS fuer alle Webanwendungen |
| **Eingabekontrolle** | Logging aller Datenbankaenderungen, Audit-Trail im ERP-System |
| **Auftragskontrolle** | AVV mit Cloud-Anbieter (Azure), regelmaessige Kontrolle des Dienstleisters |
| **Verfuegbarkeitskontrolle** | Taegliches Backup (3-2-1-Regel), USV-Anlage, Redundanter Internetanschluss |
| **Trennungsgebot** | Mandantentrennung in der Datenbank, getrennte Test-/Produktivumgebungen |

---

## Beispiel 3: BSI-Grundschutz anwenden

Ein kleines IT-Startup (15 Mitarbeiter) moechte seine IT-Sicherheit verbessern. Es entscheidet sich fuer den BSI-Grundschutz.

**Schritt 1 – Vorgehensweise waehlen:**
- Basis-Absicherung (da kleines Unternehmen, Einstieg)

**Schritt 2 – Informationsverbund definieren:**
- 15 Arbeitsplaetze (Laptops)
- 2 Server (Fileserver, Anwendungsserver)
- 1 Firewall, 1 Switch, WLAN
- Cloud-Dienste (Office 365, GitHub)

**Schritt 3 – Bausteine zuordnen:**

| Bereich | Baustein | Massnahme |
|---------|---------|-----------|
| Arbeitsplatz | SYS.2.1 Allgemeiner Client | Festplattenverschluesselung, Virenscanner, Updates |
| Server | SYS.1.1 Allgemeiner Server | Haertung, Backup, Monitoring |
| Netzwerk | NET.1.1 Netzarchitektur | Netzwerksegmentierung, Firewall-Regeln |
| Organisation | ORP.1 Organisation | Sicherheitsrichtlinie erstellen |
| Personal | ORP.4 Identitaetsmanagement | Berechtigungskonzept, Passwortrichtlinie |

**Schritt 4 – Soll-Ist-Vergleich:**
- Festplattenverschluesselung: Nur bei 5 von 15 Laptops → **Luecke!**
- Backup: Nur woechentlich statt taeglich → **Luecke!**
- Passwortrichtlinie: Existiert nicht → **Luecke!**

**Schritt 5 – Massnahmen umsetzen:**
- Alle Laptops mit BitLocker verschluesseln
- Taegliches automatisches Backup einrichten
- Passwortrichtlinie einfuehren (min. 12 Zeichen, Komplexitaet, 2FA)

---

## Beispiel 4: Datenschutz vs. Informationssicherheit

**Szenario:** Ein Unternehmen speichert sowohl Kundendaten (personenbezogen) als auch Quellcode (nicht personenbezogen).

| Schutzmassnahme | Datenschutz-relevant? | Informationssicherheit-relevant? |
|----------------|----------------------|--------------------------------|
| Verschluesselung der Kundendatenbank | Ja (personenbezogene Daten) | Ja (Vertraulichkeit) |
| Zugriffskontrolle fuer das Git-Repository | Nein (kein Personenbezug) | Ja (Schutz des Quellcodes) |
| Backup aller Systeme | Ja (Verfuegbarkeit personenbez. Daten) | Ja (Verfuegbarkeit aller Daten) |
| Datenschutz-Schulung fuer Mitarbeiter | Ja (DSGVO-Pflicht) | Teilweise (Awareness) |
| Einbruchmeldeanlage im Serverraum | Indirekt (physischer Schutz der Daten) | Ja (Zutrittskontrolle) |
| Loeschkonzept fuer alte Bewerberdaten | Ja (Speicherbegrenzung, DSGVO) | Nein (kein Sicherheitsthema) |

**Erkenntnis:** Informationssicherheit umfasst ALLE Informationen. Datenschutz ist ein Teilbereich, der sich auf personenbezogene Daten konzentriert.

---

## Beispiel 5: DSGVO Art. 5 – Grundsaetze pruefen

Ein Unternehmen erhebt bei der Online-Registrierung folgende Daten: Name, E-Mail, Telefon, Geburtsdatum, Lieblingsfarbe, Einkommen, Hobbys, Adresse.

**Pruefung nach DSGVO Art. 5 – Datenminimierung:**

| Datum | Fuer Registrierung noetig? | Bewertung |
|-------|---------------------------|-----------|
| Name | Ja (Identifikation) | ✓ Erforderlich |
| E-Mail | Ja (Kommunikation, Login) | ✓ Erforderlich |
| Telefon | Ggf. fuer 2FA | ✓ Optional, mit Begruendung |
| Geburtsdatum | Nur wenn Altersprüfung noetig | ⚠ Nur mit Zweckbindung |
| Lieblingsfarbe | Nein | ✗ Verstoss gegen Datenminimierung |
| Einkommen | Nein | ✗ Verstoss gegen Datenminimierung |
| Hobbys | Nein | ✗ Verstoss gegen Datenminimierung |
| Adresse | Nur bei physischem Versand | ⚠ Nur mit Zweckbindung |

**Ergebnis:** Lieblingsfarbe, Einkommen und Hobbys verstoesseln gegen den Grundsatz der **Datenminimierung**. Nur Daten erheben, die fuer den konkreten Zweck erforderlich sind.
