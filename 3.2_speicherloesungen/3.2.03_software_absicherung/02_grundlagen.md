# Grundlagen: 3.2.03 – Moeglichkeiten der softwaretechnischen Absicherung

## 1. Firewall/Webfilter

**Definition:** Eine Firewall ist ein Sicherheitssystem, das den Netzwerkverkehr anhand definierter Regeln filtert und unerlaubte Zugriffe blockiert. Ein Webfilter kontrolliert und beschraenkt den Zugriff auf Webinhalte.

**Firewall-Typen im Vergleich:**

| Typ | OSI-Schicht | Funktionsweise | Vor-/Nachteile |
|-----|------------|---------------|----------------|
| **Paketfilter** | 3–4 | Filtert nach IP-Adresse, Port, Protokoll | Schnell, aber kein Inhalt geprueft |
| **Stateful Inspection** | 3–4 | Prueft zusaetzlich den Verbindungszustand | Erkennt zusammengehoerige Pakete |
| **Application Layer Firewall** | 7 | Analysiert Anwendungsdaten (HTTP, FTP etc.) | Erkennt Angriffe im Inhalt, aber langsamer |
| **Next-Generation Firewall (NGFW)** | 3–7 | Kombination aller Typen + IDS/IPS, Deep Packet Inspection | Umfassender Schutz, komplex in der Konfiguration |

**Firewall-Regelaufbau (vereinfacht):**

| Nr. | Quelle | Ziel | Port | Protokoll | Aktion |
|-----|--------|------|------|-----------|--------|
| 1 | 192.168.1.0/24 | any | 443 | TCP | ALLOW |
| 2 | 192.168.1.0/24 | any | 80 | TCP | ALLOW |
| 3 | any | 192.168.1.10 | 22 | TCP | DENY |
| 4 | any | any | any | any | DENY |

**Wichtige Begriffe:**
- **Paketfilter** – filtert einzelne Pakete ohne Zustandsinformation
- **Stateful Inspection** – merkt sich den Verbindungszustand (z.B. SYN, ACK)
- **Deep Packet Inspection (DPI)** – analysiert den Inhalt der Datenpakete
- **Webfilter/Proxy** – kontrolliert HTTP/HTTPS-Verkehr, sperrt Kategorien (z.B. Social Media)
- **DMZ (Demilitarisierte Zone)** – Netzwerkbereich zwischen internem und externem Netz fuer oeffentlich zugaengliche Dienste

**Erklaerung:** Firewall-Regeln werden von oben nach unten abgearbeitet (First Match). Die letzte Regel ist meist eine **Deny-All-Regel** (alles blockieren, was nicht ausdruecklich erlaubt ist). Dies nennt man **Whitelist-Ansatz**.

---

## 2. Portsecurity

**Definition:** Portsecurity ist eine Sicherheitsfunktion auf managed Switches, die den Zugriff auf Netzwerkports anhand von MAC-Adressen kontrolliert.

**Kernaussagen:**
- Jeder Switchport wird auf eine bestimmte Anzahl erlaubter MAC-Adressen beschraenkt
- Unbekannte MAC-Adressen werden blockiert oder der Port wird deaktiviert
- Schutz vor: Unbefugtem Anschliessen von Geraeten, MAC-Flooding-Angriffen

**Portsecurity-Modi:**

| Modus | Reaktion bei Verstoss | Beschreibung |
|-------|----------------------|-------------|
| **Protect** | Pakete werden verworfen | Kein Alarm, Port bleibt aktiv |
| **Restrict** | Pakete werden verworfen + Logmeldung | Port bleibt aktiv, Verstoss wird protokolliert |
| **Shutdown** | Port wird deaktiviert | Port muss manuell oder per Timer reaktiviert werden |

**Ergaenzend: IEEE 802.1X**
- Authentifizierung am Netzwerkport mittels RADIUS-Server
- Bevor ein Geraet Netzwerkzugriff erhaelt, muss es sich authentifizieren
- Komponenten: **Supplicant** (Client), **Authenticator** (Switch), **Authentication Server** (RADIUS)

**Wichtige Begriffe:**
- **MAC-Adresse** – eindeutige Hardwareadresse einer Netzwerkkarte
- **MAC-Flooding** – Angriff, bei dem ein Switch mit gefaelschten MAC-Adressen ueberflutet wird
- **RADIUS** – Remote Authentication Dial-In User Service, zentraler Authentifizierungsdienst
- **802.1X** – Standard fuer portbasierte Netzwerkzugangs-Kontrolle

