import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from testdata.saucedemo_data import VALID_USER, PRODUCT_SETS

from testdata.saucedemo_data import (
    VALID_USER,
    PRODUCTS_TO_ADD,
    PRODUCT_TO_REMOVE,
    CHECKOUT_USER,
    ORDER_SUCCESS_TEXT
)

def test_saucedemo_end_to_end(driver):

  # ---------- Login ----------
    login_page = LoginPage(driver)
    login_page.login(VALID_USER['username'], VALID_USER["password"])
    # ---------- Add Products ----------
    product_page = ProductPage(driver)
    product_page.add_multiple_products_to_cart(PRODUCTS_TO_ADD)
    product_page.go_to_cart()

    # ---------- Cart Badge Validation ---------
    assert product_page.get_cart_badge_count() == len(PRODUCTS_TO_ADD)
    # ---------- Cart Validation ---------
    cart_page = CartPage(driver)
    cart_page.remove_item_from_cart(PRODUCT_TO_REMOVE)
    assert product_page.get_cart_badge_count() == len(PRODUCTS_TO_ADD)-1
    cart_page.checkout()
    # ---------- Checkout: User Details ----------
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_checkout_details(
        CHECKOUT_USER["first_name"],
        CHECKOUT_USER["last_name"],
        CHECKOUT_USER["zip_code"])
    #-------------Checkout:Overview-----------------
    checkout_overview_page = CheckoutOverviewPage(driver)
    item_total= checkout_overview_page.get_item_total()
    tax = checkout_overview_page.get_tax()
    total = checkout_overview_page.get_sum_total()
    assert item_total + tax == total
    checkout_overview_page.finish()
    # ------------------Order Success---------------------------
    checkout_complete = CheckoutCompletePage(driver)
    message_text = checkout_complete.get_success_message()
    assert ORDER_SUCCESS_TEXT in message_text.upper()

