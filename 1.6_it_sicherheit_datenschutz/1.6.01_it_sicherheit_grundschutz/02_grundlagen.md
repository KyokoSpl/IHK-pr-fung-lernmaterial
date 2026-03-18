# Grundlagen: 1.6.01 – IT-Sicherheit auf Grundschutzniveau

## BSI-IT-Grundschutz-Kompendium

**Definition:** Das BSI (Bundesamt fuer Sicherheit in der Informationstechnik) veroeffentlicht das IT-Grundschutz-Kompendium als Sammlung von Bausteinen, die typische Gefaehrdungen und Massnahmen beschreiben.

**Kernaussagen:**
- Bausteine sind nach Schichten gegliedert: ISMS, ORP (Organisation), CON (Konzepte), OPS (Betrieb), DER (Detektion/Reaktion), INF (Infrastruktur), NET (Netze), SYS (Systeme), APP (Anwendungen)
- Jeder Baustein enthaelt Anforderungen (Basis, Standard, erhoehter Schutzbedarf)
- Grundschutz = Standardabsicherung fuer normalen Schutzbedarf

---

## Technische Massnahmen

| Massnahme | Beschreibung |
|---|---|
| **Virenschutz** | Erkennung/Entfernung von Schadsoftware, regelmaessige Updates |
| **Personal Firewall** | Software-Firewall am Arbeitsplatz, regelt ein-/ausgehenden Datenverkehr |
| **Verschluesselung** | Schutz von Daten durch kryptografische Verfahren |

**Verschluesselungsarten:**

| Art | Prinzip | Schluessel | Beispiel |
|---|---|---|---|
| **Symmetrisch** | Gleicher Schluessel fuer Ver- und Entschluesselung | 1 Schluessel | AES, DES |
| **Asymmetrisch** | Schluessel-Paar (oeffentlich + privat) | 2 Schluessel | RSA, ECC |
| **Hybrid** | Asymmetrisch fuer Schluesselaustausch, symmetrisch fuer Daten | Kombination | TLS/HTTPS |

---

## Personenbezogene Daten

**Definition (Art. 4 DSGVO):** Alle Informationen, die sich auf eine identifizierte oder identifizierbare natuerliche Person beziehen.

**Beispiele:**
- Name, Adresse, Geburtsdatum
- E-Mail-Adresse, Telefonnummer
- IP-Adresse, Cookie-IDs
- Kontodaten, Sozialversicherungsnummer
- Gesundheitsdaten (besondere Kategorie!)

**Besondere Kategorien (Art. 9 DSGVO):** Gesundheit, Biometrie, Religion, politische Meinung, sexuelle Orientierung → erhoehter Schutz

---

## Datenschutzgesetze

| Gesetz | Geltungsbereich | Kerninhalt |
|---|---|---|
| **DSGVO** | EU-weit | Schutz personenbezogener Daten, Betroffenenrechte, Verarbeitungsgrundsaetze |
| **BDSG** | Deutschland | Ergaenzung zur DSGVO fuer nationale Besonderheiten |

**DSGVO-Grundsaetze der Datenverarbeitung (Art. 5):**
1. Rechtmaessigkeit, Verarbeitung nach Treu und Glauben, Transparenz
2. Zweckbindung
3. Datenminimierung
4. Richtigkeit
5. Speicherbegrenzung
6. Integritaet und Vertraulichkeit
7. Rechenschaftspflicht

---

## IT-Sicherheitsrichtlinien / Passwort-Policy

**Passwort-Policy (typische Anforderungen):**
- Mindestlaenge: 12 Zeichen (BSI-Empfehlung, frueher 8)
- Komplexitaet: Gross-/Kleinbuchstaben, Zahlen, Sonderzeichen
- Aenderungsintervall: Nur nach Verdacht der Kompromittierung (BSI aktuell)
- Kein Passwort-Recycling
- Multi-Faktor-Authentifizierung (MFA) empfohlen

---

## Schutzziele der Informationssicherheit

