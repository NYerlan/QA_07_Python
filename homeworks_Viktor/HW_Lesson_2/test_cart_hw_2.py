from selenium.webdriver.common.by import By
from locators import *


def test_add_to_cart(driver, login):
    text_before = driver.find_element(By.XPATH, ITEM_1_TITLE).text

    driver.find_element(By.XPATH, ITEM_1_ADD_BUTTON).click()

    driver.find_element(By.XPATH, CART_LOGO).click()

    text_after = driver.find_element(By.XPATH, ITEM_1_TITLE).text

    assert text_before == text_after


def test_delete_item(driver, login):
    driver.find_element(By.XPATH, ITEM_1_ADD_BUTTON).click()
    driver.find_element(By.XPATH, CART_LOGO).click()

    driver.find_element(By.XPATH, ITEM_1_DELETE_BUTTON).click()
    text_after = driver.find_element(By.XPATH, '//div[@class="removed_cart_item"]').is_displayed()
    assert text_after == False


def test_add_to_cart_from_item_view(driver, login):
    item_name_before = driver.find_element(By.ID, 'item_0_title_link').text
    driver.find_element(By.ID, 'item_0_title_link').click()
    item_name_in_cart = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Bike Light")]').text

    assert item_name_before == item_name_in_cart

    driver.find_element(By.XPATH, ADD_TO_CART_BUTTON).click()
    item_in_cart_badge = driver.find_element(By.XPATH, ITEMS_IN_CART_BADGE)

    assert item_in_cart_badge.is_displayed()

    driver.find_element(By.XPATH, CART_LOGO).click()
    item_name_in_cart = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Bike Light")]').text

    assert item_name_before == item_name_in_cart


def test_delete_from_cart_from_item_view(driver, login):
    item_name_before = driver.find_element(By.ID, 'item_0_title_link').text
    driver.find_element(By.ID, 'item_0_title_link').click()

    driver.find_element(By.XPATH, ADD_TO_CART_BUTTON).click()

    driver.find_element(By.XPATH, CART_LOGO).click()
    item_name_in_cart = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Bike Light")]').text

    assert item_name_before == item_name_in_cart

    driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Bike Light")]').click()
    driver.find_element(By.XPATH, REMOVE_FROM_CART_BUTTON).click()
    driver.find_element(By.XPATH, CART_LOGO).click()
    element_before_item = driver.find_element(By.CSS_SELECTOR, '.cart_quantity_label')
    element_after_item = driver.find_element(By.CSS_SELECTOR, '.cart_desc_label')
    elements_between = driver.find_element(By.CSS_SELECTOR, '.cart_quantity_label ~ .cart_desc_label')

    # assert not elements_between
