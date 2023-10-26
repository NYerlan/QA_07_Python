import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from data import LOGIN, PASSWORD, MAIN_PAGE


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    print('\nquit browser...')
    driver.quit()


@pytest.fixture
def login(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    time.sleep(1)
    yield driver
    # driver.close()
