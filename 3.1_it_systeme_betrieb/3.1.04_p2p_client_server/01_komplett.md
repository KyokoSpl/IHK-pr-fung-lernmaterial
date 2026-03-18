# Komplett: 3.1.04 – Peer-to-Peer vs. Client-Server

## Einordnung

- **Pruefungsteil:** 3.1 – Betreiben von IT-Systemen (Netzwerktechnik)
- **Thema-ID:** 3.1.04
- **Thema:** Peer-to-Peer- und Client-Server-Konzepte unterscheiden koennen

## Themenkreise

### 1. Dateifreigaben (SMB/CIFS)

**Definition:** SMB (Server Message Block) / CIFS (Common Internet File System) ist ein Netzwerkprotokoll zur Freigabe von Dateien, Druckern und anderen Ressourcen in lokalen Netzwerken.

**Kernaussagen:**
- SMB ist das Standard-Protokoll fuer Dateifreigaben in Windows-Netzwerken
- CIFS ist eine aeltere Bezeichnung / Erweiterung von SMB
- Aktuelle Version: SMB 3 (verschluesselt, performant)
- Arbeitet ueber TCP-Port 445
- Kann im P2P-Modus (Arbeitsgruppe) oder im Client-Server-Modus (Domaene) genutzt werden

**Einsatz in P2P:** Jeder PC gibt eigene Ordner frei. Zugriffskontrolle erfolgt lokal auf jedem Rechner. Geeignet fuer kleine Netzwerke (< 10 Geraete).

**Einsatz in Client-Server:** Ein zentraler Fileserver stellt Freigaben bereit. Berechtigungen werden zentral ueber Active Directory verwaltet. Geeignet fuer Unternehmen.

### 2. Datenabruf (HTTP, ODBC)

**Definition:** HTTP (Hypertext Transfer Protocol) und ODBC (Open Database Connectivity) sind Protokolle/Schnittstellen fuer den Abruf von Daten ueber das Netzwerk im Client-Server-Modell.

**HTTP:**
- Client (Browser) sendet Anfrage an Webserver → Server antwortet mit Daten
- Typisches Client-Server-Protokoll auf Anwendungsschicht (Port 80/443)
- Request-Response-Modell: Client fragt, Server antwortet
- Zustandslos (jede Anfrage ist unabhaengig)

**ODBC:**
- Standardisierte Schnittstelle fuer den Zugriff auf Datenbanken
- Client-Anwendung verbindet sich ueber ODBC-Treiber mit Datenbankserver
- Datenbank laeuft auf zentralem Server (z.B. MySQL, MS SQL, PostgreSQL)
- Reines Client-Server-Modell: Anfrage → Verarbeitung → Ergebnis

---

## Peer-to-Peer vs. Client-Server – Vergleich

| Kriterium | Peer-to-Peer (P2P) | Client-Server |
|-----------|---------------------|---------------|
| Architektur | Dezentral, alle gleichberechtigt | Zentral, Server stellt Dienste bereit |
| Verwaltung | Jeder Rechner verwaltet sich selbst | Zentrale Administration (z.B. Active Directory) |
| Sicherheit | Gering (lokale Benutzerkonten) | Hoch (zentrale Richtlinien, Gruppenrichtlinien) |
| Skalierbarkeit | Schlecht (empfohlen < 10 Geraete) | Gut (hunderte bis tausende Clients) |
| Kosten | Gering (keine Server-Hardware/-Lizenzen) | Hoeher (Server, Betriebssystem-Lizenzen) |
| Ausfallsicherheit | Robust (kein Single Point of Failure) | Abhaengig vom Server (Redundanz noetig) |
| Datensicherung | Dezentral auf jedem Geraet | Zentral auf dem Server |
| Benutzerverwaltung | Lokal auf jedem Rechner | Zentral (Single Sign-On moeglich) |
| Beispiel | Heimnetzwerk, kleine Buerogemeinschaft | Unternehmensnetzwerk mit Domaene |

### ASCII-Darstellung

**Peer-to-Peer:**
```
[PC-A] <-----> [PC-B]
  ^               ^
  |               |
  v               v
[PC-C] <-----> [PC-D]

Jeder kommuniziert direkt mit jedem.
Jeder kann Dienste anbieten UND nutzen.
```

**Client-Server:**
```
               [Server]
              /   |    \
             /    |     \
         [PC-A] [PC-B] [PC-C]
         Client  Client  Client

Clients fragen an, Server antwortet.
Zentrale Datenhaltung und Verwaltung.
```

---

## Praktische Szenarien

**Szenario 1 – P2P:** Ein Grafikdesign-Buero mit 5 Mitarbeitern teilt Dateien direkt ueber Windows-Freigaben. Jeder Mitarbeiter gibt seinen Projektordner frei. Es gibt keinen dedizierten Server. → P2P genuegt, da wenige Geraete, geringe Komplexitaet, niedrige Kosten.

**Szenario 2 – Client-Server:** Ein Unternehmen mit 150 Mitarbeitern benoetigt zentrale Benutzerverwaltung, einheitliche Gruppenrichtlinien und einen Fileserver. Mitarbeiter melden sich mit einem Domaenen-Konto an und haben ueberall Zugriff auf ihre Daten. → Client-Server mit Active Directory ist notwendig.

