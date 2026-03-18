# Vertiefung: 1.1.03 – Arbeitsaufgaben im Rahmen von Geschaefts- und Leistungsprozessen

## Bearbeitungsstatus – Vertiefung

### Lebenszyklus eines Tickets

```
Neu → Zugewiesen → In Bearbeitung → Wartend → Geloest → Geschlossen
                                        ↓
                                   Eskaliert → Zugewiesen (naechstes Level)
```

### Zusammenhang zu anderen Themen
- **SLA** (Thema 3.1.12): Ticketsysteme muessen SLA-Zeiten ueberwachen
- **Qualitaetssicherung** (Thema 1.5.02): Ticketstatistiken dienen der Qualitaetsmessung
- **Monitoring** (Thema 3.1.11): Automatische Ticketerstellung bei Schwellwertueberschreitung

### Typische Pruefungsaspekte
- Ticketstatus-Uebergaenge beschreiben
- Vorteile eines Ticketsystems gegenueber informeller Kommunikation (E-Mail, Anruf) benennen
- Priorisierungskriterien erlaeutern

### Haeufige Fehler
- Tickets werden geloest, aber nicht geschlossen → Statistik verfaelscht
- Fehlende Dokumentation im Ticket → Nachvollziehbarkeit geht verloren

---

## Fehlermanagement – Vertiefung

### Fehlerklassifizierung

| Schweregrad | Beschreibung | Beispiel |
|-------------|-------------|----------|
| Kritisch | System komplett ausgefallen | Datenbankserver nicht erreichbar |
| Hoch | Wichtige Funktion eingeschraenkt | E-Mail-Versand funktioniert nicht |
| Mittel | Teilfunktion betroffen | Drucken ueber Netzwerk langsam |
| Niedrig | Kosmetischer Fehler, keine Auswirkung auf Betrieb | Falsches Icon in der Anwendung |

### Zusammenhang zu anderen Themen
- **PDCA-Zyklus** (Thema 1.5.02): Fehlermanagement ist Teil der Check- und Act-Phase
- **Debugging** (Thema 2.2.01): Technische Fehlersuche in Softwaresystemen
- **Testverfahren** (Thema 2.3.01): Fehler durch Tests frueh erkennen

### Typische Pruefungsaspekte
- Unterschied zwischen Workaround und dauerhafter Loesung erklaeren
- Fehler nach Schweregrad klassifizieren
- Dokumentationsanforderungen benennen

### Haeufige Fehler
- Workaround wird als Loesung markiert → Fehler tritt erneut auf
- Root Cause wird nicht analysiert → Symptombehandlung statt Ursachenbeseitigung

---

## KI-Unterstuetzung – Vertiefung

### Einsatzbereiche von KI im IT-Betrieb

| Bereich | KI-Anwendung | Nutzen |
|---------|-------------|--------|
| Support | Chatbot fuer Erstanfragen | Entlastung des 1st-Level-Supports |
| Monitoring | Anomalieerkennung | Fruehe Stoerungserkennung |
| Fehlermanagement | Automatische Kategorisierung | Schnellere Zuweisung |
| Wartung | Predictive Maintenance | Ausfaelle verhindern |
| Entwicklung | Code-Analyse, Code-Generierung | Qualitaetssteigerung, Effizienz |

### Zusammenhang zu anderen Themen
- **Predictive Maintenance** (Thema 3.1.11): KI-basierte Vorhersage von Systemausfaellen
- **KI-Software** (Thema 1.3.01): KI als Softwareprodukt im Markt
- **Automatisierung** (Thema 3.3.07): Skripte und KI zur Automatisierung

### Typische Pruefungsaspekte
- Einsatzmoeglichkeiten von KI im IT-Betrieb benennen
- Grenzen von KI einschaetzen (z.B. komplexe Entscheidungen, ethische Fragen)
- Zusammenspiel von KI und menschlichem Support beschreiben

### Haeufige Fehler
- KI wird als Allzweckloesung dargestellt → sie ergaenzt, ersetzt nicht
- Datenschutzaspekte beim KI-Einsatz werden vergessen (siehe Thema 1.6.01)

