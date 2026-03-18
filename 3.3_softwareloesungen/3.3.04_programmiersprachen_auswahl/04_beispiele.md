# 3.3.04 – Beispiele: Situationsgerechte Auswahl einer Programmiersprache

## Beispiel 1: Sprachwahl fuer ein Startup-Projekt

**Szenario**: Ein Startup entwickelt eine Web-Plattform fuer Essensbestellungen. Das Team besteht aus 3 Entwicklern mit Python- und JavaScript-Erfahrung. Die Plattform soll schnell am Markt sein (MVP in 3 Monaten).

### Entscheidungsmatrix

| Kriterium | Gewicht | Python + Django | Java + Spring | C# + .NET |
|-----------|---------|----------------|--------------|-----------|
| Teamkompetenz | 30% | ++ (bekannt) | - (neu) | - (neu) |
| Time-to-Market | 25% | ++ (schnell) | + (mittel) | + (mittel) |
| Portabilitaet | 10% | ++ | ++ | ++ (.NET Core) |
| Performance | 15% | + (ausreichend) | ++ | ++ |
| Oekosystem | 20% | ++ (Django REST) | ++ (Spring Boot) | ++ (ASP.NET) |

**Empfehlung**: **Python + Django** – Das Team kennt Python, Django ermoeglicht schnelle Entwicklung, und fuer ein MVP ist die Performance ausreichend. Bei spaeterem Wachstum kann auf performantere Systeme migriert oder skaliert werden.

---

## Beispiel 2: Mobile App – Native vs. Cross-Platform

**Szenario**: Ein mittelstaendisches Unternehmen moechte eine Kunden-App fuer Android und iOS entwickeln. Budget ist begrenzt, das Team hat Web-Erfahrung (JavaScript/TypeScript).

| Option | Vorteile | Nachteile |
|--------|---------|-----------|
| **Native (Swift + Kotlin)** | Beste Performance, voller Zugriff auf OS-APIs | Zwei Codebases, doppelter Aufwand, Team kennt es nicht |
| **React Native** | Ein Code fuer beide Plattformen, Team kennt JS | Performance etwas schlechter, native Module manchmal noetig |
| **Flutter** | Ein Code, gute Performance, eigene Rendering-Engine | Neues Framework (Dart), kleinere Community bei Plugins |
| **Progressive Web App** | Kein App-Store noetig, Web-Technologie | Eingeschraenkter Zugriff auf Geraete-APIs |

**Empfehlung**: **React Native** – nutzt vorhandene JavaScript-Kenntnisse, eine Codebase fuer beide Plattformen, reiches Oekosystem, gute Community.

---

## Beispiel 3: Embedded System fuer Industriesteuerung

**Szenario**: Entwicklung einer Steuerungssoftware fuer eine Fertigungsmaschine. Echtzeitanforderungen, begrenzter Speicher (256 KB RAM), direkter Hardwarezugriff erforderlich.

| Kriterium | Bewertung |
|-----------|----------|
| Performance | C/C++ – direkter Hardwarezugriff, determinstische Ausfuehrung |
| Speicher | C – minimaler Overhead, manuelle Speicherverwaltung |
| Portabilitaet | Nicht relevant (spezifische Hardware) |
| Know-how | Embedded-Entwickler beherrschen C/C++ standardmaessig |
| Echtzeit | C/C++ mit RTOS (Real-Time Operating System) |

**Empfehlung**: **C/C++** – einzige realistische Wahl fuer Embedded mit Echtzeitanforderungen und begrenzten Ressourcen.

---

## Beispiel 4: IDE-Auswahl nach Projekt

| Projekt | Empfohlene IDE | Begruendung |
|---------|---------------|-------------|
| Java-Webapplikation mit Spring | IntelliJ IDEA | Beste Java-Unterstuetzung, Spring-Integration |
| Python Data Science | PyCharm / VS Code + Jupyter | Python-Tooling, Notebook-Support |
| C#/.NET Webservice | Visual Studio | .NET-Oekosystem, Debugging, NuGet |
| JavaScript/TypeScript Frontend | VS Code | Leichtgewichtig, groesstes Plugin-Oekosystem |
| iOS App (Swift) | Xcode | Einzige offizielle IDE fuer Apple-Plattformen |
| Android App (Kotlin) | Android Studio | Offizielles Android-SDK, Emulator |

---

## Beispiel 5: Framework vs. Bibliothek in der Praxis

### Bibliothek: Axios (JavaScript)

```
// DU rufst Axios auf – du hast die Kontrolle
const axios = require('axios');

async function holeDaten() {
    const antwort = await axios.get('/api/kunden');
    console.log(antwort.data);
}

holeDaten();  // Du entscheidest, wann und wie
```

### Framework: Express.js (JavaScript)

```
// Express gibt die Struktur vor – FRAMEWORK ruft deinen Code auf
const express = require('express');
const app = express();

// Du registrierst Handler (Callback) – Express ruft sie auf
app.get('/api/kunden', (req, res) => {
    res.json([{ id: 1, name: 'Mueller' }]);
});

app.listen(3000);  // Framework kontrolliert den Ablauf
```

**Unterschied verdeutlicht**:
- Bei **Axios** (Bibliothek): Du schreibst `holeDaten()` und rufst Axios auf
- Bei **Express** (Framework): Du registrierst einen Handler; Express entscheidet, WANN er aufgerufen wird (wenn ein Request kommt)
