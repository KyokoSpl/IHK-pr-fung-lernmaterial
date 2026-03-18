# Grundlagen: 3.4.03 – Strukturierte Analyse- und Designverfahren

## Bottom-up-Entwurf

**Definition:** Beim Bottom-up-Entwurf werden zuerst die kleinsten Bausteine (elementare Module, Funktionen) entwickelt und anschliessend schrittweise zu groesseren Einheiten zusammengesetzt.

**Kernaussagen:**
- Start bei den Detailkomponenten, dann Zusammenbau zum Gesamtsystem
- Gut geeignet, wenn wiederverwendbare Bausteine bereits vorhanden sind
- Einzelne Module koennen frueh getestet werden
- Risiko: Das Gesamtergebnis passt moeglicherweise nicht zusammen

**Wichtige Begriffe:**
- **Modul** – in sich geschlossene Einheit mit definierter Aufgabe
- **Wiederverwendung** – bestehende Module in neuen Kontexten einsetzen
- **Integration** – Zusammenfuegen von Modulen zu einem groesseren System

**Erklaerung:** Beispiel: Ein Entwickler baut zuerst eine Login-Komponente, eine Datenbankzugriffs-Schicht und eine PDF-Export-Funktion. Anschliessend werden diese Module zu einer Anwendung zusammengefuegt.

---

## Modularisierung

**Definition:** Modularisierung ist das Prinzip, ein Softwaresystem in voneinander unabhaengige, austauschbare Module zu zerlegen, die ueber klar definierte Schnittstellen kommunizieren.

**Kernaussagen:**
- Jedes Modul erfuellt genau eine klar abgegrenzte Aufgabe
- Module sind ueber Schnittstellen (Interfaces) verbunden
- Aenderungen in einem Modul sollen keine Auswirkungen auf andere Module haben
- Zwei zentrale Qualitaetsmerkmale: **Kohaesion** und **Kopplung**

**Kohaesion und Kopplung:**

| Eigenschaft | Definition | Ziel |
|------------|-----------|------|
| Kohaesion | Wie stark die Bestandteile eines Moduls inhaltlich zusammengehoeren | Hoch (alles in einem Modul gehoert thematisch zusammen) |
| Kopplung | Wie stark Module voneinander abhaengig sind | Niedrig (Module sollen unabhaengig sein) |

**Vorteile der Modularisierung:**
- Bessere Wartbarkeit (Fehler lokal beheben)
- Bessere Testbarkeit (Module einzeln testbar)
- Bessere Wiederverwendbarkeit (Module in anderen Projekten nutzbar)
- Arbeitsteilung im Team (jedes Teammitglied bearbeitet ein Modul)

**Wichtige Begriffe:**
- **Schnittstelle (Interface)** – definierter Ein-/Ausgabekanal zwischen Modulen
- **Information Hiding** – interne Details eines Moduls sind von aussen nicht sichtbar
- **Separation of Concerns** – Trennung von Zustaendigkeiten

---

## Top-down-Entwurf

**Definition:** Beim Top-down-Entwurf wird das Gesamtsystem als Ganzes betrachtet und schrittweise in immer kleinere Teilsysteme und Module zerlegt (Divide and Conquer).

**Kernaussagen:**
- Start beim Gesamtproblem, dann Zerlegung in Teilprobleme
- Hierarchische Struktur: Hauptprogramm → Unterprogramme → Einzelfunktionen
- Gut geeignet fuer komplett neue Systeme ohne bestehende Bausteine
- Fruehe Sicht auf die Gesamtarchitektur

**Wichtige Begriffe:**
- **Divide and Conquer** – Teile und Herrsche: Problem in Teilprobleme zerlegen
- **Verfeinerung** – schrittweise Detaillierung der Loesung
- **Hierarchie** – Ober-/Unterordnung der Module

**Erklaerung:** Beispiel: Ein Projektleiter plant ein ERP-System. Zuerst wird das Gesamtsystem in Module aufgeteilt: Lagerverwaltung, Buchhaltung, Personalverwaltung. Dann wird jedes Modul weiter zerlegt, z.B. Lagerverwaltung in: Wareneingang, Warenausgang, Bestandsfuehrung.

```
          Gesamtsystem (ERP)
         /        |         \
   Lager      Buchhaltung    Personal
   /   \        /    \        /    \
Eingang Ausgang Debit  Kredit Stamm  Gehalt
```
