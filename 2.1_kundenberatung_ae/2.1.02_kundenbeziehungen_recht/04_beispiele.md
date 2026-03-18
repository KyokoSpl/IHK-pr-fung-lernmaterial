# Beispiele: 2.1.02 – Kundenbeziehungen unter Beachtung rechtlicher Regelungen

## Beispiel 1: AGB in der Praxis

Ein IT-Systemhaus verkauft Server an ein mittelstaendisches Unternehmen. Im Angebot stehen die AGB des Systemhauses.

**Situation:** Der Kunde reklamiert nach 3 Monaten einen defekten RAID-Controller.

| Schritt | Aktion |
|---|---|
| 1. AGB pruefen | Gewaehrleistungsklausel: "2 Jahre gemaess §437 BGB" → gueltig |
| 2. HGB beachten | Beide sind Kaufleute → Ruegeobliegenheit nach §377 HGB |
| 3. Ruege pruefen | Reklamation nach 3 Monaten → War der Mangel bei Lieferung erkennbar? |
| 4. Entscheidung | Verdeckter Mangel → Reklamation rechtzeitig, Nacherfuellung leisten |

---

## Beispiel 2: CRM-Einsatz bei IT-Dienstleister

**Ausgangslage:** Ein IT-Dienstleister betreut 200 Firmenkunden mit unterschiedlichen SLA-Stufen.

**CRM-System Konfiguration:**

```
Kundendatensatz:
+----------------------------------+
| Firma: Mueller GmbH              |
| Ansprechpartner: Max Mueller      |
| SLA-Stufe: Premium (4h Reaktion) |
| Vertragslaufzeit: 01.01-31.12    |
| Offene Tickets: 2                |
| Letzte Kontaktaufnahme: 15.03    |
| Umsatz YTD: 45.000 €            |
| Cross-Sell-Potenzial: Cloud-     |
|   Migration, Backup-Loesung      |
+----------------------------------+
```

**Nutzen:**
- Servicemitarbeiter sehen sofort die SLA-Stufe und reagieren priorisiert
- Vertrieb erkennt Cross-Selling-Potenzial
- Management erhaelt Umsatz- und Zufriedenheitsreports

---

## Beispiel 3: UWG-konformes Marketing

Ein Softwareunternehmen plant eine Marketingkampagne fuer sein neues ERP-System.

**Pruefung der Werbemassnahmen:**

| Massnahme | UWG-konform? | Begruendung |
|---|---|---|
| "Marktfuehrender ERP-Anbieter" | Nein (wenn kein Beleg) | Irrefuehrende Spitzenstellung |
| "95% Kundenzufriedenheit (n=500)" | Ja | Belegbare Aussage mit Quelle |
| Wettbewerber namentlich schlecht machen | Nein | Unzulaessige Herabsetzung |
| Feature-Vergleichstabelle (sachlich) | Ja | Zulaessige vergleichende Werbung |
| Unaufgeforderter Werbeanruf bei Firmen | Nein (ohne Einwilligung) | Unzumutbare Belaestigung |

---

## Beispiel 4: Compliance im Softwareprojekt

**Szenario:** Ein Entwicklungsteam erstellt eine Webanwendung fuer eine Arztpraxis (Patientenverwaltung).

**Compliance-Checkliste:**

| Bereich | Anforderung | Massnahme |
|---|---|---|
| DSGVO | Personenbezogene Daten schuetzen | Verschluesselung, Zugriffskontrollen |
| AVV | Auftragsverarbeitung regeln | Vertrag nach Art. 28 DSGVO |
| Dokumentation | Verarbeitungsverzeichnis | Art. 30 DSGVO einhalten |
| Loeschkonzept | Daten nach Zweckerfuellung loeschen | Aufbewahrungsfristen beachten |
| Betroffenenrechte | Auskunft, Loeschung ermoeglichen | Export-/Loeschfunktion einbauen |
| Lizenzrecht | Open-Source-Lizenzen beachten | License-Audit durchfuehren |
