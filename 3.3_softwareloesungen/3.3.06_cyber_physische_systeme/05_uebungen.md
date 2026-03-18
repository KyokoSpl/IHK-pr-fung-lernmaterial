# 3.3.06 – Uebungen: Cyber-physische Systeme

## Aufgabe 1: Sensor oder Aktor?

Ordne zu: Sensor (S) oder Aktor (A)?

| Nr. | Bauteil | S oder A? |
|-----|---------|-----------|
| a) | Temperaturfuehler (DHT22) | |
| b) | Servomotor | |
| c) | Ultraschallsensor (HC-SR04) | |
| d) | Relais | |
| e) | Fotowiderstand (LDR) | |
| f) | LCD-Display | |
| g) | PIR-Bewegungsmelder | |
| h) | Buzzer/Piezo | |
| i) | RFID-Leser | |
| j) | LED | |

---

## Aufgabe 2: Polling vs. Interrupt

Fuer welche der folgenden Anwendungen wuerdest du Polling verwenden, fuer welche Interrupt? Begruende kurz.

a) Rauchmelder – soll bei Rauchentwicklung sofort Alarm schlagen
b) Wetterstation – erfasst alle 10 Minuten Temperatur und Luftfeuchte
c) Notaus-Schalter an einer Maschine
d) Fuellstandsmessung eines Wassertanks (nicht zeitkritisch)
e) Tastendruck auf einem Bedienfeld

---

## Aufgabe 3: CPS-Entwurf

Entwirf ein Cyber-physisches System fuer einen **intelligenten Briefkasten**, der dem Bewohner eine Benachrichtigung sendet, wenn Post eingeworfen wurde.

a) Welche Sensoren und Aktoren werden benoetigt?
b) Welcher Abfragerhythmus ist sinnvoll (Polling oder Interrupt)?
c) Erstelle einen Pseudocode fuer die Steuerungslogik.
d) Welche Kommunikationstechnologie wuerdest du waehlen?

---

## Aufgabe 4: GPIO-Verstaendnis

Ein Raspberry Pi soll eine LED und einen Taster steuern. Erklaere:

a) Wie wird der GPIO-Pin fuer die LED konfiguriert?
b) Wie wird der GPIO-Pin fuer den Taster konfiguriert?
c) Was ist ein Pull-up / Pull-down Widerstand und warum wird er gebraucht?
d) Warum darf man einen Motor nicht direkt an einen GPIO-Pin anschliessen?

---

## Aufgabe 5: Kommunikationsprotokolle zuordnen

Welches Kommunikationsprotokoll (GPIO digital, I2C, SPI, UART) passt am besten?

| Bauteil | Protokoll? |
|---------|-----------|
| a) Einfacher Taster | |
| b) LCD-Display mit Adresse 0x27 | |
| c) GPS-Modul | |
| d) SD-Karten-Leser | |
| e) LED | |
| f) Temperatursensor BME280 | |

---
---

## Loesung Aufgabe 1

| Nr. | Bauteil | Typ | Begruendung |
|-----|---------|-----|-------------|
| a) | DHT22 | **Sensor** | Misst Temperatur + Feuchte |
| b) | Servomotor | **Aktor** | Bewegt etwas (Drehbewegung) |
| c) | HC-SR04 | **Sensor** | Misst Abstand |
| d) | Relais | **Aktor** | Schaltet Stromkreis |
| e) | LDR | **Sensor** | Misst Lichintensitaet |
| f) | LCD-Display | **Aktor** | Gibt Information aus (zeigt an) |
| g) | PIR-Bewegungsmelder | **Sensor** | Erkennt Bewegung |
| h) | Buzzer | **Aktor** | Erzeugt Ton |
| i) | RFID-Leser | **Sensor** | Liest Daten von RFID-Karte |
| j) | LED | **Aktor** | Erzeugt Licht |

---

## Loesung Aufgabe 2

