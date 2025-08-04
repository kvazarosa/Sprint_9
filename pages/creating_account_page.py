from data import Urls
from pages.base_page import BasePage
from locators.creating_account_locators import CreatingAccountLocators


class CreatingAccountPage(BasePage):
    def click_create_account_button(self):
        self.click_element(CreatingAccountLocators.BUTTON_CREATE_ACCOUNT_UP)
        return self

    def click_submit_button(self):
        self.click_element(CreatingAccountLocators.BUTTON_CREATE_ACCOUNT_DOWN)
        return self

    def open_registration_form(self):
        self.driver.get(Urls.HOME_PAGE_URL)
        self.click_create_account_button()
        return self

    def fill_registration_form(self, name, lastname, username, email, password):
        self.input_text(CreatingAccountLocators.FIELD_NAME, name)
        self.input_text(CreatingAccountLocators.FIELD_LASTNAME, lastname)
        self.input_text(CreatingAccountLocators.FIELD_USERNAME, username)
        self.input_text(CreatingAccountLocators.FIELD_EMAIL_ADDRESS, email)
        self.input_text(CreatingAccountLocators.FIELD_PASSWORD, password)
        return self

    def submit_registration(self):
        self.click_submit_button()
        return self

    def is_login_button_displayed(self):
        return self.element_is_visible(CreatingAccountLocators.BUTTON_ENTER_DOWN).is_displayed()

    def is_authorization_form_displayed(self):
        return self.is_login_button_displayed()
