# Phase 1 — Python for AI + OpenPilot v0.1 (Weeks 2–6)

Start date: 2025-10-12 · Branch: `phase-1` · Gate: **v0.1 beats the keyword baseline on macro-F1** (see runbook).

## Task tracker (one slice ≈ one week, ~12h build + 4–6h study)

- [ ] **T1 · Synthetic dataset generator** (`openpilot/generate_cases.py`)
      Spec + acceptance tests already in repo: `tests/test_generate_cases.py` (they skip until you
      implement — green CI doesn't lie). Run them: `pytest tests/test_generate_cases.py -v`
- [ ] **T2 · EDA notebook** (`phases/phase-1-python-ai/eda.ipynb`): category mix, SLA distribution,
      overdue rate, top terms per category. Paste 2–3 chart screenshots into `notes.md`.
- [ ] **T3 · TF-IDF search CLI**: `openpilot/search.py` with `build_index(cases)` + `search(query, k=5)`
      returning `(case, score)`; wire a `python -m openpilot.search "consent token error"` one-liner.
- [ ] **T4 · Classifier**: TF-IDF + LinearSVC, stratified 80/20 split, macro-F1 vs keyword baseline
      (`openpilot/triage.py`). Save metrics to `benchmarks/`.
- [ ] **T5 · Benchmark + release**: fill `benchmarks/v0.1.md`, write `gate.md`, merge `phase-1` → `main`
      via PR, tag `v0.1`.

## Environment (already installed for you)
```bash
source .venv/bin/activate     # numpy, pandas, scikit-learn, pytest, ruff ready
pytest                        # must stay green — CI runs the same thing
ruff check .                  # lint before each commit
```

## Study track (4–6h/week, bullets go to notes.md)
Python: dataclasses, generators, `pathlib`, `argparse` (you'll need it for the CLIs) →
NumPy basics → pandas (io/jsonl, groupby, datetime) → scikit-learn Vectorizer/Classifier intro →
Karpathy Zero to Hero p1–2 (PE, backprop intuition).

## Commit convention this phase
`phase1: T1 dataset generator` · `phase1: T3 tfidf search + tests` … (small, frequent, ≥4/week).
