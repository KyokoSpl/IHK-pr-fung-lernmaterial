# Grundlagen: 2.4.03 – Ziele zur Entwicklung von IT-Sicherheitskriterien

## Objektive Bewertung der Systeme (IT-Grundschutzmodellierung)

**Definition:** Die IT-Grundschutzmodellierung des BSI (Bundesamt fuer Sicherheit in der Informationstechnik) ist eine standardisierte Methode, um den Sicherheitszustand von IT-Systemen objektiv zu bewerten und passende Schutzmassnahmen abzuleiten.

**IT-Grundschutz-Vorgehensweise:**

| Schritt | Beschreibung |
|---|---|
| 1. Strukturanalyse | IT-Infrastruktur erfassen (Server, Netze, Anwendungen, Raeume) |
| 2. Schutzbedarfsfeststellung | Schutzbedarf fuer jedes Objekt bestimmen (normal, hoch, sehr hoch) |
| 3. Modellierung | Passende Bausteine aus dem IT-Grundschutz-Kompendium zuordnen |
| 4. IT-Grundschutz-Check | Soll-Ist-Vergleich: Welche Massnahmen sind umgesetzt, welche fehlen? |
| 5. Risikoanalyse | Fuer Objekte mit hohem Schutzbedarf: ergaenzende Risikoanalyse |

**Schutzbedarfskategorien:**

| Kategorie | Beschreibung | Beispiel |
|---|---|---|
| Normal | Begrenzte Auswirkungen bei Verletzung | Internes Newsletter-System |
| Hoch | Erhebliche Auswirkungen | Personalverwaltungssystem |
| Sehr hoch | Existenzbedrohende Auswirkungen | Steuerungssystem Kraftwerk (KRITIS) |

**BSI IT-Grundschutz-Kompendium:**
- Sammlung von **Bausteinen** (z.B. OPS.1.1.3 Patch-Management, APP.1.1 Office-Produkte)
- Jeder Baustein enthaelt **Anforderungen** (Basis, Standard, erhoehter Schutzbedarf)
- Bausteinschichten: ISMS, ORP, CON, OPS, DER, APP, SYS, IND, NET, INF

---

## Richtschnur fuer Entwickler

**Definition:** Sicherheitskriterien dienen als verbindliche Leitlinie fuer Entwickler, um Software und Systeme von Beginn an sicher zu gestalten.

**Wichtige Standards und Leitlinien:**

| Standard/Leitlinie | Beschreibung |
|---|---|
| OWASP Top 10 | Die 10 haeufigsten Sicherheitsrisiken in Webanwendungen |
| BSI-Leitfaden Sichere Webentwicklung | Empfehlungen des BSI fuer sichere Webapplikationen |
| ISO/IEC 27034 | Anwendungssicherheit im ISMS |
| Common Weakness Enumeration (CWE) | Katalog typischer Softwareschwachstellen |

**OWASP Top 10 (Auszug fuer Pruefung):**

| Rang | Schwachstelle | Beschreibung |
|---|---|---|
| 1 | Broken Access Control | Fehlende oder fehlerhafte Zugriffskontrolle |
| 2 | Cryptographic Failures | Schwache oder fehlende Verschluesselung |
| 3 | Injection | SQL-Injection, XSS – Einschleusung von Code |
| 4 | Insecure Design | Fehlende Sicherheitsarchitektur im Entwurf |
| 5 | Security Misconfiguration | Fehlerhafte Konfiguration (Default-Passwoerter) |

**Secure Coding Prinzipien:**
- **Input Validation:** Alle Eingaben pruefen und bereinigen
- **Output Encoding:** Ausgaben kodieren (gegen XSS)
- **Least Privilege:** Minimale Rechte fuer Prozesse und Nutzer
- **Defense in Depth:** Mehrere Sicherheitsschichten
- **Fail Securely:** Im Fehlerfall sicher reagieren (kein Datenabfluss)
- **Code Review:** Regelmaessige Sicherheitspruefung des Quellcodes

---

## Unterstuetzung von Anwendern bei Auswahl (Security by Design)

**Definition:** Security by Design bedeutet, dass Sicherheit von Anfang an in den Entwurf und die Entwicklung eines Produkts integriert wird – nicht erst nachtraeglich.

**Prinzipien von Security by Design:**

| Prinzip | Beschreibung |
|---|---|
| Minimale Angriffsflaeche | Nur notwendige Funktionen und Schnittstellen bereitstellen |
| Sichere Standardeinstellungen | Standardkonfiguration ist die sicherste (Secure Defaults) |
| Verteidigung in der Tiefe | Mehrere unabhaengige Sicherheitsschichten |
| Prinzip der minimalen Rechte | Nutzer und Prozesse erhalten nur die minimal noetigen Rechte |
| Datensparsamkeit | Nur notwendige Daten erheben (→ Privacy by Design, DSGVO) |
| Transparenz | Sicherheitsmassnahmen sind dokumentiert und nachvollziehbar |

**Privacy by Design (DSGVO Art. 25):**
- Datenschutz durch Technikgestaltung
- Datenschutz durch datenschutzfreundliche Voreinstellungen
- Muss bei jedem neuen System/Produkt beruecksichtigt werden

**Zertifizierung und Bewertung fuer Anwender:**

| Zertifizierung | Beschreibung |
|---|---|
| Common Criteria (CC) | Internationaler Standard zur Bewertung der Sicherheit von IT-Produkten |
| ISO/IEC 27001 | Zertifizierung eines ISMS |
| BSI-Zertifizierung | IT-Grundschutz-Zertifikat (Basis, Standard, Kern) |
| IT-Sicherheitskennzeichen (BSI) | Verbraucherfreundliches Kennzeichen fuer IT-Produkte |

**Common Criteria – Vertrauensstufen (EAL):**

| Stufe | Bezeichnung | Prueftiefe |
|---|---|---|
| EAL 1 | Funktional getestet | Minimal |
| EAL 2 | Strukturell getestet | Gering |
| EAL 3 | Methodisch getestet und geprueft | Mittel |
| EAL 4 | Methodisch entworfen, getestet, geprueft | Standard fuer kommerzielle Produkte |
| EAL 5-7 | Formal verifiziert | Hoch bis sehr hoch (Militaer, Regierung) |

## Querverweise
- → 1.6.03 (ISMS – ISO 27001, BSI IT-Grundschutz)
- → 1.6.04 (Security by Design, Sicherheitskonzept)
- → 2.4.04 (Kundenberatung, Rahmenbedingungen)
