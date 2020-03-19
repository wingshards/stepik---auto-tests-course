import unittest

from selenium import webdriver
import time


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        # Ссылка на сайт без ошибки
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        name = browser.find_element_by_css_selector(".first_block .first")
        name.send_keys("Ivan")
        surname = browser.find_element_by_css_selector(".first_block .second")
        surname.send_keys("Petrov")
        mail = browser.find_element_by_css_selector(".first_block .third")
        mail.send_keys("ip@mail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration is failed")
        browser.quit()

    def test_abs2(self):
        # Ссылка на сайт c ошибкой
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        name = browser.find_element_by_css_selector(".first_block .first")
        name.send_keys("Ivan")
        surname = browser.find_element_by_css_selector(".first_block .second")
        surname.send_keys("Petrov")
        mail = browser.find_element_by_css_selector(".first_block .third")
        mail.send_keys("ip@mail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration is failed")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
