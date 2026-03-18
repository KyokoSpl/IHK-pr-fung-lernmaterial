# Uebungen: 1.6.01 – IT-Sicherheit auf Grundschutzniveau

## Aufgabe 1: Schutzziele zuordnen
Ordne folgende Szenarien dem verletzten Schutzziel zu (Vertraulichkeit, Integritaet, Verfuegbarkeit):

a) Ein Mitarbeiter kann seinen E-Mail-Server nicht erreichen
b) Eine Excel-Datei wurde ohne Berechtigung veraendert
c) Ein USB-Stick mit Kundendaten wird im Zug vergessen
d) Nach einem Stromausfall sind Datenbank-Eintraege beschaedigt
e) Ein Hacker liest vertrauliche E-Mails mit

## Aufgabe 2: Verschluesselung
Erklaere in 3 Saetzen den Ablauf der hybriden Verschluesselung und warum man nicht nur asymmetrische Verschluesselung verwendet.

## Aufgabe 3: TOM zuordnen
Ordne folgende Massnahmen der richtigen TOM-Kategorie zu:
a) Kameraüberwachung am Gebaeude
b) Active-Directory-Gruppenrichtlinien
c) Festplattenverschluesselung mit BitLocker
d) Passwort-Policy mit 12 Zeichen Minimum
e) Taegliches inkrementelles Backup

## Aufgabe 4: DSGVO-Grundsaetze
Nenne 5 der 7 Verarbeitungsgrundsaetze der DSGVO und gib jeweils ein IT-Beispiel.

## Aufgabe 5: Anonymisierung vs. Pseudonymisierung
Ein Unternehmen moechte Kundendaten fuer eine Marktanalyse nutzen.
a) Erklaere, ob die DSGVO bei anonymisierten Daten gilt.
b) Erklaere, ob die DSGVO bei pseudonymisierten Daten gilt.
c) Nenne je ein konkretes Beispiel.

## Aufgabe 6: Rollenunterscheidung
Vervollstaendige die Tabelle:

| Kriterium | IT-Sicherheitsbeauftragter | Datenschutzbeauftragter |
|---|---|---|
| Gesetzliche Pflicht? | ? | ? |
| Weisungsfrei? | ? | ? |
| Fokus? | ? | ? |

## Aufgabe 7: Betroffenenrechte
Ein Kunde fordert die Loeschung seiner Daten. Nenne 2 Gruende, warum das Unternehmen die Loeschung verweigern darf.

---
---

# Loesungen

## Loesung 1
a) **Verfuegbarkeit** – System nicht erreichbar
b) **Integritaet** – Daten unbefugt veraendert
c) **Vertraulichkeit** – Daten gelangen an Unbefugte
d) **Integritaet** – Daten beschaedigt/unvollstaendig
e) **Vertraulichkeit** – Unbefugter Zugriff auf Kommunikation

## Loesung 2
Bei der hybriden Verschluesselung wird zunaechst asymmetrische Verschluesselung (z.B. RSA) genutzt, um einen zufaellig erzeugten symmetrischen Session-Key sicher auszutauschen. Danach werden alle Daten mit dem schnellen symmetrischen Verfahren (z.B. AES) verschluesselt. Man nutzt nicht nur asymmetrische Verschluesselung, weil diese fuer grosse Datenmengen zu langsam ist.

## Loesung 3
a) **Zutrittskontrolle** – physische Sicherung des Gebaeudes
b) **Zugriffskontrolle** – Berechtigungen ueber Gruppenrichtlinien
c) **Weitergabekontrolle** – Verschluesselung von Datentraegern
d) **Zugangskontrolle** – Authentifizierung am System
e) **Verfuegbarkeitskontrolle** – Datensicherung

## Loesung 4
1. **Rechtmaessigkeit:** Daten nur mit Rechtsgrundlage verarbeiten (z.B. Einwilligung oder Vertrag)
2. **Zweckbindung:** Daten nur fuer den angegebenen Zweck nutzen (z.B. Kontaktdaten nur fuer Anfrage)
3. **Datenminimierung:** Nur notwendige Daten erheben (z.B. kein Geburtsdatum fuer Newsletter)
4. **Richtigkeit:** Daten aktuell halten (z.B. Adressaenderung einpflegen)
5. **Speicherbegrenzung:** Daten nicht laenger als noetig speichern (z.B. Bewerbungen nach 6 Monaten loeschen)

## Loesung 5
a) Nein, die DSGVO gilt NICHT fuer anonymisierte Daten, da kein Personenbezug mehr herstellbar ist.
b) Ja, die DSGVO gilt fuer pseudonymisierte Daten, da der Personenbezug ueber die Zuordnungstabelle wiederhergestellt werden kann.
c) Anonymisiert: „60% der Nutzer verwenden Chrome" – keine Zuordnung zu Personen.
   Pseudonymisiert: „Nutzer U-4711 hat 5 Bestellungen" – mit Zuordnungstabelle ist U-4711 = Max Mueller.

## Loesung 6

| Kriterium | IT-Sicherheitsbeauftragter | Datenschutzbeauftragter |
|---|---|---|
| Gesetzliche Pflicht? | Nein (empfohlen) | Ja (ab 20 MA mit personenbez. Daten) |
| Weisungsfrei? | Nein | Ja (Art. 38 DSGVO) |
| Fokus? | Technische IT-Sicherheit | Schutz personenbezogener Daten |

## Loesung 7
1. **Gesetzliche Aufbewahrungspflichten:** Z.B. steuerrechtliche Aufbewahrung von Rechnungsdaten (10 Jahre HGB/AO)
2. **Geltendmachung von Rechtsanspruechen:** Die Daten werden zur Verteidigung gegen rechtliche Ansprueche benoetigt (z.B. laufender Rechtsstreit)
Weitere moeglich: Vertragserfuellung, oeffentliches Interesse
