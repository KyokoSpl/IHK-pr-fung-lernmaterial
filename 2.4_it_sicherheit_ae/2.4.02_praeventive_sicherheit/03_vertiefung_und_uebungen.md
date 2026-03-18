# Vertiefung und Uebungen: 2.4.02 – Praeventive IT-Sicherheitsmassnahmen

## Vertiefung

### Vergleich der Bedrohungsszenarien

| Kriterium | Datendiebstahl | Phishing | Ransomware |
|---|---|---|---|
| Angriffstyp | Technisch + Social | Primaer Social | Technisch + Social |
| Hauptziel | Daten exfiltrieren | Zugangsdaten stehlen | Loesegeld erpressen |
| Primaeres Schutzziel | Vertraulichkeit | Authentizitaet | Verfuegbarkeit |
| Wichtigste Massnahme | Verschluesselung, DLP | MFA, Awareness | Backup, EDR |
| Erkennung | DLP, SIEM-Logs | Spamfilter, Nutzer | EDR, Anomalie-Erkennung |

### Zusammenhang der Massnahmen

```
+-------------------------------+
|     Praeventive Massnahmen    |
+-------------------------------+
        |           |           |
   +----+----+ +----+----+ +---+----+
   | Techni- | | Organi- | | Perso- |
   | sche    | | satori- | | nelle  |
   | Massn.  | | sche    | | Massn. |
   +---------+ +---------+ +--------+
   | Firewall| | Richt-  | | Schu-  |
   | VPN     | | linien  | | lungen |
   | MFA     | | Notfall-| | Aware- |
   | EDR     | | plan    | | ness   |
   | Backup  | | Melde-  | | Phish- |
   | Patch-  | | kette   | | ing-   |
   | Mgmt.   | |         | | Tests  |
   +---------+ +---------+ +--------+
```

### Multi-Faktor-Authentifizierung (MFA) im Detail

| Faktor | Kategorie | Beispiel |
|---|---|---|
| Wissen | Etwas, das man weiss | Passwort, PIN |
| Besitz | Etwas, das man hat | Smartphone (TOTP), Hardware-Token (YubiKey) |
| Biometrie | Etwas, das man ist | Fingerabdruck, Gesichtserkennung |
| Standort | Wo man ist | Geo-IP, Netzwerkstandort |

**MFA = mindestens zwei unterschiedliche Faktorkategorien**

### E-Mail-Authentifizierung: SPF, DKIM, DMARC

| Protokoll | Funktion |
|---|---|
| SPF (Sender Policy Framework) | Definiert, welche Server fuer eine Domaene Mails senden duerfen |
| DKIM (DomainKeys Identified Mail) | Digitale Signatur im Mail-Header zur Integritaetspruefung |
| DMARC (Domain-based Message Authentication) | Kombiniert SPF + DKIM, legt Reaktion bei Verstoessen fest |

### Typische Pruefungsaspekte
- Massnahmen einem Bedrohungsszenario zuordnen koennen
- Unterschied zwischen Phishing-Varianten (Spear-Phishing, Whaling, Smishing)
- 3-2-1-Backup-Regel erklaeren und auf Ransomware anwenden
- MFA-Faktoren benennen und erklaeren
- Ransomware-Kill-Chain beschreiben
- E-Mail-Sicherheit (SPF/DKIM/DMARC) erklaeren

### Haeufige Fehler
- MFA = Passwort + Sicherheitsfrage → Beides ist Faktor „Wissen", also kein echtes MFA
- Backup auf demselben Server → Ransomware verschluesselt auch das Backup
- Awareness-Schulung einmalig → Muss regelmaessig wiederholt werden
- Phishing = nur E-Mail → Smishing (SMS) und Vishing (Telefon) vergessen

---

## Uebungen

