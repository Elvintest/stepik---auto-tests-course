from selenium import webdriver
import math
"""использование метод text для преобразования веб-элемента к строке"""

# link = "http://suninjuly.github.io/math.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# # Вводим в поле ответ на формулу
# x_web = browser.find_element_by_id('input_value')
# x = x_web.text
# answer = str(math.log(abs(12*math.sin(int(x)))))
# answer_input = browser.find_element_by_class_name('form-control')
# answer_input.send_keys(answer)
#
# # Отмечаем чекбок im the robot
# im_robot_check_box = browser.find_element_by_id('robotCheckbox').click()
# robot_rules_box = browser.find_element_by_id('robotsRule').click()
# submit_button = browser.find_element_by_class_name('btn.btn-default').click()



"""использование метода get_attribute для получения значения элемента"""
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# Вводим в поле ответ на формулу
x_web = browser.find_element_by_id('treasure')
x = x_web.get_attribute('valuex')
answer = str(math.log(abs(12*math.sin(int(x)))))
answer_input = browser.find_element_by_id('answer')
answer_input.send_keys(answer)

# Отмечаем чекбок im the robot
im_robot_check_box = browser.find_element_by_id('robotCheckbox').click()
robot_rules_box = browser.find_element_by_id('robotsRule').click()
submit_button = browser.find_element_by_class_name('btn.btn-default').click()