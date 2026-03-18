# Komplett: 3.4.15 – Prototypen (Mockups) erstellen

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.15
- **Thema:** Prototypen (Mockups) erstellen koennen

## Ziel

Du musst die verschiedenen Stufen der Prototypenentwicklung kennen (Wireframe, Mockup, Prototyp), Tools benennen und den iterativen Designprozess verstehen. In der Pruefung kann gefragt werden, wann welcher Prototyp-Typ sinnvoll ist.

## Themenkreise

KEIN THEMENKREIS ANGEGEBEN – umfassendes Thema.

---

## Grundlagen

### Wireframe, Mockup, Prototyp – Abgrenzung

| Kriterium | Wireframe | Mockup | Prototyp |
|-----------|-----------|--------|----------|
| Definition | Grobe Skizze der Struktur/Layout | Detaillierter visueller Entwurf | Interaktives, klickbares Modell |
| Detail-Level | Gering (Low Fidelity) | Mittel bis hoch (High Fidelity) | Hoch (funktional) |
| Interaktivitaet | Keine | Keine (statisches Bild) | Ja (klickbar, navigierbar) |
| Farben/Design | Grautöne, Platzhalter | Echte Farben, Schriften, Icons | Echtes Design + Interaktion |
| Zweck | Struktur und Layout festlegen | Visuelles Design abstimmen | Nutzererlebnis testen |
| Aufwand | Gering (Minuten bis Stunden) | Mittel (Stunden bis Tage) | Hoch (Tage bis Wochen) |
| Typisches Tool | Papier, Balsamiq, draw.io | Figma, Sketch, Adobe XD | Figma (Prototyp), Axure, HTML |

### Fidelity-Stufen (Detailgrad)

```
Low Fidelity          Medium Fidelity          High Fidelity
+----------------+    +----------------+    +-------------------+
| [Logo]         |    | LOGO           |    | +-Logo-+  Suche   |
|                |    | ================|    | Startseite | Shop |
| [Navigation]   |    | Start | Shop   |    |==================|
|                |    |                |    | Willkommen!       |
| [Inhalt]       |    | Produktliste   |    | +--+ +--+ +--+   |
|                |    | +--+ +--+ +--+ |    | |  | |  | |  |   |
| [Footer]       |    | [Button]       |    | |Prod|Prod|Prod|  |
+----------------+    +----------------+    | +--+ +--+ +--+   |
                                            | [In den Warenkorb]|
  Papier, Stift        Balsamiq, draw.io    +-------------------+
                                              Figma, Adobe XD
```

### Werkzeuge (Tools)

| Tool | Typ | Staerke | Kosten |
|------|-----|---------|--------|
| Papier + Stift | Low Fidelity | Schnellste Methode, keine Einarbeitung | Kostenlos |
| Balsamiq | Low/Medium Fidelity | Bewusst skizzenhaft, fokussiert auf Struktur | Kostenpflichtig |
| draw.io (diagrams.net) | Low/Medium Fidelity | Kostenlos, webbasiert, auch fuer Diagramme | Kostenlos |
| Figma | Medium/High Fidelity | Kollaborativ, Browser-basiert, Prototyping | Freemium |
| Adobe XD | High Fidelity | Professionelles Design + Prototyping | Kostenpflichtig |
| Axure RP | High Fidelity | Komplexe interaktive Prototypen | Kostenpflichtig |
| HTML/CSS | High Fidelity | Echter Code, direkt nutzbar | Kostenlos (Eigenentwicklung) |

### Iterativer Designprozess

**Definition:** Prototypen werden nicht einmal erstellt und dann umgesetzt, sondern in mehreren Zyklen verbessert. Jede Iteration besteht aus: Entwerfen → Testen → Feedback → Ueberarbeiten.

```
        Entwerfen
           |
           v
     +-----------+
     |  Prototyp  |
     |  erstellen |
     +-----------+
           |
           v
     +-----------+
     |  Testen   |------> Feedback sammeln
     |  (Nutzer) |               |
     +-----------+               v
           ^              +-----------+
           |              | Auswerten |
           +--------------| Anpassen  |
         Neue Iteration   +-----------+
```

**Vorteile des iterativen Vorgehens:**
- Fruehes Erkennen von Usability-Problemen
- Kostenguenstige Korrekturen (Aenderungen am Papier statt am fertigen Code)
- Benutzer werden frueh eingebunden → hoehere Akzeptanz
- Risikominimierung: Fehlentwicklungen werden frueh erkannt

---

## Vertiefung

### Wann welchen Prototyp-Typ einsetzen?

| Projektphase | Empfohlener Typ | Begruendung |
|-------------|-----------------|-------------|
| Ideenfindung | Papier-Wireframe | Schnell, flexibel, foerdert Diskussion |
| Anforderungsanalyse | Digitaler Wireframe | Struktur mit Kunden abstimmen |
| Entwurfsphase | Mockup | Visuelles Design freigeben lassen |
| Vor Implementierung | Klickbarer Prototyp | Nutzererlebnis validieren |
| Usability-Test | High-Fidelity-Prototyp | Realistisches Testerlebnis |

