from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

import time

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    return driver

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=20)
    return wait

def test_visible_after_with_explicit_waits(driver, wait):
    driver.get('https://victoretc.github.io/selenium_waits')
    visible_after_button = wait.until(EC.element_to_be_clickable((By.ID, 'startTest')))

    assert visible_after_button.text == 'Начать тестирование'

    driver.find_element(By.ID, 'startTest').click()
    title = driver.find_element(By.TAG_NAME, 'h1').text
    assert title == 'Практика с ожиданиями в Selenium'

    driver.find_element(By.ID, 'login').send_keys("user")
    driver.find_element(By.ID, 'password').send_keys('resu')
    driver.find_element(By.ID, 'agree').click()
    driver.find_element(By.ID, 'register').click()
    loader = driver.find_element(By.ID, 'loader').text
    assert loader == 'Загрузка...'

    wait.until(EC.visibility_of_element_located((By.ID, 'successMessage')))
    success_registration = driver.find_element(By.ID, 'successMessage').text

    assert success_registration == 'Вы успешно зарегистрированы!'



