# Uebungen: 1.4.07 – Programmierwerkzeuge

## Aufgabe 1: Pseudocode schreiben
Schreibe einen Pseudocode-Algorithmus, der prueft, ob eine eingegebene Zahl eine Primzahl ist. Der Algorithmus soll `WAHR` oder `FALSCH` zurueckgeben.

---

## Aufgabe 2: Schreibtischtest
Fuehre einen Schreibtischtest fuer folgenden Code durch und erstelle eine Variablentabelle:

```
a = 10
b = 3
c = a MOD b     // MOD = Modulo (Rest der Division)
a = a - c
b = b + c
AUSGABE a, b, c
```

---

## Aufgabe 3: Fehler im Code finden
Finde alle Fehler im folgenden Pseudocode. Erklaere jeweils die Fehlerart (Syntax, Laufzeit, Logik).

```
FUNKTION maximum(liste: Liste von Integer): Integer
    max = liste[1]
    FUER i = 1 BIS LAENGE(liste)
        WENN liste[i] >= max DANN
            max = i
        ENDE WENN
    ENDE FUER
    RUECKGABE max
ENDE FUNKTION
```

---

## Aufgabe 4: Use-Case-Diagramm
Ein Bibliothekssystem hat folgende Anforderungen:
- Mitglieder koennen Buecher suchen, ausleihen und zurueckgeben
- Bei der Ausleihe wird automatisch die Verfuegbarkeit geprueft (include)
- Mitglieder koennen optional eine Verlaengerung beantragen (extend)
- Bibliothekare koennen Buecher hinzufuegen und Mahnungen versenden

Zeichne ein Use-Case-Diagramm mit allen Akteuren, Use Cases und Beziehungen.

---

## Aufgabe 5: Klassendiagramm
Erstelle ein Klassendiagramm fuer ein einfaches Fahrzeugverwaltungssystem:
- Klasse `Fahrzeug` mit Attributen: kennzeichen (String), baujahr (int), kmStand (double)
- Klasse `PKW` erbt von Fahrzeug, zusaetzlich: sitzplaetze (int)
- Klasse `LKW` erbt von Fahrzeug, zusaetzlich: ladekapazitaet (double)
- Klasse `Fuhrpark` enthaelt mehrere Fahrzeuge

Gib Sichtbarkeiten und Kardinalitaeten an.

---

## Aufgabe 6: Bildschirmmaske bewerten
Bewerte folgende Bildschirmmaske anhand der DIN EN ISO 9241 Grundsaetze:

```
┌──────────────────────────────────────────┐
│  DATEN EINGEBEN                          │
│                                          │
│  [___________]  [___________]            │
│  [___________]  [___________]            │
│  [___________]                           │
│                                          │
│  [OK]  [Abbrechen]  [Reset]  [Hilfe]    │
└──────────────────────────────────────────┘
```

Welche Probleme erkennst du? Welche Verbesserungen schlage vor?

---

## Aufgabe 7: Pseudocode zu Aktivitaetsdiagramm
Setze folgenden Pseudocode in ein Aktivitaetsdiagramm um:

```
EINGABE benutzername, passwort
WENN benutzername leer ODER passwort leer DANN
    AUSGABE "Bitte alle Felder ausfuellen"
SONST
    pruefe = authentifiziere(benutzername, passwort)
    WENN pruefe == WAHR DANN
        AUSGABE "Willkommen!"
        zeigeDashboard()
    SONST
        versuche = versuche + 1
        WENN versuche >= 3 DANN
            sperreKonto()
        ENDE WENN
        AUSGABE "Falsches Passwort"
    ENDE WENN
ENDE WENN
```

---

## Aufgabe 8: Schreibtischtest mit Schleife
Fuehre einen Schreibtischtest durch:

```
ergebnis = ""
text = "HALLO"
FUER i = LAENGE(text) - 1 BIS 0 SCHRITT -1
    ergebnis = ergebnis + text[i]
ENDE FUER
AUSGABE ergebnis
```

Was wird ausgegeben?

---
---

# Loesungen

## Loesung 1: Primzahl-Pseudocode
```
FUNKTION istPrimzahl(zahl: Integer): Boolean
    WENN zahl <= 1 DANN
        RUECKGABE FALSCH
    ENDE WENN
    WENN zahl <= 3 DANN
        RUECKGABE WAHR
    ENDE WENN
    WENN zahl MOD 2 == 0 DANN
        RUECKGABE FALSCH
    ENDE WENN
    FUER teiler = 3 BIS WURZEL(zahl) SCHRITT 2
        WENN zahl MOD teiler == 0 DANN
            RUECKGABE FALSCH
        ENDE WENN
    ENDE FUER
    RUECKGABE WAHR
ENDE FUNKTION
```

