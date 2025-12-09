from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def count_items(self):
        try:
            items = self.driver.find_elements(*self.CART_ITEMS)
            return len(items)
        except:
            return 0
