# Grundlagen: 3.5.02 – Qualitaetssicherung von Softwareanwendungen

## Testarten

**Definition:** Testarten beschreiben, WAS getestet wird – also die Art der Pruefung, die an einem Softwaresystem durchgefuehrt wird.

**Kernaussagen:**
- Jede Testart hat ein spezifisches Ziel (Funktion, Leistung, Sicherheit etc.)
- Testarten koennen auf verschiedenen Teststufen angewendet werden
- Kombination mehrerer Testarten ergibt eine vollstaendige Teststrategie

**Uebersicht der Testarten:**

| Testart | Ziel | Beschreibung | Beispiel |
|---|---|---|---|
| **Funktionaler Test** | Korrektheit | Prueft, ob die Software die spezifizierten Funktionen korrekt ausfuehrt | Login-Funktion liefert bei falschem Passwort eine Fehlermeldung |
| **Nicht-funktionaler Test** | Qualitaet | Prueft Eigenschaften wie Performance, Sicherheit, Usability | Ladezeit der Startseite unter 2 Sekunden |
| **Regressionstest** | Stabilitaet | Prueft, ob bestehende Funktionen nach einer Aenderung noch korrekt arbeiten | Nach Bug-Fix: alle bisherigen Tests erneut durchlaufen |
| **Lasttest** | Belastbarkeit | Prueft das Systemverhalten unter hoher Last | 1000 gleichzeitige Benutzer auf dem Webshop |
| **Performancetest** | Geschwindigkeit | Misst Antwortzeiten und Durchsatz | API-Antwortzeit < 200ms |
| **Sicherheitstest** | Schutz | Prueft auf Schwachstellen (SQL-Injection, XSS etc.) | Eingabe von `' OR 1=1 --` in Login-Feld |
| **Usability-Test** | Bedienbarkeit | Prueft die Benutzerfreundlichkeit | Testpersonen fuehren typische Aufgaben durch |
| **Smoke-Test** | Grundfunktion | Schnelltest, ob die grundlegenden Funktionen nach Deployment funktionieren | Nach Release: Login, Navigation, Hauptfunktion pruefen |

**Wichtige Begriffe:**
- **Testfall (Test Case)** – Konkrete Beschreibung einer Eingabe, der Ausfuehrungsschritte und des erwarteten Ergebnisses
- **Testplan** – Dokument, das Umfang, Ziele, Zeitplan und Ressourcen der Tests festlegt
- **Testsuite** – Sammlung zusammengehoeriger Testfaelle
- **Testprotokoll** – Dokumentation der Testergebnisse (bestanden / nicht bestanden)

**Erklaerung:** In der Pruefung wird haeufig nach dem Unterschied zwischen funktionalen und nicht-funktionalen Tests gefragt. Merke: Funktional = WAS die Software tut. Nicht-funktional = WIE GUT die Software es tut.

---

## Teststufen

**Definition:** Teststufen beschreiben, WANN und auf welcher Ebene getestet wird. Jede Teststufe hat einen bestimmten Fokus und einen definierten Testgegenstand.

**Die vier Teststufen:**

| Teststufe | Testgegenstand | Durchfuehrung | Ziel |
|---|---|---|---|
| **Unit-Test (Komponententest)** | Einzelne Methoden, Funktionen, Klassen | Entwickler | Korrektheit einzelner Codebausteine |
| **Integrationstest** | Zusammenspiel mehrerer Komponenten | Entwickler / Tester | Schnittstellen und Datenaustausch pruefen |
| **Systemtest** | Gesamtes System | Testteam | Erfuellung aller Anforderungen (funktional + nicht-funktional) |
| **Abnahmetest (Akzeptanztest)** | Gesamtes System aus Kundensicht | Kunde / Auftraggeber | Freigabe des Systems fuer den Produktivbetrieb |

**Details zu den Teststufen:**

### Unit-Test (Komponententest)
- Testet die kleinste pruefbare Einheit (Methode, Funktion)
- Wird vom Entwickler geschrieben (z.B. mit JUnit, pytest, Jest)
- Schnell ausfuehrbar, automatisiert
- Isoliert von anderen Komponenten (Mocking, Stubbing)
- Erkennt Fehler frueh → geringe Behebungskosten

