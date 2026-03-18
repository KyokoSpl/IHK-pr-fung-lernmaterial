# Ueberblick und Grundlagen: 3.2.01 – Technische und organisatorische Massnahmen (TOM)

## Einordnung

- **Pruefungsteil:** 3.2 – Inbetriebnehmen von Speicherloesungen
- **Thema-ID:** 3.2.01
- **Thema:** Technische und organisatorische Massnahmen (TOM)

## Ziel

Du musst die drei Schutzziele (Vertraulichkeit, Integritaet, Verfuegbarkeit) verstehen und technische sowie organisatorische Massnahmen unterscheiden koennen. Insbesondere die Abgrenzung von Zugang, Zutritt und Zugriff ist pruefungsrelevant.

## Themenkreise im Ueberblick

| Nr. | Themenkreis | Schwerpunkt |
|-----|-------------|-------------|
| 1 | Berechtigungskonzepte | RBAC, DAC, MAC, Least-Privilege-Prinzip |
| 2 | Organisationsstrukturen (Zugang, Zutritt, Zugriff) | Abgrenzung der drei Begriffe, physische und logische Kontrolle |

### Querverweise
- Thema 3.2.02: Physische/hardwaretechnische Absicherung (Zutrittskontrollen)
- Thema 3.2.03: Softwaretechnische Absicherung (Zugriffsmanagement, Verschluesselung)
- Thema 3.1.07: IT-Sicherheit und Schutzziele

---

## Grundlagen

### 1. Berechtigungskonzepte

**Definition:** Ein Berechtigungskonzept legt fest, welche Personen oder Systeme auf welche Ressourcen mit welchen Rechten zugreifen duerfen. Es dient der Umsetzung des Schutzziels Vertraulichkeit.

**Kernaussagen:**
- Berechtigungen werden nach dem **Need-to-know-Prinzip** vergeben
- Das **Least-Privilege-Prinzip** (Minimalprinzip) gibt jedem Nutzer nur die Rechte, die er fuer seine Aufgabe benoetigt
- Berechtigungen werden regelmaessig ueberprueft (Rezertifizierung)
- Trennung von Pflichten (Separation of Duties) verhindert Missbrauch

**Modelle im Vergleich:**

| Modell | Abkuerzung | Beschreibung | Beispiel |
|--------|-----------|--------------|----------|
| Role-Based Access Control | RBAC | Rechte werden Rollen zugeordnet, Benutzer erhalten Rollen | Rolle "Buchhalter" darf auf Finanzdaten zugreifen |
| Discretionary Access Control | DAC | Der Eigentuemer einer Ressource bestimmt die Rechte | Dateibesitzer legt Lese-/Schreibrechte fest (z.B. NTFS) |
| Mandatory Access Control | MAC | System erzwingt Regeln, Benutzer kann sie nicht aendern | Sicherheitsstufen im militaerischen Bereich (Top Secret, Secret) |
| Attribute-Based Access Control | ABAC | Zugriff basiert auf Attributen (Rolle, Standort, Zeit) | Zugriff nur waehrend der Arbeitszeit von Firmen-IP |

**Wichtige Begriffe:**
- **Least Privilege** – minimale Rechtevergabe fuer die jeweilige Aufgabe
- **Need-to-know** – Informationen nur fuer diejenigen, die sie benoetigen
- **Rezertifizierung** – regelmaessige Ueberpruefung vergebener Rechte
- **Separation of Duties** – Trennung kritischer Aufgaben auf verschiedene Personen

**Erklaerung:** In der Praxis wird am haeufigsten RBAC eingesetzt, da es gut skaliert. Neue Mitarbeiter erhalten eine Rolle (z.B. "Entwickler"), die vordefinierte Rechte mitbringt. Bei Abteilungswechsel wird die Rolle geaendert – nicht einzelne Rechte.

---

### 2. Organisationsstrukturen (Zugang, Zutritt, Zugriff)

**Definition:** Die drei Begriffe Zutritt, Zugang und Zugriff beschreiben unterschiedliche Ebenen des Schutzes von IT-Systemen und Daten. Sie bilden die Grundlage der technischen und organisatorischen Massnahmen (TOM) gemaess DSGVO.

