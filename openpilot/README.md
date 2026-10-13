# OpenPilot 🛩️ — AI copilot for Open Finance regulatory incidents

Evolving project of the [12-month AI roadmap](../ROADMAP.md). Domain: triage, root-cause
classification and remediation drafting for regulatory incident cases (Open Finance / BACEN),
built on a **synthetic** dataset — never real bank data.

## Versions
- **v0.1 (Phase 1)** — synthetic case generator, TF-IDF search, sklearn incident-type classifier
- **v0.2 (Phase 3)** — fine-tuned BERT + embeddings
- **v0.3 (Phase 4)** — RAG chat + evaluation harness
- **v0.4 (Phase 5)** — agent workflow + LoRA model
- **v1.0 (Phase 6)** — production API

## Dev
```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
ruff check .
```

## Layout
```
openpilot/     package code (grows per phase)
tests/         pytest suite (CI runs it)
```
