import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    # Инициализируются опции браузера
    options = Options()

    # В опции вебдрайвера передаем параметр из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)

    yield browser
    browser.quit()
