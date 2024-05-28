from pageObjects.HomePage import HomePage
from pageObjects.LogoutPage import LogoutPage
from playwright.sync_api import Page, expect


expected_myacct_dropdown_values = ['Register', 'Login']


def test_logout_dropmenu(set_up_tear_down_auth, request):
    page = set_up_tear_down_auth
    base_url = request.config.getoption('--base_url')
    home_p = HomePage(page)
    logout_p = LogoutPage(page)
    home_p.click_my_account()
    home_p.click_logout()
    logout_p.click_continue()

    expect(home_p.get_myacct_dropdown_values()).to_contain_text(expected_myacct_dropdown_values)
    expect(page).to_have_url(base_url+home_p.URL)