### Integrationstest
- Testet das Zusammenspiel mehrerer Komponenten oder Module
- Prueft Schnittstellen (APIs, Datenbankanbindung, Dateisysteme)
- Strategien: Top-Down, Bottom-Up, Big-Bang

| Strategie | Beschreibung | Vorteil | Nachteil |
|---|---|---|---|
| **Top-Down** | Von oben nach unten integrieren, Stubs fuer untere Module | Fruehe Validierung der Architektur | Stubs aufwaendig |
| **Bottom-Up** | Von unten nach oben integrieren, Treiber fuer obere Module | Keine Stubs noetig | Spaete Validierung der Gesamtstruktur |
| **Big-Bang** | Alle Module auf einmal integrieren | Kein inkrementeller Aufwand | Fehlerlokalisation sehr schwer |

### Systemtest
- Testet das Gesamtsystem gegen die Anforderungen
- Beinhaltet funktionale und nicht-funktionale Tests
- Testumgebung sollte der Produktivumgebung moeglichst entsprechen
- Typischerweise Black-Box-Verfahren

### Abnahmetest (Akzeptanztest)
- Letzte Teststufe vor dem Go-Live
- Durchfuehrung durch den Kunden oder Auftraggeber
- Grundlage: Abnahmekriterien aus dem Pflichtenheft / Vertrag
- Erfolgreich → Abnahmeerklaerung → Produktivbetrieb

**Erklaerung:** Fuer die Pruefung ist die Reihenfolge entscheidend: Unit → Integration → System → Abnahme. Fehler, die frueh erkannt werden, sind guenstiger zu beheben.

---

## V-Modell im Zusammenhang mit Tests

**Definition:** Das V-Modell ordnet jeder Entwicklungsphase (linke Seite) eine korrespondierende Teststufe (rechte Seite) zu. Es verdeutlicht, dass Testplanung bereits in fruehen Phasen beginnt.

**Darstellung des V-Modells:**

```
  Anforderungsanalyse ─────────────────── Abnahmetest
       \                                    /
    Funktionaler Entwurf ──────── Systemtest
         \                            /
      Technischer Entwurf ──── Integrationstest
           \                      /
        Implementierung ──── Unit-Test
```

**Zuordnung im Detail:**

| Entwicklungsphase (links) | Teststufe (rechts) | Testbasis |
|---|---|---|
| Anforderungsanalyse | Abnahmetest | Lastenheft, Vertrag |
| Funktionaler Entwurf | Systemtest | Pflichtenheft, Spezifikation |
| Technischer Entwurf | Integrationstest | Schnittstellenbeschreibung, Architektur |
| Implementierung | Unit-Test | Quellcode, technische Spezifikation |

**Kernaussagen:**
- Linke Seite = Entwicklung (Spezifikation → Implementierung)
- Rechte Seite = Verifikation (Unit-Test → Abnahme)
- Jede Testphase bezieht sich auf die korrespondierende Entwicklungsphase
- Testplanung und Testfalldesign beginnen parallel zur jeweiligen Spezifikationsphase
- Verifikation: Wurde das Produkt richtig gebaut? (technisch korrekt)
- Validierung: Wurde das richtige Produkt gebaut? (Kundenanforderungen erfuellt)

**Wichtige Begriffe:**
- **Verifikation** – Pruefung gegen die Spezifikation ("Bauen wir das Produkt richtig?")
- **Validierung** – Pruefung gegen die Kundenanforderungen ("Bauen wir das richtige Produkt?")
- **Testbasis** – Dokument, aus dem Testfaelle abgeleitet werden
- **Rueckverfolgbarkeit (Traceability)** – Zuordnung von Anforderungen zu Testfaellen

**Erklaerung:** Das V-Modell wird in der Pruefung sehr haeufig abgefragt. Du musst die Zuordnung der Teststufen zu den Entwicklungsphasen beherrschen und erklaeren koennen, warum fruehe Testplanung wichtig ist.
