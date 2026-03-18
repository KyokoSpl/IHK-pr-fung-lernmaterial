# 4.5.02 – Informationstechnische Schutzziele bei der Kommunikation: Uebungen

## Aufgabe 1: Phishing-Mail erkennen

Du erhaeltst folgende E-Mail:

```
Von: support@amaz0n-sicherheit.com
Betreff: DRINGEND: Ihr Konto wird gesperrt!
Datum: 15.03.2026

Sehr geehrter Kunde,

wir haben ungewoehnliche Aktivitaeten in Ihrem Konto festgestellt.
Um eine Sperrung zu vermeiden, bestaetigen Sie bitte Ihre Identitaet
innerhalb der naechsten 24 Stunden.

Klicken Sie hier: https://amaz0n-sicherheit.com/verify?id=83721

Mit freundlichen Gruessen
Amazon Sicherheitsteam
```

a) Nenne mindestens 5 Merkmale, die auf Phishing hindeuten.
b) Um welche Social-Engineering-Methode handelt es sich?
c) Wie solltest du reagieren?
d) Welches Schutzziel der IT-Sicherheit wird hier angegriffen?

---
---

**Loesung Aufgabe 1:**

a) **Phishing-Merkmale:**

| Nr | Merkmal | Erklaerung |
|----|---------|------------|
| 1 | Absender-Domain | "amaz0n-sicherheit.com" – Null statt "o", keine offizielle Amazon-Domain |
| 2 | Dringlichkeit | "DRINGEND", "innerhalb von 24 Stunden" – Zeitdruck erzeugen |
| 3 | Generische Anrede | "Sehr geehrter Kunde" statt persoenlicher Name |
| 4 | Verdaechtiger Link | Domain stimmt nicht mit amazon.de ueberein |
| 5 | Drohung | "Konto wird gesperrt" – Angst erzeugen |
| 6 | Unuebliche Absender-Adresse | Serioeser Support kaeme von @amazon.de |

b) **Methode:** Phishing (Massen-Phishing, nicht Spear-Phishing, da generisch adressiert)

c) **Richtige Reaktion:**
1. Link NICHT anklicken
2. E-Mail als Phishing/Spam markieren
3. Bei Unsicherheit: Amazon-Website DIREKT im Browser aufrufen (nicht ueber Link)
4. Im geschaeftlichen Kontext: IT-Sicherheitsabteilung melden
5. E-Mail loeschen

d) **Angegriffene Schutzziele:**
- **Vertraulichkeit** (Zugangsdaten abgreifen)
- **Authentizitaet** (Identitaetstaeuchung des Absenders)

---

## Aufgabe 2: E-Mail-Kommunikation – BCC, CC, TO

Entscheide fuer die folgenden Szenarien, welches Adressfeld (TO, CC, BCC) jeweils korrekt ist. Begruende deine Entscheidung.

a) Du schreibst eine Projektstatusmail an deinen Teamleiter. Dein Scrum Master soll informiert sein.
b) Du versendest eine Einladung zu einem IT-Workshop an 80 externe Kunden.
c) Du antwortest auf eine Supportanfrage eines Kunden und informierst gleichzeitig den zustaendigen Entwickler.
d) Du leitest eine interne Richtlinie an alle 12 Teammitglieder weiter.
e) Du meldest einen Sicherheitsvorfall an den CISO und den Datenschutzbeauftragten.

---
---

**Loesung Aufgabe 2:**

| Szenario | TO | CC | BCC | Begruendung |
|----------|----|----|-----|-------------|
| a) Statusmail | Teamleiter | Scrum Master | – | Teamleiter = Hauptempfaenger, SM zur Info |
| b) Workshop-Einladung | – | – | 80 Kunden | DSGVO: E-Mail-Adressen der Kunden schuetzen |
| c) Supportantwort | Kunde | Entwickler | – | Kunde = Hauptempfaenger, Entwickler zur Info |
| d) Interne Richtlinie | Alle 12 Teammitglieder | – | – | Intern, alle sollen sehen wer informiert ist |
| e) Sicherheitsvorfall | CISO + DSB | – | – | Beide muessen handeln, beide Hauptempfaenger |

**Wichtig bei b):** Alternativ sollte ein professionelles Newsletter-Tool verwendet werden. Bei CC waeren alle 80 Kundenmailadressen fuer alle sichtbar → DSGVO-Verstoss (unbefugte Offenlegung personenbezogener Daten).

---

## Aufgabe 3: Social-Engineering-Szenarien zuordnen

Ordne die folgenden Szenarien der passenden Social-Engineering-Methode zu:

a) Ein "Techniker" steht vor der Tuer und sagt, er muss den Server warten. Er hat keinen Ausweis.
b) Du findest einen USB-Stick mit der Aufschrift "Gehaelter_2026.xlsx" auf dem Parkplatz.
c) Du erhaeltst einen Anruf: "Hier ist die IT-Abteilung. Wir haben ein Sicherheitsproblem. Bitte nennen Sie mir Ihr Passwort zur Verifizierung."
d) Eine E-Mail an den CEO: "Lieber Herr Mueller, anbei die Quartalsabrechnung von Ihrem Steuerberater Dr. Fischer."
e) Jemand mit einem grossen Karton bittet dich, ihm die gesicherte Tuer aufzuhalten.
f) Eine unbekannte Firma bietet dir einen "kostenlosen Sicherheitscheck" deines Laptops an.

