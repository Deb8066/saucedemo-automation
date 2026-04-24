from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class ProductPage(BasePage):
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    ADD_TO_CART_TEMPLATE = ("//div[text()='{}']"
                            "/ancestor::div[contains(@class, 'inventory_item')]//button")

    PRICE_XPATH = (
        "//div[text()='{}']"
        "/ancestor::div[contains(@class,'inventory_item')]"
        "//div[contains(@class,'inventory_item_price')]")

    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart(self, product_name):
        add_button = (By.XPATH, self.ADD_TO_CART_TEMPLATE.format(product_name))
        self.click(add_button)

    def add_multiple_products_to_cart(self, products_names):

        for product in products_names:
            self.add_product_to_cart(product)

    def product_price(self, product_name):
        price_locator = (By.XPATH,self.PRICE_XPATH.format(product_name))
        price_text =self.get_text(price_locator)
        return float(price_text.replace("$", ""))

    def get_cart_badge_count(self):
        """
        Returns the cart badge count as int
        """
        if self.is_element_visible(self.SHOPPING_CART_BADGE):
            return int(self.get_text(self.SHOPPING_CART_BADGE))
        return 0

    def go_to_cart(self):
        """
        Navigates to cart page
        """
        self.click(self.SHOPPING_CART)


