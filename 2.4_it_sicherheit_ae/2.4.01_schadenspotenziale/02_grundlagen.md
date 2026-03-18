# Grundlagen: 2.4.01 – Schadenspotenziale von IT-Sicherheitsvorfaellen einschaetzen

## Datenverlust

**Definition:** Unbeabsichtigter oder boesartiger Verlust von Daten, sodass diese nicht mehr verfuegbar oder nutzbar sind.

**Ursachen:**

| Ursache | Beschreibung | Beispiel |
|---|---|---|
| Technisches Versagen | Hardwaredefekt, Speicherausfall | Festplattencrash ohne RAID |
| Menschliches Versagen | Versehentliches Loeschen, Fehlkonfiguration | Admin loescht Produktivdatenbank |
| Cyberangriff | Ransomware, Datendiebstahl | Verschluesselungstrojaner sperrt Dateien |
| Hoehe Gewalt | Brand, Hochwasser, Blitzschlag | Rechenzentrum durch Feuer zerstoert |
| Softwarefehler | Bugs, fehlerhafte Updates | Update korrumpiert Datenbank |

**Folgen von Datenverlust:**
- **Betriebsunterbrechung:** Geschaeftsprozesse stehen still
- **Verstoss gegen Aufbewahrungspflichten:** GoBD, HGB (6-10 Jahre), DSGVO
- **Verlust von Geschaeftsgeheimnissen:** Wettbewerbsnachteil
- **Haftungsrisiken:** Schadensersatzansprueche von Kunden/Partnern

**Gegenmassnahmen:**

| Massnahme | Beschreibung |
|---|---|
| Backup-Strategie | 3-2-1-Regel: 3 Kopien, 2 Medien, 1 extern |
| RAID-Systeme | Redundante Festplatten (RAID 1, 5, 6, 10) |
| Versionierung | Git, Snapshots, Schattenkopien |
| Disaster Recovery | Wiederherstellungsplan mit definierten RTO/RPO |
| Schulung | Sensibilisierung der Mitarbeiter |

**Wichtige Begriffe:**
- **RTO (Recovery Time Objective):** Maximale tolerierbare Ausfallzeit
- **RPO (Recovery Point Objective):** Maximaler tolerierbarer Datenverlust (Zeitspanne)
- **GoBD:** Grundsaetze ordnungsmaessiger Buchfuehrung und Dokumentation

---

## Imageschaden

**Definition:** Verlust der Reputation eines Unternehmens durch oeffentlich bekanntgewordene IT-Sicherheitsvorfaelle.

**Ausloeser:**

| Ausloeser | Beispiel |
|---|---|
| Datenleck | Kundendaten im Darknet veroeffentlicht |
| Ransomware-Angriff | Unternehmen tagelang offline |
| Meldepflichtverletzung | DSGVO-Verstoss wird oeffentlich |
| Social Engineering | CEO-Fraud wird bekannt |
| Insider-Bedrohung | Mitarbeiter entwendet Daten |

**Folgen:**
- **Kundenverlust:** Vertrauen sinkt, Kunden wechseln zur Konkurrenz
- **Aktienkursverlust:** Boersennotierte Unternehmen verlieren Marktwert
- **Geschaeftspartner:** Kooperationen werden beendet oder erschwert
- **Medienberichterstattung:** Negative Presse verstaerkt den Schaden
- **Recruiting:** Fachkraeftegewinnung wird schwieriger

**Gegenmassnahmen:**

| Massnahme | Beschreibung |
|---|---|
| Incident-Response-Plan | Strukturierter Ablauf bei Sicherheitsvorfaellen |
| Krisenkommunikation | Transparente, schnelle Information der Betroffenen |
| Meldepflicht einhalten | DSGVO Art. 33/34: Meldung an Aufsichtsbehoerde innerhalb 72 Stunden |
| Security Awareness | Regeln und Schulungen fuer alle Mitarbeiter |

---

## Wirtschaftlicher Schaden

**Definition:** Direkte und indirekte finanzielle Verluste durch IT-Sicherheitsvorfaelle.

**Schadenskategorien:**

| Kategorie | Beschreibung | Beispiel |
|---|---|---|
| Direkte Kosten | Sofort anfallende Kosten | Wiederherstellung, Forensik, Hardware-Ersatz |
| Indirekte Kosten | Folgekosten | Produktionsausfall, Umsatzeinbussen |
| Bussgelder | Strafen durch Aufsichtsbehoerden | DSGVO: bis 20 Mio. EUR oder 4% Jahresumsatz |
| Vertragsstrafen | Verletzung von SLAs | Nichtverfuegbarkeit gemeldeter Dienste |
| Rechtskosten | Anwalt, Gericht | Klagen von Betroffenen |
| Versicherung | Kosten fuer Cyber-Versicherung | Praemien steigen nach Vorfall |

**Typische Schadenshoehen (Orientierung):**

| Szenario | Geschaetzte Kosten |
|---|---|
| Ransomware-Angriff (KMU) | 50.000 – 500.000 EUR |
| Datenleck (1.000 Datensaetze) | 100.000 – 1.000.000 EUR |
| DDoS-Angriff (1 Tag Ausfall) | 10.000 – 100.000 EUR/Tag |
| DSGVO-Bussgeld (schwer) | Bis 20.000.000 EUR |

**Berechnung wirtschaftlicher Schaeden:**
- **Ausfallkosten = Ausfallzeit × Kosten pro Stunde**
- **TCO (Total Cost of Ownership):** Gesamtkosten einer Sicherheitsloesung vs. potenzieller Schaden
- **ROI von Sicherheitsmassnahmen:** Investition in Sicherheit vs. vermiedener Schaden

## Querverweise
- → 1.6.01 (Schutzziele: Vertraulichkeit, Integritaet, Verfuegbarkeit)
- → 1.6.04 (Sicherheitskonzept, Risikoanalyse)
- → 2.4.02 (Praeventive Massnahmen gegen Bedrohungen)
