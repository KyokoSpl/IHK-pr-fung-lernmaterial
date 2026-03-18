# Vertiefung und Uebungen: 4.2.05 – Ziele von Betrieben und Unternehmen

## Vertiefung

### Kennzahlen im Vergleich

| Kennzahl | Formel | Bezug | Einheit | Aussage |
|----------|--------|-------|---------|---------|
| Produktivitaet | Output / Input | Menge | Stueck/Stunde | Wie effizient werden Ressourcen eingesetzt? |
| Wirtschaftlichkeit | Ertrag / Aufwand | Wert (EUR) | Faktor (z.B. 1,2) | Arbeitet das Unternehmen gewinnbringend? |
| Rentabilitaet | Gewinn / Kapital × 100 | Wert (EUR) | Prozent (%) | Wie gut verzinst sich das eingesetzte Kapital? |

### Berechnungsbeispiel – Komplett

**Ausgangslage:** Ein IT-Unternehmen im Geschaeftsjahr 2025:
- 5 Entwickler arbeiten je 1.600 Stunden/Jahr = 8.000 Stunden gesamt
- Es werden 40 Softwareprojekte abgeschlossen
- Ertrag (Umsatz): 800.000 EUR
- Aufwand (Kosten): 650.000 EUR
- Gewinn: 150.000 EUR
- Eigenkapital: 500.000 EUR

**Berechnung:**

```
Arbeitsproduktivitaet = 40 Projekte / 8.000 Stunden = 0,005 Projekte/Stunde
                      = 1 Projekt pro 200 Arbeitsstunden

Wirtschaftlichkeit    = 800.000 / 650.000 = 1,23 (> 1 → wirtschaftlich)

Eigenkapitalrent.     = (150.000 / 500.000) × 100 = 30 %

Umsatzrentabilitaet   = (150.000 / 800.000) × 100 = 18,75 %
```

### Minimal- und Maximalprinzip in der IT

| Prinzip | IT-Beispiel | Erklaerung |
|---------|------------|-----------|
| Maximalprinzip | Budget: 20.000 EUR → moeglichst leistungsfaehigen Server kaufen | Mit festem Budget das beste Ergebnis erzielen |
| Minimalprinzip | Anforderung: 99,9 % Uptime → guenstigste Loesung finden | Definiertes Ziel mit geringstem Aufwand erreichen |
| Optimalprinzip | Beste Balance aus Serverleistung, Kosten und Wartungsaufwand | Bestes Verhaeltnis von Leistung zu Kosten |

### Zielkonflikte visualisiert

```
Typische Zielkonflikte in IT-Unternehmen:

  Kosten senken  ◄──────────────────►  Qualitaet steigern
       ↑                                      ↑
       |         ZIELKONFLIKT                  |
       |                                       |
  Weniger Tests  ◄──── widerspricht ────►  Mehr Tests
  Billige HW     ◄──── widerspricht ────►  Hochverfuegbar
  Outsourcing    ◄──── widerspricht ────►  Kontrolle/Sicherheit

Zielharmonie:
  Mitarbeiterschulung → Produktivitaet steigt → Gewinn steigt ✓
  Automatisierung → Fehler sinken → Kundenzufriedenheit steigt ✓
```

### Typische Pruefungsaspekte
- Berechnungsaufgaben: Produktivitaet, Wirtschaftlichkeit, Rentabilitaet
- Zuordnung eines Szenarios zum richtigen Prinzip (Minimal/Maximal)
- Identifikation von Zielkonflikten in einem Unternehmensszenario
- Vorschlaege zur Loesung von Zielkonflikten

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| Produktivitaet mit EUR berechnet | Produktivitaet ist MENGENBEZOGEN (Stueck/Stunden) |
| Wirtschaftlichkeit in % angegeben | Wirtschaftlichkeit ist ein FAKTOR (z.B. 1,2), keine Prozentzahl |
| Rentabilitaet ohne × 100 | Rentabilitaet wird immer in % angegeben → × 100 nicht vergessen |
| Umsatz = Gewinn | Umsatz = Gesamteinnahmen; Gewinn = Umsatz – Kosten |
| Minimalprinzip: wenig Leistung | Minimalprinzip: GLEICHE Leistung mit WENIGER Aufwand |

---

## Uebungen

**Aufgabe 1:** Berechne die Arbeitsproduktivitaet:
- Ein Helpdesk-Team (4 Mitarbeiter) bearbeitet 480 Tickets pro Woche.
- Jeder Mitarbeiter arbeitet 40 Stunden pro Woche.
- Wie viele Tickets bearbeitet ein Mitarbeiter pro Stunde?

