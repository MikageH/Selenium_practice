import pytest
from selenium.webdriver.common.by import By
import time
import math


@pytest.mark.parametrize('links', ['236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_check_answers(driver, links):
    link = f"https://stepik.org/lesson/{links}/step/1"
    email = ""  # your email on Stepic
    password = ""  # your password on Stepic
    driver.get(link)
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "navbar__auth_login").click()
    driver.find_element(By.ID, "id_login_email").send_keys(email)
    driver.find_element(By.ID, "id_login_password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "sign-form__btn").click()
    time.sleep(7)
    driver.find_element(By.TAG_NAME, "textarea").send_keys(str(math.log(int(time.time()))))
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "submit-submission").click()
    time.sleep(3)
    pieces = driver.find_element(By.CLASS_NAME, "smart-hints__hint").text
    if pieces != "Correct":
        print(pieces)
