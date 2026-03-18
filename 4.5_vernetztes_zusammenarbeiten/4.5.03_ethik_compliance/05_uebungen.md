# 4.5.03 – Ethische Aspekte und Compliance-Regelungen: Uebungen

## Aufgabe 1: Compliance-Management-System

Die **ByteForce GmbH** (250 Mitarbeiter) hatte im letzten Jahr einen Datenschutzvorfall: Ein Mitarbeiter hat Kundendaten auf einem privaten USB-Stick gespeichert und verloren. Bisher gibt es kein formales Compliance-Management-System.

a) Nenne die 7 Elemente eines Compliance-Management-Systems.
b) Beschreibe fuer jedes Element eine konkrete Massnahme, die die ByteForce GmbH umsetzen sollte.
c) Welche gesetzliche Pflicht hat die ByteForce GmbH bezueglich eines Hinweisgebersystems? Begruende mit dem HinSchG.
d) Welche Konsequenzen drohen bei einem erneuten DSGVO-Verstoss?

---
---

**Loesung Aufgabe 1:**

a) + b) **CMS-Elemente mit konkreten Massnahmen:**

| Element | Konkrete Massnahme fuer ByteForce GmbH |
|---------|----------------------------------------|
| 1. Compliance-Kultur | Geschaeftsfuehrung kommuniziert Null-Toleranz bei Datenschutzverstoessen, lebt Datenschutz vor |
| 2. Compliance-Ziele | Ziel: Null Datenschutzvorfaelle, DSGVO-Konformitaet bis Q2 |
| 3. Compliance-Risiken | Risikobewertung: USB-Nutzung, Cloud-Speicher, E-Mail, mobile Geraete |
| 4. Compliance-Programm | Richtlinie: Keine privaten Speichermedien, USB-Ports sperren, Verschluesselungspflicht |
| 5. Compliance-Organisation | Datenschutzbeauftragten benennen, Compliance-Officer einstellen |
| 6. Compliance-Kommunikation | Pflichtschulung Datenschutz fuer alle Mitarbeitenden, Intranet-Bereich |
| 7. Compliance-Monitoring | Quartalsweise Audits, Phishing-Tests, Kennzahl: Anzahl Vorfaelle |

c) **Hinweisgebersystem:**
- ByteForce GmbH hat 250 Mitarbeitende → ueber der Schwelle von 50 (HinSchG)
- **Pflicht:** Einrichtung einer internen Meldestelle
- **Anforderungen:** Vertraulichkeit, Eingangsbestaetigung in 7 Tagen, Rueckmeldung in 3 Monaten
- **Sanktion bei Verstoss:** Bis zu 50.000 EUR Bussgeld

d) **Konsequenzen bei erneutem DSGVO-Verstoss:**
- Bussgeld bis zu 20 Mio. EUR oder 4% des weltweiten Jahresumsatzes (Art. 83 DSGVO)
- Meldepflicht an Datenschutzbehoerde innerhalb 72 Stunden (Art. 33 DSGVO)
- Information der Betroffenen bei hohem Risiko (Art. 34 DSGVO)
- Schadensersatzansprueche der Betroffenen (Art. 82 DSGVO)
- Reputationsschaden, Vertrauensverlust bei Kunden

---

## Aufgabe 2: Gender-Neutralitaet in IT-Systemen

Du entwickelst ein Registrierungsformular fuer eine Web-Anwendung.

a) Welche Optionen sollte das Feld "Geschlecht" mindestens bieten? Begruende rechtlich.
b) Entwirf ein Datenbankschema (als Tabelle) fuer eine Benutzertabelle, das Gender-Neutralitaet beruecksichtigt.
c) Formuliere eine gender-neutrale E-Mail-Begruessung fuer einen automatisierten Newsletter.
d) Nenne 3 weitere Stellen in einer typischen Web-Anwendung, an denen Gender-Neutralitaet beruecksichtigt werden sollte.

---
---

**Loesung Aufgabe 2:**

