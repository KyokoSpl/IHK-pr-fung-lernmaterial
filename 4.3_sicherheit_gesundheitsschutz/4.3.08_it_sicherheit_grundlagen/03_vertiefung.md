# Vertiefung: 4.3.08 – Grundlagen der IT-Sicherheit kennen und umsetzen

## CIA-Triade – Vertiefung und Bedrohungsszenarien

```
                    VERTRAULICHKEIT
                   (Confidentiality)
                         /\
                        /  \
                       /    \
                      / CIA  \
                     / Triade \
                    /          \
                   /____________\
     INTEGRITAET                  VERFUEGBARKEIT
     (Integrity)                  (Availability)

  + AUTHENTIZITAET (Authenticity)
```

### Bedrohungen pro Schutzziel

| Schutzziel | Bedrohung | Beispiel | Gegenmassnahme |
|-----------|-----------|---------|----------------|
| Vertraulichkeit | Unbefugter Zugriff | Hacker liest Kundendatenbank | Verschluesselung, Zugriffsrechte |
| Vertraulichkeit | Social Engineering | Phishing-Mail, Telefonbetrug | Awareness-Schulung |
| Integritaet | Datenmanipulation | SQL-Injection veraendert Daten | Input-Validierung, Pruefsummen |
| Integritaet | Man-in-the-Middle | Manipulation bei der Uebertragung | TLS, digitale Signaturen |
| Verfuegbarkeit | DDoS-Angriff | Server nicht erreichbar | Redundanz, Cloud-Schutz, Rate Limiting |
| Verfuegbarkeit | Hardwareausfall | Festplattendefekt | RAID, Backup, USV |
| Authentizitaet | Identitaetsdiebstahl | Gestohlene Login-Daten | 2FA, Zertifikate |
| Authentizitaet | Spoofing | Gefaelschte Absenderadresse | DKIM, SPF, DMARC |

## BSI IT-Grundschutz – Vorgehensmodell

```
  +-------------------+
  | 1. ISMS aufbauen  |  BSI-Standard 200-1
  | (Managementsystem)|
  +--------+----------+
           |
           v
  +-------------------+
  | 2. Vorgehensweise |  BSI-Standard 200-2
  | waehlen:          |
  | - Basis           |
  | - Standard        |
  | - Kern            |
  +--------+----------+
           |
           v
  +-------------------+
  | 3. Modellierung   |  IT-Grundschutz-Kompendium
  | Bausteine zuordnen|  (Prozess-/System-Bausteine)
  +--------+----------+
           |
           v
  +-------------------+
  | 4. IT-Grundschutz-|  Soll-Ist-Vergleich
  | Check             |  Umsetzungsstatus pruefen
  +--------+----------+
           |
           v
  +-------------------+
  | 5. Risikoanalyse  |  BSI-Standard 200-3
  | (ergaenzend)      |  Fuer hohen/sehr hohen Schutzbedarf
  +--------+----------+
           |
           v
  +-------------------+
  | 6. Massnahmen     |  Umsetzung und Ueberwachung
  | umsetzen          |  Kontinuierliche Verbesserung
  +-------------------+
```

## IT-Grundschutz-Kompendium – Bausteinstruktur

| Schicht | Bezeichnung | Beispiel-Bausteine |
|---------|-------------|-------------------|
| ISMS | Informationssicherheitsmanagement | ISMS.1 Sicherheitsmanagement |
| ORP | Organisation und Personal | ORP.1 Organisation, ORP.4 Identitaetsmanagement |
| CON | Konzeption | CON.1 Kryptokonzept, CON.3 Datensicherungskonzept |
| OPS | Betrieb | OPS.1.1.3 Patch-Management, OPS.1.1.4 Malware-Schutz |
| DER | Detektion und Reaktion | DER.1 Detektion, DER.2.1 Incident Management |
| APP | Anwendungen | APP.1.1 Office, APP.5.3 E-Mail |
| SYS | IT-Systeme | SYS.1.1 Server, SYS.2.1 Client |
| IND | Industrielle IT | IND.1 Prozessleit-/Automatisierungstechnik |
| NET | Netze | NET.1.1 Netzarchitektur, NET.3.1 Router |
| INF | Infrastruktur | INF.1 Gebaeude, INF.2 Rechenzentrum |

