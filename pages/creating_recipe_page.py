import time
import os
from pages.base_page import BasePage
from locators.creating_recipe_locators import CreateRecipeLocators
from pathlib import Path
from selenium.webdriver.support import expected_conditions as EC

class AuthorizationPage(BasePage):
    def enter_email(self, email):
        self.input_text(CreateRecipeLocators.FIELD_EMAIL_ADDRESS, email)

    def enter_password(self, password):
        self.input_text(CreateRecipeLocators.FIELD_PASSWORD, password)

    def click_login_button(self):
        self.click_element(CreateRecipeLocators.BUTTON_ENTER_DOWN)

    def wait_for_logout_button(self):
        return self.element_is_visible(CreateRecipeLocators.BUTTON_EXIT)


class CreateRecipePage(BasePage):
    def click_create_recipe_button(self):
        self.click_element(CreateRecipeLocators.BUTTON_CREATE_RECIPE_UP)

    def enter_recipe_name(self, name):
        self.input_text(CreateRecipeLocators.FIELD_RECIPE_NAME, name)

    def enter_ingredient_name(self, name):
        ingredient_input = self.wait.until(EC.element_to_be_clickable(CreateRecipeLocators.FIELD_INGREDIENT_NAME))
        ingredient_input.click()
        partial_name = "картофель мол"
        for char in partial_name:
            ingredient_input.send_keys(char)
            time.sleep(0.15)
        dropdown = self.wait.until(EC.visibility_of_element_located(CreateRecipeLocators.INGREDIENT_DROPDOWN))
        option = self.wait.until(EC.element_to_be_clickable(CreateRecipeLocators.INGREDIENT_OPTION))
        self.driver.execute_script("arguments[0].click();", option)

    def enter_ingredient_weight(self, weight):
        self.input_text(CreateRecipeLocators.FIELD_INGREDIENT_WEIGHT, weight)

    def click_add_ingredient_button(self):
        self.click_element(CreateRecipeLocators.BUTTON_ADD_INGREDIENT)

    def enter_cooking_time(self, time):
        self.input_text(CreateRecipeLocators.FIELD_COOKING_TIME, time)

    def enter_recipe_description(self, description):
        self.input_text(CreateRecipeLocators.FIELD_RECIPE_DESCRIPTION, description)

    # def upload_recipe_image(self):
    #     file_path = Path(__file__).parent.parent.parent / "assets" / "картинка.png"
    #     self.element_is_present(CreateRecipeLocators.FILE_UPLOAD_INPUT).send_keys(str(file_path))
    #     return file_path
    def upload_recipe_image(self):
        # Для CI используем /tmp, для локального тестирования - assets
        if os.getenv('CI'):
            file_path = Path('/tmp/картинка.png')
        else:
            file_path = Path(__file__).parent.parent.parent / "assets" / "картинка.png"
        
        self.element_is_present(CreateRecipeLocators.FILE_UPLOAD_INPUT).send_keys(str(file_path))
        return file_path

    def click_create_recipe_final_button(self):
        self.click_element(CreateRecipeLocators.CREATE_RECIPE_BUTTON)

    def is_recipe_name_displayed(self):
        return self.is_element_displayed(CreateRecipeLocators.RECIPE_NAME_ON_PAGE)
