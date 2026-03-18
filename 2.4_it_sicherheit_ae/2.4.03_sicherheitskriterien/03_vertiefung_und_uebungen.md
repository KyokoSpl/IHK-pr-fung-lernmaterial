# Vertiefung und Uebungen: 2.4.03 – Ziele zur Entwicklung von IT-Sicherheitskriterien

## Vertiefung

### Vergleich der drei Ziele

| Kriterium | Objektive Bewertung | Richtschnur Entwickler | Anwenderunterstuetzung |
|---|---|---|---|
| Zielgruppe | IT-Sicherheitsbeauftragte, Auditoren | Softwareentwickler, Architekten | Anwender, Entscheider, Beschaffer |
| Fokus | Ist-Zustand bewerten | Sichere Entwicklung | Produktauswahl, Vergleich |
| Methodik | IT-Grundschutz, Risikoanalyse | OWASP, Secure Coding | Common Criteria, Zertifikate |
| Ergebnis | Massnahmenkatalog, Zertifikat | Sicherer Code, weniger Schwachstellen | Informierte Kaufentscheidung |
| Standard | BSI IT-Grundschutz-Kompendium | OWASP Top 10, CWE | Common Criteria (ISO 15408) |

### IT-Grundschutz-Vorgehensmodell

```
+--------------------+
| 1. Strukturanalyse |
| (IT-Inventar)      |
+--------+-----------+
         |
         v
+--------+-----------+
| 2. Schutzbedarf    |
| (normal/hoch/      |
|  sehr hoch)        |
+--------+-----------+
         |
         v
+--------+-----------+
| 3. Modellierung    |
| (Bausteine         |
|  zuordnen)         |
+--------+-----------+
         |
         v
+--------+-----------+
| 4. IT-Grundschutz- |
| Check (Soll/Ist)   |
+--------+-----------+
         |
         v
+--------+-----------+     +-------------------+
| 5. Risikoanalyse   +---->| Massnahmenplan    |
| (bei hohem         |     | (Umsetzung)       |
|  Schutzbedarf)     |     +-------------------+
+--------------------+
```

### Security by Design vs. Security by Obscurity

| Aspekt | Security by Design | Security by Obscurity |
|---|---|---|
| Ansatz | Sicherheit eingebaut | Sicherheit durch Geheimhaltung |
| Transparenz | Offen, nachpruefbar | Verborgen, intransparent |
| Nachhaltigkeit | Langfristig sicher | Unsicher, sobald Geheimnis bekannt |
| Beispiel | Verschluesselung (AES) | Versteckte Admin-URL |
| Bewertung | Best Practice | Nicht empfohlen (allein unzureichend) |

### Zusammenhang: Sicherheitskriterien im Lebenszyklus

```
  Planung     Entwicklung     Test        Betrieb       Ausserbetrieb
  +-------+   +-----------+   +-------+   +---------+   +-----------+
  |Security|   |Secure     |   |Penetra|   |IT-Grund-|   |Sichere    |
  |by      |-->|Coding,    |-->|tions- |-->|schutz-  |-->|Daten-     |
  |Design  |   |OWASP,     |   |tests, |   |Check,   |   |loeschung, |
  |Privacy |   |Code Review|   |Audit  |   |Monitoring|  |Entsorgung |
  |by      |   |           |   |       |   |         |   |           |
  |Design  |   |           |   |       |   |         |   |           |
  +-------+   +-----------+   +-------+   +---------+   +-----------+
```

### Typische Pruefungsaspekte
- IT-Grundschutz-Vorgehensmodell in den Schritten beschreiben
- Unterschied Schutzbedarf normal/hoch/sehr hoch an Beispielen
- OWASP Top 10: typische Schwachstellen benennen und Gegenmassnahmen
- Security by Design vs. Security by Obscurity unterscheiden
- Common Criteria (EAL-Stufen) erklaeren
- Privacy by Design (DSGVO Art. 25) in eigenem Softwareprojekt anwenden

### Haeufige Fehler
- IT-Grundschutz = nur Checkliste → Es ist ein umfassendes Vorgehensmodell mit Risikoanalyse
- Security by Design = nur Verschluesselung → Umfasst das gesamte System (Architektur, Defaults, Rechte)
- OWASP Top 10 = Pruefungsliste → Es ist eine Risikobewertung, keine Checkliste
- Common Criteria EAL = je hoeher desto besser → EAL 4 ist Standard, hoehere Stufen nur fuer spezielle Anwendungen

