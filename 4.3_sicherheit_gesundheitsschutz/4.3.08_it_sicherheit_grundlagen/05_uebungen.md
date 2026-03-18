# Uebungen: 4.3.08 – Grundlagen der IT-Sicherheit kennen und umsetzen

## Aufgabe 1
Erklaere die vier Schutzziele der Informationssicherheit (CIA + Authentizitaet) und gib je ein praxisnahes Beispiel.

## Aufgabe 2
Ordne die folgenden Massnahmen der korrekten TOM-Kategorie zu:
- a) Chipkarten-Zugang zum Serverraum
- b) Passwortrichtlinie mit 2-Faktor-Authentifizierung
- c) Rollenbasiertes Berechtigungskonzept (RBAC)
- d) HTTPS-Verschluesselung fuer die Webanwendung
- e) Taegliches Backup auf einem externen Medium

## Aufgabe 3
Erklaere den Unterschied zwischen Zutrittskontrolle, Zugangskontrolle und Zugriffskontrolle. Gib je ein Beispiel.

## Aufgabe 4
Nenne die vier BSI-Standards (200-1 bis 200-4) mit ihrem jeweiligen Schwerpunkt.

## Aufgabe 5
Erklaere den Unterschied zwischen Datenschutz und Informationssicherheit. Wer ist jeweils verantwortlich?

## Aufgabe 6
Nenne fuenf der sieben Grundsaetze der Datenverarbeitung nach Art. 5 DSGVO.

## Aufgabe 7
Ein Unternehmen wird Opfer eines Ransomware-Angriffs. Alle Server werden verschluesselt und sind nicht mehr erreichbar. Welche Schutzziele sind verletzt? Welche TOM haetten den Schaden begrenzen koennen?

## Aufgabe 8
Nenne drei Unterschiede zwischen ISO 27001 und BSI IT-Grundschutz.

## Aufgabe 9
Ein Mitarbeiter erhaelt eine E-Mail, die angeblich von der Geschaeftsfuehrung stammt und ihn auffordert, 10.000 EUR zu ueberweisen (CEO-Fraud). Welches Schutzziel ist hier bedroht? Welche Massnahmen koennen helfen?

## Aufgabe 10
Ordne die folgenden Szenarien dem verletzten Schutzziel zu:
- a) Ein Mitarbeiter aendert unbemerkt einen Datensatz in der Kundendatenbank
- b) Der Webserver faellt durch einen Hardwaredefekt fuer 12 Stunden aus
- c) Ein ehemaliger Mitarbeiter hat noch Zugriff auf vertrauliche Projektdaten
- d) Eine Phishing-Mail wird im Namen des Unternehmens an Kunden verschickt

---
---

# Loesungen

## Aufgabe 1
| Schutzziel | Definition | Beispiel |
|-----------|-----------|---------|
| **Vertraulichkeit** | Nur Befugte haben Zugriff auf Informationen | Verschluesselung der Kundendatenbank, nur Vertrieb hat Zugriff |
| **Integritaet** | Daten sind vollstaendig und unveraendert | Pruefsummen bei Software-Downloads sichern Unveraendertheit |
| **Verfuegbarkeit** | Systeme/Daten sind bei Bedarf zugaenglich | Redundanter Server stellt sicher, dass der Online-Shop immer erreichbar ist |
| **Authentizitaet** | Echtheit von Daten/Personen ist nachweisbar | Digitale Signatur bei E-Mails belegt den Absender |

## Aufgabe 2
- a) **Zutrittskontrolle** – physischer Zugang zum Serverraum
- b) **Zugangskontrolle** – Anmeldung am IT-System
- c) **Zugriffskontrolle** – Berechtigung auf bestimmte Daten
- d) **Weitergabekontrolle** – sichere Datenuebertragung
- e) **Verfuegbarkeitskontrolle** – Schutz vor Datenverlust

## Aufgabe 3
| Kontrolle | Schutzobjekt | Frage | Beispiel |
|-----------|-------------|-------|---------|
| **Zutrittskontrolle** | Raeume/Gebaeude | Wer darf physisch hinein? | Chipkarte fuer den Serverraum |
| **Zugangskontrolle** | IT-Systeme | Wer darf sich am System anmelden? | Passwort + 2FA fuer den PC-Login |
| **Zugriffskontrolle** | Daten/Informationen | Wer darf welche Daten sehen/aendern? | Nur die Buchhaltung darf Gehaltsdaten einsehen |

