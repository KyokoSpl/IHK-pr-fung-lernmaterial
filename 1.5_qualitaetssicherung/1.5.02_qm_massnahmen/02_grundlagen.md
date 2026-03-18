# Grundlagen: 1.5.02 – PDCA, KVP, Qualitaetsplanung

## PDCA-Zyklus (Deming-Kreislauf)

**Definition:** Der PDCA-Zyklus ist ein iterativer vierstufiger Managementprozess zur kontinuierlichen Verbesserung von Produkten, Dienstleistungen und Prozessen.

| Phase | Bedeutung | Beschreibung | IT-Beispiel |
|---|---|---|---|
| **Plan** | Planen | Problem analysieren, Ziel definieren, Massnahmen planen | Testplan fuer neue Software erstellen |
| **Do** | Umsetzen | Geplante Massnahmen ausfuehren (ggf. im kleinen Rahmen) | Tests durchfuehren, Software installieren |
| **Check** | Pruefen | Ergebnisse mit Zielen vergleichen, Abweichungen erkennen | Testergebnisse auswerten, Soll-Ist-Vergleich |
| **Act** | Handeln | Bei Erfolg: standardisieren. Bei Misserfolg: Korrektur und neuer Zyklus | Prozess anpassen, Dokumentation aktualisieren |

**Kernprinzip:** Nach Act beginnt der Zyklus erneut → Endlosschleife der Verbesserung

```
    ┌──────┐
    │ PLAN │ → Ziel definieren, Massnahmen planen
    └──┬───┘
       ↓
    ┌──────┐
    │  DO  │ → Massnahmen umsetzen
    └──┬───┘
       ↓
    ┌──────┐
    │CHECK │ → Ergebnis pruefen
    └──┬───┘
       ↓
    ┌──────┐
    │ ACT  │ → Standardisieren oder korrigieren
    └──┬───┘
       ↓
    (zurueck zu PLAN)
```

**KVP – Kontinuierlicher Verbesserungsprozess:**
- Philosophie, die auf staendiger, schrittweiser Verbesserung basiert
- PDCA ist das Werkzeug, KVP ist die Denkweise
- Alle Mitarbeiter sind einbezogen (Bottom-up)
- Kleine Verbesserungen statt grosser Umbrueche

---

## Qualitaetslenkung

**Definition:** Qualitaetslenkung umfasst die operativen Taetigkeiten, die zur Erfuellung der Qualitaetsanforderungen eingesetzt werden – also die Umsetzung der Planungsphase.

**Massnahmen der Qualitaetslenkung in der IT:**

| Massnahme | Beschreibung |
|---|---|
| Code-Review | Manuelle Pruefung des Quellcodes durch Kollegen |
| Unit-Tests | Automatisierte Tests einzelner Programmeinheiten |
| Integrationstests | Testen des Zusammenspiels von Komponenten |
| Abnahmetests | Pruefung gegen Kundenanforderungen |
| Checklisten | Strukturierte Pruefung anhand vordefinierter Kriterien |
| Coding-Guidelines | Verbindliche Regeln fuer Code-Stil und -Struktur |

---

## Qualitaetsplanung und Qualitaetsziele

**Definition:** Qualitaetsplanung ist das Festlegen der Qualitaetsmerkmale, -anforderungen und der Prozesse zu deren Erreichung.

**Vorgehen:**
1. **Ist-Zustand ermitteln:** Aktuelle Qualitaet messen (z.B. Fehlerquote, Kundenzufriedenheit)
2. **Soll-Zustand festlegen:** Qualitaetsziele definieren (SMART-Kriterien!)
3. **Massnahmen planen:** Welche Aktivitaeten fuehren zum Ziel?
4. **Ressourcen zuweisen:** Personal, Zeit, Budget
5. **Messgroessen definieren:** Wie wird die Zielerreichung gemessen?

**Beispiel IT-Qualitaetsziele:**
- Fehlerquote in Produktion < 2% (messbar)
- Reaktionszeit First-Level-Support < 30 Minuten (zeitgebunden)
- Testabdeckung > 80% (spezifisch)

---

## Testprotokoll fuer Arbeitsplatzeinrichtung

**Definition:** Ein Testprotokoll dokumentiert systematisch alle Pruefschritte bei der Einrichtung eines Arbeitsplatzes und deren Ergebnisse.

**Inhalt eines Testprotokolls:**

| Feld | Beschreibung |
|---|---|
| Datum/Uhrzeit | Wann wurde getestet? |
| Pruefer | Wer hat getestet? |
| Pruefgegenstand | Was wurde getestet? (z.B. „Arbeitsplatz IT-03") |
| Pruefschritt | Einzelne Testschritte nummeriert |
| Erwartetes Ergebnis | Was soll passieren? |
| Tatsaechliches Ergebnis | Was ist passiert? |
| Status | OK / NICHT OK / TEILWEISE |
| Bemerkung | Abweichungen, Massnahmen |

**Beispiel-Testprotokoll Arbeitsplatz:**

| Nr. | Pruefschritt | Erwartet | Ergebnis | Status |
|---|---|---|---|---|
| 1 | PC startet | Boot in < 60s | 45s | OK |
| 2 | Netzwerkverbindung | IP via DHCP | 192.168.1.105 | OK |
| 3 | Drucker erreichbar | Testseite druckt | Drucker offline | NICHT OK |
| 4 | Software installiert | Office, Browser | Office fehlt | NICHT OK |
| 5 | Benutzer-Login | AD-Anmeldung | Erfolgreich | OK |
