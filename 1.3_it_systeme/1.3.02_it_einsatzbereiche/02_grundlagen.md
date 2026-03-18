# Grundlagen: 1.3.02 – Typische IT-Systeme und deren Einsatzbereiche

## Client-Server-Systeme

**Definition:** Eine Architektur, bei der ein zentraler Server Dienste, Daten oder Ressourcen bereitstellt und Clients diese ueber das Netzwerk anfragen und nutzen.

**Kernaussagen:**
- Server stellt Dienste bereit (z.B. Dateiserver, Mailserver, Datenbankserver, Webserver)
- Client fragt Dienste an (z.B. Browser, E-Mail-Client, Datenbankanwendung)
- Zentralisierte Datenhaltung und -verwaltung
- Skalierbar durch leistungsfaehigere Server oder Load Balancing
- Vorteile: Zentrale Administration, Datensicherheit, Zugriffssteuerung
- Nachteile: Single Point of Failure (bei fehlender Redundanz), hoehe Anschaffungskosten

**Wichtige Begriffe:**
- **Thin Client** – Client ohne eigene Rechenleistung/Daten, alles vom Server
- **Fat Client** – Client mit eigener Software und lokaler Datenverarbeitung
- **Terminalserver** – Stellt Desktops/Anwendungen zentral bereit

**Erklaerung:** In der Pruefung werden haeufig Szenarien beschrieben, in denen du entscheiden musst, ob ein Client-Server-System oder eine andere Architektur geeignet ist. Entscheidend sind: Nutzeranzahl, Sicherheitsanforderungen, Verwaltungsaufwand.

---

## Einbindung in einer Domaene

**Definition:** Eine Domaene ist eine logische Verwaltungseinheit in einem Netzwerk, in der Benutzer, Computer und Ressourcen zentral verwaltet werden. Typisches Beispiel: Microsoft Active Directory (AD).

**Kernaussagen:**
- Zentrale Benutzerverwaltung (Anlegen, Sperren, Loeschen von Konten)
- Gruppenrichtlinien (GPO): Einheitliche Konfiguration aller Clients (z.B. Passwort-Policy, Softwareverteilung, Desktop-Einschraenkungen)
- Single Sign-On (SSO): Ein Login fuer alle Dienste der Domaene
- Organisationseinheiten (OU): Strukturierung der Domaene (z.B. nach Abteilung, Standort)
- DNS ist Voraussetzung fuer Active Directory

**Wichtige Begriffe:**
- **Domain Controller (DC)** – Server, der die Domaene verwaltet und Authentifizierung durchfuehrt
- **LDAP** – Protokoll fuer Verzeichnisdienste (Lightweight Directory Access Protocol)
- **Kerberos** – Authentifizierungsprotokoll in Active Directory
- **GPO (Group Policy Object)** – Richtlinie zur zentralen Konfiguration

**Erklaerung:** Fuer die Pruefung ist wichtig: Was sind Vorteile einer Domaene gegenueber einer Arbeitsgruppe? Antwort: Zentrale Verwaltung, Sicherheit, Skalierbarkeit. Eine Arbeitsgruppe eignet sich nur fuer kleine Netze (< 10 Geraete).

---

## Kommunikationssysteme

**Definition:** IT-Systeme, die den Austausch von Informationen und die Zusammenarbeit zwischen Personen ermoeglichen – synchron (Echtzeit) oder asynchron.

**Kernaussagen:**
- **Videokonferenzsysteme:** z.B. Microsoft Teams, Zoom, Webex – Echtzeit-Audio/Video-Kommunikation
- **Social-Media-Systeme:** Interne Plattformen (z.B. Yammer, Slack) oder externe (LinkedIn, Twitter)
- **Groupware:** Gemeinsame Kalender, Aufgaben, Dokumente (z.B. Microsoft 365, Google Workspace)
- **Unified Communications (UC):** Integration von Telefonie, Video, Chat, E-Mail in einer Plattform

**Wichtige Begriffe:**
- **Synchrone Kommunikation** – Echtzeit (Telefonat, Videocall, Chat)
- **Asynchrone Kommunikation** – Zeitversetzt (E-Mail, Forum, Wiki)
- **Kollaboration** – Gemeinsames Arbeiten an Dokumenten/Projekten

**Erklaerung:** In der Pruefung kann nach der Auswahl eines geeigneten Kommunikationssystems fuer ein Szenario gefragt werden. Kriterien: Teilnehmeranzahl, Standorte, Datenschutz, vorhandene Infrastruktur.

---

## Mobile Geraete

**Definition:** Tragbare IT-Geraete wie Smartphones und Tablets, die im privaten und beruflichen Umfeld eingesetzt werden.

**Kernaussagen:**
- **Smartphone:** Telefonie, Internet, Apps, Kamera, GPS
- **Tablet:** Groesserer Bildschirm, haeufig im Aussendienst/Praesentation
- **BYOD (Bring Your Own Device):** Mitarbeiter nutzen private Geraete beruflich
- **COPE (Corporate Owned, Personally Enabled):** Firmengeraet, auch privat nutzbar
- **MDM (Mobile Device Management):** Zentrale Verwaltung mobiler Geraete (Apps, Richtlinien, Fernloeschung)
- Sicherheitsaspekte: Verschluesselung, Bildschirmsperre, VPN, Container-Loesung

**Wichtige Begriffe:**
- **MDM** – Mobile Device Management (z.B. Microsoft Intune, Jamf)
- **Containerisierung** – Trennung beruflicher und privater Daten auf einem Geraet
- **Fernloeschung (Remote Wipe)** – Bei Verlust Daten aus der Ferne loeschen

**Erklaerung:** Pruefungsrelevant ist die Abwaegung BYOD vs. Firmengeraet (Kosten, Sicherheit, Datenschutz, Akzeptanz) sowie die Kenntnis von MDM-Funktionen.

---

## Netzwerkprotokolle und OSI-Modell

**Definition:** Netzwerkprotokolle regeln die Kommunikation zwischen IT-Systemen. Das OSI-Modell ordnet diese Protokolle in 7 Schichten.

**Kernaussagen:**

| Protokoll | OSI-Schicht | Funktion |
|---|---|---|
| Ethernet | 1-2 | Physische Uebertragung im LAN |
| IP (IPv4/IPv6) | 3 | Logische Adressierung und Routing |
| DNS | 7 (Anwendung) | Namensaufloesung (Domain → IP) |
| TCP | 4 | Verbindungsorientierte Uebertragung |
| UDP | 4 | Verbindungslose Uebertragung |

**Wichtige Begriffe:**
- **MAC-Adresse** – Hardware-Adresse (Schicht 2, 48 Bit)
- **IP-Adresse** – Logische Adresse (Schicht 3, IPv4: 32 Bit, IPv6: 128 Bit)
- **Subnetzmaske** – Trennung von Netz- und Hostanteil
- **Default Gateway** – Router, der Pakete ins externe Netz weiterleitet

**Erklaerung:** Das OSI-Modell ist Grundlagenwissen fuer die Pruefung. Du musst Protokolle den richtigen Schichten zuordnen koennen und verstehen, wie Datenpakete durch die Schichten wandern (Kapselung/Entkapselung).

## Querverweise
- → 3.1.01 (Schichtenmodelle, ARP, TCP/UDP detailliert)
- → 3.1.02 (Netzwerkkomponenten: Switch, Router, Firewall)
- → 3.1.07 (DHCP, DNS, Proxy)
