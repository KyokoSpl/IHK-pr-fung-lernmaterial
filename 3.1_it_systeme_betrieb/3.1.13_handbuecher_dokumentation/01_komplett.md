# Komplett: 3.1.13 – Erstellen und Erweitern von Handbuechern fuer Benutzer und Systembetreuer

## Einordnung

- **Pruefungsteil:** 3.1 – Betreiben von IT-Systemen
- **Thema-ID:** 3.1.13
- **Thema:** Erstellen und Erweitern von Handbuechern fuer Benutzer und Systembetreuer

## Ziel

Du musst Dokumentationstypen kennen, zielgruppengerechte Handbuecher erstellen und Checklisten fuer typische IT-Aufgaben entwerfen koennen. Die Pruefung fragt haeufig nach dem Unterschied zwischen Benutzer- und Administratordokumentation.

---

## Themenkreis 1: Checklisten

**Definition:** Eine Checkliste ist eine strukturierte Abhakliste, die sicherstellt, dass alle notwendigen Schritte oder Pruefpunkte bei einer Aufgabe beruecksichtigt werden.

**Kernaussagen:**
- Checklisten reduzieren Fehler durch Vergessen
- Sie sind kuerzer und weniger detailliert als SOPs (→ Thema 3.1.12)
- Typisch fuer wiederkehrende Routine-Aufgaben
- Jeder Punkt kann abgehakt werden (✓ / ✗)

**Typische IT-Checklisten:**

| Checkliste | Typische Pruefpunkte |
|---|---|
| Server-Inbetriebnahme | Hardware verbaut? BIOS konfiguriert? OS installiert? Netzwerk konfiguriert? Monitoring eingerichtet? Backup konfiguriert? |
| Arbeitsplatz-Rollout | PC aufgestellt? Netzwerk verkabelt? OS installiert? Software installiert? Drucker eingerichtet? Nutzer eingewiesen? |
| Sicherheitsaudit | Firewall-Regeln geprueft? Updates installiert? Passwoerter konform? Backups getestet? Zugaenge dokumentiert? |
| Onboarding neuer Mitarbeiter | AD-Konto erstellt? E-Mail eingerichtet? Berechtigungen gesetzt? Hardware ausgegeben? Einweisung erfolgt? |
| Wartungsfenster | Change genehmigt? Nutzer informiert? Monitoring auf Wartung gesetzt? Aenderung durchgefuehrt? Verifizierung abgeschlossen? Monitoring reaktiviert? |

**Aufbau einer Checkliste:**

```
Checkliste: Server-Inbetriebnahme
Datum: ___________    Verantwortlich: ___________
Server-Name: ___________

[ ] Hardware in Rack eingebaut
[ ] Stromversorgung angeschlossen (redundant)
[ ] Netzwerkkabel angeschlossen (Management + Produktion)
[ ] BIOS/UEFI konfiguriert (Boot-Reihenfolge, RAID)
[ ] Betriebssystem installiert
[ ] IP-Adresse konfiguriert (statisch oder DHCP-Reservierung)
[ ] Hostname gesetzt und DNS-Eintrag erstellt
[ ] Updates und Patches installiert
[ ] Monitoring-Agent installiert und geprueft
[ ] Backup-Job konfiguriert und getestet
[ ] Firewall-Regeln geprueft
[ ] Dokumentation aktualisiert (CMDB, Netzwerkplan)
[ ] Abnahme durch Verantwortlichen

Unterschrift: ___________
```

---

## Themenkreis 2: Programm- und Konfigurationsdokumentation

**Definition:** Die Programm- und Konfigurationsdokumentation beschreibt den Aufbau, die Konfiguration und die Funktionsweise von IT-Systemen und Software. Sie dient als Referenz fuer Administratoren und Entwickler.

### Dokumentationstypen

| Typ | Zielgruppe | Inhalt | Beispiel |
|---|---|---|---|
| **Benutzerdokumentation** | Endanwender | Bedienung, Funktionen, FAQ | „Wie aendere ich mein Passwort?" |
| **Administratordokumentation** | Systemadministratoren | Installation, Konfiguration, Wartung | „Datenbank-Backup manuell starten" |
| **Programmdokumentation** | Entwickler | Quellcode-Beschreibung, Architektur, APIs | „Funktion calculatePrice(): Parameter, Rueckgabewert" |
| **Konfigurationsdokumentation** | Admins / DevOps | Aktuelle Systemeinstellungen, Parameter | „Webserver: Port 443, TLS 1.3, DocumentRoot /var/www" |
| **Netzwerkdokumentation** | Netzwerk-Admins | IP-Schema, VLAN-Zuordnung, Netzwerkplaene | „VLAN 10: Verwaltung, 192.168.10.0/24" |

### Benutzer- vs. Administratordokumentation

