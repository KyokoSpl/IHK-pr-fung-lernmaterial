# Vertiefung: 3.4.17 – OOP-Methodenkonzepte anwenden

## Zusammenhang der OOP-Konzepte

```
+--------------------------------------------------+
|                    OOP                            |
|                                                  |
|  +-------------+    +---------------+            |
|  | Kapselung   |    | Vererbung     |            |
|  | (Schutz der |    | (Wiederver-   |            |
|  |  Daten)     |    |  wendung)     |            |
|  +------+------+    +-------+-------+            |
|         |                   |                    |
|         v                   v                    |
|  +-------------+    +---------------+            |
|  | Getter/     |    | Kindklasse    |            |
|  | Setter      |    | erbt von      |            |
|  +-------------+    | Elternklasse  |            |
|                     +-------+-------+            |
|                             |                    |
|                             v                    |
|                     +---------------+            |
|                     | Polymorphie   |            |
|                     | (verschiedenes|            |
|                     |  Verhalten)   |            |
|                     +-------+-------+            |
|                             |                    |
|                             v                    |
|                     +---------------+            |
|                     | Interfaces    |            |
|                     | (Vertraege)   |            |
|                     +---------------+            |
+--------------------------------------------------+
```

## Kapselung – Vertiefung

### Warum Getter/Setter statt oeffentliche Attribute?

| Direkter Zugriff (schlecht) | Ueber Getter/Setter (gut) |
|---------------------------|--------------------------|
| `konto.stand = -500` | `konto.abheben(500)` → Validierung! |
| Keine Kontrolle moeglich | Logik im Setter moeglich |
| Interne Aenderungen brechen externen Code | Interne Darstellung aenderbar |

### Kapselung in der Praxis

```
// SCHLECHT: Oeffentliches Attribut
KLASSE Mitarbeiter
    OEFFENTLICH gehalt: Zahl    // Jeder kann direkt aendern!
ENDE KLASSE

m = neuer Mitarbeiter()
m.gehalt = -1000               // Unsinn, aber moeglich!

// GUT: Gekapseltes Attribut mit Validierung
KLASSE Mitarbeiter
    PRIVAT gehalt: Zahl

    OEFFENTLICH METHODE setGehalt(wert: Zahl)
        WENN wert >= 0 DANN
            gehalt = wert
        SONST
            ausgabe("Ungültiges Gehalt!")
        ENDE WENN
    ENDE METHODE
ENDE KLASSE
```

---

## Vererbung vs. Komposition

| Kriterium | Vererbung | Komposition |
|-----------|-----------|-------------|
| Beziehung | "ist ein" (is-a) | "hat ein" (has-a) |
| Beispiel | PKW ist ein Fahrzeug | Auto hat einen Motor |
| Kopplung | Eng (Aenderung der Elternklasse wirkt sich aus) | Lose (Komponenten austauschbar) |
| Empfehlung | Fuer echte Hierarchien | Bevorzugt, wenn keine echte is-a-Beziehung |

**Faustregel:** "Favor Composition over Inheritance" – Komposition bevorzugen, wenn moeglich.

---

## Polymorphie – Vertiefung

### Overloading vs. Overriding

| Kriterium | Overloading (Ueberladen) | Overriding (Ueberschreiben) |
|-----------|-------------------------|---------------------------|
| Wo? | In derselben Klasse | In Kindklasse |
| Was aendert sich? | Parameterliste | Implementierung |
| Methodenname | Gleich | Gleich |
| Rueckgabetyp | Kann verschieden sein | Muss gleich sein |
| Bindung | Compile-Time (statisch) | Runtime (dynamisch) |
| Beispiel | `addiere(a,b)` und `addiere(a,b,c)` | `Hund.sprechen()` statt `Tier.sprechen()` |

### Dynamische Bindung

```
// Variable vom Typ Tier, Objekt vom Typ Hund
tier: Tier = neuer Hund()
tier.sprechen()       // Ruft Hund.sprechen() auf → "Wau!"
                      // NICHT Tier.sprechen()!
```

