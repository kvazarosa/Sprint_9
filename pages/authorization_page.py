from pages.base_page import BasePage
from locators.authorization_locators import AuthorizationLocators


class AuthorizationPage(BasePage):
    def enter_email(self, email):
        self.input_text(AuthorizationLocators.FIELD_EMAIL_ADDRESS, email)

    def enter_password(self, password):
        self.input_text(AuthorizationLocators.FIELD_PASSWORD, password)

    def click_login_button(self):
        self.click_element(AuthorizationLocators.BUTTON_ENTER_DOWN)

    def is_logout_button_visible(self):
        return self.is_element_displayed(AuthorizationLocators.BUTTON_EXIT)

    def wait_for_logout_button(self):
        return self.element_is_visible(AuthorizationLocators.BUTTON_EXIT)
