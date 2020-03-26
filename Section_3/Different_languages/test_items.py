import pytest
import time
from selenium.common.exceptions import NoSuchElementException

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    try:
        assert browser.find_element_by_css_selector(".btn-add-to-basket")
    except NoSuchElementException:
        pytest.fail("The basket button is not present")
