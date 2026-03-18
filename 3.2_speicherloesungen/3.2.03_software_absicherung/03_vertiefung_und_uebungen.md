# Vertiefung und Uebungen: 3.2.03 – Moeglichkeiten der softwaretechnischen Absicherung

## Vertiefung

### Firewall-Architekturen

```
INTERNET
    |
[Router mit Paketfilter]
    |
---[DMZ]--- (Webserver, Mailserver)
    |
[Interne Firewall / NGFW]
    |
[Internes LAN] (Clients, Fileserver, Datenbank)
```

**Dual-Homed Firewall:** Eine Firewall mit zwei Netzwerkschnittstellen trennt internes Netz vom Internet.

**DMZ-Architektur:** Zwei Firewalls (oder eine mit drei Interfaces) bilden eine DMZ. Oeffentlich zugaengliche Dienste stehen in der DMZ, das interne Netz wird dadurch doppelt geschuetzt.

### Portsecurity vs. 802.1X

| Kriterium | Portsecurity | 802.1X |
|-----------|-------------|--------|
| Authentifizierung | MAC-Adresse (kann gefaelscht werden) | Benutzername/Passwort oder Zertifikat |
| Sicherheit | Mittel (MAC-Spoofing moeglich) | Hoch (kryptographisch) |
| Verwaltung | Pro Switch/Port | Zentral ueber RADIUS |
| Eignung | Kleine Netze | Unternehmensnetze |
| Standard | Herstellerspezifisch | IEEE 802.1X |

### Full-Disk vs. File-Level Encryption

| Kriterium | Full-Disk Encryption | File-Level Encryption |
|-----------|---------------------|----------------------|
| Umfang | Gesamte Festplatte | Einzelne Dateien/Ordner |
| Schutz bei Diebstahl | Ja (Festplatte nicht lesbar) | Nur verschluesselte Dateien geschuetzt |
| Performance | Leicht reduziert (gesamter I/O) | Nur bei Zugriff auf verschluesselte Dateien |
| Nutzertransparenz | Hoch (nach Anmeldung automatisch entschluesselt) | Mittel (Dateien muessen gezielt verschluesselt werden) |
| Beispiel | Bitlocker, LUKS | EFS, VeraCrypt-Container |
| Schwaeche | Im laufenden Betrieb sind Daten entschluesselt | Nicht verschluesselte Dateien bleiben ungeschuetzt |

### Zusammenspiel der Massnahmen

| Schicht | Massnahme | Schutz vor |
|---------|----------|-----------|
| Netzwerk (Perimeter) | Firewall, DMZ | Externen Angriffen |
| Netzwerk (intern) | Portsecurity, 802.1X, VLAN | Unbefugten Geraeten im LAN |
| System | User-Management, GPO, Passwort-Policy | Unbefugter Systemnutzung |
| Daten | Verschluesselung (FDE/File-Level) | Datendiebstahl bei physischem Zugriff |

### Typische Pruefungsaspekte
- Firewall-Typen unterscheiden und fuer ein Szenario empfehlen
- Firewall-Regeln lesen und interpretieren
- Portsecurity-Modi erklaeren
- Verschluesselung: symmetrisch vs. asymmetrisch, FDE vs. File-Level
- Bitlocker-Funktionsweise und TPM erklaeren
- DMZ erklaeren und zeichnen

### Haeufige Fehler
- Paketfilter und Application Layer Firewall verwechseln: Paketfilter prueft nur Header (IP, Port), Application Layer prueft Inhalt
- Portsecurity schuetzt nicht vor MAC-Spoofing → fuer hohe Sicherheit ist 802.1X noetig
- Bitlocker allein schuetzt nicht im laufenden Betrieb: Daten sind nach der Anmeldung entschluesselt
- Symmetrische und asymmetrische Verschluesselung verwechseln: AES = symmetrisch, RSA = asymmetrisch

---

## Uebungen

**Aufgabe 1:** Erklaere den Unterschied zwischen einem Paketfilter und einer Application Layer Firewall. Auf welchen OSI-Schichten arbeiten sie?

**Aufgabe 2:** Gegeben ist folgende Firewall-Regeltabelle:

| Nr. | Quelle | Ziel | Port | Protokoll | Aktion |
|-----|--------|------|------|-----------|--------|
| 1 | 10.0.0.0/24 | any | 443 | TCP | ALLOW |
| 2 | any | 10.0.0.5 | 80 | TCP | ALLOW |
| 3 | 10.0.0.0/24 | any | 22 | TCP | DENY |
| 4 | any | any | any | any | DENY |

a) Darf ein Client mit IP 10.0.0.15 auf eine HTTPS-Webseite zugreifen?
b) Darf ein externer Rechner per SSH auf 10.0.0.5 zugreifen?
c) Was bewirkt Regel 4?