---

## Loesung 2: Schreibtischtest

| Schritt | a | b | c |
|---|---|---|---|
| Init | 10 | 3 | – |
| c = a MOD b | 10 | 3 | 1 |
| a = a - c | 9 | 3 | 1 |
| b = b + c | 9 | 4 | 1 |

**Ausgabe:** 9, 4, 1

---

## Loesung 3: Fehler im Code

| Nr. | Zeile | Fehler | Art | Korrektur |
|---|---|---|---|---|
| 1 | `max = liste[1]` | Index beginnt bei 0, nicht 1 → Erstes Element wird uebersprungen | Logisch | `max = liste[0]` |
| 2 | `FUER i = 1` | Muss bei 0 beginnen (wenn 0-basiert) oder bei 2 (wenn 1-basiert, da max schon mit [1] gesetzt) | Logisch | `FUER i = 0` |
| 3 | `max = i` | Speichert den Index statt den Wert | Logisch | `max = liste[i]` |

---

## Loesung 4: Use-Case-Diagramm
```
Akteure: Mitglied, Bibliothekar

Use Cases:
- Buch suchen ← Mitglied
- Buch ausleihen ← Mitglied
  - <<include>> Verfuegbarkeit pruefen
  - <<extend>> Verlaengerung beantragen
- Buch zurueckgeben ← Mitglied
- Buch hinzufuegen ← Bibliothekar
- Mahnung versenden ← Bibliothekar
```

---

## Loesung 5: Klassendiagramm

```
┌──────────────────────┐
│    <<abstract>>       │
│      Fahrzeug         │
├──────────────────────┤
│ - kennzeichen: String│
│ - baujahr: int       │
│ - kmStand: double    │
├──────────────────────┤
│ + getKennzeichen()   │
└──────────┬───────────┘
           △
     ┌─────┴──────┐
     │            │
┌────┴────┐ ┌────┴────────┐
│   PKW   │ │    LKW      │
├─────────┤ ├─────────────┤
│-sitzpl.:│ │-ladekap.:   │
│  int    │ │  double     │
└─────────┘ └─────────────┘

┌──────────────┐ 1    * ┌───────────┐
│  Fuhrpark    │────────│ Fahrzeug  │
└──────────────┘        └───────────┘
```

- PKW und LKW erben von Fahrzeug (Vererbung △)
- Fuhrpark enthaelt 0..* Fahrzeuge (Aggregation/Komposition)

---

## Loesung 6: Bildschirmmaskenbewertung

**Probleme:**
1. **Selbstbeschreibungsfaehigkeit:** Keine Labels – Nutzer weiss nicht, was in die Felder einzugeben ist
2. **Aufgabenangemessenheit:** Unklar, welche Daten benoetigt werden
3. **Erwartungskonformitaet:** Unuebliches Layout ohne klare Struktur
4. **Fehlertoleranz:** Keine Hinweise bei Fehlern

**Verbesserungen:**
- Labels vor jedem Feld (z.B. „Vorname:", „Nachname:")
- Pflichtfelder markieren (*)
- Fehlermeldungen bei ungueltigem Input
- Tab-Reihenfolge festlegen
- Tooltip/Hilfetext je Feld

---

## Loesung 7: Aktivitaetsdiagramm

```
(●) Start
  ↓
[Eingabe: Benutzername + Passwort]
  ↓
◇ Felder leer?
├── Ja → [Ausgabe: "Bitte alle Felder ausfuellen"] → (◉)
└── Nein ↓
    [Authentifizierung pruefen]
    ↓
    ◇ Erfolgreich?
    ├── Ja → [Ausgabe: "Willkommen!"] → [Dashboard anzeigen] → (◉)
    └── Nein ↓
        [versuche + 1]
        ↓
        ◇ versuche >= 3?
        ├── Ja → [Konto sperren] → [Ausgabe: "Falsches Passwort"] → (◉)
        └── Nein → [Ausgabe: "Falsches Passwort"] → (◉)
```

---

## Loesung 8: Schreibtischtest

| Schritt | i | text[i] | ergebnis |
|---|---|---|---|
| Init | – | – | "" |
| i=4 | 4 | "O" | "O" |
| i=3 | 3 | "L" | "OL" |
| i=2 | 2 | "L" | "OLL" |
| i=1 | 1 | "A" | "OLLA" |
| i=0 | 0 | "H" | "OLLAH" |

**Ausgabe:** OLLAH (Text rueckwaerts)
