# Uebungen: 1.1.01 – Merkmale und Methoden des Projektmanagements

## Merkmale eines Projektes

**Aufgabe 1:** Nenne mindestens fuenf Merkmale, die ein Projekt von einer Routineaufgabe unterscheiden.

**Aufgabe 2:** Ein Unternehmen fuehrt woechentlich Softwareupdates auf allen Clientrechnern durch. Handelt es sich dabei um ein Projekt? Begruende deine Antwort anhand der Projektmerkmale.

**Aufgabe 3:** Ein Autohaus beauftragt die Entwicklung einer individuellen Kundenverwaltungssoftware. Zeitrahmen: 6 Monate, Budget: 80.000 EUR. Welche Projektmerkmale sind hier erfuellt?

---

## Phasen der Teambildung

**Aufgabe 4:** Ordne die folgenden Situationen den Teambildungsphasen nach Tuckman zu:
- a) Die Teammitglieder diskutieren hitzig ueber die Aufgabenverteilung.
- b) Das Team arbeitet effizient und selbstorganisiert an den Arbeitspaketen.
- c) Neue Mitglieder stellen sich vor und erkundigen sich nach den Projektzielen.
- d) Das Team hat gemeinsame Regeln fuer die Zusammenarbeit aufgestellt.

**Aufgabe 5:** Ein neuer Entwickler stoesst in der Performing-Phase zum Team. Welche Auswirkungen kann das haben? In welche Phase kann das Team zurueckfallen?

---

## Projektphasen: Wasserfallmodell vs. SCRUM

**Aufgabe 6:** Nenne die Phasen des Wasserfallmodells in der korrekten Reihenfolge.

**Aufgabe 7:** Ein Kunde moechte eine E-Commerce-Plattform entwickeln lassen. Die Anforderungen sind noch unklar, und der Kunde moechte frueh erste Ergebnisse sehen. Welches Vorgehensmodell empfiehlst du? Begruende mit mindestens drei Argumenten.

**Aufgabe 8:** Nenne die drei Rollen in SCRUM und beschreibe jeweils in einem Satz deren Aufgabe.

**Aufgabe 9:** Was ist der Unterschied zwischen Sprint Backlog und Product Backlog?

---

## Projektplanung

**Aufgabe 10:** Erklaere den Unterschied zwischen Gesamtpuffer und freiem Puffer im Netzplan.

**Aufgabe 11:** Gegeben ist folgender Netzplan:

| Vorgang | Dauer (Tage) | Vorgaenger |
|---------|-------------|------------|
| A | 4 | – |
| B | 3 | A |
| C | 6 | A |
| D | 2 | B |
| E | 3 | C, D |

a) Fuehre die Vorwaerts- und Rueckwaertsrechnung durch.
b) Bestimme den kritischen Weg.
c) Berechne die Pufferzeiten fuer alle Vorgaenge.

**Aufgabe 12:** Formuliere das folgende Projektziel SMART um: "Wir muessen die Website irgendwann mal ueberarbeiten."

**Aufgabe 13:** Was ist ein Meilenstein und wozu dient er? Nenne zwei Beispiele fuer Meilensteine in einem IT-Projekt.

---

## Reflektionsmethoden

**Aufgabe 14:** Beschreibe den Ablauf eines Lessons-Learned-Workshops in vier Schritten.

**Aufgabe 15:** Formuliere ein konstruktives Feedback fuer folgende Situation: Ein Kollege hat die Dokumentation fuer eine Schnittstelle geschrieben, allerdings fehlen alle Fehlercodes.

**Aufgabe 16:** Erklaere den Zusammenhang zwischen Lessons Learned und dem PDCA-Zyklus.

---

---

# Loesungen

## Aufgabe 1
Einmaligkeit, zeitliche Begrenzung, definiertes Ziel, begrenzte Ressourcen, Komplexitaet, eigene Organisationsform (Projektteam).

## Aufgabe 2
Nein, kein Projekt. Begruendung: Woechentliche Softwareupdates sind wiederkehrend (keine Einmaligkeit), haben kein definiertes Ende und gehoeren zur Routinearbeit der IT-Abteilung.

## Aufgabe 3
Einmaligkeit (individuelle Software), zeitliche Begrenzung (6 Monate), begrenzte Ressourcen (80.000 EUR), definiertes Ziel (Kundenverwaltungssoftware), eigene Organisation (Entwicklungsteam).

