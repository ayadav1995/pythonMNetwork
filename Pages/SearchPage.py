import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from Pages.BasePage import BasePage
from Utilities.properties import Properties
from selenium import webdriver


class SearchPage():
    # defining page elements/locators
    searchBox = (By.ID, "searchbox_input")
    searchButton = (By.XPATH, "//button[@type=\"submit\"]")

    def __init__(self, driver):
        self.driver = driver
        # super().__init__(driver)

    def search(self, search_query):
        self.driver.find_element(*self.searchBox).send_keys(search_query)
        self.driver.find_element(*self.searchButton).click()
