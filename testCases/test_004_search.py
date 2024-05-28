from pageObjects.HomePage import HomePage
from pageObjects.SearchPage import SearchPage
from playwright.sync_api import expect

def test_search_existing_product(set_up_tear_down) -> None:
    search_title = "Search - "
    product = 'mac'

    page = set_up_tear_down
    home_p = HomePage(page)
    search_p = home_p.do_search(product)

    expect(search_p.get_search_results()).to_contain_text(['mac'], ignore_case=True)
    expect(search_p.get_search_title()).to_have_text(search_title + product)
    expect(search_p.get_search_criteria_value()).to_have_value(product)

def test_search_nonexisting_product(set_up_tear_down) -> None:
    search_title = "Search - "
    product ="igligu"
    search_error_msg = "There is no product that matches the search criteria."

    page = set_up_tear_down
    home_p = HomePage(page)
    search_p = home_p.do_search(product)

    expect(search_p.search_error_msg).to_have_text(search_error_msg)
    expect(search_p.get_search_title()).to_have_text(search_title+product)
    expect(search_p.get_search_criteria_value()).to_have_value(product)

def test_search_empty(set_up_tear_down) -> None:
    search_title = "Search"
    search_error_msg = "There is no product that matches the search criteria."

    page = set_up_tear_down
    home_p = HomePage(page)
    search_p = home_p.click_search_btn()

    expect(search_p.search_error_msg).to_have_text(search_error_msg)
    expect(search_p.get_search_title()).to_have_text(search_title)
    expect(search_p.get_search_criteria_value()).to_be_empty()