## Aufgabe 4
- a) **Storming** – Konflikte ueber Rollen und Aufgaben
- b) **Performing** – produktive, eigenstaendige Arbeit
- c) **Forming** – Kennenlernen und Orientierung
- d) **Norming** – Regeln werden festgelegt und akzeptiert

## Aufgabe 5
Das Team kann in die Storming-Phase zurueckfallen, da neue Gruppendynamiken entstehen. Rollen und Zustaendigkeiten muessen neu verhandelt werden.

## Aufgabe 6
1. Anforderungsanalyse, 2. Entwurf/Design, 3. Implementierung, 4. Test, 5. Betrieb/Wartung.

## Aufgabe 7
SCRUM. Begruendung: (1) Anforderungen sind unklar und koennen sich aendern – SCRUM erlaubt laufende Anpassung. (2) Der Kunde will frueh Ergebnisse sehen – nach jedem Sprint gibt es ein funktionsfaehiges Increment. (3) Durch Sprint Reviews erhaelt der Kunde regelmaessig die Moeglichkeit, Feedback zu geben.

## Aufgabe 8
- **Product Owner:** Verantwortet die Anforderungen und priorisiert das Product Backlog.
- **Scrum Master:** Sorgt fuer die Einhaltung des SCRUM-Prozesses und beseitigt Hindernisse.
- **Entwicklungsteam:** Setzt die Anforderungen aus dem Sprint Backlog technisch um.

## Aufgabe 9
- **Product Backlog:** Gesamte, priorisierte Liste aller Anforderungen fuer das Produkt. Wird vom Product Owner gepflegt.
- **Sprint Backlog:** Teilmenge des Product Backlogs, die fuer den aktuellen Sprint ausgewaehlt und vom Entwicklungsteam bearbeitet wird.

## Aufgabe 10
- **Gesamtpuffer (GP):** Zeitspanne, um die ein Vorgang verschoben werden kann, ohne das Projektende zu gefaehrden. GP = SA - FA.
- **Freier Puffer (FP):** Zeitspanne, um die ein Vorgang verschoben werden kann, ohne den fruehesten Anfang des Nachfolgers zu verschieben. FP = FA(Nachfolger) - FE(Vorgang).

## Aufgabe 11
**Vorwaertsrechnung:**
- A: FA=0, FE=4
- B: FA=4, FE=7
- C: FA=4, FE=10
- D: FA=7, FE=9
- E: FA=10 (max(FE_C, FE_D) = max(10,9) = 10), FE=13

**Rueckwaertsrechnung:**
- E: SE=13, SA=10
- C: SE=10, SA=4 → GP=0
- D: SE=10, SA=8 → GP=1
- B: SE=8, SA=5 → GP=1
- A: SE=4, SA=0 → GP=0

**Kritischer Weg:** A → C → E (Dauer: 13 Tage)
**Pufferzeiten:** A=0, B=1, C=0, D=1, E=0

## Aufgabe 12
Beispiel: "Bis zum 31.03.2026 wird die Unternehmenswebsite redesignt. Die Startseite, die Produktseiten und das Kontaktformular werden ueberarbeitet. Das Budget betraegt 15.000 EUR. Die Abnahme erfolgt durch die Marketingabteilung."

## Aufgabe 13
Ein Meilenstein ist ein definierter Zeitpunkt im Projekt, der den Abschluss einer wichtigen Phase markiert. Er hat keine Dauer. Beispiele: (1) Abnahme des Pflichtenhefts, (2) Abschluss der Testphase.

## Aufgabe 14
1. Daten sammeln: Fakten und Erfahrungen zusammentragen (Was war geplant? Was ist passiert?)
2. Analyse: Ursachen fuer Abweichungen identifizieren
3. Dokumentation: Erkenntnisse strukturiert festhalten
4. Transfer: Ergebnisse fuer zukuenftige Projekte verfuegbar machen

## Aufgabe 15
"Deine Schnittstellendokumentation ist gut strukturiert und verstaendlich. Mir ist aufgefallen, dass die Fehlercodes noch fehlen. Koenntest du diese ergaenzen? Das wuerde die Dokumentation fuer die Entwickler deutlich nuetzlicher machen."

## Aufgabe 16
Lessons Learned entspricht den Phasen **Check** (Ergebnisse pruefen, Soll-Ist-Vergleich) und **Act** (Massnahmen ableiten, Verbesserungen umsetzen) im PDCA-Zyklus. Die gewonnenen Erkenntnisse fliessen in die Plan-Phase des naechsten Zyklus ein.