| Schutzziel | Englisch | Bedeutung | Bedrohung |
|---|---|---|---|
| **Vertraulichkeit** | Confidentiality | Nur Berechtigte haben Zugang | Datendiebstahl, Spionage |
| **Integritaet** | Integrity | Daten sind vollstaendig und unveraendert | Manipulation, Malware |
| **Verfuegbarkeit** | Availability | Systeme/Daten sind nutzbar wenn benoetigt | DoS-Angriff, Hardwareausfall |

Erweiterung (CIA+):
- **Authentizitaet:** Echtheit des Absenders sichergestellt
- **Nichtabstreitbarkeit:** Handlungen koennen nachgewiesen werden
- **Zurechenbarkeit:** Aktionen koennen Personen zugeordnet werden

---

## Anonymisierung und Pseudonymisierung

| Verfahren | Beschreibung | Umkehrbar? | Beispiel |
|---|---|---|---|
| **Anonymisierung** | Personenbezug vollstaendig entfernen | Nein | Statistische Auswertungen ohne Namen |
| **Pseudonymisierung** | Personenbezug durch Kennzeichen ersetzen | Ja (mit Zuordnungstabelle) | Kundennummer statt Name |

---

## Technisch-organisatorische Massnahmen (TOM)

**Definition:** Massnahmen nach Art. 32 DSGVO zum Schutz personenbezogener Daten.

| Kategorie | Beispiele |
|---|---|
| **Zutrittskontrolle** | Schlossanlage, Chipkarte, Videoüberwachung |
| **Zugangskontrolle** | Passwort, Biometrie, Bildschirmsperre |
| **Zugriffskontrolle** | Berechtigungskonzept, Rollenmodell |
| **Weitergabekontrolle** | Verschluesselung, VPN |
| **Eingabekontrolle** | Protokollierung, Audit-Logs |
| **Verfuegbarkeitskontrolle** | Backup, USV, Redundanz |
| **Trennungsgebot** | Mandantentrennung, getrennte Datenbanken |

---

## Personelle Massnahmen / Sicherheitsbewusstsein

- Regelmaessige Awareness-Schulungen
- Phishing-Simulationen
- Verpflichtung auf Datengeheimnis
- Clean-Desk-Policy
- Verhalten bei Sicherheitsvorfaellen trainieren

---

## Rechte der Betroffenen (DSGVO)

| Recht | Artikel | Beschreibung |
|---|---|---|
| Auskunft | Art. 15 | Welche Daten werden verarbeitet? |
| Berichtigung | Art. 16 | Falsche Daten korrigieren |
| Loeschung | Art. 17 | „Recht auf Vergessenwerden" |
| Einschraenkung | Art. 18 | Verarbeitung voruebergehend sperren |
| Datenuebertragbarkeit | Art. 20 | Daten in maschinenlesbarem Format erhalten |
| Widerspruch | Art. 21 | Verarbeitung widersprechen |

**Einwilligung (Art. 6/7 DSGVO):**
- Muss freiwillig, informiert, unmissverstaendlich und widerrufbar sein
- Fuer besondere Kategorien: ausdrueckliche Einwilligung noetig

---

## IT-Sicherheitsbeauftragter vs. Datenschutzbeauftragter

| Kriterium | IT-Sicherheitsbeauftragter | Datenschutzbeauftragter |
|---|---|---|
| **Fokus** | Technische Sicherheit der IT-Systeme | Schutz personenbezogener Daten |
| **Rechtsgrundlage** | BSI-Grundschutz, interne Richtlinien | DSGVO, BDSG |
| **Pflicht** | Keine gesetzliche Pflicht (empfohlen) | Gesetzliche Pflicht ab 20 MA mit personenbez. Daten |
| **Aufgaben** | Sicherheitskonzepte, Risikobewertung, Incident Response | Datenschutz-Folgenabschaetzung, Betroffenenrechte, Schulung |
| **Berichtet an** | Geschaeftsfuehrung | Unabhaengig (Weisungsfreiheit!) |
