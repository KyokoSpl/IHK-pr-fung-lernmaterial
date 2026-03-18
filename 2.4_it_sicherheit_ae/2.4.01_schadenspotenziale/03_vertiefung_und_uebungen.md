# Vertiefung und Uebungen: 2.4.01 – Schadenspotenziale von IT-Sicherheitsvorfaellen

## Vertiefung

### Schadenskategorien im Vergleich

| Kriterium | Datenverlust | Imageschaden | Wirtschaftlicher Schaden |
|---|---|---|---|
| Zeithorizont | Sofort spuerbar | Mittel- bis langfristig | Sofort + langfristig |
| Messbarkeit | Gut (Datenbestand) | Schwer (Reputation) | Gut (EUR-Betrag) |
| Reversibilitaet | Moeglich (Backup) | Schwer umkehrbar | Teilweise (Versicherung) |
| Betroffene | IT-Abteilung, Nutzer | Gesamtes Unternehmen | Geschaeftsfuehrung, Finanzen |
| Praevention | Backup, RAID, DR | Awareness, Kommunikation | Risikoanalyse, Versicherung |

### Zusammenhang der Schadenspotenziale

```
+-------------------+
|  IT-Sicherheits-  |
|    vorfall         |
+--------+----------+
         |
    +----+----+----+----+----+
    |              |              |
    v              v              v
+---------+  +-----------+  +------------+
| Daten-  |  | Image-    |  | Wirtschaft-|
| verlust |  | schaden   |  | licher     |
|         |  |           |  | Schaden    |
+----+----+  +-----+-----+  +-----+------+
     |             |               |
     +------+------+-------+-------+
            |              |
            v              v
    +-------+------+ +----+--------+
    | Betriebsunter| | Bussgeld /  |
    | brechung     | | Rechtsfolgen|
    +--------------+ +-------------+
```

### Risikobetrachtung nach Eintrittswahrscheinlichkeit

| Bedrohung | Eintrittswahrscheinlichkeit | Schadenshoehe | Risikostufe |
|---|---|---|---|
| Ransomware | Hoch | Sehr hoch | Kritisch |
| Hardwaredefekt | Mittel | Mittel | Hoch |
| Naturkatastrophe | Niedrig | Sehr hoch | Mittel |
| Bedienfehler | Hoch | Gering–Mittel | Mittel |
| Insider-Angriff | Niedrig | Hoch | Mittel |

**Formel:** Risiko = Eintrittswahrscheinlichkeit × Schadenshoehe

### Meldepflichten bei Sicherheitsvorfaellen

| Regelwerk | Pflicht | Frist |
|---|---|---|
| DSGVO Art. 33 | Meldung an Aufsichtsbehoerde | 72 Stunden |
| DSGVO Art. 34 | Benachrichtigung Betroffener | Unverzueglich |
| IT-Sicherheitsgesetz | Meldung an BSI (KRITIS) | Unverzueglich |
| NIS2-Richtlinie | Fruehwarnung an CSIRT | 24 Stunden |

### Typische Pruefungsaspekte
- Schadenspotenzial eines Szenarios einschaetzen und begruenden
- Zusammenhang zwischen Datenverlust, Image und wirtschaftlichem Schaden erkennen
- Backup-Strategien (3-2-1-Regel) anwenden
- RTO und RPO erklaeren und auf Szenarien anwenden
- Meldepflichten kennen (DSGVO Art. 33/34)

### Haeufige Fehler
- Imageschaden wird unterschaetzt → kann gravierender sein als der direkte finanzielle Verlust
- RAID wird als Backup angesehen → RAID schuetzt nur vor Hardwareausfall, nicht vor Loeschen oder Ransomware
- Wirtschaftlicher Schaden = nur die Reparaturkosten → Folgekosten (Bussgeld, Kundenverlust) vergessen
- Meldepflicht bei DSGVO-Verstoss vergessen → 72-Stunden-Frist

---

## Uebungen

**Aufgabe 1:** Ein mittelstaendisches Unternehmen wird Opfer eines Ransomware-Angriffs. Alle Server sind verschluesselt, das letzte Backup ist 7 Tage alt. Beschreibe die drei Schadenskategorien (Datenverlust, Imageschaden, wirtschaftlicher Schaden) fuer dieses Szenario.

