# Vertiefung und Uebungen: 1.5.02 – PDCA, KVP, Qualitaetsplanung

## Vergleich: PDCA-Phasen und QM-Konzepte

| QM-Konzept | PDCA-Phase | Zusammenhang |
|---|---|---|
| Qualitaetsplanung | Plan | Ziele und Massnahmen festlegen |
| Qualitaetslenkung | Do | Massnahmen operativ umsetzen |
| Qualitaetssicherung | Check | Ergebnisse pruefen und bewerten |
| Qualitaetsverbesserung | Act | Prozesse anpassen und standardisieren |

## PDCA in verschiedenen IT-Szenarien

| Szenario | Plan | Do | Check | Act |
|---|---|---|---|---|
| **Arbeitsplatz einrichten** | Checkliste erstellen | Installation durchfuehren | Testprotokoll pruefen | Fehler beheben |
| **Software-Release** | Testplan, Kriterien | Tests ausfuehren | Testergebnisse analysieren | Bugfixes / Freigabe |
| **Netzwerk-Monitoring** | Schwellwerte definieren | Monitoring aktivieren | Alarme auswerten | Kapazitaeten anpassen |

## Typische Pruefungsaspekte

1. **PDCA-Zuordnung:** Aktivitaeten den richtigen Phasen zuordnen
2. **KVP erklaeren:** Unterschied zwischen KVP und einmaliger Verbesserung
3. **Testprotokoll erstellen:** Pruefschritte fuer ein Szenario formulieren
4. **Ist-Soll-Vergleich:** Abweichungen erkennen und Massnahmen ableiten
5. **Qualitaetsziele:** SMART-Kriterien auf QM-Ziele anwenden

## Haeufige Fehler

| Fehler | Richtig |
|---|---|
| PDCA ist ein einmaliger Durchlauf | PDCA ist ein endloser Kreislauf |
| KVP = grosse Veraenderungen | KVP = kleine, stetige Verbesserungen |
| Qualitaetslenkung = Qualitaetsplanung | Lenkung = operative Umsetzung, Planung = strategische Festlegung |
| Testprotokoll nur bei Fehler erstellen | Testprotokoll wird IMMER erstellt (auch bei Erfolg) |

---

## Aufgabe 1
Ordne folgende Aktivitaeten den PDCA-Phasen zu:
a) Testabdeckung liegt bei 65% statt 80% → Ursachen analysieren
b) Unit-Tests automatisieren
c) Fehlerquote soll von 5% auf 2% gesenkt werden
d) Coding-Guidelines verbindlich einfuehren

## Aufgabe 2
Erstelle ein Testprotokoll (3-5 Pruefschritte) fuer die Einrichtung eines Remote-Arbeitsplatzes mit VPN-Zugang.

## Aufgabe 3
Ein IT-Team stellt fest, dass die durchschnittliche Reaktionszeit im First-Level-Support bei 45 Minuten liegt. Das Ziel ist 30 Minuten.
Beschreibe einen PDCA-Durchlauf fuer dieses Problem.

## Aufgabe 4
Erklaere den Unterschied zwischen KVP und PDCA. In welchem Verhaeltnis stehen sie zueinander?

---
---

## Loesung 1
a) **Check** – Ergebnisse mit Zielen vergleichen, Abweichung erkennen
b) **Do** – Geplante Massnahme umsetzen
c) **Plan** – Qualitaetsziel definieren
d) **Act** – Erfolgreiche Massnahme als Standard einfuehren

## Loesung 2

| Nr. | Pruefschritt | Erwartet | Ergebnis | Status |
|---|---|---|---|---|
| 1 | VPN-Client installiert | Client v3.2 vorhanden | v3.2 installiert | OK |
| 2 | VPN-Verbindung aufbauen | Verbindung zu Firmennetz | Verbunden, IP 10.0.1.x | OK |
| 3 | Internes Laufwerk erreichbar | \\\\server\\share oeffnet sich | Zugriff verweigert | NICHT OK |
| 4 | Videokonferenz-Tool | Teams-Anruf moeglich | Audio + Video funktioniert | OK |
| 5 | Drucken ueber VPN | Netzwerkdrucker erreichbar | Nicht verfuegbar | NICHT OK |

## Loesung 3
- **Plan:** Ist-Zustand = 45 Min., Soll = 30 Min. Massnahme: Wissensdatenbank aufbauen, haeufige Anfragen kategorisieren, Vorlagen erstellen
- **Do:** Wissensdatenbank implementieren, Team schulen, Vorlagen fuer Top-10-Anfragen erstellen
- **Check:** Nach 4 Wochen Reaktionszeit messen → z.B. 32 Min. Verbesserung, aber Ziel noch nicht erreicht
- **Act:** Zusaetzlich automatische Ticket-Zuweisung einfuehren, weitere Vorlagen ergaenzen → naechster PDCA-Zyklus

## Loesung 4
- **PDCA** ist ein konkretes Werkzeug/Methode – ein strukturierter Vierschritt-Prozess
- **KVP** ist eine Philosophie/Grundhaltung – die Ueberzeugung, dass staendige kleine Verbesserungen zu grossem Fortschritt fuehren
- Verhaeltnis: PDCA ist das wichtigste Werkzeug zur Umsetzung von KVP. KVP ist der Rahmen, PDCA die Methode.
