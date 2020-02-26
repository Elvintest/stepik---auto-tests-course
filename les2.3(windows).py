from selenium import webdriver
import time
import math

"""alert это модалки, которые блокируют страницу,на них надо переключиться, без поиска
browser.switch_to_alert, затем можно получить текст .text принять accept() отказатьс
dismiss() что-то вписать send_keys()"""
# browser = webdriver.Chrome()
# link = 'http://suninjuly.github.io/alert_accept.html'
# browser.get(link)
#
# try:
#     # Щелкаем в alert
#     submit_button = browser.find_element_by_class_name('btn.btn-primary').click()
#     confirm = browser.switch_to_alert()
#     confirm.accept()
#     # Вводим в поле ответ на формулу
#     x_web = browser.find_element_by_id('input_value')
#     x = x_web.text
#     answer = str(math.log(abs(12*math.sin(int(x)))))
#     answer_input = browser.find_element_by_class_name('form-control')
#     answer_input.send_keys(answer)
#     submit_button = browser.find_element_by_class_name('btn.btn-primary')
#     browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
#     submit_button.click()
#     time.sleep(10)
# finally:
#     browser.quit()

"""перекючиться на новое окно switch_to.window(window name), получить список 
окон window.handle, обратиться к элементу массива"""
# browser = webdriver.Chrome()
# link = 'http://suninjuly.github.io/redirect_accept.html'
# browser.get(link)
# new_window_button = browser.find_element_by_class_name('trollface.btn.btn-primary').click()
# new_window = browser.window_handles[1]
# print(new_window)
# browser.switch_to.window(new_window)
# x_web = browser.find_element_by_id('input_value')
# x = x_web.text
# answer = str(math.log(abs(12*math.sin(int(x)))))
# answer_input = browser.find_element_by_class_name('form-control')
# answer_input.send_keys(answer)
# submit_button = browser.find_element_by_class_name('btn.btn-primary')
# submit_button.click()
# time.sleep(10)
# browser.quit()

"""implicitly wait"""
browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/cats.html'
browser.get(link)
browser.find_element_by_id("button")