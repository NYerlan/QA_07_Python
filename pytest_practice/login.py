from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def login():
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//input[@data-test="username"]')\
        .send_keys("standard_user")

    driver.find_element(By.XPATH, '//input[@data-test="password"]')\
        .send_keys("secret_sauce")

    driver.find_element(By.XPATH, '//input[@data-test="login-button"]')\
        .click()

    time.sleep(1)
