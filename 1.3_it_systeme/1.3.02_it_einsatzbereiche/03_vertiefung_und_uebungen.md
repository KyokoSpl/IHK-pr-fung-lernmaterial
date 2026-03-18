# Vertiefung und Uebungen: 1.3.02 – Typische IT-Systeme und deren Einsatzbereiche

## Vertiefung

### Client-Server vs. Peer-to-Peer

| Kriterium | Client-Server | Peer-to-Peer |
|---|---|---|
| Verwaltung | Zentral (Admin) | Dezentral (jeder Nutzer) |
| Sicherheit | Hoch (zentrale Policies) | Gering (keine zentrale Kontrolle) |
| Skalierbarkeit | Gut | Schlecht ab ~10 Geraeten |
| Kosten | Hoeher (Server-HW/Lizenzen) | Geringer |
| Eignung | Unternehmen, >10 Nutzer | Kleine Bueros, Homegroups |

### Domaene vs. Arbeitsgruppe

| Kriterium | Domaene | Arbeitsgruppe |
|---|---|---|
| Verwaltung | Zentral (Domain Controller) | Lokal (jeder PC einzeln) |
| Benutzerkonten | Zentral im AD | Lokal auf jedem PC |
| Gruppenrichtlinien | Ja (GPO) | Nein |
| Max. Geraete | Unbegrenzt | Empfohlen < 10 |
| Kosten | Server + Lizenzen noetig | Kostenfrei |

### Typische Pruefungsaspekte
- Szenario: Welches System fuer welchen Einsatzzweck?
- Vorteile einer Domaene benennen koennen
- OSI-Schicht zu Protokoll zuordnen
- BYOD-Risiken bewerten

### Haeufige Fehler
- DNS mit DHCP verwechseln (DNS = Namensaufloesung, DHCP = IP-Vergabe)
- Thin Client und Terminal verwechseln: Thin Client ist die Hardware, Terminalserver ist der Dienst
- BYOD wird als rein positiv dargestellt → Datenschutzrisiken vergessen

---

## Uebungen

**Aufgabe 1:** Ein Unternehmen mit 80 Mitarbeitern moechte alle PCs zentral verwalten, Software einheitlich verteilen und Passwortrichtlinien durchsetzen. Welche Loesung empfiehlst du? Begruende.

**Aufgabe 2:** Ordne folgende Protokolle den OSI-Schichten zu: Ethernet, IP, TCP, DNS, ARP.

**Aufgabe 3:** Nenne drei Vorteile und zwei Risiken von BYOD.

**Aufgabe 4:** Erklaere den Unterschied zwischen synchroner und asynchroner Kommunikation. Nenne je zwei Beispiele.

**Aufgabe 5:** Ein Aussendienst-Mitarbeiter verliert sein Firmen-Tablet. Welche MDM-Massnahme sollte sofort ergriffen werden?

---

## Loesungen

**Aufgabe 1:** Active-Directory-Domaene mit Domain Controller. Begruendung: Zentrale Benutzerverwaltung, Gruppenrichtlinien fuer Passwort-Policy und Softwareverteilung, Single Sign-On, skalierbar fuer 80+ Nutzer.

**Aufgabe 2:** Ethernet: Schicht 1-2, ARP: Schicht 2, IP: Schicht 3, TCP: Schicht 4, DNS: Schicht 7.

**Aufgabe 3:** Vorteile: (1) Kosteneinsparung (kein Geraetekauf), (2) Hoehere Mitarbeiterzufriedenheit (vertrautes Geraet), (3) Flexibilitaet. Risiken: (1) Datenschutzprobleme (private + geschaeftliche Daten vermischt), (2) Sicherheitsrisiko (keine zentrale Kontrolle ueber Updates/Konfiguration).

**Aufgabe 4:** Synchron = Echtzeit, beide Parteien gleichzeitig aktiv. Beispiele: Videocall, Telefonat. Asynchron = Zeitversetzt, Antwort nicht sofort. Beispiele: E-Mail, Forum.

**Aufgabe 5:** Fernloeschung (Remote Wipe) ueber das MDM-System, um Unternehmensdaten zu schuetzen. Zusaetzlich: Geraet sperren, Vorfall melden, Passwoerter aendern.
