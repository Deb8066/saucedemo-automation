
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductPage
from testdata.saucedemo_data import VALID_USER, PRODUCT_SETS


@pytest.mark.parametrize("products", PRODUCT_SETS)
def test_add_products_to_cart(driver, products):

    login_page = LoginPage(driver)
    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"]
    )

    product_page = ProductPage(driver)
    product_page.add_multiple_products_to_cart(products)

    assert product_page.get_cart_badge_count() == len(products)