**Abgrenzung der drei Begriffe:**

| Begriff | Ebene | Schutz vor | Beispiel |
|---------|-------|-----------|----------|
| **Zutritt** | Physisch | Unbefugtes Betreten von Raeumen/Gebaeuden | Schliessanlage, Chipkarte, Pfoertner, Videoueberwachung |
| **Zugang** | Logisch (Systemebene) | Unbefugtes Nutzen von IT-Systemen | Benutzername/Passwort, Zwei-Faktor-Authentifizierung, biometrische Anmeldung |
| **Zugriff** | Logisch (Datenebene) | Unbefugtes Lesen/Aendern/Loeschen von Daten | Dateiberechtigungen (NTFS), Datenbankrechte, Verschluesselung |

**Eselsbruecke:**
```
Zutritt  →  Tuer     →  Wer darf in den Raum?
Zugang   →  Anmelden →  Wer darf das System nutzen?
Zugriff  →  Daten    →  Wer darf welche Daten sehen/aendern?
```

**Technische vs. organisatorische Massnahmen:**

| Typ | Beschreibung | Beispiele |
|-----|-------------|----------|
| **Technische Massnahmen** | Durch Technik umgesetzte Schutzmechanismen | Firewall, Verschluesselung, Zugangskontrollsysteme, Backup |
| **Organisatorische Massnahmen** | Durch Regeln und Prozesse umgesetzte Schutzmechanismen | Schulungen, Richtlinien, Besucherregelungen, Clean-Desk-Policy |

**Wichtige Begriffe:**
- **TOM** – Technische und Organisatorische Massnahmen (Art. 32 DSGVO)
- **Zwei-Faktor-Authentifizierung (2FA)** – Kombination aus zwei Authentifizierungsfaktoren (z.B. Passwort + Token)
- **Clean-Desk-Policy** – keine vertraulichen Unterlagen sichtbar am Arbeitsplatz
- **Besucherregelung** – Dokumentation und Begleitung von Gaesten im Unternehmen

**Erklaerung:** Fuer die Pruefung ist die korrekte Zuordnung von Massnahmen zu Zutritt, Zugang oder Zugriff entscheidend. Beispiel: Ein Fingerabdruckscanner am Serverraum ist eine **Zutrittskontrolle**. Ein Fingerabdruckscanner zur Anmeldung am Laptop ist eine **Zugangskontrolle**.

---

## Vertiefung

### Zusammenspiel der drei Ebenen

```
+-----------------------------------------------------+
|                  PHYSISCH (Zutritt)                   |
|  Gebaeude → Etage → Serverraum → Serverschrank       |
|  +-----------------------------------------------+   |
|  |            SYSTEM (Zugang)                     |   |
|  |  Login → Authentifizierung → Autorisierung     |   |
|  |  +---------------------------------------+     |   |
|  |  |          DATEN (Zugriff)              |     |   |
|  |  |  Lesen / Schreiben / Loeschen         |     |   |
|  |  |  Dateien, Datenbanken, Dienste        |     |   |
|  |  +---------------------------------------+     |   |
|  +-----------------------------------------------+   |
+-----------------------------------------------------+
```

### RBAC in der Praxis

**Beispiel einer Rollenstruktur:**

| Rolle | Zugriff auf | Rechte |
|-------|------------|--------|
| Administrator | Alle Systeme und Daten | Vollzugriff (Lesen, Schreiben, Loeschen, Konfigurieren) |
| Entwickler | Quellcode, Testumgebung | Lesen und Schreiben |
| Buchhalter | Finanzdaten, ERP-System | Lesen und Schreiben nur fuer eigenen Mandanten |
| Praktikant | Dokumentation, Wiki | Nur Lesen |

### Typische Pruefungsaspekte
- Zuordnung: Massnahme zu Zutritt, Zugang oder Zugriff?
- Unterschied technische vs. organisatorische Massnahme benennen
- Berechtigungsmodell (RBAC, DAC, MAC) fuer ein Szenario vorschlagen
- Least-Privilege-Prinzip erklaeren und anwenden

