# checkout_test.py – SauceCart QA Project
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Proceed to checkout
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("Kavya")
driver.find_element(By.ID, "last-name").send_keys("Bakshi")
driver.find_element(By.ID, "postal-code").send_keys("R3T0L6")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()

# Verify success
assert "checkout-complete" in driver.current_url
print("Checkout test passed.")
driver.quit()

