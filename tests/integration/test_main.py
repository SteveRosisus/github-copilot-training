import pytest


@pytest.mark.asyncio
@pytest.mark.integration
async def test_status_returns_ok(client) -> None:
    response = await client.get("/status")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
@pytest.mark.integration
async def test_tasks_returns_all_seeded_tasks(client) -> None:
    response = await client.get("/tasks")

    assert response.status_code == 200
    payload = response.json()
    assert len(payload) == 3
    assert payload[0]["task_id"] == 1
    assert payload[0]["status"] == "complete"


@pytest.mark.asyncio
@pytest.mark.integration
async def test_task_status_returns_task_status_for_existing_task(client) -> None:
    response = await client.get("/task/1/status")

    assert response.status_code == 200
    assert response.json() == "complete"


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_returns_structured_response(client) -> None:
    response = await client.post(
        "/log_task",
        json={
            "task_id": 0,
            "title": "Document API behavior",
            "status": "pending",
            "hours_spent": 1.5,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "task_id": 4,
        "message": "Task logged successfully.",
    }


@pytest.mark.asyncio
@pytest.mark.integration
async def test_report_counts_only_completed_tasks(client) -> None:
    response = await client.get("/report")

    assert response.status_code == 200
    assert response.json() == {
        "total_tasks": 3,
        "completed_tasks": 1,
        "total_hours_spent": 23.5,
        "completion_rate": 0.33,
    }


@pytest.mark.asyncio
@pytest.mark.integration
async def test_task_status_returns_404_for_missing_task(client) -> None:
    response = await client.get("/task/999/status")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


@pytest.mark.asyncio
@pytest.mark.integration
async def test_log_task_returns_422_for_invalid_payload(client) -> None:
    response = await client.post(
        "/log_task",
        json={
            "task_id": 0,
            "status": "pending",
            "hours_spent": 1.0,
        },
    )

    assert response.status_code == 422