### Haeufige Fehler
- Zutritt und Zugang werden verwechselt → Merke: Zutritt = physisch (Tuer), Zugang = logisch (Login)
- RBAC mit DAC verwechselt: Bei DAC bestimmt der Besitzer die Rechte, bei RBAC werden Rechte ueber Rollen vergeben
- Least Privilege wird vergessen – Nutzer behalten Rechte aus frueheren Abteilungen (Rechteakkumulation)

---

## Uebungen

**Aufgabe 1:** Ordne die folgenden Massnahmen den Kategorien Zutritt, Zugang oder Zugriff zu:
- a) Chipkarte fuer den Serverraum
- b) Passwortpflicht fuer den Firmen-Laptop
- c) NTFS-Berechtigung "Nur Lesen" auf einem Netzlaufwerk
- d) Videoueberwachung am Gebaeudeeingang
- e) VPN-Einwahl mit Zertifikat
- f) Verschluesselung einer Datenbank

**Aufgabe 2:** Erklaere den Unterschied zwischen RBAC und DAC. Nenne jeweils ein Praxisbeispiel.

**Aufgabe 3:** Ein neuer Mitarbeiter beginnt in der Buchhaltung. Beschreibe, welche Schritte beim Anlegen seiner Berechtigungen nach dem RBAC-Modell durchgefuehrt werden.

**Aufgabe 4:** Was bedeutet das Least-Privilege-Prinzip? Nenne ein Beispiel, bei dem dieses Prinzip verletzt wird.

**Aufgabe 5:** Nenne je zwei technische und zwei organisatorische Massnahmen fuer jede der drei Ebenen (Zutritt, Zugang, Zugriff).

---
---

# Loesungen

## Aufgabe 1
- a) **Zutritt** – physischer Zugang zum Serverraum wird kontrolliert
- b) **Zugang** – Anmeldung am System wird geschuetzt
- c) **Zugriff** – Rechte auf Datenebene werden eingeschraenkt
- d) **Zutritt** – physische Ueberwachung des Gebaeudes
- e) **Zugang** – Authentifizierung fuer die Systemnutzung per VPN
- f) **Zugriff** – Schutz der Daten vor unbefugtem Lesen

## Aufgabe 2
- **RBAC:** Rechte werden ueber Rollen vergeben. Beispiel: Alle Mitarbeiter mit der Rolle "Vertrieb" erhalten automatisch Zugriff auf das CRM-System.
- **DAC:** Der Eigentuemer einer Ressource legt fest, wer zugreifen darf. Beispiel: Ein Projektleiter gibt seinen Projektordner fuer bestimmte Kollegen frei (Windows-Freigabe).

## Aufgabe 3
1. Rolle "Buchhalter" ist bereits im System definiert (mit vordefinierten Rechten auf Finanzdaten, ERP-System etc.)
2. Benutzerkonto wird im Active Directory angelegt
3. Dem Benutzerkonto wird die Rolle "Buchhalter" zugewiesen
4. Der Mitarbeiter erhaelt automatisch alle mit der Rolle verknuepften Berechtigungen
5. Keine individuellen Rechte werden vergeben (Least Privilege)

## Aufgabe 4
Das Least-Privilege-Prinzip besagt, dass jeder Benutzer nur die minimal notwendigen Rechte fuer seine aktuelle Aufgabe erhalten soll. Verletzung: Ein Mitarbeiter wechselt von der IT-Abteilung in den Vertrieb, behaelt aber seine Administrator-Rechte. Er hat nun Zugriff auf Systeme, die er nicht mehr benoetigt.

## Aufgabe 5

| Ebene | Technische Massnahme | Organisatorische Massnahme |
|-------|---------------------|---------------------------|
| Zutritt | Chipkartensystem, Videoueberwachung | Besucherregelung, Schliessplan |
| Zugang | Zwei-Faktor-Authentifizierung, biometrischer Scanner | Passwortrichtlinie, Schulung zur Kontosicherheit |
| Zugriff | NTFS-Berechtigungen, Verschluesselung | Berechtigungskonzept, regelmaessige Rezertifizierung |
