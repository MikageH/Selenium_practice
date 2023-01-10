import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    print("\nquitting")
    driver.quit()
