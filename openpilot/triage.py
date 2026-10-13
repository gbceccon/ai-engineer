"""Keyword triage baseline — the bar every later model must beat.

Phase 1 replaces this with a TF-IDF + sklearn classifier; Phase 3 with a
fine-tuned BERT. Until then, this dumb-but-honest baseline defines the
benchmark floor (see benchmarks/).
"""

from __future__ import annotations

from .case_model import Case

# Simple signal words per category (Portuguese + English mix, as cases arrive).
_SIGNALS: dict[str, tuple[str, ...]] = {
    "consent": ("consent", "consentimento", "enrollment", "cadastro", "token consent"),
    "data_sharing": ("data sharing", "compartilhamento", "transmission", "transmissao", "payload"),
    "sla_breach": ("sla", "prazo", "deadline", "overdue", "atraso", "late response"),
    "availability": ("outage", "indisponibilidade", "down", "downtime", "unavailable", "429"),
    "security": ("security", "seguranca", "fraud", "fraude", "credential", "token expired"),
}


def triage(case: Case) -> str:
    """Return the best-matching category for a case by keyword scoring."""
    haystack = case.text.lower()
    scores = {
        category: sum(1 for word in signals if word in haystack)
        for category, signals in _SIGNALS.items()
    }
    best = max(scores, key=lambda c: scores[c])
    return best if scores[best] > 0 else "other"
