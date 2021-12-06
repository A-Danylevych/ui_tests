from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from constants import *


class UITester(object):
    def __init__(self, time_to_wait=30):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(time_to_wait)

    def __go_to(self, url: str):
        self.browser.get(url)

    def __click(self, selector: str):
        element = self.browser.find_element(By.CSS_SELECTOR, selector)
        self.browser.execute_script("arguments[0].click();", element)

    def __write(self, selector: str, text: str):
        self.browser.find_element(By.CSS_SELECTOR, selector).send_keys(text)

    def __press_enter(self, selector: str):
        self.browser.find_element(By.CSS_SELECTOR, selector).send_keys(Keys.RETURN)

    def __get(self, selector: str):
        return self.browser.find_element(By.CSS_SELECTOR, selector).text

    @staticmethod
    def __check(actual, expected):
        assert actual == expected

    def test_log_in_invalid_data(self):
        self.__go_to(LOGIN_URL)
        self.__click(LOGIN_INPUT_ID)
        self.__write(LOGIN_INPUT_ID, EMAIL)
        self.__press_enter(LOGIN_INPUT_ID)
        result = self.__get(RESPONSE_FIELD)
        self.__check(result, EXPECTED_ERROR_LOGIN_RESULT)

    def test_log_in_enter_nothing(self):
        self.__go_to(LOGIN_URL)
        self.__click(LOGIN_INPUT_ID)
        self.__press_enter(LOGIN_INPUT_ID)
        result = self.__get(RESPONSE_FIELD)
        self.__check(result, EXPECTED_NOT_ENTERED_LOGIN_RESULT)

    def test_log_in_account_found(self):
        self.__go_to(LOGIN_URL)
        self.__click(LOGIN_INPUT_ID)
        self.__write(LOGIN_INPUT_ID, USERNAME)
        self.__press_enter(LOGIN_INPUT_ID)
        result = self.__get(USER_NAME_ID)
        self.__check(result, USERNAME)

    def test_log_in_wrong_password(self):
        self.test_log_in_account_found()
        self.__click(PASSWORD_ID)
        self.__write(PASSWORD_ID, WRONGPASSWORD)
        self.__press_enter(PASSWORD_ID)
        result = self.__get(RESPONSE_FIELD)
        self.__check(result, EXPECTED_INCORRECT_PASSWORD)

    def test_loging(self):
        self.test_log_in_account_found()
        self.__click(PASSWORD_ID)
        self.__write(PASSWORD_ID, PASSWORD)
        self.__press_enter(PASSWORD_ID)
        result = self.__get(WELLCOME_CLASS)
        self.__check(result, EXPECTED_TEXT)


tester = UITester(TIME_TO_WAIT)
tester.test_log_in_enter_nothing()
tester.test_log_in_invalid_data()
tester.test_log_in_account_found()
tester.test_log_in_wrong_password()
tester.test_loging()
