from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_css_selector("input")
    i = 1
    for element in elements:
        if i % 2 == 0:
            element.send_keys("Зачем")
        elif i % 3 == 0:
            element.send_keys("Почему")
        else:
            element.send_keys("Что")
        i += 1
        if i > 3:
            i = 1
#  element.send_keys("Мой ответ")
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()