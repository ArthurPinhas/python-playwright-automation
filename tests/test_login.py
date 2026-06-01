from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from test_data.credentials import USERNAME, PASSWORD, INVENTORY_URL

def test_login_page_loads(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    expect(login_page.page).to_have_title("Swag Labs")

def test_login_with_valid_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(USERNAME, PASSWORD)
    expect(page).to_have_url(INVENTORY_URL)

def test_login_with_invalid_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("invalid_user", "invalid_pass")
    expect(page.locator(login_page.error_message)).to_be_visible()