# Beispiele: 4.1.12 – Arbeitstechniken

## Beispiel 1: Eisenhower-Matrix anwenden

**Szenario:** Du bist Fachinformatiker in einem mittelstaendischen Unternehmen. Folgende Aufgaben liegen an einem Montag vor:

1. Der Fileserver ist ausgefallen – Mitarbeiter koennen nicht arbeiten
2. Du sollst bis Freitag einen Projektbericht fertigstellen
3. Ein Kollege bittet dich, ihm beim Drucker-Problem zu helfen
4. Du scrollst durch Social-Media-Nachrichten auf dem Handy

**Einordnung in die Eisenhower-Matrix:**

| Quadrant | Aufgabe | Begruendung |
|----------|---------|-------------|
| A (dringend + wichtig) | 1. Fileserver ausgefallen | Geschaeftskritisch, sofort handeln |
| B (wichtig + nicht dringend) | 2. Projektbericht bis Freitag | Wichtig, aber noch Zeit → terminieren |
| C (dringend + nicht wichtig) | 3. Drucker-Problem | Nicht deine Kernaufgabe → delegieren |
| D (weder dringend noch wichtig) | 4. Social Media | Zeitfresser → eliminieren |

---

## Beispiel 2: Kanban-Board fuer ein Azubi-Projekt

**Szenario:** Du erstellst als Abschlussprojekt eine Webanwendung. Du organisierst deine Aufgaben mit einem Kanban-Board.

```
+------------------+------------------+------------------+------------------+
|     BACKLOG      |   IN PROGRESS    |     REVIEW       |      DONE        |
|                  |   (WIP: max. 2)  |                  |                  |
+------------------+------------------+------------------+------------------+
| Login-Seite      | Datenbank-Schema | Projektdoku      | Anforderungs-    |
| erstellen        | erstellen        | pruefen lassen   | analyse          |
|                  |                  |                  |                  |
| REST-API         | Frontend-Design  |                  | Projekt-Setup    |
| implementieren   | umsetzen         |                  | (Git, IDE)       |
|                  |                  |                  |                  |
| Tests schreiben  |                  |                  |                  |
+------------------+------------------+------------------+------------------+
```

**WIP-Limit = 2:** Maximal zwei Aufgaben gleichzeitig in "In Progress", um Fokus zu behalten und Multitasking zu vermeiden.

---

## Beispiel 3: ALPEN-Methode fuer einen Arbeitstag

**Szenario:** Dein Arbeitstag als Fachinformatiker (8 Stunden = 480 Minuten):

**A – Aufgaben notieren:**
1. Server-Update durchfuehren
2. Ticket #247 (Fehlerbehebung) bearbeiten
3. Dokumentation aktualisieren
4. Meeting mit Projektleiter
5. E-Mails beantworten

**L – Laenge schaetzen:**
| Aufgabe | Geschaetzte Dauer |
|---------|------------------|
| Server-Update | 90 min |
| Ticket #247 | 120 min |
| Dokumentation | 60 min |
| Meeting | 30 min |
| E-Mails | 30 min |
| **Summe** | **330 min** |

**P – Pufferzeit:**
60 % geplant (330 min) + 40 % Puffer (220 min) = 550 min → Passt nicht ganz, also Aufgaben priorisieren.

**E – Entscheidungen (Prioritaeten):**
1. Server-Update (A – dringend + wichtig)
2. Ticket #247 (A – dringend + wichtig)
3. Meeting (fester Termin)
4. E-Mails (C – delegierbar)
5. Dokumentation (B – wichtig, aber nicht dringend → auf morgen verschieben)

**N – Nachkontrolle (Tagesende):**
Was wurde geschafft? Was wurde verschoben? → In den naechsten Tag uebernehmen.

---

## Beispiel 4: Quellenbewertung

**Szenario:** Du recherchierst zum Thema "Containerisierung mit Docker" und findest folgende Quellen:

| Quelle | Aktualitaet | Serioesitaet | Relevanz | Bewertung |
|--------|------------|-------------|---------|-----------|
| Docker offizielle Docs (docs.docker.com) | Aktuell | Hoch (Hersteller) | Hoch | ✔ Sehr gut |
| Blog-Artikel von 2018 | Veraltet | Mittel (privater Blog) | Mittel | ⚠ Vorsicht, pruefen |
| c't-Artikel von 2025 | Aktuell | Hoch (Fachzeitschrift) | Hoch | ✔ Gut |
| Wikipedia-Artikel | Aktuell | Mittel (Community) | Einstieg | ⚠ Fuer Ueberblick ok |
| YouTube-Tutorial ohne Quellenangabe | Unklar | Gering | Unklar | ✘ Kritisch pruefen |

→ Bevorzuge immer offizielle Dokumentationen und Fachzeitschriften. Pruefe Datum und Autor.

---

## Beispiel 5: Praesentationstechnik

**Szenario:** Du praesentierst dein Abschlussprojekt vor dem IHK-Pruefungsausschuss (15 Minuten).

**Struktur:**
1. **Einleitung (2 min):** Vorstellung, Projektname, Kurzbeschreibung
2. **Hauptteil (10 min):**
   - Ausgangssituation und Ziel (IST/SOLL)
   - Planung (Gantt, Ressourcen, Kosten)
   - Umsetzung (Technologien, Architektur, Code-Ausschnitte)
   - Testergebnisse
3. **Schluss (3 min):** Fazit, Soll/Ist-Vergleich, Ausblick

**Tipps:**
- Maximal 10–12 Folien
- Keine Textwaende – Stichworte und Visualisierungen
- Live-Demo nur, wenn Rueckfallplan vorhanden (Screenshots)
- Zeitmanagement: Vorher mehrfach proben
- Blickkontakt mit allen Pruefern halten
