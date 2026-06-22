# Übergabe-Notiz — BA-Tutor → LeadBusinessAnalyst

Diese Notiz beschreibt, wie der hier (im Repo `vereinsverwaltung-releases`,
Branch `claude/lead-business-analyst-tbtcpj`) gebaute BA-Tutor in den
Ziel-Repo `haraldberthold-collab/LeadBusinessAnalyst` übernommen wird.

> **Warum Staging?** Die Session, in der dieser Code entstand, hatte nur
> Schreibzugriff auf `vereinsverwaltung-releases`. Der Code wurde deshalb hier
> zwischengelagert. Inhaltlich gehört er in den App-Repo.

---

## 1. Was wohin gehört

Quelle (dieser Repo) → Ziel (`LeadBusinessAnalyst`, Repo-Wurzel):

| Quelle | Ziel |
|--------|------|
| `_staging_LeadBusinessAnalyst/ba_tutor/` | `ba_tutor/` |
| `_staging_LeadBusinessAnalyst/requirements.txt` | `requirements.txt` (mergen, falls vorhanden) |
| `_staging_LeadBusinessAnalyst/README.md` | als `ba_tutor/README.md` oder Abschnitt im Haupt-README |
| `_staging_LeadBusinessAnalyst/.gitignore` | in vorhandenes `.gitignore` mergen |
| `ba_knowledge_base.md` (Repo-Wurzel) | `data/ba_knowledge_base.md` (oder Repo-Wurzel) |
| `glossary.json` (Repo-Wurzel) | `data/glossary.json` (oder Repo-Wurzel) |
| `ba_tutor_concept.md` (Repo-Wurzel) | `docs/ba_tutor_concept.md` |

> Wenn die Datendateien nicht in der Wurzel liegen, beim Aufruf den Pfad
> angeben: `BATutor.from_files("data/ba_knowledge_base.md", "data/glossary.json")`.

---

## 2. Transfer-Wege (einer reicht)

### A) Neue Session auf LeadBusinessAnalyst (empfohlen)
In einer Claude-Code-Session, die auf `LeadBusinessAnalyst` zeigt, sagen:
> „Übernimm den BA-Tutor aus dem Staging-Branch
> `claude/lead-business-analyst-tbtcpj` des Repos `vereinsverwaltung-releases`."

Claude legt dann alle Dateien am richtigen Ort an.

### B) Manuell per git
```bash
# im LeadBusinessAnalyst-Klon
git remote add releases https://github.com/haraldberthold-collab/vereinsverwaltung-releases.git
git fetch releases claude/lead-business-analyst-tbtcpj
git checkout releases/claude/lead-business-analyst-tbtcpj -- \
    _staging_LeadBusinessAnalyst/ba_tutor \
    _staging_LeadBusinessAnalyst/requirements.txt \
    ba_knowledge_base.md glossary.json ba_tutor_concept.md
# danach _staging_LeadBusinessAnalyst/ba_tutor -> ba_tutor verschieben
git mv _staging_LeadBusinessAnalyst/ba_tutor ba_tutor
```

### C) Datei-Download
Die Dateien einzeln aus dem Branch herunterladen und im App-Repo ablegen.

---

## 3. Verifikation nach dem Transfer

```bash
pip install -r requirements.txt

# Offline (keine API-Kosten) — müssen ohne Fehler laufen:
python -m ba_tutor.cli smart "Das System soll schnell sein."
#   erwartet: Specific 🔴, Measurable 🔴, Traceable 🔴

python -m ba_tutor.cli smart "FR-001: Startseite lädt bei 500 Nutzern in < 1,5 s."
#   erwartet: Specific 🟢, Measurable 🟢, Attainable 🟢

python -m ba_tutor.cli glossary "use case"
#   erwartet: Definition von "Use Case" + verwandte Begriffe

python -m ba_tutor.cli assess
#   interaktiv: 12 Skills mit 1–4 bewerten -> Lernpfad

# KI-Tutor (braucht API-Key):
export ANTHROPIC_API_KEY=sk-ant-...
python -m ba_tutor.cli chat
#   Beispiel-Frage: "Wann nehme ich ein Requirement-Workshop statt Interviews?"
```

### Caching prüfen (optional, beim Q&A-Tutor)
Ab dem 2. Aufruf sollte `usage.cache_read_input_tokens > 0` sein. Wenn 0
bleibt, bricht ein „silent invalidator" den Cache (z. B. ein Zeitstempel im
System-Prompt) — siehe `ba_tutor_concept.md`, Abschnitt 6.

---

## 4. Status der Komponenten

| Komponente | Stand |
|------------|-------|
| `knowledge.py` | fertig; lädt KB + Glossar, Lookup/Suche getestet |
| `smart_checker.py` | fertig; **verifiziert** gegen echte Daten |
| `assessment.py` | fertig; **verifiziert** (Lernpfad korrekt) |
| `tutor.py` | fertig codiert nach Claude-API-Referenz; **API-Test ausstehend** (braucht Key) |
| `cli.py` | fertig; smart/glossary/assess getestet, chat ausstehend |

---

## 5. Mögliche nächste Ausbaustufen

- **GUI-Anbindung:** `BATutor.ask_stream()` an ein Chat-Widget hängen.
- **RAG (Strategie B):** Bei wachsender Wissensbasis `knowledge.search_sections()`
  nutzen, statt alles in den System-Prompt zu injizieren.
- **Requirements-Editor-Integration:** `smart_check()` live im Editor (offline).
- **Lernpfad ↔ Tutor:** Assessment-Ergebnis als Kontext an den Tutor geben,
  damit er gezielt Module zu Schwächen vorschlägt.
- **Persistenz:** Assessment-Verlauf speichern (Progress-Tracking über Zeit).
