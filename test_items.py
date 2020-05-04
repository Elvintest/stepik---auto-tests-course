from selenium import webdriver
import pytest
import time
def test_check_basket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_css_selector('.btn-add-to-basket'), 'NO button on the page'