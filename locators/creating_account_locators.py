from selenium.webdriver.common.by import By


class CreatingAccountLocators:
    BUTTON_CREATE_ACCOUNT_UP = (By.CSS_SELECTOR, "a.style_link__1kPh8.styles_menuButton__1RUEF")
    BUTTON_CREATE_ACCOUNT_DOWN = (By.CSS_SELECTOR, "button.style_button__1FFWl.styles_button__146Sy.style_button_style_dark-blue__1cpq7")
    FIELD_NAME = (By.XPATH, "//input[@type='text' and @name='first_name']")
    FIELD_LASTNAME = (By.XPATH, "//input[@type='text' and @name='last_name']")
    FIELD_USERNAME = (By.XPATH, "//input[@name='username']")
    FIELD_EMAIL_ADDRESS = (By.XPATH, "//input[@name='email']")
    FIELD_PASSWORD = (By.XPATH, "//input[@name='password']")

    FIELD_EMAIL_AUTHORIZATION = (By.XPATH, "//input[contains(@class, 'inputField')]")
    BUTTON_ENTER_DOWN = (By.XPATH, "//button[contains(@class, 'style_button_style_dark-blue__1cpq7') and text()='Войти']")
