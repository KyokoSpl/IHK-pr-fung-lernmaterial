# 3.3.07 – Wiederkehrende Systemablaeufe automatisieren

## Einordnung

Dieses Thema gehoert zum Bereich **3.3 Programmieren von Softwareloesungen** und behandelt die Automatisierung von wiederkehrenden Aufgaben durch **Shellprogrammierung** und **Skriptprogrammierung**.

## Themenkreise

| Nr. | Themenkreis | Schwerpunkt |
|-----|-------------|-------------|
| 1 | Shellprogrammierung (PowerShell, Bash) | Systemadministration, Automatisierung |
| 2 | Skriptprogrammierung (Python) | Dateiverarbeitung, Reporting, Automation |

---

## Querverweise

- **3.3.04** – Programmiersprachen-Auswahl (Scripting vs. kompilierte Sprachen)
- **3.3.06** – CPS (Automatisierung mit Skripten)
- **2.1** – Netzwerktechnik (Netzwerkautomatisierung)

---

## 1. Bash (Linux/macOS)

### Grundlagen

| Element | Syntax | Beispiel |
|---------|--------|---------|
| Shebang | `#!/bin/bash` | Erste Zeile jedes Skripts |
| Variable setzen | `NAME=wert` | `DATEI="log.txt"` |
| Variable lesen | `$NAME` oder `${NAME}` | `echo $DATEI` |
| Eingabe | `read VARIABLE` | `read -p "Name: " NAME` |
| Ausgabe | `echo "text"` | `echo "Hallo $NAME"` |
| Kommentar | `# Kommentar` | `# Dies ist ein Kommentar` |
| Ausfuehrbar machen | `chmod +x skript.sh` | Dann: `./skript.sh` |

### Kontrollstrukturen in Bash

**if-Verzweigung**:
```bash
#!/bin/bash
if [ -f "/var/log/syslog" ]; then
    echo "Logdatei existiert"
    GROESSE=$(du -h /var/log/syslog | cut -f1)
    echo "Groesse: $GROESSE"
else
    echo "Logdatei nicht gefunden"
fi
```

**for-Schleife**:
```bash
#!/bin/bash
# Alle .log-Dateien im Verzeichnis durchgehen
for DATEI in /var/log/*.log; do
    echo "Verarbeite: $DATEI"
    wc -l "$DATEI"       # Zeilen zaehlen
done
```

**while-Schleife**:
```bash
#!/bin/bash
ZAEHLER=1
while [ $ZAEHLER -le 5 ]; do
    echo "Durchlauf $ZAEHLER"
    ZAEHLER=$((ZAEHLER + 1))
done
```

### Wichtige Bash-Befehle fuer Automation

| Befehl | Funktion | Beispiel |
|--------|----------|---------|
| `grep` | Text suchen | `grep "ERROR" logfile.txt` |
| `awk` | Textverarbeitung spaltenweise | `awk '{print $1, $3}' datei.txt` |
| `sed` | Text ersetzen (Stream Editor) | `sed 's/alt/neu/g' datei.txt` |
| `cut` | Spalten ausschneiden | `cut -d',' -f2 datei.csv` |
| `sort` | Zeilen sortieren | `sort -n zahlen.txt` |
| `wc` | Zeilen/Woerter/Zeichen zaehlen | `wc -l datei.txt` |
| `find` | Dateien suchen | `find /home -name "*.pdf"` |
| `tar` | Archiv erstellen/entpacken | `tar -czf backup.tar.gz /daten` |
| `cron` | Zeitgesteuerte Ausfuehrung | `crontab -e` |
| `rsync` | Dateien synchronisieren | `rsync -av quelle/ ziel/` |

### Praxisbeispiel: Backup-Skript (Bash)

```bash
#!/bin/bash
# Taegliches Backup-Skript
QUELLE="/home/benutzer/dokumente"
ZIEL="/backup"
DATUM=$(date +%Y-%m-%d)
DATEINAME="backup_$DATUM.tar.gz"

echo "Starte Backup: $DATUM"

# Backup erstellen
tar -czf "$ZIEL/$DATEINAME" "$QUELLE" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "Backup erfolgreich: $ZIEL/$DATEINAME"
    # Alte Backups loeschen (aelter als 30 Tage)
    find "$ZIEL" -name "backup_*.tar.gz" -mtime +30 -delete
    echo "Alte Backups bereinigt."
else
    echo "FEHLER: Backup fehlgeschlagen!" >&2
fi
```

### Cron-Jobs (zeitgesteuerte Ausfuehrung)

