# Vertiefung: 2.4.06 – Wirksamkeit und Effizienz der umgesetzten TOM pruefen

## Zutritt, Zugang, Zugriff – Abgrenzung

| Kontrollart | Schuetzt vor | Ebene | Beispiel |
|---|---|---|---|
| Zutrittskontrolle | Unbefugtem physischem Betreten | Gebaeude/Raum | Chipkarte am Serverraum |
| Zugangskontrolle | Unbefugtem Einloggen in Systeme | IT-System | Passwort + MFA am PC |
| Zugriffskontrolle | Unbefugtem Datenzugriff | Daten/Ressourcen | Rollenkonzept, Verschluesselung |

**Merkhilfe:**
```
Zutrittskontrolle:  Wer darf in den RAUM?
Zugangskontrolle:   Wer darf an das SYSTEM?
Zugriffskontrolle:  Wer darf an die DATEN?
```

## Zusammenspiel der TOM-Kontrollbereiche

```
+------------------------------------------------------+
|                  Physische Ebene                       |
|  +------------------------------------------------+  |
|  |             Zutrittskontrolle                   |  |
|  |  Alarmanlage | Video | Chipkarte | Besucher     |  |
|  +------------------------+------------------------+  |
|                           |                            |
|  +------------------------v------------------------+  |
|  |             Zugangskontrolle                    |  |
|  |  Passwort | MFA | Biometrie | Bildschirmsperre  |  |
|  +------------------------+------------------------+  |
|                           |                            |
|  +------------------------v------------------------+  |
|  |             Zugriffskontrolle                   |  |
|  |  Rollen | ACL | Verschluesselung | Loeschung    |  |
|  +------------------------+------------------------+  |
|                           |                            |
|  +------------------------v------------------------+  |
|  |          Monitoring & Compliance                |  |
|  |  Log Management | SIEM | Compliance Reports     |  |
|  +-------------------------------------------------+  |
+-------------------------------------------------------+
```

## Compliance-Kreislauf (PDCA)

```
+------------------+        +------------------+
|   Plan           |        |   Do             |
|   (TOM planen,   |------->|   (TOM           |
|    Richtlinien)  |        |    umsetzen)     |
+--------+---------+        +--------+---------+
         ^                           |
         |                           v
+--------+---------+        +--------+---------+
|   Act            |        |   Check          |
|   (Verbessern,   |<-------|   (Pruefen:      |
|    anpassen)     |        |    Audit, Logs,  |
+------------------+        |    Reports)      |
                             +------------------+
```

## Log-Analyse: Verdaechtige Muster

| Muster | Moeglicher Vorfall | Massnahme |
|---|---|---|
| Viele fehlgeschlagene Logins | Brute-Force-Angriff | IP sperren, MFA pruefen |
| Login ausserhalb Geschaeftszeiten | Unbefugter Zugriff | Konto pruefen, Mitarbeiter kontaktieren |
| Grosser Datentransfer nach extern | Datenexfiltration | DLP pruefen, Konto sperren |
| Rechteaenderung ohne Ticket | Privilege Escalation | Aenderung rueckgaengig, untersuchen |
| Zugriff auf viele verschiedene Dateien | Insider-Bedrohung / Ransomware | Konto isolieren, Forensik |
| Wiederholte 403/404-Fehler im Webserver | Schwachstellen-Scan | IP blockieren, WAF pruefen |

## Biometrische Verfahren im Vergleich

| Verfahren | Sicherheit | Akzeptanz | Kosten | Schwaeche |
|---|---|---|---|---|
| Fingerabdruck | Hoch | Hoch | Gering | Faelschbar mit Attrappen |
| Gesichtserkennung | Hoch | Mittel | Mittel | Foto/Maske (ohne 3D-Erkennung) |
| Iris-Scan | Sehr hoch | Gering | Hoch | Geringe Nutzerakzeptanz |
| Venenmuster | Sehr hoch | Mittel | Hoch | Kaum faelschbar |
| Stimmerkennung | Mittel | Hoch | Gering | Umgebungsgeraeusche, Aufnahmen |

**Datenschutz bei Biometrie:** Biometrische Daten sind **besondere Kategorien personenbezogener Daten** (DSGVO Art. 9) → Einwilligung oder betriebliche Erforderlichkeit noetig, strenge Schutzanforderungen.

## Verschluesselungsverfahren fuer die Zugriffskontrolle

| Verfahren | Typ | Schluessellaenge | Einsatz |
|---|---|---|---|
| AES-256 | Symmetrisch | 256 Bit | Festplattenverschluesselung, Dateiverschluesselung |
| RSA | Asymmetrisch | 2048-4096 Bit | Zertifikate, Schluesseltausch |
| TLS 1.3 | Hybrid | Variabel | HTTPS, E-Mail, VPN |
| PGP/GPG | Hybrid | Variabel | E-Mail-Verschluesselung |

## Wirksamkeitspruefung der TOM – Methoden

| Methode | Beschreibung | Haeufigkeit |
|---|---|---|
| Internes Audit | Selbstpruefung anhand definierter Checklisten | Quartalsweise |
| Externes Audit | Pruefung durch unabhaengige Stelle (ISO 27001) | Jaehrlich |
| Log-Auswertung | Analyse der Protokolldaten mit SIEM | Kontinuierlich |
| Penetrationstest | Kontrollierter Angriff zur Schwachstellensuche | Jaehrlich |
| Phishing-Simulation | Test der Mitarbeiter-Awareness | Quartalsweise |
| Compliance Scan | Automatisierte Pruefung der Konfiguration | Woechentlich |
| Notfalluebung | Simulation eines Sicherheitsvorfalls | Jaehrlich |

## Typische Pruefungsaspekte
- Unterschied Zutritts-, Zugangs- und Zugriffskontrolle mit Beispielen
- Log-Management: Warum sind Logs wichtig? SIEM erklaeren
- Compliance Report: Aufbau und Zweck beschreiben
- Biometrische Verfahren vergleichen und Datenschutz beruecksichtigen
- Verschluesselung von Datentraegern: BitLocker, LUKS benennen
- Sichere Datentraegerloeschung: Methoden und deren Sicherheitsstufe
- Passwortrichtlinie: aktuelle BSI-Empfehlung kennen

## Haeufige Fehler
- Zugangs- und Zugriffskontrolle verwechselt → Zugang = System-Login, Zugriff = Datenzugriff
- Videoueberwachung = grenzenlos moeglich → DSGVO und Betriebsratsvereinbarung beachten
- Schnellformatierung = sicher → Daten sind wiederherstellbar, Ueberschreiben oder physische Vernichtung noetig
- Biometrie = 100% sicher → Fingerabdruck kann gefaelscht werden, Biometrie als Teil von MFA nutzen
- Logs muessen ewig gespeichert werden → DSGVO: Datensparsamkeit, Aufbewahrungsfristen definieren
