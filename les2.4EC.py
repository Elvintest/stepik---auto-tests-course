from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

"""Ожидание невное browser.implicitly_wait(5) будет ждать 5 секунд до выброса
ошибка NosuchElement"""
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
# дожидамемся текста в элементе h5 '$100'
button = browser.find_element_by_id('book')
price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )
# после этого нажимаем кнопку
button.click()
# определяем поле для ответа и скролим страницу до него через execute script
answer_input = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.ID, "answer"))
    )
browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
answer_input.click()
# считаем формулу, вставляем, отправляем
x_web = browser.find_element_by_id('input_value')
x = x_web.text
answer = str(math.log(abs(12*math.sin(int(x)))))
answer_input = browser.find_element_by_class_name('form-control')
answer_input.send_keys(answer)
submit_button = browser.find_element_by_id('solve')
submit_button.click()
time.sleep(10)
browser.quit()