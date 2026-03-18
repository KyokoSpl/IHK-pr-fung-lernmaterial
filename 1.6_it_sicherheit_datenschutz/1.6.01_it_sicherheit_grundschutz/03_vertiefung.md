# Vertiefung: 1.6.01 – IT-Sicherheit auf Grundschutzniveau

## Vergleich: Verschluesselungsverfahren

| Kriterium | Symmetrisch | Asymmetrisch | Hybrid |
|---|---|---|---|
| **Schluesselanzahl** | 1 (gemeinsam) | 2 (oeffentlich + privat) | Beide |
| **Geschwindigkeit** | Schnell | Langsam | Schnell (nach Handshake) |
| **Schluesselproblem** | Schluesselaustausch unsicher | Kein Austauschproblem | Geloest |
| **Einsatz** | Dateiverschluesselung, AES | Signaturen, Schluesselaustausch | TLS/HTTPS |
| **Beispiele** | AES-256, 3DES | RSA, ECC | TLS 1.3 |

## Vergleich: Anonymisierung vs. Pseudonymisierung

| Kriterium | Anonymisierung | Pseudonymisierung |
|---|---|---|
| **Personenbezug** | Vollstaendig entfernt | Durch Kennzeichen ersetzt |
| **DSGVO-Anwendbarkeit** | DSGVO gilt NICHT mehr | DSGVO gilt weiterhin |
| **Umkehrbar** | Nein | Ja (mit Zuordnungstabelle) |
| **Beispiel** | „42% der Befragten nutzen Linux" | „Kunde K-1234 hat Ticket eroeffnet" |

## Vergleich: Zutritt / Zugang / Zugriff

| Kontrolle | Schutz gegen | Massnahme | Beispiel |
|---|---|---|---|
| **Zutrittskontrolle** | Unbefugtes Betreten | Physische Barrieren | Chipkarte, Schliessanlage |
| **Zugangskontrolle** | Unbefugte Systemnutzung | Authentifizierung | Login, Biometrie |
| **Zugriffskontrolle** | Unbefugten Datenzugriff | Autorisierung | Berechtigungskonzept, Rollen |

## Zusammenhang: BSI-Grundschutz und DSGVO

```
DSGVO (Datenschutz) ←→ BSI-Grundschutz (Informationssicherheit)
         ↓                        ↓
  Schutz personenbez.       Schutz aller
  Daten                     Informationen
         ↓                        ↓
  TOM nach Art. 32    BSI-Bausteine + Anforderungen
         ↓                        ↓
           → Gemeinsam: Schutzziele CIA ←
```

## Typische Pruefungsaspekte

1. **Schutzziele benennen:** CIA-Dreieck mit Beispielen erklaeren
2. **Verschluesselung:** Symmetrisch vs. asymmetrisch unterscheiden
3. **DSGVO-Grundsaetze:** Die 7 Verarbeitungsgrundsaetze nennen
4. **Betroffenenrechte:** Mindestens 4 Rechte mit Artikeln nennen
5. **TOM-Kategorien:** Zutritt/Zugang/Zugriff korrekt zuordnen
6. **Rollen unterscheiden:** IT-Sicherheitsbeauftragter ≠ Datenschutzbeauftragter

## Haeufige Fehler

| Fehler | Richtig |
|---|---|
| Anonymisierung = Pseudonymisierung | Anonymisierung ist irreversibel, Pseudonymisierung nicht |
| DSGVO gilt nur fuer digitale Daten | DSGVO gilt auch fuer analoge personenbezogene Daten |
| Zugang = Zutritt | Zutritt = physisch, Zugang = System-Login |
| IP-Adresse ist kein personenbezogenes Datum | IP-Adressen sind personenbezogene Daten (EuGH-Urteil) |
| Datenschutzbeauftragter ist weisungsgebunden | DSB ist weisungsfrei (Art. 38 DSGVO) |
| Symmetrische Verschluesselung ist unsicher | Sie ist schnell und sicher, nur der Schluesselaustausch ist problematisch |
