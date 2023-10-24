import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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


def test_visible_after_with_time_sleep(driver):
    driver.get('https://victoretc.github.io/selenium_waits')
    time.sleep(10)
    visible_after_button = driver.find_element(By.ID, 'startTest').text

    assert visible_after_button == 'Начать тестирование'

    driver.find_element(By.ID, 'startTest').click()
    title = driver.find_element(By.TAG_NAME, 'h1').text

    assert title == 'Практика с ожиданиями в Selenium'

    driver.find_element(By.ID, 'login').send_keys("user")
    driver.find_element(By.ID, 'password').send_keys('resu')
    driver.find_element(By.ID, 'agree').click()
    driver.find_element(By.ID, 'register').click()
    loader = driver.find_element(By.ID, 'loader').text

    assert loader == 'Загрузка...'

    time.sleep(5)

    success_registration = driver.find_element(By.ID, 'successMessage').text

    assert success_registration == 'Вы успешно зарегистрированы!'
