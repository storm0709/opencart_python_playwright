from playwright.sync_api import Page

class AccountRegistrationPage:

    URL = 'index.php?route=account/register'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.lbl_first_name = page.get_by_label("First Name")
        self.lbl_last_name = page.get_by_label("Last Name")
        self.lbl_email = page.get_by_label("E-Mail")
        self.lbl_telephone = page.get_by_label("Telephone")
        self.lbl_password = page.locator("//input[@id='input-password']")
        self.lbl_password_confirm = page.locator("//input[@id='input-confirm']")
        self.chk_policy_name = page.locator("//input[@name='agree']")
        self.btn_continue = page.locator("//input[@value='Continue']")
        self.txt_msg_confirm = page.locator("//h1[normalize-space()='Your Account Has Been Created!']")

    def load_reg_acct_page(self) -> None:
        self.page.goto(self.URL)

    def set_first_name(self, fname: str) -> None:
        self.lbl_first_name.fill(fname)

    def set_last_name(self, lname: str) -> None:
        self.lbl_last_name.fill(lname)

    def set_email(self, email: str) -> None:
        self.lbl_email.fill(email)

    def set_telephone(self, tel: str) -> None:
        self.lbl_telephone.fill(tel)

    def set_password(self, pwd: str) -> None:
        self.lbl_password.fill(pwd)

    def set_confirm_password(self, cnfpwd: str) -> None:
        self.lbl_password_confirm.fill(cnfpwd)

    def set_privacy_policy(self) -> None:
        self.chk_policy_name.click()

    def click_continue(self) -> None:
        self.btn_continue.click()

    @property
    def get_confirmation_msg(self):
        return self.txt_msg_confirm

    def do_registration(self, first: str, last: str, email: str, tel: str, passw: str, pwd_conf: str) -> None:
        self.set_first_name(first)
        self.set_last_name(last)
        self.set_email(email)
        self.set_telephone(tel)
        self.set_password(passw)
        self.set_confirm_password(pwd_conf)
        self.set_privacy_policy()
        self.click_continue()


