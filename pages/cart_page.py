from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CartPage(BasePage):
    REMOVE_ITEM_TEMPLATE = ("//div[text()='{}']"
                            "/ancestor::div[contains(@class, 'cart_item')]//button")
    CHECKOUT = (By.ID, "checkout")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        super().__init__(driver)

    def remove_item_from_cart(self, product_name):
        locator = (By.XPATH, self.REMOVE_ITEM_TEMPLATE.format(product_name))
        self.click(locator)

    def item_count_on_cart(self):
        if self.is_element_visible(self.SHOPPING_CART_BADGE):
            return int(self.get_text(self.SHOPPING_CART_BADGE))
        return 0

    def checkout(self):
        self.click(self.CHECKOUT)
