from Pages.SearchResultsPage import SearchResultsPage
from Utilities.properties import Properties
from Pages.SearchPage import SearchPage
import pytest

@pytest.mark.usefixtures("setup")
class TestPart2:

    def test_image_source(self):
        print("\n TEST RUNNING : test_image_source")
        search_results_page = self.navigateToPage()
        source_is_present = search_results_page.checkSourceOfImage(Properties.SOURCE_WEBSITE)
        assert source_is_present

    def test_word_in_title(self):
        print("\n TEST RUNNING : test_word_in_title")
        search_results_page = self.navigateToPage()
        word_is_present = search_results_page.check_words_exist(Properties.WORDS_TO_CHECK)
        # can uncomment below to see the generated report with screenshot in case of failed tests
        # word_is_present = False
        assert word_is_present

    def navigateToPage(self):
        search_page = SearchPage(self.driver)
        search_page.search(Properties.SEARCH_QUERY)
        search_results_page = SearchResultsPage(self.driver)
        return search_results_page