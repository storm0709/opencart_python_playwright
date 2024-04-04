from playwright.sync_api import Page
from utilities.readProperties import ReadConfig


class HomePage:

    # URL = 'http://localhost'
    #URL = ReadConfig.get_application_url()

    def __init__(self, page: Page, headless=False) -> None:
        self.page = page
        self.lnk_myaccount = page.locator("//span[normalize-space()='My Account']")
        self.lnk_register = page.get_by_text("Register")
        self.lnk_login = page.get_by_text("Login")

    def load_home_page(self) -> None:
        self.page.goto(self.URL)

    def click_my_account(self) -> None:
        self.lnk_myaccount.click()

    def click_register(self) -> None:
        self.lnk_register.click()

    def click_login(self) -> None:
        self.lnk_login.click()
