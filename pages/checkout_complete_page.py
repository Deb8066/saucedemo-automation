from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    MESSAGE_LOCATOR = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        super().__init__(driver)

    def get_success_message(self):
        return self.get_text(self.MESSAGE_LOCATOR)