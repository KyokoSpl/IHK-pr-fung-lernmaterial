# Grundlagen: 4.3.07 – Verhaltensweisen im Brandfall sowie vorbeugender Brandschutz

## Brandmeldung

**Definition:** Die Brandmeldung ist die schnellstmoegliche Information der Feuerwehr und der betrieblichen Brandschutzorganisation ueber einen Brand.

**Kernaussagen:**
- **Handfeuermelder** (roter Kasten mit Glasscheibe) → Scheibe einschlagen, Knopf druecken
- **Automatische Brandmeldeanlage (BMA)** → Rauchmelder, Waermemelder loesen Alarm aus
- **Notruf 112** → Feuerwehr alarmieren (5 W-Fragen)
- **Intern:** Meldekette beachten (Brandschutzhelfer, Vorgesetzter, Etagenbeauftragter)

**Wichtige Begriffe:**
- **Handfeuermelder** – manuell ausgeloester Feueralarm
- **BMA** – Brandmeldeanlage (automatisch oder manuell)
- **Brandschutzhelfer** – ausgebildeter Mitarbeiter fuer Erstmassnahmen (5 % der Belegschaft)

---

## Brandschutzklassen (A/B/C/D/F)

**Definition:** Braende werden nach dem brennenden Stoff in Brandklassen eingeteilt. Jede Brandklasse erfordert ein spezifisches Loeschmittel.

| Brandklasse | Symbol | Brennender Stoff | Beispiele | Geeignetes Loeschmittel |
|-------------|--------|-----------------|-----------|------------------------|
| **A** | Feste Stoffe | Feststoffe (Glutbildner) | Holz, Papier, Textilien, Kunststoffe | Wasser, Schaum, ABC-Pulver |
| **B** | Fluessigkeiten | Fluessige/fluessig werdende Stoffe | Benzin, Oel, Lack, Alkohol, Kunststoff (schmelzend) | Schaum, CO2, ABC-Pulver, BC-Pulver |
| **C** | Gase | Gasfoermige Stoffe | Erdgas, Propan, Wasserstoff, Acetylen | ABC-Pulver, BC-Pulver (Gas zuerst absperren!) |
| **D** | Metalle | Brennbare Metalle | Aluminium, Magnesium, Natrium, Lithium | Metallbrandpulver (KEIN Wasser!) |
| **F** | Speisefette | Speiseoele/-fette (ueberhitzt) | Fritteuse, Pfanne | Spezialloescher Klasse F (KEIN Wasser!) |

**Achtung – Brandklasse D:** Lithium-Ionen-Akkus (Laptops, Smartphones) koennen Metallbraende verursachen! Wasser ist verboten (Knallgasbildung).

---

## Brandschutzmittel (Feuerloescher und Loeschdecken)

**Definition:** Feuerloescher sind tragbare Loeschgeraete zur Bekaempfung von Entstehungsbraenden. Die Wahl des Loeschmittels haengt von der Brandklasse ab.

### Feuerloescher-Typen

| Loeschmittel | Brandklasse | Vorteile | Nachteile | IT-Eignung |
|-------------|-------------|----------|-----------|-----------|
| **Wasser** | A | Guenstig, umweltfreundlich | Nur fuer Glutbraende, elektrisch leitend | ✗ Nicht fuer IT |
| **Schaum** | A, B | Gute Loeschwirkung | Verschmutzt, leitend | ✗ Nicht fuer IT |
| **ABC-Pulver** | A, B, C | Universell einsetzbar | Starke Verschmutzung, Korrosion | ✗ Zerstoert IT-Geraete |
| **CO2** | B | Rueckstandsfrei, nicht leitend | Nur fuer kleine Braende, Erstickungsgefahr | ✓ **Ideal fuer IT** |

**Wichtig fuer IT/Serverraeume:**
- **CO2-Feuerloescher** sind die beste Wahl → rueckstandsfrei, keine Beschaedigung der Hardware
- ABC-Pulverloescher zerstoeren IT-Geraete durch Pulverrueckstaende (Korrosion)
- In grossen Serverraeumen: Gasloschanlagen (Inertgas wie Argon/Stickstoff)

### Loeschdecken
- Fuer kleine Braende (z.B. Papierkorb, Kleidung)
- Loesch-Prinzip: Sauerstoffzufuhr unterbinden (Ersticken)
- Nicht fuer Fettbraende in der Kueche geeignet (Wiederentzuendung)

---

## Brandschutzordnung

**Definition:** Die Brandschutzordnung ist ein betriebliches Regelwerk nach DIN 14096, das das Verhalten im Brandfall und die vorbeugenden Massnahmen festlegt.

