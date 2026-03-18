# Grundlagen: 3.1.09 – Risiken identifizieren, Massnahmen planen

## MTBF / AFR

**Definition MTBF:** Die Mean Time Between Failures (MTBF) gibt die durchschnittliche Betriebszeit in Stunden an, die eine Komponente zwischen zwei aufeinanderfolgenden Ausfaellen ohne Unterbrechung laeuft.

**Definition AFR:** Die Annualized Failure Rate (AFR) gibt die Wahrscheinlichkeit in Prozent an, dass eine Komponente innerhalb eines Jahres ausfaellt.

**Formeln:**

```
MTBF = Gesamtbetriebszeit / Anzahl der Ausfaelle

AFR = 1 - e^(-8.760 / MTBF)    (exakte Formel)

AFR ≈ 8.760 / MTBF * 100 %     (Naeherung fuer hohe MTBF-Werte)
```

Hinweis: 8.760 = Stunden pro Jahr (365 * 24)

**Typische MTBF-Werte:**

| Komponente | Typische MTBF | AFR (ca.) |
|---|---|---|
| Enterprise-Festplatte (HDD) | 1.200.000 h | 0,73 % |
| Desktop-Festplatte (HDD) | 300.000 h | 2,92 % |
| SSD (Enterprise) | 2.000.000 h | 0,44 % |
| Server-Netzteil | 100.000 h | 8,76 % |
| Server (gesamt) | 50.000–100.000 h | 8,76–17,52 % |

**Wichtige Begriffe:**
- **MTBF (Mean Time Between Failures)** – mittlere Betriebszeit zwischen Ausfaellen
- **MTTR (Mean Time To Repair)** – mittlere Reparaturzeit
- **MTTF (Mean Time To Failure)** – mittlere Betriebszeit bis zum ersten Ausfall (bei nicht reparierbaren Teilen)
- **AFR (Annualized Failure Rate)** – jaehrliche Ausfallrate

**Zusammenhang MTBF, MTTR und Verfuegbarkeit:**

```
Verfuegbarkeit = MTBF / (MTBF + MTTR)
```

**Erklaerung:** Eine hohe MTBF allein garantiert keine hohe Verfuegbarkeit. Wichtig ist auch, wie schnell repariert wird (MTTR). Ist die MTTR niedrig, bleibt die Verfuegbarkeit hoch, selbst wenn die MTBF nicht extrem hoch ist.

---

## Notfallkonzept (Disaster Recovery)

**Definition:** Ein Disaster-Recovery-Plan (DRP) ist ein dokumentierter Prozess, der beschreibt, wie der IT-Betrieb nach einem schwerwiegenden Stoerfall wiederhergestellt wird.

**Kernaussagen:**
- Ziel: Minimierung von Datenverlust und Ausfallzeit
- Bestandteil des Business Continuity Management (BCM)
- Muss regelmaessig getestet und aktualisiert werden

**Zentrale Kenngroessen:**

| Kenngroesse | Definition | Beispiel |
|---|---|---|
| RPO (Recovery Point Objective) | Maximaler tolerierbarer Datenverlust (Zeitraum) | RPO = 1 h → max. 1 Stunde Datenverlust |
| RTO (Recovery Time Objective) | Maximale tolerierbare Ausfallzeit | RTO = 4 h → System muss in 4 h wieder laufen |
| WRT (Work Recovery Time) | Zeit fuer Verifizierung nach Wiederherstellung | WRT = 1 h → Testen, ob alles funktioniert |
| MTD (Maximum Tolerable Downtime) | Maximale Zeit, die ein Ausfall toleriert wird | MTD = RTO + WRT |

**Bestandteile eines Disaster-Recovery-Plans:**

| Bestandteil | Inhalt |
|---|---|
| Risikoanalyse | Welche Risiken bestehen? (Brand, Cyberangriff, Stromausfall, ...) |
| Business Impact Analysis (BIA) | Welche Systeme sind geschaeftskritisch? |
| RPO/RTO-Definitionen | Fuer jedes System individuell festlegen |
| Wiederherstellungsreihenfolge | Welches System wird zuerst wiederhergestellt? |
| Verantwortlichkeiten | Wer macht was im Notfall? |
| Kommunikationsplan | Wer wird wann informiert? (intern/extern) |
| Backup-Strategie | Wo liegen Backups? Wie werden sie zurueckgespielt? |
| Testplan | Wie oft wird der DRP getestet? (mind. jaehrlich) |

**Wichtige Begriffe:**
- **BIA (Business Impact Analysis)** – Analyse der geschaeftlichen Auswirkungen eines Ausfalls
- **RPO** – wieviel Datenverlust ist tolerierbar (in Zeit gemessen)
- **RTO** – wie schnell muss das System wieder laufen
- **BCM (Business Continuity Management)** – uebergeordnetes Management zur Sicherstellung der Geschaeftskontinuitaet
- **Hot Site / Cold Site / Warm Site** – Typen von Ausweichrechenzentren

**Ausweichrechenzentren:**

| Typ | Beschreibung | RTO | Kosten |
|---|---|---|---|
| Cold Site | Leerer Raum mit Strom/Netzwerk, keine Hardware | Tage–Wochen | Niedrig |
| Warm Site | Grundlegende Hardware vorhanden, Daten muessen eingespielt werden | Stunden–Tage | Mittel |
| Hot Site | Vollstaendig gespiegelte Infrastruktur, sofort einsatzbereit | Minuten–Stunden | Hoch |

---

## PDCA-Zyklus

**Definition:** Der Plan-Do-Check-Act-Zyklus (auch Deming-Kreis) ist ein vierstufiges Modell zur kontinuierlichen Verbesserung von Prozessen. Er wird im IT-Risikomanagement, Qualitaetsmanagement und ISMS (nach ISO 27001) eingesetzt.

**Die vier Phasen:**

| Phase | Beschreibung | Beispiel (IT-Risikomanagement) |
|---|---|---|
| **Plan** | Risiken identifizieren, Massnahmen planen | Risikoanalyse durchfuehren, Schutzmassnahmen definieren |
| **Do** | Massnahmen umsetzen | Firewall konfigurieren, Backup einrichten, USV installieren |
| **Check** | Wirksamkeit pruefen | Monitoring auswerten, Penetrationstest durchfuehren, Backup-Restore testen |
| **Act** | Verbesserungen ableiten, Prozess anpassen | Schwachstellen beheben, Richtlinien aktualisieren |

```
     +-------+
     | Plan  |
     +---+---+
         |
         v
     +---+---+
     |  Do   |
     +---+---+
         |
         v
     +---+---+
     | Check |
     +---+---+
         |
         v
     +---+---+
     |  Act  |-----> zurueck zu Plan (neuer Zyklus)
     +-------+
```

**Kernaussagen:**
- Der Zyklus ist endlos – nach Act beginnt Plan erneut
- Jeder Durchlauf verbessert den Prozess schrittweise
- Im ISMS (ISO 27001) ist PDCA die Grundlage des Managementsystems
- Der PDCA-Zyklus kann auf einzelne Risiken oder ganze IT-Prozesse angewendet werden

**Wichtige Begriffe:**
- **PDCA** – Plan-Do-Check-Act
- **KVP (Kontinuierlicher Verbesserungsprozess)** – Philosophie der stetigen Optimierung
- **ISMS (Informationssicherheits-Managementsystem)** – Managementsystem nach ISO 27001
- **ISO 27001** – Internationale Norm fuer Informationssicherheit
