
# testdata/saucedemo_data.py

# ---------- Login Data ----------
VALID_USER = {
    "username": "standard_user",
    "password": "secret_sauce"
}

# ---------- Invalid Login ----------
INVALID_USER = {
    "username": "locked_out_user",
    "password": "secret_sauce"
}

LOGIN_ERROR_MESSAGE = "Epic sadface"

# ---------- Products ----------
PRODUCTS_TO_ADD = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light"
]

PRODUCT_SETS = [
    ["Sauce Labs Backpack"],
    ["Sauce Labs Bike Light"],
    ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
]

PRODUCT_TO_REMOVE = "Sauce Labs Bike Light"

# ---------- Checkout User ----------
CHECKOUT_USER = {
    "first_name": "John",
    "last_name": "Doe",
    "zip_code": "12345"
}

# ---------- Success Message ----------
ORDER_SUCCESS_TEXT = "THANK YOU FOR YOUR ORDER"
