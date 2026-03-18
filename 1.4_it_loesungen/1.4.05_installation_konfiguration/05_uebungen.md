# Uebungen: 1.4.05 – Installation und Konfiguration

## Konsolenbefehle

**Aufgabe 1:** Nenne den Windows- und Linux-Befehl fuer folgende Aktionen:
- a) IP-Konfiguration anzeigen
- b) Erreichbarkeit eines Servers testen
- c) Ordner erstellen
- d) DNS-Abfrage durchfuehren
- e) Route zum Ziel verfolgen

**Aufgabe 2:** Ein Linux-Administrator moechte alle Dateien im Verzeichnis `/var/log/` auflisten, die aelter als 30 Tage sind. Welcher Befehl ist geeignet?

---

## Troubleshooting

**Aufgabe 3:** Ein Benutzer meldet: „Ich kann die Webseite firma.de nicht aufrufen." Beschreibe eine systematische Fehlersuche in 5 Schritten mit je einem passenden Konsolenbefehl.

**Aufgabe 4:** Der Befehl `ipconfig /all` zeigt folgende Ausgabe:
```
IP-Adresse: 169.254.12.34
Subnetzmaske: 255.255.0.0
Standardgateway: (leer)
DHCP: Ja
```
Was ist das Problem? Wie loest du es?

**Aufgabe 5:** Was ist der Unterschied zwischen `ping` und `tracert`? Wann nutzt du welchen Befehl?

---

## Installation und Konfiguration

**Aufgabe 6:** Beschreibe den Ablauf der Installation eines Betriebssystems (Windows) in 6 Schritten.

**Aufgabe 7:** Wie lautet der Befehl, um auf einem Linux-System die Berechtigungen der Datei `script.sh` so zu setzen, dass der Eigentuemer lesen, schreiben und ausfuehren darf, Gruppe und Andere nur lesen?

---

---

# Loesungen

## Aufgabe 1
- a) Windows: `ipconfig /all` | Linux: `ip a` oder `ifconfig`
- b) Windows: `ping server` | Linux: `ping server`
- c) Windows: `mkdir ordner` | Linux: `mkdir ordner`
- d) Windows: `nslookup domain` | Linux: `nslookup domain`
- e) Windows: `tracert ziel` | Linux: `traceroute ziel`

## Aufgabe 2
`find /var/log/ -type f -mtime +30` – Findet alle Dateien (-type f) im Verzeichnis, die vor mehr als 30 Tagen geaendert wurden (-mtime +30).

## Aufgabe 3
1. Kabel/WLAN pruefen → visuell
2. IP-Konfiguration pruefen → `ipconfig /all`
3. Gateway erreichbar? → `ping 192.168.1.1` (Gateway-IP)
4. Internet erreichbar? → `ping 8.8.8.8`
5. DNS funktioniert? → `nslookup firma.de`
→ Falls Schritt 4 OK aber 5 fehlschlaegt: DNS-Problem. DNS-Server pruefen oder `ipconfig /flushdns`.

## Aufgabe 4
Problem: Die IP-Adresse 169.254.x.x ist eine APIPA-Adresse (Automatic Private IP Addressing). Der PC konnte keine IP vom DHCP-Server beziehen.
Loesung: (1) `ipconfig /release` + `ipconfig /renew` versuchen. (2) Falls erfolglos: Netzwerkkabel/Switch pruefen. (3) DHCP-Server-Status pruefen (laeuft der Dienst? Adresspool erschoepft?).

## Aufgabe 5
`ping`: Testet, ob ein Ziel erreichbar ist (Antwortzeit, Paketverlust). Nutzen: Schneller Test der Konnektivitaet.
`tracert/traceroute`: Zeigt den Weg (alle Hops/Router) zum Ziel an. Nutzen: Feststellung, wo auf dem Weg ein Problem liegt.

## Aufgabe 6
(1) Boot-Medium erstellen (USB-Stick). (2) BIOS/UEFI: Boot-Reihenfolge aendern (USB zuerst). (3) Windows-Setup starten: Sprache, Lizenzschluessel. (4) Partitionierung/Formatierung der Festplatte. (5) Installation durchfuehren, Neustart. (6) Ersteinrichtung: Benutzerkonto, Netzwerk, Windows Update.

## Aufgabe 7
`chmod 744 script.sh` – Eigentuemer: rwx (7), Gruppe: r-- (4), Andere: r-- (4).
