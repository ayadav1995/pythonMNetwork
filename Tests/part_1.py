from Pages.SearchResultsPage import SearchResultsPage
from Utilities.properties import Properties
from selenium import webdriver
from Pages.BasePage import BasePage
from Pages.SearchPage import SearchPage
from webdriver_manager.chrome import ChromeDriverManager


class Part1:

    # Just plain part-1 implementation and tests not using pytest and fixtures. Meant to test functions in POM

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


    def get_image_urls(self):
        print("get image urls test ran")
        search_results_page = self.navigateToPage()
        image_urls = search_results_page.get_image_urls()
        print(image_urls)
        return image_urls

    def get_titles(self):
        print("get titles test ran")
        search_results_page = self.navigateToPage()
        titles = search_results_page.get_search_titles()
        print(titles)
        return titles

    def navigateToPage(self):
        self.driver.get(Properties.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        search_page = SearchPage(self.driver)
        search_page.search("nice cars")
        search_results_page = SearchResultsPage(self.driver)
        return search_results_page

    def teardown(self):
        self.driver.quit()


# Below code to test the functions implemented in part-1
part1 = Part1()
part1.get_image_urls()
part1.get_titles()
part1.teardown()