**Aufgabe 2:** Erklaere die 3-2-1-Backup-Regel und begruende, warum sie auch gegen Ransomware schuetzt.

**Aufgabe 3:** Ein Onlineshop speichert Kundendaten (Name, Adresse, Kreditkartendaten). Durch eine SQL-Injection werden 10.000 Datensaetze gestohlen. Welche Meldepflichten bestehen? Nenne die relevanten DSGVO-Artikel und Fristen.

**Aufgabe 4:** Berechne die Ausfallkosten: Ein E-Commerce-Unternehmen hat einen durchschnittlichen Stundenumsatz von 15.000 EUR. Ein DDoS-Angriff legt den Shop fuer 8 Stunden lahm. Nenne die direkten Umsatzeinbussen und erklaere, welche weiteren Kosten entstehen koennen.

**Aufgabe 5:** Ordne die folgenden Szenarien den Risikostufen „Kritisch", „Hoch" und „Mittel" zu und begruende deine Einschaetzung:
(a) Ransomware-Angriff auf ein Krankenhaus
(b) Ausfall einer einzelnen Arbeitsstation
(c) Datenleck mit 500 Kundendatensaetzen bei einem Verein

---
---

# Loesungen

## Aufgabe 1
**Datenverlust:** 7 Tage an Daten sind verloren (alle Aenderungen seit dem letzten Backup). Geschaeftsdokumente, E-Mails, Datenbankeintraege fehlen. **Imageschaden:** Wenn der Vorfall oeffentlich wird (z.B. durch Meldepflicht), verlieren Kunden und Partner Vertrauen. **Wirtschaftlicher Schaden:** Kosten fuer Forensik, ggf. Loesegeld, Produktionsausfall waehrend der Wiederherstellung, evtl. DSGVO-Bussgeld falls personenbezogene Daten betroffen, Umsatzausfall waehrend Downtime.

## Aufgabe 2
3-2-1-Regel: **3 Kopien** der Daten (1 Original + 2 Backups), auf **2 verschiedenen Medientypen** (z.B. lokale Festplatte + Band), davon **1 Kopie extern** (z.B. Cloud oder anderer Standort). Schutz gegen Ransomware: Die externe Kopie (offline/air-gapped) kann von Ransomware nicht erreicht werden, da sie nicht mit dem Netzwerk verbunden ist.

## Aufgabe 3
(1) **DSGVO Art. 33:** Meldung an die zustaendige Datenschutz-Aufsichtsbehoerde **innerhalb von 72 Stunden** nach Bekanntwerden. (2) **DSGVO Art. 34:** Benachrichtigung der **betroffenen 10.000 Kunden** unverzueglich, da ein hohes Risiko fuer persoenliche Rechte besteht (Kreditkartendaten = sensible Finanzdaten). Zusaetzlich: Dokumentation des Vorfalls (Art. 33 Abs. 5).

## Aufgabe 4
**Direkte Umsatzeinbussen:** 15.000 EUR × 8 Stunden = **120.000 EUR**. **Weitere Kosten:** Kosten fuer DDoS-Mitigation/Dienstleister, entgangene Neukunden (die zur Konkurrenz wechseln), Imageschaden (negative Bewertungen), moegliche SLA-Vertragsstrafen gegenueber Geschaeftskunden, Kosten fuer zusaetzliche Schutzmassnahmen nach dem Angriff.

## Aufgabe 5
**(a) Kritisch:** Ransomware im Krankenhaus → Patientendaten unzugaenglich, lebensbedrohliche Situationen moeglich, hoechste Schadenshoehe, hohe Eintrittswahrscheinlichkeit. **(b) Mittel:** Einzelner Arbeitsplatz → geringer Schaden, Nutzer kann auf anderes Geraet wechseln, kurze Ausfallzeit. **(c) Hoch:** 500 Datensaetze bei einem Verein → personenbezogene Daten betroffen, Meldepflicht nach DSGVO, Imageschaden fuer den Verein, aber geringere wirtschaftliche Folgen als bei einem Konzern.
