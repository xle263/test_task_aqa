from selene import browser
from selene.support.conditions import have


class LoginPage:
    URL = 'https://crop-monitoring.eos.com/login'
    CONFIRM_URL = 'https://crop-monitoring.eos.com/login/confirm'
    AUTH_URL = 'https://crop-monitoring.eos.com/login/auth'
    MAIN_MAP_URL = 'https://crop-monitoring.eos.com/main-map'
    EMAIL = 'input[data-id="email"]'
    FIRST_NAME = 'input[data-id="first_name"]'
    LAST_NAME = 'input[data-id="last_name"]'
    PASSWORD = 'input[data-id="password"]'
    SIGN_UP_BUTTON = '[data-id="sign-up-btn"]'
    SIGN_IN_BUTTON = '[data-id="sign-in-btn"]'
    CHECKBOX = '.mat-checkbox-inner-container'
    LOGIN_TOGGLER = '[data-id="sign-in-button"]'
    USERNAME = 'div .full-user-name'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        browser.open_url(self.URL)
        return self

    def type_email(self, email: str):
        browser.element(self.EMAIL).type(email)
        return self

    def type_first_name(self, first_name: str):
        browser.element(self.FIRST_NAME).type(first_name)
        return self

    def type_last_name(self, last_name: str):
        browser.element(self.LAST_NAME).type(last_name)
        return self

    def type_password(self, password: str):
        browser.element(self.PASSWORD).type(password)
        return self

    def submit_privacy_agreement(self):
        browser.element(self.CHECKBOX).click()
        return self

    def click_on_registration_button(self):
        browser.element(self.SIGN_UP_BUTTON).click()
        return self

    def check_confirm_registration_page_loaded(self):
        browser.wait_to(have.url_containing(self.CONFIRM_URL), timeout=10)

    def switch_to_login(self):
        browser.element(self.LOGIN_TOGGLER).click()

    def wait_till_auth_page_loaded(self):
        browser.wait_to(have.url_containing(self.AUTH_URL), timeout=10)

    def click_on_login_button(self):
        browser.element(self.SIGN_IN_BUTTON).click()
        return self

    def wait_till_main_page_loaded(self):
        browser.wait_to(have.url_containing(self.MAIN_MAP_URL), timeout=10)

    def username_is(self, username):
        browser.element(self.USERNAME).should(have.exact_text(username))
        return self
