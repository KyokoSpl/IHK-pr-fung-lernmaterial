# Uebungen: 1.1.02 – Machbarkeit und Wirtschaftlichkeit von Projekten

## Einfluss der Stakeholder

**Aufgabe 1:** Definiere den Begriff "Stakeholder" und nenne je drei Beispiele fuer interne und externe Stakeholder eines IT-Projekts.

**Aufgabe 2:** Ein Unternehmen plant die Einfuehrung eines neuen CRM-Systems. Folgende Personen/Gruppen sind beteiligt: Geschaeftsfuehrung, Vertriebsmitarbeiter, IT-Administrator, externer Softwareanbieter, Betriebsrat. Ordne sie in eine Stakeholder-Matrix (Einfluss/Interesse) ein und begruende.

**Aufgabe 3:** Welche Massnahme empfiehlst du fuer einen Stakeholder mit hohem Einfluss, aber geringem Interesse?

---

## Machbarkeitsanalyse

**Aufgabe 4:** Nenne die vier Dimensionen einer Machbarkeitsanalyse und erklaere jede in einem Satz.

**Aufgabe 5:** Ein Kunde moechte eine Lagerverwaltungssoftware innerhalb von 6 Wochen. Budget: 15.000 EUR. Das verfuegbare Team besteht aus einem Entwickler. Die Software soll an ein bestehendes ERP-System angebunden werden, dessen Schnittstelle nicht dokumentiert ist. Pruefe die Machbarkeit in allen Dimensionen.

**Aufgabe 6:** Was ist der Unterschied zwischen einer Machbarkeitsanalyse und einer Risikoanalyse?

---

## Risikoanalyse

**Aufgabe 7:** Erklaere die Formel zur Risikobewertung und nenne ein Beispiel.

**Aufgabe 8:** Erstelle eine Risikomatrix fuer folgendes Szenario: Migration eines Mailservers auf eine Cloud-Loesung. Identifiziere mindestens drei Risiken mit Bewertung und Massnahme.

**Aufgabe 9:** Nenne die vier Risikosteuerungsstrategien und ordne jeweils ein Beispiel aus der IT zu.

---

## Vor- und Nachkalkulation

**Aufgabe 10:** Erstelle eine vereinfachte Vorkalkulation fuer die Einrichtung von 20 Arbeitsplaetzen (Hardware, Software, Personal, Netzwerk). Waehle realistische Werte.

**Aufgabe 11:** Die Vorkalkulation eines Projekts ergab 45.000 EUR. Die Ist-Kosten betragen 52.000 EUR. Berechne die prozentuale Abweichung und nenne zwei moegliche Ursachen.

**Aufgabe 12:** Warum ist eine Nachkalkulation auch dann sinnvoll, wenn das Projekt im Budget geblieben ist?

---

---

# Loesungen

## Aufgabe 1
**Stakeholder:** Personen, Gruppen oder Organisationen mit Interesse am Projekt oder Betroffenheit durch dessen Ergebnis.
- **Intern:** Geschaeftsfuehrung, IT-Abteilung, Betriebsrat
- **Extern:** Kunden, Lieferanten, Behoerden (z.B. Datenschutzaufsicht)

## Aufgabe 2
| Stakeholder | Einfluss | Interesse | Strategie |
|------------|---------|-----------|-----------|
| Geschaeftsfuehrung | Hoch | Hoch | Eng einbinden |
| Vertriebsmitarbeiter | Niedrig | Hoch | Informieren |
| IT-Administrator | Hoch | Hoch | Eng einbinden |
| Softwareanbieter | Hoch | Mittel | Zufriedenstellen |
| Betriebsrat | Mittel | Mittel | Informieren/Einbinden |

## Aufgabe 3
Strategie: **Zufriedenstellen**. Den Stakeholder regelmaessig ueber Fortschritte informieren, aber nicht mit Details belasten. Sicherstellen, dass seine Bedenken gehoert werden, falls er sich staerker einbringt.

