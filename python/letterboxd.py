from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

password = "acz8ehd9fkh.FMW_heb"
username = "frankie.celentano@yahoo.com"

# Set the path to the Chrome WebDriver executable
chrome_driver_path = "/Applications/chromedriver_mac_arm64/chromedriver"

# Create Chrome options and set the page load strategy to 'none'
# options are none, eager, normal
chrome_options = Options()
chrome_options.page_load_strategy = "eager"

# Replace "path_to_webdriver" with the actual path to your Chrome WebDriver executable
driver = webdriver.Chrome(
    options=chrome_options, service=Service(executable_path=chrome_driver_path)
)
driver.get("https://letterboxd.com/")

try:
    # Find the "Sign In" button by its XPath and click it
    sign_in_button = driver.find_element(
        By.XPATH, "//li[@class='navitem sign-in-menu']//a[@class='navlink has-icon']"
    )
    sign_in_button.click()

    # enter username
    input_element = driver.find_element(By.ID, "username")
    input_element.send_keys(username)

    # enter password
    input_element = driver.find_element(By.ID, "password")
    input_element.send_keys(password)

    # Find the "Sign in" button by its class name and value attribute
    sign_in_button = driver.find_element(
        By.CSS_SELECTOR, 'input.button.-action.button-green[value="Sign in"]'
    )
    sign_in_button.click()

    time.sleep(5)
except Exception as e:
    print("Error occurred:", e)

finally:
    # Close the browser window
    driver.quit()
