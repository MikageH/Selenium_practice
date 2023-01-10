from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def formula(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(2)
    alert = driver.switch_to.alert  # switches to a modal window
    alert.accept() # closes the window by accepting it
    input = driver.find_element(By.ID, "input_value").text
    ans = formula(input)
    driver.find_element(By.ID, "answer").send_keys(ans)
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(3)
    print(driver.switch_to.alert.text)
finally:
    driver.quit()