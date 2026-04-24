from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRSTNAME_LOCATOR = (By.ID, "first-name")
    LASTNAME_LOCATOR = (By.ID, "last-name")
    ZIPCODE_LOCATOR = (By.ID, "postal-code")
    CONTINUE_LOCATOR = (By.ID, "continue")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_checkout_details(self, firstname, lastname, zipcode):
        self.enter_text(self.FIRSTNAME_LOCATOR, firstname)
        self.enter_text(self.LASTNAME_LOCATOR, lastname)
        self.enter_text(self.ZIPCODE_LOCATOR, zipcode)
        self.click(self.CONTINUE_LOCATOR)

    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
