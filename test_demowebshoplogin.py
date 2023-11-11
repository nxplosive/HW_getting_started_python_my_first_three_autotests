from selene import browser, have

browser.config.timeout = 2


def open_login_form():
    browser.open('https://demowebshop.tricentis.com/')
    browser.element('[class=ico-login]').click()


def test_valid_login():
    open_login_form()

    browser.element('#Email').type('xicat5000@yandex.ru')
    browser.element('#Password').type('Beli$$im0')
    browser.element('.login-button').click()

    browser.element('[class="account"]').should(have.exact_text('xicat5000@yandex.ru'))

def test_logout():
    ...