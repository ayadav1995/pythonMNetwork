from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    # defining page elements/locators
    searchBox = (By.ID, "searchbox_input")
    searchButton = (By.XPATH, "//button[@type=\"submit\"]")

    def __init__(self, driver):
        self.driver = driver

    def search(self, search_query):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.searchBox))
        self.driver.find_element(*self.searchBox).send_keys(search_query)
        self.driver.find_element(*self.searchButton).click()
