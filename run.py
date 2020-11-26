import sys
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# prepare the option for the chrome driver
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(options=options)
driver.get("https://google.com")

print(driver.title)

print("-----Searching------")

search = driver.find_element_by_name("q")

search_str = sys.argv[1]
pages = int(sys.argv[2])

search.send_keys(search_str)
search.send_keys(Keys.RETURN)

for i in range(pages):
    titles = driver.find_elements_by_xpath("//a/h3");

    for title in titles:
        print(title.text.rstrip())

    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[5]/div[2]/span[1]/div/table/tbody/tr/td[12]/a/span[2]"))
        )
        element.click()
    finally:
        print("-----end page------")

driver.quit()