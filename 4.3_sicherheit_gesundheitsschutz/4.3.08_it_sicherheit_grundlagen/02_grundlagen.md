# Grundlagen: 4.3.08 – Grundlagen der IT-Sicherheit kennen und umsetzen

## Betriebliches IT-Sicherheitskonzept

**Definition:** Ein IT-Sicherheitskonzept beschreibt die systematische Planung, Umsetzung und Ueberwachung aller Massnahmen zum Schutz der IT-Systeme, Daten und Prozesse eines Unternehmens.

**Kernaussagen:**
- Basiert auf einer Risikoanalyse (Bedrohungen, Schwachstellen, Schadensausmass)
- Definiert Schutzziele, Verantwortlichkeiten und Massnahmen
- Muss regelmaessig aktualisiert werden
- Orientiert sich an Standards (BSI-Grundschutz, ISO 27001)

**Bestandteile eines IT-Sicherheitskonzepts:**

| Bestandteil | Beschreibung |
|-------------|-------------|
| Geltungsbereich | Welche Systeme/Bereiche sind abgedeckt? |
| Schutzziele | CIA + Authentizitaet (siehe unten) |
| Risikoanalyse | Bedrohungen identifizieren und bewerten |
| Massnahmen | TOMs definieren und umsetzen |
| Verantwortlichkeiten | Wer ist wofuer zustaendig? (z.B. IT-Sicherheitsbeauftragter) |
| Notfallplan | Business Continuity, Disaster Recovery |
| Schulungen | Sensibilisierung der Mitarbeiter |
| Ueberpruefung | Regelmaessige Audits und Anpassungen |

---

## BSI-Aufgaben

**Definition:** Das BSI (Bundesamt fuer Sicherheit in der Informationstechnik) ist die zentrale Cyberssicherheitsbehoerde Deutschlands und dem Bundesministerium des Innern unterstellt.

**Kernaussagen:**

| Aufgabe | Beschreibung |
|---------|-------------|
| Schutz der Regierungsnetze | IT-Sicherheit fuer Bundesbehoerden |
| Warnungen und Empfehlungen | Sicherheitshinweise fuer Unternehmen und Buerger |
| IT-Grundschutz | Bereitstellung des IT-Grundschutz-Kompendiums |
| Zertifizierung | Pruefung und Zertifizierung von IT-Produkten (z.B. Common Criteria) |
| CERT-Bund | Computer Emergency Response Team → Krisenreaktion bei IT-Sicherheitsvorfaellen |
| Beratung | Unterstuetzung von Unternehmen und Behoerden |
| Forschung | Forschung zu IT-Sicherheitsthemen |

**Wichtige Begriffe:**
- **BSI** – Bundesamt fuer Sicherheit in der Informationstechnik (Sitz: Bonn)
- **CERT-Bund** – Computer Emergency Response Team der Bundesverwaltung
- **IT-Grundschutz-Kompendium** – Sammlung von Bausteinen fuer die IT-Sicherheit

---

## BSI-Standards

**Definition:** Die BSI-Standards sind Empfehlungen und Methoden fuer die Umsetzung von Informationssicherheit in Organisationen.

| Standard | Titel | Inhalt |
|----------|-------|--------|
| **BSI-Standard 200-1** | Managementsysteme fuer Informationssicherheit (ISMS) | Aufbau eines ISMS, Anforderungen, Prozesse |
| **BSI-Standard 200-2** | IT-Grundschutz-Methodik | Vorgehensmodell: Basis-/Standard-/Kern-Absicherung |
| **BSI-Standard 200-3** | Risikomanagement | Risikoanalyse, Risikobewertung, Risikobehandlung |
| **BSI-Standard 200-4** | Business Continuity Management (BCM) | Notfallmanagement, Aufrechterhaltung des Geschaeftsbetriebs |

**Drei Vorgehensweisen nach BSI-Standard 200-2:**

| Vorgehensweise | Zielgruppe | Aufwand | Beschreibung |
|---------------|-----------|---------|-------------|
| **Basis-Absicherung** | Einsteiger, kleine Unternehmen | Gering | Grundlegende Sicherheitsmassnahmen schnell umsetzen |
| **Standard-Absicherung** | Mittlere/grosse Unternehmen | Mittel | Umfassende Sicherheit nach IT-Grundschutz |
| **Kern-Absicherung** | Alle | Hoch (fuer Kernprozesse) | Fokus auf besonders schuetzenswerte Bereiche |

---

## Verfuegbarkeit, Integritaet, Vertraulichkeit und Authentizitaet

**Definition:** Die drei klassischen Schutzziele der Informationssicherheit bilden die CIA-Triade. Ergaenzt wird sie im deutschen Raum oft durch Authentizitaet.

### CIA-Triade + Authentizitaet

| Schutzziel | Englisch | Definition | Beispiel |
|-----------|----------|-----------|---------|
| **Vertraulichkeit** | Confidentiality | Nur Befugte haben Zugriff auf die Daten | Verschluesselung, Zugriffsrechte |
| **Integritaet** | Integrity | Daten sind vollstaendig und unveraendert | Hashwerte, Pruefsummen, digitale Signaturen |
| **Verfuegbarkeit** | Availability | Systeme und Daten sind bei Bedarf zugaenglich | Redundanz, USV, Backup, SLA |
| **Authentizitaet** | Authenticity | Echtheit und Herkunft von Daten/Personen ist nachweisbar | Digitale Zertifikate, 2-Faktor-Authentifizierung |

