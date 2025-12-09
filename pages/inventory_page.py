from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, 'title')
    ADD_FIRST = (By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')

    def title_text(self):
        return self.get_text(self.TITLE)

    def add_first_item(self):
        self.click(self.ADD_FIRST)

    def cart_count(self):
        try:
            return int(self.get_text(self.CART_BADGE))
        except Exception:
            return 0

    def go_to_cart(self):
        self.click(self.CART_LINK)


