import pytest
from selene.support.shared import browser

@pytest.fixture(scope="function", autouse=True)
def size_browser():
    browser.config.window_width = 1680
    browser.config.window_height = 1050

@pytest.fixture(scope="function", autouse=True)
def base_url_browser(size_browser):
    browser.config.base_url = 'https://chocodiamond.ru'
    yield
    browser.quit()