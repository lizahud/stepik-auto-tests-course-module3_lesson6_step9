import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_have_button_basket(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button")
    assert button, "This page doesn't have button add to basket"
    time.sleep(30)
