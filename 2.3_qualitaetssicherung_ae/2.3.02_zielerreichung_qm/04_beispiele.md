# Beispiele: 2.3.02 – Methoden zur Messung der Zielerreichung im QM-Prozess

## Beispiel 1: Abnahmeprotokoll IT-Projekt

```
================================================================
              ABNAHMEPROTOKOLL
================================================================
Projekt:        Migration E-Mail-System auf Microsoft 365
Auftraggeber:   Mueller GmbH, Herr Max Mueller
Auftragnehmer:  IT-Service Schmidt, Frau Anna Schmidt
Datum:          15.03.2024
Ort:            Mueller GmbH, Berlin
----------------------------------------------------------------

Gegenstand der Abnahme:
- Migration von 50 Postfaechern zu Microsoft 365
- Einrichtung Exchange Online + Teams
- Schulung der Mitarbeiter (2 Termine)

Pruefergebnisse:
[x] E-Mail-Empfang/-Versand funktioniert
[x] Kalender synchronisiert
[x] Teams-Telefonie eingerichtet
[ ] Archivierung alter E-Mails → MANGEL

Festgestellte Maengel:
Nr.  Beschreibung                    Schwere      Frist
M01  Alte E-Mails nicht vollstaendig  Erheblich   31.03.2024
     migriert (ca. 5% fehlen)

Abnahmestatus: ABNAHME UNTER VORBEHALT
Nachbesserungsfrist: 31.03.2024

Unterschriften:
_________________    _________________
Auftraggeber          Auftragnehmer
================================================================
```

---

## Beispiel 2: Soll-Ist-Vergleich eines Softwareprojekts

| Phase | Soll (Tage) | Ist (Tage) | Abw. absolut | Abw. relativ |
|---|---|---|---|---|
| Anforderungsanalyse | 10 | 12 | +2 | +20% |
| Design | 8 | 8 | 0 | 0% |
| Implementierung | 25 | 32 | +7 | +28% |
| Test | 12 | 10 | -2 | -16,7% |
| Deployment | 5 | 5 | 0 | 0% |
| **Gesamt** | **60** | **67** | **+7** | **+11,7%** |

**Analyse:** Die Implementierung hatte die groesste Abweichung (+28%). Ursache: Zusaetzliche Kundenanforderungen waehrend der Umsetzung (Scope Creep). Die Testphase war kuerzer, was auf weniger gruendliches Testen hindeutet.

---

## Beispiel 3: PDCA in der Praxis

**Problem:** Die First-Fix-Rate im IT-Support liegt bei nur 45% (Ziel: >70%).

| Phase | Aktion |
|---|---|
| **Plan** | Analyse: Support-Mitarbeiter haben zu wenig Zugriff auf Wissens-DB. Massnahme: Wiki mit Loesungen fuer Top-20-Probleme erstellen |
| **Do** | Wiki erstellt, Schulung durchgefuehrt, 4 Wochen Testphase |
| **Check** | Messung nach 4 Wochen: First-Fix-Rate = 68% (+23 PP) |
| **Act** | Wiki wird Standardwerkzeug, monatliche Aktualisierung als Prozess definiert. Naechstes Ziel: 75% |
