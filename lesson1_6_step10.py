from selenium import webdriver
import time

link = 'http://suninjuly.github.io/registration2s.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element_by_tag_name('input[placeholder="Input your first name"]')
    input.send_keys('NAME')
    input = browser.find_element_by_tag_name('input[placeholder="Input your last name"]')
    input.send_keys('BU-GA-GA')
    input = browser.find_element_by_tag_name('input[placeholder="Input your email"]')
    input.send_keys('microsoft@ms.com')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    time.sleep(5)

    welcome_text_elt = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:   

    time.sleep(5)
#    browser.quit()