# Komplett: 3.4.13 – Anforderungen an Softwareergonomie

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.13
- **Thema:** Anforderungen an Softwareergonomie kennen und beurteilen koennen

## Ziel

Du musst die Grundsaetze der Softwareergonomie nach DIN EN ISO 9241 kennen, anwenden und in Pruefungsszenarien bewerten koennen. Dazu gehoeren auch Barrierefreiheit (WCAG/BITV) und praktische Bewertungskriterien.

## Themenkreise

KEIN THEMENKREIS ANGEGEBEN – umfassendes Thema.

---

## Grundlagen

### DIN EN ISO 9241 – Ergonomie der Mensch-System-Interaktion

Die Norm DIN EN ISO 9241 (Teil 110) definiert sieben Grundsaetze der Dialoggestaltung, die die Interaktion zwischen Benutzer und Software bewerten:

| Nr. | Grundsatz | Bedeutung | Beispiel |
|-----|-----------|-----------|----------|
| 1 | Aufgabenangemessenheit | Software unterstuetzt die Aufgabe ohne unnoetige Schritte | Bestellformular zeigt nur relevante Felder |
| 2 | Selbstbeschreibungsfaehigkeit | Jeder Schritt ist verstaendlich, ohne Handbuch | Tooltips, Hilfetexte, klare Beschriftungen |
| 3 | Erwartungskonformitaet | Software verhaelt sich so, wie der Benutzer es erwartet | "Speichern"-Button oben links, Abbruch mit ESC |
| 4 | Fehlertoleranz | Fehlerhafte Eingaben fuehren nicht zu Datenverlust | Rueckgaengig-Funktion, Validierung vor Absenden |
| 5 | Steuerbarkeit | Benutzer kann Ablauf und Geschwindigkeit steuern | Zurueck-Button, Abbruch-Moeglichkeit, Undo |
| 6 | Individualisierbarkeit | Software laesst sich an Benutzerbeduerfnisse anpassen | Schriftgroesse, Farbschema, Dashboard-Layout |
| 7 | Lernfoerderlichkeit | Software unterstuetzt das Erlernen der Bedienung | Tutorials, Assistenten, kontextsensitive Hilfe |

**Merkhilfe:** **A**ufgabe – **S**elbst – **E**rwartung – **F**ehler – **S**teuerung – **I**ndividuell – **L**ernen

### Usability (Gebrauchstauglichkeit)

**Definition (DIN EN ISO 9241-11):** Das Ausmass, in dem ein Produkt von bestimmten Benutzern in einem bestimmten Nutzungskontext genutzt werden kann, um bestimmte Ziele **effektiv**, **effizient** und **zufriedenstellend** zu erreichen.

| Kriterium | Bedeutung | Beispiel |
|-----------|-----------|----------|
| Effektivitaet | Aufgabe wird korrekt und vollstaendig erledigt | Bestellung wird fehlerfrei abgeschlossen |
| Effizienz | Aufgabe wird mit minimalem Aufwand erledigt | Wenige Klicks bis zum Ziel |
| Zufriedenheit | Benutzer hat positives Nutzungserlebnis | Klare Rueckmeldungen, angenehmes Design |

### Barrierefreiheit (Accessibility)

**Definition:** Software muss so gestaltet sein, dass sie auch von Menschen mit Behinderungen genutzt werden kann.

**Regelwerke:**

| Standard | Beschreibung | Geltungsbereich |
|----------|-------------|-----------------|
| WCAG 2.1 | Web Content Accessibility Guidelines (W3C) | International, Webinhalte |
| BITV 2.0 | Barrierefreie-Informationstechnik-Verordnung | Deutschland, oeffentliche Stellen |
| DIN EN ISO 9241-171 | Leitlinien fuer barrierefreie Software | International, allgemein |

**WCAG-Prinzipien (POUR):**
1. **Perceivable (Wahrnehmbar):** Textalternativen fuer Bilder, Untertitel fuer Videos
2. **Operable (Bedienbar):** Tastaturnavigation, ausreichend Zeit fuer Eingaben
3. **Understandable (Verstaendlich):** Klare Sprache, konsistente Navigation
4. **Robust:** Kompatibel mit Hilfstechnologien (Screenreader, Braillezeile)

**Praktische Massnahmen:**
- Alt-Texte fuer Bilder
- Kontrastverhaeeltnis mindestens 4,5:1 (normal) bzw. 3:1 (gross)
- Tastaturbedienbarkeit aller Funktionen
- Formularbeschriftungen mit `<label>`-Elementen
- Skip-Links fuer Screenreader
- Keine reinen Farb-Informationen (z.B. "rote Felder sind Pflichtfelder")

---

## Vertiefung

### Zusammenhang der Konzepte

```
+---------------------------+
|  DIN EN ISO 9241-110      |
|  (7 Grundsaetze der       |
|   Dialoggestaltung)       |
+---------------------------+
            |
            v
+---------------------------+
|  Usability                |
|  (DIN EN ISO 9241-11)     |
|  Effektiv, Effizient,     |
|  Zufriedenstellend        |
+---------------------------+
            |
            v
+---------------------------+
|  Accessibility            |
|  (WCAG, BITV)             |
|  Barrierefreiheit fuer    |
|  alle Nutzergruppen       |
+---------------------------+
```

### Evaluationskriterien in der Praxis

