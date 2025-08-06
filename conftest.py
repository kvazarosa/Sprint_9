import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import RemoteConnection
from data import Urls
import os

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    
    if os.getenv('SELENOID_ENABLED') == 'true':
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=chrome_options
        )
    else:
        chrome_options.add_argument("--window-size=1920,1200")
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
    
    driver.implicitly_wait(30)  
    driver.set_page_load_timeout(60) 
    
    driver.get(Urls.HOME_PAGE_URL)
    yield driver
    driver.quit()