from LoginPages import SearchHelper
from data import *


def test_log_in_invalid_data(browser):
    logging_page = SearchHelper(browser)
    logging_page.go_to_site()
    logging_page.enter_email_or_username(EMAIL)
    logging_page.press_submit_button()
    error = logging_page.read_error_response()
    assert error == EXPECTED_ERROR_LOGIN_RESULT


def test_log_in_enter_nothing(browser):
    logging_page = SearchHelper(browser)
    logging_page.go_to_site()
    logging_page.press_submit_button()
    error = logging_page.read_error_response()
    assert error == EXPECTED_NOT_ENTERED_LOGIN_RESULT


def test_log_in_account_found(browser):
    logging_page = SearchHelper(browser)
    logging_page.go_to_site()
    logging_page.enter_email_or_username(USERNAME)
    logging_page.press_submit_button()
    account = logging_page.read_found_account()
    assert account == USERNAME


def test_log_in_wrong_password(browser):
    logging_page = SearchHelper(browser)
    logging_page.go_to_site()
    logging_page.enter_email_or_username(USERNAME)
    logging_page.press_submit_button()
    account = logging_page.read_found_account()
    assert account == USERNAME
    logging_page.enter_password(WRONG_PASSWORD)
    logging_page.press_submit_button()
    error = logging_page.read_error_response()
    assert error == EXPECTED_INCORRECT_PASSWORD


def test_loging(browser):
    logging_page = SearchHelper(browser)
    logging_page.go_to_site()
    logging_page.enter_email_or_username(USERNAME)
    logging_page.press_submit_button()
    account = logging_page.read_found_account()
    assert account == USERNAME
    logging_page.enter_password(PASSWORD)
    logging_page.press_submit_button()
    text = logging_page.read_welcome_text()
    assert text == EXPECTED_TEXT
