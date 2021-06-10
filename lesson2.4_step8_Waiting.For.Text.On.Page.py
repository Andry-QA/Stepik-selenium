from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    waiter = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element_by_id("book").click()
    x = int(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(str(calc(x)))
    browser.find_element_by_css_selector("button[type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()