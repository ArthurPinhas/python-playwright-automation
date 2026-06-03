import pytest
import os
from playwright.sync_api import Page, Playwright
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
    }

@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    context = playwright.request.new_context(base_url=os.getenv("API_BASE_URL"))
    yield context
    context.dispose()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page: Page = item.funcargs.get("page")
        if page:
            os.makedirs("reports", exist_ok=True)
            page.screenshot(path=f"reports/{item.name}.png")
