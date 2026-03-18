---
agent: ask
description: Generate unit and integration tests for selected FastAPI code using repository rules
---
Generate tests for the current selection or referenced symbol using the repository test standards.

Requirements:
1. Use `pytest`.
2. Put unit tests in `tests/unit/test_<module>.py` and integration tests in `tests/integration/test_<module>.py`.
3. Reuse fixtures from `tests/conftest.py` (`app`, `client`, `db_session`, `auth_token`).
4. Integration tests must use `@pytest.mark.asyncio` and `@pytest.mark.integration`.
5. Name tests as `test_<target>_<expected_behavior>`.
6. For endpoints, include:
   - happy path assertions
   - validation failures (`422`)
   - explicit error conditions (`404` when applicable)
7. Assert response JSON fields against models defined in `app/models.py`.
8. Keep tests deterministic and avoid shared mutable-state leaks between tests.
9. Return only test code edits (no prose) and keep changes scoped to `tests/` unless configuration updates are strictly required.
