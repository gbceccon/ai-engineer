# Gabriel Ceccon — AI Engineering Journey 🚀

> **From 18 years in fintech infrastructure to AI Engineer specialized in regulated finance.**
> A public, versioned learning program: 7 phases, 12 months, one evolving project. Progress tracker: [ROADMAP.md](ROADMAP.md).

## Who I am

Senior Technical Program Manager in Open Finance (Brazil's Central Bank regulatory programs at [Sicredi](https://www.sicredi.com.br/)), scaling a regulatory incident program from 20 to 200 cases/month — now building the AI systems that automate what I used to run manually. Background from C/C++ firmware at HP to cross-team incident command in core banking.

## The evolving project: OpenPilot

**An AI copilot for Open Finance regulatory incident management** — the domain where I have 4+ years of hands-on experience. Synthetic dataset of incident cases (no real bank data); the system evolves with each roadmap phase:

| Version | Phase | Capability |
|---------|-------|------------|
| v0.1 | 1 | Search (TF-IDF) + incident-type classifier (sklearn baseline) |
| v0.2 | 3 | Fine-tuned BERT root-cause classifier + semantic embeddings |
| v0.3 | 4 | RAG chat over incident history & BACEN rules, with citations + eval harness |
| v0.4 | 5 | Agentic remediation-draft workflow + own fine-tuned (LoRA) model |
| v1.0 | 6 | Production deployment: API, observability, guardrails, tests |

Each release ships with a [benchmark report](benchmarks/) comparing it to the previous version.

## Writing

Monthly technical articles in [writing/](writing/) — from baselines to LLM evaluation in regulated domains.

## Repo map

```
ROADMAP.md      one-page plan with progress
phases/         study notes and exercises per phase
openpilot/      the evolving project (tested code)
writing/        public articles (English)
benchmarks/     version-vs-version evaluation reports
```

**Stack being built:** Python · NumPy/pandas · scikit-learn · PyTorch · Hugging Face · LangGraph · pgvector · FastAPI · Docker · GitHub Actions

*This repository is my portfolio. Every phase gate is a working, documented deliverable — no certificates-only learning.*