```
# Crontab-Syntax:
# Min  Std  Tag  Mon  WTag  Befehl
# *    *    *    *    *     command

# Jeden Tag um 02:00 Uhr Backup ausfuehren
0 2 * * * /home/benutzer/backup.sh

# Jeden Montag um 06:00 Uhr
0 6 * * 1 /home/benutzer/wochenbericht.sh

# Alle 15 Minuten
*/15 * * * * /home/benutzer/check_service.sh

# Am 1. jedes Monats um 00:00
0 0 1 * * /home/benutzer/monatsreport.sh
```

**Crontab-Felder**:
```
┌───────── Minute (0-59)
│ ┌─────── Stunde (0-23)
│ │ ┌───── Tag im Monat (1-31)
│ │ │ ┌─── Monat (1-12)
│ │ │ │ ┌─ Wochentag (0-7, 0 und 7 = Sonntag)
│ │ │ │ │
* * * * * Befehl
```

---

## 2. PowerShell (Windows)

### Grundlagen

| Element | Syntax | Beispiel |
|---------|--------|---------|
| Variable | `$Name = wert` | `$Pfad = "C:\Logs"` |
| Ausgabe | `Write-Host "text"` | `Write-Host "Hallo $Name"` |
| Pipe | `Befehl1 | Befehl2` | `Get-Process | Sort-Object CPU` |
| Cmdlet-Schema | `Verb-Substantiv` | `Get-Service`, `Stop-Process` |
| Hilfe | `Get-Help Cmdlet` | `Get-Help Get-Process` |

### Wichtige PowerShell-Cmdlets

| Cmdlet | Funktion | Beispiel |
|--------|----------|---------|
| `Get-ChildItem` | Verzeichnis auflisten (≈ ls/dir) | `Get-ChildItem C:\Logs` |
| `Get-Content` | Dateiinhalt lesen (≈ cat) | `Get-Content log.txt` |
| `Set-Content` | In Datei schreiben | `"Text" | Set-Content datei.txt` |
| `Get-Process` | Laufende Prozesse | `Get-Process | Where CPU -gt 50` |
| `Get-Service` | Windows-Dienste | `Get-Service | Where Status -eq "Stopped"` |
| `Start-Service` | Dienst starten | `Start-Service -Name "Spooler"` |
| `Copy-Item` | Datei kopieren | `Copy-Item quelle.txt ziel.txt` |
| `Remove-Item` | Datei loeschen | `Remove-Item *.tmp` |
| `Select-String` | Text suchen (≈ grep) | `Select-String "ERROR" log.txt` |
| `Export-Csv` | Daten als CSV exportieren | `Get-Process | Export-Csv procs.csv` |

### Praxisbeispiel: Dienst-Ueberwachung (PowerShell)

```powershell
# Dienste pruefen und bei Bedarf neustarten
$Dienste = @("Spooler", "W3SVC", "MSSQLSERVER")

foreach ($Dienst in $Dienste) {
    $Status = Get-Service -Name $Dienst -ErrorAction SilentlyContinue

    if ($Status.Status -ne "Running") {
        Write-Host "WARNUNG: $Dienst ist gestoppt. Starte neu..."
        Start-Service -Name $Dienst
        $Zeitstempel = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        Add-Content -Path "C:\Logs\dienst_log.txt" `
            -Value "$Zeitstempel - $Dienst wurde neugestartet"
    } else {
        Write-Host "$Dienst laeuft normal."
    }
}
```

### Windows Task Scheduler (≈ Cron unter Linux)

| Merkmal | Beschreibung |
|---------|-------------|
| GUI | Aufgabenplanung ueber `taskschd.msc` |
| CLI | `schtasks /Create /SC DAILY /TN "Backup" /TR "C:\backup.ps1" /ST 02:00` |
| Trigger | Zeitbasiert, ereignisbasiert, bei Anmeldung, bei Start |
| Aktion | Programm starten, E-Mail senden |

---

## 3. Python-Skriptprogrammierung

### Praxisbeispiel: Log-Analyse (Python)

```python
#!/usr/bin/env python3
"""Analysiert Logdatei und erstellt Zusammenfassung."""
import re
from collections import Counter
from datetime import date

LOG_DATEI = "/var/log/application.log"
REPORT = f"/tmp/report_{date.today()}.txt"

# Fehlermeldungen zaehlen
fehler_zaehler = Counter()

with open(LOG_DATEI, "r") as f:
    for zeile in f:
        if "ERROR" in zeile:
            # Fehlerkategorie extrahieren (z.B. "[DB_ERROR]")
            match = re.search(r'\[(\w+_ERROR)\]', zeile)
            if match:
                fehler_zaehler[match.group(1)] += 1

