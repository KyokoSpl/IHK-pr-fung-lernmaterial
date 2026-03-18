# Beispiele: 1.6.01 – IT-Sicherheit auf Grundschutzniveau

## Beispiel 1: Hybride Verschluesselung (HTTPS)

**Szenario:** Ein Nutzer ruft eine Online-Banking-Seite auf.

**Ablauf:**
1. Browser kontaktiert Server (HTTPS-Anfrage)
2. Server sendet sein Zertifikat mit oeffentlichem Schluessel (asymmetrisch)
3. Browser prueft Zertifikat (Vertrauenskette)
4. Browser erzeugt zufaelligen Session-Key (symmetrisch)
5. Browser verschluesselt Session-Key mit oeffentlichem Schluessel des Servers
6. Server entschluesselt Session-Key mit privatem Schluessel
7. Alle weiteren Daten werden symmetrisch mit Session-Key verschluesselt

→ Asymmetrisch fuer den Schluesselaustausch, symmetrisch fuer die schnelle Datenuebertragung = **hybrid**

---

## Beispiel 2: Schutzzielverletzungen erkennen

| Szenario | Verletztes Schutzziel | Begruendung |
|---|---|---|
| Webserver faellt durch DDoS-Angriff aus | **Verfuegbarkeit** | System nicht erreichbar |
| Angreifer aendert Rechnungsbetrag in Datenbank | **Integritaet** | Daten wurden manipuliert |
| Mitarbeiter liest vertrauliche Personalakten | **Vertraulichkeit** | Unbefugter Zugriff |
| E-Mail mit gefaelschtem Absender | **Authentizitaet** | Absenderidentitaet nicht gesichert |

---

## Beispiel 3: TOM in der Praxis

**Szenario:** Ein IT-Unternehmen verarbeitet Kundendaten und muss TOM nachweisen.

| Kontrolle | Massnahme | Umsetzung |
|---|---|---|
| Zutrittskontrolle | Serverraum absichern | Chipkarte + PIN, Videoüberwachung |
| Zugangskontrolle | Systeme schuetzen | AD-Login, 2FA, Passwort-Policy |
| Zugriffskontrolle | Daten schuetzen | Rollenbasiertes Berechtigungskonzept (RBAC) |
| Weitergabekontrolle | Transport schuetzen | E-Mail-Verschluesselung, VPN |
| Eingabekontrolle | Nachvollziehbarkeit | Audit-Logs, Aenderungsprotokoll |
| Verfuegbarkeit | Ausfallsicherheit | Taegliches Backup, USV, RAID |
| Trennungsgebot | Mandanten trennen | Separate Datenbanken pro Kunde |

---

## Beispiel 4: Betroffenenrechte in der Praxis

**Szenario:** Kunde schreibt an IT-Dienstleister:
> „Ich moechte wissen, welche Daten Sie ueber mich gespeichert haben."

**Reaktion (Auskunftsrecht Art. 15 DSGVO):**
1. Identitaet des Anfragenden pruefen
2. Alle gespeicherten Daten zusammenstellen
3. Innerhalb von 1 Monat antworten
4. Zweck der Verarbeitung, Empfaenger, Speicherdauer mitteilen
5. Auf weitere Rechte hinweisen (Loeschung, Berichtigung)

---

## Beispiel 5: Pseudonymisierung vs. Anonymisierung

**Ausgangsdaten:**

| Name | Alter | Diagnose |
|---|---|---|
| Max Mueller | 34 | Grippe |
| Anna Schmidt | 28 | Allergie |

**Pseudonymisiert:**

| ID | Alter | Diagnose |
|---|---|---|
| P-001 | 34 | Grippe |
| P-002 | 28 | Allergie |

→ Zuordnungstabelle existiert: P-001 = Max Mueller → DSGVO gilt!

**Anonymisiert:**

| Altersgruppe | Diagnose | Anzahl |
|---|---|---|
| 25-35 | Grippe | 1 |
| 25-35 | Allergie | 1 |

→ Kein Rueckschluss auf Personen moeglich → DSGVO gilt NICHT
