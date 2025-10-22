from selenium.webdriver.common.by import By

class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")
        self.search_button = (By.NAME, "btnK")

    def search(self, text):
        box = self.driver.find_element(*self.search_box)
        box.send_keys(text)
        box.submit()  # Press enter
