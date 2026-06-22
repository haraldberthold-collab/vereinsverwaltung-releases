"""BATutor — KI-gestützter Business-Analysis-Coach.

Beantwortet Fragen gestützt auf die Wissensbasis (ba_knowledge_base.md +
glossary.json). Nutzt claude-opus-4-8 mit adaptive thinking, Streaming und
Prompt-Caching auf der stabilen Wissensbasis.
"""
from __future__ import annotations

import os
from collections.abc import Iterator
from dataclasses import dataclass, field

import anthropic

from .knowledge import KnowledgeBase

MODEL = "claude-opus-4-8"

SYSTEM_PERSONA = """\
Du bist ein erfahrener Business-Analysis-Coach für die App "LeadBusinessAnalyst" \
(Telekommunikationsbranche). Du hilfst angehenden und praktizierenden Business \
Analysts, BA-Konzepte zu verstehen und anzuwenden.

Regeln:
- Stütze deine Antworten auf die unten bereitgestellte Wissensbasis. Wenn die \
Wissensbasis eine Frage nicht abdeckt, sage das offen und antworte mit \
allgemeinem BA-Fachwissen, klar als solches gekennzeichnet.
- Antworte didaktisch: erst die Kernidee, dann ein konkretes Beispiel, bei \
Bedarf eine Rückfrage.
- Sei präzise und praxisnah. Nutze die Terminologie aus dem Glossar.
- Antworte auf Deutsch, außer der Nutzer fragt auf Englisch.
- Wenn eine Anforderung zu prüfen ist, wende die SMART-Kriterien an.
"""


@dataclass
class BATutor:
    """Stateful Q&A-Tutor mit Konversationsverlauf."""

    knowledge: KnowledgeBase
    client: anthropic.Anthropic = field(default=None)  # type: ignore[assignment]
    effort: str = "medium"
    _messages: list[dict] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.client is None:
            # Liest ANTHROPIC_API_KEY aus der Umgebung.
            self.client = anthropic.Anthropic()

    # ------------------------------------------------------------------ #
    # System-Prompt mit gecachter Wissensbasis
    # ------------------------------------------------------------------ #
    def _system(self) -> list[dict]:
        return [
            {"type": "text", "text": SYSTEM_PERSONA},
            {
                "type": "text",
                "text": "# WISSENSBASIS\n\n" + self.knowledge.as_context(),
                # Stabiler, großer Block -> cachen (Folge-Calls ~90 % günstiger)
                "cache_control": {"type": "ephemeral"},
            },
        ]

    # ------------------------------------------------------------------ #
    # Frage stellen (Streaming)
    # ------------------------------------------------------------------ #
    def ask_stream(self, question: str) -> Iterator[str]:
        """Stellt eine Frage und streamt die Antwort als Text-Chunks."""
        self._messages.append({"role": "user", "content": question})
        answer_parts: list[str] = []

        with self.client.messages.stream(
            model=MODEL,
            max_tokens=4096,
            system=self._system(),
            thinking={"type": "adaptive"},
            output_config={"effort": self.effort},
            messages=self._messages,
        ) as stream:
            for text in stream.text_stream:
                answer_parts.append(text)
                yield text
            final = stream.get_final_message()

        # Vollständige Antwort (inkl. thinking-Blöcke) in den Verlauf übernehmen.
        self._messages.append({"role": "assistant", "content": final.content})

    def ask(self, question: str) -> str:
        """Bequeme Variante: gibt die vollständige Antwort als String zurück."""
        return "".join(self.ask_stream(question))

    def reset(self) -> None:
        """Konversationsverlauf zurücksetzen."""
        self._messages.clear()

    # ------------------------------------------------------------------ #
    # Convenience-Konstruktor
    # ------------------------------------------------------------------ #
    @classmethod
    def from_files(
        cls,
        kb_path: str = "ba_knowledge_base.md",
        glossary_path: str = "glossary.json",
        effort: str = "medium",
    ) -> "BATutor":
        if not os.environ.get("ANTHROPIC_API_KEY"):
            raise RuntimeError(
                "ANTHROPIC_API_KEY ist nicht gesetzt. "
                "Setze die Umgebungsvariable, bevor du den Tutor startest."
            )
        kb = KnowledgeBase.load(kb_path, glossary_path)
        return cls(knowledge=kb, effort=effort)
