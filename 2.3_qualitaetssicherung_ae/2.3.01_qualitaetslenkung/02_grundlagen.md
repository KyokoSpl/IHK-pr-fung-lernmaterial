# Grundlagen: 2.3.01 – Methoden der Qualitaetslenkung anwenden

## Debugging und Ablaufverfolgung

**Ablaufverfolgung (Tracing):** Protokollierung des Programmablaufs zur Laufzeit, um Fehler und Engpaesse zu identifizieren.

| Methode | Beschreibung | Einsatz |
|---|---|---|
| Print-Debugging | Ausgaben im Code zur Laufzeit | Schnelle Fehlersuche |
| Breakpoint-Debugging | Programm anhalten, Zustand pruefen | IDE-gestuetzte Analyse |
| Logging | Strukturierte Protokollierung (Level: DEBUG, INFO, WARN, ERROR) | Produktivsysteme |
| Profiling | Laufzeit und Speicherverbrauch messen | Performance-Analyse |
| Stack Trace | Aufrufhierarchie bei Fehler anzeigen | Laufzeitfehler lokalisieren |

**Log-Level:**

| Level | Bedeutung | Beispiel |
|---|---|---|
| DEBUG | Detaillierte Entwicklerinfos | Variable x = 42 |
| INFO | Normale Betriebsinformation | Server gestartet auf Port 8080 |
| WARN | Potenzielles Problem | Speicherauslastung bei 85% |
| ERROR | Fehler, Funktion beeintraechtigt | Datenbankverbindung fehlgeschlagen |
| FATAL | Kritisch, System nicht nutzbar | OutOfMemoryError |

---

## Software-Testverfahren (Vertiefung)

### Statisch vs. Dynamisch

| Merkmal | Statisch | Dynamisch |
|---|---|---|
| Code wird ausgefuehrt | Nein | Ja |
| Beispiele | Review, Walkthrough, Linter | Black Box, White Box, Lasttest |
| Findet | Stilfehler, Logikfehler, Sicherheitsluecken | Funktionale Fehler, Performanceprobleme |

### Last- und Performancetest

| Testtyp | Beschreibung | Ziel |
|---|---|---|
| Lasttest | System unter erwarteter Last testen | SLA-Anforderungen validieren |
| Stresstest | System ueber die Grenze belasten | Verhalten bei Ueberlast pruefen |
| Dauerlasttest (Soak) | Ueber laengeren Zeitraum belasten | Memory Leaks finden |
| Spike-Test | Ploetzlicher Lastanstieg | Reaktion auf Spitzen pruefen |

**Tools:** JMeter, Gatling, k6, Locust

---

## Pruefverfahren (Paritaet, Redundanz)

### Paritaetspruefung

**Definition:** Ein Pruefbit wird hinzugefuegt, um Uebertragungsfehler zu erkennen.

| Art | Regel | Beispiel (Datenbits: 1010110) |
|---|---|---|
| Gerade Paritaet | Anzahl 1en = gerade | Pruefbit = 0 → 10101100 |
| Ungerade Paritaet | Anzahl 1en = ungerade | Pruefbit = 1 → 10101101 |

**Einschraenkung:** Erkennt nur Einfachfehler (1 Bit gekippt).

### Redundanzverfahren

| Verfahren | Beschreibung | Beispiel |
|---|---|---|
| CRC (Cyclic Redundancy Check) | Polynomiale Pruefung | Netzwerkuebertragung (Ethernet) |
| Pruefsumme (Checksum) | Summe der Datenwerte | IP-Header-Pruefsumme |
| Hashwert | Einweg-Funktion | MD5, SHA-256 fuer Integritaet |
| RAID | Datenredundanz auf Festplatten | RAID 1 (Spiegelung), RAID 5 (Paritaet) |
| ECC-RAM | Fehlerkorrektur im Arbeitsspeicher | Server-RAM |
