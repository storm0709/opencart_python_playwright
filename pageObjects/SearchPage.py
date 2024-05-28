from playwright.sync_api import Page

class SearchPage:

    URL = 'index.php?route=product/search'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_title = page.locator("//h1")
        self.search_criteria_field = page.locator("//input[@id='input-search']")
        self.search_result_list = page.locator("//h4/a")
        self.search_error_msg = page.locator("//h2/following-sibling::p")

    def load_search_page(self) -> None:
        self.page.goto(self.URL)


    def get_search_results(self):
        return self.search_result_list

    def get_search_error_msg(self):
        return self.search_error_msg

    def get_search_title(self):
        return self.search_title

    def get_search_criteria_value(self):
        return self.search_criteria_field