# Komplett: 3.4.11 – Normalisierung anwenden

## Einordnung

- **Pruefungsteil:** 3.4 – Konzipieren und Umsetzen von kundenspezifischen Softwareanwendungen
- **Thema-ID:** 3.4.11
- **Thema:** Normalisierung anwenden koennen

## Ziel

Du musst die 1. bis 3. Normalform kennen, Verstoeße erkennen, funktionale und transitive Abhaengigkeiten identifizieren und eine unnormalisierte Tabelle schrittweise in die 3. Normalform ueberfuehren koennen.

## Themenkreise

| Nr. | Themenkreis | Schwerpunkte |
|-----|------------|-------------|
| 1 | 1. bis 3. Normalform | Normalformen, funktionale Abhaengigkeiten, Transformation |

---

## Grundlagen

### Warum Normalisierung?

**Definition:** Normalisierung ist ein systematisches Verfahren zur Strukturierung relationaler Datenbanken, um Redundanzen zu vermeiden und Anomalien (Einfuege-, Aenderungs-, Loeschanomalie) zu verhindern.

**Anomalien bei unnormalisierten Tabellen:**

| Anomalie | Beschreibung | Beispiel |
|----------|-------------|---------|
| Einfuegeanomalie | Daten koennen nicht eingefuegt werden, weil Pflichtfelder fehlen | Neuer Kurs kann nicht angelegt werden, solange kein Student eingeschrieben ist |
| Aenderungsanomalie | Gleiche Information muss an mehreren Stellen geaendert werden | Dozent-Name aendert sich → muss in jeder Zeile angepasst werden |
| Loeschanomalie | Beim Loeschen eines Datensatzes gehen ungewollte Informationen verloren | Letzter Student wird ausgetragen → Kursinformationen gehen verloren |

### Funktionale Abhaengigkeit

**Definition:** Ein Attribut B ist funktional abhaengig von Attribut A, wenn zu jedem Wert von A genau ein Wert von B gehoert.

**Schreibweise:** A → B (A bestimmt B)

**Beispiele:**
- KundeNr → Name (zu jeder KundeNr gehoert genau ein Name)
- BestellNr → Datum (zu jeder BestellNr gehoert genau ein Datum)
- PLZ → Ort (zu jeder PLZ gehoert genau ein Ort) – vereinfacht

### Transitive Abhaengigkeit

**Definition:** B ist transitiv abhaengig von A, wenn A → C und C → B gilt, wobei C kein Schluesselattribut ist.

**Schreibweise:** A → C → B

**Beispiel:** KundeNr → PLZ → Ort
- KundeNr bestimmt PLZ
- PLZ bestimmt Ort
- Also: Ort ist transitiv abhaengig von KundeNr (ueber PLZ)

---

### Die drei Normalformen

### 1. Normalform (1NF)

**Regel:** Jedes Attribut enthaelt nur **atomare** (unteilbare) Werte. Keine Wiederholungsgruppen, keine Aufzaehlungen in einer Zelle.

**Verstoss-Beispiel (NICHT in 1NF):**

| BestellNr | Kunde | Artikel |
|-----------|-------|---------|
| 001 | Mueller | Maus, Tastatur, Monitor |
| 002 | Schmidt | Laptop |

**Problem:** Das Attribut "Artikel" enthaelt mehrere Werte in einer Zelle.

**In 1NF ueberfuehrt:**

| BestellNr | Kunde | Artikel |
|-----------|-------|---------|
| 001 | Mueller | Maus |
| 001 | Mueller | Tastatur |
| 001 | Mueller | Monitor |
| 002 | Schmidt | Laptop |

→ Jede Zelle enthaelt genau einen Wert.

---

### 2. Normalform (2NF)

**Voraussetzung:** Tabelle ist in 1NF.

**Regel:** Jedes Nichtschluessel-Attribut ist **voll funktional abhaengig** vom gesamten Primaerschluessel (nicht nur von einem Teil davon).

**Verstoss-Beispiel (in 1NF, NICHT in 2NF):**

PK: (BestellNr, ArtikelNr)