## Aufgabe 4
| Standard | Schwerpunkt |
|----------|-------------|
| **BSI-Standard 200-1** | Managementsysteme fuer Informationssicherheit (ISMS) |
| **BSI-Standard 200-2** | IT-Grundschutz-Methodik (Basis-/Standard-/Kern-Absicherung) |
| **BSI-Standard 200-3** | Risikomanagement (Risikoanalyse und -behandlung) |
| **BSI-Standard 200-4** | Business Continuity Management (Notfallmanagement) |

## Aufgabe 5
| Aspekt | Datenschutz | Informationssicherheit |
|--------|------------|----------------------|
| Schutzobjekt | Personenbezogene Daten | Alle Informationen |
| Rechtsgrundlage | DSGVO, BDSG | BSI-Gesetz, ISO 27001 |
| Ziel | Schutz der informationellen Selbstbestimmung | Schutz vor Verlust, Manipulation, unbefugtem Zugriff |
| Verantwortlich | **Datenschutzbeauftragter (DSB)** | **IT-Sicherheitsbeauftragter (ITSB)** |

## Aufgabe 6
1. **Rechtmaessigkeit** – Verarbeitung nur mit Rechtsgrundlage
2. **Zweckbindung** – Nur fuer festgelegte Zwecke
3. **Datenminimierung** – Nur so viele Daten wie noetig
4. **Richtigkeit** – Daten muessen korrekt und aktuell sein
5. **Speicherbegrenzung** – Loeschung nach Zweckerfuellung
(Weitere: Integritaet und Vertraulichkeit, Rechenschaftspflicht)

## Aufgabe 7
**Verletzte Schutzziele:**
- **Verfuegbarkeit:** Server sind nicht mehr erreichbar (verschluesselt)
- **Integritaet:** Daten wurden durch die Ransomware manipuliert (verschluesselt)
- **Vertraulichkeit:** Ggf. auch verletzt, wenn der Angreifer Daten exfiltriert hat (Double Extortion)

**TOM, die den Schaden begrenzt haetten:**
- **Verfuegbarkeitskontrolle:** Regelmaessiges Backup (3-2-1-Regel), offline/offsite-Backup
- **Zugangskontrolle:** Starke Passwörter, 2FA haetten den initialen Zugang erschwert
- **Organisatorisch:** Awareness-Schulung (Phishing als haeufigster Angriffsvektor)
- **Technisch:** Netzwerksegmentierung (Ausbreitung begrenzen), Endpoint Detection & Response (EDR)

## Aufgabe 8
| Aspekt | ISO 27001 | BSI IT-Grundschutz |
|--------|-----------|-------------------|
| **Herausgeber** | ISO (international) | BSI (deutsch) |
| **Ansatz** | Risikobasiert (generisch) | Massnahmenbasiert (konkrete Bausteine) |
| **Detailgrad** | Abstrakt (Anforderungen formuliert) | Sehr detailliert (Umsetzungshinweise fuer jeden Baustein) |

## Aufgabe 9
- **Bedrohtes Schutzziel:** **Authentizitaet** – der Absender gibt sich als jemand anderes aus
- **Massnahmen:**
  - Vier-Augen-Prinzip bei Ueberweisungen ueber einem Schwellenwert
  - Rueckbestaetiung ueber einen zweiten Kanal (Telefon, persoenlich)
  - Awareness-Schulung zu Social Engineering / CEO-Fraud
  - E-Mail-Authentifizierung (DKIM, SPF, DMARC) implementieren
  - Warnsystem fuer externe E-Mails mit internem Absendernamen

## Aufgabe 10
- a) **Integritaet** – Daten wurden unbefugt veraendert
- b) **Verfuegbarkeit** – System ist nicht erreichbar
- c) **Vertraulichkeit** – Unbefugter hat Zugriff auf vertrauliche Daten
- d) **Authentizitaet** – Absender ist gefaelscht (Phishing im Namen des Unternehmens)
