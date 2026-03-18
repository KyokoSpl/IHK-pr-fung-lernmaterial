# Uebungen: 1.6.04 – Umsetzung des Sicherheitskonzepts

## Aufgabe 1: Backup-Berechnung
Ein Unternehmen macht sonntags ein Vollbackup (200 GB). Taeglich kommen 20 GB hinzu.
a) Wie viel Speicher benoetigt eine Woche mit inkrementellen Backups (Mo-Sa)?
b) Wie viel Speicher benoetigt eine Woche mit differenziellen Backups (Mo-Sa)?
c) Am Donnerstag faellt das inkrementelle Backup von Dienstag aus. Was passiert bei der Wiederherstellung am Freitag?

## Aufgabe 2: 2FA-Szenarien
Welche der folgenden Kombinationen sind echte Zweifaktor-Authentifizierung? Begruende.
a) Passwort + Fingerabdruck
b) PIN + Passwort
c) Chipkarte + PIN
d) Gesichtserkennung + Iris-Scan
e) Passwort + OTP per Authenticator-App

## Aufgabe 3: Digitale Signatur
Erklaere in 5 Schritten den Ablauf einer digitalen Signatur. Welche Schutzziele werden damit gewaehrleistet?

## Aufgabe 4: OS-Haertung
Nenne 6 Massnahmen zur Haertung eines Windows-10-Arbeitsplatz-PCs.

## Aufgabe 5: Berechtigungsmodelle
Erklaere den Unterschied zwischen DAC und RBAC. Nenne jeweils ein Beispiel und bewerte, welches Modell fuer ein Unternehmen mit 500 Mitarbeitenden sinnvoller ist.

## Aufgabe 6: Hashwerte
a) Wofuer werden Hashwerte eingesetzt? Nenne 3 Einsatzbereiche.
b) Warum ist MD5 fuer sicherheitskritische Anwendungen nicht mehr geeignet?
c) Erklaere, warum ein Hashwert nicht „entschluesselt" werden kann.

## Aufgabe 7: Security by Design vs. Security by Default
Erklaere beide Begriffe und gib je ein IT-Beispiel.

---
---

# Loesungen

## Loesung 1
a) **Inkrementell:**
   - Vollbackup So: 200 GB
   - Mo-Sa je 20 GB = 6 × 20 = 120 GB
   - **Gesamt: 320 GB**

b) **Differenziell:**
   - Vollbackup So: 200 GB
   - Mo: 20 GB, Di: 40 GB, Mi: 60 GB, Do: 80 GB, Fr: 100 GB, Sa: 120 GB
   - Summe Diff: 420 GB
   - **Gesamt: 620 GB**

c) Bei inkrementellen Backups bilden die Sicherungen eine Kette. Wenn das Dienstag-Inkrement fehlt, koennen Mittwoch, Donnerstag und Freitag nicht vollstaendig wiederhergestellt werden → **Datenverlust fuer ab Dienstag geaenderte Daten**.

## Loesung 2
a) ✅ **Ja** – Wissen (Passwort) + Biometrie (Fingerabdruck) = 2 verschiedene Faktoren
b) ❌ **Nein** – Beides ist Wissen = nur 1 Faktor
c) ✅ **Ja** – Besitz (Chipkarte) + Wissen (PIN) = 2 Faktoren
d) ❌ **Nein** – Beides ist Biometrie = nur 1 Faktor
e) ✅ **Ja** – Wissen (Passwort) + Besitz (Smartphone mit App) = 2 Faktoren

## Loesung 3
1. Sender erstellt Nachricht (Klartext)
2. Sender berechnet kryptografischen Hash der Nachricht (z.B. SHA-256)
3. Sender verschluesselt den Hash mit seinem privaten Schluessel → digitale Signatur
4. Empfaenger entschluesselt Signatur mit dem oeffentlichen Schluessel des Senders → erhaelt Hash
5. Empfaenger berechnet eigenen Hash der empfangenen Nachricht und vergleicht → bei Uebereinstimmung: Integritaet und Authentizitaet bestaetigt

**Schutzziele:** Integritaet (Nachricht nicht veraendert), Authentizitaet (Sender verifiziert), Nichtabstreitbarkeit (Sender kann nicht leugnen)

## Loesung 4
1. Windows-Updates automatisch installieren
2. Windows Defender Firewall aktivieren
3. Nicht benoetigte Dienste deaktivieren (z.B. Remote Desktop, Telnet)
4. Lokales Gastkonto deaktivieren
5. Nutzer arbeiten NICHT als Administrator (Least Privilege)
6. BitLocker-Festplattenverschluesselung aktivieren

## Loesung 5
- **DAC (Discretionary Access Control):** Der Dateieigentuemer entscheidet, wer Zugriff bekommt. Beispiel: Nutzer teilt seinen Ordner per Rechtsklick → „Freigabe" mit einem Kollegen.
- **RBAC (Role-Based Access Control):** Rechte werden ueber Rollen vergeben, nicht individuell. Beispiel: Alle Mitglieder der Gruppe „Buchhaltung" erhalten automatisch Zugriff auf den Finanzordner.
- **Fuer 500 MA:** RBAC ist deutlich sinnvoller, da individuelle Rechtevergabe (DAC) bei 500 Personen unuebersichtlich und fehleranfaellig wird. RBAC erleichtert Onboarding/Offboarding und Audit.

## Loesung 6
a) Einsatzbereiche:
   - Integritaetspruefung (Datei unveraendert?)
   - Passwortspeicherung (Passwort wird als Hash gespeichert, nie im Klartext)
   - Digitale Signaturen (Hash der Nachricht wird signiert)

b) MD5 ist unsicher, weil Kollisionen gefunden wurden: Zwei verschiedene Eingaben koennen denselben MD5-Hash erzeugen. Angreifer koennen gefaelschte Dateien mit identischem Hash erstellen.

c) Hashing ist eine Einweg-Funktion: Aus der Eingabe wird ein fester Hashwert berechnet, aber die urspruengliche Eingabe kann aus dem Hash nicht zurueckgerechnet werden (Information geht verloren). Deshalb heisst es „hashen" und nicht „verschluesseln".

## Loesung 7
- **Security by Design:** Sicherheit wird schon in der Entwurfsphase beruecksichtigt. Beispiel: Eine Webanwendung wird von Anfang an mit Eingabevalidierung und Prepared Statements gegen SQL-Injection entwickelt.
- **Security by Default:** Die Standardeinstellungen eines Produkts sind maximal sicher. Beispiel: Ein neuer Router hat werksseitig die Firewall aktiviert und ein individuelles WLAN-Passwort statt „admin/admin".
