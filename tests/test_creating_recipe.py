import allure
from data import TestData
from locators.creating_recipe_locators import CreateRecipeLocators
from pages.creating_recipe_page import AuthorizationPage, CreateRecipePage


@allure.title("Проверка создания рецепта")
@allure.description("Тест проверяет возможность создания нового рецепта")
def test_create_recipe(driver):
    # Авторизация
    auth_page = AuthorizationPage(driver)
    with allure.step("Открытие формы авторизации"):
        auth_page.click_element(CreateRecipeLocators.BUTTON_ENTER_UP)
    with allure.step("Ввод email"):
        auth_page.enter_email(TestData.VALID_EMAIL)
    with allure.step("Ввод пароля"):
        auth_page.enter_password(TestData.VALID_PASSWORD)
    with allure.step("Нажатие кнопки входа"):
        auth_page.click_login_button()
    with allure.step("Проверка успешной авторизации"):
        assert auth_page.wait_for_logout_button().is_displayed()

    # Создание рецепта
    create_page = CreateRecipePage(driver)
    with allure.step("Открытие формы создания рецепта"):
        create_page.click_create_recipe_button()
    with allure.step("Ввод названия рецепта"):
        create_page.enter_recipe_name(TestData.RECIPE_NAME)
    with allure.step("Выбор ингредиента"):
        create_page.enter_ingredient_name(TestData.INGREDIENT_NAME)
    with allure.step("Ввод количества ингредиента"):
        create_page.enter_ingredient_weight(TestData.INGREDIENT_WEIGHT)
    with allure.step("Добавление ингредиента"):
        create_page.click_add_ingredient_button()
    with allure.step("Ввод времени приготовления"):
        create_page.enter_cooking_time(TestData.COOKING_TIME)
    with allure.step("Ввод описания рецепта"):
        create_page.enter_recipe_description(TestData.RECIPE_DESCRIPTION)
    with allure.step("Загрузка изображения"):
        create_page.upload_recipe_image()
    with allure.step("Создание рецепта"):
        create_page.click_create_recipe_final_button()
    with allure.step("Проверка отображения названия рецепта"):
        assert create_page.is_recipe_name_displayed()
