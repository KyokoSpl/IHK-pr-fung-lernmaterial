# Uebungen: 4.2.03 – Unternehmensstruktur und Organisationsform

## Aufgabe 1: Organisationsform erkennen

Ein Unternehmen hat folgende Struktur: Jeder Mitarbeiter hat genau einen Vorgesetzten. Es gibt drei Abteilungen (Entwicklung, Vertrieb, Support), die jeweils einem Abteilungsleiter unterstehen. Die Abteilungsleiter berichten an die Geschaeftsfuehrung.

a) Um welche Organisationsform handelt es sich?
b) Nenne zwei Vorteile und zwei Nachteile dieser Organisationsform.
c) Die Geschaeftsfuehrung moechte eine Rechtsabteilung einrichten, die nicht weisungsbefugt ist, aber die GF beraet. Wie veraendert sich die Organisationsform?

## Aufgabe 2: Organigramm zeichnen

Zeichne ein Organigramm fuer folgendes Szenario:
- Geschaeftsfuehrung an der Spitze
- Stabsstelle "Qualitaetsmanagement" (beratend)
- Drei Abteilungen: Softwareentwicklung, Systemadministration, Kundenservice
- Softwareentwicklung hat zwei Teams: Frontend und Backend

## Aufgabe 3: Matrix vs. Einliniensystem

Ein Softwareunternehmen mit drei Produkten (App A, App B, App C) und zwei Abteilungen (Entwicklung, Testing) ueberlegt, von einem Einliniensystem auf eine Matrixorganisation umzustellen.

a) Skizziere die Matrixorganisation.
b) Nenne drei Vorteile des Wechsels.
c) Welche Probleme koennen entstehen?

## Aufgabe 4: Aufbau- vs. Ablauforganisation

Erklaere den Unterschied zwischen Aufbau- und Ablauforganisation. Erstelle fuer ein IT-Unternehmen je ein Beispiel:
a) Aufbauorganisation: Wie ist die IT-Abteilung strukturiert?
b) Ablauforganisation: Wie laeuft die Bearbeitung eines Kundenauftrags ab?

## Aufgabe 5: Spartenorganisation bewerten

Ein IT-Konzern ist in drei Sparten gegliedert: Cloud, On-Premise-Software und IT-Beratung. Jede Sparte hat eigene Entwicklung, Vertrieb und Support.

a) Welchen Vorteil hat diese Organisation gegenueber einem Einliniensystem?
b) Welcher typische Nachteil kann auftreten?
c) Wie koennte der Konzern den Nachteil abmildern?

## Aufgabe 6: IT-Abteilung einordnen

Diskutiere: Sollte die IT-Abteilung eines mittelstaendischen Unternehmens als Stabsstelle, als Linienabteilung oder als eigene Sparte organisiert werden? Nenne fuer jede Variante einen Vor- und einen Nachteil.

---
---

# Loesungen

## Aufgabe 1
a) **Einliniensystem** – jeder MA hat genau einen Vorgesetzten, klare Hierarchie.
b) Vorteile: (1) Eindeutige Verantwortlichkeiten, (2) einfache, uebersichtliche Struktur.
   Nachteile: (1) Lange Dienstwege bei grossen Unternehmen, (2) Ueberlastung der Geschaeftsfuehrung, da alle Informationen ueber sie laufen.
c) Es wird ein **Stab-Liniensystem**. Die Rechtsabteilung wird als Stabsstelle ohne Weisungsrecht eingerichtet, die die GF beratend unterstuetzt.

## Aufgabe 2
```
        +---------------------+----[ Stab: QM ]
        | Geschaeftsfuehrung  |
        +---------------------+
       /          |            \
      v           v             v
+--------+  +------------+  +-----------+
| SW-Entw|  | Sys-Admin  |  | Kunden-   |
+--------+  +------------+  | service   |
  /    \                     +-----------+
 v      v
+----+ +----+
| FE | | BE |
+----+ +----+
```

## Aufgabe 3
a) Matrixorganisation:

|  | App A | App B | App C |
|---|------|------|------|
| Entwicklung | Team A-Dev | Team B-Dev | Team C-Dev |
| Testing | Team A-QA | Team B-QA | Team C-QA |

b) Vorteile: (1) Entwickler und Tester koennen produktuebergreifend Best Practices teilen, (2) Flexiblere Ressourcenzuordnung bei Engpaessen, (3) Bessere fachliche Steuerung durch Funktionsleiter.
c) Probleme: Widerspruchliche Anweisungen (z.B. Produktmanager will Feature, Testleiter will mehr Testzeit), hoher Abstimmungsbedarf, unklare Priorisierung.

## Aufgabe 4
a) Aufbauorganisation (Wer macht was):
```
IT-Leiter
├── Team Infrastruktur (Netzwerk, Server)
├── Team Entwicklung (Software, Datenbanken)
└── Team Helpdesk (Anwenderunterstuetzung)
```

b) Ablauforganisation (Wie laeuft ein Kundenauftrag ab):
1. Kundenanfrage eingeht → Vertrieb nimmt auf
2. Anforderungsanalyse → IT-Beratung erstellt Konzept
3. Angebot → Vertrieb erstellt Angebot
4. Auftrag → Projektplanung durch IT-Leitung
5. Umsetzung → Team Entwicklung implementiert
6. Test → QA-Pruefung
7. Auslieferung → Uebergabe an Kunden
8. Support → Team Helpdesk uebernimmt

## Aufgabe 5
a) **Marktnaehe:** Jede Sparte kann schnell und eigenstaendig auf die spezifischen Anforderungen ihres Marktsegments reagieren (z.B. Cloud-Trends vs. On-Premise-Kundenanforderungen).
b) **Doppelstrukturen:** Drei separate Entwicklungs-, Vertriebs- und Supportabteilungen fuehren zu hoeheren Kosten und moeglicherweise redundanter Arbeit.
c) Einrichtung von **Zentralbereichen** fuer uebergreifende Funktionen (z.B. zentrale IT-Infrastruktur, gemeinsames Personalwesen, einheitliches Qualitaetsmanagement).

## Aufgabe 6

| Variante | Vorteil | Nachteil |
|----------|---------|----------|
| Stabsstelle | Direkter Zugang zur GF, strategische Beratung | Kein Weisungsrecht, Umsetzung abhaengig von Linienabteilungen |
| Linienabteilung | Eigene Ressourcen, klare Verantwortung, Weisungsrecht | Kann von anderen Abteilungen als "Dienstleister" wahrgenommen werden |
| Eigene Sparte | Hohe Eigenstaendigkeit, eigenes Budget, eigene Entscheidungen | Nur sinnvoll, wenn IT zum Kerngeschaeft gehoert, sonst ueberdimensioniert |

Empfehlung fuer ein mittelstaendisches Unternehmen: **Linienabteilung**, da die IT operative Aufgaben hat (Support, Administration) und Weisungsrecht benoetigt (z.B. Sicherheitsrichtlinien durchsetzen).
