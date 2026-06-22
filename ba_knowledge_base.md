# Business Analysis Knowledge Base
## Wissensbasis für die LeadBusinessAnalyst App

> Eigenständig formulierte Zusammenfassung der BA-Grundlagen.
> Quellen: Industry-standard BA-Konzepte (Jeremy Aschenbrenner / TheBAGuide.com, Udemy).
> Erstellt: 2026-06-22

---

## Inhaltsverzeichnis

1. [BA-Grundlagen und Rollenverständnis](#1-ba-grundlagen-und-rollenverständnis)
2. [Der Requirements-Prozess (4 Phasen)](#2-der-requirements-prozess-4-phasen)
3. [Anforderungskategorien](#3-anforderungskategorien)
4. [SMART-Anforderungen](#4-smart-anforderungen)
5. [Anforderungsattribute](#5-anforderungsattribute)
6. [Priorisierung von Anforderungen](#6-priorisierung-von-anforderungen)
7. [Ableitung von Anforderungen (Deriving)](#7-ableitung-von-anforderungen-deriving)
8. [Business Rules vs. Business Requirements](#8-business-rules-vs-business-requirements)
9. [Das Business Requirements Document (BRD)](#9-das-business-requirements-document-brd)
10. [Elicitation-Techniken](#10-elicitation-techniken)
11. [SDLC-Methoden](#11-sdlc-methoden)
12. [BA-Glossar](#12-ba-glossar)
13. [BA Skills Self-Assessment](#13-ba-skills-self-assessment)
14. [Feature-Mapping: App-Features aus der Wissensbasis](#14-feature-mapping-app-features-aus-der-wissensbasis)

---

## 1. BA-Grundlagen und Rollenverständnis

### Was macht ein Business Analyst?

Ein Business Analyst (BA) ist die Brücke zwischen Fachbereichen (Business) und IT/Entwicklung. Kernaufgabe: Bedürfnisse des Unternehmens verstehen, in klare Anforderungen übersetzen und sicherstellen, dass die gelieferte Lösung den tatsächlichen Geschäftsbedarf erfüllt.

**Zentrale Verantwortlichkeiten:**
- Stakeholder identifizieren und mit ihnen kommunizieren
- Geschäftsprozesse dokumentieren und analysieren
- Anforderungen erheben, analysieren, spezifizieren und freigeben lassen
- Als Vermittler zwischen Business und Technik agieren
- Den gesamten Projektlebenszyklus begleiten

**Abgrenzung zu anderen Rollen:**
- **Project Manager:** Plant und überwacht das Projekt (Zeit, Budget, Risiko) — der BA liefert den Inhalt, der PM den Rahmen
- **Product Owner (Scrum):** In agilen Teams oft deckungsgleich oder eng verzahnt mit dem BA
- **System Analyst / Solutions Architect:** Fokus auf technische Umsetzung; BA fokussiert auf Business-Bedarf

### BA im Projektkontext

Der BA startet idealerweise **vor** der Entwicklung und begleitet bis zur Abnahme. Hauptlieferobjekte:
- Business Requirements Document (BRD)
- Use Cases / User Stories
- Prozessdiagramme (AS-IS / TO-BE)
- Testunterstützung (Anforderungen → Akzeptanzkriterien → Testfälle)

---

## 2. Der Requirements-Prozess (4 Phasen)

Der Requirements-Prozess ist ein iterativer Zyklus — in der Praxis durchläuft man ihn mehrfach, selten einmalig linear.

### Phase 1: Elicitation (Erhebung)

Ziel: Anforderungen aus verschiedenen Quellen gewinnen. Nicht nur fragen, was Stakeholder *wollen*, sondern auch was sie *brauchen* — oft sind das zwei verschiedene Dinge.

Typische Quellen:
- Stakeholder-Interviews
- Workshops und Meetings
- Bestehende Dokumentation
- Beobachtung (Job Shadowing)
- Prototypen und Demos

### Phase 2: Analysis (Analyse)

Ziel: Erhobene Rohinformationen in strukturierte, konsistente Anforderungen umwandeln. Konflikte erkennen, Lücken schließen, Duplikate entfernen.

Kernaktivitäten:
- Anforderungen validieren (vollständig? korrekt? umsetzbar?)
- Widersprüche zwischen Stakeholdern auflösen
- Anforderungen kategorisieren und priorisieren
- Business Rules von Requirements trennen

### Phase 3: Specification (Spezifikation)

Ziel: Anforderungen formal und nachvollziehbar dokumentieren. Jede Anforderung muss eindeutig, testbar und rückverfolgbar sein.

Ergebnisse:
- BRD (Business Requirements Document)
- Use Cases / User Stories
- Datenmodelle, Prozessflüsse
- Interface-Beschreibungen

### Phase 4: Approval (Freigabe)

Ziel: Stakeholder bestätigen formell, dass die Anforderungen korrekt und vollständig sind.

Vorgehen:
- Review-Meetings mit Stakeholdern
- Walkthrough der Spezifikation
- Signoff / formelle Freigabe
- Basis für Change-Management (jede spätere Änderung braucht formalen Prozess)

---

## 3. Anforderungskategorien

### Functional Requirements (Funktionale Anforderungen)

Beschreiben **was** ein System tun soll — beobachtbares Verhalten, Aktionen, Berechnungen.

Erkennungsmerkmale:
- Verben wie: berechnen, speichern, anzeigen, senden, validieren
- Direkt testbar (Pass/Fail)
- Beispiel: "Das System muss dem Benutzer ermöglichen, sich per E-Mail und Passwort anzumelden."

### Non-Functional Requirements (Nicht-funktionale Anforderungen)

Beschreiben **wie** ein System sich verhalten soll — Qualitätseigenschaften, die für den Betrieb entscheidend sind.

Kategorien (Auswahl):
| Kategorie | Beschreibung | Beispiel |
|-----------|-------------|---------|
| Performance | Reaktionszeiten, Durchsatz | "Seite lädt in < 2 Sek. bei 1.000 gleichzeitigen Nutzern" |
| Security | Schutz vor unbefugtem Zugriff | "Passwörter werden mit bcrypt (Faktor 12) gespeichert" |
| Usability | Bedienbarkeit, Lernkurve | "Neue Nutzer können Core-Task ohne Schulung in < 5 Min. erledigen" |
| Availability | Betriebsbereitschaft | "System verfügbar 99,9% im Monat (max. 43 Min. Downtime)" |
| Scalability | Skalierbarkeit | "System muss 10x Nutzerwachstum ohne Architekturänderung tragen" |
| Maintainability | Wartbarkeit | "Modulare Architektur, Code-Coverage > 80%" |
| Portability | Plattformunabhängigkeit | "Läuft auf Windows 10+, macOS 12+, Ubuntu 22+" |
| Compliance | Regulatorische Vorgaben | "DSGVO-konform, Datenspeicherung nur in EU" |

### Product Constraints (Produkt-/Projektbeschränkungen)

Randbedingungen, die den Lösungsraum einengen — meist nicht verhandelbar.

Arten:
- **Technische Constraints:** Vorgegebene Technologien, Plattformen, Integrationen
- **Budget-Constraints:** Maximale Investition
- **Zeit-Constraints:** Feste Deadlines (z.B. gesetzliche Fristen)
- **Ressourcen-Constraints:** Verfügbare Teammitglieder, Skillsets
- **Regulatorische Constraints:** Gesetzliche Vorgaben, Industry Standards

---

## 4. SMART-Anforderungen

Jede Anforderung sollte dem SMART-Prinzip genügen, um testbar und umsetzbar zu sein.

| Buchstabe | Begriff | Bedeutung |
|-----------|---------|-----------|
| **S** | Specific | Klar und eindeutig formuliert — kein Interpretationsspielraum |
| **M** | Measurable | Messbar — es gibt konkrete Kriterien, ob die Anforderung erfüllt ist |
| **A** | Attainable | Erreichbar — technisch und wirtschaftlich umsetzbar |
| **R** | Reasonable | Vernünftig/sinnvoll — im Kontext des Projekts und Geschäftsziels relevant |
| **T** | Traceable | Rückverfolgbar — von der Geschäftsanforderung bis zum Test nachvollziehbar |

### Häufige Verstöße gegen SMART

**Nicht spezifisch (vague):**
- Schlecht: "Das System soll schnell sein."
- Besser: "Die Startseite muss bei bis zu 500 gleichzeitigen Nutzern innerhalb von 1,5 Sekunden vollständig geladen sein."

**Nicht messbar:**
- Schlecht: "Benutzer sollen das System einfach bedienen können."
- Besser: "Ein neuer Benutzer muss die Kernfunktion (Bestellung aufgeben) ohne Schulung in maximal 3 Minuten abschließen können."

**Nicht erreichbar:**
- Schlecht: "100% Uptime."
- Besser: "99,95% Verfügbarkeit pro Kalendermonat (entspricht max. 22 Minuten Downtime)."

**Nicht vernünftig:**
- Anforderungen, die nichts mit dem Projektziel zu tun haben oder unverhältnismäßig teuer sind.

**Nicht rückverfolgbar:**
- Anforderungen ohne ID, ohne Herkunftsangabe oder ohne zugehörige Geschäftsanforderung.

### SMART-Prüf-Checkliste

```
[ ] Ist klar, was genau das System tun soll? (Specific)
[ ] Gibt es einen messbaren Akzeptanzwert? (Measurable)
[ ] Ist die Umsetzung technisch/wirtschaftlich möglich? (Attainable)
[ ] Unterstützt die Anforderung ein Geschäftsziel? (Reasonable)
[ ] Hat die Anforderung eine eindeutige ID und Quelle? (Traceable)
```

---

## 5. Anforderungsattribute

Jede dokumentierte Anforderung sollte folgende Attribute besitzen:

| Attribut | Beschreibung | Pflicht? |
|----------|-------------|---------|
| **Unique ID** | Eindeutige Kennung (z.B. FR-001, NFR-003) | Ja |
| **Name / Kurztitel** | Prägnante Bezeichnung | Ja |
| **Beschreibung** | Vollständige Formulierung der Anforderung | Ja |
| **Kategorie** | Functional / Non-Functional / Constraint | Ja |
| **Status** | Proposed → Approved → In Development → Done | Ja |
| **Priorität** | High / Medium / Low (oder MoSCoW) | Ja |
| **Akzeptanzkriterien** | Konkrete Bedingungen für "erfüllt" | Ja |
| **Business Value** | Geschäftswert / Nutzen | Empfohlen |
| **Komplexität** | Simple / Medium / Complex | Empfohlen |
| **Quelle** | Stakeholder oder Dokument, aus dem die Anforderung stammt | Empfohlen |
| **Abhängigkeiten** | IDs anderer Anforderungen, von denen diese abhängt | Empfohlen |
| **Notizen** | Offene Fragen, Annahmen, Kontext | Optional |

### Status-Workflow

```
Proposed → Under Review → Approved → In Development → Testing → Done
                ↓                                         ↓
            Rejected                                  Deferred
```

---

## 6. Priorisierung von Anforderungen

### 3-Schritt-Prozess

**Schritt 1: Business-Nutzen (Business Usefulness)**
- Wie viel Geschäftswert bringt die Anforderung?
- Ist sie notwendig für einen Kern-Geschäftsprozess?
- Beeinflusst sie Umsatz, Compliance, Wettbewerbsposition?

**Schritt 2: Kosten (Cost)**
- Was kostet die Umsetzung (Entwicklung, Infrastruktur, Test)?
- Verhältnis von Nutzen zu Kosten (ROI)?

**Schritt 3: Zeitrahmen (Timeframe)**
- Gibt es externe Deadlines (regulatorisch, vertraglich)?
- Blockiert diese Anforderung andere?
- Wann wird sie tatsächlich benötigt?

**Entscheidungsprinzip:** Business Value hat Vorrang. Eine Anforderung mit hohem Geschäftswert wird auch bei hohen Kosten oder frühem Termin oft priorisiert.

### MoSCoW-Methode

| Kategorie | Bedeutung |
|-----------|-----------|
| **M**ust Have | Nicht verhandelbar — ohne diese ist das Projekt gescheitert |
| **S**hould Have | Wichtig, aber nicht kritisch — kann zur Not verschoben werden |
| **C**ould Have | Wünschenswert — nur wenn Zeit/Budget reicht |
| **W**on't Have | Explizit ausgeschlossen (aus diesem Release) |

---

## 7. Ableitung von Anforderungen (Deriving)

Aus Business-Anforderungen oder Business Rules werden konkrete System-Anforderungen abgeleitet. Dieser Prozess hat 4 Schritte:

### 1. Parsing (Zerlegen)
Die Quellinformation in ihre Bestandteile zerlegen. Eine Business-Anforderung kann mehrere System-Anforderungen enthalten.

### 2. Interpreting (Interpretieren)
Die Intention hinter der Anforderung verstehen. Was möchte der Stakeholder *wirklich* erreichen? Implizite Anforderungen explizit machen.

### 3. Focusing (Fokussieren)
Irrelevante oder redundante Informationen herausfiltern. Den Scope klar abgrenzen: Was ist IN-Scope, was ist OUT-of-Scope?

### 4. Qualifying (Qualifizieren)
Die abgeleiteten Anforderungen SMART-konform formulieren. Ggf. Rückfragen an Stakeholder stellen, um Lücken zu schließen.

---

## 8. Business Rules vs. Business Requirements

Ein häufiger Fehler: Business Rules werden als Anforderungen dokumentiert — das erzeugt Verwirrung.

### Business Rule (Geschäftsregel)

Eine Business Rule ist eine **Unternehmensrichtlinie** — eine Bedingung, die wahr oder falsch ist. Sie existiert unabhängig vom IT-System und beschreibt, wie das Unternehmen operiert.

Erkennungsmerkmale:
- Wenn-Dann-Logik
- Zutreffen oder Nicht-Zutreffen (boolean)
- Gilt auch ohne Software

Beispiele:
- "Ein Kunde, der mehr als 500€ pro Jahr ausgibt, erhält Platinum-Status."
- "Bestellungen über 10.000€ benötigen eine Genehmigung durch einen Manager der Stufe 2."
- "Rückgaben sind nur innerhalb von 30 Tagen nach Kaufdatum möglich."

### Business Requirement (Geschäftsanforderung)

Eine Business Requirement beschreibt, was das **System** tun muss, um die Geschäftsregel zu unterstützen.

**Eine Business Rule erzeugt typischerweise mehrere Requirements:**

Business Rule: "Platinum-Status ab 500€ Jahresumsatz"
→ FR-001: "Das System berechnet den Jahresumsatz eines Kunden zum Monatsende."
→ FR-002: "Das System setzt den Kundenstatus automatisch auf 'Platinum', wenn der Jahresumsatz ≥ 500€."
→ FR-003: "Das System sendet eine Bestätigungs-E-Mail, wenn ein Kunde in den Platinum-Status wechselt."
→ FR-004: "Das System zeigt den aktuellen Status auf der Kundenprofil-Seite an."

### Ablage

Business Rules gehören in ein **Business Rules Repository** (oder eigenen Abschnitt im BRD), nicht in die Requirements-Liste.

---

## 9. Das Business Requirements Document (BRD)

Das BRD ist das zentrale Lieferobjekt des BA — die formelle Dokumentation aller Anforderungen für ein Projekt.

### Typische BRD-Struktur

```
1. Executive Summary
   - Projektzusammenfassung in 1-2 Seiten
   - Business-Ziel und erwarteter Nutzen

2. Projekt-Hintergrund / Business Context
   - Ausgangssituation (AS-IS)
   - Problem oder Chance
   - Scope und Out-of-Scope

3. Stakeholder-Verzeichnis
   - Namen, Rollen, Kontaktdaten
   - Einfluss und Interesse

4. Business Rules
   - Alle relevanten Geschäftsregeln

5. Functional Requirements
   - FR-001, FR-002, ... mit allen Attributen

6. Non-Functional Requirements
   - NFR-001, NFR-002, ... mit allen Attributen

7. Product Constraints
   - PC-001, PC-002, ...

8. Use Cases / User Stories (optional, je nach Methodik)

9. Annahmen und Abhängigkeiten

10. Glossar

11. Anhang (Diagramme, Interviews, etc.)
```

### BRD-Qualitätskriterien

- **Vollständigkeit:** Alle bekannten Anforderungen sind dokumentiert
- **Konsistenz:** Keine widersprüchlichen Anforderungen
- **Klarheit:** Jede Anforderung ist eindeutig interpretierbar
- **Testbarkeit:** Jede Anforderung hat Akzeptanzkriterien
- **Rückverfolgbarkeit:** Jede Anforderung ist auf eine Business-Quelle rückführbar

---

## 10. Elicitation-Techniken

### Übersicht

| Technik | Beste Anwendung | Aufwand | Ergebnis |
|---------|----------------|---------|---------|
| Brainstorming | Neue Ideen, kreative Lösungen | Niedrig | Ideenliste |
| Requirement Workshop | Komplexe, kritische Anforderungen | Hoch | Abgestimmte Requirements |
| Interview | Tiefes Expertenwissen | Mittel | Detaillierte Informationen |
| Survey / Fragebogen | Viele Stakeholder, verteilte Teams | Niedrig-Mittel | Quantitative + qualitative Daten |
| Documentation Review | Bestehende Systeme, Prozesse | Mittel | Baseline, Constraints |
| Interface Analysis | Systemintegrationen | Mittel-Hoch | Interface Requirements |

---

### Technik 1: Brainstorming

**Was es ist:** Strukturierte Kreativitätssitzung zur Generierung möglichst vieler Ideen ohne sofortige Bewertung.

**Typen:**
- *Structured Brainstorming:* Jeder nennt der Reihe nach eine Idee (erzwingt Beteiligung aller)
- *Unstructured Brainstorming:* Freier Austausch (bevorzugt von vielen, kann aber dominante Stimmen begünstigen)
- *Electronic Brainstorming:* Anonyme digitale Eingabe (z.B. über kollaborative Tools) — reduziert sozialen Druck

**Wann einsetzen:**
- Frühphase des Projekts
- Wenn Lösungsraum noch offen ist
- Bei Bedarf an innovativen Ansätzen

**Erfolgsfaktoren:**
- Klare Regeln: Keine Kritik während der Ideenphase
- Zeitbegrenzung (Timeboxing: z.B. 15 Min. für Ideenphase)
- Moderator steuert Prozess, nicht Inhalt
- Alle Ideen festhalten (Whiteboard, digitales Board)
- Erst nach der Sammlung: Bewerten, gruppieren, priorisieren

**Typische Outputs:** Themenliste, geclusterte Ideen, priorisierte Shortlist

---

### Technik 2: Requirement Workshop (JAD Session)

**Was es ist:** Strukturierter Workshop (typisch: 1-3 Tage) mit allen relevanten Stakeholdern zur gemeinsamen Erarbeitung von Anforderungen. Auch bekannt als JAD (Joint Application Development/Design).

**Rollen im Workshop:**
- **Facilitator (Moderator):** Der BA — steuert den Prozess, bleibt neutral zu Inhalten
- **Sponsor/Entscheider:** Löst Konflikte bei Business-Fragen
- **Subject Matter Experts (SMEs):** Fachexperten aus dem Business
- **Technische Vertreter:** IT/Entwicklung (für Machbarkeits-Input)
- **Scribe (Protokollant):** Dokumentiert — entlastet den Facilitator

**Ablauf:**
1. Pre-Workshop: Agenda, Ziele, Teilnehmer, Material vorbereiten
2. Einführung: Ziele und Spielregeln erklären
3. AS-IS analysieren: Aktuellen Zustand verstehen
4. TO-BE definieren: Gewünschten Zustand beschreiben
5. Requirements erarbeiten: Gemeinsam formulieren und abstimmen
6. Review und Konfliktlösung: Widersprüche auflösen
7. Post-Workshop: Dokumentieren, verteilen, Feedback einholen

**Vorteile:**
- Schnell (viele Stakeholder auf einmal)
- Sofortige Klärung von Konflikten
- Höheres Buy-in der Beteiligten

**Nachteile:**
- Kostspielig (Vollzeit mehrerer Stakeholder für Tage)
- Dominante Persönlichkeiten können Ergebnis verzerren
- Logistisch aufwändig (Terminkoordination)

---

### Technik 3: Interview

**Was es ist:** Strukturiertes oder semi-strukturiertes Gespräch mit einzelnen Stakeholdern zur gezielten Informationsgewinnung.

**Interview-Typen:**
- *Structured Interview:* Vorbereitete Fragen, standardisiert (gut für Vergleichbarkeit)
- *Unstructured Interview:* Offenes Gespräch, flexibel (gut für Exploration)
- *Semi-structured Interview:* Mix — Kernfragen vorbereitet, Raum für Nachfragen (empfohlen für BA)

**Vorbereitung:**
- Ziel des Interviews klar definieren
- Interviewpartner und dessen Rolle/Perspektive verstehen
- Offene Fragen formulieren (keine Ja/Nein-Fragen)
- Zeitrahmen festlegen (typisch: 45-90 Min.)

**Interview-Fragenbank (Beispiele nach Themen):**

*Prozessverständnis:*
- "Beschreiben Sie Ihren typischen Arbeitstag bezüglich [Prozess X]."
- "Was passiert, wenn [Ausnahmefall Y] eintritt?"
- "Wo sehen Sie die größten Engpässe im aktuellen Prozess?"

*Anforderungserhebung:*
- "Was funktioniert am aktuellen System gut, was nicht?"
- "Wenn Sie eine Sache ändern könnten — welche wäre das?"
- "Was würde Ihnen Ihren Job wesentlich erleichtern?"

*Prioritäten:*
- "Wenn wir nur X von Y umsetzen könnten — was wäre Ihnen am wichtigsten?"
- "Was muss beim Go-Live funktionieren?"

*Validierung:*
- "Verstehe ich richtig, dass...?" (Paraphrase)
- "Gibt es Fälle, wo das nicht stimmt?"

**Nachbereitung:**
- Mitschriften direkt nach dem Interview reinschreiben
- Zusammenfassung an Interviewpartner schicken zur Bestätigung
- Offene Punkte markieren

---

### Technik 4: Survey / Fragebogen

**Was es ist:** Standardisiertes Befragungsinstrument für viele Stakeholder gleichzeitig.

**Fragetypen:**
- *Closed Questions:* Multiple Choice, Rating-Skala, Ja/Nein — leicht auswertbar
- *Open Questions:* Freitext — reichhaltig, aber aufwändiger auszuwerten
- *Rating/Likert Scale:* "1-5: Wie wichtig ist Ihnen...?" — quantifizierbar

**Wann einsetzen:**
- Viele geografisch verteilte Stakeholder
- Validierung bereits erhobener Anforderungen
- Priorisierungsübung (alle sollen ranken)
- Anonymes Feedback gewünscht

**Design-Prinzipien:**
- Kurz halten (max. 10-15 Minuten Bearbeitungszeit)
- Klare, eindeutige Formulierungen
- Keine Suggestivfragen
- Logischer Aufbau (allgemein → spezifisch)
- Pilottesten vor breitem Versand

**Limitations:**
- Kein Nachfragen möglich
- Rücklaufquote oft niedrig
- Tiefe Einblicke fehlen

---

### Technik 5: Documentation Review

**Was es ist:** Systematische Analyse bestehender Unterlagen zur Gewinnung von Baseline-Informationen.

**Dokumenttypen (Auswahl):**
- Bestehende System-Dokumentation, Handbücher
- Prozessdokumentationen, SOPs
- Frühere Projektunterlagen, BRDs
- Gesetzliche Vorgaben, Normen, Verträge
- Organigramme, Rollenprofile

**Vorgehen:**
1. Relevante Dokumente identifizieren und beschaffen
2. Strukturiert lesen (nicht alles ist relevant)
3. Informationen extrahieren und kategorisieren
4. Lücken und Widersprüche notieren
5. Erkenntnisse in Requirements überführen

**Stärken:**
- Kostengünstig (kein Stakeholder-Aufwand)
- Unverfälscht (Dokumente lügen nicht über Ist-Zustand)
- Gute Basis für Interviews (informierter starten)

**Schwächen:**
- Dokumente können veraltet sein
- Implizites Wissen fehlt
- Zeitaufwändig bei großen Dokumentenmengen

---

### Technik 6: Interface Analysis (Schnittstellenanalyse)

**Was es ist:** Analyse aller Schnittstellen, mit denen das System interagiert — externe Systeme, Benutzer, Hardware, Daten.

**Interface-Typen:**
- **System-zu-System:** APIs, Dateiaustausch, Datenbanken
- **Mensch-zu-System (UI):** Bildschirme, Formulare, Berichte
- **System-zu-Hardware:** Drucker, Scanner, Sensoren

**Analyse-Vorgehen:**
1. Alle beteiligten Systeme/Nutzer/Hardware identifizieren (Context Diagram)
2. Für jede Schnittstelle: Was fließt rein? Was fließt raus? Wann? Wie oft?
3. Format, Protokoll, Datenstruktur klären
4. Fehlerszenarien und Fallbacks definieren

**Interface-Requirements-Template:**
```
Interface ID: IF-001
Von: System A
Zu: System B
Daten: [Was wird übertragen?]
Format: [JSON / XML / CSV / etc.]
Frequenz: [Real-time / Batch täglich um 02:00 / etc.]
Fehlerbehandlung: [Retry / Alert / Logging]
```

---

## 11. SDLC-Methoden

Der Software Development Life Cycle (SDLC) beschreibt den Prozess von der Idee bis zur produktiven Software. Es gibt mehrere Modelle — jedes mit eigenen Stärken und Schwächen.

### Übersicht

| Modell | Planung | Flexibilität | Kundenkontakt | Einsatzbereich |
|--------|---------|-------------|---------------|----------------|
| Waterfall | Hoch (upfront) | Niedrig | Wenig | Klare, stabile Anforderungen |
| Incremental | Mittel | Mittel | Mittel | Phasenweise Lieferung gewünscht |
| Spiral | Sehr hoch | Mittel | Mittel | Hohes Risiko, große Projekte |
| Scrum/Agile | Niedrig (iterativ) | Sehr hoch | Sehr viel | Sich ändernde Anforderungen |
| RAD | Niedrig | Hoch | Viel | Schnelle Prototypen, UI-intensiv |
| Prototyping | Mittel | Hoch | Viel | Unklare Anforderungen |

---

### Modell 1: Waterfall (Wasserfall)

**Beschreibung:** Streng sequenzielles Modell — jede Phase muss abgeschlossen sein, bevor die nächste beginnt. Keine Rückwärtsiterationen vorgesehen.

**Phasen:**
```
Requirements → Design → Implementation → Testing → Deployment → Maintenance
```

**Vorteile:**
- Klare Struktur und Dokumentation
- Einfach zu managen (Meilensteine, Deliverables)
- Gut für Projekte mit gesetzlichen Compliance-Anforderungen
- Kostenpläne und Zeitpläne zuverlässig schätzbar

**Nachteile:**
- Kein Spielraum für veränderte Anforderungen
- Fehler in frühen Phasen werden erst spät entdeckt
- Kunde sieht keine lauffähige Software bis zum Ende
- "Big Bang" Delivery — hohes Risiko

**Wann einsetzen:**
- Anforderungen sind vollständig bekannt und werden sich nicht ändern
- Regulatorisch vorgeschrieben (Militär, Luft/Raumfahrt, medizinische Geräte)
- Kurze Projekte mit klarer Abgrenzung

---

### Modell 2: Incremental (Inkrementell)

**Beschreibung:** Das System wird in Teillieferungen (Inkremente/Releases) entwickelt. Jedes Inkrement fügt Funktionalität hinzu.

**Struktur:**
```
Core Release → Increment 1 → Increment 2 → ... → Full System
```

**Vorteile:**
- Frühe Lieferung von Kernfunktionen
- Feedback nach jedem Inkrement möglich
- Risiko verteilt über mehrere Lieferungen
- Nutzer können frühzeitig mit dem System arbeiten

**Nachteile:**
- Integration späterer Inkremente kann komplex sein
- Gesamtarchitektur muss von Anfang an solide sein
- Jedes Inkrement braucht vollständigen Test-Zyklus

**Wann einsetzen:**
- Bekannte Anforderungen, aber phasenweise Lieferung gewünscht
- Teile des Systems werden früher benötigt als andere
- Budget wird in Tranchen freigegeben

---

### Modell 3: Spiral

**Beschreibung:** Iteratives Modell mit explizitem Risikomanagement. Jede "Spiralrunde" durchläuft: Ziele setzen → Risiken analysieren → Entwickeln/Testen → Planen des nächsten Zyklus.

**4 Quadranten pro Iteration:**
1. Ziele, Alternativen, Einschränkungen definieren
2. Risiken evaluieren und minimieren
3. Entwickeln und testen
4. Nächste Iteration planen

**Vorteile:**
- Explizites Risikomanagement eingebaut
- Anpassungen pro Iteration möglich
- Gut für große, komplexe Systeme

**Nachteile:**
- Sehr hoher Management-Aufwand
- Schwer zu schätzen (Kosten, Zeit)
- Nicht geeignet für kleine Projekte

**Wann einsetzen:**
- Hohes technisches oder geschäftliches Risiko
- Große, mehrjährige Projekte
- Anforderungen entwickeln sich parallel zur Technologie

---

### Modell 4: Scrum / Agile

**Beschreibung:** Iterative, inkrementelle Entwicklung in kurzen Zyklen (Sprints, typisch 2 Wochen). Fokus auf Zusammenarbeit, Anpassungsfähigkeit und kontinuierliche Lieferung.

**3 Rollen:**
| Rolle | Verantwortung |
|-------|--------------|
| **Product Owner (PO)** | Priorisiert das Product Backlog, repräsentiert Business-Interessen |
| **Scrum Master** | Beseitigt Hindernisse, sichert Scrum-Prozess (kein PM!) |
| **Development Team** | Selbstorganisiertes Team, liefert das Inkrement |

**Artefakte:**
- **Product Backlog:** Priorisierte Liste aller gewünschten Features/Anforderungen (User Stories)
- **Sprint Backlog:** Subset des Product Backlogs — was in diesem Sprint umgesetzt wird
- **Increment:** Die fertige, potenziell auslieferbare Software am Sprint-Ende

**5 Scrum-Events:**
| Event | Zweck | Dauer |
|-------|-------|-------|
| Sprint Planning | Was und wie wird im Sprint gemacht? | Max. 8h für 4-Wochen-Sprint |
| Daily Scrum / Standup | Tägliche Synchronisation (Was gestern? Was heute? Blocker?) | 15 Min. |
| Sprint Review | Demo des Increments an Stakeholder | Max. 4h |
| Sprint Retrospective | Prozessverbesserung im Team | Max. 3h |
| Backlog Refinement | Stories schärfen, schätzen, priorisieren | Laufend (ca. 10% der Sprint-Zeit) |

**User Story Format:**
```
Als [Rolle]
möchte ich [Funktionalität]
damit [Nutzen/Ziel]

Akzeptanzkriterien:
- [ ] ...
- [ ] ...
```

**Definition of Done (DoD):** Team-Vereinbarung, wann eine Story als "fertig" gilt (z.B. Code reviewed, Tests grün, Dokumentation aktualisiert, in Produktion deploybar).

**Vorteile:**
- Maximale Flexibilität bei sich ändernden Anforderungen
- Frühe und häufige Lieferung von Wert
- Enge Kundenzusammenarbeit
- Transparenz durch kurze Feedbackzyklen

**Nachteile:**
- Schwer zu skalieren (große Teams → Frameworks wie SAFe nötig)
- Erfordert hohe Kundenverfügbarkeit
- Scope-Creep-Risiko ohne starken PO
- Kostenplanung schwieriger

**Wann einsetzen:**
- Anforderungen unklar oder sich häufig ändernd
- Innovationsprojekte, neue Produktentwicklung
- Kleines bis mittelgroßes Team (3-9 Personen)
- Kunde kann regelmäßig Feedback geben

---

### Modell 5: RAD (Rapid Application Development)

**Beschreibung:** Fokus auf schnelle Lieferung durch intensive Nutzung von Prototypen und visuellen Entwicklungstools. Weniger Planung upfront, dafür mehr Iteration mit Nutzern.

**Phasen:**
```
Requirements Planning → User Design → Construction → Cutover
```

**Charakteristika:**
- Timeboxing (fester Zeitrahmen, flexibler Scope)
- Intensive Nutzereinbindung während "User Design"
- Verwendung von Low-Code/Prototyping-Tools
- Wiederverwendung bestehender Komponenten

**Vorteile:**
- Sehr schnelle Lieferung (Wochen statt Monate)
- Hohe Nutzerzufriedenheit (Nutzer sehen und formen Lösung)
- Fehler werden früh sichtbar

**Nachteile:**
- Schlecht skalierbar für große Systeme
- Technik-Schulden bei schlechter Architektur
- Anforderungen müssen relativ klar sein
- Erfordert erfahrene Entwickler

**Wann einsetzen:**
- Klare Business-Ziele, aber flexible Anforderungen
- System mit vielen UI-Interaktionen
- Enger Zeitrahmen

---

### Modell 6: Prototyping

**Beschreibung:** Vor der eigentlichen Entwicklung wird ein vereinfachtes Modell (Prototyp) erstellt, um Anforderungen zu klären und Feedback zu sammeln.

**Typen:**
- *Throwaway Prototyping:* Prototyp wird nach dem Feedback weggeworfen — sauberere Entwicklung
- *Evolutionary Prototyping:* Prototyp wird schrittweise zur echten Lösung ausgebaut
- *Horizontal Prototyping:* Zeigt die Breite (alle Screens), aber keine Tiefe (kein Backend)
- *Vertical Prototyping:* Zeigt die Tiefe eines Features (inkl. Backend), aber nicht alle Screens

**Vorteile:**
- Anforderungen werden durch Ausprobieren klar
- Reduktion von Missverständnissen
- Frühe Nutzerbeteiligung

**Nachteile:**
- Stakeholder verwechseln Prototyp mit finalem Produkt
- Scope-Creep durch "solange wir dabei sind..."
- Kann teuer werden, wenn schlecht gemanagt

**Wann einsetzen:**
- Anforderungen sehr unklar
- Neuartige Technologie oder unbekannte Nutzerbedürfnisse
- UI/UX-kritische Systeme

---

## 12. BA-Glossar

Wichtige Begriffe im Business Analysis Umfeld:

| Begriff | Definition |
|---------|-----------|
| **Acceptance Criteria** | Konkrete, messbare Bedingungen, die eine Anforderung erfüllen muss, um als "done" zu gelten |
| **Assumption** | Annahme, die als wahr gilt, aber noch nicht bestätigt ist |
| **Baseline** | Festgelegter, freigegebener Stand einer Anforderung oder eines Dokuments — Ausgangspunkt für Änderungen |
| **Business Case** | Dokumentation des geschäftlichen Nutzens und der Rechtfertigung eines Projekts |
| **Business Rule** | Richtlinie, die beschreibt, wie das Unternehmen in einer bestimmten Situation handelt (true/false) |
| **Change Request** | Formeller Antrag zur Änderung einer freigegebenen Anforderung oder eines Deliverables |
| **Constraint** | Beschränkung, die den Lösungsraum einengt (technisch, zeitlich, budgetär, regulatorisch) |
| **Deliverable** | Konkretes, lieferbares Ergebnis eines Projekts oder einer Projektphase |
| **Dependency** | Abhängigkeit zwischen Anforderungen oder Aufgaben — A kann nicht ohne B |
| **Elicitation** | Prozess der Informationsgewinnung von Stakeholdern und anderen Quellen |
| **Feasibility** | Machbarkeit — technische, finanzielle und organisatorische Durchführbarkeit |
| **Functional Requirement** | Anforderung, die beschreibt, was ein System tun soll (beobachtbares Verhalten) |
| **Gap Analysis** | Vergleich des IST-Zustands mit dem SOLL-Zustand zur Identifikation von Lücken |
| **In Scope** | Explizit im Projektumfang enthalten |
| **Issue** | Identifiziertes Problem, das gelöst werden muss |
| **Iteration** | Zeitlich begrenzter Entwicklungszyklus (synonym zu Sprint in Scrum) |
| **MoSCoW** | Priorisierungsmethode: Must / Should / Could / Won't Have |
| **NFR** | Non-Functional Requirement — Qualitätseigenschaften eines Systems |
| **Out of Scope** | Explizit vom Projekt ausgeschlossen |
| **Prioritization** | Prozess zur Festlegung der Reihenfolge von Anforderungen nach Geschäftswert |
| **Requirement** | Beschreibung einer Fähigkeit oder Bedingung, die ein System erfüllen muss |
| **Risk** | Potenzielle zukünftige Ereignisse, die das Projekt negativ beeinflussen könnten |
| **Scope Creep** | Schleichende, unkontrollierte Ausweitung des Projektumfangs |
| **Signoff** | Formelle Freigabe/Genehmigung durch autorisierte Stakeholder |
| **SME** | Subject Matter Expert — Fachexperte für einen Bereich |
| **Stakeholder** | Person oder Gruppe, die Einfluss auf oder Interesse am Projekt hat |
| **Traceability** | Rückverfolgbarkeit — Verbindung von Anforderungen zu Quellen, Tests und Deliverables |
| **Traceability Matrix** | Tabelle, die Anforderungen mit Quellen und Tests verknüpft |
| **Use Case** | Beschreibung einer Interaktion zwischen Nutzer/System und dem zu entwickelnden System |
| **User Story** | Agiles Format: "Als [Rolle] möchte ich [Feature] damit [Nutzen]" |
| **Validation** | Prüfung, ob das richtige Produkt gebaut wird (Kundenbedarf erfüllt?) |
| **Verification** | Prüfung, ob das Produkt richtig gebaut wird (Spezifikation erfüllt?) |
| **Wireframe** | Grafischer Entwurf einer Benutzeroberfläche (ohne Design/Styling) |

---

## 13. BA Skills Self-Assessment

Ein BA benötigt Kompetenzen in mehreren Dimensionen. Das folgende Framework ermöglicht eine strukturierte Selbstbewertung.

### Kompetenz-Dimensionen

#### 1. Analytical Skills (Analytische Fähigkeiten)
- Fähigkeit, komplexe Probleme zu zerlegen und zu verstehen
- Datenanalyse und Interpretation
- Mustererkennung in Prozessen
- Gap-Analyse und Ursachenforschung

*Indikatoren für hohe Kompetenz:*
- Findet Widersprüche in Anforderungen eigenständig
- Stellt die richtigen Fragen, bevor Annahmen getroffen werden
- Unterscheidet Symptome von Ursachen

#### 2. Communication Skills (Kommunikation)
- Schriftlich: Klar, präzise, zielgruppengerecht
- Mündlich: Überzeugend, aktives Zuhören
- Visuell: Diagramme, Prozessflüsse, Wireframes

*Indikatoren:*
- Kann technische Konzepte nicht-technischen Stakeholdern erklären
- Passt Kommunikationsstil an Zielgruppe an
- Fasst Meetings klar zusammen

#### 3. Elicitation Skills (Erhebungskompetenz)
- Beherrschung verschiedener Elicitation-Techniken
- Interviewführung
- Workshop-Moderation
- Umgang mit schwierigen Stakeholdern

*Indikatoren:*
- Wählt die richtige Technik für den Kontext
- Erkennt implizite Anforderungen hinter expliziten Aussagen
- Stellt offene Fragen statt geschlossene

#### 4. Documentation Skills (Dokumentation)
- BRD-Erstellung
- Use Cases, User Stories
- Prozessdiagramme (BPMN, Flussdiagramme)
- Qualitätsstandards für Anforderungen

*Indikatoren:*
- Dokumente sind klar strukturiert und vollständig
- Anforderungen sind SMART formuliert
- Konsistente Terminologie und Attributierung

#### 5. Technical Understanding (Technisches Verständnis)
- Grundverständnis von Softwarearchitektur
- Datenbankgrundlagen (SQL-Grundkenntnisse)
- API/Integration-Konzepte
- SDLC-Methoden und Tools

*Indikatoren:*
- Kann mit Entwicklern auf Augenhöhe kommunizieren
- Versteht technische Einschränkungen
- Erkennt unrealistische technische Anforderungen

#### 6. Stakeholder Management
- Stakeholder identifizieren und kartieren
- Erwartungen managen
- Konflikte moderieren
- Politisches Bewusstsein

*Indikatoren:*
- Weiß, wer Entscheidungsträger ist vs. wer Einfluss hat
- Eskaliert richtig — nicht zu früh, nicht zu spät
- Baut Vertrauen bei Stakeholdern auf

#### 7. Business Domain Knowledge
- Verständnis des Geschäftsumfelds
- Branchenkenntnisse
- Prozessverständnis (Finanzen, HR, Supply Chain etc.)

*Indikatoren:*
- Versteht den Kontext hinter Anforderungen
- Erkennt Business Rules implizit
- Kennt regulatorische Rahmenbedingungen

### Self-Assessment-Skala

```
1 — Keine Erfahrung (theoretical knowledge only)
2 — Anfänger (mit starker Unterstützung arbeitsfähig)
3 — Fortgeschrittener Anfänger (eigenständig mit gelegentlicher Unterstützung)
4 — Kompetent (eigenständig in den meisten Situationen)
5 — Erfahren (Mentor für andere, führt eigenständig komplexe Projekte)
```

### Entwicklungspfad

Priorität für BA-Einsteiger:
1. Communication Skills (Kommunikation ist das Fundament)
2. Elicitation Skills (Techniken lernen und üben)
3. Documentation Skills (SMART Requirements, BRD-Struktur)
4. Analytical Skills (mit Erfahrung wächst das automatisch)
5. Technical Understanding (Grundlagen reichen für viele BA-Rollen)
6. Stakeholder Management (kommt mit Projekterfahrung)
7. Business Domain Knowledge (projektspezifisch aufbauen)

---

## 14. Feature-Mapping: App-Features aus der Wissensbasis

Dieses Kapitel leitet aus der Wissensbasis konkrete Features für die `LeadBusinessAnalyst` Python-App ab.

### Feature-Übersicht

| Feature | Wissensbasis-Quelle | Priorität | Beschreibung |
|---------|-------------------|-----------|-------------|
| SMART-Checker | Kap. 4 | HIGH | Anforderung eingeben → automatisch auf SMART prüfen |
| Requirements-Editor | Kap. 3, 5 | HIGH | Anforderungen mit allen Attributen erstellen/bearbeiten |
| Elicitation-Assistent | Kap. 10 | HIGH | Technikauswahl + Fragebank für Interviews |
| SDLC-Empfehlung | Kap. 11 | MEDIUM | Projektparameter → passende Methode empfehlen |
| Business Rules Manager | Kap. 8 | MEDIUM | Rules erfassen → Requirements ableiten |
| BRD-Generator | Kap. 9 | MEDIUM | Aus Daten ein BRD-Dokument generieren |
| Prioritäts-Wizard | Kap. 6 | MEDIUM | 3-Schritt-Priorisierung mit Scoring |
| Glossar & Nachschlagewerk | Kap. 12 | LOW | Integriertes BA-Glossar |
| Skills Self-Assessment | Kap. 13 | LOW | Interaktive Kompetenzbewertung |
| Traceability Matrix | Kap. 5 | LOW | Anforderungen ↔ Tests ↔ Business Goals verknüpfen |

---

### Feature 1: SMART-Checker

**Was:** Der Nutzer gibt eine Anforderung als Freitext ein. Die App analysiert sie und gibt Feedback, ob/wie gut sie dem SMART-Kriterium entspricht.

**Logik:**

```python
# Dimension: Specific
# → Prüfe: Ist das Subjekt klar? Gibt es ein Verb? Ist die Aktion eindeutig?
# Schlecht: Signalwörter für Vagheit: "schnell", "einfach", "benutzerfreundlich", "gut", "angemessen"

# Dimension: Measurable
# → Prüfe: Enthält die Anforderung messbare Werte (Zahlen, Zeitangaben, Prozentwerte)?
# Gut: Zahlen, Einheiten, Zeitangaben
# Schlecht: Keine quantifizierbaren Elemente

# Dimension: Attainable
# → Prüfe: Enthält die Anforderung physisch unmögliche Ziele?
# Schlecht: "100% Uptime", "0 Fehler", "sofortige Antwortzeit"

# Dimension: Reasonable
# → Kann nur durch Kontext bewertet werden (Projektbezug)

# Dimension: Traceable
# → Prüfe: Hat die Anforderung eine ID? Gibt es eine Quelle?
```

**UI-Konzept:**
- Textfeld für Anforderungseingabe
- 5 Ampel-Symbole (Grün/Gelb/Rot) für jede SMART-Dimension
- Konkrete Verbesserungsvorschläge per Dimension
- Vorher/Nachher-Vergleich

---

### Feature 2: Requirements-Editor

**Was:** Vollständiger Editor für einzelne Anforderungen mit allen Pflicht- und optionalen Attributen.

**Datenmodell:**

```python
@dataclass
class Requirement:
    id: str                    # FR-001, NFR-003
    title: str
    description: str
    category: RequirementCategory  # FUNCTIONAL / NON_FUNCTIONAL / CONSTRAINT
    status: RequirementStatus  # PROPOSED / UNDER_REVIEW / APPROVED / ...
    priority: Priority         # HIGH / MEDIUM / LOW / MUST / SHOULD / COULD / WONT
    acceptance_criteria: list[str]
    business_value: str
    complexity: Complexity     # SIMPLE / MEDIUM / COMPLEX
    source: str
    dependencies: list[str]    # IDs anderer Requirements
    notes: str
    created_at: datetime
    updated_at: datetime
```

**Features des Editors:**
- Formulareingabe mit Validierung
- SMART-Check als integrierten Schritt
- Import/Export (JSON, CSV, Markdown)
- Requirements-Liste mit Filter und Suche
- Status-Workflow-Anzeige

---

### Feature 3: Elicitation-Assistent

**Was:** Guided Workflow zur Auswahl der richtigen Elicitation-Technik + Generierung situationsspezifischer Interview-Fragen.

**Technikauswahl-Logik:**

```python
TECHNIQUE_SELECTOR = {
    # Bedingungen → Empfohlene Technik
    ("many_stakeholders", "distributed"): "Survey",
    ("complex_requirements", "conflict_resolution_needed"): "Workshop",
    ("deep_expert_knowledge", "few_stakeholders"): "Interview",
    ("existing_system", "documentation_heavy"): "Documentation Review",
    ("system_integration", "api_heavy"): "Interface Analysis",
    ("early_stage", "creative_phase"): "Brainstorming",
}
```

**Fragenbank-Struktur:**

```json
{
  "interview_questions": {
    "process_understanding": [
      "Describe your typical workday related to [process].",
      "What happens when [exception case] occurs?",
      "Where do you see the biggest bottlenecks in the current process?"
    ],
    "requirements_discovery": [
      "What works well in the current system, and what doesn't?",
      "If you could change one thing, what would it be?",
      "What would make your job significantly easier?"
    ],
    "prioritization": [
      "If we could only implement X out of Y features, which would matter most?",
      "What must work at go-live?"
    ],
    "validation": [
      "Do I understand correctly that...?",
      "Are there cases where this doesn't apply?"
    ]
  }
}
```

---

### Feature 4: SDLC-Empfehlung

**Was:** Fragebogen über Projektcharakteristika → App empfiehlt die passende SDLC-Methode mit Begründung.

**Entscheidungsparameter:**

```python
SDLC_DECISION_FACTORS = {
    "requirements_clarity": ["very_clear", "mostly_clear", "unclear", "unknown"],
    "expected_changes": ["none", "few", "moderate", "frequent"],
    "team_size": ["small_1_5", "medium_6_15", "large_16_plus"],
    "customer_availability": ["high", "medium", "low"],
    "risk_level": ["low", "medium", "high"],
    "time_constraint": ["fixed_deadline", "flexible", "asap"],
    "compliance_required": [True, False],
}
```

**Empfehlungs-Matrix:**
- Klare Anforderungen + kein Wandel + Compliance → Waterfall
- Unklar + häufig ändernd + Kunde verfügbar → Scrum
- Hohes Risiko + groß → Spiral
- Schnelle Lieferung + UI-intensiv → RAD
- Sehr unklar + neue Technologie → Prototyping

---

### Feature 5: Business Rules Manager

**Was:** Separate Verwaltung von Business Rules mit automatischer Ableitung von System-Requirements.

**Datenmodell:**

```python
@dataclass
class BusinessRule:
    id: str                    # BR-001
    description: str           # Die Regel in natürlicher Sprache
    condition: str             # IF-Teil
    consequence: str           # THEN-Teil
    derived_requirements: list[str]  # IDs der abgeleiteten Requirements
    source: str                # Dokument / Stakeholder
    effective_date: date
    review_date: date
```

**Ableitungs-Workflow:**
1. Rule erfassen
2. Bedingung und Konsequenz strukturieren
3. System generiert Vorschläge für abzuleitende Requirements
4. BA bearbeitet und bestätigt die Requirements
5. Automatische Verknüpfung BR ↔ Requirements

---

### Feature 6: BRD-Generator

**Was:** Aus den erfassten Daten (Requirements, Rules, Stakeholder) wird ein strukturiertes BRD-Dokument generiert.

**Output-Formate:** Markdown, Word (via python-docx), PDF (via reportlab/weasyprint)

**BRD-Template-Sections:**
1. Executive Summary (auto-generiert aus Projektmetadaten)
2. Background & Context (Freitext-Eingabe)
3. Stakeholder Register (aus Stakeholder-Liste)
4. Business Rules (aus BR-Manager)
5. Functional Requirements (gefiltert + formatiert)
6. Non-Functional Requirements (gefiltert + formatiert)
7. Constraints (gefiltert + formatiert)
8. Assumptions & Dependencies (Freitext)
9. Glossar (aus integriertem Glossar)

---

### Feature 7: Prioritäts-Wizard

**Was:** Interaktiver 3-Schritt-Wizard zur Priorisierung von Requirements (Business Value → Cost → Timeframe).

**Scoring-Logik:**

```python
def calculate_priority_score(
    business_value: int,   # 1-10
    cost_inverse: int,     # 10 = niedrige Kosten, 1 = sehr hohe Kosten
    urgency: int,          # 1-10
    weights: dict = {"business_value": 0.5, "cost": 0.3, "urgency": 0.2}
) -> float:
    return (
        business_value * weights["business_value"] +
        cost_inverse * weights["cost"] +
        urgency * weights["urgency"]
    )
```

**Output:** Sortierte Requirements-Liste mit Scores + MoSCoW-Klassifizierung

---

### Feature 8: Glossar & Nachschlagewerk

**Was:** Integriertes, durchsuchbares BA-Glossar mit 30+ Definitionen + kontextsensitive Hilfe im Editor.

**Zusatzfunktionen:**
- Suchfunktion (Fuzzy-Search)
- Verlinkung von Begriffen im Editor (Hover → Definition)
- Nutzer kann eigene Begriffe hinzufügen
- Export als Glossar-Anhang für BRD

---

### Feature 9: Skills Self-Assessment

**Was:** Interaktives Assessment der 7 BA-Kompetenz-Dimensionen mit Radar-Chart-Visualisierung und Entwicklungsempfehlungen.

**Dimensionen:** Analytical, Communication, Elicitation, Documentation, Technical, Stakeholder Management, Domain Knowledge

**Output:**
- Radar-Chart (matplotlib / plotly)
- Stärken/Schwächen-Analyse
- Priorisierte Lernempfehlungen (basierend auf Entwicklungspfad aus Kap. 13)
- Speicherbar für Verlauf (Progress Tracking über Zeit)

---

### Feature 10: Traceability Matrix

**Was:** Visualisierung der Rückverfolgbarkeit: Business Goals ↔ Requirements ↔ Test Cases.

**Datenstruktur:**

```python
@dataclass
class TraceabilityEntry:
    requirement_id: str
    business_goal: str
    test_cases: list[str]
    status: str
    verified: bool
```

**Output:** Interaktive Tabelle + exportierbar als CSV/Excel

---

## Anhang: Schnellreferenz-Karten

### Anforderungs-Kategorien auf einen Blick

```
FUNCTIONAL (Was tut das System?)
  → Das System MUSS / SOLL / KANN [Verb + Objekt + Bedingung]
  → Testbar mit Pass/Fail

NON-FUNCTIONAL (Wie tut das System es?)
  → Performance, Security, Usability, Availability, Scalability,
    Maintainability, Portability, Compliance

CONSTRAINT (Was schränkt die Lösung ein?)
  → Technologie, Budget, Zeit, Regulatorik, Ressourcen
```

### SMART-Schnellcheck

```
S: Ist klar WAS, WER, WANN, WIE VIEL?
M: Gibt es eine messbare Zahl / ein Kriterium?
A: Ist das physisch möglich? (kein "100%", kein "instant")
R: Warum braucht das Projekt das?
T: Hat es eine ID und eine Quelle?
```

### Elicitation-Technik-Wahl

```
Viele Stakeholder, verteilt? → Survey
Konflikte, kritische Requirements? → Workshop
Tiefes Expertenwissen? → Interview
Bestehendes System? → Documentation Review
APIs / Integrationen? → Interface Analysis
Frühe Phase, kreativ? → Brainstorming
```

### SDLC-Schnellwahl

```
Klare Requirements, Compliance? → Waterfall
Sich ändernde Requirements, Kundeneinbindung? → Scrum
Hohes Risiko, großes Projekt? → Spiral
Phasenweise Lieferung? → Incremental
Sehr schnell, UI-intensiv? → RAD
Requirements sehr unklar? → Prototyping
```