### Drei Teile der Brandschutzordnung

| Teil | Zielgruppe | Inhalt | Form |
|------|-----------|--------|------|
| **Teil A** | Alle Personen im Gebaeude (auch Besucher) | Verhalten im Brandfall (Kurzanweisung) | Aushang (DIN A4, gut sichtbar) |
| **Teil B** | Alle Beschaeftigten (ohne besondere Aufgaben) | Detaillierte Verhaltensregeln, Brandverhuetung | Schriftliches Dokument, Unterweisung |
| **Teil C** | Personen mit besonderen Brandschutzaufgaben | Organisation, Brandschutzhelfer, Evakuierung | Internes Dokument |

### Inhalt Teil A (Aushang)

```
  +----------------------------------------------+
  |        VERHALTEN IM BRANDFALL                 |
  |                                               |
  |  BRAND MELDEN:                                |
  |  - Feuermelder betaetigen                     |
  |  - Notruf 112                                 |
  |  - Wo? Was? Wie viele? Welche Gefahren?       |
  |                                               |
  |  IN SICHERHEIT BRINGEN:                       |
  |  - Ruhe bewahren                              |
  |  - Gebaeude ueber Fluchtwege verlassen        |
  |  - Keine Aufzuege benutzen                    |
  |  - Tueren schliessen                          |
  |  - Sammelplatz aufsuchen                      |
  |                                               |
  |  LOESCHVERSUCH UNTERNEHMEN:                   |
  |  - Nur bei Entstehungsbraenden                |
  |  - Feuerloescher benutzen                     |
  |  - Eigene Sicherheit beachten                 |
  +----------------------------------------------+
```

---

## Brandursachen

**Definition:** Brandursachen sind die Faktoren, die einen Brand ausloesen. Die Kenntnis der haeufigsten Ursachen dient der Praevention.

**Haeufige Brandursachen im IT-Bereich:**

| Ursache | Beschreibung | Praevention |
|---------|-------------|-------------|
| Kurzschluss | Defekte Kabel, ueberlastete Steckdosen | DGUV V3-Pruefung, keine Mehrfachsteckdosen kaskadieren |
| Ueberhitzung | Serverlüfter defekt, blockierte Kuehlung | Monitoring, Klimaanlage, regelmaessige Wartung |
| Defekte Akkus | Lithium-Ionen-Akkus (Laptop, Smartphone) | Keine beschaedigten Akkus laden, Herstellervorgaben beachten |
| Unachtsamkeit | Kaffeetasse auf Hardware, Rauchen am Arbeitsplatz | Rauchverbot, Getraenke fernhalten |
| Blitzschlag | Ueberspannung durch Blitzeinschlag | Ueberspannungsschutz, Blitzableiter |
| Elektrostatische Entladung | ESD bei Hardwarearbeiten | ESD-Schutz (Armband, Matte) |

---

## Flucht- und Rettungswege

**Kernaussagen:**
- Kennzeichnung durch gruene Rettungszeichen (ISO 7010, E001/E002)
- Maximale Fluchtweglänge: 35 m (bei normaler Brandgefaehrdung)
- Sicherheitsbeleuchtung bei Stromausfall (min. 1 Lux, 60 min)
- Flucht- und Rettungsplaene in jedem Geschoss (DIN ISO 23601)
- Tueren in Fluchtrichtung oeffnend (Panikbeschlag)

---

## Sammelplaetze

**Kernaussagen:**
- Gekennzeichnet durch Schild E007 (gruenes Rechteck, Personen mit Pfeilen)
- Ausreichend Abstand zum Gebaeude
- Allen Beschaeftigten bekannt (Unterweisung, Aushang)
- Vollzaehligkeitskontrolle muss durchgefuehrt werden
- Sammelplatz erst verlassen, wenn Einsatzleiter es erlaubt

---

## Sicherheitszeichen im Brandschutz

| Zeichen | Kennzeichnung | Farbe | Bedeutung |
|---------|--------------|-------|-----------|
| F001 | Feuerloescher | Rot/Rechteck | Standort eines Feuerloeschers |
| F002 | Loeschwasserhahn | Rot/Rechteck | Wandhydrant |
| F003 | Feuerleiter | Rot/Rechteck | Standort einer Feuerleiter |
| F005 | Brandmelder | Rot/Rechteck | Standort eines Handfeuermelders |
| E001 | Notausgang (links/rechts) | Gruen/Rechteck | Richtung zum Notausgang |
| E002 | Sammelstelle | Gruen/Rechteck | Sammelplatz nach Evakuierung |
