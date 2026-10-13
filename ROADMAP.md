# AI Engineer Roadmap — 12 Months (2025–2026)

**Target profile:** AI/LLM Engineer specialized in regulated fintech (AI Delivery / Fintech AI Engineer, remote US contractor & Brazil).
**Pace:** 15–20h/week · 12h project / 4–6h theory · **never study without a commit**.
**Rules:** phase gate = working, documented deliverable · ≥4 commits/week · 1 public artifact/month (English) · 2-week buffers after Phases 4 and 6.

## 👉 WHERE I AM — current task

> **Phase 0 · Week 1 — Setup.** Open [phases/PHASE-0-1-RUNBOOK.md](phases/PHASE-0-1-RUNBOOK.md) and work the
> "Phase 0" checklist top-to-bottom: create GitHub repo → push → branch protection → local install + `pytest` →
> LinkedIn post #0. Gate ✔ when GitHub Actions shows green and the README is live. Then Phase 1 starts (same file).

*Update this block every Sunday retro (phase / week / slice of the week). This is the single "you are here" marker.*


| # | Phase | Weeks | Deliverable (exit gate) | Status |
|---|-------|-------|--------------------------|--------|
| 0 | Setup & Toolkit | 1 | Public repo + green CI + revised US CV v1 | 🔵 in progress |
| 1 | Python for AI | 2–6 | **OpenPilot v0.1** — synthetic Open Finance incident dataset + TF-IDF search + sklearn incident-type classifier (baseline documented) | ⚪ |
| 2 | Applied ML + Evaluation | 7–12 | Evaluation dashboard + SLA breach predictor + Article 1 ("Baselines matter") | ⚪ |
| 3 | Deep Learning (PyTorch) | 13–20 | **v0.2** — fine-tuned BERT root-cause classifier + semantic embeddings search; beats v0.1 on benchmark | ⚪ |
| 4 | LLMs + RAG | 21–28 | **v0.3** — RAG chat over incident history + BACEN rules with citations + evaluation harness (20 golden questions; accuracy/cost/latency) + Article 2 | ⚪ |
| 5 | Agents + Fine-tuning | 29–36 | **v0.4** — remediation-draft agent (search + timeline + regulatory checklist) + own LoRA model in A/B vs API + Article 3 | ⚪ |
| 6 | Production + MLOps | 37–44 | **v1.0** — deployed app (auth, rate-limit, observability, E2E tests) + Article 4 ("From notebook to production in a regulated domain") | ⚪ |
| 7 | Specialization + Market | 45–52 | 1 paper implementation + recruiter-ready portfolio (3-min demo) + certification + 10 applications/week + interviews | ⚪ |

## Study resources (free by default)
- **Ph1–2:** Python docs, *NumPy/pandas* tutorials, Karpathy *Zero to Hero* (p1–2), Kaggle Learn
- **Ph3:** fast.ai part 1, Karpathy *makemore* + *neural nets zero-to-hero*
- **Ph4:** Hugging Face LLM Course, ChromaDB/pgvector docs
- **Ph5:** LangGraph docs, HF `trl` + PEFT/LoRA docs
- **Ph6:** FastAPI, Docker, Langfuse, GitHub Actions deploy
- **Ph7:** 2 papers/month implemented, LLM system design, NIST AI RMF + EU AI Act (my compliance edge)

## Weekly cadence
- [ ] Monday: 30-min planning (pick the week's deliverable slice)
- [ ] Sun: retro in this file (update status column, adjust pace)
- [ ] Post: 1 English LinkedIn post / article per month

## Milestones (git tags)
`v0.1` Ph1 · `v0.2` Ph3 · `v0.3` Ph4 · `v0.4` Ph5 · `v1.0` Ph6 — each with a `benchmarks/` report proving improvement over the previous version.

## CV alignment (US/BR market)
- Positioning: **"I scaled Open Finance regulatory incident management 20→200 cases/month — then built the AI that automates triage."**
- After each phase, update the **AI Projects** section of `gabriel_ceccon_cv_us_ai_v1.docx` and the repo README.
- Public artifacts in English (US remote roles); "open to remote, US companies, contractor".
