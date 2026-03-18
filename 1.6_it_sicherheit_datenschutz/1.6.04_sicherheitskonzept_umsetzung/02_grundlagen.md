# Grundlagen: 1.6.04 – Umsetzung des Sicherheitskonzepts

## Authentifizierung / Zweifaktor / Passwort-Policy

**Authentifizierungsfaktoren:**

| Faktor | Prinzip | Beispiel |
|---|---|---|
| **Wissen** | Etwas, das man weiss | Passwort, PIN |
| **Besitz** | Etwas, das man hat | Smartcard, Token, Smartphone |
| **Biometrie** | Etwas, das man ist | Fingerabdruck, Gesichtserkennung |

**Zweifaktor-Authentifizierung (2FA):** Kombination von mindestens zwei verschiedenen Faktoren. Beispiel: Passwort (Wissen) + SMS-Code (Besitz).

**Passwort-Policy (BSI-Empfehlung aktuell):**
- Mindestens 8 Zeichen (besser 12+)
- Gross-/Kleinbuchstaben, Zahlen, Sonderzeichen
- Kein regelmaessiger Wechselzwang mehr (nur bei Kompromittierung)
- Keine Wiederverwendung alter Passwoerter
- Nutzung von Passwort-Managern empfohlen

---

## Datensicherung / Backup-Verfahren

| Verfahren | Beschreibung | Speicherbedarf | Wiederherstellung |
|---|---|---|---|
| **Vollbackup** | Alle Daten komplett sichern | Hoch | Schnell (1 Sicherung) |
| **Inkrementell** | Nur Aenderungen seit letztem Backup | Gering | Langsam (Vollbackup + alle Inkremente) |
| **Differenziell** | Aenderungen seit letztem Vollbackup | Mittel | Mittel (Vollbackup + letztes Diff.) |

**3-2-1-Regel:**
- **3** Kopien der Daten (Original + 2 Backups)
- **2** verschiedene Medien (z.B. Festplatte + Cloud)
- **1** Kopie extern/offsite (fuer Katastrophenfall)

**Generationenprinzip (Grossvater-Vater-Sohn):**
- Sohn: Taegliche Sicherung
- Vater: Woechentliche Sicherung
- Grossvater: Monatliche Sicherung

---

## Technische, organisatorische und personelle Schutzmassnahmen

| Kategorie | Beispiele |
|---|---|
| **Technisch/Infrastrukturell** | Firewall, Verschluesselung, USV, Zutrittskontrollen |
| **Organisatorisch** | Sicherheitsrichtlinien, Rollenkonzepte, Change Management |
| **Personell** | Schulungen, Verpflichtungserklärungen, Awareness |

---

## Hashwerte, Zertifikate, digitale Signaturen

**Hashwerte:**
- Einweg-Funktion: Aus Daten wird fester Hashwert berechnet
- Nicht umkehrbar
- Gleiche Eingabe → immer gleicher Hash
- Kleinste Aenderung → voellig anderer Hash
- Algorithmen: SHA-256, SHA-3, MD5 (veraltet!)
- Einsatz: Integritaetspruefung, Passwortspeicherung

**Digitale Zertifikate:**
- Elektronischer Ausweis fuer Server/Personen
- Ausgestellt von einer Certificate Authority (CA)
- Inhalt: Oeffentlicher Schluessel, Identitaet, Gueltigkeit, Signatur der CA
- Standard: X.509

**Digitale Signatur:**
- Sender erstellt Hash der Nachricht
- Hash wird mit privatem Schluessel verschluesselt → Signatur
- Empfaenger entschluesselt mit oeffentlichem Schluessel und vergleicht Hash
- Gewaehrleistet: Integritaet + Authentizitaet + Nichtabstreitbarkeit

---

## Haertung des Betriebssystems

**Definition:** Reduzierung der Angriffsflaeche durch Deaktivierung nicht benoetigter Dienste und Funktionen.

**Massnahmen:**
- Nicht benoetigte Dienste/Ports deaktivieren
- Regelmaessige Updates und Patches einspielen
- Standard-Administratorkonto umbenennen/deaktivieren
- Minimale Rechtevergabe (Least-Privilege-Prinzip)
- Logging aktivieren
- Autostart-Programme pruefen
- Gastkonten deaktivieren

---

## IT-Sicherheitsmanagement

**Definition:** Gesamtheit der Aktivitaeten zur Planung, Steuerung und Ueberwachung der Informationssicherheit.

**Kern:** Risikomanagement + ISMS (→ 1.6.03) + operative Massnahmen

---

## Personal Firewall

**Definition:** Software-basierte Firewall auf einem Endgeraet, die ein-/ausgehenden Netzwerkverkehr filtert.

**Funktionen:**
- Anwendungsbasierte Regeln (welche Programme duerfen ins Internet?)
- Portfilterung (eingehend/ausgehend)
- Benachrichtigung bei unerlaubten Verbindungsversuchen

---

## Sicherheitsbewusstsein / Security by Design / Security by Default

| Konzept | Beschreibung |
|---|---|
| **Security by Design** | Sicherheit wird von Anfang an in die Entwicklung eingebaut |
| **Security by Default** | Standardeinstellungen sind maximal sicher (z.B. Verschluesselung aktiv) |
| **Awareness** | Mitarbeiter sind sich der Sicherheitsrisiken bewusst und handeln entsprechend |

---

## Verfuegbarkeitssicherung (NAS)

**NAS (Network Attached Storage):**
- Netzwerkspeicher fuer zentrale Datenhaltung
- Zugriff ueber Netzwerk (SMB, NFS)
- Unterstuetzt RAID fuer Redundanz
- Einsatz: Backup-Ziel, Dateiserver, Archiv

---

## Verschluesselungstechniken

(Zusammenfassung – Details in 1.6.01)
- Symmetrisch: AES-256, 3DES
- Asymmetrisch: RSA, ECC
- Hybrid: TLS/HTTPS

**Praxiseinsatz:**
- Festplattenverschluesselung: BitLocker, VeraCrypt
- E-Mail-Verschluesselung: PGP, S/MIME
- Netzwerk: VPN (IPsec, WireGuard)

---

## Zugangs- und Zugriffskontrolle

**Zugangskontrolle** = WER darf das System nutzen? (Authentifizierung)
**Zugriffskontrolle** = WAS darf der Nutzer im System tun? (Autorisierung)

**Berechtigungskonzepte:**

| Modell | Beschreibung |
|---|---|
| **DAC** (Discretionary) | Besitzer legt Rechte fest |
| **MAC** (Mandatory) | System legt Rechte fest (Sicherheitsstufen) |
| **RBAC** (Role-Based) | Rechte ueber Rollen zugewiesen |

**Least-Privilege-Prinzip:** Jeder Nutzer erhaelt nur die minimal notwendigen Berechtigungen.
