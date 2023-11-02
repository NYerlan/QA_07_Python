from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_visible_after_with_implicit_wait(driver):
    driver.get('https://victoretc.github.io/selenium_waits')
    visible_after_button = driver.find_element(By.ID, 'startTest')
    assert visible_after_button.is_enabled()

    driver.find_element(By.ID, 'startTest').click()
    title = driver.find_element(By.TAG_NAME, 'h1').text
    assert title == 'Практика с ожиданиями в Selenium'

    driver.find_element(By.ID, 'login').send_keys("user")
    driver.find_element(By.ID, 'password').send_keys('resu')
    driver.find_element(By.ID, 'agree').click()
    driver.find_element(By.ID, 'register').click()
    loader = driver.find_element(By.ID, 'loader').text
    assert loader == 'Загрузка...'

    # while not driver.find_element(By.ID, 'successMessage').is_displayed():
    #     continue

    success_registration = driver.find_element(By.XPATH, '//p[@id="successMessage"][@class=""]').text

    assert success_registration == 'Вы успешно зарегистрированы!'
