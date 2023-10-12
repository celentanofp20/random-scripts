from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time


# run p3 letterdoxd_login.py
def login_to_letterboxd(username, password):
    # Create Chrome options and set the page load strategy to 'none'
    # options are none, eager, normal
    chrome_options = Options()
    chrome_options.page_load_strategy = "eager"
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    # Set the desired width and height for the window (in pixels)
    width = 1200
    height = 400

    # Set the window size using the set_window_size() method
    driver.set_window_size(width, height)

    driver.get("https://letterboxd.com/")

    try:
        # Find the "Sign In" button by its XPath and click it
        sign_in_button = driver.find_element(
            By.XPATH,
            "//li[@class='navitem sign-in-menu']//a[@class='navlink has-icon']",
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

        # Wait for the completion of the document request
        wait = WebDriverWait(
            driver, 30
        )  # Replace 30 with the maximum waiting time in seconds
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".navitem.nav-account.js-nav-account")
            )
        )

        # get avatar name
        # Find the parent element with the class name
        parent_element = driver.find_element(
            By.CSS_SELECTOR, ".navitem.nav-account.js-nav-account"
        )

        # Find the first <a> tag within the parent element using XPath
        avatar_element = parent_element.find_element(By.XPATH, "./a[1]")

        # Get the text value of the first <a> tag
        avatar_text = avatar_element.text

        # go to films
        driver.get("https://letterboxd.com/%s/films" % avatar_text)

        # Wait for the completion of the document request
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "ul.poster-list.-p70.-grid.film-list.clear")
            )
        )

        time.sleep(5)
        return driver

    except Exception as e:
        print("Error occurred:", e)

    # finally:
    #     # Close the browser window
    #     driver.quit()


if __name__ == "__main__":
    password = "acz8ehd9fkh.FMW_heb"
    username = "frankie.celentano@yahoo.com"
    login_to_letterboxd(username, password)


# TODO
# refetch list items if source contains empty poster
