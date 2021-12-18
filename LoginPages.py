from BaseApp import BasePage
from selenium.webdriver.common.by import By


class LoginSearchLocators:
    LOCATOR_EMAIL_USERNAME_FIELD = (By.ID, "UsernameOrEmail")
    LOCATOR_PASSWORD_FIELD = (By.ID, "Password")
    LOCATOR_SUBMIT_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    LOCATOR_ERROR_RESPONSE_FIELD = (By.CLASS_NAME, "field-message-error")
    LOCATOR_FOUND_ACCOUNT = (By.CLASS_NAME, "user-username")
    LOCATOR_LOGGED_IN_ACCOUNT = (By.CLASS_NAME, "dashboard-account-username")


class SearchHelper(BasePage):

    def enter_email_or_username(self, word):
        search_field = self.find_element(LoginSearchLocators.LOCATOR_EMAIL_USERNAME_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def press_submit_button(self):
        return self.find_element(LoginSearchLocators.LOCATOR_SUBMIT_BUTTON).click()

    def enter_password(self, password):
        search_field = self.find_element(LoginSearchLocators.LOCATOR_PASSWORD_FIELD)
        search_field.click()
        search_field.send_keys(password)
        return search_field

    def read_error_response(self):
        return self.find_element(LoginSearchLocators.LOCATOR_ERROR_RESPONSE_FIELD).text

    def read_found_account(self):
        return self.find_element(LoginSearchLocators.LOCATOR_FOUND_ACCOUNT).text

    def read_welcome_text(self):
        return self.find_element(LoginSearchLocators.LOCATOR_LOGGED_IN_ACCOUNT).text
