from playwright.sync_api import Page

class LogoutPage:
    URL = 'index.php?route=account/logout'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.btn_continue = page.locator("//a[@class='btn btn-primary']")


    def click_continue(self) -> None:
        self.btn_continue.click()