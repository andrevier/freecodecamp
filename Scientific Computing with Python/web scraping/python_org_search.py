# Example with Selenium from
# https://selenium-python.readthedocs.io/getting-started.html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Use the chrome drive that is in this path.
driver = webdriver.Chrome('chromedriver.exe')
driver.get("http://www.python.org")

# Asure the title name.
print('title: ', driver.title)

# If the title has a "python" in it.
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
input("Press enter...")
driver.close()