| Aspekt | Benutzerdokumentation | Administratordokumentation |
|---|---|---|
| Zielgruppe | Endanwender (wenig IT-Wissen) | IT-Fachpersonal |
| Sprache | Einfach, verstaendlich, wenig Fachbegriffe | Technisch, praezise, Fachbegriffe erlaubt |
| Inhalt | Bedienung, Funktionen, Schritt-fuer-Schritt-Anleitungen | Installation, Konfiguration, Fehlerbehebung |
| Screenshots | Viele (zur Orientierung) | Wenige (CLI-Befehle, Config-Dateien) |
| Tiefe | Oberflaeche (was tut die Software?) | Tiefgehend (wie funktioniert das System?) |
| Beispiel | „Klicken Sie auf Datei → Drucken" | „SMTP-Relay konfigurieren: postconf -e 'relayhost = mail.firma.de'" |

### Runbook / Betriebshandbuch

**Definition:** Ein Runbook ist eine Sammlung von Anleitungen fuer den taeglichen IT-Betrieb. Es enthaelt SOPs, Checklisten, Kontaktlisten und Notfallprozeduren.

**Typischer Aufbau eines Runbooks:**

| Kapitel | Inhalt |
|---|---|
| 1. Systemuebersicht | Architekturdiagramm, Komponentenliste, Abhaengigkeiten |
| 2. Kontaktliste | Ansprechpartner, Rufbereitschaft, Hersteller-Support |
| 3. Zugangsdaten | Verweis auf Passwort-Manager (KEINE Passwoerter im Runbook!) |
| 4. Taeglliche Aufgaben | Monitoring pruefen, Backup-Status pruefen |
| 5. SOPs | Server-Neustart, Backup-Restore, Failover, Patching |
| 6. Checklisten | Wartungsfenster, Server-Inbetriebnahme, Onboarding |
| 7. Fehlerbehebung | Known Errors und Loesungen |
| 8. Notfallprozeduren | Disaster Recovery, Eskalation |

### Qualitaetskriterien fuer gute Dokumentation

| Kriterium | Beschreibung |
|---|---|
| Aktuell | Wird bei jeder Aenderung aktualisiert |
| Vollstaendig | Alle relevanten Informationen enthalten |
| Verstaendlich | An die Zielgruppe angepasst |
| Strukturiert | Logischer Aufbau, Inhaltsverzeichnis, Nummerierung |
| Auffindbar | Zentral abgelegt (Wiki, SharePoint, Runbook) |
| Versioniert | Aenderungen nachvollziehbar (Versionsnummer, Datum, Autor) |

### Typische Pruefungsaspekte
- Unterschied Benutzer- vs. Administratordokumentation erklaeren
- Aufbau einer Checkliste erstellen
- Zielgruppengerechte Dokumentation verfassen
- Aufbau eines Runbooks beschreiben
- Qualitaetskriterien fuer Dokumentation benennen

### Haeufige Fehler
- Dokumentation einmal erstellen und nie aktualisieren → veraltet schnell
- Passwoerter in der Dokumentation speichern → Sicherheitsrisiko (Verweis auf Passwort-Manager)
- Zielgruppe nicht beachten → Endanwender verstehen keine CLI-Befehle, Admins brauchen keine Screenshots
- Dokumentation nur im Kopf behalten → „Bus-Faktor": Was passiert, wenn der einzige Wissende ausfaellt?

---

## Uebungen

**Aufgabe 1:** Erklaere den Unterschied zwischen einer Benutzerdokumentation und einer Administratordokumentation. Nenne je zwei Beispiele fuer typische Inhalte.

**Aufgabe 2:** Erstelle eine Checkliste mit mindestens 8 Punkten fuer die Aufgabe „Neuen Arbeitsplatz-PC einrichten".

**Aufgabe 3:** Ein Kollege hat eine Anleitung geschrieben: „Server neustarten: Auf Herunterfahren klicken und warten." Was fehlt in dieser Dokumentation? Nenne mindestens vier Verbesserungen.

**Aufgabe 4:** Nenne fuenf Qualitaetskriterien fuer gute IT-Dokumentation und erklaere, warum jedes Kriterium wichtig ist.

**Aufgabe 5:** Was ist ein Runbook? Nenne vier typische Kapitel und beschreibe deren Inhalt.

**Aufgabe 6:** Warum sollten Passwoerter **nicht** in der Dokumentation stehen? Welche Alternative gibt es?

**Aufgabe 7:** Schreibe eine kurze Administratordokumentation (ca. 5–8 Zeilen) fuer die Konfiguration eines statischen DNS-Eintrags auf einem Linux-Server. Zielgruppe: Systemadministrator.

---
---

# Loesungen

