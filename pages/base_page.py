from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def element_is_visible(self, locator, timeout=15):
        """Ожидает появление видимого элемента с добавлением диагностики"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except Exception as e:
            # Диагностика при ошибке
            print(f"\n--- Ошибка при поиске элемента {locator} ---")
            print(f"URL страницы: {self.driver.current_url}")
            print(f"Текущий HTML (первые 2000 символов):\n{self.driver.page_source[:2000]}")
            
            # Сохраняем скриншот
            screenshot_path = "element_not_found.png"
            self.driver.save_screenshot(screenshot_path)
            print(f"Скриншот сохранен: {screenshot_path}")
            
            raise  # Перебрасываем исключение дальше


    def element_is_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.element_is_visible(locator).click()

    def input_text(self, locator, text):
        element = self.element_is_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def is_element_displayed(self, locator):
        return self.element_is_visible(locator).is_displayed()

    def wait_and_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
