import pytest

@pytest.fixture()
def set_up_tear_down(page, request):
    base_url = request.config.getini('base_url')
    page.set_viewport_size({"width":1536, "height":800})
    page.goto("/")
    yield page



def pytest_addoption(parser):
    parser.addini('base_url', help='base url of site under test', default='http://localhost')


# # This will get the value from CLI /hooks
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# # This will return the Browser value to setup method
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
