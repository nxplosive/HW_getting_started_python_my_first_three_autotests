from selene import browser
from selene import have

def test_demoqa():
    browser.open('https://demoqa.com/text-box')

    browser.element('#userName').type('Gosha')
    browser.element('#userEmail').type('gosha@mail.ru')
    browser.element('#currentAddress').type('test address')
    browser.element('#permanentAddress').type('dom')

    browser.execute_script("window.scrollTo(0,500)")
    browser.element('#submit').click()

    browser.element('#name').should(have.exact_text('Name:Gosha'))
    browser.element('#email').should(have.exact_text('Email:gosha@mail.ru'))
    browser.element('#currentAddress.mb-1').should(have.text("test address"))
    browser.element('#permanentAddress.mb-1').should(have.text("dom"))