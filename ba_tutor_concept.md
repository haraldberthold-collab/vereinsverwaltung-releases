# BA-Tutor — Architektur-Konzept

> Wie aus der Wissensbasis (`ba_knowledge_base.md` + `glossary.json`) ein
> KI-gestützter Tutor für die `LeadBusinessAnalyst` App wird.
> Stand: 2026-06-22

---

## 1. Grundidee

Der Tutor beantwortet BA-Fragen **gestützt auf die geprüfte Wissensbasis** —
nicht aus dem Bauch des Modells. Das verhindert Halluzinationen über Methoden
und sorgt für branchenkonsistente, konsistente Antworten.

```
Nutzerfrage
    │
    ▼
┌─────────────────────────────────────────────┐
│  Wissensbasis als Kontext                    │
│  (ba_knowledge_base.md + glossary.json)      │  ◄── Prompt-Caching
│  → in den System-Prompt injiziert            │      (stabil, 1x bezahlt)
└─────────────────────────────────────────────┘
    │
    ▼
Claude (claude-opus-4-8, adaptive thinking)
    │
    ▼
Fundierte, auf den Nutzer zugeschnittene Antwort (gestreamt)
```

---

## 2. Zwei Wissens-Strategien

| Strategie | Wann | Vorteil | Nachteil |
|-----------|------|---------|----------|
| **A) Volle Injektion** (umgesetzt) | KB passt in den Kontext (~50–60k Tokens) | Einfach, robust, kein Retrieval nötig; mit Prompt-Caching günstig | Höhere Tokenkosten beim 1. Call |
| **B) RAG / Retrieval** | KB wächst über das Kontextfenster hinaus | Skaliert auf beliebig große Wissensmengen | Mehr Code (Chunking, Scoring), Retrieval-Qualität |

**Entscheidung:** Strategie A mit Prompt-Caching. Die aktuelle Wissensbasis
passt locker in das 1M-Kontextfenster von `claude-opus-4-8`. Caching macht
Folge-Anfragen ~90 % günstiger. Strategie B ist als Erweiterung vorgesehen
(`knowledge.py` kann beides).

---

## 3. Komponenten

```
ba_tutor/
├── knowledge.py      # Lädt KB + Glossar, baut Kontext, optionale Suche
├── smart_checker.py  # SMART-Prüfung (heuristisch, ohne LLM)
├── assessment.py     # Skills-Self-Assessment → Lernpfad
├── tutor.py          # Claude-gestützter Q&A-Tutor (Kern)
└── cli.py            # Einfache Kommandozeile zum Ausprobieren
```

### 3.1 Q&A-Tutor (`tutor.py`)
- Lädt KB + Glossar einmalig in den System-Prompt (mit `cache_control`).
- Multi-Turn-Konversation (Verlauf wird mitgeführt).
- Streaming der Antwort (`messages.stream`).
- Adaptive Thinking für komplexe Fragen.
- BA-Coach-Persona: erklärt, gibt Beispiele, stellt Rückfragen.

### 3.2 SMART-Checker (`smart_checker.py`)
- **Kein LLM nötig** — reine Heuristik, sofort & kostenlos.
- Prüft jede der 5 SMART-Dimensionen und gibt Ampel + Hinweise.
- Optionaler LLM-Modus: Claude formuliert eine verbesserte Version.

### 3.3 Skills-Assessment (`assessment.py`)
- 12 BA-Skills, 4-stufige Skala (Very Poor … Very Good).
- Zwei-Track-Auswertung (Leverageable / To Improve).
- Leitet aus Schwächen einen priorisierten Lernpfad ab.

---

## 4. Modell-Konfiguration

| Parameter | Wert | Begründung |
|-----------|------|-----------|
| `model` | `claude-opus-4-8` | Aktuell stärkstes Opus-Modell |
| `thinking` | `{"type": "adaptive"}` | Modell entscheidet Denktiefe selbst |
| `output_config.effort` | `"medium"` | Guter Kosten/Qualitäts-Kompromiss für Q&A |
| Streaming | ja (`messages.stream`) | Sofortige Ausgabe, keine Timeouts |
| `cache_control` | auf KB-Block | KB ist stabil → ~90 % günstigere Folge-Calls |

---

## 5. App-Integration (Ausblick)

- **Desktop/GUI:** `BATutor.ask()` an ein Chat-Widget binden; `stream=True`
  für Live-Tokens.
- **Lernpfad-Modul:** Assessment-Ergebnis → `LearningPath` → Tutor bekommt den
  Pfad als Kontext und kann gezielt Module vorschlagen.
- **Inline-Hilfe:** Im Requirements-Editor den SMART-Checker live laufen lassen
  (kein API-Call, sofort).
- **Datenschutz:** API-Key über Umgebungsvariable `ANTHROPIC_API_KEY`; keine
  Hardcodes. Nutzereingaben gehen nur an die Anthropic-API, sonst nirgends.

---

## 6. Sicherheits- & Kostenhinweise

- **API-Key** niemals im Code — nur `os.environ["ANTHROPIC_API_KEY"]`.
- **Prompt-Caching** verifizieren: `usage.cache_read_input_tokens > 0` ab dem
  2. Call. Wenn 0 → ein „silent invalidator" (z. B. Zeitstempel im Prompt)
  bricht den Cache.
- **SMART-Checker und Assessment laufen offline** — keine API-Kosten.
- Nur der Q&A-Tutor verursacht Tokenkosten.
