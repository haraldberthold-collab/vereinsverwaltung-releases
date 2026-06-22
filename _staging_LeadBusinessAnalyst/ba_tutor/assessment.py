"""BA Skills Self-Assessment -> personalisierter Lernpfad.

12 Skills, 4-stufige Skala (Very Poor … Very Good), Zwei-Track-Auswertung
gemäß Wissensbasis Kap. 13. Läuft offline.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import IntEnum


class SkillRating(IntEnum):
    VERY_POOR = 1
    POOR = 2
    GOOD = 3
    VERY_GOOD = 4


# Die 12 Skills aus dem offiziellen Excel-Tool
SKILLS: list[str] = [
    "Oral Communication",
    "Written Communication",
    "Problem Solving",
    "Critical Thinking",
    "Negotiation",
    "Decision-Making",
    "Facilitation",
    "Technical Aptitude",
    "Documentation",
    "Visual Modeling",
    "Relationship-Building",
    "Self-Managing",
]

# Empfohlene Lernreihenfolge (Entwicklungspfad, Kap. 13)
_DEVELOPMENT_ORDER = [
    "Oral Communication", "Written Communication", "Facilitation",
    "Documentation", "Problem Solving", "Critical Thinking",
    "Technical Aptitude", "Negotiation", "Relationship-Building",
    "Decision-Making", "Self-Managing", "Visual Modeling",
]

# Lernhinweise pro Skill (für die Entwicklungsempfehlungen)
_LEARNING_HINTS: dict[str, str] = {
    "Oral Communication": "Meetings moderieren üben; aktives Zuhören; Paraphrasieren.",
    "Written Communication": "BRDs und User Stories schreiben; SMART-Formulierung üben.",
    "Problem Solving": "Root-Cause-Analyse (5-Why, Fishbone) anwenden.",
    "Critical Thinking": "Annahmen hinterfragen; Optionen systematisch bewerten.",
    "Negotiation": "Stakeholder-Konflikte moderieren; Win-Win-Lösungen suchen.",
    "Decision-Making": "Entscheidungsmatrizen nutzen; Alternativen abwägen.",
    "Facilitation": "Requirement-Workshops (JAD) planen und leiten.",
    "Technical Aptitude": "SQL-Grundlagen, API-/Integrationskonzepte lernen.",
    "Documentation": "BRD-Struktur, Use-Case-Templates, Glossarpflege üben.",
    "Visual Modeling": "BPMN, Flussdiagramme, Wireframes, Use-Case-Diagramme.",
    "Relationship-Building": "Stakeholder-Map pflegen; Vertrauen aktiv aufbauen.",
    "Self-Managing": "Aufgaben priorisieren; proaktiv Deadlines steuern.",
}


@dataclass
class AssessmentResult:
    ratings: dict[str, SkillRating]
    leverageable: list[str] = field(default_factory=list)   # Good + Very Good
    to_improve: list[str] = field(default_factory=list)     # Poor + Very Poor
    learning_path: list[tuple[str, str]] = field(default_factory=list)

    def report(self) -> str:
        lines = ["=== BA Skills Self-Assessment ===", ""]
        lines.append("Leverageable Skills (Stärken):")
        lines += [f"  + {s}" for s in self.leverageable] or ["  (keine)"]
        lines.append("")
        lines.append("Skills to Improve (Entwicklungsfelder):")
        lines += [f"  - {s}" for s in self.to_improve] or ["  (keine)"]
        lines.append("")
        lines.append("Empfohlener Lernpfad (priorisiert):")
        for i, (skill, hint) in enumerate(self.learning_path, 1):
            lines.append(f"  {i}. {skill} — {hint}")
        return "\n".join(lines)


def evaluate(ratings: dict[str, SkillRating]) -> AssessmentResult:
    """Wertet eine Skill-Bewertung aus und leitet einen Lernpfad ab."""
    leverageable = [s for s, r in ratings.items() if r >= SkillRating.GOOD]
    to_improve = [s for s, r in ratings.items() if r <= SkillRating.POOR]

    # Lernpfad: Entwicklungsfelder, sortiert nach empfohlener Reihenfolge,
    # schwächste zuerst.
    order_index = {s: i for i, s in enumerate(_DEVELOPMENT_ORDER)}
    ranked = sorted(
        to_improve,
        key=lambda s: (ratings[s], order_index.get(s, 99)),
    )
    learning_path = [(s, _LEARNING_HINTS.get(s, "")) for s in ranked]

    return AssessmentResult(
        ratings=ratings,
        leverageable=leverageable,
        to_improve=to_improve,
        learning_path=learning_path,
    )


def empty_ratings() -> dict[str, SkillRating]:
    """Vorlage mit allen Skills auf GOOD — zum Befüllen in der UI."""
    return {s: SkillRating.GOOD for s in SKILLS}
