from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Replace "path_to_webdriver" with the actual path to your Chrome WebDriver executable
driver = webdriver.Chrome(
    service=Service(executable_path="/Applications/chromedriver_mac_arm64/chromedriver")
)
driver.get("https://letterboxd.com/")

try:
    sign_in_button = driver.find_element(
        By.XPATH, "//li[@class='navitem sign-in-menu']//a[@class='navlink has-icon']"
    )
    sign_in_button.click()
    time.sleep(50)
except Exception as e:
    print("Error occurred:", e)

finally:
    # Close the browser window
    driver.quit()
