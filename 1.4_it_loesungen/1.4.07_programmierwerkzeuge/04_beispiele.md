# Beispiele: 1.4.07 – Programmierwerkzeuge

## Pseudocode-Beispiel: Notendurchschnitt berechnen

```
FUNKTION berechneNotendurchschnitt(noten: Liste von Integer): Double
    WENN noten leer DANN
        AUSGABE "Keine Noten vorhanden"
        RUECKGABE 0.0
    ENDE WENN

    summe = 0
    FUER JEDE note IN noten
        summe = summe + note
    ENDE FUER

    durchschnitt = summe / LAENGE(noten)
    RUECKGABE durchschnitt
ENDE FUNKTION

// Aufruf:
ergebnis = berechneNotendurchschnitt([2, 3, 1, 4, 2])
AUSGABE "Durchschnitt: " + ergebnis   // → 2.4
```

---

## Schreibtischtest: Fakultaet berechnen

**Code:**
```
n = 4
ergebnis = 1
i = 1
SOLANGE i <= n
    ergebnis = ergebnis * i
    i = i + 1
ENDE SOLANGE
AUSGABE ergebnis
```

**Variablentabelle:**

| Schritt | n | ergebnis | i | Bedingung i<=n |
|---|---|---|---|---|
| Init | 4 | 1 | 1 | – |
| Durchlauf 1 | 4 | 1 | 2 | 1<=4 → wahr |
| Durchlauf 2 | 4 | 2 | 3 | 2<=4 → wahr |
| Durchlauf 3 | 4 | 6 | 4 | 3<=4 → wahr |
| Durchlauf 4 | 4 | 24 | 5 | 4<=4 → wahr |
| Abbruch | 4 | 24 | 5 | 5<=4 → falsch |

**Ausgabe:** 24 (= 4!)

---

## Fehler im Code finden: Beispiel

**Fehlerhafter Code (Java-aehnlich):**
```java
public int summe(int[] zahlen) {
    int ergebnis;                    // Fehler 1: nicht initialisiert
    for (int i = 0; i <= zahlen.length; i++) {  // Fehler 2: <= statt <
        ergebnis = ergebnis + zahlen[i];
    }
    return ergebnis;
}
```

**Gefundene Fehler:**

| Nr. | Zeile | Fehlerart | Beschreibung | Korrektur |
|---|---|---|---|---|
| 1 | 2 | Logisch | Variable `ergebnis` wird nicht initialisiert | `int ergebnis = 0;` |
| 2 | 3 | Laufzeit | `<=` fuehrt zu ArrayIndexOutOfBoundsException | `i < zahlen.length` |

---

## Use-Case-Diagramm: Online-Shop

```
┌────────────────────────────────────────────┐
│              Online-Shop-System             │
│                                            │
│   ┌──────────────────────┐                 │
│   │  Produkt suchen      │←───── Kunde     │
│   └──────────────────────┘                 │
│                                            │
│   ┌──────────────────────┐                 │
│   │  Warenkorb verwalten │←───── Kunde     │
│   └──────────────────────┘                 │
│         │ <<include>>                      │
│         ▼                                  │
│   ┌──────────────────────┐                 │
│   │  Bestellung aufgeben │←───── Kunde     │
│   └──────────────────────┘                 │
│         │ <<include>>    │ <<extend>>      │
│         ▼                ▼                 │
│   ┌─────────────┐ ┌──────────────┐        │
│   │ Bezahlung   │ │ Gutschein    │        │
│   │ durchfuehren│ │ einloesen    │        │
│   └─────────────┘ └──────────────┘        │
│                                            │
│   ┌──────────────────────┐                 │
│   │  Bestellung verwalten│←──── Admin      │
│   └──────────────────────┘                 │
└────────────────────────────────────────────┘
```

- **Akteure:** Kunde, Admin
- **<<include>>:** Bezahlung ist immer Teil der Bestellung
- **<<extend>>:** Gutschein einloesen ist optional

---

## Klassendiagramm: Kunden und Bestellungen

```
┌──────────────────┐         ┌──────────────────────┐
│     Kunde        │ 1    *  │     Bestellung       │
├──────────────────┤─────────├──────────────────────┤
│ - kundenNr: int  │         │ - bestellNr: int     │
│ - name: String   │         │ - datum: Date        │
│ - email: String  │         │ - gesamtpreis: double│
├──────────────────┤         ├──────────────────────┤
│ + getName(): Str │         │ + getGesamt(): double│
│ + bestellen()    │         │ + stornieren(): void │
└──────────────────┘         └──────────────────────┘
                                      │ 1
                                      │
                                      │ *
                             ┌──────────────────────┐
                             │  Bestellposition     │
                             ├──────────────────────┤
                             │ - menge: int         │
                             │ - einzelpreis: double│
                             ├──────────────────────┤
                             │ + getPositionspreis() │
                             └──────────────────────┘
```

- Kunde 1 → * Bestellung (ein Kunde kann viele Bestellungen haben)
- Bestellung 1 → * Bestellposition (Komposition: Positionen gehoeren zur Bestellung)

---

## Bildschirmmaske: Login-Formular (Bewertung)

```
┌─────────────────────────────────────┐
│  [Logo]     Firmenname              │
├─────────────────────────────────────┤
│                                     │
│   Benutzername: [________________]  │
│                                     │
│   Passwort:     [________________]  │
│                                     │
│   [ ] Angemeldet bleiben            │
│                                     │
│         [  Anmelden  ]              │
│                                     │
│   Passwort vergessen?               │
│                                     │
└─────────────────────────────────────┘
```

**Bewertung nach DIN EN ISO 9241:**
- ✅ Aufgabenangemessen: Nur notwendige Felder
- ✅ Selbstbeschreibend: Labels vorhanden
- ✅ Erwartungskonform: Standard-Login-Layout
- ✅ Fehlertoleranz: „Passwort vergessen"-Link
- ⚠️ Verbesserung: Fehlermeldung bei falschem Login fehlt noch
