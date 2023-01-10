import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# for this way to work the file needs to be in the same directory as executive file (your code)
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    inputs = browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    for i in inputs:
        i.send_keys("QA")
    current_dir = os.path.abspath(os.path.dirname(__file__)) # adds an absolute path
    file_name = "tips.txt"
    file_path = os.path.join(current_dir, file_name) # gathers together name and dir
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(10)
finally:
    browser.quit()