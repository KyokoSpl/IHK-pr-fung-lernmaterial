# Grundlagen: 2.3.02 – Methoden zur Messung der Zielerreichung im QM-Prozess

## Abnahmeprotokoll

**Definition:** Formales Dokument, das die Uebergabe und Abnahme einer Leistung durch den Auftraggeber dokumentiert.

**Inhalte eines Abnahmeprotokolls:**

| Feld | Beschreibung |
|---|---|
| Projektbezeichnung | Name/Nummer des Projekts |
| Auftraggeber / Auftragnehmer | Vertragspartner |
| Datum der Abnahme | Wann wurde abgenommen? |
| Gegenstand der Abnahme | Was wurde geliefert/installiert? |
| Pruefergebnisse | Testresultate, Checklisten |
| Maengel | Gefundene Maengel mit Schweregrad |
| Abnahmestatus | Ohne Maengel / mit Maengeln / verweigert |
| Nachbesserungsfrist | Frist zur Maengelbehebung |
| Unterschriften | Bestaetigung beider Parteien |

**Abnahmearten:**
- **Foermliche Abnahme:** Schriftliches Protokoll, ausdrueckliche Erklaerung
- **Konkludente Abnahme:** Durch schluessiges Verhalten (z.B. Nutzung der Software)
- **Abnahme unter Vorbehalt:** Abnahme mit festgehaltenen Maengeln

---

## Soll-Ist-Vergleich und Abweichungsanalyse

**Vorgehen:**
1. Soll-Werte definieren (Planung, Vertrag, SLA)
2. Ist-Werte erheben (nach Durchfuehrung)
3. Abweichungen berechnen (absolut und prozentual)
4. Ursachen analysieren
5. Massnahmen ableiten

**Berechnung:**
- Absolute Abweichung = Ist - Soll
- Relative Abweichung = (Ist - Soll) / Soll × 100%

| Kennzahl | Soll | Ist | Abweichung |
|---|---|---|---|
| Projektdauer (Tage) | 60 | 72 | +12 (+20%) |
| Budget (€) | 50.000 | 48.000 | -2.000 (-4%) |
| Fehlerquote (%) | < 2% | 3,5% | +1,5 PP |
| Verfuegbarkeit (%) | 99,5% | 99,2% | -0,3 PP |

---

## Testdatengeneratoren

**Definition:** Tools, die automatisch Testdaten erzeugen, um Software unter realistischen Bedingungen zu testen.

**Einsatzgebiete:**

| Szenario | Testdatentyp | Tool-Beispiel |
|---|---|---|
| Datenbanktest | Kundendaten (Name, Adresse, E-Mail) | Faker, Mockaroo |
| Lasttest | Tausende gleichzeitige Anfragen | JMeter, k6 |
| Grenzwerttest | Extremwerte (MIN, MAX, Leerstring) | Eigenentwicklung |
| DSGVO-konform | Anonymisierte/pseudonymisierte Daten | Jailer, ARX |

**Vorteile:**
- Grosse Datenmengen schnell erzeugen
- Reproduzierbare Testszenarien
- Kein Risiko durch echte Personendaten
- Grenzfaelle systematisch abdecken

---

## Testprotokolle

**Definition:** Dokumentation der Testergebnisse mit Testfall, Erwartung, Ergebnis und Status.

**Aufbau:**

| Testfall-Nr | Beschreibung | Eingabe | Erwartetes Ergebnis | Tatsaechliches Ergebnis | Status |
|---|---|---|---|---|---|
| T-001 | Login mit gueltigen Daten | user/pass123 | Dashboard angezeigt | Dashboard angezeigt | Bestanden |
| T-002 | Login mit falschem PW | user/falsch | Fehlermeldung | Fehlermeldung | Bestanden |
| T-003 | Login ohne Passwort | user/"" | Validierungsfehler | Kein Fehler, Absturz | Fehlgeschlagen |

**Zusaetzliche Informationen:**
- Tester, Datum, Testumgebung
- Softwareversion
- Vorbedingungen
- Fehlerstatus und Prioritaet

---

## Verbesserungsprozess (PDCA, KVP, Kennzahlen)

### PDCA-Zyklus

```
    Plan ────→ Do
     ^          |
     |          v
    Act ←──── Check
```

| Phase | Beschreibung | QM-Beispiel |
|---|---|---|
| Plan | Problem analysieren, Massnahme planen | "Fehlerquote ist 3,5%, Ziel: < 2%" |
| Do | Massnahme umsetzen | Code-Review-Pflicht einfuehren |
| Check | Ergebnis pruefen | Fehlerquote nach 4 Wochen: 1,8% |
| Act | Standard setzen oder anpassen | Code-Review als Standard etablieren |

### KVP (Kontinuierlicher Verbesserungsprozess)

**Prinzip:** Stetige, kleine Verbesserungen statt grosser Umbrueche (Kaizen).

**Merkmale:**
- Alle Mitarbeiter sind beteiligt
- Kleine Schritte, schnelle Umsetzung
- Messbarer Fortschritt durch Kennzahlen

### Qualitaetskennzahlen (KPIs)

| Kennzahl | Formel/Beschreibung | Zielwert (Beispiel) |
|---|---|---|
| Fehlerquote | Fehler / Testfaelle × 100% | < 2% |
| Testabdeckung | Getestete Funktionen / Alle Funktionen × 100% | > 80% |
| MTTR | Mean Time to Repair (durchschnittliche Reparaturzeit) | < 4 Stunden |
| Kundenzufriedenheit | Bewertungsskala 1-5 | > 4,0 |
| First-Fix-Rate | Beim ersten Mal geloest / Alle Tickets × 100% | > 70% |
