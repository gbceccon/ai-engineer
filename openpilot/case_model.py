"""Incident case domain model — the core data structure OpenPilot evolves around.

A `Case` mirrors the shape of an Open Finance regulatory incident record
(anonymized/synthetic only): who reported it, what happened, which BACEN
requirement is at stake, and its lifecycle.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date

# Incident categories inspired by common Open Finance regulatory case types.
CATEGORIES = (
    "consent",          # enrollment/consent flow failures
    "data_sharing",     # API data transmission errors or delays
    "sla_breach",       # response time commitments missed
    "availability",     # directory/API outages
    "security",         # credentials, tokens, fraud signals
    "other",
)


@dataclass
class Case:
    """A single regulatory incident case (synthetic data only)."""

    case_id: str
    title: str
    description: str
    participant: str                 # reporting institution (synthetic names)
    bacen_requirement: str           # e.g. "Res. 440 Art. 12"
    opened: date
    sla_days: int = 10
    category: str | None = None      # filled by classifier (Phase 1+)
    tags: list[str] = field(default_factory=list)

    @property
    def text(self) -> str:
        """Text used for retrieval and classification."""
        return f"{self.title}. {self.description}"

    def is_overdue(self, today: date | None = None) -> bool:
        today = today or date.today()
        deadline_days = self.sla_days
        return (today - self.opened).days > deadline_days
