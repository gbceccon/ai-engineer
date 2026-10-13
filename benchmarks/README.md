# Benchmarks — every release proves it beat the previous one

One Markdown report per tagged release: `vX.Y.md`. Template:

```md
# vX.Y — <date>
**Task:** incident-type classification (5 categories, synthetic set of N=500)
**Dataset:** synthetic, reproducible seed
**Metrics:** macro-F1, precision/recall per class, latency, cost

| Model | macro-F1 | Δ vs previous |
|-------|----------|---------------|
| keyword baseline (v0.0) | | |
| TF-IDF + LinearSVC (v0.1) | | |
| fine-tuned BERT (v0.2) | | |

**Conclusion:** …
**Reproduce:** `python benchmarks/run_vX_Y.py`
```

The keyword baseline (`openpilot/triage.py`) is the floor. If a fancier model
doesn't beat it, the benchmark says so — honesty is the portfolio piece.
