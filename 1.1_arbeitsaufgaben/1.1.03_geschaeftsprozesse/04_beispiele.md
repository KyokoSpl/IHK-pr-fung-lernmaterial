# Beispiele: 1.1.03 – Arbeitsaufgaben im Rahmen von Geschaefts- und Leistungsprozessen

## Bearbeitungsstatus / Ticketsystem

**Beispiel 1:** Ein Mitarbeiter meldet, dass sein E-Mail-Programm nicht startet. Im Ticketsystem wird ein Ticket erstellt: Ticket-ID #4521, Prioritaet: Mittel, Status: Neu. Der 1st-Level-Support weist es sich zu (Status: In Bearbeitung), prueft die Installation und behebt den Fehler durch Neuinstallation (Status: Geloest). Nach Bestaetigung durch den Mitarbeiter wird das Ticket geschlossen.

**Beispiel 2:** Ein Server zeigt erhoehte Auslastung. Das Monitoring-System erstellt automatisch ein Ticket mit Prioritaet: Hoch. Der 1st-Level-Support erkennt, dass er das Problem nicht loesen kann, und eskaliert an den 2nd-Level (Status: Eskaliert). Der 2nd-Level identifiziert einen fehlerhaften Dienst, beendet ihn und dokumentiert die Loesung.

---

## Fehlermanagement

**Beispiel 1:** Nutzer melden, dass die interne Webanwendung sporadisch langsam laedt. Der Support erstellt einen Fehlerbericht: Beschreibung (Anwendung laedt > 10 Sekunden), Haeufigkeit (3-5 Mal taeglich), Betroffene (alle Nutzer). Root Cause Analysis ergibt: Die Datenbankanfragen sind nicht optimiert. Workaround: Server-Cache aktivieren. Fix: SQL-Abfragen optimieren (Eintrag ins Product Backlog).

**Beispiel 2:** Nach einem Update startet eine Buchhaltungssoftware nicht mehr. Schweregrad: Kritisch (geschaeftskritische Anwendung). Workaround: Rollback auf vorherige Version. Root Cause: Inkompatibilitaet mit aktueller Java-Version. Dauerloesung: Hersteller stellt angepasstes Update bereit.

---

## KI-Unterstuetzung

**Beispiel 1:** Ein Chatbot beantwortet Standardanfragen im IT-Support: "Wie aendere ich mein Passwort?" Der Bot liefert eine Schritt-fuer-Schritt-Anleitung. Nur wenn der Nutzer nicht weiterkommt, wird ein Ticket fuer den menschlichen Support erstellt. Ergebnis: 40% weniger Tickets im 1st-Level.

**Beispiel 2:** Ein KI-gestuetztes Monitoring-System erkennt, dass die Festplattenbelegung eines Servers seit 3 Wochen linear steigt. Es berechnet, dass in 10 Tagen der Speicher voll ist, und erstellt automatisch ein Ticket mit Empfehlung: "Alte Logdateien bereinigen oder Speicher erweitern." → Predictive Maintenance.

---

## Kundenkommunikation

**Beispiel 1 – Statusmeldung:**
"Guten Tag Herr Mueller, zu Ihrem Ticket #3892 (Drucker druckt nicht): Wir haben festgestellt, dass ein Treiberupdate erforderlich ist. Dieses wird morgen bis 10:00 Uhr installiert. Ihr Drucker wird danach wieder verfuegbar sein. Bei Fragen erreichen Sie uns unter der bekannten Supportnummer."
→ Sachlich, verstaendlich, mit Zeitangabe.

**Beispiel 2 – Deeskalation:** Ein Kunde beschwert sich: "Seit zwei Tagen funktioniert mein Internet nicht und niemand hilft mir!" Antwort: "Ich verstehe, dass das sehr aergerlich ist. Ich schaue mir den Status sofort an. Bitte geben Sie mir 5 Minuten, dann informiere ich Sie ueber das weitere Vorgehen."
→ Verstaendnis zeigen, konkrete Zusage machen.

---

## Stoerungs-Management

**Beispiel 1:** Der E-Mail-Server ist seit 8:00 Uhr nicht erreichbar. Einstufung: Major Incident. Ablauf: 1) Stoerung wird vom Monitoring erkannt und automatisch gemeldet. 2) 1st-Level erstellt Ticket, Prioritaet: Kritisch. 3) Sofortige Eskalation an 2nd-Level. 4) Diagnose: Festplatte voll → alte Logs belegen 98% des Speichers. 5) Workaround: Logs manuell loeschen, Server neu starten. 6) Dauerloesung: Automatische Log-Rotation einrichten. 7) Ticket wird dokumentiert und geschlossen.

**Beispiel 2:** Mehrere Mitarbeiter melden, dass der WLAN-Zugang im 2. OG nicht funktioniert. 1st-Level prueft: Access Point ist offline. Massnahme: Neustart des Access Points per Remote-Zugriff. WLAN funktioniert wieder. Dokumentation im Ticket: Ursache unklar, Einzelfall. Bei wiederholtem Auftreten → Eskalation an 2nd-Level zur näheren Analyse.

---

## Support- und Serviceanfragen

**Beispiel 1 – First-Level:** Ein Mitarbeiter ruft an: "Ich kann mich nicht einloggen." Der 1st-Level-Support prueft: Account gesperrt nach 3 Fehlversuchen. Massnahme: Passwort zuruecksetzen, Nutzer informieren. → Problem im 1st-Level geloest.

**Beispiel 2 – Second-Level:** Der 1st-Level konnte ein Druckerproblem nicht loesen (Drucker ist im Netzwerk nicht sichtbar). Eskalation an 2nd-Level. Der Spezialist prueft: IP-Konfiguration des Druckers ist falsch, Subnetz stimmt nicht ueberein. Massnahme: IP-Adresse korrigieren, Drucker ist wieder erreichbar.

**Beispiel 3 – Third-Level:** Ein ERP-System zeigt nach einem Update Berechnungsfehler bei der Rechnungsstellung. 2nd-Level kann den Fehler eingrenzen, aber nicht beheben. Eskalation an den Softwarehersteller (3rd-Level). Der Hersteller analysiert den Quellcode und liefert einen Patch.
