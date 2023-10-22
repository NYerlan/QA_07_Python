from selenium.webdriver.common.by import By
from locators import *


def test_filter_az(driver, login):
    driver.find_element(By.XPATH, FILTER_BUTTON).click()
    driver.find_element(By.XPATH, FILTER_AZ_DROPDOWN).click()
    items_name_list = driver.find_elements(By.XPATH, ITEMS_NAME_LIST)

    items_name = [element.text for element in items_name_list]
    sorted_az_list = sorted(items_name)

    assert items_name == sorted_az_list


def test_filter_za(driver, login):
    driver.find_element(By.XPATH, FILTER_BUTTON).click()
    driver.find_element(By.XPATH, FILTER_ZA_DROPDOWN).click()
    items_name_list = driver.find_elements(By.XPATH, ITEMS_NAME_LIST)

    items_name = [element.text for element in items_name_list]
    sorted_za_list = sorted(items_name, reverse=True)

    assert items_name == sorted_za_list


def test_filter_low_high_prices(driver, login):
    driver.find_element(By.XPATH, FILTER_BUTTON).click()
    driver.find_element(By.XPATH, FILTER_PRICE_LOW_HIGH_DROPDOWN).click()
    items_price_list = driver.find_elements(By.XPATH, ITEMS_PRICE_LIST)

    items_price = [element.text for element in items_price_list]
    numeric_prices = [float(price.replace('$', '')) for price in items_price]

    # Sort the list of numeric prices
    sorted_numeric_prices_low_high = sorted(numeric_prices)

    # Optionally, convert them back to strings with the '$' symbol
    sorted_prices_low_high = [f'${price:.2f}' for price in sorted_numeric_prices_low_high]

    assert items_price == sorted_prices_low_high


def test_filter_high_low_prices(driver, login):
    driver.find_element(By.XPATH, FILTER_BUTTON).click()
    driver.find_element(By.XPATH, FILTER_PRICE_HIGH_LOW_DROPDOWN).click()
    items_price_list = driver.find_elements(By.XPATH, ITEMS_PRICE_LIST)

    items_price = [element.text for element in items_price_list]
    numeric_prices = [float(price.replace('$', '')) for price in items_price]

    # Sort the list of numeric prices
    sorted_numeric_prices_high_low = sorted(numeric_prices, reverse=True)

    # Optionally, convert them back to strings with the '$' symbol
    sorted_prices_high_low = [f'${price:.2f}' for price in sorted_numeric_prices_high_low]

    assert items_price == sorted_prices_high_low
