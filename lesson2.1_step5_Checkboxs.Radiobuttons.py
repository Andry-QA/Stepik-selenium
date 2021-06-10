from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_web = browser.find_element_by_id("input_value")
    x = int(x_web.text)
    y = calc(x)
    filed = browser.find_element_by_id("answer")
    filed.send_keys(y)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_css_selector("[for='robotsRule']").click()
    time.sleep(1)
    browser.find_element_by_css_selector("button[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()
