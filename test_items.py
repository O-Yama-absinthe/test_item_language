import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def is_element_present(browser):
    try:
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector(".btn-add-to-basket")
        return True
    except:
        return False
    
def test_language(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert is_element_present(browser), "корзинка не найдена"

