# Beispiele: 2.4.06 – Wirksamkeit und Effizienz der umgesetzten TOM pruefen

## Compliance Reports

**Beispiel 1:** Ein mittelstaendisches Unternehmen (150 Mitarbeiter) bereitet sich auf ein ISO-27001-Audit vor. Der IT-Sicherheitsbeauftragte erstellt einen internen Compliance Report.

| Pruefbereich | Soll (ISO 27001) | Ist-Zustand | Bewertung | Massnahme |
|---|---|---|---|---|
| Passwortrichtlinie | Mind. 12 Zeichen, MFA | 8 Zeichen, kein MFA | Nicht konform | MFA einfuehren, Richtlinie anpassen |
| Backup | Taeglich, verschluesselt, extern | Taeglich, unverschluesselt, lokal | Teilweise konform | Verschluesselung + Off-Site-Backup |
| Patch-Management | Kritische Patches in 72h | Monatlicher Patchday | Nicht konform | Automatisiertes Patch-Management |
| Zugangskontrolle | Rollenbasiert (RBAC) | Individuelle Berechtigungen | Teilweise konform | Rollenkonzept einfuehren |
| Logging | Zentral, SIEM, 6 Monate | Lokal, keine Auswertung | Nicht konform | SIEM einfuehren (z.B. Elastic) |

---

## Log Management

**Beispiel 2:** Das SIEM-System eines Onlineshops zeigt folgende Auffaelligkeiten an einem Montagmorgen:

| Uhrzeit | Ereignis | Quelle | Bewertung |
|---|---|---|---|
| 02:14 | 47 fehlgeschlagene SSH-Logins | Firewall-Log | Brute-Force-Angriff |
| 02:31 | Erfolgreicher SSH-Login (Root) | Server-Log | Moeglicher Einbruch |
| 02:33 | Neuer Benutzer „admin2" angelegt | Active Directory | Privilege Escalation |
| 02:40 | 2 GB Upload auf externe IP | DLP-System | Datenexfiltration |
| 03:00 | Firewall-Regel geaendert | Firewall-Log | Backdoor-Verdacht |

**Bewertung:** Typischer Ablauf eines Angriffs (Kill Chain). **Sofortmassnahmen:** Server isolieren, Forensik starten, Firewall-Regeln zuruecksetzen, Benutzer „admin2" sperren, Root-Passwort aendern, Meldung an IT-Sicherheitsbeauftragten.

---

## Zugangskontrolle

**Beispiel 3:** Ein Unternehmen fuehrt Multi-Faktor-Authentifizierung ein. Vergleich vorher/nachher:

| Aspekt | Vorher (nur Passwort) | Nachher (Passwort + TOTP) |
|---|---|---|
| Login-Sicherheit | Gering (Phishing-anfaellig) | Hoch (zweiter Faktor noetig) |
| Phishing-Schutz | Kein Schutz nach Diebstahl | Angreifer braucht auch das Smartphone |
| Brute-Force-Schutz | Nur durch Sperrung | Zusaetzlich durch Einmalcode |
| Benutzerfreundlichkeit | Einfach | Minimaler Mehraufwand (6-stelliger Code) |
| Kosten | Keine | Authenticator-App kostenlos, Token ca. 30-50 EUR |

**Beispiel 4:** Eine Arztpraxis nutzt Chipkarten fuer den Zugang zu PCs mit Patientendaten:

| Ablauf | Beschreibung |
|---|---|
| Chipkarte einstecken | Arzt/MFA steckt persoenliche Chipkarte in Leser |
| PIN eingeben | 6-stellige PIN eingeben (MFA: Besitz + Wissen) |
| Zugang gewaehrt | Zugriff auf Praxis-Software mit rollenbasiertem Profil |
| Chipkarte entfernen | Automatische Sperrung des PCs |
| Audit-Trail | Login wird protokolliert (Wer, Wann, Welches System) |

---

## Zugriffskontrolle

**Beispiel 5:** Berechtigungsmatrix eines KMU:

