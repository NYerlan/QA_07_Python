import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


@pytest.fixture
def login():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.XPATH, '//input[@data-test="username"]') \
        .send_keys("standard_user")
    driver.find_element(By.XPATH, '//input[@data-test="password"]') \
        .send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//input[@data-test="login-button"]') \
        .click()
    time.sleep(1)
    yield
    driver.close()


def test_add_to_cart(login):
    text_before = driver.find_element(By.XPATH, '//a[@id="item_1_title_link"]').text

    driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()

    text_after = driver.find_element(By.XPATH, '//a[@id="item_1_title_link"]').text

    assert text_before == text_after


def test_delete_item(login):
    driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()

    driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-bolt-t-shirt"]').click()
    text_after = driver.find_element(By.XPATH, '//div[@class="removed_cart_item"]').is_displayed()
    assert text_after == False


def test_add_to_cart_from_item_view(login):
    item_name_before = driver.find_element(By.ID, 'item_0_title_link').text
    driver.find_element(By.ID, 'item_0_title_link').click()
    item_name_in_cart = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Bike Light")]').text

    assert item_name_before == item_name_in_cart

    driver.find_element(By.XPATH, '//button[contains(text(), "Add to cart")]').click()
    item_in_cart_badge = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')

    assert item_in_cart_badge.is_displayed()

    driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    item_name_in_cart = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Bike Light")]').text

    assert item_name_before == item_name_in_cart


def test_delete_from_cart_from_item_view(login):
    item_name_before = driver.find_element(By.ID, 'item_0_title_link').text
    driver.find_element(By.ID, 'item_0_title_link').click()

    driver.find_element(By.XPATH, '//button[contains(text(), "Add to cart")]').click()

    driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    item_name_in_cart = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Bike Light")]').text

    assert item_name_before == item_name_in_cart

    driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Bike Light")]').click()
    driver.find_element(By.XPATH, '//button[contains(text(), "Remove")]').click()
    driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]').click()
    element_before_item = driver.find_element(By.CSS_SELECTOR, '.cart_quantity_label')
    element_after_item = driver.find_element(By.CSS_SELECTOR, '.cart_desc_label')
    elements_between = driver.find_element(By.CSS_SELECTOR, '.cart_quantity_label ~ .cart_desc_label')

    # assert not elements_between
