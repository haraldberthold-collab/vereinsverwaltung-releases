# BA-Tutor (Staging)

KI-gestützter Business-Analysis-Tutor für die `LeadBusinessAnalyst`-App.

> **Hinweis:** Dieser Ordner ist ein *Staging-Bereich* im Repo
> `vereinsverwaltung-releases`, weil die aktuelle Claude-Code-Session keinen
> Schreibzugriff auf `haraldberthold-collab/LeadBusinessAnalyst` hat. Inhalt
> 1:1 dorthin verschieben.

## Bestandteile

| Datei | Zweck | API nötig? |
|-------|-------|------------|
| `ba_tutor/knowledge.py` | Lädt Wissensbasis + Glossar; Suche/Lookup | nein |
| `ba_tutor/smart_checker.py` | SMART-Prüfung von Anforderungen | nein |
| `ba_tutor/assessment.py` | Skills-Assessment → Lernpfad | nein |
| `ba_tutor/tutor.py` | Claude-gestützter Q&A-Coach | **ja** |
| `ba_tutor/cli.py` | Kommandozeile zum Ausprobieren | teils |

## Benötigte Datendateien

Im selben Verzeichnis (oder Pfad anpassen):
- `ba_knowledge_base.md`
- `glossary.json`

(Beide liegen im `vereinsverwaltung-releases`-Repo bereit und werden mit
übernommen.)

## Setup

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...    # nur für den Q&A-Tutor
```

## Nutzung

```bash
# Offline (keine API-Kosten):
python -m ba_tutor.cli smart "Die Startseite muss bei 500 Nutzern in < 1,5 s laden."
python -m ba_tutor.cli glossary "use case"
python -m ba_tutor.cli assess

# KI-Tutor (braucht API-Key):
python -m ba_tutor.cli chat
```

Programmatisch:

```python
from ba_tutor import smart_check, assess, empty_ratings, SkillRating
from ba_tutor.tutor import BATutor

# Offline
print(smart_check("Das System soll schnell sein.").summary())

# KI-Tutor
tutor = BATutor.from_files("ba_knowledge_base.md", "glossary.json")
for chunk in tutor.ask_stream("Wann nehme ich ein Requirement-Workshop statt Interviews?"):
    print(chunk, end="", flush=True)
```

## Modell

`claude-opus-4-8` mit adaptive thinking, Streaming und Prompt-Caching auf der
(stabilen) Wissensbasis. Details: `ba_tutor_concept.md`.
