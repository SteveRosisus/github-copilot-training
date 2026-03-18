from collections.abc import AsyncIterator

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

import app.main as main_module
from app.main import app as fastapi_app
from app.models import DeveloperTask, TaskStatus


@pytest.fixture
def app():
    return fastapi_app


@pytest_asyncio.fixture
async def client(app) -> AsyncIterator[AsyncClient]:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as async_client:
        yield async_client


@pytest.fixture
def db_session() -> None:
    return None


@pytest.fixture
def auth_token() -> str:
    return "test-token"


@pytest.fixture(autouse=True)
def reset_mock_tasks() -> None:
    main_module.MOCK_TASKS.clear()
    main_module.MOCK_TASKS.update(
        {
            1: DeveloperTask(
                task_id=1,
                title="Refactor legacy service",
                status=TaskStatus.COMPLETE,
                hours_spent=8.5,
            ),
            2: DeveloperTask(
                task_id=2,
                title="Implement new user auth flow",
                status=TaskStatus.IN_PROGRESS,
                hours_spent=15.0,
            ),
            3: DeveloperTask(
                task_id=3,
                title="Write unit tests for checkout",
                status=TaskStatus.PENDING,
                hours_spent=0.0,
            ),
        }
    )
