from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(calc(x))
    button = browser.find_element_by_css_selector("button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_css_selector("[for='robotsRule']").click()
    button.click()

finally:
    time.sleep(5)
    browser.quit()