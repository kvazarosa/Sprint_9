import allure
from data import Urls, TestData
from pages.authorization_page import AuthorizationPage


class TestAuthorization:
    @allure.title("Проверка успешной авторизации")
    @allure.description("Тест проверяет возможность входа в систему с валидными учетными данными")
    def test_successful_login(self, driver):
        auth_page = AuthorizationPage(driver)
        with allure.step("Ввод email"):
            auth_page.enter_email(TestData.VALID_EMAIL)
        with allure.step("Ввод пароля"):
            auth_page.enter_password(TestData.VALID_PASSWORD)
        with allure.step("Нажатие кнопки входа"):
            auth_page.click_login_button()
        with allure.step("Ожидание кнопки выхода"):
            auth_page.wait_for_logout_button()
        with allure.step("Проверка URL после входа"):
            current_url = auth_page.get_current_url()
            assert current_url == Urls.RECIPES_PAGE_URL
        with allure.step("Проверка видимости кнопки выхода"):
            assert auth_page.is_logout_button_visible()
            
