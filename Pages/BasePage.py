from selenium import webdriver
from Utilities.properties import Properties


class BasePage:
    def __init__(self, driver):
        self.driver = self.setup()
        driver = webdriver.Chrome(executable_path=Properties.CHROME_DRIVER)
        driver.get(Properties.URL)




