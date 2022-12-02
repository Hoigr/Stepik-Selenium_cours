from selenium import webdriver
import time

#link = 'http://suninjuly.github.io/registration2.html'
link = 'http://suninjuly.github.io/registration1.html'
try:
    broweser = webdriver.Chrome()
    broweser.get(link)

    input = broweser.find_element_by_tag_name("input[placeholder = 'Input your name']")
    input.send_keys('NAME')
    input = broweser.find_element_by_tag_name("input[placeholder = 'Input your email']")
    input.send_keys('microsoft@ms.com')

    button = broweser.find_element_by_css_selector('button.btn')
    button.click()
    time.sleep(5)

    welcome_text_elm = broweser.find_element_by_tag('h1')
    welcome_text = welcome_text_elm.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(25)
#    broweser.quit()    