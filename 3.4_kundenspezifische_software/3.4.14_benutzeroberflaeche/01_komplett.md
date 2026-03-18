# Komplett: 3.4.14 – Benutzeroberflaeche gestalten

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.14
- **Thema:** Benutzeroberflaeche gestalten koennen

## Ziel

Du musst die Unterschiede zwischen Usability und UX kennen, Prinzipien des nutzerzentrierten Designs anwenden und Gestaltungsentscheidungen fuer Benutzeroberflaechen begruenden koennen.

## Themenkreise

| Nr. | Themenkreis | Schwerpunkt |
|-----|-------------|-------------|
| 1 | Usability | Gebrauchstauglichkeit, Effizienz, Effektivitaet |
| 2 | User-Experience | Gesamterlebnis, Emotionen, Aesthetik |

---

## Grundlagen

### Usability vs. User Experience (UX)

| Aspekt | Usability | User Experience (UX) |
|--------|-----------|---------------------|
| Definition | Gebrauchstauglichkeit (ISO 9241-11) | Gesamterlebnis des Benutzers |
| Fokus | Aufgabe effektiv, effizient, zufrieden erledigen | Emotionen, Erwartungen, Aesthetik |
| Umfang | Teilaspekt von UX | Umfasst Usability + Gesamteindruck |
| Messbar durch | Aufgabenerfuellung, Fehlerquote, Zeit | Befragung, Emotionsmessung, Net Promoter Score |
| Beispiel | "Ich konnte die Bestellung in 3 Klicks aufgeben" | "Die App fuehlt sich modern an und macht Spass" |

**Merke:** Gute UX setzt gute Usability voraus, aber gute Usability allein reicht fuer gute UX nicht aus.

### User-Centered Design (UCD) – Nutzerzentrierter Entwurf

**Definition:** Ein Designprozess, bei dem die Beduerfnisse, Wuensche und Einschraenkungen der Benutzer in jeder Phase beruecksichtigt werden.

**Ablauf (nach DIN EN ISO 9241-210):**

```
+---------------------+
| 1. Nutzungskontext  |
|    verstehen        |
+--------+------------+
         |
         v
+--------+------------+
| 2. Anforderungen    |
|    spezifizieren    |
+--------+------------+
         |
         v
+--------+------------+
| 3. Gestaltungs-     |
|    loesungen        |<-------+
|    entwerfen        |        |
+--------+------------+        |
         |                     |
         v                     |
+--------+------------+        |
| 4. Evaluation       |--------+
|    (Testen mit      |  Iteration
|     Benutzern)      |
+---------------------+
```

**Phasen im Detail:**
1. **Nutzungskontext verstehen:** Wer sind die Benutzer? Welche Aufgaben erledigen sie? In welcher Umgebung?
2. **Anforderungen spezifizieren:** Welche Funktionen benoetigen die Benutzer? Welche Einschraenkungen gibt es?
3. **Gestaltungsloesungen entwerfen:** Wireframes, Mockups, Prototypen erstellen
4. **Evaluation:** Testen mit echten Benutzern, Ergebnisse auswerten, zurueck zu Schritt 3

### Heuristische Evaluation nach Nielsen

Jakob Nielsen definierte 10 Usability-Heuristiken zur Bewertung von Benutzeroberflaechen:

| Nr. | Heuristik | Erklaerung |
|-----|-----------|------------|
| 1 | Sichtbarkeit des Systemstatus | System informiert ueber aktuellen Zustand (z.B. Ladebalken) |
| 2 | Uebereinstimmung System / reale Welt | Begriffe und Symbole aus der Nutzerwelt verwenden |
| 3 | Nutzerkontrolle und Freiheit | Undo/Redo, Abbrechen-Button |
| 4 | Konsistenz und Standards | Einheitliche Begriffe und Layouts |
| 5 | Fehlervermeidung | Validierung vor Absenden, Bestaetigungsdialoge |
| 6 | Erkennen statt Erinnern | Sichtbare Optionen statt versteckter Befehle |
| 7 | Flexibilitaet und Effizienz | Shortcuts fuer Experten, Standard fuer Einsteiger |
| 8 | Aesthetisches und minimalistisches Design | Nur relevante Informationen anzeigen |
| 9 | Fehler erkennen und beheben | Klare Fehlermeldungen mit Loesungsvorschlag |
| 10 | Hilfe und Dokumentation | Kontextsensitive Hilfe, FAQ, Suchfunktion |

### Responsive Design

**Definition:** Webdesign, bei dem sich das Layout automatisch an verschiedene Bildschirmgroessen anpasst (Desktop, Tablet, Smartphone).

**Techniken:**

| Technik | Beschreibung |
|---------|-------------|
| Media Queries | CSS-Regeln fuer verschiedene Bildschirmbreiten |
| Flexibles Grid | Spalten passen sich prozentual an |
| Flexible Bilder | Bilder skalieren mit max-width: 100% |
| Mobile First | Design beginnt mit der kleinsten Ansicht |
| Breakpoints | Definierte Punkte, an denen das Layout wechselt |

**Typische Breakpoints:**

```
Smartphone:  < 576px   (1 Spalte)
Tablet:      576-992px (2 Spalten)
Desktop:     > 992px   (3+ Spalten)
```

### Gestaltungsgesetze (Gestaltpsychologie)

