import time
import math
from selenium import webdriver
import pytest



"""фикстура для закрытия и открытия браузера при запуске каждого теста"""
#     def setup_class(self):
#         self.browser = webdriver.Chrome()
#
#     def teardown_class(self):
#         self.browser.quit()
"""такие методы используются к каждому методу класса, но не работают с поочередным запуском тестов через параметризация"""


class Test_task:
    @pytest.mark.parametrize('number_of_lesson',
                             ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
    def test_correct_answer(self, browser, number_of_lesson):
        link = f'https://stepik.org/lesson/{number_of_lesson}/step/1'
        browser.get(link)
        browser.implicitly_wait(10)
        input_answer = browser.find_element_by_class_name(
            'textarea.string-quiz__textarea.ember-text-area.ember-view')
        input_answer.send_keys(str(math.log(int(time.time()))))
        submit_button = browser.find_element_by_class_name('submit-submission')
        submit_button.click()
        browser.implicitly_wait(10)
        feedback = browser.find_element_by_class_name('smart-hints__hint')
        assert feedback.text == 'Correct!', 'Should be correct'

# https: // stepik.org / lesson / 236895 / step / 1
# https: // stepik.org / lesson / 236896 / step / 1
# https: // stepik.org / lesson / 236897 / step / 1
# https: // stepik.org / lesson / 236898 / step / 1
# https: // stepik.org / lesson / 236899 / step / 1
# https: // stepik.org / lesson / 236903 / step / 1
# https: // stepik.org / lesson / 236904 / step / 1
# https: // stepik.org / lesson / 236905 / step / 1
