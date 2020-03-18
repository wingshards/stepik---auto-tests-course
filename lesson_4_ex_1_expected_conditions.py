from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    book = browser.find_element_by_css_selector("#book")
    price = WebDriverWait(browser, 13).until(
        text_to_be_present_in_element((By.ID, "price"), '100')
    )
    book.click()

    # Находим х и вычисляем значение формулы
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    # Заполняем ответ
    value = browser.find_element_by_css_selector("#answer")
    value.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("#solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
