# 4.5.02 – Informationstechnische Schutzziele bei der Kommunikation: Beispiele

## Beispiel 1: Spear-Phishing-Angriff auf ein Entwicklerteam

### Szenario

Die Firma **TechSoft GmbH** entwickelt eine Banking-App. Ein Angreifer hat ueber LinkedIn herausgefunden, dass Entwickler Max Mueller im Frontend-Team arbeitet und regelmaessig Confluence nutzt.

### Angriffsablauf

| Schritt | Handlung des Angreifers |
|---------|------------------------|
| 1 | Recherche: LinkedIn-Profil von Max, Unternehmenswebsite, GitHub-Account |
| 2 | Erstellt E-Mail-Adresse: it-admin@techseft.de (Tippfehler: "e" statt "o") |
| 3 | Sendet E-Mail: "Confluence-Wartung – bitte Passwort zuruecksetzen" |
| 4 | Link fuehrt auf gefaelschte Confluence-Login-Seite |
| 5 | Max gibt Zugangsdaten ein → Angreifer erhaelt Zugriff |
| 6 | Angreifer nutzt Confluence-Zugang fuer laterale Bewegung (Jira, Git) |

### Analyse: Erkennungsmerkmale

| Merkmal | Auffaelligkeit in diesem Fall |
|---------|------------------------------|
| Absender | techseft.de statt techsoft.de – Buchstabendreher |
| Dringlichkeit | "Bitte innerhalb von 2 Stunden zuruecksetzen" |
| Link | URL zeigt auf externe Domain (nicht techsoft.de) |
| Anrede | "Lieber Mitarbeiter" statt persoenliche Anrede |
| Signatur | Keine Standard-Firmensignatur |

### Richtige Reaktion

1. E-Mail NICHT anklicken
2. Absenderadresse genau pruefen
3. IT-Sicherheitsabteilung informieren
4. E-Mail als Phishing melden (Phishing-Button im Mail-Client)
5. NICHT weiterleiten (erhoet Verbreitung)

---

## Beispiel 2: Social-Media-Vorfall mit arbeitsrechtlichen Konsequenzen

### Szenario

Entwicklerin Lisa Schneider ist frustriert nach einem gescheiterten Projekt bei der **DataFlow AG**. Sie postet auf Twitter/X:

> "Absoluter Saftladen hier! Die Chefs haben keine Ahnung von IT. Kein Wunder, dass das Projekt gescheitert ist. #DataFlowAG #WorstJobEver"

### Juristische Analyse

| Aspekt | Bewertung |
|--------|-----------|
| Meinungsfreiheit (Art. 5 GG) | Grundsaetzlich geschuetzt, aber nicht grenzenlos |
| Loyalitaetspflicht (§ 241 II BGB) | Verletzt – oeffentliche Herabwuerdigung des Arbeitgebers |
| Schmaehurkritik | "Saftladen", "keine Ahnung" – grenzwertig bis ja |
| Geschaeftsgeheimnisse | "Projekt gescheitert" – moeglicher Verstoss gegen GeschGehG |
| Hashtag mit Firmenname | Erhoet Auffindbarkeit, vergroessert Schaden |
| Reichweite | Oeffentlich sichtbar, potenziell grosse Verbreitung |

### Moegliche Konsequenzen

| Konsequenz | Wahrscheinlichkeit | Begruendung |
|------------|--------------------:|-------------|
| Abmahnung | Hoch | Erster Verstoss, proportionale Reaktion |
| Ordentliche Kuendigung | Mittel | Bei Wiederholung oder schwerem Reputationsschaden |
| Ausserordentliche Kuendigung | Gering | Nur bei besonders schwerwiegendem Fall |
| Schadensersatz | Moeglich | Wenn bezifferbarer Reputationsschaden entsteht |

### Richtige Alternative