| Anwendung | Methode | Begruendung |
|-----------|---------|-------------|
| a) Rauchmelder | **Interrupt** | Sofortige Reaktion bei Rauch lebensrettend |
| b) Wetterstation | **Polling** | Regelmaessige Messung ausreichend, nicht zeitkritisch |
| c) Notaus-Schalter | **Interrupt** | Sicherheitskritisch, sofortige Abschaltung noetig |
| d) Fuellstandsmessung | **Polling** | Nicht zeitkritisch, regelmaessige Abfrage genuegt |
| e) Tastendruck | **Interrupt** | Sofortige Reaktion auf Benutzereingabe erwartet |

---

## Loesung Aufgabe 3

### a) Komponenten
- **Sensor**: Lichtsensor (LDR) oder Lichtschranke im Briefkasteneinwurf – erkennt, wenn etwas eingeworfen wird
- **Alternative Sensor**: Neigungssensor an der Klappe oder Gewichtssensor auf dem Boden
- **Aktor**: LED (Status-Anzeige), optional Buzzer (lokaler Alarm)
- **Controller**: ESP32 (WiFi integriert)

### b) Abfragerhythmus
**Interrupt** – der Einwurf ist ein seltenes, punktuelles Ereignis. Polling wuerde unnoetig Strom verbrauchen. GPIO-Interrupt bei Zustandsaenderung des Sensors.

### c) Pseudocode
```
FUNKTION bei_post_eingeworfen()
    zeitstempel = aktuelle_zeit()
    led.einschalten()
    sende_nachricht("Post eingeworfen um " + zeitstempel)
    warte(500)   // Entprellung
ENDE-FUNKTION

// Interrupt registrieren
registriere_interrupt(SENSOR_PIN, FALLENDE_FLANKE, bei_post_eingeworfen)

// Hauptprogramm: Energiesparmodus
WIEDERHOLE
    deep_sleep(60)    // CPU schlaeft, Interrupt weckt
ENDLOS
```

### d) Kommunikationstechnologie
**WiFi + MQTT** oder **WiFi + Push-Notification** (z.B. ueber einen Dienst wie Pushover, IFTTT). ESP32 hat WiFi integriert, MQTT ist leichtgewichtig fuer IoT.

---

## Loesung Aufgabe 4

a) **LED**: GPIO-Pin als **Output** konfigurieren (`GPIO.setup(pin, GPIO.OUT)`). Pin auf HIGH setzen → LED leuchtet, LOW → LED aus.

b) **Taster**: GPIO-Pin als **Input** konfigurieren (`GPIO.setup(pin, GPIO.IN)`). Zustand per `GPIO.input(pin)` abfragen.

c) **Pull-up/Pull-down Widerstand**: Definiert den Zustand eines Input-Pins, wenn KEIN Signal anliegt (z.B. Taster nicht gedrueckt). Ohne Widerstand "schwebt" der Pin (floating) und liefert zufaellige Werte.
   - **Pull-up**: Pin ist standardmaessig HIGH, wird durch Taster auf LOW gezogen
   - **Pull-down**: Pin ist standardmaessig LOW, wird durch Taster auf HIGH gezogen

d) **Motor direkt an GPIO**: GPIO-Pins liefern nur ca. **3.3V und max. 16mA**. Ein Motor braucht deutlich mehr Strom (100mA+) und erzeugt beim Abschalten Spannungsspitzen (Induktivitaet), die den GPIO-Pin oder den gesamten Raspberry Pi zerstoeren koennen. Loesung: **Motortreiber** (z.B. L293D) oder **Relais** verwenden.

---

## Loesung Aufgabe 5

| Bauteil | Protokoll | Begruendung |
|---------|-----------|-------------|
| a) Taster | **GPIO digital** | Einfaches HIGH/LOW-Signal |
| b) LCD-Display 0x27 | **I2C** | Adresse deutet auf I2C-Bus hin |
| c) GPS-Modul | **UART** | Typische serielle Verbindung (TX/RX) |
| d) SD-Karten-Leser | **SPI** | Schnelle Datenuebertragung ueber SPI |
| e) LED | **GPIO digital** | Einfaches Ein/Aus (oder PWM zum Dimmen) |
| f) BME280 | **I2C** (oder SPI) | Standard-I2C-Sensor, auch SPI moeglich |
