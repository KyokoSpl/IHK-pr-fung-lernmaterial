# 4.5.02 – Informationstechnische Schutzziele bei der Kommunikation: Vertiefung

## Vergleich: Social-Engineering-Methoden

| Methode | Angriffsvektor | Ziel | Erkennung | Schwierigkeitsgrad |
|---------|---------------|------|-----------|-------------------|
| Phishing | E-Mail | Zugangsdaten, Malware | Absender pruefen, URL pruefen | Niedrig |
| Spear-Phishing | Gezielte E-Mail | Bestimmte Person/Abteilung | Schwieriger – personalisiert | Mittel |
| Whaling | E-Mail/Telefon | C-Level-Management | Sehr schwer – sehr gezielt | Hoch |
| Pretexting | Telefon/persoenlich | Informationen, Zugang | Identitaet verifizieren | Mittel |
| Baiting | Physisch (USB etc.) | Systemzugang | Unbekannte Medien ignorieren | Niedrig |
| Tailgating | Physisch (Tuer) | Gebaeudezugang | Ausweiskontrolle, Challenge | Niedrig |
| Vishing | Telefon | Zugangsdaten, Infos | Rueckruf ueber offizielle Nummer | Mittel |
| Quid pro Quo | Telefon/E-Mail | Zugang gegen "Service" | Angebote hinterfragen | Mittel |

## Vergleich: E-Mail-Verschluesselungsverfahren

| Kriterium | S/MIME | PGP/GPG |
|-----------|--------|---------|
| Vertrauensmodell | Hierarchisch (CA) | Web of Trust (dezentral) |
| Zertifikate | Von Zertifizierungsstelle ausgestellt | Selbst erstellt, von anderen signiert |
| Verbreitung | Unternehmen, Behoerden | Technik-affine Nutzer, Open Source |
| Integration | In den meisten Mail-Clients nativ | Oft Plugin erforderlich |
| Verschluesselung | Asymmetrisch (RSA/ECC) | Asymmetrisch (RSA/ECC) |
| Signatur | Ja | Ja |
| Kosten | Zertifikat oft kostenpflichtig | Kostenlos (GPG) |

## Ablauf eines Phishing-Angriffs

```
+------------------------------------------------------------------+
|                   PHISHING-ANGRIFF: ABLAUF                        |
+------------------------------------------------------------------+
|                                                                   |
|  1. AUFKLAERUNG (Reconnaissance)                                  |
|     +-------------------------------------------+                 |
|     | Angreifer sammelt Informationen ueber Ziel |                |
|     | - Social Media (LinkedIn, Xing)            |                |
|     | - Unternehmenswebsite                       |                |
|     | - OSINT-Tools                               |                |
|     +-------------------------------------------+                 |
|                        |                                          |
|                        v                                          |
|  2. VORBEREITUNG (Weaponization)                                  |
|     +-------------------------------------------+                 |
|     | Angreifer erstellt Phishing-Material        |                |
|     | - Gefaelschte E-Mail                        |                |
|     | - Fake-Login-Seite (Klon)                   |                |
|     | - Aehnliche Domain (z.B. rnicro-soft.com)   |                |
|     +-------------------------------------------+                 |
|                        |                                          |
|                        v                                          |
|  3. ZUSTELLUNG (Delivery)                                         |
|     +-------------------------------------------+                 |
|     | E-Mail wird an Ziel gesendet               |                |
|     | - Dringlichkeit erzeugen                    |                |
|     | - Autoritaet vortaeuschen                   |                |
|     | - Neugier wecken                            |                |
|     +-------------------------------------------+                 |
|                        |                                          |
|                        v                                          |
|  4. AUSBEUTUNG (Exploitation)                                     |
|     +-------------------------------------------+                 |
|     | Opfer klickt Link / oeffnet Anhang          |                |
|     | - Gibt Zugangsdaten ein                     |                |
|     | - Malware wird installiert                  |                |
|     | - Makro wird ausgefuehrt                    |                |
|     +-------------------------------------------+                 |
|                        |                                          |
|                        v                                          |
|  5. SCHADEN (Impact)                                              |
|     +-------------------------------------------+                 |
|     | - Datenverlust / Datendiebstahl             |                |
|     | - Ransomware-Verschluesselung               |                |
|     | - Laterale Bewegung im Netzwerk             |                |
|     | - Finanzieller Schaden                      |                |
|     +-------------------------------------------+                 |
|                                                                   |
+------------------------------------------------------------------+
```

## Vier-Seiten-Modell in der IT-Kommunikation

