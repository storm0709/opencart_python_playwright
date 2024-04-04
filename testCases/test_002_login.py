from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from playwright.sync_api import Page, expect
from utilities.readProperties import ReadConfig
from pytest import mark


ddt_valid_creds = {
    'argnames': 'email, password, msg',
    'argvalues': [('abc@qa.com', 'abcxyz', 'My Account')],
    'ids': ['valid creds']
}

# Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour.

ddt_invalid_creds = {
    'argnames': 'email, password, msg',
    'argvalues': [('abc@qa.com', '123', 'Warning: No match for E-Mail Address and/or Password.'),
                  ('123', 'abcxyz', 'Warning: No match for E-Mail Address and/or Password.'),
                  ('user', 'passw', 'Warning: No match for E-Mail Address and/or Password.')],
    'ids': ['invalid password', 'invalid email', 'invalid creds']

}

@mark.parametrize(**ddt_valid_creds)
def test_valid_login(set_up_tear_down, email, password, msg):
    page = set_up_tear_down
    # home_p = HomePage(page)
    login_p = LoginPage(page)

    # home_p.click_my_account()
    # home_p.click_login()
    login_p.load_login_page()
    login_p.do_login(email, password)

    expect(login_p.get_myacct_msg).to_have_text(msg)

@mark.parametrize(**ddt_invalid_creds)
def test_invalid_login(set_up_tear_down, email, password, msg):
    page = set_up_tear_down
    # home_p = HomePage(page)
    login_p = LoginPage(page)

    # home_p.load_home_page()
    # home_p.click_my_account()
    # home_p.click_login()
    login_p.load_login_page()
    login_p.do_login(email, password)

    expect(login_p.get_error_msg).to_have_text(msg)

