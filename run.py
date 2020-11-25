from selenium import webdriver
PATH = "chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://google.com")
print(driver.title)
driver.quit()