**Erweiterte Schutzziele (ergaenzend):**
- **Nichtabstreitbarkeit (Non-Repudiation):** Absender kann Nachricht nicht leugnen (digitale Signatur)
- **Zurechenbarkeit (Accountability):** Aktionen koennen Personen zugeordnet werden (Logging)

---

## DSGVO-Ziele

**Definition:** Die Datenschutz-Grundverordnung (DSGVO/GDPR) ist eine EU-Verordnung zum Schutz personenbezogener Daten natuerlicher Personen.

**Grundsaetze der Datenverarbeitung (Art. 5 DSGVO):**

| Grundsatz | Bedeutung |
|-----------|----------|
| **Rechtmaessigkeit** | Verarbeitung nur mit Rechtsgrundlage (Einwilligung, Vertrag, gesetzliche Pflicht) |
| **Zweckbindung** | Daten nur fuer festgelegte, eindeutige Zwecke verarbeiten |
| **Datenminimierung** | Nur so viele Daten wie noetig erheben |
| **Richtigkeit** | Daten muessen korrekt und aktuell sein |
| **Speicherbegrenzung** | Loeschung, wenn Zweck erfuellt |
| **Integritaet und Vertraulichkeit** | Angemessene Sicherheit durch TOMs |
| **Rechenschaftspflicht** | Verantwortlicher muss Einhaltung nachweisen koennen |

**Art. 32 DSGVO – Sicherheit der Verarbeitung:**
- Verarbeiter muessen geeignete **technische und organisatorische Massnahmen (TOM)** treffen
- Unter Beruecksichtigung von: Stand der Technik, Implementierungskosten, Risiko

---

## Informationssicherheit vs. Datenschutz

**Definition:** Informationssicherheit und Datenschutz haben unterschiedliche Schutzobjekte und Ziele, ueberlappen sich aber in der Praxis.

| Aspekt | Informationssicherheit | Datenschutz |
|--------|----------------------|-------------|
| **Schutzobjekt** | Alle Informationen (digital, analog, geistig) | Personenbezogene Daten natuerlicher Personen |
| **Ziel** | Schutz vor Verlust, Manipulation, unbefugtem Zugriff | Schutz der informationellen Selbstbestimmung |
| **Rechtsgrundlage** | Kein einheitliches Gesetz (BSI-Gesetz, ISO 27001) | DSGVO, BDSG |
| **Verantwortlicher** | IT-Sicherheitsbeauftragter (ITSB) | Datenschutzbeauftragter (DSB) |
| **Schutzziele** | CIA-Triade + Authentizitaet | Rechte der Betroffenen, Zweckbindung, Datenminimierung |
| **Umfang** | Alle Informationen des Unternehmens | Nur personenbezogene Daten |
| **Ueberlappung** | Vertraulichkeit und Integritaet personenbezogener Daten | Technische Sicherheit als Mittel zum Datenschutz |

**Wichtig:** Informationssicherheit ist der **uebergeordnete** Begriff. Datenschutz ist ein **Teilbereich**, der sich auf personenbezogene Daten konzentriert.

---

## TOM – Technische und Organisatorische Massnahmen

**Definition:** TOMs sind Massnahmen, die der Verantwortliche nach Art. 32 DSGVO treffen muss, um ein angemessenes Schutzniveau fuer personenbezogene Daten zu gewaehrleisten.

### TOM-Kategorien

| Kategorie | Beschreibung | Beispiele |
|-----------|-------------|----------|
| **Zutrittskontrolle** | Unbefugte duerfen Raeume mit IT-Systemen nicht physisch betreten | Schluessel, Chipkarte, Codeschloss, Videoaueberwachung |
| **Zugangskontrolle** | Unbefugte duerfen IT-Systeme nicht nutzen | Benutzername + Passwort, 2FA, Bildschirmsperre, Festplattenverschluesselung |
| **Zugriffskontrolle** | Befugte duerfen nur auf die Daten zugreifen, die sie benoetigen | Berechtigungskonzept, Rollenkonzept (RBAC), Need-to-know-Prinzip |
| **Weitergabekontrolle** | Daten duerfen bei der Uebertragung nicht unbefugt gelesen werden | Verschluesselung (TLS, VPN), sichere E-Mail (S/MIME, PGP) |
| **Eingabekontrolle** | Es muss nachvollziehbar sein, wer wann welche Daten eingegeben/geaendert hat | Protokollierung, Logging, Audit-Trail |
| **Auftragskontrolle** | Auftragsverarbeiter duerfen Daten nur nach Weisung verarbeiten | Auftragsverarbeitungsvertrag (AVV), Kontrollen |
| **Verfuegbarkeitskontrolle** | Schutz vor Datenverlust | Backup, USV, Redundanz, Disaster Recovery |
| **Trennungsgebot** | Daten verschiedener Zwecke muessen getrennt verarbeitet werden | Mandantentrennung, getrennte Datenbanken |

### Merkregel fuer die vier wichtigsten Kontrollen

```
  ZUTRITT → Wer darf in den RAUM?
     |       (physisch, Tuer, Gebaeude)
     v
  ZUGANG → Wer darf an das SYSTEM?
     |       (Login, Passwort, 2FA)
     v
  ZUGRIFF → Wer darf welche DATEN sehen?
     |        (Berechtigungen, Rollen)
     v
  WEITERGABE → Wie werden DATEN sicher uebertragen?
                (Verschluesselung, VPN)
```
