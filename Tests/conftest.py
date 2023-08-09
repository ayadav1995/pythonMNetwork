import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Utilities.properties import Properties


@pytest.fixture(scope="function")
def setup(request):
    browser = Properties.BROWSER
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Chrome(executable_path=GeckoDriverManager.install())

    wait = WebDriverWait(driver, 10)
    driver.get(Properties.URL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()
