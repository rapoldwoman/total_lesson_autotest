import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,help="Choose language")



@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("--language")
    if language_name is not None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
        browser = webdriver.Chrome(options=options)
        print("\start browser test..")
    else:
        raise Exception("Выбери язык")

    browser.implicitly_wait(30)
    yield browser
    print("\nend browser test..")
    browser.quit()