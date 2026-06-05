import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from test_data.credentials import USERNAME, PASSWORD, INVENTORY_URL

@pytest.mark.regression
@pytest.mark.smoke
def test_login_page_loads(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    expect(login_page.page).to_have_title("Swag Labs")

@pytest.mark.regression
@pytest.mark.smoke
def test_login_with_valid_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(USERNAME, PASSWORD)
    expect(page).to_have_url(INVENTORY_URL)

@pytest.mark.regression
@pytest.mark.parametrize("username,password,expected_error", [
("", "secret_sauce", "Epic sadface: Username is required"),
("standard_user", "", "Epic sadface: Password is required"),
("wrong_user", "wrong_pass", "Epic sadface: Username and password do not match any user in this service")
])

def test_invalid_login_parametrized(page: Page, username: str, password: str, expected_error: str):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(username, password)
    expect(page.locator(login_page.error_message)).to_contain_text(expected_error)