---
---

**Loesung Aufgabe 3:**

| Szenario | Methode | Begruendung |
|----------|---------|-------------|
| a) Falscher Techniker | **Pretexting** | Erfundene Identitaet und Geschichte |
| b) USB-Stick auf Parkplatz | **Baiting** | Koeder mit verlockendem Inhalt |
| c) Anruf IT-Abteilung | **Vishing** | Voice-Phishing per Telefon |
| d) E-Mail an CEO | **Whaling** | Gezieltes Phishing auf Fuehrungskraft |
| e) Tuer aufhalten | **Tailgating** | Unbefugtes Mitgehen durch gesicherte Tuer |
| f) Kostenloser Sicherheitscheck | **Quid pro Quo** | Gegenleistung (Service) gegen Zugang |

---

## Aufgabe 4: Nachricht aus Empfaengersicht (Vier-Seiten-Modell)

Analysiere folgende Nachricht eines Teamleiters an einen Entwickler nach dem Vier-Seiten-Modell von Schulz von Thun:

**Situation:** Freitag, 17:30 Uhr. Der Entwickler wollte gerade gehen.

**Nachricht:** _"Der Hotfix ist immer noch nicht deployed."_

Analysiere die Nachricht auf allen vier Ebenen – jeweils aus Sicht des Senders und des Empfaengers.

---
---

**Loesung Aufgabe 4:**

| Seite | Sender-Perspektive (Teamleiter) | Empfaenger-Perspektive (Entwickler) |
|-------|--------------------------------|-------------------------------------|
| **Sachinhalt** | Der Hotfix wurde noch nicht in Produktion gebracht | "Ich weiss, der Hotfix ist nicht deployed" |
| **Selbstoffenbarung** | "Ich bin besorgt/unter Druck (z.B. vom Kunden)" | "Er ist sauer / ungeduldig" |
| **Beziehung** | "Du bist dafuer verantwortlich" | "Er haelt mich fuer unzuverlaessig / kontrolliert mich" |
| **Appell** | "Bitte deploy den Hotfix jetzt noch" | "Ich soll Ueberstunden machen / jetzt noch arbeiten" |

**Analyse:** Die gleiche Nachricht kann voellig unterschiedlich interpretiert werden. Der Teamleiter meint vielleicht nur eine sachliche Feststellung, der Entwickler hoert einen Vorwurf. Besser waere eine konkrete, empfaengersensible Formulierung:

_"Mir ist aufgefallen, dass der Hotfix noch nicht deployed ist. Ist etwas dazwischengekommen? Wir koennen das am Montag als Erstes angehen, falls es nicht kritisch ist."_

---

## Aufgabe 5: Loyalitaetspflicht und Social Media

Bewerte die folgenden Aeusserungen eines Arbeitnehmers in sozialen Netzwerken hinsichtlich der arbeitsrechtlichen Zulaessigkeit:

a) Kununu-Bewertung: "Das Gehalt ist unterdurchschnittlich, die Karrierechancen begrenzt." (3/5 Sterne)
b) Twitter/X: "Unser neues Produkt ist Schrott. Kauft es nicht! @FirmaXYZ"
c) Instagram-Story vom Firmenfest mit Kollegen (ohne deren Einwilligung)
d) LinkedIn-Post: "Spannender Tag heute – grosses Kundenprojekt gewonnen! #ProudOfMyTeam @FirmaXYZ"
e) WhatsApp-Gruppe (5 Freunde): "Mein Chef ist echt der Letzte, totaler Kontrollfreak."

---
---

**Loesung Aufgabe 5:**

| Aeusserung | Zulaessig? | Begruendung |
|------------|-----------|-------------|
| a) Sachliche Kununu-Bewertung | **Ja** | Sachlich, Meinungsfreiheit, keine Schmaehurkritik |
| b) Produkt oeffnetlich diskreditieren | **Nein** | Loyalitaetspflicht verletzt, Geschaeftsschaedigung, Abmahnung/Kuendigung moeglich |
| c) Fotos ohne Einwilligung | **Nein** | Recht am eigenen Bild (KunstUrhG), ggf. DSGVO-Verstoss |
| d) Positiver LinkedIn-Post | **Ja, aber Vorsicht** | Grundsaetzlich ok, aber: Ist das Projekt vertraulich? "Kundenprojekt gewonnen" koennte Geschaeftsgeheimnis sein |
| e) WhatsApp ueber Chef | **Grauzone** | Kleine, private Gruppe – Art. 5 GG schuetzt Meinungsfreiheit im privaten Raum. Aber: Screenshots koennen verbreitet werden |

**Merke:** Auch im vermeintlich privaten Raum ist Vorsicht geboten. Was digital geteilt wird, kann unkontrolliert weiterverbreitet werden.
