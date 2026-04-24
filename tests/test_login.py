
import pytest
from pages.login_page import LoginPage
from testdata.saucedemo_data import INVALID_USER, LOGIN_ERROR_MESSAGE


@pytest.mark.smoke
def test_login_with_invalid_user_shows_error(driver):
    login_page = LoginPage(driver)

    login_page.login(
        INVALID_USER["username"],
        INVALID_USER["password"]
    )

    error_message = login_page.get_error_message()
    assert LOGIN_ERROR_MESSAGE in error_message
