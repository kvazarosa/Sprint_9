from random import randint


class Urls:
    HOME_PAGE_URL = "https://foodgram-frontend-1.prakticum-team.ru/"
    LOGIN_PAGE_URL = f"{HOME_PAGE_URL}signin"
    RECIPES_PAGE_URL = f"{HOME_PAGE_URL}recipes"


class TestData:
    VALID_EMAIL = "kvazarosa3344@yandex.com"
    VALID_PASSWORD = "135798642poiu"
    VALID_NAME = "Иннокентий"
    VALID_LASTNAME = "Продольный"
    VALID_USERNAME = "kvazarosa"

    # Данные для создания рецепта
    RECIPE_NAME = "Картопляник"
    INGREDIENT_NAME = "картофель молодой"
    INGREDIENT_WEIGHT = "500"
    COOKING_TIME = "60"
    RECIPE_DESCRIPTION = "Варить до готовности"

    @staticmethod
    def get_random_email():
        return f"kvazarosa{randint(1000, 9999)}@yandex.com"

    @staticmethod
    def get_random_username():
        return f"user{randint(1000, 9999)}"

    @staticmethod
    def get_simple_password():
        return f"Qwerty{randint(1000, 9999)}ytrewQ"
