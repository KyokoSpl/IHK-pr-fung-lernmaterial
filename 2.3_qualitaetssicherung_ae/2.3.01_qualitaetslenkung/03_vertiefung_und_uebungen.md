# Vertiefung und Uebungen: 2.3.01 – Methoden der Qualitaetslenkung

## Vertiefung

### Zusammenhang: Debugging → Test → Pruefverfahren

```
Entwicklung
    |
    v
+------------------+
| Statische Tests  |  (Review, Linter, statische Analyse)
+------------------+
    |
    v
+------------------+
| Dynamische Tests |  (Unit, Integration, System)
+------------------+
    |              \
    |               +---> Last-/Performancetest
    v
+------------------+
| Debugging        |  (bei gefundenen Fehlern)
| Ablaufverfolgung |
+------------------+
    |
    v
+------------------+
| Pruefverfahren   |  (Datenintegritaet sicherstellen)
| Paritaet, CRC,   |
| Hashwerte, RAID  |
+------------------+
```

### Typische Pruefungsaspekte

- Statische vs. dynamische Testverfahren unterscheiden
- Log-Level richtig zuordnen
- Paritaetsbit berechnen
- Last- vs. Stresstest unterscheiden
- RAID-Level und deren Redundanzprinzip erklaeren

### Haeufige Fehler

| Fehler | Richtig |
|---|---|
| Paritaet erkennt alle Fehler | Nur Einfachfehler, Doppelfehler bleiben unerkannt |
| Lasttest = Stresstest | Lasttest = erwartete Last; Stresstest = ueber Grenze |
| Review ist dynamisch | Review = statisch (kein Ausfuehren) |
| MD5 ist sicher | MD5 gilt als unsicher, SHA-256 bevorzugen |

---

## Uebungen

### Aufgabe 1: Paritaetsbit berechnen
Berechne das Paritaetsbit (gerade Paritaet) fuer folgende Datenwerte:
a) 1100101
b) 0111000
c) 1111111

---
---

**Loesung Aufgabe 1:**
a) 1100101 → Anzahl 1en = 4 (gerade) → Paritaetsbit = **0** → 11001010
b) 0111000 → Anzahl 1en = 3 (ungerade) → Paritaetsbit = **1** → 01110001
c) 1111111 → Anzahl 1en = 7 (ungerade) → Paritaetsbit = **1** → 11111111

---

### Aufgabe 2: Testverfahren zuordnen
Ordne die folgenden Szenarien dem passenden Testverfahren zu:
a) Ein Webshop wird mit 10.000 gleichzeitigen Nutzern getestet
b) Ein Kollege liest den Quellcode und gibt Feedback
c) Eine Eingabemaske wird mit gueltigen und ungueltigen Werten getestet, ohne den Code zu kennen
d) Nach einem Fehler wird der Log analysiert und ein Breakpoint gesetzt
e) Ein Tool prueft den Code auf Einhaltung von Coding-Standards

---
---

**Loesung Aufgabe 2:**
a) **Lasttest** (dynamisch) – Simuliert erwartete Nutzerlast.
b) **Code-Review** (statisch) – Manuelles Pruefen ohne Ausfuehrung.
c) **Black-Box-Test** (dynamisch) – Testen anhand Spezifikation.
d) **Debugging / Ablaufverfolgung** – Fehleranalyse mit Werkzeugen.
e) **Statische Analyse / Linter** (statisch) – Automatische Pruefung ohne Ausfuehrung.

---

### Aufgabe 3: Redundanzverfahren
a) Erklaere den Unterschied zwischen einem Hashwert und einer Pruefsumme.
b) Ein Server hat RAID 5 mit 4 Festplatten à 2 TB. Wie gross ist die nutzbare Kapazitaet?
c) Warum reicht eine einfache Paritaetspruefung nicht aus, um Datenfehler in einem RAID-System zu erkennen?

---
---

**Loesung Aufgabe 3:**
a) Eine **Pruefsumme** ist eine einfache Berechnung (z.B. Summe der Bytes), die leicht kollidieren kann. Ein **Hashwert** wird durch eine kryptographische Einwegfunktion berechnet (z.B. SHA-256) und ist kollisionsresistent – selbst minimale Aenderungen fuehren zu voellig anderen Hashwerten.
b) RAID 5: Kapazitaet = (n-1) × Einzelkapazitaet = (4-1) × 2 TB = **6 TB** nutzbar. 1 Platte dient als Paritaetsinformation (verteilt).
c) Eine einfache Paritaetspruefung erkennt nur Einfachfehler (1 Bit). Bei Festplattenausfaellen oder groesseren Datenverlusten werden komplexere Verfahren benoetigt (XOR-Paritaet ueber Festplatten bei RAID 5, Doppelparitaet bei RAID 6).
