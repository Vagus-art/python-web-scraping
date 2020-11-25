import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# prepare the option for the chrome driver
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options)
driver.get("https://google.com")
print(driver.title)

search = driver.find_element_by_name("q")

search_str = sys.argv[1]

search.send_keys(search_str)
search.send_keys(Keys.RETURN)

titles = driver.find_elements_by_xpath("//a/h3");

for title in titles:
    print(title.text.rstrip())

driver.quit()