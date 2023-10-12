from selenium.webdriver.chrome.service import Service

import time

from selenium import webdriver

#  was necessary in old version of selenium and chrome driver had to match installed version
# not necessary in new selenium: https://stackoverflow.com/questions/77111127/how-can-we-download-chromedriver-117
service = Service()
driver = webdriver.Chrome(
    service=Service(executable_path="/Applications/chromedriver_mac_arm64/chromedriver")
)


driver.get("http://www.google.com/")
# time.sleep(5)  # Let the user actually see something!
# search_box = driver.find_element_by_name("q")

# search_box.send_keys("ChromeDriver")

# search_box.submit()

time.sleep(5)  # Let the user actually see something!

driver.quit()
