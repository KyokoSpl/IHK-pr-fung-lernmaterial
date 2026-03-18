# 3.3.01 – Grundlagen: Softwareanforderungen erfassen

## Funktionale vs. nicht-funktionale Anforderungen

| Merkmal | Funktionale Anforderungen | Nicht-funktionale Anforderungen |
|---------|--------------------------|-------------------------------|
| Definition | WAS das System tun soll | WIE GUT das System arbeiten soll |
| Beispiel | "Benutzer kann sich einloggen" | "Login dauert max. 2 Sekunden" |
| Pruefung | Funktionstest | Leistungstest, Review |
| Quelle | Fachliche Anforderungen | Qualitaetsanforderungen |
| Dokumentation | Use Cases, User Stories | Qualitaetsszenarien |

---

## ISO 25010 – Qualitaetsmodell im Detail

### TK 1: Benutzbarkeit (Usability)

**Definition**: Grad, in dem ein Produkt durch bestimmte Benutzer effektiv, effizient und zufriedenstellend genutzt werden kann.

| Untermerkmal | Beschreibung | Beispiel |
|--------------|-------------|----------|
| Erlernbarkeit | Wie schnell kann ein neuer Benutzer das System bedienen? | Einarbeitungszeit < 1 Tag |
| Bedienbarkeit | Wie einfach laesst sich das System steuern? | Max. 3 Klicks bis zur Zielfunktion |
| Fehlertoleranz (UI) | Wie gut wird der Benutzer vor Fehlern geschuetzt? | Validierung bei Formulareingaben |
| Aesthetik | Ansprechendes, konsistentes Design | Einheitliches Farbschema, klare Struktur |
| Barrierefreiheit | Zugaenglichkeit fuer Menschen mit Einschraenkungen | Screenreader-Kompatibilitaet, Kontraste |

**Messgroessen**: Aufgabenabschlussrate, Fehlerrate bei Bedienung, Zufriedenheitsbefragung (SUS-Score)

---

### TK 2: Effizienz (Performance Efficiency)

**Definition**: Leistung im Verhaeltnis zu den eingesetzten Ressourcen unter bestimmten Bedingungen.

| Untermerkmal | Beschreibung | Beispiel |
|--------------|-------------|----------|
| Zeitverhalten | Antwort- und Verarbeitungszeiten | Seitenladezeit < 3 Sekunden |
| Ressourcenverbrauch | CPU, RAM, Speicherplatz, Bandbreite | Max. 512 MB RAM-Verbrauch |
| Kapazitaet | Maximale Grenzen des Systems | 10.000 gleichzeitige Benutzer |

**Messgroessen**: Response Time, Throughput, CPU-/RAM-Auslastung, Requests pro Sekunde

---

### TK 3: Funktionalitaet (Functional Suitability)

**Definition**: Grad, in dem das Produkt Funktionen bereitstellt, die erklaerte und implizierte Beduerfnisse erfuellen.

| Untermerkmal | Beschreibung | Beispiel |
|--------------|-------------|----------|
| Funktionale Vollstaendigkeit | Alle geforderten Funktionen vorhanden | Alle Use Cases implementiert |
| Funktionale Korrektheit | Ergebnisse sind richtig und praezise | Berechnungen liefern korrekte Werte |
| Funktionale Angemessenheit | Funktionen unterstuetzen die Aufgaben | Keine ueberfluessigen Features |

**Messgroessen**: Testabdeckung, Fehleranzahl pro Feature, Anforderungserfuellungsgrad

---

### TK 4: Normen anwenden

**ISO 25010** (ehemals ISO 9126): Definiert acht Hauptqualitaetsmerkmale fuer Softwareprodukte.

```
ISO 25010 – Produktqualitaet
├── Funktionale Eignung
├── Leistungseffizienz
├── Kompatibilitaet
├── Benutzbarkeit
├── Zuverlaessigkeit
├── Sicherheit
├── Wartbarkeit
└── Uebertragbarkeit
```

Weitere relevante Normen:

| Norm | Inhalt |
|------|--------|
| ISO 25010 | Qualitaetsmodell fuer Softwareprodukte |
| IEEE 830 | Empfehlungen fuer Softwareanforderungsspezifikationen |
| ISO 25030 | Qualitaetsanforderungen |
| ISO 9241 | Ergonomie der Mensch-System-Interaktion |

