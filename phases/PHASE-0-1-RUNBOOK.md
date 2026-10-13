# Phase 0 & 1 Runbook — first commit to v0.1 (Weeks 1–6)

## Phase 0 — Setup (Week 1, do this first)
- [ ] Create GitHub repo `ai-engineer` (public) and connect:
      `git remote add origin git@github.com:<user>/ai-engineer.git && git push -u origin main`
- [ ] Enable branch protection on `main` (require CI green)
- [x] Install local tooling: `python -m venv .venv && pip install -e ".[dev]"` → run `pytest` ✔ (2025-10-12, 4 passed on pyenv 3.11.9)
- [ ] Post #0 on LinkedIn: announce the 12-month public learning journey (link repo)
- **Gate:** CI green on GitHub + README live. Done ✔ when the Actions badge shows passing.

## Phase 1 — Python for AI + OpenPilot v0.1 (Weeks 2–6, ~12h/week)
**Study (4–6h/week):** Python fluency (comprehensions, dataclasses, typing, pathlib),
NumPy basics, pandas (groupby/merge/datetime), scikit-learn intro, Karpathy *Zero to Hero* p1–2.

**Build (12h/week):**
1. **Synthetic dataset (wk 2):** write `openpilot/generate_cases.py` → 500 synthetic cases
   across the 6 categories, with realistic PT-BR/EN mixed text; commit as `data/cases.jsonl`.
2. **EDA (wk 3):** pandas notebook `phases/phase-1-python-ai/eda.ipynb` — category mix, SLA
   distribution, overdue rate. Screenshot charts into the phase notes.
3. **Search (wk 3–4):** TF-IDF (sklearn) over case text + a `search(query)` CLI returning
   top-k similar past cases. This is literally v0 of retrieval — you'll upgrade it in Ph4.
4. **Classifier (wk 4–5):** TF-IDF + LinearSVC, stratified 80/20 split, macro-F1 report
   vs the keyword baseline in `openpilot/triage.py`.
5. **Benchmark report (wk 5–6):** fill `benchmarks/v0.1.md`, tag `v0.1`, write `gate.md`.

**Gate:** v0.1 classifier beats keyword baseline on macro-F1 (report proves it), all tests
green, tag pushed. **Only then** start Phase 2.

## Study log (Feynman notes → phases/phase-1-python-ai/notes.md)
Keep it lightweight: after each study session, 5 bullet points in English explaining what
you learned *to a colleague*. Those bullets become your LinkedIn posts later.