## TOM – Vertiefung: Zutrittskontrolle vs. Zugangskontrolle vs. Zugriffskontrolle

| Aspekt | Zutrittskontrolle | Zugangskontrolle | Zugriffskontrolle |
|--------|-------------------|------------------|-------------------|
| Schutzobjekt | Raeume / Gebaeude | IT-Systeme | Daten / Informationen |
| Frage | Wer darf **hinein**? | Wer darf sich **anmelden**? | Wer darf **was sehen/aendern**? |
| Physisch/Logisch | Physisch | Logisch | Logisch |
| Beispiele | Schloss, Chipkarte, Pfoertner | Passwort, 2FA, Biometrie | RBAC, ACL, Need-to-know |
| IT-Bezug | Serverraum, Rechenzentrum | Login am PC, VPN-Zugang | Dateiberechtigung, DB-Rechte |

## DSGVO und IT-Sicherheit – Zusammenhang

```
  DSGVO Art. 5 (Grundsaetze)
       |
       +-- Integritaet und Vertraulichkeit
       |      |
       |      v
       +-- Art. 32 DSGVO: Sicherheit der Verarbeitung
              |
              v
          TOM (Technische und Organisatorische Massnahmen)
              |
              +-- Zutrittskontrolle
              +-- Zugangskontrolle
              +-- Zugriffskontrolle
              +-- Weitergabekontrolle
              +-- Eingabekontrolle
              +-- Auftragskontrolle
              +-- Verfuegbarkeitskontrolle
              +-- Trennungsgebot
```

## Vergleich: ISO 27001 vs. BSI IT-Grundschutz

| Aspekt | ISO 27001 | BSI IT-Grundschutz |
|--------|-----------|-------------------|
| Herausgeber | ISO (international) | BSI (deutsch) |
| Geltungsbereich | International | Primaer Deutschland |
| Ansatz | Risikobasiert (generisch) | Massnahmenbasiert (konkrete Bausteine) |
| Detailgrad | Abstrakt (Anforderungen) | Sehr detailliert (Umsetzungshinweise) |
| Zertifizierung | ISO 27001-Zertifikat | ISO 27001-Zertifikat auf Basis IT-Grundschutz |
| Kosten | Geringer (weniger Detailarbeit) | Hoeher (umfangreiche Dokumentation) |

## Typische Pruefungsaspekte

- CIA-Triade erklaeren und mit Beispielen belegen
- Unterschied Datenschutz vs. Informationssicherheit
- TOM-Kategorien benennen und unterscheiden (Zutritt/Zugang/Zugriff/Weitergabe)
- DSGVO Art. 5 Grundsaetze nennen
- BSI-Standards 200-1/200-2/200-3/200-4 zuordnen
- Drei Vorgehensweisen des BSI-Grundschutzes unterscheiden
- IT-Sicherheitskonzept: Bestandteile benennen

## Haeufige Fehler

| Fehler | Richtigstellung |
|--------|----------------|
| Datenschutz = Informationssicherheit | Datenschutz schuetzt personenbezogene Daten; Informationssicherheit schuetzt ALLE Informationen |
| CIA steht fuer den US-Geheimdienst | Im IT-Kontext: Confidentiality, Integrity, Availability |
| Zutrittskontrolle = Zugangskontrolle | Zutritt = physisch (Raum); Zugang = logisch (System) |
| DSGVO gilt nur in Deutschland | DSGVO ist eine EU-Verordnung, gilt in allen EU-Mitgliedstaaten |
| BSI-Grundschutz ist Pflicht fuer alle | BSI-Grundschutz ist eine Empfehlung/Standard, keine gesetzliche Pflicht (ausser fuer Bundesbehoerden) |
| Verschluesselung allein genuegt als TOM | TOMs umfassen viele Massnahmen (physisch, organisatorisch, technisch) |
| IT-Sicherheitsbeauftragter = Datenschutzbeauftragter | Zwei verschiedene Rollen mit unterschiedlichen Aufgaben und Rechtsgrundlagen |
| Authentifizierung = Authentizitaet | Authentifizierung ist der Prozess der Identitaetspruefung; Authentizitaet ist das Schutzziel |