### Prototyping-Methoden

| Methode | Beschreibung |
|---------|-------------|
| Paper Prototyping | Skizzen auf Papier, Tester "klickt" auf gezeichnete Buttons |
| Horizontal | Alle Seiten/Ansichten, aber ohne Funktionalitaet (Breitentest) |
| Vertikal | Eine Funktion vollstaendig durchgaengig (Tiefentest) |
| Wizard-of-Oz | System wird simuliert, Mensch im Hintergrund reagiert |

### Typische Pruefungsaspekte
- Unterschied Wireframe / Mockup / Prototyp erklaeren
- Passendes Prototyping-Tool fuer ein Szenario empfehlen
- Vorteile des iterativen Vorgehens benennen
- Fidelity-Stufen zuordnen koennen
- Zusammenhang mit User-Centered Design (Thema 3.4.14)

### Haeufige Fehler
- Wireframe wird mit Mockup verwechselt: Wireframe = Struktur, Mockup = visuelles Design
- Prototyp wird als fertige Software missverstanden → Prototyp dient nur der Validierung
- Zu frueher Einsatz von High-Fidelity: In der Ideenphase genuegt Papier → spart Zeit und Kosten
- Iteration wird uebersprungen: "Einmal entwerfen und umsetzen" fuehrt zu Usability-Problemen

---

## Uebungen

**Aufgabe 1:** Erklaere die Unterschiede zwischen Wireframe, Mockup und Prototyp. Nenne fuer jeden Typ ein geeignetes Werkzeug.

**Aufgabe 2:** Ein Kunde moechte eine neue Webanwendung fuer sein Reisebuero. Der Designer hat drei Vorschlaege:
- a) Eine Papier-Skizze mit Kaestchen fuer Navigation, Inhalt und Footer.
- b) Ein farbiges Design mit echtem Logo, Schriften und Bildern (nicht klickbar).
- c) Eine klickbare Version im Browser, bei der man durch die Seiten navigieren kann.
Ordne jedem Vorschlag den korrekten Typ zu und erklaere, in welcher Projektphase er sinnvoll ist.

**Aufgabe 3:** Erklaere, warum der Prototyping-Prozess iterativ sein sollte. Nenne drei Vorteile.

**Aufgabe 4:** Nenne drei Prototyping-Tools und beschreibe deren Einsatzbereich.

**Aufgabe 5:** Was versteht man unter "Fidelity" im Zusammenhang mit Prototypen? Erklaere Low Fidelity und High Fidelity.

---
---

# Loesungen

## Aufgabe 1
- **Wireframe:** Grobe Skizze der Seitenstruktur, ohne Farben oder Details. Werkzeug: Balsamiq oder Papier.
- **Mockup:** Detaillierter visueller Entwurf mit echten Farben, Schriften und Icons, aber nicht interaktiv. Werkzeug: Figma.
- **Prototyp:** Interaktives, klickbares Modell, das das Nutzererlebnis simuliert. Werkzeug: Figma (Prototyp-Modus) oder Axure.

## Aufgabe 2
- a) **Wireframe** – Geeignet in der Ideenfindung/Anforderungsanalyse, um die Grundstruktur abzustimmen.
- b) **Mockup** – Geeignet in der Entwurfsphase, um das visuelle Design mit dem Kunden freizugeben.
- c) **Prototyp** – Geeignet vor der Implementierung, um die Navigation und das Nutzererlebnis zu testen.

## Aufgabe 3
Der Prozess sollte iterativ sein, weil:
1. Usability-Probleme frueh erkannt und guenstig behoben werden koennen (Aenderungen am Prototyp statt am fertigen Code).
2. Benutzerfeedback in jede Iteration einfliesst → das Ergebnis entspricht besser den Beduerfnissen.
3. Risiko sinkt: Fehlentwicklungen werden vor der teuren Implementierung entdeckt.

## Aufgabe 4
1. **Balsamiq:** Low-Fidelity-Wireframes, bewusst skizzenhaft, fuer fruehe Entwuerfe.
2. **Figma:** Kollaboratives Design-Tool fuer Wireframes, Mockups und klickbare Prototypen.
3. **draw.io (diagrams.net):** Kostenlos, fuer einfache Wireframes und Diagramme.

## Aufgabe 5
**Fidelity** beschreibt den Detailgrad eines Prototyps.
- **Low Fidelity:** Grobe Darstellung (Kaestchen, Platzhalter, keine Farben). Schnell erstellbar, fokussiert auf Struktur. Beispiel: Papier-Wireframe.
- **High Fidelity:** Detaillierte Darstellung (echte Farben, Schriften, Bilder, Interaktion). Nah am Endprodukt. Beispiel: Klickbarer Figma-Prototyp.
