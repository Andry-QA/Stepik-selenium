from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_tag_name("button").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    x = int(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(str(calc(x)))
    browser.find_element_by_css_selector("button[type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()