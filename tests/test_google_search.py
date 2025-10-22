import pytest
from selenium import webdriver
from pages.google_page import GooglePage
import allure
import time

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    yield driver
    driver.quit()

@allure.feature("Google Search Feature")
@allure.story("Search Test")
def test_google_search(setup):
    page = GooglePage(setup)
    page.search("OpenAI")
    time.sleep(3)  # wait for results
    assert "OpenAI" in setup.title
