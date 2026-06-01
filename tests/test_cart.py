from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from test_data.credentials import USERNAME, PASSWORD, INVENTORY_URL

def test_add_item_to_cart(page: Page):
    # Login first
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(USERNAME, PASSWORD) 
    expect(page).to_have_url(INVENTORY_URL)
    inventory_page = InventoryPage(page)
    # Add an item to the cart
    inventory_page.add_to_cart("Sauce Labs Backpack")
    # Verify the cart count is updated
    assert inventory_page.get_cart_count() == "1"
