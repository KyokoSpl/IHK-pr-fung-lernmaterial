# Uebungen: 3.1.03 – Netzwerkkonzepte benennen und charakterisieren

## Netzwerktypen und Topologien

**Aufgabe 1:** Ordne die folgenden Szenarien dem richtigen Netzwerktyp zu (PAN, LAN, MAN, WAN, GAN):
a) Ein Buero mit 30 PCs, verbunden ueber Switches
b) Zwei Unternehmensstandorte in verschiedenen Laendern, verbunden ueber VPN
c) Ein Bluetooth-Headset, verbunden mit einem Smartphone
d) Drei Krankenhaeuser einer Stadt, verbunden ueber Glasfaser
e) Das Internet

**Aufgabe 2:** Zeichne eine Stern-Topologie mit einem Switch und vier PCs. Nenne einen Vorteil und einen Nachteil.

**Aufgabe 3:** Erklaere den Unterschied zwischen physischer und logischer Topologie. Gib ein Beispiel, bei dem beide unterschiedlich sind.

---

## VLAN

**Aufgabe 4:** Ein Unternehmen hat folgende Abteilungen: Personal (15 PCs), IT (20 PCs), Buchhaltung (10 PCs), Gaeste (WLAN). Alle Geraete haengen an zwei Switches.
a) Wie viele VLANs wuerdest du einrichten?
b) Warum ist ein Trunk-Port zwischen den Switches noetig?
c) Was wird fuer die Kommunikation zwischen den VLANs benoetigt?

**Aufgabe 5:** Erklaere, was ein 802.1Q-Tag ist und wann er einem Frame hinzugefuegt wird.

---

## Strukturierte Verkabelung

**Aufgabe 6:** Benenne die drei Ebenen der strukturierten Verkabelung (Primaer, Sekundaer, Tertiaer) und ordne jeweils zu: Bereich, typisches Medium und maximale Laenge.

**Aufgabe 7:** Welche Kabelkategorie wird fuer 10-Gigabit-Ethernet ueber Kupfer benoetigt? Wie lang darf das Installationskabel der Tertiaerverkabelung maximal sein?

---

## WLAN-Sicherheit

**Aufgabe 8:** Vergleiche WPA2-Personal und WPA2-Enterprise. Nenne fuer jedes Verfahren: Authentifizierungsmethode, typischen Einsatzbereich und einen Vor-/Nachteil.

**Aufgabe 9:** Ein Kollege schlaegt vor, die SSID des Firmen-WLANs zu verbergen und einen MAC-Filter einzurichten. Reichen diese Massnahmen als Sicherheitskonzept? Begruende.

**Aufgabe 10:** Nenne drei Sicherheitsmassnahmen fuer ein Unternehmens-WLAN und bewerte deren Wirksamkeit.

---

## VPN

**Aufgabe 11:** Erklaere den Unterschied zwischen Site-to-Site-VPN und End-to-Site-VPN. Gib jeweils ein Praxisbeispiel.

**Aufgabe 12:** Was ist Split Tunneling und welches Sicherheitsrisiko birgt es?

---

## Zugriffskontrolle

**Aufgabe 13:** Beschreibe den Ablauf einer 802.1X-Authentifizierung mit RADIUS in vier Schritten.

**Aufgabe 14:** Erklaere das Kerberos-Prinzip. Was ist ein TGT und warum ermoeglicht es Single Sign-On?

**Aufgabe 15:** Vergleiche RADIUS und Kerberos hinsichtlich Einsatzgebiet, Authentifizierungsmethode und SSO-Faehigkeit.

---

## Sicherheitskonzepte

**Aufgabe 16:** Erklaere das Prinzip "Defense in Depth" und nenne vier konkrete Sicherheitsschichten in einem Unternehmensnetzwerk.

**Aufgabe 17:** Was ist eine DMZ und warum werden oeffentlich erreichbare Server dort platziert?

---
---

# Loesungen

## Aufgabe 1
a) LAN – lokal begrenztes Netzwerk im Gebaeude
b) WAN – laenderuebergreifende Verbindung
c) PAN – Bluetooth-Verbindung im Nahbereich
d) MAN – Stadtweites Netzwerk
e) GAN – Globales Netzwerk (Internet)