---

## Kundenkommunikation – Vertiefung

### Kommunikationsregeln im IT-Support

| Grundsatz | Umsetzung |
|-----------|-----------|
| Verstaendlichkeit | Fachbegriffe erklaeren oder vermeiden |
| Transparenz | Ueber Status und naechste Schritte informieren |
| Zuverlaessigkeit | Zusagen einhalten, bei Verzoegerung informieren |
| Loesungsorientierung | Auf Loesungen fokussieren, nicht auf Schuldzuweisungen |

### Zusammenhang zu anderen Themen
- **Kommunikationsmodelle** (Thema 1.2.03): 4-Ohren-Modell, Sender-Empfaenger-Modell
- **Praesentation** (Thema 1.2.04): Informationen aufbereiten und verstaendlich darstellen
- **Nettikette** (Thema 4.5.02): Professionelle digitale Kommunikation

### Typische Pruefungsaspekte
- Professionelle Statusmeldung an einen Kunden formulieren
- Fachbegriffe kundengerecht uebersetzen
- Deeskalation bei unzufriedenen Kunden beschreiben

### Haeufige Fehler
- Zu viel Fachsprache gegenueber Nicht-IT-Kunden
- Keine Rueckmeldung zum Bearbeitungsstand → Kunde fragt wiederholt nach

---

## Stoerungs-Management – Vertiefung

### Incident Management vs. Problem Management

| Aspekt | Incident Management | Problem Management |
|--------|-------------------|--------------------|
| Ziel | Schnelle Wiederherstellung | Dauerhafte Ursachenbeseitigung |
| Zeitrahmen | Sofort | Mittelfristig |
| Ergebnis | Workaround oder Fix | Root Cause und dauerhafte Loesung |
| Beispiel | Server neu starten | Fehlerhafte Konfiguration korrigieren |

### Zusammenhang zu anderen Themen
- **SLA** (Thema 3.1.12): Reaktions- und Loesungszeiten sind vertraglich geregelt
- **Notfallkonzept** (Thema 3.1.09): Disaster Recovery bei schwerwiegenden Stoerungen
- **Monitoring** (Thema 3.1.11): Stoerungen frueh erkennen

### Typische Pruefungsaspekte
- Ablauf des Stoerungsmanagements beschreiben
- Major Incident von normaler Stoerung unterscheiden
- Priorisierungskriterien anwenden

### Haeufige Fehler
- Incident Management und Problem Management werden verwechselt
- Stoerungen werden nicht dokumentiert → Muster bleiben unerkannt

---

## Supportlevel – Vertiefung

### Eskalationsmatrix

| Kriterium | 1st Level | 2nd Level | 3rd Level |
|-----------|-----------|-----------|-----------|
| Kompetenz | Basis | Spezialisiert | Experte/Hersteller |
| Bearbeitungszeit | Sofort (< 30 Min.) | Stunden | Tage/Wochen |
| Beispiel | Passwort-Reset | Netzwerkdiagnose | Softwarepatch entwickeln |
| Eskalation bei | Problem nicht loesbar | Problem nicht loesbar | – |

### Zusammenhang zu anderen Themen
- **Service Level Agreement** (Thema 3.1.12): SLA definiert Zeiten je Supportlevel
- **Ticket-Workflow** (siehe oben): Eskalation aendert Ticketstatus
- **Wissensdatenbank:** Gesammelte Loesungen reduzieren Eskalationen

### Typische Pruefungsaspekte
- Support-Levels mit Aufgaben und Beispielen beschreiben
- Eskalation anhand eines Szenarios begruenden
- Unterschied zwischen funktionaler und hierarchischer Eskalation

### Haeufige Fehler
- Annahme, dass jede Anfrage alle Level durchlaufen muss → die meisten werden im 1st Level geloest
- Funktionale Eskalation (an Spezialisten) wird mit hierarchischer Eskalation (an Vorgesetzten) verwechselt
