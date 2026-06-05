![CI](https://github.com/ArthurPinhas/python-playwright-automation/actions/workflows/ci.yml/badge.svg)

# Python Playwright Automation

End-to-end test automation framework built with Python, pytest, and Playwright.
Covers web UI flows and REST API testing against SauceDemo and JSONPlaceholder.
Follows Page Object Model architecture with GitHub Actions CI.

## Setup
```bash
pip install -r requirements.txt
python -m playwright install chromium
```

## Run Tests
```bash
# Full suite
python -m pytest tests/ -v

# Smoke tests only
python -m pytest -m smoke -v

# Regression suite
python -m pytest -m regression -v
```

## Project Structure
- `pages/` — Page Object classes (LoginPage, InventoryPage)
- `tests/` - Test specs (login, cart, API)
- `test_data/` — Credentials and constants
- `conftest.py` — Fixtures and browser config
- `pytest.ini` — Markers and test configuration

## Test Coverage
| Test | Type | Marker |
|------|------|--------|
| Login page loads | UI | smoke, regression |
| Valid login | UI | smoke, regression |
| Invalid login (3 scenarios) | UI | regression |
| Add item to cart | UI | smoke, regression |
| GET users | API | regression |
| POST create user | API | smoke, regression |
| DELETE user | API | regression |