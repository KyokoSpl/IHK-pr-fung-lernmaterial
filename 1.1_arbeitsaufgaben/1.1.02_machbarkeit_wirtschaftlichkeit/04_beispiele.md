# Beispiele: 1.1.02 – Machbarkeit und Wirtschaftlichkeit von Projekten

## Einfluss der Stakeholder

**Beispiel 1:** Ein Unternehmen plant die Einfuehrung eines neuen ERP-Systems. Stakeholder sind: Geschaeftsfuehrung (hoher Einfluss, hohes Interesse), IT-Abteilung (hoher Einfluss, hohes Interesse), Endanwender in der Buchhaltung (niedriger Einfluss, hohes Interesse), externer Softwarelieferant (hoher Einfluss, mittleres Interesse). Die Geschaeftsfuehrung und IT-Abteilung muessen eng eingebunden werden. Die Buchhaltung wird regelmaessig informiert.

**Beispiel 2:** Bei der Migration eines Webshops auf eine neue Plattform vergisst das Projektteam, den Datenschutzbeauftragten als Stakeholder einzubeziehen. Erst kurz vor Go-Live stellt sich heraus, dass die neue Plattform nicht DSGVO-konform konfiguriert ist. → Start verschoben. Lektion: Alle relevanten Stakeholder frueh identifizieren.

---

## Machbarkeitsanalyse

**Beispiel 1:** Ein Kunde moechte eine mobile App fuer iOS und Android innerhalb von 3 Monaten mit einem Budget von 20.000 EUR entwickeln lassen. Das Entwicklungsteam besteht aus zwei Personen. Pruefung:
- Technisch: Machbar (Frameworks wie Flutter ermoeglichen Cross-Platform-Entwicklung)
- Wirtschaftlich: Kritisch (20.000 EUR fuer 2 Entwickler in 3 Monaten ist knapp)
- Zeitlich: Riskant (bei Vollzeit moeglicherweise machbar, aber ohne Puffer)
- → Empfehlung: Funktionsumfang reduzieren oder Budget erhoehen.

**Beispiel 2:** Ein Unternehmen plant die Anbindung seiner lokalen Server an eine Cloud-Loesung. Budget: 50.000 EUR. Das Team hat keine Cloud-Erfahrung. → Organisatorische Machbarkeit fraglich. Massnahme: Schulung oder externen Dienstleister einbinden, Kosten neu kalkulieren.

---

## Risikoanalyse

**Beispiel 1:** Projekt: Einfuehrung eines neuen Ticketsystems.

| Risiko | Wahrscheinlichkeit | Schaden | Einstufung | Massnahme |
|--------|-------------------|---------|------------|-----------|
| Serverausfall waehrend Migration | Gering | Hoch | Mittel | Backup vor Migration, Fallback-Plan |
| Mitarbeiter verweigern Nutzung | Mittel | Mittel | Mittel | Schulung, Einbindung der Mitarbeiter |
| Datenverlust bei Migration | Gering | Hoch | Mittel | Testmigration im Vorfeld |
| Lizenzverzug durch Lieferant | Mittel | Gering | Gering | Alternativanbieter vorhalten |

**Beispiel 2:** Bei der Entwicklung einer Webanwendung faellt der leitende Entwickler fuer 4 Wochen aus (Risiko: Personalausfall). Eintrittswahrscheinlichkeit: Mittel. Schaden: Hoch (Terminverschiebung). Massnahme: Wissenstransfer sicherstellen, zweiten Entwickler einarbeiten.

---

## Vor- und Nachkalkulation

**Beispiel 1 – Vorkalkulation:**
Projekt: Einrichtung von 50 Arbeitsplaetzen.

| Kostenart | Betrag |
|-----------|--------|
| Hardware (50 PCs) | 35.000 EUR |
| Software-Lizenzen | 8.000 EUR |
| Netzwerkinfrastruktur | 5.000 EUR |
| Personalkosten (Installation, 10 Tage, 2 Mitarbeiter) | 6.000 EUR |
| Risikozuschlag (10%) | 5.400 EUR |
| **Gesamtkosten (Soll)** | **59.400 EUR** |

**Beispiel 2 – Nachkalkulation:**
Nach Projektabschluss:

| Kostenart | Soll | Ist | Abweichung |
|-----------|------|-----|------------|
| Hardware | 35.000 | 36.500 | +1.500 (Preiserhoehung) |
| Software-Lizenzen | 8.000 | 8.000 | 0 |
| Netzwerk | 5.000 | 4.200 | -800 (guenstigerer Anbieter) |
| Personal | 6.000 | 8.400 | +2.400 (Ueberstunden) |
| **Gesamt** | **54.000** | **57.100** | **+3.100 (+5,7%)** |

Ergebnis: Die Abweichung liegt innerhalb des Risikozuschlags (5.400 EUR). Das Projekt ist wirtschaftlich im Rahmen geblieben.
