# Phase 1 — Python for AI study notes (Feynman technique)

One bullet per study session, in English, as if explaining to a colleague. These bullets
become the material for LinkedIn posts later.

## Session 1 — setup & first dataset slice (2025-10-12)
- `openpilot/generate_cases.py` produces 500 synthetic Open Finance incident cases across 6
  categories, written to `data/cases.jsonl`.
- Dataclass `Case` is the single source of truth: `case_id`, `title`, `description`,
  `participant`, `bacen_requirement`, `opened`, `sla_days`, `category`, `tags`.
- `Case.text` joins title + description — the string every retrieval/classifier model reads.
- `Case.is_overdue()` compares `(today - opened).days > sla_days` — the SLA signal that Phase 2
  will learn to predict.

## Session 2 — study notes
_(add your bullets here after each session)_