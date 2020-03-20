import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_check_the_answer(browser, url):
    link = url
    browser.get(link)
    time.sleep(5)
    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector("#ember68").send_keys(str(answer))
    browser.find_element_by_css_selector(".submit-submission").click()
    time.sleep(3)
    assert browser.find_element_by_css_selector(".smart-hints__hint").text == "Correct!"
