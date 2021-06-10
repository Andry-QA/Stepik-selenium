from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    pic = browser.find_element_by_tag_name("img")
    x = int(pic.get_attribute("valuex"))
    y = calc(x)
    filed = browser.find_element_by_id("answer")
    filed.send_keys(y)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    time.sleep(1)
    browser.find_element_by_css_selector("button[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()