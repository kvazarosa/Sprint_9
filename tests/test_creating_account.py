import allure
from data import TestData
from pages.creating_account_page import CreatingAccountPage


class TestAccountRegistration:
    @allure.title("Проверка успешного создания аккаунта")
    @allure.description("Тест проверяет возможность регистрации нового пользователя")
    def test_successful_account_creation(self, driver):
        page = CreatingAccountPage(driver)
        random_email = TestData.get_random_email()
        random_username = TestData.get_random_username()
        random_password = TestData.get_simple_password()

        with allure.step("Открытие формы регистрации"):
            page.open_registration_form()
        with allure.step("Заполнение формы регистрации"):
            page.fill_registration_form(
                name=TestData.VALID_NAME,
                lastname=TestData.VALID_LASTNAME,
                username=random_username,
                email=random_email,
                password=random_password
            )
        with allure.step("Отправка формы регистрации"):
            page.submit_registration()

        with allure.step("Проверка URL после регистрации"):
            current_url = page.get_current_url()
            assert "signup" in current_url
        with allure.step("Проверка отображения кнопки входа"):
            assert page.is_login_button_displayed()
