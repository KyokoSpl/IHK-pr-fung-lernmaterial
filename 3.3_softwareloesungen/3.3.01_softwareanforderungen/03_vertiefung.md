# 3.3.01 – Vertiefung: Softwareanforderungen erfassen

## Vergleichstabelle: Qualitaetsmerkmale im Kontext

| Merkmal | Stakeholder | Pruefmethode | Typische Metrik |
|---------|------------|-------------|-----------------|
| Benutzbarkeit | Endbenutzer | Usability-Test, Befragung | SUS-Score, Task Completion Rate |
| Effizienz | Betreiber, Benutzer | Lasttest, Profiling | Response Time, Throughput |
| Funktionalitaet | Auftraggeber | Funktionstest, Abnahme | Testabdeckung, Fehlerrate |
| Normen | Compliance-Abteilung | Audit, Review | Normkonformitaetsgrad |
| Wartbarkeit | Entwickler | Code Review, Metriken | Zyklom. Komplexitaet, Coupling |
| Zuverlaessigkeit | Betreiber | Dauertest, Monitoring | MTBF, Verfuegbarkeit |
| Aenderbarkeit | Entwickler, PM | Architektur-Review | Change Impact, Modularitaet |
| Uebertragbarkeit | Betreiber | Installationstest | Plattformanzahl, Setupzeit |

---

## Anforderungen messbar formulieren (SMART)

Anforderungen muessen **messbar** sein, damit sie pruefbar werden:

| Schlecht (vage) | Gut (messbar) |
|----------------|---------------|
| "Das System soll schnell sein" | "Die Antwortzeit betraegt max. 2 Sekunden bei 1000 Nutzern" |
| "Einfache Bedienung" | "Ein neuer Benutzer kann die Kernaufgabe in < 5 Minuten erledigen" |
| "Hohe Verfuegbarkeit" | "Verfuegbarkeit >= 99,9% pro Monat (max. 43 Min. Downtime)" |
| "Sicher" | "Authentifizierung per 2FA, Verschluesselung mit AES-256" |
| "Wartbar" | "Zyklomatische Komplexitaet pro Methode < 10" |

**SMART-Kriterien fuer Anforderungen**:
- **S**pezifisch – klar und eindeutig formuliert
- **M**essbar – quantifizierbar mit Metriken
- **A**kzeptiert – vom Stakeholder abgenommen
- **R**ealistisch – technisch umsetzbar
- **T**erminiert – zeitlich eingrenzbar

---

## Anforderungsdokument: Aufbau

```
Anforderungsspezifikation
├── 1. Einleitung
│   ├── Zweck
│   ├── Geltungsbereich
│   └── Definitionen
├── 2. Allgemeine Beschreibung
│   ├── Produktperspektive
│   ├── Produktfunktionen (Ueberblick)
│   └── Benutzergruppen
├── 3. Funktionale Anforderungen
│   ├── FA-001: Benutzerregistrierung
│   ├── FA-002: Login
│   └── ...
├── 4. Nicht-funktionale Anforderungen
│   ├── NFA-001: Performance
│   ├── NFA-002: Sicherheit
│   └── ...
└── 5. Abnahmekriterien
```

---

## Pruefungsaspekte

### Typische Fragestellungen

1. **Zuordnungsaufgaben**: "Ordnen Sie die folgenden Anforderungen den Qualitaetsmerkmalen zu"
2. **Bewertungsaufgaben**: "Bewerten Sie, ob die Anforderung messbar formuliert ist"
3. **Lueckentexte**: ISO 25010 Merkmale vervollstaendigen
4. **Szenarien**: "Welches Qualitaetsmerkmal ist in folgendem Fall betroffen?"

### Haeufige Fehler in der Pruefung

| Fehler | Korrektur |
|--------|-----------|
| Funktionale mit nicht-funktionalen Anforderungen verwechseln | Funktional = WAS, Nicht-funktional = WIE GUT |
| Effizienz und Effektivitaet verwechseln | Effizienz = mit wenig Ressourcen, Effektivitaet = Ziel erreichen |
| Wartbarkeit und Aenderbarkeit gleichsetzen | Wartbarkeit ist der Oberbegriff (ISO 25010), Aenderbarkeit ein Aspekt |
| Zuverlaessigkeit nur als "laeuft ohne Fehler" verstehen | Umfasst auch Fehlertoleranz und Wiederherstellbarkeit |
| Benutzbarkeit mit "schoenem Design" gleichsetzen | Umfasst Erlernbarkeit, Bedienbarkeit, Barrierefreiheit etc. |

---

## Zusammenhang: Qualitaetszielkonflikte

Qualitaetsmerkmale koennen in Konflikt stehen:

```
Effizienz <──────────> Wartbarkeit
  (optimierter Code)     (lesbarer Code)

Sicherheit <─────────> Benutzbarkeit
  (strenge Kontrollen)   (einfache Bedienung)

Funktionalitaet <────> Effizienz
  (viele Features)       (schlankes System)

Uebertragbarkeit <───> Effizienz
  (plattformunabhaengig) (plattformoptimiert)
```

**Pruefungsrelevant**: Man muss Trade-offs erkennen und begruenden koennen, warum man sich fuer ein Merkmal auf Kosten eines anderen entscheidet.

---

## Anforderungserfassung: Methoden

| Methode | Beschreibung | Geeignet fuer |
|---------|-------------|---------------|
| Interview | Direktes Gespraech mit Stakeholdern | Detaillierte funktionale Anforderungen |
| Workshop | Gemeinsame Erarbeitung in Gruppen | Komplexe Systeme, viele Stakeholder |
| Fragebogen | Strukturierte schriftliche Erhebung | Grosse Benutzergruppen |
| Beobachtung | Benutzer bei Arbeit beobachten | Benutzbarkeitsanforderungen |
| Prototyping | Fruehe Modelle zum Testen | UI-Anforderungen, Feedback |
| Dokumentenanalyse | Bestehende Dokumente auswerten | Normen, Altsysteme |