## Aufgabe 4
- **Technisch:** Sind die benoetigten Technologien verfuegbar und beherrschbar?
- **Wirtschaftlich:** Kann das Projekt im vorgegebenen Budget umgesetzt werden?
- **Organisatorisch:** Stehen ausreichend qualifizierte Mitarbeiter und Infrastruktur zur Verfuegung?
- **Zeitlich:** Kann der geforderte Fertigstellungstermin eingehalten werden?

## Aufgabe 5
- **Technisch:** Kritisch – Schnittstelle zum ERP-System ist nicht dokumentiert, Aufwand schwer schaetzbar
- **Wirtschaftlich:** Riskant – 15.000 EUR fuer einen Entwickler in 6 Wochen (ca. 6.000 EUR Personal + Lizenzkosten moeglich)
- **Organisatorisch:** Kritisch – nur ein Entwickler, kein Backup bei Ausfall
- **Zeitlich:** Kritisch – 6 Wochen mit undokumentierter Schnittstelle sehr knapp
- → Empfehlung: Projekt in aktueller Form nicht machbar. Entweder Zeitrahmen verlaengern, Budget erhoehen oder Schnittstellendokumentation anfordern.

## Aufgabe 6
- **Machbarkeitsanalyse:** Prueft vor Projektstart, OB das Projekt umsetzbar ist (Ja/Nein-Entscheidung).
- **Risikoanalyse:** Identifiziert WAEHREND der Planung und Durchfuehrung moegliche Gefaehrdungen und plant Gegenmassnahmen.

## Aufgabe 7
**Risiko = Eintrittswahrscheinlichkeit x Schadenshoehe**
Beispiel: Serverausfall waehrend der Migration. Eintrittswahrscheinlichkeit: 20%. Schadenshoehe: 10.000 EUR. Risiko: 2.000 EUR.

## Aufgabe 8
| Risiko | Wahrscheinlichkeit | Schaden | Einstufung | Massnahme |
|--------|-------------------|---------|------------|-----------|
| Datenverlust bei Migration | Gering | Hoch | Mittel | Vollbackup vor Start |
| Ausfallzeit des Maildienstes | Mittel | Hoch | Hoch | Parallelbetrieb waehrend Migration |
| Inkompatibilitaet mit Clients | Mittel | Mittel | Mittel | Vorab-Tests mit allen Clients |

## Aufgabe 9
- **Vermeiden:** Auf veraltete, unsichere Software verzichten und Alternativprodukt waehlen
- **Vermindern:** RAID-System einsetzen, um Auswirkung eines Festplattenausfalls zu reduzieren
- **Uebertragen:** IT-Haftpflichtversicherung fuer Datenverlust abschliessen
- **Akzeptieren:** Geringes Risiko eines kurzen Netzwerkausfalls (< 5 Min.) dokumentieren, keine Massnahme

## Aufgabe 10
| Kostenart | Betrag |
|-----------|--------|
| Hardware (20 PCs a 650 EUR) | 13.000 EUR |
| Software-Lizenzen (20 x Office) | 3.000 EUR |
| Netzwerk (Kabel, Switch) | 2.000 EUR |
| Personal (5 Tage, 1 Techniker a 400 EUR/Tag) | 2.000 EUR |
| Risikozuschlag (10%) | 2.000 EUR |
| **Gesamt** | **22.000 EUR** |

## Aufgabe 11
Abweichung: (52.000 - 45.000) / 45.000 x 100 = **15,6%**
Moegliche Ursachen: (1) Personalkosten hoeher als geplant (Ueberstunden, zusaetzliche Mitarbeiter). (2) Ungeplante Zusatzanforderungen des Kunden (Scope Creep).

## Aufgabe 12
Die Nachkalkulation liefert wertvolle Daten fuer zukuenftige Projekte: Waren die Schaetzungen realistisch? Welche Kostenarten wurden ueber-/unterschaetzt? Auch bei Einhaltung des Budgets koennen Verschiebungen zwischen Kostenarten aufgetreten sein, die fuer die Kalkulation kuenftiger Projekte relevant sind.
