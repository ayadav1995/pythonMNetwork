from selenium import webdriver
from properties import Properties


class helper:

    def setup(self):
        driver = webdriver.Chrome(executable_path= Properties.CHROME_DRIVER)
        driver.get(Properties.URL)



