# Beispiele: 1.4.05 – Installation und Konfiguration

## Troubleshooting-Szenario

**Beispiel 1:** Ein Mitarbeiter meldet: „Ich kann keine Webseiten aufrufen, aber mein Kollege am Nachbarplatz schon."

**Analyse:**
1. `ipconfig /all` → IP-Adresse pruefen. Ergebnis: 169.254.x.x (APIPA-Adresse)
2. → Der PC hat keine IP vom DHCP-Server erhalten
3. `ipconfig /release` + `ipconfig /renew` → Neue IP anfordern
4. Falls kein DHCP: Kabel pruefen, Switch-Port pruefen, DHCP-Server pruefen

---

**Beispiel 2:** Ein Azubi meldet: „Ping auf 8.8.8.8 funktioniert, aber google.de nicht."

**Analyse:**
- Internetverbindung funktioniert (Ping auf IP erfolgreich)
- Problem liegt bei **DNS-Namensaufloesung**
- `nslookup google.de` → Timeout/Fehler?
- Loesung: DNS-Server-Konfiguration pruefen oder `ipconfig /flushdns`

---

## Konsolenbefehle

**Beispiel 3:** Einen Ordner mit Unterordnern erstellen und eine Datei kopieren:
```
Windows:
mkdir C:\Projekte\WebApp
copy C:\Vorlagen\config.ini C:\Projekte\WebApp\

Linux:
mkdir -p /home/user/projekte/webapp
cp /home/user/vorlagen/config.ini /home/user/projekte/webapp/
```

---

## Softwareanpassung

**Beispiel 4:** Ein Unternehmen rollt einen neuen Browser fuer alle 200 Mitarbeiter aus. Startseite soll automatisch auf das Intranet gesetzt werden.

**Loesung:** Gruppenrichtlinie (GPO) in Active Directory:
- Computerkonfiguration → Administrative Vorlagen → Google Chrome/Microsoft Edge → Startseite festlegen
- Vorteil: Zentrale Verwaltung, kein manueller Eingriff auf 200 PCs noetig.

---

## Hardware-Installation

**Beispiel 5:** Ein neuer Netzwerkdrucker soll im Buero eingerichtet werden.

**Schritte:**
1. Drucker physisch anschliessen (Ethernet oder WLAN)
2. Feste IP-Adresse konfigurieren (z.B. 192.168.1.200)
3. Auf dem Druckserver: Druckertreiber installieren, Drucker hinzufuegen
4. Freigabe erstellen (SMB)
5. Per GPO auf alle Clients verteilen
6. Testseite drucken
