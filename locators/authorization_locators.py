from selenium.webdriver.common.by import By


class AuthorizationLocators:
    BUTTON_CREATE_ACCOUNT_UP = (By.CSS_SELECTOR, "a.style_link__1kPh8.styles_menuButton__1RUEF")
    BUTTON_ENTER_UP = (By.CSS_SELECTOR, "a.style_link__1kPh8.styles_menuLink__3a59I")
    BUTTON_ENTER_DOWN = (By.XPATH, "//button[contains(@class, 'style_button_style_dark-blue__1cpq7') and text()='Войти']")
    FIELD_EMAIL_ADDRESS = (By.XPATH, "//input[@name='email']")
    FIELD_PASSWORD = (By.XPATH, "//input[@name='password']")

    BUTTON_EXIT = (By.XPATH, "//a[contains(@class, 'styles_menuLink__3a59I') and text()='Выход']")
