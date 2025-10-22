# tests/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    # Comment this line if you want to SEE the browser
    # chrome_options.add_argument("--headless")

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")

    service = Service("C:\\path\\to\\chromedriver.exe")  # Update your path if needed
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()
