from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CheckoutOverviewPage(BasePage):
    ITEM_TOTAL_LOCATOR = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_LOCATOR = (By.CLASS_NAME, "summary_tax_label")
    SUM_TOTAL_LOCATOR = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON_LOCATOR = (By.ID, "finish")

    def __init__(self, driver):
        super().__init__(driver)

    def get_item_total(self):
        item_total = self.get_text(self.ITEM_TOTAL_LOCATOR)
        return float(item_total.split("$")[1])

    def get_tax(self):
        tax_total = self.get_text(self.TAX_LOCATOR)
        return float(tax_total.split("$")[1])

    def get_sum_total(self):
        sum_total = self.get_text(self.SUM_TOTAL_LOCATOR)
        return float(sum_total.split("$")[1])
    def finish(self):
        self.click(self.FINISH_BUTTON_LOCATOR)