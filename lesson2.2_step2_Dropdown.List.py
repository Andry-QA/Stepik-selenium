from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link1 = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html?"
choice = 1

try:
    browser = webdriver.Chrome()
    if choice == 1:             #Список с выпадающим окном вариантов ответов
        browser.get(link1)
        browser.find_element_by_id("dropdown").click()
    if choice == 2:             #Список с сразу открытыми вариантами
        browser.get(link2)
    x = int(browser.find_element_by_id("num1").text)
    y = int(browser.find_element_by_id("num2").text)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(x+y))
    browser.find_element_by_css_selector("button[type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()