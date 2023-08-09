import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Utilities.properties import Properties


@pytest.fixture(scope="function")
def setup(request):
    global driver
    browser = Properties.BROWSER
    if browser == "chrome":
        d = ChromeDriverManager()
        driver = webdriver.Chrome(executable_path=d.install())
    elif browser == "firefox":
        d = GeckoDriverManager()
        driver = webdriver.Firefox(executable_path=d.install())
    driver.get(Properties.URL)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    print("=========================")
    print("TEST EXECUTION STARTED")
    print("=========================")
    yield
    print("=========================")
    print("TEST EXECUTION COMPLETED")
    print("=========================")
    driver.quit()


# below code is for generating screenshot and attaching it to the html report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # getting name of test case from item
            test_name = item.nodeid.replace("::", "_").replace("/", "_").replace("(", "_").replace(")", "_")
            file_name = test_name + "screenshot.png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    print("Trying to capture screenshot")
    driver.get_screenshot_as_file(name)


def pytest_html_report_title(report):
    report.title = "MN coding test report"