# Report erstellen
with open(REPORT, "w") as f:
    f.write(f"=== Fehlerreport vom {date.today()} ===\n\n")
    f.write(f"Gesamtfehler: {sum(fehler_zaehler.values())}\n\n")
    for fehler, anzahl in fehler_zaehler.most_common():
        f.write(f"  {fehler}: {anzahl}x\n")

print(f"Report erstellt: {REPORT}")
```

### Praxisbeispiel: Dateien organisieren (Python)

```python
#!/usr/bin/env python3
"""Sortiert Dateien in einem Ordner nach Dateityp in Unterordner."""
import os
import shutil

QUELLE = "/home/benutzer/Downloads"

ZUORDNUNG = {
    ".pdf": "Dokumente",
    ".docx": "Dokumente",
    ".xlsx": "Tabellen",
    ".jpg": "Bilder",
    ".png": "Bilder",
    ".mp3": "Musik",
    ".mp4": "Videos",
    ".zip": "Archive",
}

for dateiname in os.listdir(QUELLE):
    dateipfad = os.path.join(QUELLE, dateiname)

    if os.path.isfile(dateipfad):
        _, endung = os.path.splitext(dateiname)
        zielordner = ZUORDNUNG.get(endung.lower(), "Sonstiges")
        zielpfad = os.path.join(QUELLE, zielordner)

        os.makedirs(zielpfad, exist_ok=True)
        shutil.move(dateipfad, os.path.join(zielpfad, dateiname))
        print(f"Verschoben: {dateiname} → {zielordner}/")
```

---

## Vergleich: Bash vs. PowerShell vs. Python

| Kriterium | Bash | PowerShell | Python |
|-----------|------|-----------|--------|
| Plattform | Linux/macOS | Windows (auch Linux) | Alle |
| Staerke | Dateioperationen, Pipes | Windows-Administration | Komplexe Logik, APIs |
| Syntax | Kompakt, kryptisch | Ausfuehrlich, lesbar | Klar, universell |
| Datentypen | Alles ist Text | Objekte (strukturiert) | Alle Typen |
| Einsatz | Server-Automation, Cron | Windows-Server, AD | Reporting, Web, Scripting |

---

## Pruefungsaspekte

### Haeufige Fehler

| Fehler | Korrektur |
|--------|-----------|
| Bash-Skript nicht ausfuehrbar | `chmod +x skript.sh` nicht vergessen |
| Leerzeichen bei Bash if-Bedingung fehlen | `[ $x -eq 5 ]` – Leerzeichen sind Pflicht! |
| PowerShell-Execution-Policy blockiert | `Set-ExecutionPolicy RemoteSigned` setzen |
| Cron-Syntax verwechselt | Minute ZUERST, dann Stunde (nicht umgekehrt) |
| Python-Pfade unter Windows mit Backslash | `os.path.join()` oder raw Strings `r"C:\pfad"` verwenden |

---

## Uebungen

### Aufgabe 1
Schreibe ein Bash-Skript, das alle `.tmp`-Dateien in `/tmp` zaehlt und loescht. Am Ende soll ausgegeben werden, wie viele Dateien geloescht wurden.

### Aufgabe 2
Erklaere den folgenden Crontab-Eintrag:
```
30 6 * * 1-5 /opt/scripts/backup.sh
```

### Aufgabe 3
Schreibe ein Python-Skript, das alle CSV-Dateien in einem Verzeichnis liest und die Anzahl der Zeilen pro Datei ausgibt.

---
---

## Loesung Aufgabe 1

```bash
#!/bin/bash
ANZAHL=$(find /tmp -maxdepth 1 -name "*.tmp" -type f | wc -l)
find /tmp -maxdepth 1 -name "*.tmp" -type f -delete
echo "$ANZAHL .tmp-Datei(en) geloescht."
```

## Loesung Aufgabe 2

| Feld | Wert | Bedeutung |
|------|------|-----------|
| Minute | 30 | Um Minute 30 |
| Stunde | 6 | Um 6 Uhr |
| Tag | * | Jeden Tag |
| Monat | * | Jeden Monat |
| Wochentag | 1-5 | Montag bis Freitag |

**Zusammen**: Das Skript `/opt/scripts/backup.sh` wird **jeden Werktag (Mo-Fr) um 06:30 Uhr** ausgefuehrt.

## Loesung Aufgabe 3

```python
#!/usr/bin/env python3
import os

VERZEICHNIS = "/pfad/zum/verzeichnis"

for datei in os.listdir(VERZEICHNIS):
    if datei.endswith(".csv"):
        pfad = os.path.join(VERZEICHNIS, datei)
        with open(pfad, "r") as f:
            zeilen = sum(1 for _ in f)
        print(f"{datei}: {zeilen} Zeilen")
```
