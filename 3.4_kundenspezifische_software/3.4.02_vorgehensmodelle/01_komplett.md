# Komplett: 3.4.02 – Vorgehensmodelle unterscheiden

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.02
- **Thema:** Vorgehensmodelle unterscheiden koennen

## Ziel

Du musst klassische und agile Vorgehensmodelle mit ihren Phasen, Rollen, Vor- und Nachteilen kennen und begruenden koennen, wann welches Modell geeignet ist.

## Themenkreise

| Nr. | Themenkreis | Schwerpunkte |
|-----|------------|-------------|
| 1 | Agile Modelle (z.B. Scrum) | Sprints, Rollen, Artefakte, Events |
| 2 | Klassische Modelle | Wasserfallmodell, Spiralmodell, V-Modell |

---

## Grundlagen

### TK 1: Agile Modelle – Scrum

**Definition:** Scrum ist ein agiles Framework fuer die iterative und inkrementelle Softwareentwicklung. Anforderungen werden in kurzen Zeitboxen (Sprints) umgesetzt und regelmaessig mit dem Kunden abgestimmt.

**Rollen in Scrum:**

| Rolle | Aufgabe |
|-------|---------|
| Product Owner | Verantwortet das Product Backlog, priorisiert Anforderungen, vertritt den Kunden |
| Scrum Master | Sorgt fuer die Einhaltung des Scrum-Prozesses, beseitigt Hindernisse, ist kein Projektleiter |
| Entwicklungsteam | Selbstorganisiert, setzt die Sprint-Aufgaben um (3–9 Personen) |

**Artefakte in Scrum:**

| Artefakt | Beschreibung |
|----------|-------------|
| Product Backlog | Priorisierte Liste aller Anforderungen (User Stories), gepflegt vom Product Owner |
| Sprint Backlog | Teilmenge des Product Backlogs, die im aktuellen Sprint umgesetzt wird |
| Increment | Funktionsfaehiges, potenziell auslieferbares Produktinkrement nach jedem Sprint |

**Events in Scrum:**

| Event | Beschreibung | Dauer (bei 2-Wochen-Sprint) |
|-------|-------------|---------------------------|
| Sprint Planning | Team plant Sprint-Inhalt aus dem Product Backlog | max. 4 Stunden |
| Daily Scrum | Taegliches Standup: Was habe ich gemacht? Was mache ich heute? Gibt es Hindernisse? | max. 15 Minuten |
| Sprint Review | Vorstellung des Increments an Stakeholder, Feedback sammeln | max. 2 Stunden |
| Sprint Retrospective | Reflexion des Teams: Was lief gut? Was kann verbessert werden? | max. 1,5 Stunden |

**Weitere agile Begriffe:**
- **User Story** – Anforderung aus Nutzersicht: "Als [Rolle] moechte ich [Funktion], damit [Nutzen]."
- **Definition of Done (DoD)** – Kriterien, wann ein Backlog-Eintrag als abgeschlossen gilt
- **Velocity** – Menge der erledigten Story Points pro Sprint
- **Burndown Chart** – Grafische Darstellung des Restaufwands im Sprint

### TK 2: Klassische Modelle

#### Wasserfallmodell

**Definition:** Sequenzielles Vorgehensmodell, bei dem jede Phase abgeschlossen sein muss, bevor die naechste beginnt.

**Phasen:**

```
  +-----------------------+
  | 1. Anforderungsanalyse|
  +-----------+-----------+
              |
  +-----------v-----------+
  | 2. Entwurf / Design   |
  +-----------+-----------+
              |
  +-----------v-----------+
  | 3. Implementierung     |
  +-----------+-----------+
              |
  +-----------v-----------+
  | 4. Test / Verifikation |
  +-----------+-----------+
              |
  +-----------v-----------+
  | 5. Betrieb / Wartung   |
  +-----------------------+
```

**Vorteile:** Klare Struktur, einfache Planung, gute Dokumentation
**Nachteile:** Unflexibel bei Aenderungen, spaete Fehlererkennung, Kunde sieht Ergebnis erst am Ende

#### V-Modell

**Definition:** Erweiterung des Wasserfallmodells, bei dem jeder Entwicklungsphase (linke Seite) eine korrespondierende Testphase (rechte Seite) gegenueber­steht.

```
Anforderungsanalyse  ─────────────────────  Abnahmetest
       \                                       /
   Grobentwurf  ─────────────────  Systemtest
          \                            /
     Feinentwurf  ──────────  Integrationstest
            \                    /
        Implementierung ── Unittest
```

**Teststufen im V-Modell:**

| Entwicklungsphase | Korrespondierende Testphase |
|-------------------|-----------------------------|
| Anforderungsanalyse | Abnahmetest (Validierung: Richtiges System gebaut?) |
| Grobentwurf (Systemdesign) | Systemtest (Gesamtsystem gegen Spezifikation) |
| Feinentwurf (Komponentendesign) | Integrationstest (Zusammenspiel der Komponenten) |
| Implementierung | Unittest / Modultest (einzelne Funktionen/Klassen) |

**Vorteile:** Fruehe Testplanung, klare Qualitaetssicherung, gut fuer sicherheitskritische Systeme
**Nachteile:** Starr wie Wasserfallmodell, wenig Flexibilitaet bei Aenderungen

#### Spiralmodell

**Definition:** Iteratives Modell von Barry Boehm, das in mehreren Zyklen (Spiralen) die Phasen Planung, Risikoanalyse, Entwicklung und Bewertung durchlaeuft.

**Phasen pro Zyklus:**
1. **Ziele festlegen** – Anforderungen und Alternativen identifizieren
2. **Risiken analysieren** – Prototypen erstellen, Risiken bewerten
3. **Entwicklung und Test** – Umsetzung des aktuellen Zyklus
4. **Naechsten Zyklus planen** – Bewertung und Planung der naechsten Iteration