Lisa haette:
- Intern ueber offizielle Kanaele Kritik aeussern koennen (Retrospektive, Betriebsrat)
- Auf anonymen Plattformen (Kununu) sachlich bewerten koennen
- Ein persoenliches Gespraech mit dem Vorgesetzten suchen koennen

---

## Beispiel 3: BCC-Fehler mit DSGVO-Verstoss

### Szenario

Der IT-Dienstleister **NetService GmbH** versendet eine Einladung zum Kunden-Webinar an 150 Geschaeftskunden. Der Mitarbeiter traegt alle E-Mail-Adressen in das **CC-Feld** statt in das **BCC-Feld** ein.

### Analyse

| Aspekt | Bewertung |
|--------|-----------|
| Datenschutz-Verstoss | Ja – E-Mail-Adressen sind personenbezogene Daten (Art. 4 Nr. 1 DSGVO) |
| Betroffene | 150 Geschaeftskunden, deren E-Mail-Adressen offengelegt wurden |
| Art des Verstosses | Unbefugte Offenlegung personenbezogener Daten (Art. 5 Abs. 1 lit. f DSGVO) |
| Meldepflicht | Moeglicherweise – Risikobewertung erforderlich (Art. 33 DSGVO: 72h-Frist) |

### Konsequenzen

| Konsequenz | Details |
|------------|---------|
| Meldung an Datenschutzbehoerde | Innerhalb von 72 Stunden, wenn Risiko fuer Betroffene |
| Information der Betroffenen | Art. 34 DSGVO – bei hohem Risiko |
| Bussgeld | Bis zu 20 Mio. EUR oder 4% des Jahresumsatzes (Art. 83 DSGVO) |
| Reputationsschaden | Vertrauensverlust bei Kunden |
| Interne Massnahmen | Schulung, Prozessaenderung, technische Loesung |

### Praeventionsmassnahmen

| Massnahme | Beschreibung |
|-----------|-------------|
| Newsletter-Tool verwenden | Professionelle Tools (Mailchimp, etc.) verhindern diesen Fehler |
| Verteiler vorher pruefen | Vier-Augen-Prinzip bei Massen-E-Mails |
| BCC als Standard | Outlook-Regel: Bei >5 externen Empfaengern warnen |
| Schulung | Regelmaessige Datenschutzschulung fuer alle Mitarbeitenden |
| Technische Sperre | E-Mail-Gateway kann bei vielen CC-Empfaengern warnen |

---

## Beispiel 4: Security-Awareness-Kampagne in einem Unternehmen

### Szenario

Die **CloudIT AG** (300 Mitarbeiter) hatte im letzten Jahr 3 erfolgreiche Phishing-Angriffe. Die IT-Leitung beschliesst ein Security-Awareness-Programm.

### Umsetzungsplan

| Phase | Zeitraum | Massnahme | Ziel |
|-------|----------|-----------|------|
| 1 | Monat 1 | Basis-Phishing-Test (ohne Vorwarnung) | Ausgangswert ermitteln (Klickrate) |
| 2 | Monat 2 | E-Learning-Kurs "IT-Sicherheit Grundlagen" | Wissensvermittlung |
| 3 | Monat 3 | Praesenzschulung "Social Engineering erkennen" | Praktische Uebungen |
| 4 | Monat 4 | Zweiter Phishing-Test | Verbesserung messen |
| 5 | Monat 5-6 | Poster-Kampagne, Intranet-Artikel | Verstaerkung |
| 6 | Monat 7 | Dritter Phishing-Test + Quiz | Langzeitwirkung pruefen |
| 7 | Monat 12 | Jaehrliche Auffrischung | Nachhaltigkeit sichern |

### Ergebnisse (typisch)

| Kennzahl | Vor Kampagne | Nach Kampagne |
|----------|-------------|---------------|
| Phishing-Klickrate | 35% | 8% |
| Meldequote (IT gemeldet) | 5% | 45% |
| Schulungsteilnahme | n/a | 92% |
| Sicherheitsvorfaelle/Quartal | 3 | 0 |
