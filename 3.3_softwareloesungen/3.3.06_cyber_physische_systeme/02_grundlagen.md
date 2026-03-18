# 3.3.06 – Grundlagen: Cyber-physische Systeme beschreiben und erweitern

## Was ist ein Cyber-physisches System (CPS)?

**Definition**: Ein CPS verbindet informatische (Software, Netzwerk) mit physischen Komponenten (Sensoren, Aktoren) zu einem integrierten System, das die reale Welt ueberwacht und steuert.

```
Aufbau eines CPS:

+------------------+     +------------------+     +------------------+
|   Physische      |     |   Cyber-         |     |   Netzwerk/      |
|   Welt           |     |   Komponente     |     |   Cloud          |
+------------------+     +------------------+     +------------------+
| Sensoren messen  |---->| Datenverarbeitung|---->| Datenspeicherung |
| (Temperatur,     |     | (Microcontroller,|     | Analyse          |
|  Druck, Licht)   |     |  Raspberry Pi)   |     | Fernsteuerung    |
|                  |<----| Steuerungslogik  |<----| Benachrichtigung |
| Aktoren handeln  |     |                  |     |                  |
| (Motor, LED,     |     |                  |     |                  |
|  Ventil)         |     |                  |     |                  |
+------------------+     +------------------+     +------------------+
```

---

## TK 1: Abfragerhythmus planen

### Polling vs. Interrupt

| Merkmal | Polling | Interrupt |
|---------|---------|-----------|
| Prinzip | Regelmae ssiges Abfragen des Sensors | Sensor meldet sich bei Aenderung |
| CPU-Last | Hoeher (staendige Abfrage) | Niedriger (nur bei Ereignis aktiv) |
| Reaktionszeit | Abhaengig vom Intervall | Sofort (asynchron) |
| Implementierung | Einfach (Schleife + Sleep) | Komplexer (Interrupt-Handler) |
| Geeignet fuer | Langsame Sensoren, regelmae ssige Messwerte | Schnelle Reaktion auf Ereignisse |

### Polling-Beispiel (Pseudocode)

```
// Temperatur alle 5 Sekunden abfragen
WIEDERHOLE
    temperatur = sensor.lese_temperatur()
    WENN temperatur > 30 DANN
        aktor.luefter_einschalten()
    SONST
        aktor.luefter_ausschalten()
    ENDE-WENN
    warte(5000)    // 5 Sekunden
ENDLOS
```

### Interrupt-Beispiel (Pseudocode)

```
// Bewegungsmelder loest Interrupt aus
FUNKTION bei_bewegung_erkannt()
    licht.einschalten()
    warte(60000)    // 60 Sekunden
    licht.ausschalten()
ENDE-FUNKTION

// Interrupt registrieren
registriere_interrupt(PIN_7, STEIGENDE_FLANKE, bei_bewegung_erkannt)

// Hauptprogramm laeuft weiter (oder schlaeft)
WIEDERHOLE
    // andere Aufgaben oder Energiesparmodus
ENDLOS
```

### Abtastrate (Sampling Rate)

- **Nyquist-Theorem**: Die Abtastrate muss mindestens **doppelt so hoch** sein wie die hoechste zu messende Frequenz
- Beispiel: Wenn sich eine Temperatur max. alle 10 Sekunden aendert, reicht eine Abtastrate von 1x / 5 Sekunden

| Anwendung | Typische Abtastrate |
|-----------|-------------------|
| Temperaturmessung | Alle 1-60 Sekunden |
| Bewegungserkennung | Interrupt-basiert |
| Beschleunigungssensor | 50-1000 Hz |
| Audiosignal | 44.100 Hz (CD-Qualitaet) |

---

## TK 2: Auswahl Sensoren/Aktoren

### Sensoren (Eingabe – messen die physische Welt)

| Sensortyp | Misst | Ausgabe | Beispiel-Bauteil |
|-----------|-------|---------|-----------------|
| Temperatursensor | Temperatur | Analog/Digital | DHT22, DS18B20 |
| Luftfeuchtigkeitssensor | Relative Luftfeuchtigkeit | Digital | DHT11, DHT22 |
| Lichtsensor (LDR) | Helligkeit | Analog | Fotowiderstand |
| Bewegungsmelder (PIR) | Infrarot-Bewegung | Digital (HIGH/LOW) | HC-SR501 |
| Ultraschallsensor | Abstand/Entfernung | Digital (Pulsweite) | HC-SR04 |
| Drucksensor | Luftdruck | Digital | BMP280 |
| Beschleunigungssensor | Beschleunigung, Neigung | Digital (I2C) | MPU6050 |
| Taster / Schalter | Benutzereingabe | Digital (HIGH/LOW) | Taster |

### Aktoren (Ausgabe – wirken auf die physische Welt)

| Aktortyp | Wirkung | Ansteuerung | Beispiel |
|----------|---------|-------------|---------|
| LED | Licht erzeugen | Digital / PWM | Status-LED, LED-Streifen |
| Motor (DC) | Drehbewegung | PWM + Motortreiber | Ventilator, Pumpe |
| Servomotor | Praezise Winkelbewegung | PWM | Roboterarm, Klappe |
| Relais | Schalten hoher Lasten | Digital | Lampe, Heizung ein/aus |
| Buzzer/Piezo | Ton erzeugen | Digital / PWM | Alarm, Signalton |
| Display (LCD) | Text/Grafik anzeigen | I2C / SPI | Statusanzeige |