## Aufgabe 2
```
        [PC-A]
          |
[PC-B]--[Switch]--[PC-C]
          |
        [PC-D]
```
Vorteil: Ausfall eines PCs betrifft nicht die anderen; einfache Erweiterung.
Nachteil: Switch ist Single Point of Failure – faellt der Switch aus, ist das gesamte Netz getrennt.

## Aufgabe 3
Physische Topologie = tatsaechliche Kabelverbindungen. Logische Topologie = Datenfluss im Netzwerk. Beispiel: Token Ring ist physisch eine Stern-Topologie (alle Kabel fuehren zum MAU/MSAU), aber logisch ein Ring (Token wird von Station zu Station weitergereicht).

## Aufgabe 4
a) 4 VLANs: VLAN 10 (Personal), VLAN 20 (IT), VLAN 30 (Buchhaltung), VLAN 40 (Gaeste)
b) Ein Trunk-Port ist noetig, weil VLANs sich ueber beide Switches erstrecken. Der Trunk transportiert Frames aller VLANs ueber eine Leitung, markiert mit 802.1Q-Tags.
c) Ein Layer-3-Switch oder Router fuer Inter-VLAN-Routing. Ohne Routing koennen VLANs nicht miteinander kommunizieren.

## Aufgabe 5
Ein 802.1Q-Tag ist ein 4 Byte grosses Feld, das in den Ethernet-Frame eingefuegt wird. Es enthaelt u.a. die VLAN-ID (12 Bit, Werte 0–4095). Der Tag wird hinzugefuegt, wenn ein Frame ueber einen Trunk-Port gesendet wird, damit der empfangende Switch weiss, zu welchem VLAN der Frame gehoert. An Access-Ports werden Frames ohne Tag gesendet (Untagged).

## Aufgabe 6
1. Primaerverkabelung (Gelaende/Campus): Zwischen Gebaeuden, Glasfaser Singlemode, bis mehrere Kilometer
2. Sekundaerverkabelung (Gebaeude): Zwischen Stockwerken (Steigbereiche), Glasfaser Multimode, bis ca. 500 m
3. Tertiaerverkabelung (Etage): Vom Etagenverteiler zur Datendose am Arbeitsplatz, Kupfer Cat6a/Cat7, max. 90 m Installationskabel (+ 10 m Patchkabel = 100 m gesamt)

## Aufgabe 7
Cat 6a (oder Cat 7) wird fuer 10-Gigabit-Ethernet ueber Kupfer benoetigt. Das Installationskabel der Tertiaerverkabelung darf maximal 90 Meter lang sein. Zusammen mit den Patchkabeln (je 5 m auf Switch- und Endgeraeteseite) ergibt sich eine Gesamtlaenge von 100 m.

## Aufgabe 8
- **WPA2-Personal (PSK):** Authentifizierung mit gemeinsamem Passwort (Pre-Shared Key). Einsatz: Kleine Netze, Heimbereiche. Vorteil: Einfache Einrichtung. Nachteil: Alle nutzen dasselbe Passwort, bei Mitarbeiterwechsel muss es geaendert werden.
- **WPA2-Enterprise (802.1X):** Authentifizierung mit individuellen Zugangsdaten ueber RADIUS-Server. Einsatz: Unternehmen. Vorteil: Individuelle Konten, dynamische VLAN-Zuweisung moeglich. Nachteil: RADIUS-Server noetig, hoehere Komplexitaet.

## Aufgabe 9
Nein, das reicht nicht. SSID verbergen ist kein Sicherheitsmerkmal – die SSID kann mit Netzwerk-Tools (z.B. airodump-ng) trotzdem ausgelesen werden. MAC-Filterung kann durch MAC-Spoofing umgangen werden. Wirksame Massnahmen sind: WPA2/WPA3-Verschluesselung, 802.1X-Authentifizierung mit RADIUS und ein separates Gastnetz.