| Rolle | Kundendaten | Finanzdaten | Personalakten | IT-Administration | E-Mail |
|---|---|---|---|---|---|
| Geschaeftsfuehrung | Lesen | Lesen/Schreiben | Lesen | Kein Zugriff | Vollzugriff |
| Vertrieb | Lesen/Schreiben | Kein Zugriff | Kein Zugriff | Kein Zugriff | Vollzugriff |
| Buchhaltung | Lesen | Lesen/Schreiben | Kein Zugriff | Kein Zugriff | Vollzugriff |
| Personalabteilung | Kein Zugriff | Kein Zugriff | Lesen/Schreiben | Kein Zugriff | Vollzugriff |
| IT-Administration | Kein Zugriff | Kein Zugriff | Kein Zugriff | Vollzugriff | Vollzugriff |
| Praktikant | Kein Zugriff | Kein Zugriff | Kein Zugriff | Kein Zugriff | Lesen/Senden |

**Beispiel 6:** Sichere Entsorgung alter Festplatten beim Austausch von 20 Arbeitsplatz-PCs:

| Schritt | Massnahme | Verantwortlich |
|---|---|---|
| 1 | Inventarisierung aller Festplatten (Seriennummer) | IT-Abteilung |
| 2 | Verschluesselte Laufwerke: Kryptografisch loeschen (Schluessel vernichten) | IT-Admin |
| 3 | Unverschluesselte Laufwerke: 3-fach ueberschreiben (z.B. mit DBAN) | IT-Admin |
| 4 | Festplatten mit sensiblen Daten: physische Vernichtung (Shredder) | Externer Dienstleister |
| 5 | Vernichtungsprotokoll erstellen und archivieren | IT-Sicherheitsbeauftragter |

---

## Zutrittskontrolle

**Beispiel 7:** Sicherheitskonzept fuer einen Serverraum eines Rechenzentrums:

| Sicherheitsschicht | Massnahme | Details |
|---|---|---|
| Gebaeude | Videoanlage | 24/7 Aufzeichnung, Speicherung 30 Tage |
| Eingang | Empfang + Besuchermanagement | Ausweiskontrolle, Besucherausweis mit Ablaufdatum |
| Flur | Chipkarten-Zugang | Nur Mitarbeiter mit Berechtigung |
| Serverraum | Chipkarte + PIN + Protokoll | 4-Augen-Prinzip fuer kritische Wartung |
| Rack | Physisches Schloss | Individuelle Schluessel pro Rack |
| Zusaetzlich | Alarmanlage mit Einbruchsmelder | Meldung an Wachdienst |
| Zusaetzlich | Klima-/Brandmeldeanlage | Loeschanlage (Gas, kein Wasser) |

**Beispiel 8:** Besuchermanagement in einem Buerogebaeude:

| Phase | Prozess |
|---|---|
| Voranmeldung | Besucher wird vom Mitarbeiter per System angemeldet |
| Ankunft | Empfang: Ausweiseise kontrollieren, Besucherausweis ausgeben |
| Begleitung | Besucher wird vom einladenden Mitarbeiter begleitet |
| Zutritt | Nur begleiteter Zugang zu internen Bereichen |
| Abmeldung | Besucherausweis zurueckgeben, Ausgang protokollieren |

---

## Wirksamkeitspruefung in der Praxis

**Beispiel 9:** Jaehrliche Wirksamkeitspruefung der TOM eines Unternehmens (Checkliste):

| TOM-Bereich | Pruefmethode | Ergebnis | Status |
|---|---|---|---|
| Zutrittskontrolle | Begehung, Protokollauswertung | Alle Tueren gesichert, Protokolle lueckenlos | OK |
| Zugangskontrolle | AD-Audit, MFA-Status pruefen | 95% der Konten mit MFA, 5% noch offen | Massnahme noetig |
| Zugriffskontrolle | Berechtigungsreview | 12 verwaiste Konten gefunden | Massnahme noetig |
| Log Management | SIEM-Dashboard, Stichproben | Logs vollstaendig, Korrelation funktioniert | OK |
| Backup | Restore-Test | Wiederherstellung in 2h erfolgreich | OK |
| Patch-Management | Compliance Scan | 3 Server mit kritischem Patch-Rueckstand | Massnahme noetig |
| Awareness | Phishing-Simulation | 18% der Mitarbeiter klickten Link | Schulung noetig |