```
+------------------------------------------------------------------+
|        VIER-SEITEN-MODELL (Schulz von Thun)                       |
|                                                                   |
|  Beispiel: "Das Deployment ist fehlgeschlagen."                   |
|                                                                   |
|                    SACHINHALT                                      |
|              "Das Deployment hat                                  |
|               nicht funktioniert"                                 |
|                      ^                                            |
|                      |                                            |
|  SELBSTOFFENBARUNG --+-- APPELL                                   |
|  "Ich bin besorgt/   |   "Bitte kuemmere                         |
|   frustriert"        |    dich darum /                            |
|                      |    Hilf mir"                               |
|                      |                                            |
|                      v                                            |
|                  BEZIEHUNG                                        |
|              "Du bist verantwortlich /                            |
|               Wir haben ein gemeinsames                          |
|               Problem"                                           |
|                                                                   |
+------------------------------------------------------------------+
```

## Security-Awareness-Programm: Bausteine

```
+------------------------------------------------------------------+
|              SECURITY AWARENESS PROGRAMM                          |
+------------------------------------------------------------------+
|                                                                   |
|  +------------------+  +------------------+  +------------------+ |
|  | SCHULUNGEN       |  | SIMULATIONEN     |  | RICHTLINIEN      | |
|  |                  |  |                  |  |                  | |
|  | - E-Learning     |  | - Phishing-Tests |  | - Social-Media-  | |
|  | - Praesenz       |  | - Social-Eng.-   |  |   Policy         | |
|  | - Onboarding     |  |   Tests          |  | - Passwort-      | |
|  | - Jährliche      |  | - USB-Drop-Tests |  |   Richtlinie     | |
|  |   Auffrischung   |  |                  |  | - E-Mail-        | |
|  +------------------+  +------------------+  |   Richtlinie     | |
|                                              +------------------+ |
|  +------------------+  +------------------+  +------------------+ |
|  | KOMMUNIKATION    |  | GAMIFICATION     |  | MESSUNG          | |
|  |                  |  |                  |  |                  | |
|  | - Newsletter     |  | - Quiz, Badges   |  | - Phishing-      | |
|  | - Poster/Flyer   |  | - Wettbewerbe    |  |   Klickrate      | |
|  | - Intranet-News  |  | - Escape Rooms   |  | - Meldequote     | |
|  | - Warnmeldungen  |  | - Szenarien      |  | - Schulungs-     | |
|  |                  |  |                  |  |   teilnahme      | |
|  +------------------+  +------------------+  +------------------+ |
|                                                                   |
+------------------------------------------------------------------+
```

## Typische Pruefungsaspekte

| Aspekt | Was wird geprueft? | Worauf achten? |
|--------|-------------------|----------------|
| Social Engineering | Methoden benennen und unterscheiden | Phishing vs. Spear-Phishing vs. Whaling |
| Phishing erkennen | Merkmale einer Phishing-Mail | Absenderadresse, Links, Dringlichkeit, Rechtschreibung |
| E-Mail-Sicherheit | S/MIME vs. PGP erklaeren | Vertrauensmodell, Signatur vs. Verschluesselung |
| BCC vs. CC | Unterschied und DSGVO-Relevanz | BCC bei externen Verteilern Pflicht |
| Loyalitaetspflicht | Grenzen der Meinungsfreiheit | Keine Schmaehurkritik, keine Geschaeftsgeheimnisse |
| Social-Media-Policy | Typische Inhalte benennen | Private vs. dienstliche Nutzung, Vertraulichkeit |
| Netiquette | Regeln fuer dienstliche E-Mails | Betreff, Struktur, Anrede, Antwortverhalten |
| Security Awareness | Massnahmen und Ziel benennen | Schulungen, Simulationen, Richtlinien |
| Vier-Seiten-Modell | Auf Kommunikationssituation anwenden | Jede Nachricht hat 4 Seiten |

## Haeufige Fehler

| Fehler | Warum falsch? | Richtig |
|--------|--------------|---------|
| "Phishing nur per E-Mail" | Gibt es auch per SMS (Smishing), Telefon (Vishing), Social Media | Alle Kanaele bedenken |
| "Social Engineering ist nur online" | Tailgating, Dumpster Diving sind physisch | Online UND physisch |
| "BCC ist immer besser als CC" | Intern darf/sollte CC genutzt werden | BCC vor allem bei externen Verteilern |
| "Meinungsfreiheit schuetzt alles" | Loyalitaetspflicht begrenzt Meinungsfreiheit im Arbeitsverhaeltnis | Abwaegung noetig, keine Schmaehurkritik |
| "S/MIME und PGP sind das Gleiche" | Unterschiedliche Vertrauensmodelle | CA-basiert vs. Web of Trust |
| "Verschluesselung = Signatur" | Verschluesselung schuetzt Vertraulichkeit, Signatur schuetzt Integritaet/Authentizitaet | Beides zusammen einsetzen |
| "Passwort-Komplexitaet ist wichtiger als Laenge" | Laenge erhoet Sicherheit exponentiell | Passphrasen bevorzugen (z.B. 4+ Woerter) |
| "Security Awareness einmal reicht" | Bedrohungen aendern sich, Wissen nimmt ab | Regelmaessige Auffrischung noetig |
