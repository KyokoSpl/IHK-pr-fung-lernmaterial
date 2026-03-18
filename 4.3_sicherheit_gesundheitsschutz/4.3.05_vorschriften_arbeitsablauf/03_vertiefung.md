# Vertiefung: 4.3.05 – Vorschriften im betrieblichen und persoenlichen Arbeitsablauf

## Sicherheitskennzeichnung – Gesamtuebersicht

```
  SICHERHEITSZEICHEN nach ASR A1.3 / ISO 7010

  VERBOTSZEICHEN (Rot, Kreis + Querstrich)
  +-------+    +-------+    +-------+
  |  P002 |    |  P003 |    |  P006 |
  | Rauchen|    | Offenes|    | Zutritt|
  |verboten|    | Feuer  |    |verboten|
  +-------+    +-------+    +-------+

  WARNZEICHEN (Gelb, Dreieck)
  +-------+    +-------+    +-------+
  |  W012 |    |  W001 |    |  W026 |
  | Elektr.|    | Allgem.|    | Optische|
  |Spannung|    | Warnung|    |Strahlung|
  +-------+    +-------+    +-------+

  GEBOTSZEICHEN (Blau, Kreis)
  +-------+    +-------+    +-------+
  |  M001 |    |  M004 |    |  M008 |
  | Allgem.|    | Augen- |    | Fuss-  |
  | Gebot  |    | schutz |    | schutz |
  +-------+    +-------+    +-------+

  RETTUNGSZEICHEN (Gruen, Rechteck)
  +-------+    +-------+    +-------+
  |  E001 |    |  E002 |    |  E003 |
  | Notaus-|    | Sammel-|    | Erste  |
  | gang   |    | stelle |    | Hilfe  |
  +-------+    +-------+    +-------+

  BRANDSCHUTZZEICHEN (Rot, Rechteck)
  +-------+    +-------+    +-------+
  |  F001 |    |  F002 |    |  F005 |
  | Feuer- |    | Loesc- |    | Brand- |
  | loesch.|    | hahn   |    | melder |
  +-------+    +-------+    +-------+
```

## IP-Schutzarten – Vertiefung

### Merkregel fuer den IP-Code

```
  IP [X] [Y]
      |    |
      |    +-- Ziffer 2: Wasserschutz (0-8)
      |         0=kein, 1=Tropfen, 4=Spritz, 5=Strahl,
      |         7=Tauchen, 8=Dauertauchen
      |
      +-- Ziffer 1: Beruehrungs-/Fremdkoerperschutz (0-6)
           0=kein, 2=Finger, 4=Draht, 5=Staubschutz, 6=Staubdicht
```

### Praxisbeispiele im IT-Umfeld

| Geraet | Typischer IP-Code | Begruendung |
|--------|-------------------|-------------|
| Desktop-PC (Buero) | IP20 | Fingerschutz, kein Wasser im Buero |
| Laptop | IP20–IP52 | Manche Modelle staubgeschuetzt |
| Outdoor-WLAN-AP | IP65 | Staubdicht, strahlwassergeschuetzt |
| Industrie-Switch | IP67 | Staubdicht, untertauchbar |
| Outdoor-Kamera | IP66 | Staubdicht, starkes Strahlwasser |
| Smartphone (modern) | IP68 | Staubdicht, dauerhaftes Untertauchen |

## Schutzklassen – Vertiefung

### Vergleich Schutzklasse I, II, III

```
  Schutzklasse I:                Schutzklasse II:             Schutzklasse III:
  +---------+                    +---------+                  +---------+
  | Geraet  |                    | Geraet  |                  | Geraet  |
  | Metall- |---[Schutzleiter]   | Doppelte|                  | Klein-  |
  | gehaeuse|   zur Erde         | Isolie- |  Kein            | spannung|
  |         |                    | rung    |  Schutzleiter    | ≤50V AC |
  +---------+                    +---------+                  +---------+
  3-poliger Stecker              2-poliger Stecker             SELV-Trafo
  (L, N, PE)                     (L, N)                        (Sicherheit)

  Beispiel: Server                Beispiel: Laptop-Netzteil    Beispiel: USB 5V
```

