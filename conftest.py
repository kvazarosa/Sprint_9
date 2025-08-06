import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture(scope="function")
def driver():
    options = Options()
    
    if os.getenv('SELENOID_ENABLED') == 'true':
        # Конфигурация для Selenoid
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "120.0")
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False
        })
        
        driver = webdriver.Remote(
            command_executor='http://selenoid:4444/wd/hub',
            options=options
        )
    else:
        # Локальная конфигурация
        options.add_argument("--window-size=1920,1200")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    
    yield driver
    driver.quit()