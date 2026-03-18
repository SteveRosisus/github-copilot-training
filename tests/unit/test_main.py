import pytest

import app.main as main_module
from app.main import fetch_all_tasks, generate_productivity_report
from app.models import DeveloperTask, TaskStatus


@pytest.mark.asyncio
async def test_fetch_all_tasks_returns_seeded_tasks() -> None:
    tasks = await fetch_all_tasks()

    assert len(tasks) == 3
    assert tasks[0].task_id == 1
    assert tasks[0].status == TaskStatus.COMPLETE


@pytest.mark.asyncio
async def test_generate_productivity_report_calculates_expected_metrics() -> None:
    report = await generate_productivity_report()

    assert report.total_tasks == 3
    assert report.completed_tasks == 1
    assert report.total_hours_spent == 23.5
    assert report.completion_rate == 0.33


@pytest.mark.asyncio
async def test_generate_productivity_report_handles_no_tasks(monkeypatch) -> None:
    async def fake_fetch_all_tasks() -> list[DeveloperTask]:
        return []

    monkeypatch.setattr(main_module, "fetch_all_tasks", fake_fetch_all_tasks)

    report = await generate_productivity_report()

    assert report.total_tasks == 0
    assert report.completed_tasks == 0
    assert report.total_hours_spent == 0
    assert report.completion_rate == 0.0
