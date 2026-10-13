"""T1 acceptance contract — OpenPilot synthetic dataset generator.

You (Gabriel) write `openpilot/generate_cases.py`; this file defines what "done" means.
Tests SKIP (not fail) while the module doesn't exist, so CI stays green until T1 lands.
They also document the exact api you'll build T2–T4 on top of. Run: pytest tests/test_generate_cases.py -v

Suggested module shape:
    # openpilot/generate_cases.py
    def generate_cases(n: int = 500, seed: int = 42) -> list[Case]: ...
    def write_jsonl(cases: Iterable[Case], path: Path) -> int: ...   # returns rows written
    if __name__ == "__main__": argparse CLI: --n --seed --out data/cases.jsonl
Hint: jsonl line = dataclasses.asdict(case) with opened.isoformat(); read back with
      Case(**{**d, "opened": date.fromisoformat(d["opened"])}) for T2/T3.
"""

from __future__ import annotations

from datetime import date

import pytest
from openpilot.case_model import CATEGORIES, Case

gen = pytest.importorskip(
    "openpilot.generate_cases",
    reason="T1 not started yet: implement openpilot/generate_cases.py",
)

N = 500


@pytest.fixture(scope="module")
def cases() -> list[Case]:
    return gen.generate_cases(n=N, seed=42)


def test_returns_requested_count(cases):
    assert len(cases) == N


def test_all_are_case_instances_with_valid_category(cases):
    assert all(isinstance(c, Case) for c in cases)
    assert all(c.category in CATEGORIES for c in cases)


def test_all_categories_covered_with_min_volume(cases):
    counts = {cat: sum(1 for c in cases if c.category == cat) for cat in CATEGORIES}
    assert all(counts[cat] >= 30 for cat in CATEGORIES), counts


def test_ids_are_unique(cases):
    ids = [c.case_id for c in cases]
    assert len(set(ids)) == len(ids)


def test_text_fields_are_populated(cases):
    for c in cases:
        assert len(c.title.strip()) >= 10
        assert len(c.description.strip()) >= 40
        assert c.participant.strip()
        assert c.bacen_requirement.strip()


def test_opened_dates_are_recent_and_sla_sane(cases):
    for c in cases:
        assert 0 <= (date.today() - c.opened).days <= 365
        assert 1 <= c.sla_days <= 30


def test_same_seed_is_reproducible():
    assert [c.case_id for c in gen.generate_cases(50, 7)] == [
        c.case_id for c in gen.generate_cases(50, 7)
    ]


def test_different_seed_changes_output():
    a = [c.title for c in gen.generate_cases(50, 1)]
    b = [c.title for c in gen.generate_cases(50, 2)]
    assert a != b


def test_write_jsonl_roundtrip(tmp_path, cases):
    out = tmp_path / "cases.jsonl"
    written = gen.write_jsonl(cases[:10], out)
    assert written == 10
    lines = out.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 10
    first = lines[0].split('"case_id"')
    assert len(first) == 2  # crude but proves jsonl shape; you may assert richer in your own tests
