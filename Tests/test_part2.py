from Pages.SearchResultsPage import SearchResultsPage
from Utilities.properties import Properties
from Pages.SearchPage import SearchPage
import pytest

@pytest.mark.usefixtures("setup")
class TestPart2:

    def test_source(self):
        print("verify_source test ran")
        search_results_page = self.navigateToPage()
        source_is_present = search_results_page.checkSourceOfImage(Properties.SOURCE_WEBSITE)
        assert source_is_present

    def test_word_in_title(self):
        print("verify_source test ran")
        # driver = self.setup_driver()
        search_page = SearchPage(self.driver)
        search_page.search(Properties.SEARCH_QUERY)
        search_results_page = SearchResultsPage(self.driver)
        word_is_present = search_results_page.check_words_exist(Properties.WORDS_TO_CHECK)
        print(word_is_present)
        assert word_is_present

    def navigateToPage(self):
        search_page = SearchPage(self.driver)
        search_page.search(Properties.SEARCH_QUERY)
        search_results_page = SearchResultsPage(self.driver)
        return search_results_page