# Vertiefung: 2.2.01 – Fehler erkennen, analysieren und beheben

## Vergleich: Black-Box vs. White-Box

| Kriterium | Black-Box | White-Box |
|---|---|---|
| Codekenntnisse | Nicht erforderlich | Erforderlich |
| Testbasis | Anforderungen/Spezifikation | Quellcode |
| Durchgefuehrt von | Tester, Kunde | Entwickler |
| Findet | Funktionale Fehler | Strukturelle Fehler |
| Teststufe | System-/Abnahmetest | Unit-/Integrationstest |
| Beispiel | "Login mit falschen Daten" | "Jeder If-Zweig durchlaufen" |

## V-Modell der Teststufen

```
Anforderungen ←─────────────→ Abnahmetest
      |                              |
  Grobentwurf ←──────────→ Systemtest
      |                         |
  Feinentwurf ←─────→ Integrationstest
      |                    |
  Implementierung ←→ Komponententest
```

Linke Seite = Entwicklung (Verifikation), Rechte Seite = Test (Validierung).

## Typische Pruefungsaspekte

- Teststufen dem V-Modell zuordnen
- Black-Box vs. White-Box Testverfahren anwenden
- Testdaten mit Aequivalenzklassen und Grenzwerten erstellen
- Git-Workflow (Branch → Commit → Merge) beschreiben
- Fehlerarten unterscheiden (Syntax, Laufzeit, Logik)

## Haeufige Fehler in Pruefungen

| Fehler | Richtig |
|---|---|
| Review ist ein dynamischer Test | Review = statisch (kein Ausfuehren) |
| Unit-Test testet das Gesamtsystem | Unit-Test = einzelne Funktion/Methode |
| Black-Box braucht Quellcode | Black-Box = NUR Spezifikation |
| Git Push = Aenderungen holen | Push = senden, Pull = holen |
| Testdaten beliebig waehlen | Systematisch: Aequivalenzklassen + Grenzwerte |