| Gesetz | Bedeutung | Beispiel |
|--------|-----------|----------|
| Naehe | Elemente nah beieinander werden als zusammengehoerig wahrgenommen | Formularfeld + Label |
| Aehnlichkeit | Gleichartige Elemente werden als Gruppe wahrgenommen | Gleiche Farbe fuer Aktions-Buttons |
| Geschlossenheit | Unvollstaendige Formen werden im Kopf ergaenzt | Logo mit Luecken |
| Kontinuitaet | Das Auge folgt Linien und Kurven | Navigation in einer Reihe |

---

## Vertiefung

### Vergleich: Evaluationsmethoden

| Methode | Durchfuehrung | Aufwand | Ergebnis |
|---------|--------------|---------|----------|
| Heuristische Evaluation | Experten pruefen anhand Heuristiken | Mittel | Liste von Usability-Problemen |
| Usability-Test | 5-8 Benutzer fuehren Aufgaben aus | Hoch | Konkrete Nutzungsprobleme |
| A/B-Test | Zwei Varianten werden verglichen | Mittel | Statistisch bessere Variante |
| Eye-Tracking | Blickbewegungen werden aufgezeichnet | Sehr hoch | Visuelle Aufmerksamkeitsmuster |

### Typische Pruefungsaspekte
- Usability vs. UX unterscheiden koennen
- Nielsen-Heuristiken an Beispielen anwenden
- Responsive Design: Warum und wie?
- Gestaltungsgesetze erkennen und benennen
- Szenario: Welche Gestaltungsfehler sind in einem Screenshot zu erkennen?

### Haeufige Fehler
- UX wird auf "schoen aussehen" reduziert → UX umfasst das gesamte Nutzungserlebnis
- Responsive Design wird mit "mobilfreundlich" gleichgesetzt → es umfasst ALLE Bildschirmgroessen
- Heuristische Evaluation wird mit Usability-Test verwechselt: Heuristik = Experten, Usability-Test = echte Benutzer
- Gestaltungsgesetze werden ignoriert → fuehrt zu unuebersichtlichen Oberflaechen

---

## Uebungen

**Aufgabe 1:** Erklaere den Unterschied zwischen Usability und User Experience. Gib je ein Beispiel.

**Aufgabe 2:** Ein Online-Formular hat folgende Probleme: (a) Kein Ladebalken beim Absenden, (b) Fehlermeldung lautet nur "Error 500", (c) Es gibt keine Moeglichkeit, zum vorherigen Schritt zurueckzukehren. Welche Nielsen-Heuristiken sind jeweils verletzt?

**Aufgabe 3:** Nenne die vier Phasen des nutzerzentrierten Designs (UCD) und erklaere, warum der Prozess iterativ ist.

**Aufgabe 4:** Was ist Responsive Design? Nenne drei Techniken, mit denen es umgesetzt wird.

**Aufgabe 5:** Erklaere das Gestaltungsgesetz der Naehe und nenne ein Beispiel aus der UI-Gestaltung.

---
---

# Loesungen

## Aufgabe 1
**Usability** beschreibt die Gebrauchstauglichkeit: Kann ein Benutzer seine Aufgabe effektiv, effizient und zufriedenstellend ausfuehren? Beispiel: Ein Bestellvorgang ist in wenigen Klicks abgeschlossen.
**User Experience (UX)** umfasst das gesamte Erlebnis: Wie fuehlt sich der Benutzer vor, waehrend und nach der Nutzung? Beispiel: Die App hat ein modernes Design, reagiert schnell und hinterlaesst einen positiven Gesamteindruck.

## Aufgabe 2
- a) **Heuristik 1 – Sichtbarkeit des Systemstatus:** Benutzer weiss nicht, ob die Aktion laeuft.
- b) **Heuristik 9 – Fehler erkennen und beheben:** Fehlermeldung ist technisch und bietet keine Hilfe.
- c) **Heuristik 3 – Nutzerkontrolle und Freiheit:** Keine Moeglichkeit, den Schritt rueckgaengig zu machen.

## Aufgabe 3
1. Nutzungskontext verstehen (Wer nutzt die Software? Wofuer?)
2. Anforderungen spezifizieren (Was brauchen die Benutzer?)
3. Gestaltungsloesungen entwerfen (Wireframes, Prototypen)
4. Evaluation (Testen mit Benutzern)
Iterativ, weil die Evaluation oft Schwaechen aufdeckt, die eine Ueberarbeitung der Gestaltung erfordern. Erst durch mehrere Durchlaeufe entsteht eine optimale Loesung.

## Aufgabe 4
Responsive Design ist ein Webdesign-Ansatz, bei dem sich das Layout automatisch an verschiedene Bildschirmgroessen anpasst.
Techniken: (1) Media Queries in CSS, (2) Flexibles Grid-Layout mit prozentualen Breiten, (3) Mobile-First-Ansatz (kleinste Ansicht zuerst gestalten).

## Aufgabe 5
Das Gesetz der Naehe besagt, dass Elemente, die raeumlich nah beieinander stehen, als zusammengehoerig wahrgenommen werden. Beispiel: In einem Formular stehen das Label "E-Mail" und das zugehoerige Eingabefeld direkt nebeneinander, waehrend zwischen verschiedenen Formulargruppen (z.B. Adresse und Zahlungsdaten) ein groesserer Abstand liegt.