**Aufgabe 1:** Ein Unternehmen bemerkt, dass ein Mitarbeiter ueber einen Cloud-Dienst grosse Datenmengen hochlaedt. Welche praeventive Massnahme haette diesen Vorfall verhindern koennen? Erklaere die Funktionsweise.

**Aufgabe 2:** Erklaere den Unterschied zwischen Spear-Phishing und normalem Phishing. Nenne fuer jede Variante eine geeignete Gegenmassnahme.

**Aufgabe 3:** Ein kleines Unternehmen (30 Mitarbeiter) erstellt taeglich Backups auf einem Netzlaufwerk (NAS). Bei einem Ransomware-Angriff werden sowohl die Server als auch das NAS verschluesselt. Was wurde falsch gemacht? Beschreibe eine bessere Backup-Strategie.

**Aufgabe 4:** Ordne die folgenden Massnahmen den Bedrohungsszenarien zu (Mehrfachnennung moeglich):

| Massnahme | Datendiebstahl | Phishing | Ransomware |
|---|---|---|---|
| MFA | | | |
| E-Mail-Filter | | | |
| Netzwerksegmentierung | | | |
| Offline-Backup | | | |
| DLP-System | | | |
| Awareness-Schulung | | | |

**Aufgabe 5:** Ein Kunde erhaelt folgende E-Mail: „Sehr geehrter Nutzer, Ihr Konto wurde gesperrt. Klicken Sie hier um es zu entsperren: http://sparkasse-verify.xyz". Nenne vier Erkennungsmerkmale, die auf Phishing hindeuten.

---
---

# Loesungen

## Aufgabe 1
**DLP (Data Loss Prevention):** Ein DLP-System ueberwacht den Datenverkehr und erkennt unerlaubten Datenabfluss. Es kann definierte Regeln anwenden: z.B. Uploads von Dateien mit bestimmten Klassifizierungen (vertraulich, intern) auf externe Cloud-Dienste blockieren. Zusaetzlich: USB-Port-Sperre und Protokollierung der Zugriffe.

## Aufgabe 2
**Normales Phishing:** Massenhaft versandte E-Mails an beliebige Empfaenger mit generischen Inhalten. Gegenmassnahme: Spamfilter und generelle Awareness-Schulung. **Spear-Phishing:** Gezielter Angriff auf eine bestimmte Person mit personalisierten Inhalten (Name, Position, aktuelle Projekte). Gegenmassnahme: Individuelle Sensibilisierung von Fuehrungskraeften und Finanzabteilung + MFA als zweite Schutzschicht.

## Aufgabe 3
**Fehler:** Das NAS war im selben Netzwerk wie die Server erreichbar und wurde daher mitverschluesselt. Es gab keine Offline- oder externe Backup-Kopie. **Bessere Strategie (3-2-1-Regel):** 3 Kopien der Daten, auf 2 verschiedenen Medien (z.B. NAS + USB-Festplatte), davon 1 Kopie extern/offline (z.B. Cloud-Backup oder Bandlaufwerk im Tresor). Das externe Backup darf nicht permanent mit dem Netzwerk verbunden sein (air-gapped).

## Aufgabe 4

| Massnahme | Datendiebstahl | Phishing | Ransomware |
|---|---|---|---|
| MFA | X | X | X |
| E-Mail-Filter | | X | X |
| Netzwerksegmentierung | X | | X |
| Offline-Backup | | | X |
| DLP-System | X | | |
| Awareness-Schulung | X | X | X |

## Aufgabe 5
(1) **Verdaechtige URL:** „sparkasse-verify.xyz" ist keine offizielle Sparkassen-Domain (.xyz statt .de). (2) **Unpersoenliche Anrede:** „Sehr geehrter Nutzer" statt Nennung des echten Namens. (3) **Dringlichkeit/Drohung:** „Konto gesperrt" soll zu unueberlegtem Handeln verleiten. (4) **Unuebliche Aufforderung:** Banken fordern nie per E-Mail zur Kontoentsperrung ueber einen Link auf.