| BestellNr | ArtikelNr | Menge | ArtikelBez | ArtikelPreis | KundeName |
|-----------|-----------|-------|-----------|-------------|-----------|
| 001 | A01 | 2 | Maus | 19.99 | Mueller |
| 001 | A02 | 1 | Tastatur | 49.99 | Mueller |
| 002 | A01 | 3 | Maus | 19.99 | Schmidt |

**Abhaengigkeiten:**
- (BestellNr, ArtikelNr) → Menge ✓ (voll abhaengig vom Gesamtschluessel)
- ArtikelNr → ArtikelBez, ArtikelPreis ✗ (abhaengig nur von TEIL des Schluessels)
- BestellNr → KundeName ✗ (abhaengig nur von TEIL des Schluessels)

**In 2NF ueberfuehrt – Tabellen aufteilen:**

**Tabelle: BestellPosition**

| BestellNr | ArtikelNr | Menge |
|-----------|-----------|-------|
| 001 | A01 | 2 |
| 001 | A02 | 1 |
| 002 | A01 | 3 |

**Tabelle: Artikel**

| ArtikelNr | ArtikelBez | ArtikelPreis |
|-----------|-----------|-------------|
| A01 | Maus | 19.99 |
| A02 | Tastatur | 49.99 |

**Tabelle: Bestellung**

| BestellNr | KundeName |
|-----------|-----------|
| 001 | Mueller |
| 002 | Schmidt |

→ Jedes Nichtschluessel-Attribut ist jetzt voll vom PK abhaengig.

---

### 3. Normalform (3NF)

**Voraussetzung:** Tabelle ist in 2NF.

**Regel:** Kein Nichtschluessel-Attribut ist **transitiv** von einem Schluesselkandidaten abhaengig. D.h. Nichtschluessel-Attribute duerfen nicht von anderen Nichtschluessel-Attributen abhaengen.

**Verstoss-Beispiel (in 2NF, NICHT in 3NF):**

PK: KundeNr

| KundeNr | Name | PLZ | Ort |
|---------|------|-----|-----|
| K01 | Mueller | 50667 | Koeln |
| K02 | Schmidt | 10115 | Berlin |
| K03 | Weber | 50667 | Koeln |

**Transitive Abhaengigkeit:**
- KundeNr → PLZ → Ort
- Ort ist transitiv abhaengig von KundeNr (ueber PLZ)
- Problem: Aenderungsanomalie – wird Koeln umbenannt, muss es in jeder Zeile geaendert werden

**In 3NF ueberfuehrt:**

**Tabelle: Kunde**

| KundeNr | Name | PLZ |
|---------|------|-----|
| K01 | Mueller | 50667 |
| K02 | Schmidt | 10115 |
| K03 | Weber | 50667 |

**Tabelle: Ort**

| PLZ | Ort |
|-----|-----|
| 50667 | Koeln |
| 10115 | Berlin |

→ Keine transitive Abhaengigkeit mehr. Ortsname wird nur einmal gespeichert.

---

## Vertiefung

### Zusammenfassung der Normalformen

| Normalform | Anforderung | Loest |
|-----------|------------|-------|
| 1NF | Nur atomare Werte, keine Wiederholungsgruppen | Mehrfachwerte in Zellen |
| 2NF | 1NF + volle funktionale Abhaengigkeit vom Gesamtschluessel | Teilabhaengigkeiten bei zusammengesetztem PK |
| 3NF | 2NF + keine transitiven Abhaengigkeiten | Abhaengigkeiten zwischen Nichtschluessel-Attributen |

### Vollstaendiges Normalisierungsbeispiel

**Ausgangstabelle (unnormalisiert):**

| BestellNr | Datum | KundeNr | KundeName | KundePLZ | KundeOrt | Artikel |
|-----------|-------|---------|-----------|----------|----------|---------|
| B001 | 2026-01-15 | K01 | Mueller | 50667 | Koeln | Maus (2x), Tastatur (1x) |
| B002 | 2026-01-20 | K02 | Schmidt | 10115 | Berlin | Monitor (1x) |

