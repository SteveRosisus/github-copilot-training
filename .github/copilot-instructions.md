# 🐍 GitHub Copilot Instructions for FastAPI Project

## Project Overview
This is a small RESTful API built with Python and the FastAPI framework. We prioritize clean, modern Python standards and clear separation of concerns.

## Tech Stack & Structure
* **Primary Language:** Python 3.10+
* **Framework:** FastAPI (with Uvicorn).
* **Dependency Manager:** uv (configured via pyproject.toml).
* **Data Models:** Pydantic models for all data validation and serialization.

## Mandatory Coding Guidelines (Copilot Context)
1.  **Asynchronous Code:** All route handlers and I/O-bound functions **must** be defined using `async def` and utilize `await`.
2.  **Type Hints:** All function signatures (parameters and return values) **must** use explicit, descriptive type hints.
3.  **Testing:** Any new endpoint or utility function **must** have a corresponding test in the `tests/` directory using `pytest` and `httpx.AsyncClient`.
4.  **Model Location:** All Pydantic data models **must** be placed in a dedicated `app/models.py` file.
5.  **Return Type:** API endpoints must return standard Python dicts/lists or Pydantic models, not f-strings or raw strings.

## Test Generation Rules
* **Framework:** Use `pytest` for all tests.
* **Structure:** Keep tests under `tests/` with `tests/unit/` for unit tests and `tests/integration/` for API/endpoint tests.
* **File naming:** Use `test_<module>.py` (e.g., `app/main.py` -> `tests/unit/test_main.py` and `tests/integration/test_main.py`).
* **Function naming:** Use `test_<target>_<expected_behavior>`.
* **Fixtures:** Reuse fixtures from `tests/conftest.py` (`app`, `client`, `db_session`, `auth_token`) instead of redefining them.
* **Integration marks:** Mark integration tests with `@pytest.mark.integration` and async tests with `@pytest.mark.asyncio`.
* **Coverage expectations:** Cover happy path, validation failures (`422`), and explicit error conditions (e.g., `404`) for endpoints.
* **Model-aware assertions:** For API responses, validate response shapes against the fields defined in `app/models.py`.