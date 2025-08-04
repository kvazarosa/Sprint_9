import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data import Urls


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1200")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(Urls.HOME_PAGE_URL)
    yield driver
    driver.quit()
