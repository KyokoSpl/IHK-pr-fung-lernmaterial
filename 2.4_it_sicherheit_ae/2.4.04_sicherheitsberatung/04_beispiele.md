# Beispiele: 2.4.04 – Kunden zur IT-Sicherheit beraten

## Bedrohungsszenarien

**Beispiel 1 – Man-in-the-Middle:** Ein Mitarbeiter arbeitet im Hotel-WLAN und loggt sich in das Firmen-Webmail ein. Ein Angreifer im gleichen WLAN faengt mit einem Sniffing-Tool die Daten ab. → **Loesung:** VPN-Pflicht fuer alle Verbindungen ausserhalb des Firmennetzwerks. HTTPS/TLS fuer alle Webdienste pruefen.

**Beispiel 2 – SQL-Injection:** Ein Onlineshop hat ein Suchfeld. Ein Angreifer gibt folgenden Text ein: `' UNION SELECT username, password FROM users --`. Die Datenbank gibt alle Benutzernamen und Passwort-Hashes zurueck. → **Loesung:** Prepared Statements verwenden, Input Validation, Web Application Firewall (WAF).

**Beispiel 3 – DDoS:** Ein Wettbewerber beauftragt einen DDoS-Dienst, der den Webshop eines Konkurrenten mit Millionen Anfragen ueberflutet. Der Shop ist 12 Stunden offline. → **Loesung:** CDN mit DDoS-Schutz (z.B. Cloudflare), Rate Limiting, Notfallplan mit Eskalationskette.

---

## Private Haushalte

**Beispiel 4:** Eine Familie fragt nach einem sicheren Heimnetzwerk. Aktuell nutzen alle dasselbe WLAN-Passwort, der Router hat noch das Werkspasswort.

| Empfehlung | Massnahme |
|---|---|
| Router-Passwort | Standard-Passwort sofort aendern |
| WLAN-Verschluesselung | WPA3 aktivieren, starkes Passwort (mind. 16 Zeichen) |
| Gastnetz | Separates WLAN fuer Gaeste und IoT-Geraete |
| Firmware | Automatische Updates aktivieren |
| Kinderschutz | Zeitliche Begrenzung, Inhaltsfilter am Router |
| Backup | Externe Festplatte oder Cloud-Backup fuer Fotos und Dokumente |

---

## Unternehmen – intern

**Beispiel 5:** Ein KMU (50 Mitarbeiter) stellt fest, dass ein Mitarbeiter einen privaten USB-Stick an den Firmen-PC anschliesst und Kundendaten kopiert.

| Massnahme | Beschreibung |
|---|---|
| USB-Port-Sperre | USB-Ports per Gruppenrichtlinie deaktivieren |
| DLP-System | Datenabfluss erkennen und blockieren |
| Least Privilege | Zugriff nur auf fuer die Rolle noetige Daten |
| Logging | Dateizugriffe protokollieren |
| Arbeitsvertrag | Vertraulichkeitsklausel und IT-Nutzungsrichtlinie |

---

## Unternehmen – extern

**Beispiel 6:** Ein Softwarehaus erhaelt eine Phishing-Mail, die als Rechnung eines echten Lieferanten getarnt ist (Spear-Phishing). Ein Mitarbeiter oeffnet den Anhang und installiert unwissentlich Malware.

| Phase | Vorfall | Massnahme |
|---|---|---|
| Praevention | E-Mail-Filter, Awareness-Schulung | SPF/DKIM/DMARC, regelmaessige Phishing-Tests |
| Erkennung | EDR erkennt verdaechtiges Verhalten | Alarm an IT-Abteilung |
| Reaktion | Geraet isolieren, Forensik | Incident-Response-Plan aktivieren |
| Nachbereitung | Vorfall analysieren, Lehren ziehen | Schulung wiederholen, Regeln anpassen |

---

## Risikoanalyse

**Beispiel 7:** Ein IT-Dienstleister fuehrt eine Risikoanalyse fuer eine Arztpraxis durch.

| Asset | Bedrohung | Schwachstelle | Wahrscheinlichkeit | Schaden | Risiko | Massnahme |
|---|---|---|---|---|---|---|
| Patientendaten | Ransomware | Kein Backup | Hoch | Sehr hoch | Kritisch | 3-2-1-Backup |
| Praxis-PC | Malware | Veraltete Software | Hoch | Hoch | Hoch | Patch-Management |
| WLAN | MITM | WPA2 ohne Gastnetz | Mittel | Hoch | Hoch | WPA3, Gastnetz |
| E-Mail | Phishing | Kein Spamfilter | Hoch | Mittel | Hoch | Spamfilter, MFA |
| Zugang | Unbefugter Zutritt | Keine Schliessanlage | Gering | Hoch | Mittel | Elektronische Schliessanlage |

---

## Oeffentliche Hand

**Beispiel 8:** Eine Stadtverwaltung plant die Digitalisierung der Buergerservices (Online-Antraege). Die IT-Abteilung muss ein Sicherheitskonzept erstellen.

| Anforderung | Umsetzung |
|---|---|
| BSI IT-Grundschutz | Schutzbedarfsfeststellung fuer alle Systeme |
| DSGVO | Datenschutz-Folgenabschaetzung (DSFA) fuer Buergerdaten |
| Authentifizierung | eID (elektronischer Personalausweis) oder Benutzerkonto Bund |
| Verschluesselung | TLS 1.3 fuer alle Webdienste, Ende-zu-Ende-Verschluesselung |
| Verfuegbarkeit | Redundante Server, SLA mit Hosting-Anbieter |
| Vergaberecht | IT-Sicherheitsanforderungen in der Ausschreibung (EVB-IT) |
| Barrierefreiheit | BITV 2.0 – auch Sicherheitsfunktionen muessen barrierefrei sein |

---

## TOM in der Praxis

**Beispiel 9:** Ein Unternehmen muss gemaess DSGVO Art. 32 seine TOM dokumentieren. Auszug:

| TOM-Kategorie | Technische Massnahme | Organisatorische Massnahme |
|---|---|---|
| Zutrittskontrolle | Chipkarten-Zugang, Videoanlage | Besucherliste, Begleitung von Gaesten |
| Zugangskontrolle | Passwortrichtlinie (12+ Zeichen), MFA | Sperrung nach 5 Fehlversuchen, Bildschirmsperre |
| Zugriffskontrolle | AES-256-Verschluesselung, Rollenkonzept | Need-to-Know-Prinzip, Berechtigungsmatrix |
| Weitergabekontrolle | VPN, TLS 1.3, verschluesselte USB-Sticks | Regelung zur Datenweitergabe, Loeschkonzept |
| Verfuegbarkeitskontrolle | USV, RAID 6, Cloud-Backup | Notfallhandbuch, Brandmelderlange |
