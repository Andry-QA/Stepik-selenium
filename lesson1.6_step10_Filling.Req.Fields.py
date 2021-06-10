from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
case = 1

try:
    browser = webdriver.Chrome()
    browser.get(link2)

    if case == 1:                         # case1: only required fields
        elements = browser.find_elements_by_css_selector("input[required]")
        for element in elements:
            element.send_keys("valid data")
        button = browser.find_element_by_tag_name("button")
        time.sleep(5)
        button.click()
        time.sleep(2)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert welcome_text == "Congratulations! You have successfully registered!"

    if case == 2:                         # case2: only not required fields
        elements = browser.find_elements_by_css_selector("input:not(input[required])")
        for element in elements:
            element.send_keys("any data")
        button = browser.find_element_by_tag_name("button")
        time.sleep(5)
        button.click()
        time.sleep(2)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert welcome_text == "Congratulations! You have successfully registered!"

    if case == 3:                         # case3: all fields
        elements = browser.find_elements_by_tag_name("input")
        for element in elements:
            element.send_keys("valid data")
        button = browser.find_element_by_tag_name("button")
        time.sleep(5)
        button.click()
        time.sleep(2)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert welcome_text == "Congratulations! You have successfully registered!"

finally:
    time.sleep(5)
    browser.quit()