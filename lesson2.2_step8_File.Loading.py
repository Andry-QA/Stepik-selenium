from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    fields = browser.find_elements_by_css_selector("input[type='text']")
    for field in fields:
        field.send_keys("valid data")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'example.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_css_selector("button[type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()