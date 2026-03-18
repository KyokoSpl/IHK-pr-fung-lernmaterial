# Vertiefung: 1.6.04 – Umsetzung des Sicherheitskonzepts

## Vergleich: Backup-Verfahren

| Kriterium | Vollbackup | Inkrementell | Differenziell |
|---|---|---|---|
| **Sichert** | Alle Daten | Aenderungen seit letztem Backup (egal welcher Art) | Aenderungen seit letztem Vollbackup |
| **Speicher** | Hoch | Gering | Mittel (waechst taeglich) |
| **Geschwindigkeit Sicherung** | Langsam | Schnell | Mittel |
| **Wiederherstellung** | 1 Medium | Voll + alle Inkremente | Voll + letztes Differenz |
| **Risiko** | Gering | Hoch (1 Inkrement defekt → Kette unterbrochen) | Mittel |

## Vergleich: Berechtigungsmodelle

| Modell | Wer entscheidet? | Flexibilitaet | Sicherheit | Beispiel |
|---|---|---|---|---|
| **DAC** | Dateieigentuemer | Hoch | Mittel | Windows NTFS-Rechte |
| **MAC** | System/Admin | Gering | Sehr hoch | Militaerische Systeme |
| **RBAC** | Admin (ueber Rollen) | Mittel | Hoch | Active Directory |

## Vergleich: Digitale Signatur vs. Verschluesselung

| Kriterium | Digitale Signatur | Verschluesselung |
|---|---|---|
| **Zweck** | Authentizitaet + Integritaet | Vertraulichkeit |
| **Schluessel Sender** | Privater Schluessel (signieren) | Oeffentlicher Schluessel des Empfaengers |
| **Schluessel Empfaenger** | Oeffentlicher Schluessel (verifizieren) | Privater Schluessel (entschluesseln) |
| **Daten lesbar?** | Ja (Signatur ist Anhang) | Nein (Daten verschluesselt) |

## Zusammenhang der Massnahmen

```
Authentifizierung (2FA, Passwort)
        ↓
Zugangs-/Zugriffskontrolle (RBAC, Least Privilege)
        ↓
Verschluesselung (Daten in Ruhe + Transport)
        ↓
Haertung (Angriffsflaeche minimieren)
        ↓
Backup (Datenverlust absichern)
        ↓
Monitoring + Awareness (Vorfaelle erkennen + vermeiden)
```

## Typische Pruefungsaspekte

1. **Backup-Verfahren:** Voll/Inkrementell/Differenziell unterscheiden und Szenario loesen
2. **2FA:** Faktoren benennen und Beispiele geben
3. **Hashwerte:** Funktion erklaeren, Einsatzzweck nennen
4. **Digitale Signatur:** Ablauf Schritt fuer Schritt
5. **Haertung:** Mindestens 5 Massnahmen nennen
6. **Security by Design/Default:** Begriffe abgrenzen

## Haeufige Fehler

| Fehler | Richtig |
|---|---|
| Inkrementell = Differenziell | Inkrementell: seit letztem Backup; Differenziell: seit letztem Vollbackup |
| 2FA = „Passwort + Sicherheitsfrage" | Beides ist Faktor „Wissen" → nur 1 Faktor! |
| Hashwert = Verschluesselung | Hashing ist nicht umkehrbar, Verschluesselung schon |
| Signieren = Verschluesseln | Signatur nutzt privaten Schluessel, Verschluesselung den oeffentlichen des Empfaengers |
| Haertung ist einmalig | Haertung muss nach jedem Update ueberprueft werden |
