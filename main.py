from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from constants import *


class UITester(object):
    def __init__(self, time_to_wait=30):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.implicitly_wait(time_to_wait)

    def __go_to(self, url: str):
        self.browser.get(url)

    def __click(self, selector: str):
        self.browser.find_element(By.CSS_SELECTOR, selector).click()

    def __write(self, selector: str, text: str):
        self.browser.find_element(By.CSS_SELECTOR, selector).send_keys(text)

    def __fullscreen(self):
        self.browser.fullscreen_window()

    def __press_enter(self, selector: str):
        self.browser.find_element(By.CSS_SELECTOR, selector).send_keys(Keys.ENTER)

    def __get(self, selector: str):
        return self.browser.find_element(By.CSS_SELECTOR, selector).text

    def __get_last_by_tag(self, tag: str):
        return self.browser.find_elements(By.TAG_NAME, tag).pop().text

    @staticmethod
    def __check(actual, expected):
        assert actual == expected

    def test_rozklad(self):
        self.__go_to(ROZKLAD_URL)
        self.__click(ROZKLAD_SEARCH_SELECTOR_ID)
        self.__write(ROZKLAD_SEARCH_SELECTOR_ID, GROUP)
        self.__press_enter(ROZKLAD_SEARCH_SELECTOR_ID)
        result = self.__get(ROZKLAD_RESULT_SELECTOR_ID)
        self.__check(result, EXPECTED_RESULT)

    def test_session(self):
        self.__go_to(ROZKLAD_URL)
        self.__click(ROZKLAD_SESSION_SELECTOR_ID)
        self.__click(ROZKLAD_SEARCH_SELECTOR_ID)
        self.__write(ROZKLAD_SEARCH_SELECTOR_ID, GROUP)
        self.__press_enter(ROZKLAD_SEARCH_SELECTOR_ID)
        result = self.__get_last_by_tag(SESSION_TAG)
        self.__check(result, EXPECTED_SESSION_RESULT)


tester = UITester(TIME_TO_WAIT)
tester.test_rozklad()
tester.test_session()
