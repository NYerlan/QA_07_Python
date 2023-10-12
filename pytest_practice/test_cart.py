from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_add_to_cart():
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//input[@data-test="username"]')\
        .send_keys("standard_user")

    driver.find_element(By.XPATH, '//input[@data-test="password"]')\
        .send_keys("secret_sauce")

    driver.find_element(By.XPATH, '//input[@data-test="login-button"]')\
        .click()

    time.sleep(1)

    driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