**Vorteile:** Risikogetrieben, fruehe Erkennung von Problemen, iterativ
**Nachteile:** Komplex, hoher Aufwand fuer Risikoanalyse, schwer planbar

---

## Vertiefung

### Vergleich aller Modelle

| Kriterium | Wasserfall | V-Modell | Spiralmodell | Scrum |
|-----------|-----------|----------|-------------|-------|
| Ablauf | Sequenziell | Sequenziell + Test | Iterativ (Zyklen) | Iterativ (Sprints) |
| Flexibilitaet | Gering | Gering | Mittel | Hoch |
| Kundeneinbindung | Anfang + Ende | Anfang + Ende | Pro Zyklus | Kontinuierlich |
| Fehlererkennung | Spaet | Frueh (durch Teststufen) | Frueh (Risikoanalyse) | Frueh (Sprint Review) |
| Dokumentation | Umfangreich | Umfangreich | Mittel | Schlank |
| Eignung | Stabile Anforderungen | Sicherheitskritisch | Risikoreiche Projekte | Aendernde Anforderungen |

### Wann welches Modell?

| Situation | Empfohlenes Modell | Begruendung |
|-----------|-------------------|-------------|
| Anforderungen klar, aendern sich nicht | Wasserfallmodell | Einfache, planbare Struktur |
| Sicherheitskritische Software (Medizin, Luftfahrt) | V-Modell | Systematische Testabdeckung |
| Projekt mit hohen Risiken, unklarer Technik | Spiralmodell | Risikoanalyse in jedem Zyklus |
| Anforderungen aendern sich, Kunde will frueh Ergebnisse | Scrum | Iterativ, flexibel, Kundenfeedback |
| Start-up mit innovativem Produkt | Scrum | Schnelle Anpassung an Marktfeedback |
| Oeffentlicher Auftraggeber mit festem Pflichtenheft | Wasserfallmodell / V-Modell | Vertragliche Bindung an Spezifikation |

### Typische Pruefungsaspekte
- Szenario lesen → passendes Modell waehlen und begruenden
- Rollen in Scrum benennen und deren Aufgaben beschreiben
- Phasen des Wasserfallmodells in korrekter Reihenfolge nennen
- Teststufen dem V-Modell zuordnen
- Vor- und Nachteile der Modelle gegenueberstellen

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| Scrum als "planlos" bezeichnet | Scrum ist strukturiert (Events, Rollen), aber flexibel |
| Scrum Master = Projektleiter | Der Scrum Master leitet nicht, er moderiert und beseitigt Hindernisse |
| Product Owner = Entwickler | Der Product Owner entwickelt nicht, er priorisiert Anforderungen |
| V-Modell hat keine Entwicklungsphasen | Linke Seite = Entwicklung, rechte Seite = Test |
| Spiralmodell mit Wasserfall verwechselt | Spiralmodell ist iterativ, Wasserfall ist sequenziell |

---

## Uebungen

**Aufgabe 1:** Nenne die fuenf Phasen des Wasserfallmodells in der richtigen Reihenfolge.

**Aufgabe 2:** Ordne die folgenden Teststufen den passenden Entwicklungsphasen im V-Modell zu:
- a) Integrationstest
- b) Abnahmetest
- c) Unittest
- d) Systemtest

**Aufgabe 3:** Nenne die drei Rollen in Scrum und beschreibe jeweils in einem Satz deren Aufgabe.

**Aufgabe 4:** Ein Krankenhaus beauftragt die Entwicklung einer Patientenverwaltungssoftware. Die Anforderungen sind durch Gesetze klar geregelt, Fehler im System koennen Menschenleben gefaehrden. Welches Vorgehensmodell empfiehlst du? Begruende mit mindestens drei Argumenten.

**Aufgabe 5:** Erklaere den Unterschied zwischen Product Backlog und Sprint Backlog.

---
---

# Loesungen

## Aufgabe 1
1. Anforderungsanalyse
2. Entwurf / Design
3. Implementierung
4. Test / Verifikation
5. Betrieb / Wartung

## Aufgabe 2
- a) Integrationstest → Feinentwurf (Komponentendesign)
- b) Abnahmetest → Anforderungsanalyse
- c) Unittest → Implementierung
- d) Systemtest → Grobentwurf (Systemdesign)

## Aufgabe 3
- **Product Owner:** Verantwortet das Product Backlog und priorisiert die Anforderungen im Sinne des Kunden.
- **Scrum Master:** Sorgt dafuer, dass der Scrum-Prozess eingehalten wird, und beseitigt Hindernisse fuer das Team.
- **Entwicklungsteam:** Setzt die im Sprint geplanten Aufgaben selbstorganisiert um und liefert ein funktionsfaehiges Increment.

## Aufgabe 4
**V-Modell.** Begruendung:
1. Die Anforderungen sind klar und stabil (gesetzlich geregelt) → sequenzielles Modell geeignet.
2. Sicherheitskritische Software erfordert systematische Testabdeckung → jede Entwicklungsphase hat eine korrespondierende Testphase.
3. Lueckenlose Dokumentation ist fuer Zertifizierungen und Audits erforderlich → V-Modell liefert umfangreiche Dokumentation.

## Aufgabe 5
- **Product Backlog:** Enthaelt alle Anforderungen (User Stories) des gesamten Projekts, priorisiert durch den Product Owner. Es wechselt und waechst im Laufe des Projekts.
- **Sprint Backlog:** Enthaelt nur die Auswahl an Anforderungen aus dem Product Backlog, die das Team im aktuellen Sprint (z.B. 2 Wochen) umsetzen will.