---

## 3. User- und Zugriffsmanagement

**Definition:** User- und Zugriffsmanagement umfasst die Verwaltung von Benutzerkonten, Gruppen und deren Berechtigungen auf IT-Ressourcen.

**Kernaussagen:**
- Zentrale Benutzerverwaltung ueber **Active Directory (AD)** oder **LDAP**
- Rechte werden ueber **Gruppen** und **Rollen** zugewiesen, nicht einzeln
- Passwortrichtlinien definieren Mindestlaenge, Komplexitaet, Aenderungsintervall
- **Gruppenrichtlinien (GPO)** steuern Konfigurationen zentral

**Elemente der Benutzerverwaltung:**

| Element | Beschreibung | Beispiel |
|---------|-------------|---------|
| Benutzerkonto | Identitaet eines Nutzers im System | max.mustermann |
| Gruppe | Zusammenfassung von Benutzern mit gleichen Rechten | Gruppe "Buchhaltung" |
| Organisationseinheit (OU) | Container im AD zur Strukturierung | OU "Standort-Berlin" |
| Gruppenrichtlinie (GPO) | Zentrale Konfigurationsregel | Passwort-Policy: min. 12 Zeichen |

**Passwortsicherheit:**

| Kriterium | Empfehlung |
|-----------|-----------|
| Mindestlaenge | 12 Zeichen oder mehr |
| Komplexitaet | Gross-/Kleinbuchstaben, Zahlen, Sonderzeichen |
| Aenderungsintervall | Regelmaessig oder bei Verdacht auf Kompromittierung |
| Wiederverwendung | Verbot der letzten 10 Passwoerter |
| Multi-Faktor | 2FA/MFA zusaetzlich zum Passwort |

**Wichtige Begriffe:**
- **Active Directory (AD)** – zentraler Verzeichnisdienst von Microsoft fuer Benutzer- und Ressourcenverwaltung
- **LDAP** – Lightweight Directory Access Protocol, Protokoll fuer Verzeichniszugriff
- **GPO (Group Policy Object)** – Gruppenrichtlinie zur zentralen Konfiguration
- **SSO (Single Sign-On)** – einmalige Anmeldung fuer mehrere Systeme

---

## 4. Verschluesselung (z.B. Bitlocker)

**Definition:** Verschluesselung wandelt lesbare Daten (Klartext) in unlesbare Daten (Chiffretext) um, die nur mit dem passenden Schluessel wiederhergestellt werden koennen.

**Verschluesselungsarten:**

| Art | Beschreibung | Schluessel | Beispiele |
|-----|-------------|-----------|----------|
| **Symmetrisch** | Gleicher Schluessel fuer Ver- und Entschluesselung | 1 Schluessel | AES, DES, 3DES |
| **Asymmetrisch** | Zwei Schluessel (oeffentlich + privat) | Schluesselpaar | RSA, ECC |
| **Hybrid** | Kombination: asymmetrisch fuer Schluesselaustausch, symmetrisch fuer Daten | Beide | TLS/SSL, HTTPS |

**Verschluesselungsebenen fuer Speicher:**

| Ebene | Beschreibung | Beispiel |
|-------|-------------|---------|
| **Full-Disk Encryption (FDE)** | Gesamte Festplatte wird verschluesselt | Bitlocker (Windows), LUKS (Linux), FileVault (macOS) |
| **File-Level Encryption** | Einzelne Dateien/Ordner werden verschluesselt | EFS (Encrypting File System), VeraCrypt-Container |
| **Datenbankverschluesselung** | Daten innerhalb der Datenbank werden verschluesselt | TDE (Transparent Data Encryption) in SQL Server |

**Bitlocker im Detail:**
- Full-Disk-Encryption fuer Windows
- Nutzt AES-128 oder AES-256
- Schluessel wird im **TPM (Trusted Platform Module)** gespeichert
- Recovery Key als Backup bei TPM-Fehler
- Schuetzt Daten bei Diebstahl der Festplatte

**Wichtige Begriffe:**
- **AES (Advanced Encryption Standard)** – symmetrischer Verschluesselungsalgorithmus, Standard fuer Festplattenverschluesselung
- **TPM (Trusted Platform Module)** – Sicherheitschip auf dem Mainboard zur Schluesselspeicherung
- **Recovery Key** – Wiederherstellungsschluessel fuer verschluesselte Laufwerke
- **EFS (Encrypting File System)** – dateibasierte Verschluesselung unter Windows (NTFS)