---

### TK 5: Wartbarkeit (Maintainability)

**Definition**: Grad der Effektivitaet und Effizienz, mit der ein Produkt modifiziert werden kann.

| Untermerkmal | Beschreibung | Beispiel |
|--------------|-------------|----------|
| Modularitaet | Aenderung einer Komponente hat minimale Auswirkung | Lose Kopplung zwischen Modulen |
| Wiederverwendbarkeit | Komponenten koennen in anderen Systemen genutzt werden | Bibliotheken, Microservices |
| Analysierbarkeit | Wie leicht kann man Fehlerursachen finden? | Aussagekraeftige Logs, klarer Code |
| Modifizierbarkeit | Wie einfach sind Aenderungen umsetzbar? | Saubere Architektur, Design Patterns |
| Testbarkeit | Wie einfach kann man Tests durchfuehren? | Unit-Test-Abdeckung > 80% |

**Messgroessen**: Zyklomatische Komplexitaet, Code-Coverage, Coupling/Cohesion-Metriken

---

### TK 6: Zuverlaessigkeit (Reliability)

**Definition**: Grad, in dem ein System unter bestimmten Bedingungen fuer einen bestimmten Zeitraum funktioniert.

| Untermerkmal | Beschreibung | Beispiel |
|--------------|-------------|----------|
| Reife | Zuverlaessigkeit im Normalbetrieb | MTBF > 1000 Stunden |
| Verfuegbarkeit | System ist einsatzbereit wenn benoetigt | 99,9% Verfuegbarkeit (SLA) |
| Fehlertoleranz | Funktioniert trotz Fehlern weiter | Graceful Degradation |
| Wiederherstellbarkeit | Daten und Zustand nach Ausfall wiederherstellen | Recovery Time < 5 Minuten |

**Schluesselkennzahlen**:
- **MTBF** = Mean Time Between Failures (Mittlere Betriebsdauer zwischen Ausfaellen)
- **MTTR** = Mean Time To Repair (Mittlere Reparaturzeit)
- **Verfuegbarkeit** = MTBF / (MTBF + MTTR)

---

### TK 7: Aenderbarkeit / Erweiterbarkeit

**Definition**: Faehigkeit der Software, an neue Anforderungen angepasst oder um neue Funktionen erweitert zu werden.

| Prinzip | Beschreibung | Umsetzung |
|---------|-------------|-----------|
| Open/Closed-Prinzip | Offen fuer Erweiterung, geschlossen fuer Aenderung | Interfaces, Abstraktion |
| Lose Kopplung | Geringe Abhaengigkeiten zwischen Modulen | Dependency Injection |
| Hohe Kohaesion | Zusammengehoerige Funktionen gebuendelt | Single Responsibility |
| Modularitaet | Unabhaengige, austauschbare Bausteine | Microservices, Plugins |

---

### TK 8: Uebertragbarkeit (Portability)

**Definition**: Grad der Effektivitaet und Effizienz, mit der ein System von einer Umgebung in eine andere uebertragen werden kann.

| Untermerkmal | Beschreibung | Beispiel |
|--------------|-------------|----------|
| Anpassbarkeit | An verschiedene Umgebungen anpassbar | Konfigurationsdateien statt Hardcoding |
| Installierbarkeit | Einfache Installation/Deinstallation | Setup-Wizard, Paketmanager |
| Austauschbarkeit | Kann andere Software ersetzen | Standardisierte Schnittstellen |

**Messgroessen**: Anzahl unterstuetzter Plattformen, Installationszeit, Konfigurationsaufwand

---

## Zusammenfassung: Alle acht Merkmale auf einen Blick

| Nr. | Merkmal | Kernfrage |
|-----|---------|-----------|
| 1 | Benutzbarkeit | Ist die Software leicht bedienbar? |
| 2 | Effizienz | Ist die Software schnell und ressourcenschonend? |
| 3 | Funktionalitaet | Macht die Software was sie soll? |
| 4 | Normen | Welche Standards muessen eingehalten werden? |
| 5 | Wartbarkeit | Kann die Software leicht gepflegt werden? |
| 6 | Zuverlaessigkeit | Laeuft die Software stabil? |
| 7 | Aenderbarkeit | Kann die Software leicht erweitert werden? |
| 8 | Uebertragbarkeit | Laeuft die Software auf verschiedenen Systemen? |
