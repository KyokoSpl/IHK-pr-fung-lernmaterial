# 3.3.06 – Beispiele: Cyber-physische Systeme

## Beispiel 1: Smartes Gewaechshaus

### Szenario
Ein Gewaechshaus soll automatisch bewaessert werden. Die Bodenfeuchte und Temperatur werden gemessen, bei Bedarf wird eine Pumpe aktiviert.

### Komponenten

| Komponente | Typ | Funktion |
|-----------|-----|----------|
| Bodenfeuchtigkeitssensor | Sensor (analog) | Misst Wassergehalt im Boden |
| Temperatursensor (DHT22) | Sensor (digital) | Misst Temperatur + Luftfeuchte |
| Wasserpumpe | Aktor | Bewaessert den Boden |
| Relais-Modul | Aktor (Schalter) | Schaltet Pumpe ein/aus |
| ESP32 | Controller | Verarbeitung + WiFi-Anbindung |

### Ablaufdiagramm

```
    ●
    |
[Sensoren auslesen]
    |
   ◇ Bodenfeuchte < 40%?
  / \
ja   nein
/      \
[Pumpe EIN]  [Pumpe AUS]
|             |
[30 Sek. warten]  [5 Min. warten]
|             |
+------+------+
       |
[Daten an Cloud senden]
       |
[5 Min. warten]
       |
       └──→ zurueck zu "Sensoren auslesen"
```

### Pseudocode

```
WIEDERHOLE
    feuchte = bodenSensor.lese()
    temperatur = dhtSensor.lese_temperatur()

    WENN feuchte < 40 DANN
        relais.einschalten()     // Pumpe an
        warte(30000)             // 30 Sekunden bewaessern
        relais.ausschalten()     // Pumpe aus
    ENDE-WENN

    cloud.sende({
        "feuchte": feuchte,
        "temperatur": temperatur,
        "zeitstempel": aktuelle_zeit()
    })

    warte(300000)                // 5 Minuten Pause
ENDLOS
```

---

## Beispiel 2: Zugangskontrollsystem

### Szenario
Ein Buerogebaeude hat ein elektronisches Zugangssystem mit RFID-Karten. Bei gueltigem Ausweis oeffnet die Tuer, bei ungueltigem ertönt ein Warnsignal.

### Komponenten

| Komponente | Typ | Funktion |
|-----------|-----|----------|
| RFID-Leser (RC522) | Sensor | Liest Kartennummer |
| Servomotor | Aktor | Oeffnet/schliesst Türschloss |
| Buzzer | Aktor | Akustisches Feedback |
| Gruene LED | Aktor | Zugang gewaehrt |
| Rote LED | Aktor | Zugang verweigert |
| Raspberry Pi | Controller | Verarbeitung + Datenbank |

### Pseudocode

```
// Berechtigte Karten in Datenbank
berechtigte = lade_aus_datenbank()

WIEDERHOLE
    WENN rfid.karte_erkannt() DANN
        kartenNr = rfid.lese_kartennummer()

        WENN kartenNr IN berechtigte DANN
            grueneLed.ein()
            servo.oeffne(90)           // Tuer oeffnen (90 Grad)
            log("Zugang: " + kartenNr + " - " + zeit())
            warte(5000)               // 5 Sekunden offen
            servo.schliesse(0)         // Tuer schliessen
            grueneLed.aus()
        SONST
            roteLed.ein()
            buzzer.piepen(3)           // 3x piepen
            log("ABGELEHNT: " + kartenNr + " - " + zeit())
            warte(2000)
            roteLed.aus()
        ENDE-WENN
    ENDE-WENN

    warte(100)                         // 100ms Polling-Intervall
ENDLOS
```

---

## Beispiel 3: Raumklimasteuerung (Smart Office)

### Szenario
Ein Buero wird automatisch klimatisiert. Sensoren messen Temperatur, CO2 und Helligkeit. Aktoren steuern Heizung, Lueftung und Beleuchtung.

### Komponentenübersicht

