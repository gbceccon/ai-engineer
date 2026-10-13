"""Smoke tests for the OpenPilot scaffold — CI must stay green."""

from datetime import date, timedelta

from openpilot.case_model import Case
from openpilot.triage import triage


def _case(**overrides) -> Case:
    base = {
        "case_id": "CASE-001",
        "title": "Consent flow failing for enrollment",
        "description": "Customer consent token rejected during enrollment",
        "participant": "Banco Sintetico S.A.",
        "bacen_requirement": "Res. 440 Art. 12",
        "opened": date(2025, 1, 1),
    }
    base.update(overrides)
    return Case(**base)


def test_case_text_combines_title_and_description():
    case = _case()
    assert "Consent flow" in case.text and "consent token" in case.text


def test_case_is_overdue_after_sla_window():
    case = _case(opened=date.today() - timedelta(days=15), sla_days=10)
    assert case.is_overdue()
    fresh = _case(opened=date.today() - timedelta(days=2), sla_days=10)
    assert not fresh.is_overdue()


def test_triage_detects_keyword_categories():
    assert triage(_case()) == "consent"
    outage = _case(
        title="Directory API unavailable",
        description="Open Finance directory down for 3 hours, 5xx responses",
    )
    assert triage(outage) == "availability"


def test_triage_falls_back_to_other():
    mystery = _case(title="Weird behavior", description="Nothing matches here at all")
    assert triage(mystery) == "other"
