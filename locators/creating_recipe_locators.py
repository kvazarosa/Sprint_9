from selenium.webdriver.common.by import By


class CreateRecipeLocators:
    BUTTON_CREATE_RECIPE_UP = (By.XPATH, "//a[contains(@class, 'style_nav__link__2rAY6') and text()='Создать рецепт']")
    BUTTON_ADD_INGREDIENT = (By.XPATH, "//div[contains(@class, 'styles_ingredientAdd__3fc32') and text()='Добавить ингредиент']")
    FIELD_RECIPE_NAME = (By.XPATH, "//div[contains(@class, 'styles_inputLabelText__WsyhD') and text()='Название рецепта']/following-sibling::input")
    FIELD_INGREDIENT_NAME = (By.XPATH, "//input[contains(@class, 'styles_inputField__3eqTj') and contains(@class, 'styles_ingredientsInput__1zzql')]")
    FIELD_INGREDIENT_WEIGHT = (By.XPATH, "//input[contains(@class, 'ingredientsAmountValue')]")
    FIELD_COOKING_TIME = (By.XPATH, "//div[contains(@class, 'cookingTimeLabel') and contains(text(), 'Время приготовления')]/following-sibling::input")
    FIELD_RECIPE_DESCRIPTION = (By.CSS_SELECTOR, "textarea.styles_textareaField__1wfhC")
    FILE_UPLOAD_INPUT = (By.CSS_SELECTOR, "input[type='file'].styles_fileInput__3HjP3")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[contains(@class, 'style_button__1FFWl') and text()='Создать рецепт']")
    RECIPE_NAME_ON_PAGE = (By.CSS_SELECTOR, "h1.styles_single-card__title__2QMPq")
    INGREDIENT_DROPDOWN = (By.CSS_SELECTOR, "div.styles_container__3ukwm")
    INGREDIENT_OPTION = (By.XPATH, "//div[contains(@class, 'styles_container__3ukwm')]/div[contains(., 'картофель молодой')]")

    # селекторы для авторизации
    BUTTON_ENTER_UP = (By.CSS_SELECTOR, "a.style_link__1kPh8.styles_menuLink__3a59I")
    BUTTON_ENTER_DOWN = (By.XPATH, "//button[contains(@class, 'style_button_style_dark-blue__1cpq7') and text()='Войти']")
    FIELD_EMAIL_ADDRESS = (By.XPATH, "//input[@name='email']")
    FIELD_PASSWORD = (By.XPATH, "//input[@name='password']")
    BUTTON_EXIT = (By.XPATH, "//a[contains(@class, 'styles_menuLink__3a59I') and text()='Выход']")
