# Business Analysis Knowledge Base
## Wissensbasis für die LeadBusinessAnalyst App

> Eigenständig formulierte Zusammenfassung der BA-Grundlagen.
> Quellen: Industry-standard BA-Konzepte (Jeremy Aschenbrenner / TheBAGuide.com, Udemy).
> Erstellt: 2026-06-22 · Erweitert: 2026-06-22 (Business Case, Use Cases, detailliertes BRD-Template, BA Key Skills)

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
13. [BA Skills Self-Assessment & BA Key Skills](#13-ba-skills-self-assessment--ba-key-skills)
14. [Der Business Case](#14-der-business-case)
15. [Use-Case-Spezifikation](#15-use-case-spezifikation)
16. [Feature-Mapping: App-Features aus der Wissensbasis](#16-feature-mapping-app-features-aus-der-wissensbasis)

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

### SMART-Checklist im Detail (Fragen + Leitlinien)

Diese Matrix dient als Grundlage für den automatisierten SMART-Checker (siehe Feature-Mapping).

| Kriterium | Beschreibung | Prüffragen | Leitlinien |
|-----------|-------------|-----------|-----------|
| **Specific** | Klar, konsistent, einfach; nicht mehrdeutig | Was? Warum? Wer? Wo? | Vage Wörter wie "einige", "viele", "mehrere" vermeiden · Werte mit Labels versehen · Bilder/Visualisierungen nutzen |
| **Measurable** | Fortschritt zum Ziel messbar, Indikatoren quantifizierbar | Wie viel? Wie viele? Woran erkenne ich, dass es erreicht ist? | Messbarkeit bereits bei der Erhebung sicherstellen · Tests zur Verifikation definieren · Eindeutigen Erfolg validieren und belegen |
| **Attainable** | Anforderung ist machbar/erreichbar | Gibt es eine theoretische Lösung? Wurde es schon einmal gemacht? Sind die Constraints bekannt? | Ausreichend Zeit, Ressourcen, Budget sicherstellen · Genügend Wissen/Erfahrung validieren · Komponenten und Learnings aus früheren Projekten wiederverwenden |
| **Reasonable** | Aufwand lohnt sich; positiver Return on Investment | Ist es lohnenswert? Stimmt das Timing? Passt es zu unseren Zielen und Bedürfnissen? | Jede Anforderung einem Sanity-Check unterziehen · Sicherstellen, dass die Anforderung im Kontext sinnvoll ist |
| **Traceable** | Anforderung vom Ursprung über Design bis in die Umsetzung verfolgbar | Wie kann ich verifizieren, dass die Anforderung berücksichtigt wurde? Habe ich die wichtigen Daten dazu erfasst? | Erfassen: Originator (Quelle), Assumptions, Business-Begründung, Dependencies, Importance |

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

### Detailliertes BRD-Template (Praxisstandard)

Ein professionelles BRD enthält mehr als nur die Anforderungsliste. Vollständige Struktur:

```
TITELSEITE
  - Projektnummer, Projektname
  - Version (N.N), Datum (YYYY-MM-DD)

VERSION & APPROVALS
  - Version History (Version# | Datum | Revised By | Reason for change)
  - Approval-Statement: Dieses Dokument wurde als offizielles BRD
    genehmigt. Nach Freigabe werden Änderungen über den Change-
    Management-Prozess gesteuert (Impact-Analyse, Reviews, Approvals).
  - Document Approvals (Approver Name | Project Role | Signature | Datum)

1. PROJECT DETAILS
   - Project Name, Project Type (z.B. New Initiative / Phase II)
   - Start Date, End Date, Project Sponsor
   - Primary Driver (z.B. Mandatory / Efficiency), Secondary Driver
   - Division, Project Manager

2. OVERVIEW
   Dieses Dokument dient als Basis für:
   - Erstellung von Lösungsdesigns
   - Entwicklung von Testplänen, -skripten und -fällen
   - Bestimmung des Projektabschlusses
   - Bewertung des Projekterfolgs

3. DOCUMENT RESOURCES (Stakeholder Map)
   - Name | Business Unit | Role
   - Alle an der Anforderungserhebung beteiligten Personen

4. GLOSSARY OF TERMS
   - Term/Acronym | Definition

5. PROJECT OVERVIEW
   5.1 Overview & Background (Vision Statement — jede Anforderung
       bringt das Projekt näher an diese Vision)
   5.2 Project Dependencies (verwandte/abhängige Projekte)
   5.3 Stakeholders (interne + externe)

6. KEY ASSUMPTIONS & CONSTRAINTS
   - Assumptions (Annahmen, auf denen die Anforderungen basieren)
   - Constraints (Beschränkungen)

7. (OPTIONAL) USE CASES
   - Use Case Diagram (UML)
   - Use Case Narratives (siehe Kap. 15)

8. BUSINESS REQUIREMENTS (nach Kategorien gegliedert)
   - General / Base
   - Security
   - Reporting
   - Usability
   - Audit
   Spalten je Anforderung: REQ# | PRIORITY | DESCRIPTION | RATIONALE | USE CASE

APPENDICES
   - Appendix A: Business Process Flows (AS-IS / TO-BE Diagramme)
   - Appendix B: Business Rules Catalog
   - Appendix C: Models
```

### Prioritäts-Rating-Schema (BRD-Standard)

Im BRD werden Anforderungen mit einem 5-stufigen Rating priorisiert:

| Wert | Rating | Beschreibung |
|------|--------|-------------|
| 1 | **Critical** | Kritisch für den Projekterfolg. Ohne diese Anforderung ist das Projekt nicht möglich. |
| 2 | **High** | Hohe Priorität, aber das Projekt kann als Minimalversion ohne sie umgesetzt werden. |
| 3 | **Medium** | Einigermaßen wichtig — bringt Mehrwert, aber das Projekt kann ohne sie fortfahren. |
| 4 | **Low** | Niedrige Priorität, "nice to have", falls Zeit und Budget es zulassen. |
| 5 | **Future** | Out of Scope für dieses Projekt, für ein mögliches künftiges Release notiert. |

### Anforderungs-Tabellenzeile (Beispiel)

| REQ# | PRIORITY | DESCRIPTION | RATIONALE | USE CASE |
|------|----------|-------------|-----------|----------|
| GEN-01 | 1 (Critical) | Das System muss bis zu 100 gleichzeitige Nutzer unterstützen. | Daten zeigen Spitzen von 45 gleichzeitigen Nutzern; Puffer für Wachstum nötig. | UC-3 |

> Anders als die SMART-Attributliste in Kap. 5 ist dies das **kompakte BRD-Tabellenformat**: Jede Anforderung trägt eine ID, eine Priorität (1-5), die Beschreibung, eine **Rationale** (Begründung — wichtig für Traceability) und eine Verknüpfung zum Use Case.

### Business Rules Catalog (Appendix-Template)

Jede Business Rule wird im BRD-Anhang nach diesem Schema dokumentiert:

```
Business Rule Name:  Aussagekräftiger Name zum Thema der Regel
Identifier:          Eindeutige ID, z.B. BR1
Description:         Die Regel im Detail
                     Beispiel: "Alle Arbeitsleistungen werden in
                     15-Minuten-Schritten erfasst, gemeldet und abgerechnet."
Example:             (optional) Ein Beispiel für die Regel
Source:              Quelle der Regel, z.B. Stakeholder
Related Rules:       Liste verwandter Regeln (für Traceability)
```

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

> **Vollständiges Glossar:** Die Datei `glossary.json` enthält alle **351 BA-Fachbegriffe** mit vollständigen englischen Definitionen — direkt für die App-Glossar-Funktion nutzbar.
> Dieses Kapitel enthält eine kuratierte Auswahl der wichtigsten ~80 Begriffe auf Deutsch.

### Kern-Begriffe (Requirements & Analysis)

| Begriff | Definition |
|---------|-----------|
| **Acceptance Criteria** | Konkrete, messbare Bedingungen, die eine Anforderung erfüllen muss, um als "done" zu gelten |
| **Analysis** | Erstellung eines problemunabhängigen Modells — Analysis fokussiert auf das *Was*, Design auf das *Wie* |
| **Assumption** | Annahme, die als wahr gilt, aber noch nicht bestätigt wurde |
| **Baseline** | Vereinbarter, freigegebener Stand eines Dokuments/einer Anforderung — Ausgangspunkt für Änderungen |
| **Business Goal** | Zustand oder Bedingung, den das Unternehmen erfüllen muss, um seine Vision zu erreichen |
| **Business Needs** | Übergeordnete Geschäftsanforderungen — Aussagen über Geschäftsziele oder gewünschte Auswirkungen |
| **Business Requirement** | Übergeordnete geschäftliche Begründung, die, wenn adressiert, Umsatz steigert, Kosten senkt, Service verbessert oder regulatorische Anforderungen erfüllt |
| **Business Rule** | Richtlinie, die beschreibt, wie das Unternehmen in einer Situation handelt (true/false-Constraint) |
| **Constraint** | Beschränkung, die den Lösungsraum einengt (technisch, zeitlich, budgetär, regulatorisch) |
| **Deliverable** | Eindeutiges, nachweisbares Arbeitsergebnis oder Lieferobjekt |
| **Dependency** | Abhängigkeit zwischen Anforderungen oder Aufgaben |
| **Desired Outcome** | Geschäftlicher Nutzen, der durch Erfüllung des Business Needs entsteht; angestrebter Endzustand |
| **Elicitation** | Prozess der Informationsgewinnung: Technikauswahl → Durchführung → Dokumentation → Bestätigung |
| **Feature** | Kohärentes Bündel extern sichtbarer Funktionalität, das auf Geschäftsziele einzahlt |
| **Functional Requirement** | Beschreibt, was ein System tun soll (beobachtbares Verhalten) |
| **Gap Analysis** | Vergleich IST- vs. SOLL-Zustand zur Identifikation von Lücken |
| **Non-Functional Requirement** | Qualitätseigenschaften eines Systems (Usability, Performance, Security, Scalability …) |
| **Prioritization** | Prozess zur Festlegung der relativen Wichtigkeit von Anforderungen |
| **Requirement** | Beschreibung einer Fähigkeit oder Bedingung, die ein System erfüllen muss |
| **Requirement Attribute** | Datenelement mit festgelegtem Typ, das eine Anforderung beschreibt (ID, Status, Priorität …) |
| **Requirements Traceability** | Fähigkeit, Anforderungen zu ihrem Ursprung, durch das Design und in die Umsetzung zu verfolgen |
| **Requirements Traceability Matrix** | Tabelle, die Anforderungen mit Quellen, Use Cases und Tests verknüpft |
| **Scope** | Gesamtheit der Arbeit und Lieferobjekte, die für ein Projekt benötigt werden |
| **Scope Creep** | Schleichende, unkontrollierte Ausweitung des Projektumfangs |
| **Signoff** | Formelle Freigabe/Genehmigung durch autorisierte Stakeholder |
| **Solution Requirement** | Anforderung, die Fähigkeiten beschreibt, die eine Lösung haben muss — funktional oder nicht-funktional |
| **Stated Requirements** | Anforderungen, wie der Stakeholder sie ausdrückt (nicht zwingend was er wirklich braucht) |
| **Transition Requirements** | Beschreiben Fähigkeiten, die temporär benötigt werden, um vom IST- zum SOLL-Zustand zu gelangen |
| **Validation** | Prüfung, ob das *richtige* Produkt gebaut wird (erfüllt es den Kundenbedarf?) |
| **Verification** | Prüfung, ob das Produkt *richtig* gebaut wird (erfüllt es die Spezifikation?) |

### Stakeholder & Rollen

| Begriff | Definition |
|---------|-----------|
| **Actor** | Menschliche und nicht-menschliche Rollen, die mit einem System interagieren |
| **Change Control Board (CCB)** | Kleine Stakeholder-Gruppe, die über Disposition und Behandlung von Anforderungsänderungen entscheidet |
| **Domain Subject Matter Expert (SME)** | Person mit spezifischer Expertise im untersuchten Fachbereich |
| **End User** | Person oder System, das direkt mit der Lösung interagiert |
| **Primary Actor** | Akteur, der Use Cases initiiert und die Systemunterstützung benötigt |
| **Product Owner** | Verantwortlich für die Priorisierung des Product Backlogs; repräsentiert Business-Interessen |
| **Project Sponsor** | Genehmigt und finanziert das Projekt |
| **Scrum Master** | Beseitigt Hindernisse, sichert den Scrum-Prozess (kein Projektmanager) |
| **SME** | Subject Matter Expert — Fachexperte für einen Bereich |
| **Stakeholder** | Person oder Gruppe, die Einfluss auf oder Interesse am Projekt hat |
| **Stakeholder Analysis** | Identifikation aller Stakeholder und ihrer Interessen, Einflüsse und Erwartungen |

### Prozess & Methoden

| Begriff | Definition |
|---------|-----------|
| **Agile** | Sammelbegriff für leichtgewichtige Methodiken (Scrum, Kanban, XP, RAD) mit iterativer Entwicklung, kurzen Zyklen und direkter Kundenbeteiligung |
| **Backlog Grooming** | Review des Product Backlogs: richtige Items, ausreichend Detail, korrekte Priorisierung |
| **BPMN** | Business Process Modeling Notation — standardisierte Notation für Prozessdiagramme |
| **Change-driven Methodology** | Methodik mit Fokus auf schnelle inkrementelle Lieferung und direktes Stakeholder-Feedback |
| **Daily Standup** | 15-Min.-Meeting: Was gestern? Was heute? Blocker? |
| **Definition of Done** | Team-vereinbartes Kriterium, wann eine User Story als fertig gilt |
| **Definition of Ready** | Kriterien, die eine User Story erfüllen muss, um bearbeitet werden zu können |
| **Incremental Delivery** | Lauffähige Software in mehreren Releases liefern — Produkt wird schrittweise ausgeliefert |
| **Iteration** | Zeitlich begrenzter Entwicklungszyklus (synonym zu Sprint in Scrum) |
| **JAD (Joint Application Development)** | Anforderungsworkshop-Methodik mit Stakeholdern, SMEs, Endnutzern, BAs und Entwicklern |
| **Kanban** | Agiles Framework mit visuellen Statussignalen (Kanban-Board: To Do / In Progress / Done) |
| **Minimum Viable Product (MVP)** | Erste Lieferung mit genug Funktionalität, um Wert zu liefern — wird danach schrittweise erweitert |
| **Plan-driven Methodology** | Methodik mit starkem Fokus auf Planung und formale Dokumentation |
| **Sprint** | Zeitlich begrenzter Entwicklungszyklus in Scrum (typisch 2 Wochen) |
| **Sprint Planning** | Meeting zu Beginn eines Sprints: Was wird gemacht und wie? |
| **Sprint Retrospective** | Meeting am Sprint-Ende zur Prozessverbesserung im Team |
| **Sprint Review** | Demo des Increments an Stakeholder am Sprint-Ende |
| **Timebox** | Festes Zeitfenster für eine Aktivität — Scope wird angepasst, nicht die Zeit |

### Analyse-Techniken & Modelle

| Begriff | Definition |
|---------|-----------|
| **Activity Diagram** | UML-Diagramm zur Modellierung von Prozessabläufen mit Swim Lanes |
| **Brainstorming** | Gruppenaktivität zur Generierung vieler Ideen ohne sofortige Bewertung |
| **Burndown Chart** | Verfolgt verbleibende Arbeit über Zeit — zeigt Fortschritt im Sprint |
| **Burn-Up Chart** | Verfolgt abgeschlossene Arbeit vs. Gesamtumfang — zeigt Scope-Änderungen |
| **Context Diagram** | Sonderform des DFD — zeigt das gesamte System als einen Prozess und seine externen Schnittstellen |
| **Cost-Benefit Analysis** | Technik zur Feststellung, ob der finanzielle Nutzen die Projektkosten überwiegt |
| **CRUD** | Create, Read, Update, Delete — die vier Grundoperationen auf persistenten Daten |
| **Data Flow Diagram (DFD)** | Modelliert ein System als Netzwerk funktionaler Prozesse und Datenflüsse |
| **Decision Tables** | Tabellarisches Modell zur kompakten Darstellung komplexer Business Rules und Logik |
| **Decision Tree** | Grafische Darstellung von Entscheidungspunkten mit Verzweigungen und Wahrscheinlichkeiten |
| **Entity Relationship Diagram (ERD)** | Modelliert Beziehungen zwischen Datenbankentitäten (Rechtecke=Entities, Rauten=Relationships) |
| **Feasibility Study** | Bewertung von Alternativen auf technische Machbarkeit und Nutzen |
| **Fishbone Diagram** | Problem-Analyse-Tool (Ursache-Wirkung-Diagramm) — auch Ishikawa-Diagramm |
| **Focus Group** | Elicitation-Methode: Ideen und Einstellungen in interaktiver Gruppe erheben |
| **Force Field Analysis** | Grafische Gegenüberstellung von Kräften, die eine Änderung unterstützen vs. blockieren |
| **Gantt Chart** | Projektplanungs-Tool: Aufgaben, Abhängigkeiten, Ressourcen und Timing |
| **Observation** | Anforderungserhebung durch direktes Beobachten der Arbeitsumgebung des Stakeholders |
| **Pareto Chart** | Absteigende Balkendiagramm — zeigt welche Probleme den größten Verbesserungseffekt haben |
| **PDCA Method** | Plan-Do-Check-Act — 4-Schritt-Methode für kontinuierliche Prozessverbesserung |
| **RACI Matrix** | Verantwortlichkeitsmatrix: Responsible / Accountable / Consulted / Informed |
| **Root Cause Analysis** | Systematische Identifikation der Grundursache eines Problems (nicht nur Symptombehandlung) |
| **SWOT Analysis** | Strengths / Weaknesses / Opportunities / Threats — strategische Analysemethode |
| **UML** | Unified Modeling Language — standardisierte Notation für Software-Diagramme |
| **Use Case Diagram** | UML-Diagramm, das Akteure und ihre Interaktionen mit dem System zeigt |
| **Voice of the Customer (VOC)** | Systematische Methode zur Erfassung von Kundenbedürfnissen und -erwartungen |
| **Wireframe** | Grafischer Low-Fidelity-Entwurf einer Benutzeroberfläche (ohne Styling) |

### Prototyping-Typen

| Begriff | Definition |
|---------|-----------|
| **Evolutionary Prototype** | Prototyp, der kontinuierlich auf Basis von Nutzerfeedback weiterentwickelt wird bis zur finalen Lösung |
| **Exploratory Prototype** | Prototyp zur Erkundung oder Verifikation von Anforderungen |
| **Horizontal Prototype** | Zeigt die Breite (alle Screens), aber keine Tiefe (kein Backend) |
| **Throwaway Prototype** | Prototyp wird nach dem Feedback verworfen — sauberere Neuentwicklung folgt |
| **Vertical Prototype** | Zeigt die Tiefe eines Features (inkl. Backend), aber nicht alle Screens |

### Finanzkennzahlen & Kennzahlen

| Begriff | Definition |
|---------|-----------|
| **Discount Rate** | Prozentsatz zur Abzinsung zukünftiger Cashflows auf den heutigen Wert |
| **KPI (Key Performance Indicator)** | Messgröße zur Steuerung eines Prozesses oder Services — nur die wichtigsten Metriken |
| **Net Present Value (NPV)** | Barwert aller zukünftigen Cashflows abzüglich Investition — berücksichtigt Zeitwert des Geldes |
| **Return on Investment (ROI)** | Prozentuales Verhältnis von Netto-Gewinn zu Investitionskosten |
| **Team Velocity** | Durchschnittliche Menge an Arbeit, die ein Team pro Sprint liefert (in Story Points) |

### Qualität & Governance

| Begriff | Definition |
|---------|-----------|
| **Change Request** | Formeller Antrag zur Änderung einer freigegebenen Anforderung oder eines Deliverables |
| **Impact Analysis** | Bewertet die Auswirkungen einer geplanten Änderung auf Stakeholder, Projekt oder System |
| **Issue** | Identifiziertes Problem, das gelöst werden muss |
| **Lessons Learned** | Reflexionsprozess nach einem Projekt/Sprint: Was lief gut? Was nicht? Was ändern wir? |
| **Milestone** | Endpunkt einer Phase — markiert Abschluss eines Work Packages oder wichtiger Deliverables |
| **Organizational Readiness Assessment** | Bewertet, ob Stakeholder bereit sind, die mit einer Lösung verbundene Veränderung zu akzeptieren |
| **Peer Review** | Validierungstechnik: kleine Gruppe bewertet einen Teil eines Arbeitsergebnisses auf Fehler |
| **Risk** | Potenzielle zukünftige Ereignisse, die das Projekt negativ beeinflussen könnten |
| **Risk Management** | Systematischer Prozess zur Identifikation, Analyse und Minderung von Risiken |
| **Signoff** | Formelle Freigabe/Genehmigung durch autorisierte Stakeholder |
| **User Acceptance Testing (UAT)** | Testen durch echte Endnutzer zur Validierung, dass die Lösung Business-Anforderungen erfüllt |
| **Work Breakdown Structure (WBS)** | Hierarchische Zerlegung aller Projektarbeiten in manageable Arbeitspakete |

---

## 13. BA Skills Self-Assessment & BA Key Skills

Ein BA benötigt Kompetenzen in mehreren Dimensionen. Das folgende Framework ermöglicht eine strukturierte Selbstbewertung.

### Die 6 Kern-Skills eines Business Analysts

| Skill | Bedeutung |
|-------|-----------|
| **Communication** | Schriftliche und mündliche Kommunikation sind essenziell. Der BA ist im Kern ein professioneller Kommunikator, der die Lücke zwischen Business- und Technik-Teams überbrückt. |
| **Negotiation** | Nicht alle Stakeholder sind einer Meinung. Der BA verhandelt zwischen den Positionen und führt sie zu einer einvernehmlichen Lösung. |
| **Problem Solving** | Kein Projekt ist ohne Probleme. Der BA definiert das Problem und erarbeitet mögliche Lösungen. |
| **Facilitation** | Meetings sind fester Bestandteil der Unternehmenskultur. Der BA muss Diskussionen angemessen moderieren, in Meetings präsentieren und Telefonkonferenzen effektiv leiten können. |
| **Organization** | Der BA muss organisiert sein und referenzierbare Notizen aus verschiedenen Meetings und Gesprächen führen. |
| **Critical Thinking** | Der BA muss viele Optionen analysieren und sicherstellen, dass die finale Lösung alle Stakeholder-Bedürfnisse und Anforderungen erfüllt. |

### Weitere wertvolle Skills

Viele BA-Rollen nutzen zusätzlich:

- **Decision-making:** Informationen nutzen, um nach Abwägung mehrerer Alternativen entschlossen zu entscheiden
- **Technical aptitude:** Hohe Vertrautheit mit verschiedenen Technologien und die Fähigkeit, neue Software schnell zu erlernen
- **Documentation:** Klare, präzise Dokumentation schreiben, die exakt wiedergibt, was besprochen oder gelernt wurde
- **Visual modeling:** Komplexe Gedanken und Prozesse visuell in Diagrammen und Modellen darstellen (Prozessflüsse, Wireframes, Use Cases)
- **Relationship-building:** Starke, positive Beziehungen zu Menschen auf allen Ebenen der Organisation aufbauen und pflegen (Nutzer, Manager, Führungskräfte)
- **Self-managing:** Aufgaben, Projekte und Deadlines eigenständig und proaktiv managen — das Richtige tun, auch wenn niemand zusieht
- **Thick skin** (kein Skill im engeren Sinn, aber wichtig): Feedback annehmen können, ohne defensiv zu werden oder es persönlich zu nehmen

> Die folgenden 7 Assessment-Dimensionen sind eine analytische Gruppierung dieser Skills für die strukturierte Selbstbewertung.

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

### Die 12 Skills des Self-Assessment (aus dem Excel-Tool)

Das offizielle Self-Assessment-Tool bewertet genau diese 12 Skills:

| # | Skill | Kategorie |
|---|-------|-----------|
| 1 | **Oral Communication** | Kommunikation |
| 2 | **Written Communication** | Kommunikation |
| 3 | **Problem Solving** | Analytisch |
| 4 | **Critical Thinking** | Analytisch |
| 5 | **Negotiation** | Stakeholder |
| 6 | **Decision-Making** | Analytisch |
| 7 | **Facilitation** | Kommunikation |
| 8 | **Technical Aptitude** | Technisch |
| 9 | **Documentation** | Dokumentation |
| 10 | **Visual Modeling** | Dokumentation |
| 11 | **Relationship-Building** | Stakeholder |
| 12 | **Self-Managing** | Persönlich |

### Self-Assessment-Skala (4-stufig)

Das Tool verwendet eine 4-Punkte-Skala — bewusst ohne Mittelkategorie, um eine klare Einschätzung zu erzwingen:

| Rating | Bedeutung |
|--------|-----------|
| **Very Poor** | Kaum vorhanden — großer Entwicklungsbedarf |
| **Poor** | Schwach — Verbesserung notwendig |
| **Good** | Solide — funktioniert in den meisten Situationen |
| **Very Good** | Stark — Stärke, die aktiv eingesetzt werden kann |

### Zwei-Track-Auswertung

Nach der Bewertung werden die Skills in zwei Tracks aufgeteilt:

**Track 1 — Leverageable Skills (Good + Very Good):**
- Diese Skills in die "Leverageable Skills"-Liste übertragen
- Für jeden Skill: Konkrete Erfahrungen mit positivem Ergebnis sammeln (Brainstorming)
- Ziel: Bewusstsein schaffen, wie diese Stärken strategisch eingesetzt werden können

**Track 2 — Skills to Improve (Poor + Very Poor):**
- Diese Skills in die "Skills to Improve"-Liste übertragen
- Für jeden Skill: Aktuelle und zukünftige Verbesserungswege erarbeiten
- Ziel: Gezielte Entwicklungsmaßnahmen ableiten (Training, Mentoring, Praxisprojekte)

### Entwicklungspfad (empfohlene Reihenfolge für BA-Einsteiger)

1. **Oral + Written Communication** — Fundament; ohne Kommunikation keine Wirkung
2. **Facilitation** — Workshops und Meetings früh lernen
3. **Documentation** — SMART Requirements, BRD-Struktur
4. **Problem Solving + Critical Thinking** — wächst mit Erfahrung, aber gezielt fördern
5. **Technical Aptitude** — Grundlagen reichen für viele BA-Rollen
6. **Negotiation + Relationship-Building** — kommt mit Projekterfahrung
7. **Decision-Making + Self-Managing** — Persönliche Reife und Eigenverantwortung
8. **Visual Modeling** — Diagramme, BPMN, Wireframes — projektspezifisch aufbauen

---

## 14. Der Business Case

Der Business Case ist das Dokument, das **vor** Projektstart die geschäftliche Rechtfertigung liefert: Warum sollte das Unternehmen Geld und Zeit investieren? Er beantwortet die Frage "Lohnt sich dieses Projekt?" mit Zahlen und Fakten und dient dem Management als Entscheidungsgrundlage (Go / No-Go).

### Struktur eines Business Case

| Abschnitt | Inhalt |
|-----------|--------|
| **1. Executive Summary** | Kurze Zusammenfassung des gesamten Business Case: Problem, Synopse der Analyse, empfohlene Lösung. Wird in der Regel **zuletzt** geschrieben, da sie die anderen Abschnitte verdichtet. |
| **2. Problem Statement** | Klare, prägnante Beschreibung der Chance oder des Problems, das adressiert wird. |
| **3. Analysis** | Beschreibt das Was, Warum und Wie des potenziellen Projekts. Definiert das Problem/die Chance vollständig und wie es entstanden ist. Erklärt, was passiert, wenn nichts getan wird. Beschreibt benötigte Ressourcen, Budget und Zeitrahmen. |
| **4. Solution Options** | Auflistung der untersuchten Top-Lösungen mit Kurzbeschreibung sowie Pros und Cons jeder Option. **Eine Option muss immer "Nichts tun" (Do Nothing) sein.** |
| **5. Cost-Benefit Analysis** | Bewertet Kosten und Nutzen jeder Lösungsoption. Enthält den erwarteten finanziellen Nutzen und den Zeitrahmen bis zum Return on Investment. Kann mit "Solution Options" kombiniert werden. |
| **6. Recommendation** | Begründet die Empfehlung und wie sie zustande kam. Dieser Abschnitt "verkauft" das Projekt. Kann Hinweise zur Durchführung enthalten (Methodik, Ressourcen, Zeitrahmen). |

### Finanzkennzahlen der Cost-Benefit-Analyse

| Kennzahl | Bedeutung |
|----------|-----------|
| **Payback Period** | Zeitraum (in Jahren), bis die Investition durch Einsparungen/Erträge wieder eingespielt ist. |
| **ROI (Return on Investment)** | Prozentuales Verhältnis von Netto-Gewinn zu Investitionskosten. |
| **NPV (Net Present Value)** | Barwert aller zukünftigen Cashflows abzüglich der Investition — berücksichtigt den Zeitwert des Geldes. |

### Praxisbeispiel: Doughlicious Pastry (Liefer-Tracking)

Ein durchgängiges Beispiel zeigt, wie ein Business Case argumentiert:

**Problem:** Eine Bäckerei verlor über 6 Monate ~22.000 $ Umsatz; Kundenzufriedenheit sank von 4,7 auf 4,2 (von 5). Über 75 % der unzufriedenen Kunden nannten den neuen Lieferprozess als Ursache (38 % verspätet, 31 % nie angekommen, 27 % falsche Rechnung).

**Root Cause:** Ein manueller, undokumentierter Lieferprozess (Zettel werden ausgedruckt, handschriftlich ergänzt, an eine Pinnwand geheftet) — fehleranfällig, nicht nachverfolgbar, keine Reports.

**Lösungsoptionen (jeweils mit Pros/Cons):**
1. *Do Nothing* — geschätzter Verlust 40.000 $+ pro Jahr; Firma in 7 Jahren unprofitabel.
2. *Bestehendes System modifizieren* — Eigenentwicklung über Contractor; löst die meisten Probleme, aber 6-8 Monate, hohe Vorabkosten.
3. *Off-the-shelf Delivery Tracking Software (SaaS)* — in 1-2 Monaten einsatzbereit, niedrige Vorabkosten, kostenlose Updates; aber Doppelerfassung, laufende Lizenzkosten.
4. *Lieferprozess entfernen* — würde Kunden zur Konkurrenz treiben (14 % im Jahr 1, 22 % im Jahr 2); in 2 Jahren unprofitabel.

**Cost-Benefit (Auszug):**
- Option 2: Payback 3,16 Jahre · ROI 39,49 % · NPV 48.390 $
- Option 3: Payback 3,27 Jahre · ROI 87 %+ · NPV 52.361 $

**Empfehlung:** Option 3 (SaaS-Lösung) — niedrigste Anfangsinvestition (15.760 $, wichtig bei knappem Cashflow), geringeres Risiko (fertig getestet), schnelle Implementierung, in-house wartbar, automatische Feature-Upgrades.

**Lehre aus dem Beispiel:** Ein überzeugender Business Case verknüpft das Problem mit *quantifizierten* Auswirkungen, stellt mehrere Optionen (inkl. "Nichts tun") gegenüber, untermauert sie mit Finanzkennzahlen und leitet daraus eine klar begründete Empfehlung ab — passend zur konkreten Situation (hier: Cashflow-Knappheit als ausschlaggebendes Kriterium).

---

## 15. Use-Case-Spezifikation

Ein Use Case erfasst das benötigte Systemverhalten aus Sicht des Endnutzers beim Erreichen eines oder mehrerer Ziele. Er beschreibt den Ablauf der Interaktion zwischen Akteuren und dem System und kann zusätzlich visuell (UML-Use-Case-Diagramm) dargestellt werden.

### Use-Case-Narrative — Template

| Feld | Definition |
|------|-----------|
| **Use Case ID** | Eindeutige numerische ID in hierarchischer Form (X.Y). Verwandte Use Cases lassen sich gruppieren. Funktionale Anforderungen können auf einen Use Case zurückverfolgt werden. |
| **Use Case Name** | Prägnanter, ergebnisorientierter Name. Spiegelt die Aufgabe wider, die der Nutzer erledigen will. Enthält Verb + Nomen (z.B. "Bestellung aufgeben", "Kampus-Karte ansehen"). |
| **Created By / Date Created** | Ersteller und Erstellungsdatum. |
| **Last Updated By / Date Last Updated** | Letzte Änderung und Datum. |
| **Actors** | Person oder externe Entität, die mit dem System interagiert und Use Cases ausführt. Verschiedene Akteure entsprechen oft verschiedenen Nutzerrollen. |
| **Description** | Kurze Beschreibung von Grund und Ergebnis des Use Case bzw. High-Level-Ablauf. |
| **Preconditions** | Bedingungen, die vor Start erfüllt sein müssen (nummeriert). Beispiel: "Nutzeridentität ist authentifiziert." |
| **Postconditions** | Zustand des Systems nach Ausführung (nummeriert). Beispiel: "Preis in der Datenbank wurde aktualisiert." |
| **Normal Course** | Detaillierter Ablauf der Nutzeraktionen und Systemantworten unter normalen Bedingungen. Als nummerierte Liste (Aktion des Akteurs ↔ Antwort des Systems). |
| **Alternative Courses** | Andere legitime Nutzungsszenarien. Nummerierung mit Use-Case-ID als Präfix + "AC" (z.B. X.Y.AC.1). |
| **Exceptions** | Erwartete Fehlerzustände und Systemreaktion. Nummerierung mit "EX" (z.B. X.Y.EX.1). |
| **Includes** | Andere Use Cases, die von diesem aufgerufen ("included") werden. Gemeinsame Funktionalität wird ausgelagert. |
| **Priority** | Relative Priorität der Umsetzung — gleiches Schema wie im BRD (1-5). |
| **Frequency of Use** | Geschätzte Häufigkeit der Ausführung pro Zeiteinheit. |
| **Business Rules** | Business Rules, die diesen Use Case beeinflussen. |
| **Special Requirements** | Zusätzliche (oft nicht-funktionale) Anforderungen, z.B. Performance, Verfügbarkeit. |
| **Assumptions** | Annahmen, die zur Aufnahme dieses Use Case führten. |
| **Notes and Issues** | Offene Punkte/TBDs mit Verantwortlichem, Fälligkeit und Auflösung. |

### Beispiel: ausgefüllter Use Case

```
Use Case ID:        1
Use Case Name:      Interaktive Kampus-Karte ansehen
Actors:             User
Description:        Beschreibt die Hauptnutzung der interaktiven Kampus-
                    Karte als Web-Browser-Anwendung. Der Nutzer ruft die
                    URL auf und interagiert mit der Funktionalität.
Preconditions:      Browser geöffnet, Karten-URL aufgerufen.
Postconditions:     Nutzer navigiert von der Karten-Website weg.
Normal Course:      1. Browser öffnen
                    2. Zur Karten-URL navigieren
                    3. Mit der Karte über verfügbare Funktionen interagieren
Alternative Courses: Keine
Exceptions:         Keine
Priority:           High
Frequency of Use:   Einmal pro Besuch
Special Requirements: 24/7-Zugriff; Antwortzeiten vergleichbar mit gängigen
                    Web-Kartendiensten (z.B. Google Maps); Accessibility-
                    und eCommunications-Vorgaben
```

> **Traceability-Hinweis:** Funktionale Anforderungen werden auf Use Cases zurückgeführt (USE-CASE-Spalte im BRD), Use Cases referenzieren Business Rules — so entsteht eine durchgängige Kette von Business Rule → Use Case → Anforderung → Test.

---

## 16. Feature-Mapping: App-Features aus der Wissensbasis

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
| Prioritäts-Wizard | Kap. 6, 9 | MEDIUM | 3-Schritt-Priorisierung + 5-stufiges BRD-Rating |
| Business-Case-Builder | Kap. 14 | MEDIUM | Business Case mit Optionen + NPV/ROI/Payback erstellen |
| Use-Case-Editor | Kap. 15 | MEDIUM | Use-Case-Narrative mit Traceability zu Requirements |
| Glossar & Nachschlagewerk | Kap. 12 | LOW | Integriertes BA-Glossar |
| Skills Self-Assessment | Kap. 13 | LOW | Interaktive Kompetenzbewertung |
| Traceability Matrix | Kap. 5, 15 | LOW | Business Rule ↔ Use Case ↔ Requirement ↔ Test |

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

**Was:** Integriertes, durchsuchbares BA-Glossar mit **351 professionellen Definitionen** (aus `glossary.json`) + kontextsensitive Hilfe im Editor.

**Datenquelle:** `glossary.json` — direkt ladbar, kein manuelles Eingeben nötig.

**Zusatzfunktionen:**
- Fuzzy-Search über alle 351 Begriffe
- Verlinkung von Begriffen im Editor (Hover → Definition)
- Nutzer kann eigene Begriffe hinzufügen (persistent gespeichert)
- Export als Glossar-Anhang für BRD
- Filter nach Kategorien (Methoden, Rollen, Techniken, Finanzkennzahlen …)

---

### Feature 9: Skills Self-Assessment

**Was:** Interaktives Assessment der 12 BA-Skills (aus dem Excel-Tool) mit Radar-Chart-Visualisierung, Zwei-Track-Auswertung und Entwicklungsempfehlungen.

**Skills:** Oral Communication, Written Communication, Problem Solving, Critical Thinking, Negotiation, Decision-Making, Facilitation, Technical Aptitude, Documentation, Visual Modeling, Relationship-Building, Self-Managing

**Skala:** Very Poor / Poor / Good / Very Good (4-stufig)

```python
SKILLS = [
    "Oral Communication", "Written Communication", "Problem Solving",
    "Critical Thinking", "Negotiation", "Decision-Making", "Facilitation",
    "Technical Aptitude", "Documentation", "Visual Modeling",
    "Relationship-Building", "Self-Managing"
]
RATINGS = ["Very Poor", "Poor", "Good", "Very Good"]

def evaluate(ratings: dict[str, str]) -> dict:
    leverageable = {k: v for k, v in ratings.items() if v in ("Good", "Very Good")}
    to_improve = {k: v for k, v in ratings.items() if v in ("Poor", "Very Poor")}
    return {"leverageable": leverageable, "to_improve": to_improve}
```

**Output:**
- Radar-Chart (matplotlib / plotly) — 12 Achsen
- Zwei-Track-Auswertung: Leverageable Skills + Skills to Improve
- Erfahrungs-Brainstorming für Stärken
- Verbesserungsmaßnahmen für Schwächen
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

### Feature 11: Business-Case-Builder

**Was:** Geführter Workflow zur Erstellung eines vollständigen Business Case inklusive Finanzkennzahlen-Rechner.

**Workflow (6 Schritte gemäß Kap. 14):**
1. Problem Statement erfassen
2. Analysis (inkl. "Was passiert bei Nichtstun?")
3. Solution Options sammeln — App erzwingt eine "Do Nothing"-Option
4. Cost-Benefit pro Option eingeben → automatische Berechnung
5. Recommendation formulieren
6. Executive Summary (zuletzt, optional auto-generiert aus den Abschnitten)

**Finanzrechner:**

```python
def payback_period(initial_investment: float, annual_net_benefit: float) -> float:
    return initial_investment / annual_net_benefit  # in Jahren

def roi(net_gain: float, investment_cost: float) -> float:
    return (net_gain / investment_cost) * 100  # in Prozent

def npv(cashflows: list[float], discount_rate: float) -> float:
    # cashflows[0] = -Investition (Jahr 0), danach jährliche Netto-Cashflows
    return sum(cf / (1 + discount_rate) ** year
              for year, cf in enumerate(cashflows))
```

**Output:** Strukturiertes Business-Case-Dokument (Markdown/Word/PDF) + Optionen-Vergleichstabelle (Payback / ROI / NPV nebeneinander) zur Entscheidungsunterstützung.

---

### Feature 12: Use-Case-Editor

**Was:** Editor für Use-Case-Narrative nach dem Template aus Kap. 15 mit automatischer Traceability-Verknüpfung.

**Datenmodell:**

```python
@dataclass
class UseCase:
    id: str                      # hierarchisch: "1", "1.2"
    name: str                    # Verb + Nomen
    actors: list[str]
    description: str
    preconditions: list[str]
    postconditions: list[str]
    normal_course: list[str]     # nummerierte Schrittfolge
    alternative_courses: list[str]   # IDs: X.Y.AC.n
    exceptions: list[str]            # IDs: X.Y.EX.n
    includes: list[str]          # IDs anderer Use Cases
    priority: Priority           # gleiches 1-5 Schema wie BRD
    frequency_of_use: str
    business_rules: list[str]    # BR-IDs
    special_requirements: list[str]
    linked_requirements: list[str]   # Requirement-IDs (Traceability)
```

**Features:**
- Schritt-für-Schritt-Erfassung des Normal Course mit Akteur/System-Wechsel
- Verknüpfung zu Business Rules und Requirements
- Optionaler Export als UML-Use-Case-Diagramm (z.B. via plantuml)
- Speist die USE-CASE-Spalte des BRD-Generators

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

### Business-Case-Aufbau (Reihenfolge)

```
1. Problem Statement   (Was ist das Problem/die Chance?)
2. Analysis            (Was/Warum/Wie + Folgen bei Nichtstun)
3. Solution Options    (mehrere Optionen, IMMER inkl. "Do Nothing")
4. Cost-Benefit        (Payback · ROI · NPV pro Option)
5. Recommendation      (begründete Empfehlung, passend zur Situation)
6. Executive Summary   (zuletzt schreiben!)
```

### Prioritäts-Ratings (BRD)

```
1 Critical → ohne sie kein Projekt
2 High     → Minimalversion ginge ohne sie
3 Medium   → Mehrwert, aber verzichtbar
4 Low      → nice to have
5 Future   → out of scope, künftiges Release
```
