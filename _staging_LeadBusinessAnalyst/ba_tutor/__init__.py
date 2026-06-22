"""ba_tutor — KI-gestützter Business-Analysis-Tutor für LeadBusinessAnalyst.

Komponenten:
- knowledge.KnowledgeBase : lädt Wissensbasis + Glossar
- smart_checker.check      : SMART-Prüfung (offline)
- assessment.evaluate      : Skills-Self-Assessment -> Lernpfad (offline)
- tutor.BATutor            : Claude-gestützter Q&A-Coach
"""
from .knowledge import KnowledgeBase, GlossaryEntry
from .smart_checker import check as smart_check, SmartResult, Rating
from .assessment import (
    evaluate as assess,
    empty_ratings,
    SkillRating,
    SKILLS,
    AssessmentResult,
)

__all__ = [
    "KnowledgeBase",
    "GlossaryEntry",
    "smart_check",
    "SmartResult",
    "Rating",
    "assess",
    "empty_ratings",
    "SkillRating",
    "SKILLS",
    "AssessmentResult",
]

# BATutor wird separat importiert, da es das anthropic-Paket benötigt:
#   from ba_tutor.tutor import BATutor
