from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = ".shopping_cart_link"
        self.cart_icon_count = ".shopping_cart_badge"
        self.add_to_cart_button = ".btn_inventory"

    def get_cart_count(self) -> str:
        return self.page.locator(self.cart_icon_count).inner_text()

    def go_to_cart(self):
        self.page.click(self.cart_icon)

    def add_to_cart(self, item_name: str):
        item_locator = f".inventory_item:has-text('{item_name}') {self.add_to_cart_button}"
        self.page.click(item_locator)