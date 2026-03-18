# Vertiefung: 1.4.07 – Programmierwerkzeuge

## Vergleich: UML-Diagrammtypen

| Kriterium | Use-Case-Diagramm | Klassendiagramm | Aktivitaetsdiagramm |
|---|---|---|---|
| **Typ** | Verhaltensdiagramm | Strukturdiagramm | Verhaltensdiagramm |
| **Zeigt** | WAS das System tut | WIE das System aufgebaut ist | WIE ein Ablauf funktioniert |
| **Akteure** | Ja (Strichmaennchen) | Nein | Nein |
| **Zeitlicher Ablauf** | Nein | Nein | Ja |
| **Klassen/Attribute** | Nein | Ja | Nein |
| **Einsatz** | Anforderungsanalyse | Design/Architektur | Prozessmodellierung |
| **Phase** | Analyse | Entwurf | Analyse + Entwurf |

## Vergleich: Pseudocode vs. Aktivitaetsdiagramm

| Kriterium | Pseudocode | Aktivitaetsdiagramm |
|---|---|---|
| **Darstellung** | Textbasiert | Grafisch |
| **Detailgrad** | Hoch (Variablen, Operationen) | Mittel (Ablauflogik) |
| **Geeignet fuer** | Algorithmen, einzelne Funktionen | Gesamtprozesse, parallele Ablaeufe |
| **Verstaendlich fuer** | Entwickler | Entwickler + Fachabteilung |
| **Parallelitaet** | Schwer darstellbar | Einfach (Synchronisationsbalken) |

## Vergleich: Fehlersuche in Code vs. Schreibtischtest

| Kriterium | Fehler in Code finden | Schreibtischtest |
|---|---|---|
| **Ziel** | Fehler identifizieren | Code-Ablauf nachvollziehen |
| **Methode** | Sichtpruefung, Analyse | Zeile-fuer-Zeile-Simulation |
| **Variablentabelle** | Optional | Zwingend |
| **Ergebnis** | Fehler + Korrekturvorschlag | Endergebnis der Ausfuehrung |
| **Pruefungsformat** | „Finde den Fehler" | „Was ist der Wert von x nach Zeile 5?" |

## Zusammenhaenge

```
Anforderungsanalyse (Use-Case) → Entwurf (Klassendiagramm + Aktivitaetsdiagramm)
                                     ↓
                                Pseudocode  → Schreibtischtest → Implementierung
                                     ↓
                              Fehlersuche / Debugging → Korrektur
```

- **Use-Case** definiert Anforderungen → daraus entstehen **Klassen** und **Ablaeufe**
- **Pseudocode** uebersetzt Ablaeufe in Algorithmen → mit **Schreibtischtest** verifizierbar
- **Bildschirmmasken** ergaenzen die Use-Cases um die Benutzerperspektive
- **Fehlersuche** ist sowohl beim Lesen fremden Codes als auch beim eigenen Debugging relevant

## Typische Pruefungsaspekte

1. **Pseudocode lesen & schreiben:** Algorithmus in Pseudocode umsetzen oder gegebenen Pseudocode interpretieren
2. **UML zeichnen & lesen:** Use-Case-Diagramm aus Beschreibung erstellen, Klassendiagramm vervollstaendigen
3. **Schreibtischtest durchfuehren:** Variablentabelle fuellen, Endwerte bestimmen
4. **Fehler im Code finden:** Syntax-, Laufzeit- und logische Fehler in gegebenem Code identifizieren
5. **Bildschirmmasken bewerten:** Softwareergonomie-Kriterien nach DIN EN ISO 9241 anwenden

## Haeufige Fehler

| Fehler | Richtig |
|---|---|
| Pseudocode mit konkreter Sprachsyntax schreiben | Pseudocode ist sprachunabhaengig |
| Use-Case mit Ablauf verwechseln | Use-Case zeigt Funktionen, NICHT den Ablauf |
| Klassendiagramm ohne Kardinalitaeten | Kardinalitaeten gehoeren zu jeder Assoziation |
| Schreibtischtest: Variablen nicht aktualisieren | Jede Zuweisung sofort in die Tabelle eintragen |
| Aktivitaetsdiagramm ohne Start-/Endknoten | Start (●) und Ende (◉) sind Pflicht |
| include/extend verwechseln | include = immer, extend = optional |
