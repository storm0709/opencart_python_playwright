import os
import json
import time
import pytest


from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage

@pytest.fixture()
def use_auth_state(playwright, request):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    base_url = request.config.getoption('--base_url')
    secure = request.config.getoption('--secure')
    config = load_config(secure)
    page = context.new_page()
    login_page = LoginPage(page)
    page.goto(base_url+login_page.URL)
    login_page.do_login(**config)
    context.storage_state(path="state.json")
    yield context


@pytest.fixture()
def set_up_tear_down(page, request):
    base_url = request.config.getoption('--base_url')
    page.set_viewport_size({"width":1536, "height":800})
    page.goto("/")
    yield page

@pytest.fixture()
def set_up_tear_down_auth(use_auth_state, browser, request):
    base_url = request.config.getoption('--base_url')
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    page.set_viewport_size({"width":1536, "height":800})
    home_page = HomePage(page)
    page.goto(base_url+home_page.URL)
    yield page
    context.close()


def pytest_addoption(parser):
     parser.addoption('--base_url', action='store', default='http://localhost')
     parser.addoption('--secure', action='store', default='secure.json')
def load_config(file):
     config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
     with open(config_file) as cfg:
         return json.loads(cfg.read())

