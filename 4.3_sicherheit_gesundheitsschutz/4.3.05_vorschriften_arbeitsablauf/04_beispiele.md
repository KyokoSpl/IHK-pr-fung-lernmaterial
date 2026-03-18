# Beispiele: 4.3.05 – Vorschriften im betrieblichen und persoenlichen Arbeitsablauf

## Beispiel 1: Sicherheitskennzeichnung im IT-Unternehmen

Ein Fachinformatiker-Azubi macht einen Rundgang durch das Unternehmen und soll die Sicherheitskennzeichnung dokumentieren.

**Gefundene Zeichen:**

| Standort | Zeichen | Farbe/Form | Typ | Bedeutung |
|----------|---------|-----------|-----|-----------|
| Serverraum-Tuer | Gelbes Dreieck mit Blitz | Gelb/Dreieck | Warnzeichen | Warnung vor elektrischer Spannung |
| Serverraum-Tuer | Roter Kreis mit Querstrich | Rot/Kreis | Verbotszeichen | Zutritt fuer Unbefugte verboten |
| Flur | Gruenes Rechteck mit Pfeil | Gruen/Rechteck | Rettungszeichen | Fluchtweg/Notausgang |
| Flur neben Treppenhaus | Rotes Rechteck mit Feuerloescher | Rot/Rechteck | Brandschutzzeichen | Standort Feuerloescher |
| Werkstatt | Blaue Kreise | Blau/Kreis | Gebotszeichen | ESD-Schutz tragen |
| Kueche | Gruenes Rechteck mit Kreuz | Gruen/Rechteck | Rettungszeichen | Erste-Hilfe-Kasten |

---

## Beispiel 2: IP-Schutzart bestimmen

Ein IT-Systemhaus plant die Netzwerkinfrastruktur fuer eine Produktionshalle mit folgenden Anforderungen:

**Anforderung 1:** Switch fuer das Buero im 1. OG (klimatisiert, sauber)
→ **IP20** genuegt: Fingerschutz, kein Wasserschutz noetig

**Anforderung 2:** WLAN-Access-Point fuer den Aussenbereich (Firmenparkplatz)
→ **IP65** empfohlen: Staubdicht + Strahlwasserschutz (Regen, Reinigung)

**Anforderung 3:** Netzwerkanschluss in der Produktionshalle (Staub, Spritzwasser durch Kuehlung)
→ **IP54** empfohlen: Staubgeschuetzt + Spritzwasserschutz

**Anforderung 4:** Kamera fuer Tiefgarage (Feuchtigkeit, gelegentlich Wasser)
→ **IP66** empfohlen: Staubdicht + starker Strahlwasserschutz

---

## Beispiel 3: Schutzklassen zuordnen

Ein Azubi soll IT-Geraete den korrekten Schutzklassen zuordnen:

| Geraet | Stecker | Gehaeuse | Schutzklasse | Begruendung |
|--------|---------|----------|-------------|-------------|
| Desktop-PC | 3-polig (Schutzkontakt) | Metallgehaeuse mit Erdung | **Klasse I** | Schutzleiter verbindet Gehaeuse mit Erde |
| Laptop-Netzteil | 2-polig (Euro-Stecker) | Kunststoff, doppelt isoliert | **Klasse II** | Schutzisolierung, kein Schutzleiter noetig |
| USB-Tastatur | USB (5V) | Kunststoff | **Klasse III** | Schutzkleinspannung (5V DC ueber USB) |
| Server (Rack) | 3-polig (Schutzkontakt) | Metallgehaeuse mit Erdung | **Klasse I** | Schutzleiter vorhanden |
| Handyladegeraet | 2-polig | Kunststoff, doppelt isoliert | **Klasse II** | Ausgangsspannung 5V, aber Eingang 230V mit Schutzisolierung |

---

## Beispiel 4: CE-Kennzeichnung pruefen

Ein Unternehmen bestellt guenstige Netzteile fuer neue Arbeitsplaetze. Der Azubi soll die Lieferung pruefen:

**Pruefschritte:**
1. CE-Kennzeichnung vorhanden? → Ja ✓
2. Abstand zwischen C und E korrekt? → Der Abstand ist auffaellig gering → **Verdacht auf "China Export"-Faelschung!**
3. Konformitaetserklaerung mitgeliefert? → Nicht vorhanden → **Mangel**
4. Herstellerangaben vollstaendig (Name, Adresse, Typ)? → Nur "Made in China", kein Herstellername → **Mangel**

**Ergebnis:** Die Netzteile duerfen **nicht verwendet werden**, da die CE-Konformitaet nicht nachweisbar ist. Rueckgabe an den Lieferanten.

**Korrekte Vorgehensweise beim Einkauf:**
- CE-Kennzeichnung und Konformitaetserklaerung pruefen
- GS-Zeichen als zusaetzliches Sicherheitsmerkmal bevorzugen
- Nur bei seriösen Haendlern kaufen
- DGUV Vorschrift 3: Auch neue Geraete vor Erstinbetriebnahme pruefen

---

## Beispiel 5: Fluchtweg-Kontrolle

Bei einer Betriebsbegehung werden folgende Maengel an Fluchtwegen festgestellt:

| Mangel | Verstoss gegen | Massnahme |
|--------|---------------|-----------|
| Serverkartons im Flur vor Notausgang | ASR A2.3 (Fluchtwege freihalten) | Sofort raeumen |
| Notausgang-Schild defekt (keine Beleuchtung) | ASR A1.3, ASR A3.4/3 | Sicherheitsbeleuchtung reparieren |
| Notausganstuer von aussen abgeschlossen | ASR A2.3 (von innen ohne Schluessel oeffenbar) | Panikverschluss pruefen, ggf. Schloss entfernen |
| Fluchtwegeplan im 2. OG fehlt | ASR A2.3 | Plan erstellen und aushaengen |
| Fluchtweg nur 0,70 m breit (20 Personen) | ASR A2.3 (min. 1,00 m) | Bauliche Aenderung oder Nutzungsaenderung |