**Schritt 1 → 1NF:** Atomare Werte, Wiederholungsgruppen aufloesen

| BestellNr | Datum | KundeNr | KundeName | KundePLZ | KundeOrt | ArtikelNr | ArtikelBez | Menge |
|-----------|-------|---------|-----------|----------|----------|-----------|-----------|-------|
| B001 | 2026-01-15 | K01 | Mueller | 50667 | Koeln | A01 | Maus | 2 |
| B001 | 2026-01-15 | K01 | Mueller | 50667 | Koeln | A02 | Tastatur | 1 |
| B002 | 2026-01-20 | K02 | Schmidt | 10115 | Berlin | A03 | Monitor | 1 |

PK: (BestellNr, ArtikelNr)

**Schritt 2 → 2NF:** Teilabhaengigkeiten entfernen

Teilabhaengigkeiten:
- BestellNr → Datum, KundeNr, KundeName, KundePLZ, KundeOrt
- ArtikelNr → ArtikelBez

Ergebnis:

```
Bestellung (BestellNr [PK], Datum, KundeNr, KundeName, KundePLZ, KundeOrt)
Artikel (ArtikelNr [PK], ArtikelBez)
BestellPosition (BestellNr [FK], ArtikelNr [FK], Menge) → PK: (BestellNr, ArtikelNr)
```

**Schritt 3 → 3NF:** Transitive Abhaengigkeiten entfernen

Transitive Abhaengigkeiten in Bestellung:
- BestellNr → KundeNr → KundeName (Name haengt transitiv ueber KundeNr ab)
- BestellNr → KundeNr → KundePLZ → KundeOrt

Ergebnis:

```
Bestellung (BestellNr [PK], Datum, KundeNr [FK → Kunde])
Kunde (KundeNr [PK], KundeName, KundePLZ [FK → Ort])
Ort (PLZ [PK], Ortsname)
Artikel (ArtikelNr [PK], ArtikelBez)
BestellPosition (BestellNr [FK], ArtikelNr [FK], Menge) → PK: (BestellNr, ArtikelNr)
```

### Typische Pruefungsaspekte
- Verstoeße gegen Normalformen in einer Tabelle erkennen
- Tabelle schrittweise von unnormalisiert → 1NF → 2NF → 3NF ueberfuehren
- Funktionale und transitive Abhaengigkeiten benennen
- Anomalien erklaeren und durch Normalisierung beseitigen
- Zusammengesetzte Primaerschluessel identifizieren

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| 2NF bei einfachem PK pruefen | 2NF ist nur bei zusammengesetztem PK relevant (bei einfachem PK ist 2NF automatisch erfuellt) |
| 3NF-Verstoss nicht erkannt | Immer pruefen: Haengt ein Nichtschluessel-Attribut von einem anderen Nichtschluessel-Attribut ab? |
| Normalformen nicht in Reihenfolge geprueft | Immer erst 1NF, dann 2NF, dann 3NF pruefen |
| Zwischentabelle vergessen | Bei n:m-Beziehungen immer eine Zwischentabelle anlegen |
| Ort direkt in Kundentabelle gelassen | PLZ → Ort ist transitive Abhaengigkeit → auslagern (3NF) |

---

## Uebungen

**Aufgabe 1:** Erklaere die drei Anomalien (Einfuege-, Aenderungs-, Loeschanomalie) jeweils in einem Satz mit Beispiel.

**Aufgabe 2:** Pruefe, ob die folgende Tabelle in 1NF ist. Falls nicht, ueberfuehre sie:

| MitarbeiterNr | Name | Telefonnummern |
|--------------|------|---------------|
| M01 | Mueller | 0221-1234, 0172-5678 |
| M02 | Schmidt | 030-9876 |

**Aufgabe 3:** Normalisiere die folgende Tabelle schrittweise bis zur 3NF:

PK: (ProjektNr, MitarbeiterNr)