---

## Uebungen

**Aufgabe 1:** Beschreibe die fuenf Schritte des IT-Grundschutz-Vorgehensmodells in eigenen Worten.

**Aufgabe 2:** Ein Unternehmen betreibt ein internes Wiki fuer Mitarbeiter und ein Onlinebanking-System. Ordne beiden Systemen den passenden Schutzbedarf zu (normal, hoch, sehr hoch) und begruende.

**Aufgabe 3:** Ein Entwickler behandelt Benutzereingaben in einem Webformular nicht. Welche OWASP-Schwachstelle liegt vor? Nenne die konkrete Gegenmassnahme (Secure Coding Prinzip).

**Aufgabe 4:** Erklaere den Unterschied zwischen „Security by Design" und „Security by Obscurity". Nenne je ein Beispiel und bewerte beide Ansaetze.

**Aufgabe 5:** Ein Kunde fragt, woran er erkennen kann, ob ein IT-Produkt sicher ist. Nenne drei Zertifizierungen oder Kennzeichen, die ihm bei der Auswahl helfen.

---
---

# Loesungen

## Aufgabe 1
(1) **Strukturanalyse:** Alle IT-Systeme, Anwendungen, Netzwerke und Raeume werden erfasst und dokumentiert (IT-Inventar). (2) **Schutzbedarfsfeststellung:** Fuer jedes erfasste Objekt wird der Schutzbedarf bewertet (normal, hoch, sehr hoch) basierend auf moeglichen Schaeden bei Verletzung der Schutzziele. (3) **Modellierung:** Passende Bausteine aus dem BSI IT-Grundschutz-Kompendium werden den Objekten zugeordnet (z.B. Baustein „Server" fuer jeden Server). (4) **IT-Grundschutz-Check:** Soll-Ist-Vergleich – welche Massnahmen aus den Bausteinen sind bereits umgesetzt, welche fehlen noch? (5) **Risikoanalyse:** Fuer Objekte mit hohem oder sehr hohem Schutzbedarf wird eine ergaenzende Risikoanalyse durchgefuehrt, um spezifische Bedrohungen zu bewerten.

## Aufgabe 2
**Internes Wiki:** Schutzbedarf **normal** – bei Ausfall oder Kompromittierung sind die Auswirkungen begrenzt (Mitarbeiter koennen kurzzeitig ohne Wiki arbeiten, keine kritischen Daten). **Onlinebanking-System:** Schutzbedarf **sehr hoch** – Verletzung der Vertraulichkeit (Kontodaten), Integritaet (Manipulierte Transaktionen) oder Verfuegbarkeit (Kunden koennen nicht auf Konten zugreifen) hat existenzbedrohende Auswirkungen (Finanzverluste, regulatorische Konsequenzen).

## Aufgabe 3
**Schwachstelle:** Injection (OWASP Top 10, Rang 3) – konkret SQL-Injection oder Cross-Site Scripting (XSS). **Gegenmassnahme:** Input Validation – alle Benutzereingaben muessen serverseitig geprueft, bereinigt und parametrisiert werden. Bei SQL: Prepared Statements/Parameterized Queries verwenden. Bei HTML-Ausgabe: Output Encoding (z.B. HTML-Entities).

## Aufgabe 4
**Security by Design:** Sicherheit wird von Anfang an in die Architektur eingebaut. Beispiel: Verschluesselung aller Daten mit AES-256, Zugriffskontrolle per Rollenkonzept. **Security by Obscurity:** Sicherheit beruht auf Geheimhaltung von Details. Beispiel: Admin-Panel ist nur ueber eine geheime URL erreichbar. **Bewertung:** Security by Design ist Best Practice – auch bei Offenlegung des Designs bleibt das System sicher. Security by Obscurity allein ist unzureichend – sobald das Geheimnis bekannt wird, ist der Schutz weg. Kann nur als ergaenzende Massnahme dienen.

## Aufgabe 5
(1) **ISO/IEC 27001-Zertifizierung:** Nachweis eines funktionierenden ISMS beim Anbieter. (2) **Common Criteria (CC) Zertifizierung:** Internationale Bewertung der Produktsicherheit mit EAL-Stufen. (3) **BSI IT-Sicherheitskennzeichen:** Verbraucherfreundliches Kennzeichen des BSI fuer IT-Produkte (z.B. Router, Smart-Home-Geraete).
