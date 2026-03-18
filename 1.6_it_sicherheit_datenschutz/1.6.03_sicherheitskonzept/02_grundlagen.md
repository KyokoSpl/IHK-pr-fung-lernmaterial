# Grundlagen: 1.6.03 – Sicherheitskonzept nach BSI-Grundschutz

## Bausteine aus dem Grundschutzkatalog

**Definition:** BSI-Bausteine sind thematische Module, die typische Gefaehrdungen und zugehoerige Sicherheitsanforderungen fuer bestimmte IT-Objekte beschreiben.

**Schichten des BSI-Grundschutz-Kompendiums:**

| Schicht | Kuerzel | Inhalt | Beispiel-Bausteine |
|---|---|---|---|
| Prozess-Bausteine | ISMS, ORP, CON, OPS, DER | Organisation, Konzepte, Betrieb | ISMS.1 Sicherheitsmanagement |
| System-Bausteine | INF, NET, SYS, APP | Infrastruktur, Netze, Systeme, Apps | SYS.1.1 Allgemeiner Server |

**Anforderungsstufen pro Baustein:**

| Stufe | Beschreibung | Verbindlichkeit |
|---|---|---|
| **Basis** | Grundlegende Anforderungen | MUSS (immer umsetzen) |
| **Standard** | Fuer normalen Schutzbedarf | SOLLTE (empfohlen) |
| **Erhoehter Schutzbedarf** | Fuer hohen/sehr hohen Bedarf | SOLLTE (bei Bedarf) |

---

## ISMS (Informations-Sicherheitsmanagementsystem)

**Definition:** Ein ISMS ist ein systematischer Ansatz aus Richtlinien, Prozessen und Kontrollen, der die Informationssicherheit eines Unternehmens managt und kontinuierlich verbessert.

**Kernelemente eines ISMS:**
1. **Sicherheitsleitlinie:** Uebergeordnetes Dokument mit Zielen und Grundsaetzen
2. **Sicherheitsorganisation:** Rollen und Verantwortlichkeiten festlegen
3. **Risikoanalyse:** Bedrohungen und Schwachstellen identifizieren
4. **Massnahmenplanung:** Gegenmassnahmen definieren und priorisieren
5. **Umsetzung:** Massnahmen implementieren
6. **Kontrolle und Verbesserung:** PDCA-Zyklus anwenden

**Standards:**
- **ISO 27001:** Internationaler Standard fuer ISMS (zertifizierbar)
- **BSI IT-Grundschutz:** Deutscher Standard, kompatibel mit ISO 27001

**ISMS-Prozess (PDCA):**
```
Plan → Sicherheitsleitlinie, Risikoanalyse, Massnahmenplanung
Do   → Massnahmen umsetzen, Schulungen durchfuehren
Check → Audits, Ueberpruefung der Wirksamkeit
Act  → Verbesserungen einfuehren, Leitlinie aktualisieren
```

---

## Risiko-Klassifikation mit Matrix

**Definition:** Die Risikobewertung erfolgt durch Kombination von Eintrittswahrscheinlichkeit und Schadenshoehe in einer Risikomatrix.

**Risikomatrix (3x3):**

| | Schaeden gering | Schaeden mittel | Schaeden hoch |
|---|---|---|---|
| **Wahrscheinlichkeit hoch** | Mittel | Hoch | Kritisch |
| **Wahrscheinlichkeit mittel** | Gering | Mittel | Hoch |
| **Wahrscheinlichkeit gering** | Gering | Gering | Mittel |

**Risikobehandlungsstrategien:**

| Strategie | Beschreibung | Beispiel |
|---|---|---|
| **Risikovermeidung** | Risikoquelle eliminieren | Cloud-Dienst nicht nutzen |
| **Risikominderung** | Wahrscheinlichkeit oder Auswirkung senken | Firewall installieren, Backup einrichten |
| **Risikouebertragung** | Risiko an Dritte uebertragen | Cyberversicherung abschliessen |
| **Risikoakzeptanz** | Restrisiko bewusst tragen | Geringes Risiko dokumentiert hinnehmen |

---

## Schutzbedarfskategorien ableiten und begruenden

**Methodik:**
1. Schadensszenarien je Schutzziel durchspielen
2. Typische Schadensszenarien nach BSI:
   - Verstoss gegen Gesetze/Vertraege
   - Beeintraechtigung des Informationellen Selbstbestimmungsrechts
   - Beeintraechtigung der persoenlichen Unversehrtheit
   - Beeintraechtigung der Aufgabenerfuellung
   - Negative Innen-/Aussenwirkung
   - Finanzielle Auswirkungen

**Ableitung:**

| Schadensszenario | Normal | Hoch | Sehr hoch |
|---|---|---|---|
| Finanzielle Auswirkung | < 10.000 € | 10.000 – 500.000 € | > 500.000 € |
| Gesetzesverstoss | Ordnungswidrigkeit | Erheblicher Verstoss | Straftat |
| Imageschaden | Lokal begrenzt | Oeffentlich wahrnehmbar | Existenzbedrohend |
| Aufgabenerfuellung | Leicht eingeschraenkt | Erheblich eingeschraenkt | Voellig unterbunden |

**Wichtig:** Die Begruendung muss nachvollziehbar und dokumentiert sein.
