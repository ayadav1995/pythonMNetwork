
from Pages.SearchResultsPage import SearchResultsPage
from Utilities.properties import Properties
from selenium import webdriver
from Pages.BasePage import BasePage
from Pages.SearchPage import SearchPage

class Part1:

    def setup_driver(self):
        driver = webdriver.Chrome(executable_path=Properties.CHROME_DRIVER)
        driver.get(Properties.URL)
        return driver


    def get_image_urls(self):
        print("get image urls test ran")
        driver = self.setup_driver()
        searchPage = SearchPage(driver)
        searchPage.search("nice cars")
        search_results_page = SearchResultsPage(driver)
        image_urls = search_results_page.get_image_urls()
        print(image_urls)
        return image_urls

    def get_titles(self):
        print("get titles test ran")
        driver = self.setup_driver()
        searchPage = SearchPage(driver)
        searchPage.search("nice cars")
        search_results_page = SearchResultsPage(driver)
        titles = search_results_page.get_search_titles()
        print(titles)
        return titles

if __name__ == "__main__":
    part1_instance = Part1()
    # part1_instance.get_image_urls()
    part1_instance.get_titles()

