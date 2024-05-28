from playwright.sync_api import Page

from pageObjects.SearchPage import SearchPage


class HomePage:

    URL = '/index.php?route=common/home'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.lnk_myaccount = page.locator("//span[normalize-space()='My Account']")
        self.myacct_dropdown_values = page.locator("//ul[@class='dropdown-menu dropdown-menu-right']/li")
        self.lnk_register = page.get_by_text("Register")
        self.lnk_login = page.get_by_text("Login")
        self.lnk_logout = page.locator("//a[normalize-space()='Logout']")
        self.search_field = page.locator("//input[@placeholder='Search']")
        self.search_btn = page.locator("//button[@class='btn btn-default btn-lg']")

    def load_home_page(self) -> None:
        self.page.goto(self.URL)

    def click_my_account(self) -> None:
        self.lnk_myaccount.click()

    def click_register(self) -> None:
        self.lnk_register.click()

    def click_login(self) -> None:
        self.lnk_login.click()

    def click_logout(self) -> None:
        self.lnk_logout.click()

    def do_search(self, product: str):
        self.search_field.click()
        self.search_field.fill(product)
        self.search_btn.click()
        return SearchPage(self.page)

    def click_search_btn(self):
        self.search_btn.click()
        return SearchPage(self.page)

    def get_myacct_dropdown_values(self):
        self.lnk_myaccount.click()
        return self.myacct_dropdown_values

