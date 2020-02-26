from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import os
import os.path


# browser = webdriver.Chrome()
# link = 'http://suninjuly.github.io/selects1.html'
# browser.get(link)

"""
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") # ищем элемент с текстом "Python"
Можно использовать еще два метода: select.select_by_visible_text("text")
и select.select_by_index(index). Первый способ ищет
элемент по видимому тексту, например, select.select_by_visible_text("Python")
Второй способ ищет элемент по его индексу или порядковому номеру.
Индексация начинается с нуля."""

# first_num = browser.find_element_by_id('num1').text
# second_num = browser.find_element_by_id('num2').text
# answer = int(first_num) + int(second_num)
# spisok = Select(browser.find_element_by_class_name('custom-select'))
# spisok.select_by_visible_text(str(answer))
# submit = browser.find_element_by_class_name('btn.btn-default')
# submit.click()

"""Исполнение скрипта JS в вебдрайвере, например для прокрутки страницы
до полной видимости элемента 
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()"""

# browser = webdriver.Chrome()
# link = 'http://suninjuly.github.io/execute_script.html'
# browser.get(link)

# Вводим в поле ответ на формулу
# x_web = browser.find_element_by_id('input_value')
# x = x_web.text
# answer = str(math.log(abs(12*math.sin(int(x)))))
# answer_input = browser.find_element_by_class_name('form-control')
# answer_input.send_keys(answer)
#
# # Отмечаем чекбок im the robot
# im_robot_check_box = browser.find_element_by_id('robotCheckbox').click()
#
# robot_rules_box = browser.find_element_by_id('robotsRule')
# browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rules_box)
# robot_rules_box.click()
#
# submit_button = browser.find_element_by_class_name('btn.btn-primary')
# browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
# submit_button.click()

"""прикерпление файла через os"""
browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

first_name = browser.find_element_by_name('firstname').send_keys('Elvin')
second_name = browser.find_element_by_name('lastname').send_keys('Yagudin')
email = browser.find_element_by_name('email').send_keys('Yagudin@mail.ru')
my_file = os.path.join(os.getcwd(),'lesson22.txt')
send_file = browser.find_element_by_id('file').send_keys(my_file)
submit_button = browser.find_element_by_class_name('btn.btn-primary')
submit_button.click()