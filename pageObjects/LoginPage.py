from playwright.sync_api import Page


class LoginPage:

    URL = 'index.php?route=account/login'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.txt_email = page.locator("//input[@id='input-email']")
        self.txt_password = page.locator("//input[@id='input-password']")
        self.btn_login = page.locator("//input[@value='Login']")
        self.msg_myaccount = page.locator("//h2[normalize-space()='My Account']")
        self.msg_wrong_creds = page.locator("//div[@class='alert alert-danger alert-dismissible']")


    def load_login_page(self) -> None:
        self.page.goto(self.URL)
    def set_email(self, email: str) -> None:
        self.txt_email.fill(email)

    def set_password(self, password: str) -> None:
        self.txt_password.fill(password)

    def click_login(self) -> None:
        self.btn_login.click()

    @property
    def get_myacct_msg(self):
        return self.msg_myaccount

    @property
    def get_error_msg(self):
        return self.msg_wrong_creds

    def do_login(self, email: str, password: str) -> None:
        self.set_email(email)
        self.set_password(password)
        self.click_login()

