# 3.3.06 – Vertiefung: Cyber-physische Systeme

## CPS im Kontext von IoT und Industrie 4.0

```
IoT-Architektur (vereinfacht)
+------------------------------------------------------------+
|                        Cloud / Server                       |
|  +------------------+  +------------------+  +----------+  |
|  | Datenbank        |  | Analyse / KI     |  | Dashboard|  |
|  +------------------+  +------------------+  +----------+  |
+-----------------------------+------------------------------+
                              |
                         Internet / WLAN
                              |
+-----------------------------+------------------------------+
|                     Gateway / Edge                          |
|  +------------------+  +------------------+                 |
|  | Datenvorverarbeitg|  | Protokoll-       |                |
|  |                  |  | Umwandlung       |                 |
|  +------------------+  +------------------+                 |
+-----------------------------+------------------------------+
                              |
                    Lokales Netz / Feldbus
                              |
+-----------------------------+------------------------------+
|                     CPS-Geraete (Sensoren/Aktoren)         |
|  [Temp] [Feuchte] [Kamera] [Motor] [Ventil] [LED]         |
+------------------------------------------------------------+
```

---

## PWM (Pulsweitenmodulation) im Detail

**Definition**: PWM steuert die "durchschnittliche" Spannung durch schnelles Ein- und Ausschalten des Signals.

```
Duty Cycle = Anteil der HIGH-Zeit pro Periode

100% Duty Cycle (immer an):
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| = volle Spannung

50% Duty Cycle:
|‾‾‾‾‾‾|______|‾‾‾‾‾‾|______| = halbe mittlere Spannung

25% Duty Cycle:
|‾‾‾|__________|‾‾‾|__________| = viertel mittlere Spannung

0% Duty Cycle (immer aus):
|__________________________| = keine Spannung
```

**Einsatz**:
- LED dimmen (25% = dunkler, 75% = heller)
- Motorgeschwindigkeit regeln
- Servomotor positionieren (Pulsbreite bestimmt Winkel)

---

## MQTT – IoT-Kommunikationsprotokoll

| Merkmal | Beschreibung |
|---------|-------------|
| Name | Message Queuing Telemetry Transport |
| Prinzip | Publish/Subscribe (Pub/Sub) |
| Broker | Zentraler Server, der Nachrichten verteilt |
| Topics | Hierarchische Nachrichtenkaanaele (z.B. `haus/wohnzimmer/temperatur`) |
| QoS | Quality of Service (0 = max. 1x, 1 = min. 1x, 2 = genau 1x) |
| Einsatz | IoT-Geraete, Smart Home, Industriesteuerung |

```
MQTT Publish/Subscribe-Muster:

  Sensor (Publisher)                    App (Subscriber)
       |                                      |
       |--- publish("haus/temp", "22.5") ---->|
       |                   |                   |
       |              [MQTT Broker]            |
       |                   |                   |
       |--- publish("haus/temp", "23.1") ---->|
```

---

## Vergleich: CPS-Plattformen

| Kriterium | Arduino Uno | Raspberry Pi 4 | ESP32 |
|-----------|-------------|----------------|-------|
| Typ | Microcontroller | Einplatinencomputer | Microcontroller + WiFi |
| CPU | ATmega328P (16 MHz) | Quad-Core ARM (1.5 GHz) | Dual-Core (240 MHz) |
| RAM | 2 KB | 1-8 GB | 520 KB |
| Speicher | 32 KB Flash | SD-Karte (beliebig) | 4 MB Flash |
| Betriebssystem | Keines (Bare Metal) | Linux (Raspbian/Raspberry Pi OS) | Keines / FreeRTOS |
| Sprachen | C/C++ | Python, C, Java, alles | C/C++, MicroPython |
| WiFi | Nein (Erweiterung noetig) | Ja (integriert) | Ja (integriert) |
| GPIO-Pins | 14 digital + 6 analog | 40 (nur digital) | 34 (digital + analog) |
| Stromverbrauch | Sehr gering (~50 mA) | Mittel (~600 mA - 2A) | Gering (~80 mA) |
| Preis | ~5-10 EUR | ~40-80 EUR | ~5-10 EUR |
| Einsatz | Einfache Steuerungen | Komplexe Anwendungen mit OS | IoT mit WiFi |

---

## Pruefungsaspekte

### Typische Fragestellungen

1. "Erklaeren Sie den Unterschied zwischen Sensor und Aktor"
2. "Nennen Sie drei Sensoren und deren Messwerte"
3. "Vergleichen Sie Polling und Interrupt"
4. "Beschreiben Sie den Aufbau eines CPS anhand eines Beispiels"
5. "Was ist PWM und wofuer wird es eingesetzt?"

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| Sensor und Aktor verwechseln | Sensor = misst (Eingabe), Aktor = handelt (Ausgabe) |
| Polling ist immer schlecht | Fuer langsame, regelmaessige Messungen ist Polling angemessen |
| Raspberry Pi ist ein Microcontroller | Raspberry Pi ist ein Einplatinencomputer mit vollem OS |
| GPIO-Pins koennen beliebige Lasten schalten | GPIO liefert nur geringe Stroeme (3.3V, ~16mA) – Relais noetig! |
| Abtastrate beliebig hoch waehlen | Hoehere Abtastrate = mehr Daten, mehr Stromverbrauch |
