"""Wissensbasis-Zugriff für den BA-Tutor.

Lädt die Knowledge-Base (Markdown) und das Glossar (JSON) und stellt sie als
Kontext für den Tutor bereit. Optional: einfache stichwortbasierte Suche für
ein späteres RAG-Setup (Strategie B im Konzept).
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class GlossaryEntry:
    term: str
    definition: str


@dataclass
class KnowledgeBase:
    """Hält Knowledge-Base-Text und Glossar im Speicher."""

    kb_markdown: str
    glossary: list[GlossaryEntry] = field(default_factory=list)

    # ------------------------------------------------------------------ #
    # Laden
    # ------------------------------------------------------------------ #
    @classmethod
    def load(
        cls,
        kb_path: str | Path = "ba_knowledge_base.md",
        glossary_path: str | Path = "glossary.json",
    ) -> "KnowledgeBase":
        kb_text = Path(kb_path).read_text(encoding="utf-8")
        glossary: list[GlossaryEntry] = []
        gpath = Path(glossary_path)
        if gpath.exists():
            data = json.loads(gpath.read_text(encoding="utf-8"))
            for item in data.get("glossary", []):
                glossary.append(
                    GlossaryEntry(term=item["term"], definition=item["definition"])
                )
        return cls(kb_markdown=kb_text, glossary=glossary)

    # ------------------------------------------------------------------ #
    # Kontext für den System-Prompt (Strategie A: volle Injektion)
    # ------------------------------------------------------------------ #
    def as_context(self) -> str:
        """Gesamte Wissensbasis als ein Textblock (für Prompt-Caching)."""
        parts = [self.kb_markdown, "\n\n# Glossar (vollständig)\n"]
        for e in self.glossary:
            parts.append(f"- **{e.term}**: {e.definition}")
        return "\n".join(parts)

    # ------------------------------------------------------------------ #
    # Glossar-Lookup (offline, sofort)
    # ------------------------------------------------------------------ #
    def lookup(self, query: str, limit: int = 5) -> list[GlossaryEntry]:
        """Fuzzy-Glossarsuche über Begriffe und Definitionen."""
        q = query.lower().strip()
        if not q:
            return []
        scored: list[tuple[int, GlossaryEntry]] = []
        for e in self.glossary:
            term = e.term.lower()
            score = 0
            if q == term:
                score = 100
            elif q in term:
                score = 60
            elif term in q:
                score = 40
            elif q in e.definition.lower():
                score = 20
            if score:
                scored.append((score, e))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [e for _, e in scored[:limit]]

    # ------------------------------------------------------------------ #
    # Einfache Chunk-Suche (Vorstufe für RAG / Strategie B)
    # ------------------------------------------------------------------ #
    def search_sections(self, query: str, limit: int = 3) -> list[str]:
        """Findet die relevantesten Markdown-Abschnitte per Stichwort-Overlap."""
        sections = self._split_sections()
        terms = {t for t in re.findall(r"\w+", query.lower()) if len(t) > 2}
        if not terms:
            return []
        scored: list[tuple[int, str]] = []
        for sec in sections:
            words = set(re.findall(r"\w+", sec.lower()))
            overlap = len(terms & words)
            if overlap:
                scored.append((overlap, sec))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [s for _, s in scored[:limit]]

    def _split_sections(self) -> list[str]:
        """Teilt die KB an `## `-Überschriften in Abschnitte."""
        parts = re.split(r"(?m)^(?=## )", self.kb_markdown)
        return [p.strip() for p in parts if p.strip()]
