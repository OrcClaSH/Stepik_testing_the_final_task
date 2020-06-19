from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help='Choose browser: chrome or firefox'
        )
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language: ru, en ...'
        )
    # parser.addoption(
    #     '--product_name',
    #     action='store',
    #     default=None,
    #     help='Input product_name'
    #     )
    # parser.addoption(
    #     '--droduct_price',
    #     action='store',
    #     default=None,
    #     help='Input product price'
    #     )


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    # product_name = request.config.getoption('product_name')
    # product_price = request.config.getoption('product_price')
    browser = None
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option(
            'prefs',
            {'intl.accept_languages': user_language}
        )
        print('\nStart chrome browser for test...')
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(5)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        print('\nStart firefox browser for test...')
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError('--browser_name should be chrome of firefox')
    yield browser
    print('\nQuit browser...')
    browser.quit()
