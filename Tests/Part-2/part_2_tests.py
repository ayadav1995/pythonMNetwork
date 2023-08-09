from Pages.SearchResultsPage import SearchResultsPage
from Utilities.properties import Properties
from selenium import webdriver
from Pages.BasePage import BasePage
from Pages.SearchPage import SearchPage


class Part2Tests:

    def setup_driver(self):
        driver = webdriver.Chrome(executable_path=Properties.CHROME_DRIVER)
        driver.get(Properties.URL)
        return driver

    def verify_source(self, source):
        print("verify_source test ran")
        driver = self.setup_driver()
        searchPage = SearchPage(driver)
        searchPage.search("nice cars")
        search_results_page = SearchResultsPage(driver)
        source_is_present = search_results_page.checkSourceOfImage(source)
        return source_is_present

    def verify_word_in_title(self, words):
        print("verify_source test ran")
        driver = self.setup_driver()
        search_page = SearchPage(driver)
        search_page.search("nice cars")
        search_results_page = SearchResultsPage(driver)
        word_is_present = search_results_page.check_words_exist(words)
        return word_is_present


if __name__ == "__main__":
    part2_instance = Part2Tests()
    # print(part2_instance.verify_source("http://wallpapercave.com/"))
    print(part2_instance.verify_word_in_title(["CARS", "cAr"]))
