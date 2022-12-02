from selenium import webdriver
import math
import time

data = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_link_text')
    link = browser.find_element_by_link_text(data)
    link.click()
    input = browser.find_element_by_name('first_name')
    input.send_keys('Ivan')
    input = browser.find_element_by_name('last_name')
    input.send_keys('Petrov')
    input = browser.find_element_by_name('firstname')
    input.send_keys('Smolensk')
    input = browser.find_element_by_id('country')
    input.send_keys('Russia')
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()