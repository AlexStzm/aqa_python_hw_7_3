import pytest
from selene.support.shared import browser
from selene import have

@pytest.fixture(scope="function", autouse=True)
def size_browser():
    browser.config.window_width = 1680
    browser.config.window_height = 1050
    yield
    browser.quit()

def test_authorization():
    browser.open('https://chocodiamond.ru/client_account/contacts/new')

    browser.element('#client_contact_name').type('TestUser2').press_tab()
    browser.element('#client_phone').type('79999999999').press_tab()
    browser.element('#client_email').type('test-email2@test.com').press_tab()
    browser.element('#client_password').type('password').press_tab()
    browser.element('#client_password_confirmation').type('password').press_tab()

    browser.element('.js-cookies-button').click()
    browser.element('.js-co-login-submit').click()

    browser.element('.co-checkout-title').should(have.text('История заказов'))