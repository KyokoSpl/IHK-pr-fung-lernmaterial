# Beispiele: 1.1.01 – Merkmale und Methoden des Projektmanagements

## Merkmale eines Projektes

**Beispiel 1:** Ein mittelstaendisches Unternehmen entscheidet, seine gesamte IT-Infrastruktur auf Cloud-Dienste zu migrieren. Es wird ein Projektteam gebildet, ein Budget von 150.000 EUR festgelegt und ein Zeitrahmen von 8 Monaten definiert. → Einmaligkeit, zeitliche Begrenzung, begrenztes Budget, eigene Organisation = **Projekt**.

**Beispiel 2:** Die IT-Abteilung fuehrt jeden Freitag eine Datensicherung aller Server durch. Der Ablauf ist dokumentiert und wiederholt sich woechentlich. → Wiederkehrend, kein definiertes Ende = **Routineaufgabe**, kein Projekt.

---

## Phasen der Teambildung

**Beispiel 1 – Forming:** Ein neues Entwicklungsteam wird zusammengestellt. Die Mitglieder kennen sich nicht, verhalten sich hoeflich und zurueckhaltend. Jeder wartet ab, welche Aufgaben er bekommt. → Typisch fuer die **Forming-Phase**.

**Beispiel 2 – Storming:** Nach zwei Wochen entsteht Streit darueber, wer die Datenbankarchitektur verantwortet. Zwei Entwickler beanspruchen die Rolle. Der Projektleiter muss moderieren und Zustaendigkeiten klar verteilen. → Typisch fuer die **Storming-Phase**.

**Beispiel 3 – Performing:** Nach einem Monat arbeitet das Team eigenstaendig. Aufgaben werden ohne Konflikte verteilt, die Kommunikation ist offen und konstruktiv. → Typisch fuer die **Performing-Phase**.

---

## Projektphasen: Wasserfallmodell vs. SCRUM

**Beispiel 1 – Wasserfallmodell:** Ein Kunde beauftragt die Entwicklung einer Verwaltungssoftware fuer eine Behoerde. Die Anforderungen sind durch gesetzliche Vorgaben exakt definiert und aendern sich nicht. Das Projekt durchlaeuft die Phasen: Anforderungsanalyse → Entwurf → Implementierung → Test → Auslieferung → Wartung. → **Wasserfallmodell** geeignet, da Anforderungen stabil und vollstaendig.

**Beispiel 2 – SCRUM:** Ein Start-up entwickelt eine Fitness-App. Die Zielgruppe ist noch nicht klar definiert, Features sollen basierend auf Nutzerfeedback angepasst werden. In 2-Wochen-Sprints werden Funktionen entwickelt, getestet und dem Product Owner vorgestellt. → **SCRUM** geeignet, da Anforderungen sich laufend aendern.

---

## Projektplanung: Netzplan

**Beispiel 1 – Netzplanberechnung:**

Gegeben:

| Vorgang | Dauer (Tage) | Vorgaenger |
|---------|-------------|------------|
| A | 3 | – |
| B | 5 | A |
| C | 2 | A |
| D | 4 | B, C |

**Vorwaertsrechnung:**
- A: FA=0, FE=3
- B: FA=3, FE=8
- C: FA=3, FE=5
- D: FA=8 (max(FE_B, FE_C) = max(8,5) = 8), FE=12

**Rueckwaertsrechnung:**
- D: SE=12, SA=8
- B: SE=8, SA=3 → GP=0 → **kritisch**
- C: SE=8, SA=6 → GP=3
- A: SE=3, SA=0 → GP=0 → **kritisch**

**Kritischer Weg:** A → B → D (Dauer: 12 Tage)
**Pufferzeit von C:** 3 Tage

**Beispiel 2 – SMART-Ziel:**
- Schlecht: "Die neue Software soll schnell fertig werden."
- **SMART:** "Die Buchhaltungssoftware soll bis zum 30.06. funktionsfaehig fuer die Abteilungen Personal und Finanzen bereitgestellt werden. Das Budget betraegt 50.000 EUR."
  - **S**pezifisch: Buchhaltungssoftware fuer zwei Abteilungen
  - **M**essbar: Funktionsfaehigkeit pruefbar durch Abnahmetest
  - **A**kzeptiert: Auftraggeber hat das Ziel freigegeben
  - **R**ealistisch: Budget und Zeitrahmen wurden geprueft
  - **T**erminiert: Deadline 30.06.

---

## Reflektionsmethoden

**Beispiel 1 – Lessons Learned:** Nach Abschluss eines Migrationsprojekts stellt das Team fest: Die Testphase war zu kurz geplant, Fehler traten erst im Livebetrieb auf. Dokumentierte Erkenntnis: "Fuer kuenftige Projekte wird die Testphase auf mindestens 20 % der Gesamtprojektdauer ausgeweitet." → Wissen wird fuer Folgeprojekte gesichert.

**Beispiel 2 – Feedback-Kultur:** Im woechentlichen Teammeeting gibt die Projektleiterin jedem Teammitglied kurzes Feedback: "Deine Dokumentation zum API-Entwurf war sehr verstaendlich. Beim naechsten Mal waere es hilfreich, die Fehlercodes mit aufzunehmen." → Konkret, zeitnah, konstruktiv.