**Szenario 3 – HTTP (Client-Server):** Mitarbeiter rufen die Firmen-Intranetseite auf. Der Browser (Client) sendet eine HTTP-GET-Anfrage an den Webserver. Der Server verarbeitet die Anfrage und sendet die HTML-Seite zurueck. → Klassisches Client-Server-Modell.

**Szenario 4 – ODBC (Client-Server):** Eine Buchhaltungssoftware auf dem PC des Mitarbeiters verbindet sich ueber ODBC mit der zentralen SQL-Datenbank. Die Anwendung sendet SQL-Abfragen, der Server verarbeitet sie und liefert die Ergebnisse. → Datenverarbeitung findet auf dem Server statt.

---

## Typische Pruefungsaspekte

- Gegebenes Szenario bewerten: P2P oder Client-Server?
- Vor- und Nachteile beider Modelle benennen
- SMB/CIFS dem korrekten Einsatzbereich zuordnen
- HTTP als Client-Server-Protokoll erkennen
- Zusammenhang zwischen Domaene (Active Directory) und Client-Server verstehen

## Haeufige Fehler

- P2P wird als "unsicher" abgestempelt – es ist fuer kleine Netze voellig ausreichend
- Verwechslung: P2P-Netzwerk (LAN) mit P2P-Filesharing (BitTorrent) – in der Pruefung ist meist das LAN-Konzept gemeint
- ODBC wird als Protokoll bezeichnet – es ist eine Schnittstelle/API, kein Netzwerkprotokoll
- Vergessen, dass Client-Server-Modelle einen Single Point of Failure haben koennen (Server-Ausfall)

---

## Uebungen

**Aufgabe 1:** Ein Steuerbuero mit 4 Mitarbeitern moechte Dateien im Netzwerk austauschen. Budget ist begrenzt. Welches Netzwerkmodell empfiehlst du? Begruende.

**Aufgabe 2:** Nenne drei Vorteile eines Client-Server-Modells gegenueber Peer-to-Peer fuer ein Unternehmen mit 80 Mitarbeitern.

**Aufgabe 3:** Erklaere den Unterschied zwischen SMB und HTTP hinsichtlich Einsatzzweck und Modell.

**Aufgabe 4:** Warum ist ODBC typischerweise ein Client-Server-Konzept und nicht Peer-to-Peer?

**Aufgabe 5:** Ein Unternehmen waechst von 8 auf 30 Mitarbeiter. Bisher wurde P2P genutzt. Welche Probleme koennen auftreten und welche Umstellung ist sinnvoll?

---
---

# Loesungen

## Aufgabe 1
Peer-to-Peer. Begruendung: Nur 4 Geraete, geringes Budget (kein Server noetig), einfache Verwaltung (jeder gibt Ordner frei), keine komplexen Sicherheitsanforderungen. Windows-Arbeitsgruppe mit SMB-Freigaben genuegt.

## Aufgabe 2
1. Zentrale Benutzerverwaltung: Alle Konten werden an einer Stelle (Active Directory) verwaltet statt auf 80 einzelnen PCs.
2. Einheitliche Sicherheitsrichtlinien: Gruppenrichtlinien (GPOs) erzwingen Passwortregeln, Softwareupdates und Zugriffsrechte.
3. Zentrale Datensicherung: Daten liegen auf dem Server und koennen einheitlich gesichert werden statt auf 80 verschiedenen Rechnern.

## Aufgabe 3
- SMB: Protokoll fuer Dateifreigaben im LAN. Kann P2P (Arbeitsgruppe) oder Client-Server (Fileserver) genutzt werden. Einsatz: Zugriff auf freigegebene Ordner und Drucker.
- HTTP: Protokoll fuer Webanfragen. Immer Client-Server (Browser fragt, Server antwortet). Einsatz: Webseiten, APIs, Intranet.

## Aufgabe 4
ODBC ist eine Schnittstelle fuer Datenbankzugriffe. Datenbanken laufen auf zentralen Servern, die Anfragen von Clients entgegennehmen, verarbeiten und Ergebnisse zurueckliefern. Die Verarbeitungslogik liegt auf dem Server. Eine P2P-Architektur wuerde bedeuten, dass jeder Rechner eine eigene Datenbank betreibt – das fuehrt zu Dateninkonsistenzen und ist fuer gemeinsame Datenbestaende unpraktikabel.

## Aufgabe 5
Probleme bei P2P mit 30 Geraeten:
- Benutzerverwaltung wird unuebersichtlich (Konten auf 30 PCs pflegen)
- Keine einheitlichen Sicherheitsrichtlinien
- Dezentrale Datenhaltung erschwert Backups
- Zugriffskontrolle kaum kontrollierbar
- Broadcast-Traffic steigt

Empfehlung: Umstellung auf Client-Server mit Active Directory, zentralem Fileserver und Gruppenrichtlinien. Investition in Server-Hardware und Windows-Server-Lizenz.
