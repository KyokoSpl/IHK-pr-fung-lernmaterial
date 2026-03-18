# Vertiefung: 2.4.04 – Kunden zur IT-Sicherheit beraten

## Bedrohungsszenarien im Vergleich

| Kriterium | Man-in-the-Middle | SQL-Injection | DDoS |
|---|---|---|---|
| Angriffstyp | Passiv/Aktiv | Aktiv (Webanwendung) | Aktiv (Netzwerk) |
| Schutzziel | Vertraulichkeit, Integritaet | Vertraulichkeit, Integritaet | Verfuegbarkeit |
| Komplexitaet | Mittel | Gering (automatisierbar) | Hoch (Botnet noetig) |
| Erkennung | Schwer (verschleiert) | WAF-Logs, IDS | Traffic-Analyse, CDN |
| Gegenmassnahme | TLS, VPN, Zertifikate | Prepared Statements, WAF | DDoS-Mitigation, CDN |

## Kundengruppen im Vergleich

| Aspekt | Private Haushalte | Unternehmen | Oeffentliche Hand |
|---|---|---|---|
| Budget | Gering | Mittel bis hoch | Haushaltsmittel (fix) |
| IT-Kenntnisse | Gering bis mittel | Mittel bis hoch | Unterschiedlich |
| Regulierung | Gering (DSGVO privat) | DSGVO, BDSG, branchenspezifisch | BSI, KRITIS, NIS2 |
| Angriffsziel | Einzelperson | Geschaeftsdaten, IP | Buerger-/Verwaltungsdaten |
| Typische Loesung | Router, Virenscanner, Backup | ISMS, Firewall, VPN, EDR | IT-Grundschutz, BSI-Konformitaet |
| Beratungstiefe | Einfach, verstaendlich | Detailliert, technisch | Formal, nach Standards |

## Risikoanalyse-Prozess

```
+--------------------+
| 1. Assets          |
| identifizieren     |
| (Was schuetzen?)   |
+--------+-----------+
         |
         v
+--------+-----------+
| 2. Bedrohungen     |
| identifizieren     |
| (Was kann passie-  |
|  ren?)             |
+--------+-----------+
         |
         v
+--------+-----------+
| 3. Schwachstellen  |
| identifizieren     |
| (Wo sind wir       |
|  verwundbar?)      |
+--------+-----------+
         |
         v
+--------+-----------+
| 4. Risiko bewerten |
| (Wahrscheinlich-   |
|  keit × Schaden)   |
+--------+-----------+
         |
         v
+--------+-----------+
| 5. Massnahmen      |         +---> Vermeiden
| ableiten           +---------+---> Vermindern
| (Was tun?)         |         +---> Uebertragen
+--------------------+         +---> Akzeptieren
```

## Risikomatrix

```
Schadenshoehe
    ^
    |
sehr|  Mittel    Hoch      Kritisch  Kritisch
hoch|
    |
hoch|  Gering    Mittel    Hoch      Kritisch
    |
mit-|  Gering    Gering    Mittel    Hoch
tel |
    |
ge- |  Gering    Gering    Gering    Mittel
ring|
    +------+------+------+------+---->
         gering   mittel   hoch   sehr hoch
                Eintrittswahrscheinlichkeit
```

## TOM nach DSGVO Art. 32 – Uebersicht

```
+--------------------------------------------------+
|        Technisch-organisatorische Massnahmen      |
+--------------------------------------------------+
|                                                    |
|  +------------------+  +----------------------+   |
|  | Zutritts-        |  | Zugangs-             |   |
|  | kontrolle        |  | kontrolle            |   |
|  | (Gebaeude)       |  | (Systeme)            |   |
|  +------------------+  +----------------------+   |
|                                                    |
|  +------------------+  +----------------------+   |
|  | Zugriffs-        |  | Weitergabe-          |   |
|  | kontrolle        |  | kontrolle            |   |
|  | (Daten)          |  | (Transport)          |   |
|  +------------------+  +----------------------+   |
|                                                    |
|  +------------------+  +----------------------+   |
|  | Eingabe-         |  | Verfuegbarkeits-     |   |
|  | kontrolle        |  | kontrolle            |   |
|  +------------------+  +----------------------+   |
|                                                    |
|  +------------------------------------------+     |
|  | Trennungskontrolle (Mandantentrennung)    |     |
|  +------------------------------------------+     |
+--------------------------------------------------+
```

## Rahmenbedingungen im Detail

### Rechtliche Rahmenbedingungen

| Gesetz/Verordnung | Relevanz |
|---|---|
| DSGVO | Schutz personenbezogener Daten, TOM-Pflicht (Art. 32) |
| BDSG | Nationale Ergaenzung zur DSGVO |
| IT-Sicherheitsgesetz 2.0 | KRITIS-Betreiber: IT-Sicherheit nachweisen, Meldepflicht |
| NIS2-Richtlinie | EU-weit: erweiterte Pflichten, hoehere Bussgelder |
| TMG / TTDSG | Telemedien: Cookie-Consent, Tracking |
| GoBD | Ordnungsmaessige Buchfuehrung, revisionssichere Archivierung |

### Ethische Aspekte

| Aspekt | Beschreibung |
|---|---|
| Verhaeltnismaessigkeit | Sicherheitsmassnahmen muessen angemessen sein (kein Totalueberwachung) |
| Transparenz | Mitarbeiter/Kunden muessen ueber Massnahmen informiert werden |
| Datensparsamkeit | Nur notwendige Daten erheben und verarbeiten |
| Mitarbeiterschutz | Ueberwachungsmassnahmen duerfen Persoenlichkeitsrechte nicht verletzen |
| Diskriminierungsfreiheit | KI-basierte Sicherheitsloesungen duerfen nicht diskriminieren |

## Typische Pruefungsaspekte
- Bedrohungsszenarien erkennen und Gegenmassnahmen zuordnen
- SQL-Injection: Angriff und Gegenmassnahme (Prepared Statements) erklaeren
- Risikoanalyse durchfuehren: Risiko = Eintrittswahrscheinlichkeit × Schadenshoehe
- TOM den Kategorien zuordnen (Zutritt, Zugang, Zugriff)
- Kundenberatung: passende Massnahmen fuer verschiedene Kundengruppen empfehlen
- Rahmenbedingungen (technologisch, organisatorisch, rechtlich, ethisch) benennen
- Unterschied interne vs. externe Bedrohungen

## Haeufige Fehler
- DDoS = ein einzelner Angreifer → DDoS nutzt tausende Geraete (Botnet), DoS ist ein einzelner
- SQL-Injection = nur bei MySQL → Betrifft alle Datenbanken ohne Prepared Statements
- TOM = nur technisch → Organisatorische Massnahmen (Richtlinien, Schulungen) gehoeren dazu
- Risikoanalyse = einmalig → Muss regelmaessig wiederholt werden
- Ethik = unwichtig fuer IT-Sicherheit → Verhaeltnismaessigkeit und Datenschutz sind pruefungsrelevant
