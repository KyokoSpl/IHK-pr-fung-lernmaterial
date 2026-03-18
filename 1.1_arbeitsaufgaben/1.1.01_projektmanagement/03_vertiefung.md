# Vertiefung: 1.1.01 – Merkmale und Methoden des Projektmanagements

## Merkmale eines Projektes – Vertiefung

### Abgrenzung Projekt vs. Routineaufgabe

| Kriterium | Projekt | Routineaufgabe |
|-----------|---------|----------------|
| Einmaligkeit | Ja | Nein (wiederkehrend) |
| Zeitrahmen | Befristet | Unbefristet |
| Komplexitaet | Hoch | Gering bis mittel |
| Organisation | Eigenes Projektteam | Linienorganisation |
| Ziel | Spezifisches Ergebnis | Laufender Betrieb |

### Typische Pruefungsaspekte
- Zuordnung: Ist eine beschriebene Aufgabe ein Projekt oder nicht?
- Begruendung anhand der Merkmale
- Benennung fehlender Projektmerkmale in einem Szenario

### Haeufige Fehler
- Verwechslung von Projekt und Prozess: Ein Prozess ist wiederholbar, ein Projekt nicht
- Fehlende Zielbeschreibung wird uebersehen – ohne klares Ziel kein Projekt

---

## Phasen der Teambildung – Vertiefung

### Zusammenhang mit Projektphasen
Die Teambildungsphasen verlaufen parallel zu den Projektphasen. In der Anfangsphase eines Projekts befindet sich das Team haeufig im Forming/Storming. Produktive Arbeit (Performing) wird erst spaeter erreicht.

### Typische Pruefungsaspekte
- Beschreibung einer Teamsituation – Zuordnung zur korrekten Phase
- Massnahmen, die der Projektleiter in einer bestimmten Phase ergreifen sollte
- Beispiel: Team streitet ueber Zustaendigkeiten → Storming → Projektleiter moderiert, klaert Rollen

### Haeufige Fehler
- Annahme, dass Performing sofort eintritt
- Storming wird als negativ bewertet – tatsaechlich ist es ein notwendiger Entwicklungsschritt

---

## Wasserfallmodell vs. SCRUM – Vertiefung

### Detaillierter Vergleich

| Aspekt | Wasserfallmodell | SCRUM |
|--------|-----------------|-------|
| Ablauf | Sequenziell | Iterativ (Sprints) |
| Flexibilitaet | Gering | Hoch |
| Kundenkontakt | Zu Beginn und Ende | Kontinuierlich (Sprint Review) |
| Dokumentation | Umfangreich | Schlank |
| Fehlererkennung | Spaet (Testphase) | Frueh (nach jedem Sprint) |
| Eignung | Klare, stabile Anforderungen | Sich aendernde Anforderungen |

### Zusammenhang zu anderen Themen
- **Lasten-/Pflichtenheft** (Thema 1.4.01): Im Waserfallmodell werden Anforderungen zu Beginn komplett erfasst. In SCRUM werden sie im Product Backlog laufend angepasst.
- **Vorgehensmodelle** (Thema 3.4.02): Weitere Modelle wie V-Modell und Spiralmodell ergaenzen die Auswahl.
- **Qualitaetsmanagement** (Thema 1.5.02): PDCA-Zyklus spiegelt sich in den Sprints wider.

### Typische Pruefungsaspekte
- Szenario lesen und passendes Vorgehensmodell empfehlen mit Begruendung
- Rollen in SCRUM benennen und deren Aufgaben beschreiben
- Vor- und Nachteile beider Modelle gegenueberstellen

### Haeufige Fehler
- SCRUM wird als "planlos" missverstanden – es ist hoch strukturiert, aber flexibel
- Verwechslung der Rollen: Product Owner (bestimmt WAS) vs. Scrum Master (sichert Prozess)

---

## Projektplanung – Vertiefung

### Netzplan: Berechnung im Detail

**Vorwaertsrechnung (frueheste Termine):**
1. FA des ersten Vorgangs = 0
2. FE = FA + Dauer
3. FA des Nachfolgers = groesster FE aller Vorgaenger

**Rueckwaertsrechnung (spaeteste Termine):**
1. SE des letzten Vorgangs = FE des letzten Vorgangs
2. SA = SE - Dauer
3. SE des Vorgaengers = kleinster SA aller Nachfolger

**Pufferzeit:**
- Gesamtpuffer (GP) = SA - FA = SE - FE
- Freier Puffer (FP) = FA(Nachfolger) - FE(Vorgang)
- Kritischer Weg: Alle Vorgaenge mit GP = 0

### Zusammenhang zu anderen Themen
- **Meilensteine** ergaenzen den Netzplan durch Kontrollpunkte
- **SMART-Prinzip** wird bei der Formulierung von Projektzielen und Arbeitspaketen angewendet
- **Gantt-Diagramm** kann aus dem Netzplan abgeleitet werden

### Loesungsmoeglichkeiten bei Terminproblemen
- Parallelisierung von Arbeitspaketen (sofern keine Abhaengigkeit)
- Ressourcenaufstockung (Crashing)
- Reduzierung des Leistungsumfangs
- Verschiebung nicht-kritischer Vorgaenge innerhalb des Puffers

### Typische Pruefungsaspekte
- Netzplan zeichnen oder vervollstaendigen
- Kritischen Weg bestimmen
- Pufferzeiten berechnen
- Massnahmen bei Terminueberschreitung vorschlagen

### Haeufige Fehler
- Verwechslung von Gesamt- und freiem Puffer
- Fehler bei der Rueckwaertsrechnung (kleinster SA, nicht groesster)
- Vergessen, dass der kritische Weg die Mindestdauer bestimmt, nicht die maximale

---

## Reflektionsmethoden – Vertiefung

### Lessons Learned im Projektkontext

**Ablauf:**
1. Daten sammeln: Was war geplant? Was ist eingetreten?
2. Analyse: Warum gab es Abweichungen?
3. Dokumentation: Erkenntnisse festhalten
4. Transfer: Ergebnisse fuer zukuenftige Projekte verfuegbar machen

### Zusammenhang zu anderen Themen
- **PDCA-Zyklus** (Thema 1.5.02): Lessons Learned entspricht der "Check"- und "Act"-Phase
- **Soll-Ist-Vergleich** (Thema 1.7.07): Grundlage fuer die Analyse in Lessons Learned
- **Nachkalkulation** (Thema 1.7.07): Wirtschaftliche Bewertung ergaenzt die qualitative Reflexion
- **Sprint Retrospective** (SCRUM): Agile Form von Lessons Learned nach jedem Sprint

### Typische Pruefungsaspekte
- Methoden benennen und deren Zweck erlaeutern
- Feedback-Regeln formulieren
- Ergebnisse eines Lessons-Learned-Workshops dokumentieren

### Haeufige Fehler
- Feedback wird mit Kritik gleichgesetzt – Feedback umfasst auch positive Rueckmeldung
- Lessons Learned wird als optional betrachtet – es ist integraler Bestandteil des Projektabschlusses