a) **Mindest-Optionen fuer Geschlecht:**

| Option | Begruendung |
|--------|-------------|
| Maennlich | Standard-Personenstand |
| Weiblich | Standard-Personenstand |
| Divers | Drittes Geschlecht seit 2018 (§ 22 Abs. 3 PStG) |
| Keine Angabe | Recht, keine Angabe zu machen (PStG + DSGVO Datenminimierung) |

**Zusaetzlich empfohlen:** Freies Textfeld oder "Moechte ich nicht angeben"

b) **Datenbankschema:**

| Spalte | Datentyp | Constraint | Bemerkung |
|--------|----------|-----------|-----------|
| user_id | INT | PRIMARY KEY, AUTO_INCREMENT | Eindeutige ID |
| vorname | VARCHAR(100) | NOT NULL | Vorname |
| nachname | VARCHAR(100) | NOT NULL | Nachname |
| gender | VARCHAR(50) | DEFAULT NULL | Freitext oder ENUM('maennlich','weiblich','divers','keine_angabe') |
| pronomen | VARCHAR(50) | DEFAULT NULL | Optional: er/sie/they etc. |
| anrede | VARCHAR(50) | DEFAULT NULL | Optional: Herr/Frau/leer |
| email | VARCHAR(255) | NOT NULL, UNIQUE | E-Mail-Adresse |

**Wichtig:** Gender als VARCHAR statt ENUM ermoeglicht spaetere Erweiterungen ohne Schema-Aenderung. Alternativ: Lookup-Tabelle fuer Gender-Optionen.

c) **Gender-neutrale E-Mail-Begruessung:**

```
STATT:     "Sehr geehrte Frau Mueller" / "Sehr geehrter Herr Mueller"
BESSER:    "Guten Tag Alex Mueller"
ODER:      "Hallo Alex Mueller"
FORMELL:   "Sehr geehrte*r Alex Mueller"
NOCH BESSER: Anrede basierend auf Nutzer-Praeferenz (im Profil einstellbar)
```

d) **Weitere Stellen fuer Gender-Neutralitaet:**

| Stelle | Umsetzung |
|--------|-----------|
| Profil-Seite | Pronomen-Feld anbieten (er/sie/they), Gender als optionales Feld |
| Suchfilter | Wenn nach Geschlecht gefiltert wird: alle Optionen anbieten oder Filter weglassen |
| Automatisierte Texte | "Ihr Paket wurde versendet" statt "Lieber Kunde, Ihr Paket..." |

---

## Aufgabe 3: Barrierefreiheit pruefen

Pruefe die folgende HTML-Struktur auf Barrierefreiheits-Probleme. Benenne fuer jedes Problem das verletzte WCAG-Prinzip und die Konformitaetsstufe.

```html
<html>
<body style="background: #fff; color: #ccc;">
  <div onclick="navigate('/home')">Startseite</div>
  <img src="organigramm.png">
  <video src="tutorial.mp4" autoplay></video>
  <form>
    <input type="text" placeholder="Name">
    <input type="email" placeholder="E-Mail">
    <div style="color: red; font-size: 10px;">Pflichtfeld</div>
    <button>Absenden</button>
  </form>
  <marquee>Neue Funktionen verfuegbar!</marquee>
</body>
</html>
```

---
---

**Loesung Aufgabe 3:**

