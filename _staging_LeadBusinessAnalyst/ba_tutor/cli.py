"""Einfache Kommandozeile zum Ausprobieren des BA-Tutors.

Beispiele:
    python -m ba_tutor.cli smart "Das System soll schnell sein."
    python -m ba_tutor.cli glossary "use case"
    python -m ba_tutor.cli assess
    python -m ba_tutor.cli chat        # interaktiver Tutor (braucht API-Key)
"""
from __future__ import annotations

import sys

from .knowledge import KnowledgeBase
from .smart_checker import check as smart_check
from .assessment import SKILLS, SkillRating, evaluate


def _cmd_smart(args: list[str]) -> None:
    if not args:
        print('Nutzung: smart "<Anforderung>"')
        return
    result = smart_check(" ".join(args))
    print(result.summary())
    print()
    print("SMART:" , "JA ✅" if result.is_smart else "NEIN — bitte überarbeiten")


def _cmd_glossary(args: list[str]) -> None:
    kb = KnowledgeBase.load()
    hits = kb.lookup(" ".join(args))
    if not hits:
        print("Kein Treffer im Glossar.")
        return
    for e in hits:
        print(f"\n## {e.term}\n{e.definition}")


def _cmd_assess(_: list[str]) -> None:
    print("Bewerte jeden Skill: 1=Very Poor, 2=Poor, 3=Good, 4=Very Good")
    ratings: dict[str, SkillRating] = {}
    for skill in SKILLS:
        while True:
            raw = input(f"  {skill}: ").strip()
            if raw in {"1", "2", "3", "4"}:
                ratings[skill] = SkillRating(int(raw))
                break
            print("    Bitte 1–4 eingeben.")
    print()
    print(evaluate(ratings).report())


def _cmd_chat(_: list[str]) -> None:
    # Import hier, damit smart/glossary/assess ohne anthropic-Paket laufen.
    from .tutor import BATutor

    tutor = BATutor.from_files()
    print("BA-Tutor bereit. 'exit' zum Beenden.\n")
    while True:
        try:
            q = input("Du: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if q.lower() in {"exit", "quit", "ende"}:
            break
        if not q:
            continue
        print("Tutor: ", end="", flush=True)
        for chunk in tutor.ask_stream(q):
            print(chunk, end="", flush=True)
        print("\n")


_COMMANDS = {
    "smart": _cmd_smart,
    "glossary": _cmd_glossary,
    "assess": _cmd_assess,
    "chat": _cmd_chat,
}


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv or argv[0] not in _COMMANDS:
        print(f"Befehle: {', '.join(_COMMANDS)}")
        return 1
    _COMMANDS[argv[0]](argv[1:])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