## Aufgabe 1
- **Benutzerdokumentation:** Richtet sich an Endanwender mit wenig IT-Wissen. Inhalte: (1) Anleitung zur Passwortaenderung, (2) FAQ zu haeufigen Fehlermeldungen.
- **Administratordokumentation:** Richtet sich an IT-Fachpersonal. Inhalte: (1) Konfiguration des Mailserver-Relays, (2) Anleitung zur Wiederherstellung eines Backups.
- **Unterschied:** Benutzerdokumentation ist einfacher formuliert, nutzt Screenshots und erklaert die Bedienung. Administratordokumentation ist technisch, nutzt Fachbegriffe und beschreibt Konfiguration und Fehlerbehebung.

## Aufgabe 2
```
Checkliste: Neuen Arbeitsplatz-PC einrichten
Datum: ___________  Mitarbeiter: ___________

[ ] PC auspacken und am Arbeitsplatz aufstellen
[ ] Monitor, Tastatur, Maus anschliessen
[ ] Netzwerkkabel einstecken (oder WLAN konfigurieren)
[ ] PC einschalten, Betriebssystem einrichten / Domaene beitreten
[ ] Windows-Updates installieren
[ ] Standardsoftware installieren (Office, Browser, Virenscanner)
[ ] Drucker einrichten
[ ] E-Mail-Konto konfigurieren
[ ] Netzlaufwerke verbinden
[ ] Benutzer einweisen (Anmeldung, Grundfunktionen)
[ ] Dokumentation aktualisieren (Inventarliste, CMDB)
```

## Aufgabe 3
Fehlende Punkte:
1. **Voraussetzungen:** Welche Rechte/Zugaenge werden benoetigt? (Admin-Zugang)
2. **Vorbereitung:** Monitoring auf Wartung setzen, Nutzer informieren, Change-Ticket pruefen
3. **Detailliertere Schritte:** Dienste vorher pruefen, Reihenfolge beachten, Wartezeit nach Shutdown
4. **Verifizierung:** Nach dem Neustart pruefen, ob alle Dienste laufen und die Anwendung erreichbar ist
5. **Nachbereitung:** Monitoring reaktivieren, Nutzer informieren, Ticket dokumentieren und schliessen
6. **Rollback-Plan:** Was tun, wenn der Server nach dem Neustart nicht mehr startet?

## Aufgabe 4
1. **Aktuell:** Veraltete Dokumentation fuehrt zu falschen Handlungen.
2. **Vollstaendig:** Fehlende Informationen erzwingen Nachfragen oder Fehler.
3. **Verstaendlich:** Unverstaendliche Dokumentation wird nicht genutzt.
4. **Strukturiert:** Ohne Struktur findet man Informationen nicht schnell genug (wichtig im Notfall).
5. **Versioniert:** Aenderungen muessen nachvollziehbar sein, um bei Problemen auf die vorherige Version zurueckgreifen zu koennen.

## Aufgabe 5
Ein **Runbook** ist ein Betriebshandbuch, das alle Informationen und Anleitungen fuer den taeglichen IT-Betrieb buendelt. Vier typische Kapitel:
1. **Systemuebersicht:** Architekturdiagramm, Komponentenliste, Abhaengigkeiten zwischen Systemen.
2. **SOPs:** Schritt-fuer-Schritt-Anleitungen fuer wiederkehrende Aufgaben (z.B. Backup, Patching).
3. **Kontaktliste:** Ansprechpartner fuer jedes System, Rufbereitschaft, Hersteller-Support.
4. **Fehlerbehebung:** Bekannte Fehler (Known Errors) mit Symptomen und Loesungen.

## Aufgabe 6
Passwoerter sollten **nicht** in der Dokumentation stehen, weil:
- Dokumentation wird oft von vielen Personen gelesen (Wiki, SharePoint)
- Passwoerter koennten von Unbefugten eingesehen werden
- Bei einem Leak waeren alle dokumentierten Zugaenge kompromittiert

**Alternative:** Verweis auf einen **Passwort-Manager** (z.B. KeePass, 1Password, HashiCorp Vault). In der Dokumentation steht nur: „Zugangsdaten: siehe Passwort-Manager, Eintrag ‚Mailserver-Admin'."

## Aufgabe 7
```
DNS-Eintrag auf Linux-Server (bind9) hinzufuegen:

1. Zonendatei oeffnen:
   nano /etc/bind/zones/db.firma.local

2. Neuen A-Record hinzufuegen:
   server-neu    IN    A    192.168.10.50

3. Serial-Nummer in der Zonendatei erhoehen (Format: YYYYMMDDNN)

4. Konfiguration pruefen:
   named-checkzone firma.local /etc/bind/zones/db.firma.local

5. Bind neu laden:
   systemctl reload bind9

6. Testen:
   nslookup server-neu.firma.local
```