**Aufgabe 2:** Berechne die Wirtschaftlichkeit:
- Ein IT-Projekt hat Kosten (Aufwand) von 85.000 EUR.
- Der Ertrag betraegt 102.000 EUR.
- Ist das Projekt wirtschaftlich? Begruende.

**Aufgabe 3:** Berechne die Rentabilitaet:
- Ein IT-Unternehmen hat ein Eigenkapital von 300.000 EUR.
- Der Jahresgewinn betraegt 45.000 EUR.
- Der Umsatz betraegt 600.000 EUR.
- Berechne Eigenkapitalrentabilitaet und Umsatzrentabilitaet.

**Aufgabe 4:** Ordne die folgenden Szenarien dem Minimal- oder Maximalprinzip zu:
- a) Ein Unternehmen hat ein IT-Budget von 100.000 EUR und moechte damit die bestmoegliche Serverinfrastruktur aufbauen.
- b) Ein Projekt muss eine Webanwendung mit exakt 10 Funktionen liefern. Das Team sucht nach der kostenguenstigsten Umsetzung.
- c) Mit 5 Entwicklern soll in 3 Monaten moeglichst viel Software produziert werden.

**Aufgabe 5:** Nenne drei typische Zielkonflikte in einem IT-Unternehmen und beschreibe jeweils, wie der Konflikt geloest oder abgemildert werden koennte.

**Aufgabe 6:** Ein IT-Unternehmen hat folgende Kennzahlen:
- Jahr 1: Produktivitaet 5 Projekte/MA, Wirtschaftlichkeit 1,15, EK-Rentabilitaet 12 %
- Jahr 2: Produktivitaet 6 Projekte/MA, Wirtschaftlichkeit 1,08, EK-Rentabilitaet 10 %

Interpretiere die Entwicklung: Was hat sich verbessert, was verschlechtert?

---
---

# Loesungen

## Aufgabe 1
- Gesamt-Arbeitsstunden: 4 MA × 40 Std. = 160 Stunden
- Arbeitsproduktivitaet: 480 Tickets / 160 Stunden = **3 Tickets pro Stunde**
- Pro Mitarbeiter: 480 / 4 = 120 Tickets pro Woche = **3 Tickets pro Stunde**

## Aufgabe 2
- Wirtschaftlichkeit = 102.000 / 85.000 = **1,2**
- Das Projekt ist **wirtschaftlich**, da der Wert groesser als 1 ist.
- Der Ertrag uebersteigt den Aufwand um 20 % (Gewinn: 17.000 EUR).

## Aufgabe 3
- Eigenkapitalrentabilitaet = (45.000 / 300.000) × 100 = **15 %**
- Umsatzrentabilitaet = (45.000 / 600.000) × 100 = **7,5 %**
- Interpretation: Pro eingesetztem Euro Eigenkapital wurden 15 Cent Gewinn erzielt. Pro Euro Umsatz blieben 7,5 Cent Gewinn uebrig.

## Aufgabe 4
- a) **Maximalprinzip** – Gegebene Mittel (100.000 EUR), bestmoegliches Ergebnis
- b) **Minimalprinzip** – Gegebenes Ziel (10 Funktionen), geringster Mitteleinsatz
- c) **Maximalprinzip** – Gegebene Mittel (5 Entwickler, 3 Monate), maximaler Output

## Aufgabe 5
1. **Sicherheit vs. Benutzerfreundlichkeit:** Strenge Passwortregeln frustrieren Nutzer. Loesung: Single Sign-On (SSO) mit starker Authentifizierung – sicher UND bequem.
2. **Kosten vs. Qualitaet:** Guenstige Hardware fuehrt zu Ausfaellen. Loesung: Total Cost of Ownership (TCO) berechnen – billig ist langfristig oft teurer.
3. **Time-to-Market vs. Testabdeckung:** Schnelles Release vernachlaessigt Tests. Loesung: Automatisierte Tests (CI/CD) ermoeglichen schnelle Releases bei hoher Testabdeckung.

## Aufgabe 6
- **Produktivitaet gestiegen** (5 → 6 Projekte/MA): Mehr Output pro Mitarbeiter → effizienteres Arbeiten.
- **Wirtschaftlichkeit gesunken** (1,15 → 1,08): Das Verhaeltnis von Ertrag zu Aufwand ist schlechter geworden → die Kosten sind staerker gestiegen als die Ertraege.
- **Rentabilitaet gesunken** (12 % → 10 %): Weniger Gewinn pro eingesetztem Eigenkapital → trotz hoeherer Produktivitaet sinkt der Gewinn (moeglicherweise durch gestiegene Kosten oder Preisdruck).
- **Fazit:** Hoehere Produktivitaet allein reicht nicht aus, wenn gleichzeitig die Kosten steigen oder die Preise sinken. Alle drei Kennzahlen muessen zusammen betrachtet werden.