| Methode | Beschreibung | Wann einsetzen |
|---------|-------------|----------------|
| Heuristische Evaluation | Experten pruefen anhand von Regeln (z.B. Nielsen) | Frueh im Entwicklungsprozess |
| Usability-Test | Echte Benutzer testen die Software | Nach Prototyp-Phase |
| Cognitive Walkthrough | Schritt-fuer-Schritt-Analyse aus Benutzersicht | Entwurfsphase |
| Fragebogen (SUS, UEQ) | Standardisierte Befragung nach Nutzung | Nach Einfuehrung / Release |

### Typische Pruefungsaspekte
- Grundsaetze der DIN EN ISO 9241-110 benennen und in Szenarien erkennen
- Negativbeispiel bewerten: Welcher Grundsatz ist verletzt?
- Unterschied Usability vs. User Experience erklaeren
- WCAG-Prinzipien nennen koennen
- Massnahmen fuer Barrierefreiheit benennen

### Haeufige Fehler
- Usability wird mit Design verwechselt: Schoen ≠ benutzbar
- Barrierefreiheit wird nur auf Sehbehinderung reduziert → betrifft auch motorische, kognitive und auditive Einschraenkungen
- Erwartungskonformitaet wird vergessen: Software funktioniert, aber anders als gewohnt → frustriert Benutzer
- Individualisierbarkeit wird als "optional nice-to-have" abgetan → ist ein Grundsatz der Norm

---

## Uebungen

**Aufgabe 1:** Nenne die sieben Grundsaetze der Dialoggestaltung nach DIN EN ISO 9241-110.

**Aufgabe 2:** Ein Online-Formular zeigt nach dem Absenden nur "Fehler" an, ohne zu sagen, welches Feld falsch ist. Welche Grundsaetze sind verletzt? Begruende.

**Aufgabe 3:** Nenne die drei Kriterien der Usability nach DIN EN ISO 9241-11 und erklaere sie jeweils in einem Satz.

**Aufgabe 4:** Ein Unternehmen moechte seine Webseite barrierefrei gestalten. Nenne fuenf konkrete Massnahmen.

**Aufgabe 5:** Ordne die folgenden Beispiele dem passenden Grundsatz zu:
- a) Die Software bietet eine Undo-Funktion fuer versehentlich geloeschte Eintraege.
- b) Ein Assistent fuehrt neue Benutzer Schritt fuer Schritt durch die Einrichtung.
- c) Der Benutzer kann die Sprache, Schriftgroesse und das Farbschema aendern.
- d) Ein Eingabefeld fuer die Postleitzahl akzeptiert nur fuenf Ziffern.

**Aufgabe 6:** Erklaere den Unterschied zwischen Usability und User Experience (UX).

---
---

# Loesungen

## Aufgabe 1
1. Aufgabenangemessenheit
2. Selbstbeschreibungsfaehigkeit
3. Erwartungskonformitaet
4. Fehlertoleranz
5. Steuerbarkeit
6. Individualisierbarkeit
7. Lernfoerderlichkeit

## Aufgabe 2
- **Selbstbeschreibungsfaehigkeit** verletzt: Der Benutzer erhaelt keine Erklaeung, was genau falsch ist.
- **Fehlertoleranz** verletzt: Die Fehlermeldung hilft nicht bei der Korrektur. Eine gute Fehlermeldung wuerde das betroffene Feld markieren und einen Hinweis geben (z.B. "PLZ muss 5 Ziffern enthalten").
- **Lernfoerderlichkeit** verletzt: Der Benutzer kann aus der Fehlermeldung nicht lernen, wie er es richtig macht.

## Aufgabe 3
- **Effektivitaet:** Die Aufgabe wird korrekt und vollstaendig erledigt (z.B. Bestellung erfolgreich aufgegeben).
- **Effizienz:** Die Aufgabe wird mit moeglichst geringem Aufwand erledigt (z.B. wenige Klicks noetig).
- **Zufriedenheit:** Der Benutzer hat ein positives Erlebnis bei der Nutzung (z.B. klare Rueckmeldungen, angenehmes Design).

## Aufgabe 4
1. Alt-Texte fuer alle Bilder hinterlegen
2. Ausreichendes Kontrastverhaeeltnis (mindestens 4,5:1)
3. Vollstaendige Tastaturbedienbarkeit
4. Formularfelder mit sichtbaren Labels versehen
5. Videos mit Untertiteln versehen

## Aufgabe 5
- a) **Fehlertoleranz** (und Steuerbarkeit) – Undo schuetzt vor Datenverlust
- b) **Lernfoerderlichkeit** – Assistent hilft beim Erlernen der Software
- c) **Individualisierbarkeit** – Anpassung an persoenliche Beduerfnisse
- d) **Aufgabenangemessenheit** (und Fehlertoleranz) – Nur gueltige Eingaben moeglich, unnoetiger Aufwand wird vermieden

## Aufgabe 6
**Usability** bezieht sich auf die Gebrauchstauglichkeit: Kann der Benutzer seine Aufgabe effektiv, effizient und zufriedenstellend erledigen? **User Experience (UX)** umfasst darueber hinaus das gesamte Nutzungserlebnis – also auch Emotionen, Aesthetik, Erwartungen vor der Nutzung und den Gesamteindruck danach. Usability ist ein Teilaspekt von UX.