→ Die aufgerufene Methode wird zur **Laufzeit** bestimmt, basierend auf dem tatsaechlichen Objekttyp (Hund), nicht dem Variablentyp (Tier).

---

## Interfaces – Vertiefung

### Mehrere Interfaces implementieren

```
INTERFACE Druckbar
    METHODE drucke()
ENDE INTERFACE

INTERFACE Exportierbar
    METHODE exportiere(format: String)
ENDE INTERFACE

KLASSE Rechnung IMPLEMENTIERT Druckbar, Exportierbar
    METHODE drucke()
        ausgabe("Rechnung wird gedruckt")
    ENDE METHODE

    METHODE exportiere(format: String)
        ausgabe("Export als " + format)
    ENDE METHODE
ENDE KLASSE
```

→ Eine Klasse kann mehrere Interfaces implementieren, aber nur von einer Klasse erben.

---

## Fehlerbehandlung – Vertiefung

### Fehlerbehandlungsstrategie

| Strategie | Beschreibung | Beispiel |
|-----------|-------------|----------|
| Fehlermeldung ausgeben | Benutzer informieren | "Datei nicht gefunden" |
| Standardwert verwenden | Sinnvoller Ersatzwert | Konfiguration: Standard-Port 8080 |
| Wiederholung | Aktion erneut versuchen | Netzwerkverbindung nochmal aufbauen |
| Weiterleiten | Fehler an aufrufende Methode weiterreichen | `throw` / weitergeben |
| Loggen | Fehler protokollieren | Log-Datei beschreiben |

### Best Practices

```
// SCHLECHT: Leerer Catch-Block
VERSUCHE
    daten = datei.lese()
FANGE FehlerTyp Exception
    // Nichts tun → Fehler wird verschluckt!
ENDE VERSUCHE

// GUT: Fehler sinnvoll behandeln
VERSUCHE
    daten = datei.lese()
FANGE FehlerTyp DateiNichtGefunden als fehler
    log("Fehler: " + fehler.nachricht)
    ausgabe("Die Datei konnte nicht geladen werden. Bitte pruefen Sie den Pfad.")
ABSCHLIESSEND
    datei.schliesse()
ENDE VERSUCHE
```

---

## Gesamtvergleich: OOP-Konzepte in UML

```
+---------------------------+          +---------------------+
| <<interface>>             |          |    Fahrzeug         |
| Serialisierbar            |          |---------------------|
|---------------------------|          | # marke: String     |
| + serialisiere(): String  |          | # baujahr: int      |
+---------------------------+          |---------------------|
         ^                             | + beschreibung()    |
         |                             +----------+----------+
   implementiert                                  ^
         |                                   erbt von
+--------+-----------+                            |
|       PKW          |----------------------------+
|--------------------| 
| - anzahlSitze: int |     Legende:
|--------------------| 
| + beschreibung()   |     + public
| + serialisiere()   |     - private
+--------------------+     # protected
                           ^ Vererbung (Dreieck)
                           ^ Interface-Implementierung (gestrichelt)
```

## Typische Pruefungsaspekte
- UML-Klassendiagramm lesen: Zugriffsmodifikatoren, Vererbung, Interface erkennen
- Pseudocode mit OOP-Konzepten schreiben und lesen
- Overloading vs. Overriding unterscheiden
- Interface vs. abstrakte Klasse: Wann welches?
- Kapselung: Warum keine oeffentlichen Attribute?
- Exception-Handling: try-catch-finally-Ablauf erklaeren
- Szenario: Fehlende Fehlerbehandlung in Code erkennen

## Haeufige Fehler
- Vererbung wird fuer "hat-ein"-Beziehungen verwendet → Komposition waere korrekt
- Overloading und Overriding verwechselt
- Interface mit Klasse verwechselt: Interface enthaelt KEINEN Code
- Kapselung ignoriert: Alle Attribute public → keine Validierung moeglich
- Leere catch-Bloecke: Fehler werden verschluckt, schwer zu debuggen
- `super` vergessen bei Konstruktor-Aufruf der Elternklasse
