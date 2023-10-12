from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_login_correct():
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//input[@data-test="username"]')\
        .send_keys("standard_user")

    driver.find_element(By.XPATH, '//input[@data-test="password"]')\
        .send_keys("secret_sauce")

    driver.find_element(By.XPATH, '//input[@data-test="login-button"]')\
        .click()

    time.sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    driver.quit()

def test_login_incorrect():
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//input[@data-test="username"]') \
            .send_keys("user")

    driver.find_element(By.XPATH, '//input[@data-test="password"]') \
            .send_keys("user")

    driver.find_element(By.XPATH, '//input[@data-test="login-button"]') \
            .click()

    time.sleep(3)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    driver.quit()