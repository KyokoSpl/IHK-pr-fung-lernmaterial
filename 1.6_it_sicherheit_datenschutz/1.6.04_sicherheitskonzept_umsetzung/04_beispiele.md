# Beispiele: 1.6.04 – Umsetzung des Sicherheitskonzepts

## Beispiel 1: Backup-Strategie (1 Woche)

**Szenario:** Wochentags werden 50 GB Daten generiert. Sonntag: Vollbackup.

| Tag | Typ | Sichert | Speicher (kumuliert) |
|---|---|---|---|
| So | Vollbackup | 500 GB | 500 GB |
| Mo | Inkrementell | 50 GB (nur Mo) | 550 GB |
| Di | Inkrementell | 50 GB (nur Di) | 600 GB |
| Mi | Inkrementell | 50 GB (nur Mi) | 650 GB |
| Do | Inkrementell | 50 GB (nur Do) | 700 GB |
| Fr | Inkrementell | 50 GB (nur Fr) | 750 GB |

**Wiederherstellung Freitag:** Vollbackup (So) + Inkrement Mo + Di + Mi + Do + Fr = 6 Medien noetig

**Alternative mit differenziell:**

| Tag | Typ | Sichert | Speicher |
|---|---|---|---|
| So | Vollbackup | 500 GB | 500 GB |
| Mo | Differenziell | 50 GB | 50 GB |
| Di | Differenziell | 100 GB (Mo+Di) | 100 GB |
| Fr | Differenziell | 250 GB (Mo-Fr) | 250 GB |

**Wiederherstellung Freitag:** Vollbackup (So) + Differenz Fr = nur 2 Medien

---

## Beispiel 2: Digitale Signatur – Ablauf

**Szenario:** Alice sendet eine signierte E-Mail an Bob.

```
Alice:
1. Schreibt E-Mail (Klartext)
2. Berechnet SHA-256-Hash der E-Mail → z.B. "a7f3..."
3. Verschluesselt Hash mit ihrem privaten Schluessel → Signatur
4. Sendet: E-Mail + Signatur

Bob:
1. Empfaengt E-Mail + Signatur
2. Entschluesselt Signatur mit Alices oeffentlichem Schluessel → Hash "a7f3..."
3. Berechnet selbst SHA-256-Hash der empfangenen E-Mail → "a7f3..."
4. Vergleich: Stimmen ueberein? → Integritaet + Authentizitaet bestaetigt ✓
```

---

## Beispiel 3: OS-Haertung Windows-Arbeitsplatz

| Massnahme | Umsetzung |
|---|---|
| Updates | Windows Update automatisch aktivieren |
| Dienste | Nicht benoetigte Dienste deaktivieren (z.B. Remote Registry) |
| Admin-Konto | Standard-Admin umbenennen, lokales Gastkonto deaktivieren |
| Firewall | Windows Defender Firewall aktivieren |
| Rechte | Nutzer arbeiten NICHT als Administrator |
| Autostart | Programme in Autostart pruefen und bereinigen |
| Logging | Sicherheitsprotokoll aktivieren |
| Verschluesselung | BitLocker fuer Festplatte aktivieren |

---

## Beispiel 4: 2FA im Unternehmen

**Szenario:** Mitarbeiter meldet sich am Firmen-VPN an.

1. Schritt 1 (Wissen): Benutzername + Passwort eingeben
2. Schritt 2 (Besitz): Push-Benachrichtigung auf Firmen-Smartphone bestaetigen

→ Selbst bei gestohlenem Passwort kann der Angreifer ohne das Smartphone nicht zugreifen.

**NICHT 2FA:**
- Passwort + Sicherheitsfrage = beides „Wissen" = nur 1 Faktor
- Passwort + zweites Passwort = beides „Wissen" = nur 1 Faktor

---

## Beispiel 5: RBAC in Active Directory

```
Rollen:
├── Geschaeftsfuehrung  → Zugriff: Alles
├── IT-Administration   → Zugriff: Server, Netzwerk, AD
├── Buchhaltung         → Zugriff: Finanzsystem, Rechnungsordner
├── Entwicklung         → Zugriff: Git-Server, Dev-Umgebung, Datenbank
└── Praktikant          → Zugriff: Wiki, E-Mail (Least Privilege!)

Mitarbeiter:
- Max Mueller → Rolle: Entwicklung → erhaelt automatisch alle Entwickler-Rechte
- Neues Mitglied im Team? → Rolle zuweisen, nicht einzelne Rechte
```