## CE vs. GS – Detailvergleich

| Aspekt | CE | GS |
|--------|----|----|
| Bedeutung | Conformité Européenne | Geprueefte Sicherheit |
| Art | Pflicht (fuer viele Produktgruppen) | Freiwillig |
| Vergabe durch | Hersteller (Selbsterklaerung) | Unabhaengige Pruefstelle (z.B. TÜV, DEKRA) |
| Pruefung | Hersteller prueft selbst | Fremduepruefung durch akkreditierte Stelle |
| Gaeltigkeit | EU-weit | Deutschland (wird aber EU-weit anerkannt) |
| Aussagekraft | Konformitaet mit EU-Richtlinien | Gepruefte Produktsicherheit |
| Missbrauch | Haeufig bei Faelschungen ("China Export") | Weniger anfaellig, da fremdgeprueft |

**Achtung:** Das CE-Zeichen des "China Export" hat einen geringeren Abstand zwischen den Buchstaben. Dies ist eine bekannte Faelschungsproblematik.

## Fluchtwegeplan – Aufbau

```
  +----------------------------------------------------------+
  |  FLUCHT- UND RETTUNGSPLAN       [Firmenname]              |
  |  Standort: Gebaeude A, 2. OG                             |
  |                                                            |
  |  +------+  +------+  +------+  +------+  +------+        |
  |  |Buero |  |Buero |  |Server|  |Buero |  |Buero |        |
  |  | 201  |  | 202  |  | raum |  | 204  |  | 205  |        |
  |  +--||--+  +--||--+  +--||--+  +--||--+  +--||--+        |
  |     ||        ||        ||        ||        ||            |
  |  ===================================================      |
  |                    FLUR                                    |
  |  ===================================================      |
  |     ||                                     ||             |
  |  [TREPPE]                              [NOTAUSGANG]       |
  |  ← Fluchtrichtung         Fluchtrichtung →                |
  |                                                            |
  |  Legende:                                                  |
  |  [Gruener Pfeil] = Fluchtweg    [Rotes Rechteck] = FeuLö  |
  |  [Gruenes Kreuz] = Erste Hilfe  [Rotes F] = Brandmelder   |
  |  [E] = Sammelplatz: Parkplatz Sued                        |
  +----------------------------------------------------------+
```

## Typische Pruefungsaspekte

- Sicherheitszeichen erkennen und zuordnen (Farbe + Form = Typ)
- IP-Code entschluesseln (z.B. IP65 → staubdicht + strahlwasserfest)
- Schutzklassen I/II/III mit Beispielen zuordnen
- CE-Kennzeichnung als Herstellererklaerung (KEIN Qualitaetssiegel) kennen
- Fluchtweganforderungen (Breite, Laenge, Kennzeichnung, Beleuchtung)
- GHS-Piktogramme erkennen und zuordnen

## Haeufige Fehler

| Fehler | Richtigstellung |
|--------|----------------|
| CE = Qualitaetssiegel / TÜV-Pruefung | CE ist eine Herstellererklaerung, keine Fremdpruefung |
| IP65 bedeutet "wasserdicht" | IP65 = strahlwasserdicht, NICHT untertauchbar (waere IP67/68) |
| Schutzklasse II = schlechterer Schutz als I | Schutzklasse II (Schutzisolierung) ist gleichwertig, nur anderes Prinzip |
| Alle Sicherheitszeichen sind rot | Farbe haengt vom Typ ab (Rot=Verbot/Brand, Gelb=Warnung, Blau=Gebot, Gruen=Rettung) |
| Fluchtweg und Rettungsweg sind dasselbe | Fluchtweg = fuer Personen im Gebaeude, Rettungsweg = fuer Rettungskraefte |
| Notausgangstueren duerfen abgeschlossen werden | Muessen jederzeit von innen ohne Schluessel zu oeffnen sein |
| GHS-Symbole gelten nur in Deutschland | GHS ist ein weltweit harmonisiertes System |
