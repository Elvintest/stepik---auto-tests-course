import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        name_button = browser.find_element_by_css_selector('.first_block .form-group.first_class .form-control.first')
        name_button.send_keys('Elvin')
        surname_button = browser.find_element_by_css_selector(
            '.first_block .form-group.second_class .form-control.second')
        surname_button.send_keys('Yagudin')
        email_button = browser.find_element_by_css_selector('.first_block .form-group.third_class .form-control.third')
        email_button.send_keys('123@mail.ru')
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

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text,f'{welcome_text} should be equal Congratulations! You have successfully registered!')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        name_button = browser.find_element_by_css_selector('.first_block .form-group.first_class .form-control.first')
        name_button.send_keys('Elvin')
        surname_button = browser.find_element_by_css_selector(
            '.first_block .form-group.second_class .form-control.second')
        surname_button.send_keys('Yagudin')
        email_button = browser.find_element_by_css_selector('.first_block .form-group.third_class .form-control.third')
        email_button.send_keys('123@mail.ru')
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

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text,f'{welcome_text} should be equal Congratulations! You have successfully registered!')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций



if __name__ == "__main__":
    unittest.main()