## Aufgabe 10
1. **WPA2/WPA3-Verschluesselung** – Hoch: Schuetzt Daten vor Abhoeren
2. **802.1X + RADIUS** – Sehr hoch: Individuelle Authentifizierung, entzieht einzelnen Nutzern den Zugang
3. **Gastnetz in eigenem VLAN** – Hoch: Trennt Gastverkehr vom Produktionsnetz, verhindert Zugriff auf interne Ressourcen

## Aufgabe 11
- **Site-to-Site-VPN:** Verbindet zwei Standort-Netzwerke permanent ueber einen verschluesselten Tunnel. Die Router/Firewalls an beiden Standorten bauen den Tunnel auf. Beispiel: Hauptsitz und Filiale einer Firma.
- **End-to-Site-VPN (Remote Access):** Ein einzelner Client (Laptop/Smartphone) verbindet sich ueber VPN-Software mit dem Firmennetz. Beispiel: Homeoffice-Mitarbeiter greift auf interne Server zu.

## Aufgabe 12
Split Tunneling bedeutet, dass nur der Datenverkehr zum Firmennetz ueber den VPN-Tunnel geleitet wird. Privater Traffic (z.B. YouTube, Social Media) geht direkt ins Internet. Sicherheitsrisiko: Der Client ist gleichzeitig mit dem Internet und dem Firmennetz verbunden. Malware auf dem Client koennte ueber den VPN-Tunnel ins Firmennetz gelangen, ohne die Unternehmens-Firewall zu passieren.

## Aufgabe 13
1. Der Client (Supplicant) verbindet sich mit dem Access Point (Authenticator) und sendet seine Zugangsdaten (EAP-Identitaet).
2. Der Access Point leitet die Zugangsdaten als RADIUS-Access-Request an den RADIUS-Server weiter.
3. Der RADIUS-Server prueft die Credentials gegen den Verzeichnisdienst (z.B. Active Directory) und sendet Access-Accept oder Access-Reject zurueck.
4. Bei Accept gewaehrt der Access Point dem Client Netzwerkzugang (ggf. dynamische VLAN-Zuweisung).

## Aufgabe 14
Kerberos ist ein Ticket-basiertes Authentifizierungsprotokoll. Der Benutzer meldet sich einmal an und erhaelt vom KDC (Key Distribution Center) ein TGT (Ticket Granting Ticket). Das TGT ist der Nachweis der erfolgreichen Authentifizierung. Wenn der Benutzer auf einen Dienst (z.B. Fileserver) zugreifen will, legt er das TGT vor und erhaelt ein Service Ticket – ohne erneute Passworteingabe. Dadurch wird Single Sign-On (SSO) ermoeglicht.

## Aufgabe 15
| Kriterium | RADIUS | Kerberos |
|-----------|--------|----------|
| Einsatzgebiet | WLAN (802.1X), VPN, Remote Access | Windows-Domaene, interne Dienste |
| Authentifizierung | Benutzername/Passwort ueber EAP | Ticket-basiert (TGT + Service Tickets) |
| SSO | Nein | Ja |

## Aufgabe 16
Defense in Depth ("Verteidigung in der Tiefe") bedeutet, mehrere unabhaengige Sicherheitsschichten einzusetzen, sodass der Ausfall einer Schicht nicht das gesamte System kompromittiert. Vier Schichten:
1. **Perimeter-Sicherheit:** Firewall, DMZ, IDS/IPS
2. **Netzwerksegmentierung:** VLANs, Zugriffsregeln zwischen Segmenten
3. **Endpoint Security:** Virenscanner, Personal Firewall, Geraeteverschluesselung
4. **Zugriffskontrolle:** 802.1X, RADIUS, Berechtigungskonzepte (Least Privilege)

## Aufgabe 17
Eine DMZ (Demilitarisierte Zone) ist ein separates Netzwerksegment zwischen dem internen LAN und dem Internet. Oeffentlich erreichbare Server (Webserver, Mailserver) werden dort platziert, weil: (1) Sie aus dem Internet erreichbar sein muessen, (2) bei einer Kompromittierung das interne Netz durch eine weitere Firewall geschuetzt bleibt, (3) die Angriffsflaeche auf das interne Netz minimiert wird.
