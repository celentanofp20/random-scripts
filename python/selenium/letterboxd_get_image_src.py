from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.webdriver.chrome.webdriver import WebDriver


def get_image_src(driver: WebDriver):
    # Find the ul element with the specified class name
    ul_element = driver.find_element(
        By.CSS_SELECTOR, "ul.poster-list.-p70.-grid.film-list.clear"
    )

    # Find all the li elements within the ul element
    li_elements = ul_element.find_elements(By.TAG_NAME, "li")

    # Get the count of movies on page
    li_count = len(li_elements)
    print(f"Count of movies: {li_count}")

    # Loop through each li element and get the image src
    for li_element in li_elements:
        # Find the img element within the provided element
        img_element = li_element.find_element(By.TAG_NAME, "img")

        # Get the value of the src attribute of the img element
        img_src = img_element.get_attribute("src")
        print("Image URL:", img_src)


# def get_image_src(element):
#     try:
#         # Find the img element within the provided element
#         img_element = element.find_element(By.TAG_NAME, "img")

#         # Get the value of the src attribute of the img element
#         img_src = img_element.get_attribute("src")
#         print("Image URL:", img_src)

#     except StaleElementReferenceException:
#         print("caught ex")
#         # Retry finding the img element in case of a StaleElementReferenceException
#         get_image_src(element)