```
+-----------------------------------------------------------+
|                  Smart Office System                       |
+-----------------------------------------------------------+
| SENSOREN:                  | AKTOREN:                     |
| [Temperatur] DHT22         | [Heizung] Relais → Thermostat|
| [CO2]        MH-Z19        | [Lueftung] Relais → Ventilator|
| [Helligkeit] BH1750 (I2C)  | [Licht] PWM → LED-Panel      |
| [Präsenz]    PIR HC-SR501  | [Display] LCD 16x2 (I2C)    |
+-----------------------------------------------------------+
| CONTROLLER: Raspberry Pi 4  | KOMMUNIKATION: MQTT + WiFi  |
+-----------------------------------------------------------+
```

### Regelungslogik

```
// Temperaturregelung
WENN temperatur < 20 DANN heizung.ein()
SONST WENN temperatur > 24 DANN heizung.aus()

// CO2-Regelung
WENN co2_ppm > 1000 DANN lueftung.ein()
SONST WENN co2_ppm < 600 DANN lueftung.aus()

// Lichtregelung (PWM abhaengig von Helligkeit)
WENN praesenz_erkannt DANN
    helligkeit_soll = 500       // 500 Lux Ziel
    differenz = helligkeit_soll - gemessene_helligkeit
    pwm_wert = berechne_pwm(differenz)
    licht.setze_pwm(pwm_wert)
SONST
    licht.aus()
ENDE-WENN
```

---

## Beispiel 4: Abstandswarner (Auto-Parkhilfe)

### Komponenten
- **Ultraschallsensor** HC-SR04 (misst Abstand per Echo)
- **Buzzer** (piept schneller je naeher)
- **LED-Ampel** (Gruen-Gelb-Rot)
- **Arduino** als Controller

### Funktionsprinzip Ultraschall

```
Sensor ──── Trigger (Ultraschall-Puls senden)
             |
             |   Schall breitet sich aus
             |   ~~~~~~~~~~~~~~~~~~~~~~~~> Hindernis
             |   <~~~~~~~~~~~~~~~~~~~~~~~~ Echo zurueck
             |
Sensor ──── Echo (Zeitdauer messen)

Entfernung = (Zeitdauer * Schallgeschwindigkeit) / 2
           = (Zeitdauer * 343 m/s) / 2
```

### Pseudocode

```
WIEDERHOLE
    abstand = ultraschall.messe_cm()

    WENN abstand > 100 DANN
        led_gruen.ein()
        led_gelb.aus()
        led_rot.aus()
        buzzer.aus()
    SONST WENN abstand > 30 DANN
        led_gruen.aus()
        led_gelb.ein()
        led_rot.aus()
        buzzer.piepen(intervall = 500)    // alle 500ms
    SONST
        led_gruen.aus()
        led_gelb.aus()
        led_rot.ein()
        buzzer.piepen(intervall = 100)    // alle 100ms (schnell)
    ENDE-WENN

    warte(50)    // 20 Messungen pro Sekunde
ENDLOS
```

---

## Beispiel 5: Wetterdatenlogger

### Szenario
Ein Raspberry Pi sammelt Wetterdaten und speichert sie in einer SQLite-Datenbank. Ueber eine Web-API koennen die Daten abgerufen werden.

```python
# Vereinfachter Python-Code (Raspberry Pi)
import Adafruit_DHT
import sqlite3
from time import sleep
from datetime import datetime

sensor = Adafruit_DHT.DHT22
pin = 4
db = sqlite3.connect('wetter.db')

# Tabelle erstellen (einmalig)
db.execute('''
    CREATE TABLE IF NOT EXISTS messwerte (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        zeitstempel TEXT,
        temperatur REAL,
        feuchte REAL
    )
''')

while True:
    feuchte, temp = Adafruit_DHT.read_retry(sensor, pin)
    if temp is not None:
        db.execute(
            'INSERT INTO messwerte (zeitstempel, temperatur, feuchte) VALUES (?,?,?)',
            (datetime.now().isoformat(), round(temp, 1), round(feuchte, 1))
        )
        db.commit()
        print(f"{datetime.now()}: {temp:.1f}°C, {feuchte:.1f}%")
    sleep(300)  # 5 Minuten
```
