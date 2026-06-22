"""SMART-Checker — prüft Anforderungen gegen die 5 SMART-Kriterien.

Läuft komplett offline (keine API-Kosten). Heuristik basiert auf der
SMART-Detail-Checklist aus der Wissensbasis (Kap. 4).
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum


class Rating(str, Enum):
    GREEN = "green"   # erfüllt
    YELLOW = "yellow"  # teilweise / unsicher
    RED = "red"       # nicht erfüllt


@dataclass
class DimensionResult:
    dimension: str
    rating: Rating
    hint: str


@dataclass
class SmartResult:
    requirement: str
    dimensions: list[DimensionResult]

    @property
    def is_smart(self) -> bool:
        return all(d.rating == Rating.GREEN for d in self.dimensions)

    def summary(self) -> str:
        icons = {Rating.GREEN: "🟢", Rating.YELLOW: "🟡", Rating.RED: "🔴"}
        lines = [f"Anforderung: {self.requirement}", ""]
        for d in self.dimensions:
            lines.append(f"{icons[d.rating]} {d.dimension}: {d.hint}")
        return "\n".join(lines)


# Signalwörter für Vagheit (Specific) und Unerreichbarkeit (Attainable)
_VAGUE_WORDS = {
    "schnell", "einfach", "benutzerfreundlich", "gut", "angemessen",
    "effizient", "intuitiv", "modern", "flexibel", "robust", "einige",
    "viele", "mehrere", "fast", "etwa", "ungefähr", "möglichst",
}
_IMPOSSIBLE = [
    r"100\s*%\s*(uptime|verfügbar)", r"\b0\s*(fehler|bugs|downtime)\b",
    r"sofort(ige)?\s*(antwort|reaktion)", r"unendlich", r"jederzeit\s*100",
    r"keinerlei\s*(fehler|ausfälle)",
]
_MEASURE = re.compile(
    r"\d+\s*(%|prozent|sek|sekunden|ms|min|minuten|std|stunden|tage?|"
    r"nutzer|user|requests|mb|gb|€|eur|zeichen)", re.IGNORECASE
)
_ID_PATTERN = re.compile(r"\b(FR|NFR|PC|BR|REQ|UC)[-\s]?\d+\b", re.IGNORECASE)


def check(requirement: str, has_id: bool = False, has_source: bool = False) -> SmartResult:
    """Prüft eine Anforderung gegen SMART. Gibt ein SmartResult zurück."""
    text = requirement.strip()
    low = text.lower()
    dims: list[DimensionResult] = []

    # --- Specific ---------------------------------------------------- #
    found_vague = sorted({w for w in _VAGUE_WORDS if re.search(rf"\b{w}\b", low)})
    has_verb = bool(re.search(
        r"\b(muss|soll|kann|wird|berechnet|speichert|zeigt|sendet|"
        r"validiert|erlaubt|ermöglicht|prüft|erstellt|löscht|aktualisiert)\b", low
    ))
    if found_vague:
        dims.append(DimensionResult(
            "Specific", Rating.RED,
            f"Vage Wörter gefunden: {', '.join(found_vague)} — konkretisieren."))
    elif not has_verb:
        dims.append(DimensionResult(
            "Specific", Rating.YELLOW,
            "Kein klares Verb (muss/soll/zeigt/…) erkennbar."))
    else:
        dims.append(DimensionResult(
            "Specific", Rating.GREEN, "Klar und ohne vage Formulierungen."))

    # --- Measurable -------------------------------------------------- #
    if _MEASURE.search(text):
        dims.append(DimensionResult(
            "Measurable", Rating.GREEN, "Enthält messbare Werte."))
    else:
        dims.append(DimensionResult(
            "Measurable", Rating.RED,
            "Kein messbarer Wert (Zahl/Zeit/Prozent/Einheit) gefunden."))

    # --- Attainable -------------------------------------------------- #
    impossible = [p for p in _IMPOSSIBLE if re.search(p, low)]
    if impossible:
        dims.append(DimensionResult(
            "Attainable", Rating.RED,
            "Physisch/wirtschaftlich unrealistisches Ziel "
            "(z. B. 100 % Uptime, 0 Fehler, sofortige Antwort)."))
    else:
        dims.append(DimensionResult(
            "Attainable", Rating.GREEN,
            "Keine offensichtlich unerreichbaren Absolutwerte."))

    # --- Reasonable -------------------------------------------------- #
    # Nur kontextabhängig vollständig prüfbar -> heuristischer Hinweis.
    dims.append(DimensionResult(
        "Reasonable", Rating.YELLOW,
        "Bezug zum Geschäftsziel manuell prüfen (Sanity-Check)."))

    # --- Traceable --------------------------------------------------- #
    detected_id = has_id or bool(_ID_PATTERN.search(text))
    if detected_id and has_source:
        dims.append(DimensionResult(
            "Traceable", Rating.GREEN, "ID und Quelle vorhanden."))
    elif detected_id or has_source:
        dims.append(DimensionResult(
            "Traceable", Rating.YELLOW,
            "Entweder ID oder Quelle fehlt — beides für Rückverfolgbarkeit nötig."))
    else:
        dims.append(DimensionResult(
            "Traceable", Rating.RED,
            "Keine eindeutige ID und keine Quelle erkennbar."))

    return SmartResult(requirement=text, dimensions=dims)
