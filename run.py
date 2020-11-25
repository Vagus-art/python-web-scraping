from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://google.com")
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("hello world")
search.send_keys(Keys.RETURN)

print(driver.title)

driver.quit()