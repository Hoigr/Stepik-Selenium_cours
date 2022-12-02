import webbrowser
from selenium import webdriver
import time

link = 'http://suninjuly.github.io/find_xpath_form'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element_by_xpath('/html/body/div/form/div[1]/input')
    input.send_keys('Ivan')
    input = browser.find_element_by_xpath('/html/body/div/form/div[2]/input')
    input.send_keys('Petrov')
    input = browser.find_element_by_xpath('/html/body/div/form/div[3]/input')
    input.send_keys('Smolensk')
    input = browser.find_element_by_xpath('//*[@id="country"]')
    input.send_keys('Russia')

    button = browser.find_element_by_xpath('/html/body/div/form/div[6]/button[3]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
