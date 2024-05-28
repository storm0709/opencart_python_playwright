from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from playwright.sync_api import Page, expect
from utilities import randomString

def test_reg_user_valid_creds(set_up_tear_down) -> None:

    f_name = 'User_' + randomString.random_string_generator()
    l_name = 'Test' + randomString.random_string_generator()
    email = randomString.random_string_generator() + '@testqa.com'
    tel = "1234567890"
    pwd = "qa12345"
    pwd_conf = "qa12345"
    expected_cong_msg = "Your Account Has Been Created!"

    page = set_up_tear_down
    acct_reg_p = AccountRegistrationPage(page)
    acct_reg_p.load_reg_acct_page()
    acct_reg_p.do_registration(f_name, l_name, email, tel, pwd, pwd_conf)

    expect(acct_reg_p.get_confirmation_msg).to_have_text(expected_cong_msg)