| ProjektNr | ProjektName | MitarbeiterNr | MitarbeiterName | AbteilungsNr | AbteilungsName | Stunden |
|-----------|------------|--------------|----------------|-------------|---------------|---------|
| P01 | Webshop | M01 | Mueller | A10 | Entwicklung | 120 |
| P01 | Webshop | M02 | Schmidt | A10 | Entwicklung | 80 |
| P02 | CRM | M01 | Mueller | A10 | Entwicklung | 60 |
| P02 | CRM | M03 | Weber | A20 | Vertrieb | 40 |

**Aufgabe 4:** Was bedeutet "volle funktionale Abhaengigkeit"? Warum ist sie fuer die 2NF wichtig?

---
---

# Loesungen

## Aufgabe 1
- **Einfuegeanomalie:** Daten koennen nicht eingefuegt werden, weil abhaengige Pflichtfelder fehlen. Beispiel: Ein neuer Kurs kann nicht angelegt werden, solange kein Student eingeschrieben ist.
- **Aenderungsanomalie:** Gleiche Information muss an mehreren Stellen geaendert werden, was zu Inkonsistenz fuehren kann. Beispiel: Abteilungsname aendert sich → muss in jeder Zeile geaendert werden.
- **Loeschanomalie:** Beim Loeschen eines Datensatzes gehen ungewollt andere Informationen verloren. Beispiel: Wird der letzte Mitarbeiter einer Abteilung geloescht, geht der Abteilungsname verloren.

## Aufgabe 2
**Nicht in 1NF**, da "Telefonnummern" mehrere Werte in einer Zelle enthaelt.

**In 1NF:**

| MitarbeiterNr | Name | Telefonnummer |
|--------------|------|--------------|
| M01 | Mueller | 0221-1234 |
| M01 | Mueller | 0172-5678 |
| M02 | Schmidt | 030-9876 |

Alternative (besser): Eigene Tabelle fuer Telefonnummern:

```
Mitarbeiter (MitarbeiterNr [PK], Name)
Telefon (MitarbeiterNr [FK], Telefonnummer) → PK: (MitarbeiterNr, Telefonnummer)
```

## Aufgabe 3

**Ausgangslage:** 1NF ist erfuellt (alle Werte sind atomar).

**Schritt 1 → 2NF:** Teilabhaengigkeiten bei PK (ProjektNr, MitarbeiterNr) identifizieren:
- ProjektNr → ProjektName (abhaengig nur von Teil des PK)
- MitarbeiterNr → MitarbeiterName, AbteilungsNr, AbteilungsName (abhaengig nur von Teil des PK)
- (ProjektNr, MitarbeiterNr) → Stunden (voll abhaengig ✓)

**Ergebnis 2NF:**

```
Projekt (ProjektNr [PK], ProjektName)
Mitarbeiter (MitarbeiterNr [PK], MitarbeiterName, AbteilungsNr, AbteilungsName)
ProjektZuordnung (ProjektNr [FK], MitarbeiterNr [FK], Stunden) → PK: (ProjektNr, MitarbeiterNr)
```

**Schritt 2 → 3NF:** Transitive Abhaengigkeiten in Mitarbeiter:
- MitarbeiterNr → AbteilungsNr → AbteilungsName (transitiv!)

**Ergebnis 3NF:**

```
Projekt (ProjektNr [PK], ProjektName)
Mitarbeiter (MitarbeiterNr [PK], MitarbeiterName, AbteilungsNr [FK → Abteilung])
Abteilung (AbteilungsNr [PK], AbteilungsName)
ProjektZuordnung (ProjektNr [FK], MitarbeiterNr [FK], Stunden) → PK: (ProjektNr, MitarbeiterNr)
```

## Aufgabe 4
**Volle funktionale Abhaengigkeit** bedeutet, dass ein Nichtschluessel-Attribut vom **gesamten** zusammengesetzten Primaerschluessel abhaengt und nicht nur von einem Teil davon. Sie ist fuer die 2NF wichtig, weil Teilabhaengigkeiten zu Redundanzen fuehren: Wenn ein Attribut nur von einem Teil des PK abhaengt, wird es bei jedem Datensatz mit dem gleichen Teilschluessel wiederholt, was Aenderungs- und Loeschanomalien verursacht.
