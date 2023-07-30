from selene.support.shared import browser
from selene import have

def test_valid_login_and_password(size_browser, base_url_browser):
    browser.open('/client_account/session/new')

    browser.element('.co-form--login [name=email]').type('test-email@test.com').press_tab()
    browser.element('[name=password]').type('password').press_enter()

    browser.element('.co-checkout-title').should(have.text('История заказов'))


def test_invalid_login_with_wrong_email(size_browser, base_url_browser):
    browser.open('/client_account/session/new')

    browser.element('.co-form--login [name=email]').type('testemail@test.com').press_tab()
    browser.element('[name=password]').type('password').press_enter()

    browser.element('.co-notice--danger').should(have.exact_text('Сочетание логина и пароля не подходит'))


def test_invalid_login_with_wrong_password(size_browser, base_url_browser):
    browser.open('/client_account/session/new')

    browser.element('.co-form--login [name=email]').type('test-email@test.com').press_tab()
    browser.element('[name=password]').type('abracadabra').press_enter()

    browser.element('.co-notice--danger').should(have.exact_text('Сочетание логина и пароля не подходит'))


def test_invalid_login_with_empty_email(size_browser, base_url_browser):
    browser.open('/client_account/session/new')

    browser.element('.co-form--login [name=password]').type('password').press_enter()

    browser.element('.co-form-controls .co-button').should(have.exact_text('Войти'))


def test_invalid_login_with_empty_password(size_browser, base_url_browser):
    browser.open('/client_account/session/new')

    browser.element('.co-form--login [name=email]').type('test-email@test.com').press_enter()

    browser.element('.co-form-controls .co-button').should(have.exact_text('Войти'))