### Analog vs. Digital

| Merkmal | Analog | Digital |
|---------|--------|---------|
| Signaltyp | Stufenlos (0V – 3.3V/5V) | Nur HIGH oder LOW (1 oder 0) |
| Beispiel Sensor | Fotowiderstand (LDR) | Taster, PIR-Sensor |
| Auswertung | ADC (Analog-Digital-Converter) | Direkt lesbar |
| Genauigkeit | Abhaengig von ADC-Aufloesung | Exakt (ein/aus) |

---

## TK 3: CPS-Software

### Architektur einer typischen CPS-Anwendung

```
+----------------------------------------------------------+
|                    CPS-Softwarearchitektur                |
+----------------------------------------------------------+
|  Anwendungsschicht  | Steuerungslogik, Regelung          |
+---------------------+------------------------------------+
|  Verarbeitungsschicht| Datenaufbereitung, Filterung      |
+---------------------+------------------------------------+
|  Kommunikationsschicht| MQTT, HTTP, Bluetooth, WiFi     |
+---------------------+------------------------------------+
|  Hardwarezugriffsschicht| GPIO, I2C, SPI, UART          |
+---------------------+------------------------------------+
|  Hardware           | Sensoren, Aktoren, Microcontroller |
+----------------------------------------------------------+
```

### Typische CPS-Plattformen

| Plattform | Typ | Sprachen | Einsatz |
|-----------|-----|---------|---------|
| Arduino | Microcontroller | C/C++ (Arduino IDE) | Einfache Steuerungen, Prototyping |
| Raspberry Pi | Einplatinencomputer | Python, C, Java | Komplexere Anwendungen, Linux-basiert |
| ESP32 | Microcontroller + WiFi | C/C++, MicroPython | IoT mit WLAN-Anbindung |
| STM32 | Microcontroller | C/C++ | Industrielle Anwendungen |

---

## TK 4: Kenntnis des Zugriffs auf Sensoren/Aktoren

### GPIO (General Purpose Input/Output)

**Definition**: Programmierbare Ein-/Ausgabe-Pins an einem Microcontroller oder Einplatinencomputer.

| Modus | Beschreibung |
|-------|-------------|
| **Input** | Pin liest Wert (HIGH/LOW) – z.B. Taster |
| **Output** | Pin setzt Wert (HIGH/LOW) – z.B. LED ein/aus |
| **PWM** | Pulsweitenmodulation – steuert z.B. Helligkeit, Motorgeschwindigkeit |

### Kommunikationsprotokolle fuer Sensoren

| Protokoll | Beschreibung | Vorteile | Beispiele |
|-----------|-------------|---------|----------|
| **GPIO (digital)** | Einzelne Datenleitungen, HIGH/LOW | Einfach | Taster, LED |
| **I2C** | Serieller Bus, 2 Leitungen (SDA, SCL) | Viele Geraete an einem Bus | BME280, LCD-Display |
| **SPI** | Serieller Bus, 4 Leitungen | Schnell | SD-Karte, TFT-Display |
| **UART** | Serielle Schnittstelle, 2 Leitungen (TX, RX) | Einfach, weit verbreitet | GPS-Modul, Bluetooth |
| **1-Wire** | Ein-Draht-Bus | Nur eine Datenleitung | DS18B20 Temperatursensor |

---

## TK 5: Nutzung von Bibliotheken

### Beispiel-Bibliotheken

| Plattform | Bibliothek | Funktion |
|-----------|-----------|----------|
| Raspberry Pi (Python) | `RPi.GPIO` | GPIO-Pins steuern |
| Raspberry Pi (Python) | `gpiozero` | Vereinfachte GPIO-Steuerung |
| Raspberry Pi (Python) | `Adafruit_DHT` | DHT11/22 Temperatursensor |
| Arduino (C++) | `Servo.h` | Servomotor ansteuern |
| Arduino (C++) | `Wire.h` | I2C-Kommunikation |
| ESP32 (Python) | `machine` | Hardware-Zugriff (MicroPython) |
| Alle (Python) | `paho-mqtt` | MQTT-Kommunikation (IoT) |

### Beispiel: LED mit gpiozero (Python, Raspberry Pi)

```python
from gpiozero import LED
from time import sleep

led = LED(17)   # LED an GPIO Pin 17

while True:
    led.on()    # LED einschalten
    sleep(1)    # 1 Sekunde warten
    led.off()   # LED ausschalten
    sleep(1)
```

### Beispiel: Temperatursensor mit Bibliothek (Python)

```python
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 4    # GPIO Pin 4

feuchte, temperatur = Adafruit_DHT.read_retry(sensor, pin)

if temperatur is not None:
    print(f"Temperatur: {temperatur:.1f} Grad C")
    print(f"Luftfeuchtigkeit: {feuchte:.1f}%")
```
