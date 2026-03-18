# Beispiele: 2.2.01 – Fehler erkennen, analysieren und beheben

## Beispiel 1: Debugging mit Breakpoint

**Fehlerhafter Pseudocode:**
```
funktion berechneRabatt(preis, kundentyp):
    rabatt = 0
    wenn kundentyp == "Premium":
        rabatt = preis * 0.15
    wenn kundentyp == "Standard":
        rabatt = preis * 0.05
    rueckgabe preis - rabatt
```

**Problem:** Kunde "Premium" erhaelt nur 5% statt 15% Rabatt.
**Ursache:** Zweite Bedingung ueberschreibt die erste nicht, ABER wenn kundentyp "Premium" ist, wird die zweite Bedingung nicht erfuellt. → Fehler liegt woanders: Uebergabewert pruefen!
**Debugging:** Breakpoint auf `rabatt = preis * 0.15` setzen → Variable `kundentyp` inspizieren → Wert zeigt "premium" (Kleinschreibung!) → Vergleich schlaegt fehl.
**Fix:** `kundentyp.toLowerCase() == "premium"` oder `kundentyp.upper() == "PREMIUM"`

---

## Beispiel 2: Testdaten mit Aequivalenzklassen

**Funktion:** Eingabefeld "Alter" (ganze Zahl, 0-120 zulaessig)

| Aequivalenzklasse | Werte | Erwartung |
|---|---|---|
| Ungueltig (zu klein) | -5, -1 | Fehlermeldung |
| Gueltig (Untergrenze) | 0, 1 | Akzeptiert |
| Gueltig (Mitte) | 25, 50, 99 | Akzeptiert |
| Gueltig (Obergrenze) | 119, 120 | Akzeptiert |
| Ungueltig (zu gross) | 121, 200 | Fehlermeldung |
| Ungueltig (kein Integer) | "abc", 25.5 | Fehlermeldung |

**Grenzwerte:** -1, 0, 1, 119, 120, 121

---

## Beispiel 3: Git-Workflow Featureentwicklung

```
1. git checkout main               # Auf Hauptbranch wechseln
2. git pull origin main             # Aktuelle Version holen
3. git checkout -b feature/login    # Neuen Branch erstellen
4. # ... Code aendern ...
5. git add .                        # Aenderungen vormerken
6. git commit -m "Login-Seite erstellt"  # Commit
7. git push origin feature/login    # Branch hochladen
8. # Pull Request erstellen (GitHub/GitLab)
9. # Code Review durch Kollegen
10. git checkout main
11. git merge feature/login         # Merge nach Freigabe
12. git push origin main
13. git branch -d feature/login     # Feature-Branch loeschen
```

---

## Beispiel 4: Teststufen in der Praxis

**Projekt:** Webanwendung fuer Rechnungserstellung

| Teststufe | Testfall | Ergebnis |
|---|---|---|
| Unit-Test | `berechneNetto(119, 19)` ergibt 100.00 | ✓ Bestanden |
| Unit-Test | `berechneMwSt(100, 19)` ergibt 19.00 | ✓ Bestanden |
| Integrationstest | Rechnung erstellen → DB-Eintrag pruefen | ✓ Bestanden |
| Integrationstest | Rechnung → PDF-Export → Datei vorhanden | ✗ Fehlgeschlagen (Pfad falsch) |
| Systemtest | Kunde anlegen → Rechnung → Versand → Archiv | ✓ Nach Bugfix bestanden |
| Abnahmetest | Kunde testet: "Rechnung sieht korrekt aus" | ✓ Abgenommen |