| Problem | WCAG-Kriterium | Prinzip | Stufe | Loesung |
|---------|---------------|---------|-------|---------|
| Geringer Kontrast (#ccc auf #fff = 1.6:1) | 1.4.3 Kontrast (Minimum) | Wahrnehmbar | AA | Mindestens 4.5:1 → z.B. #595959 auf #fff |
| div statt a/button fuer Navigation | 2.1.1 Tastatur | Bedienbar | A | `<a href="/home">` oder `<button>` verwenden |
| Bild ohne alt-Attribut | 1.1.1 Nicht-Text-Inhalt | Wahrnehmbar | A | `<img src="organigramm.png" alt="Organigramm der Abteilung">` |
| Video ohne Untertitel | 1.2.2 Untertitel | Wahrnehmbar | A | `<track kind="captions" src="tutorial.vtt">` hinzufuegen |
| Video autoplay | 2.2.2 Pausieren, Stoppen | Bedienbar | A | Autoplay entfernen, Steuerung anbieten |
| Input ohne Label | 1.3.1 Info und Beziehungen | Wahrnehmbar | A | `<label for="name">Name</label><input id="name">` |
| Placeholder als einziges Label | 3.3.2 Beschriftungen | Verstaendlich | A | Sichtbares Label zusaetzlich zum Placeholder |
| Fehlerhinweis nur farblich (rot) | 1.4.1 Verwendung von Farbe | Wahrnehmbar | A | Zusaetzlich Symbol oder Text: "⚠ Pflichtfeld" |
| Schriftgroesse 10px | 1.4.4 Textgroesse aendern | Wahrnehmbar | AA | Mindestens 16px oder relative Einheiten (rem) |
| marquee-Element | 2.2.2 Pausieren, Stoppen | Bedienbar | A | Entfernen, statischen Text oder pausierbare Animation verwenden |
| Fehlende Dokumentensprache | 3.1.1 Sprache der Seite | Verstaendlich | A | `<html lang="de">` |

---

## Aufgabe 4: Nachhaltige IT-Entscheidung

Dein Unternehmen plant die Migration eines lokalen Servers in die Cloud. Bewerte die Nachhaltigkeit der Entscheidung anhand der drei Saeulen.

a) Erstelle eine Tabelle mit Vor- und Nachteilen fuer jede Saeuele (oekologisch, oekonomisch, sozial).
b) Welche Fragen sollte man dem Cloud-Anbieter stellen, um die Nachhaltigkeit zu bewerten?
c) Nenne 3 Massnahmen, um die Cloud-Nutzung nachhaltiger zu gestalten.

---
---

**Loesung Aufgabe 4:**

a) **Nachhaltigkeitsbewertung Cloud-Migration:**

| Saeuele | Vorteile | Nachteile |
|---------|----------|-----------|
| **Oekologisch** | Bessere Auslastung (weniger Leerlauf), effizientere Kuehlung im RZ, ggf. Oekostrom | Rebound-Effekt (mehr Nutzung), Datentransfer verbraucht Energie, Abhaengigkeit vom Anbieter |
| **Oekonomisch** | Keine eigene Hardware-Wartung, skalierbar, Pay-per-Use | Langfristig ggf. teurer, Vendor Lock-in, laufende Kosten |
| **Sozial** | Flexibles Arbeiten moeglich, weltweiter Zugriff | Datenschutz-Bedenken (Serverstandort), Abhaengigkeit, Arbeitsplatzverlust im RZ-Betrieb |

b) **Fragen an den Cloud-Anbieter:**

| Nr | Frage | Warum relevant? |
|----|-------|-----------------|
| 1 | Welchen Anteil erneuerbarer Energien nutzt das Rechenzentrum? | CO2-Fussabdruck |
| 2 | Wo stehen die Server? (EU / DSGVO-konform?) | Datenschutz, rechtliche Anforderungen |
| 3 | Gibt es einen Nachhaltigkeitsbericht / Zertifizierungen? | Transparenz (ISO 14001, ISO 50001) |
| 4 | Wie wird die Abwaerme genutzt? | Energieeffizienz |
| 5 | Welche PUE (Power Usage Effectiveness) hat das RZ? | Je naeher an 1.0, desto effizienter |
| 6 | Wie werden alte Hardware-Komponenten entsorgt? | Elektroschrott, Kreislaufwirtschaft |

c) **Massnahmen fuer nachhaltigere Cloud-Nutzung:**

