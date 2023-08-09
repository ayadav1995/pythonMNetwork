from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from Pages.BasePage import BasePage


class SearchResultsPage:
    imageLinks = (By.XPATH, "//div[@class=\"module module--images\"]//a[@class=\"module--images__thumbnails__link\"]")
    searchResults = (By.XPATH, "//h2/a/span")

    def __init__(self, driver):
        self.driver = driver

    def get_image_urls(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.imageLinks))
        image_elements = self.driver.find_elements(*self.imageLinks)
        image_urls = []
        for element in image_elements:
            google_url = element.get_attribute("href")
            image_urls.append(self.get_site_url(google_url))
        return image_urls

    def get_site_url(self, google_url):
        # code to handle images with http and https both
        start_index = google_url.find("https://", google_url.find("https://") + len("https://"))
        if start_index == -1:
            start_index = google_url.find("http://", google_url.find("https://") + len("http://"))
        return google_url[start_index:]

    def get_search_titles(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.searchResults))
        result_elements = self.driver.find_elements(*self.searchResults)
        titles = []
        for title in result_elements:
            titles.append(title.text)
        return titles

    def checkSourceOfImage(self, source):
        imageUrls = self.get_image_urls()
        # if desired source url found in any string return true
        for url in imageUrls:
            if source in url:
                print("Source found in", url)
                return True
        return False

    def check_words_exist(self, words):
        titles = self.get_search_titles()
        for word in words:
            for title in titles:
                if word.lower() in title.lower().split():
                    print("Word found in", title)
                    return True
        return False
