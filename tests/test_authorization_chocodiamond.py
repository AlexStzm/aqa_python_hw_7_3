import pytest
from selene.support.shared import browser
from selene import have

@pytest.fixture(scope="function", autouse=True)
def size_browser():
    browser.config.window_width = 1680
    browser.config.window_height = 1050
    yield
    browser.quit()

def test_valid_login_and_password():
    browser.open('https://chocodiamond.ru/client_account/session/new')

    browser.element('.co-form--login [name=email]').type('test-email@test.com').press_tab()
    browser.element('[name=password]').type('password').press_enter()

    browser.element('.co-checkout-title').should(have.text('История заказов'))


def test_invalid_login_with_wrong_email():
    browser.open('https://chocodiamond.ru/client_account/session/new')

    browser.element('.co-form--login [name=email]').type('testemail@test.com').press_tab()
    browser.element('[name=password]').type('password').press_enter()

    browser.element('.co-notice--danger').should(have.exact_text('Сочетание логина и пароля не подходит'))


def test_invalid_login_with_wrong_password():
    browser.open('https://chocodiamond.ru/client_account/session/new')

    browser.element('.co-form--login [name=email]').type('test-email@test.com').press_tab()
    browser.element('[name=password]').type('abracadabra').press_enter()

    browser.element('.co-notice--danger').should(have.exact_text('Сочетание логина и пароля не подходит'))


def test_invalid_login_with_empty_email():
    browser.open('https://chocodiamond.ru/client_account/session/new')

    browser.element('.co-form--login [name=password]').type('password').press_enter()

    browser.element('.co-form-controls .co-button').should(have.exact_text('Войти'))


def test_invalid_login_with_empty_password():
    browser.open('https://chocodiamond.ru/client_account/session/new')

    browser.element('.co-form--login [name=email]').type('test-email@test.com').press_enter()

    browser.element('.co-form-controls .co-button').should(have.exact_text('Войти'))