| Nr | Massnahme | Wirkung |
|----|-----------|---------|
| 1 | Right-Sizing: Nur benoetigte Ressourcen buchen | Weniger verschwendete Rechenleistung und Energie |
| 2 | Auto-Scaling und Abschalten ungenutzter Instanzen | Vermeidung von Leerlauf |
| 3 | Cloud-Region mit hohem Oekostrom-Anteil waehlen | Geringerer CO2-Fussabdruck |

---

## Aufgabe 5: Ethische Bewertung einer IT-Loesung

Ein Supermarkt moechte ein KI-System einsetzen, das per Kameraerkennung das Alter der Kunden schaetzt, um:
- Alkohol- und Tabakverkauf an Minderjahrige zu verhindern
- Personalisierte Werbung auf Displays auszuspielen (altersabhaengig)
- Diebstahl durch auffaelliges Verhalten zu erkennen

a) Bewerte jeden Einsatzzweck anhand ethischer Prinzipien (Fairness, Transparenz, Privatsphaere, Nicht-Schaedigung).
b) Welche rechtlichen Regelungen sind zu beachten? (Nenne mindestens 4)
c) Formuliere Bedingungen, unter denen der Einsatz ethisch vertretbar waere.

---
---

**Loesung Aufgabe 5:**

a) **Ethische Bewertung:**

| Einsatzzweck | Fairness | Transparenz | Privatsphaere | Nicht-Schaedigung | Gesamtbewertung |
|-------------|----------|-------------|---------------|-------------------|-----------------|
| Altersverifikation Alkohol/Tabak | Mittel (Bias bei Altersschaetzung) | Hoch moeglich (Hinweis am Eingang) | Mittel (Gesichtserkennung) | Positiv (Jugendschutz) | **Bedingt vertretbar** |
| Personalisierte Werbung | Gering (Manipulation) | Gering (Kunden wissen nichts davon) | Gering (Profiling ohne Einwilligung) | Negativ (Manipulation) | **Ethisch bedenklich** |
| Diebstahlerkennung | Gering (Bias: "auffaelliges Verhalten" diskriminiert) | Gering (Generalverdacht) | Sehr gering (Massenueberwachung) | Negativ (Fehlalarme, Diskriminierung) | **Ethisch nicht vertretbar** |

b) **Rechtliche Regelungen:**

| Nr | Regelung | Relevanz |
|----|----------|----------|
| 1 | DSGVO (Art. 6, 9) | Rechtsgrundlage fuer Verarbeitung biometrischer Daten (besondere Kategorie!) |
| 2 | DSGVO Art. 22 | Automatisierte Einzelentscheidungen – Recht auf menschliche Ueberpruefung |
| 3 | EU AI Act | Biometrische Identifikation in oeffentlich zugaenglichen Raeumen = Hochrisiko/verboten |
| 4 | BDSG | Nationale Datenschutzregelungen, Videoueberwachung oeffentlicher Raeume |
| 5 | AGG | Diskriminierungsverbot – Diebstahlerkennung darf nicht nach Aussehen filtern |
| 6 | JuSchG | Jugendschutzgesetz – Pflicht zur Alterskontrolle bei Alkohol/Tabak |

c) **Bedingungen fuer ethisch vertretbaren Einsatz:**

| Bedingung | Umsetzung |
|-----------|-----------|
| Beschraenkung auf Altersverifikation | Nur fuer Jugendschutz, NICHT fuer Werbung oder Diebstahl |
| Transparenz | Klare Beschilderung: "Hier wird Altersschaetzung per KI eingesetzt" |
| Keine Speicherung | Bilder werden sofort nach Analyse geloescht, kein Profiling |
| Opt-out | Alternative: Ausweis vorzeigen statt KI-Schaetzung |
| Regelmaessige Bias-Ueberpruefung | Altersschaetzung auf Fairness ueber Hautfarbe/Geschlecht testen |
| Datenschutz-Folgenabschaetzung (DSFA) | Pflicht gemaess Art. 35 DSGVO bei biometrischen Daten |
| Menschliche Kontrolle | Endentscheidung bei Ablehnung immer durch Personal |