**Aufgabe 3:** Erklaere die drei Portsecurity-Modi (Protect, Restrict, Shutdown) und nenne den Unterschied.

**Aufgabe 4:** Was ist der Unterschied zwischen Full-Disk Encryption und File-Level Encryption? Nenne je ein Beispiel.

**Aufgabe 5:** Erklaere, wie Bitlocker funktioniert. Welche Rolle spielt das TPM?

**Aufgabe 6:** Ein Unternehmen moechte verhindern, dass unbekannte Geraete im Netzwerk kommunizieren. Welche zwei softwaretechnischen Massnahmen koennen eingesetzt werden? Erklaere kurz die Unterschiede.

**Aufgabe 7:** Was ist eine DMZ? Zeichne eine vereinfachte Netzwerkarchitektur mit DMZ und beschrifte die Komponenten.

---
---

# Loesungen

## Aufgabe 1
- **Paketfilter:** Arbeitet auf OSI-Schicht 3–4. Filtert nach IP-Adresse, Port und Protokoll. Prueft nur den Header, nicht den Inhalt der Pakete.
- **Application Layer Firewall:** Arbeitet auf OSI-Schicht 7. Analysiert den Inhalt der Datenpakete (z.B. HTTP-Anfragen). Kann Angriffe erkennen, die im Inhalt versteckt sind (z.B. SQL-Injection in einer URL).

## Aufgabe 2
a) **Ja.** Regel 1 erlaubt Verkehr von 10.0.0.0/24 auf Port 443 (HTTPS). Client 10.0.0.15 liegt im erlaubten Subnetz.
b) **Nein.** Regel 3 verbietet SSH (Port 22) aus dem Subnetz 10.0.0.0/24. Fuer externe Rechner greift Regel 4 (Deny All), da keine explizite Erlaubnis existiert.
c) Regel 4 ist die **Deny-All-Regel** (Default Deny). Alles, was nicht durch vorherige Regeln ausdruecklich erlaubt wurde, wird blockiert. Dies entspricht dem Whitelist-Ansatz.

## Aufgabe 3
- **Protect:** Pakete von unbekannten MAC-Adressen werden stillschweigend verworfen. Kein Alarm, Port bleibt aktiv.
- **Restrict:** Pakete werden verworfen, aber ein Logeintrag wird erzeugt. Port bleibt aktiv, Verstoss wird dokumentiert.
- **Shutdown:** Der gesamte Port wird deaktiviert. Er muss manuell oder per Aging-Timer wieder aktiviert werden. Staerkste Reaktion.

## Aufgabe 4
- **Full-Disk Encryption (FDE):** Verschluesselt die gesamte Festplatte. Nach dem Booten und der Authentifizierung sind alle Daten transparent zugaenglich. Beispiel: **Bitlocker**.
- **File-Level Encryption:** Verschluesselt nur ausgewaehlte Dateien oder Ordner. Nicht verschluesselte Bereiche bleiben ungeschuetzt. Beispiel: **EFS (Encrypting File System)**.

## Aufgabe 5
Bitlocker ist eine Full-Disk-Encryption-Loesung von Microsoft fuer Windows. Die gesamte Systempartition wird mit AES (128 oder 256 Bit) verschluesselt. Der Verschluesselungsschluessel wird im **TPM (Trusted Platform Module)** gespeichert – einem Sicherheitschip auf dem Mainboard. Beim Booten prueft das TPM, ob die Hardware unveraendert ist (Integritaetspruefung). Nur dann wird der Schluessel freigegeben. Fuer den Fall, dass das TPM ausfaellt oder die Hardware getauscht wird, gibt es einen **Recovery Key** als Backup.

## Aufgabe 6
1. **Portsecurity:** MAC-Adressen werden pro Switchport beschraenkt. Unbekannte Geraete werden blockiert. Einfach einzurichten, aber MAC-Adressen koennen gefaelscht werden.
2. **802.1X (Network Access Control):** Geraete muessen sich ueber einen RADIUS-Server authentifizieren, bevor sie Netzwerkzugriff erhalten. Sicherer als Portsecurity, da kryptographische Authentifizierung.

## Aufgabe 7
```
          INTERNET
              |
    [Externe Firewall]
              |
    ----[DMZ]----
    |  Webserver  |
    |  Mailserver |
    ---------------
              |
    [Interne Firewall]
              |
    [Internes LAN]
    (Clients, Fileserver, DB)
```
Die DMZ ist ein separater Netzwerkbereich zwischen zwei Firewalls. Oeffentlich erreichbare Dienste (Web, Mail) stehen in der DMZ. Das interne Netz ist durch die innere Firewall zusaetzlich geschuetzt. Ein Angreifer, der den Webserver kompromittiert, kann nicht direkt ins interne Netz gelangen.
