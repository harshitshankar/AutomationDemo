# tests/conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture
def driver():
    chrome_options = Options()
    
    # Comment this line if you want to SEE the browser (for debugging/demo)
    # chrome_options.add_argument("--headless")

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")

    # Path to ChromeDriver (update this path if necessary)
    driver_path = r"C:\Users\ravi3_3e8ym6i\chromedriver-win64\chromedriver.exe"

    if not os.path.exists(driver_path):
        raise FileNotFoundError(f"ChromeDriver not found at {driver_path}")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    yield driver
    driver.quit()
