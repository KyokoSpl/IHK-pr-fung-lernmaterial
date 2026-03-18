# Beispiele: 4.2.03 – Unternehmensstruktur und Organisationsform

## Beispiel 1: Einliniensystem in einem kleinen IT-Systemhaus

**Szenario:** Die "NetSolutions GmbH" ist ein IT-Systemhaus mit 20 Mitarbeitern. Der Geschaeftsfuehrer leitet drei Abteilungen direkt: Vertrieb (4 MA), Technik (10 MA) und Verwaltung (5 MA). Jeder Abteilungsleiter weist seinen Mitarbeitern Aufgaben zu.

**Organigramm:**
```
            +---------------------+
            | Geschaeftsfuehrer   |
            | Hr. Mueller         |
            +---------------------+
           /          |            \
          v           v             v
  +-----------+  +-----------+  +-----------+
  | Vertrieb  |  |  Technik  |  | Verwaltung|
  | Fr. Weber |  | Hr. Braun |  | Fr. Klein |
  | (4 MA)    |  | (10 MA)   |  | (5 MA)    |
  +-----------+  +-----------+  +-----------+
```

**Analyse:**
- Organisationsform: **Einliniensystem**
- Jeder MA hat genau einen Vorgesetzten
- Abteilungsleiter berichten direkt an Geschaeftsfuehrer
- Vorteil: Klare Verantwortlichkeiten fuer 20 MA gut geeignet
- Nachteil: Wenn ein Techniker eine kaufmaennische Frage hat, muss der Weg ueber Hr. Braun → Hr. Mueller → Fr. Klein gehen

---

## Beispiel 2: Matrixorganisation in einem Softwareunternehmen

**Szenario:** Die "DevPro AG" entwickelt drei Produkte: ERP-Software, CRM-Software und Cloud-Plattform. Gleichzeitig gibt es vier Fachabteilungen: Entwicklung, QA/Testing, UX-Design und DevOps. Jeder Mitarbeiter gehoert einem Produktteam UND einer Fachabteilung an.

**Matrixstruktur:**

| | ERP-Produkt | CRM-Produkt | Cloud-Plattform |
|---|------------|------------|----------------|
| **Entwicklung** | 5 Entwickler | 4 Entwickler | 6 Entwickler |
| **QA/Testing** | 2 Tester | 2 Tester | 3 Tester |
| **UX-Design** | 1 Designer | 1 Designer | 2 Designer |
| **DevOps** | 1 DevOps-Ing. | 1 DevOps-Ing. | 2 DevOps-Ing. |

**Analyse:**
- Ein Entwickler im ERP-Team berichtet an den **Leiter Entwicklung** (Fachvorgesetzter) UND an den **Produktmanager ERP** (Produktvorgesetzter)
- Vorteil: Entwickler bringt Fachwissen ein UND kennt die Produkt-Anforderungen
- Nachteil: Wenn Leiter Entwicklung eine Codequalitaets-Initiative startet und der ERP-Produktmanager gleichzeitig ein Featurerelease fordert, entsteht ein **Matrixkonflikt**

---

## Beispiel 3: Spartenorganisation bei einem IT-Konzern

**Szenario:** Die "TechGlobal AG" ist ein grosser IT-Konzern mit drei Geschaeftsbereichen: Business Software, Consumer Electronics und Cloud Services. Jede Sparte hat eigene Entwicklung, Vertrieb und Support.

**Organigramm:**
```
                 +---------------------+
                 | Vorstand TechGlobal |
                 +---------------------+
                /          |            \
               v           v             v
+----------------+ +----------------+ +----------------+
| Sparte:        | | Sparte:        | | Sparte:        |
| Business SW    | | Consumer Elec. | | Cloud Services |
+----------------+ +----------------+ +----------------+
| Entwicklung    | | Entwicklung    | | Entwicklung    |
| Vertrieb       | | Vertrieb       | | Vertrieb       |
| Support        | | Support        | | Support        |
| Controlling    | | Controlling    | | Controlling    |
+----------------+ +----------------+ +----------------+
```

**Analyse:**
- Jede Sparte agiert wie ein eigenes Unternehmen (Profit Center)
- Vorteil: Cloud Services kann schnell auf Marktveraenderungen reagieren, ohne auf Business SW warten zu muessen
- Nachteil: Drei separate Entwicklungsabteilungen → moeglicherweise redundante Arbeiten, z.B. drei verschiedene Login-Systeme statt eines einheitlichen

---

## Beispiel 4: Stab-Liniensystem mit IT-Sicherheit als Stabsstelle

**Szenario:** Ein mittelstaendisches Unternehmen hat ein Einliniensystem. Die Geschaeftsfuehrung richtet eine Stabsstelle "IT-Sicherheit" ein, die die Geschaeftsfuehrung in Sicherheitsfragen beraet.

```
            +---------------------+---[ Stab: IT-Sicherheit ]
            | Geschaeftsfuehrer   |---[ Stab: Datenschutz   ]
            +---------------------+
           /          |            \
          v           v             v
  +-----------+  +-----------+  +-----------+
  | Produktion|  |    IT     |  |  Vertrieb |
  +-----------+  +-----------+  +-----------+
```

**Analyse:**
- IT-Sicherheit und Datenschutz beraten die GF, haben aber **kein Weisungsrecht** gegenueber IT oder Produktion
- Die IT-Sicherheitsstelle erstellt Richtlinien, die die GF als Anweisung an die Abteilungen weitergibt
- Typisches Problem: IT-Abteilung empfindet die Stabsstelle als "Einmischung" → Kommunikation muss klar geregelt sein

---

## Beispiel 5: Ablauf- vs. Aufbauorganisation am Beispiel Ticketsystem

**Aufbauorganisation (WER):**
```
  IT-Leiter
  ├── First-Level-Support (3 MA)
  ├── Second-Level-Support (2 MA)
  └── Administration (2 MA)
```

**Ablauforganisation (WIE):**
```
  Kunde meldet Stoerung
       |
       v
  Ticket wird erstellt (First-Level)
       |
       v
  Analyse: Loesung moeglich?
      / \
    Ja   Nein
    |      |
    v      v
  Loesung  Eskalation an Second-Level
  durchf.     |
    |         v
    v      Second-Level analysiert
  Ticket      |
  geschl.     v
           Loesung durchfuehren
              |
              v
           Ticket geschlossen
```

**Analyse:** Aufbau- und Ablauforganisation ergaenzen sich. Die Aufbauorganisation zeigt die Struktur (Teams), die Ablauforganisation zeigt den Prozess (Ticketbearbeitung). Beides wird in der Pruefung abgefragt.
