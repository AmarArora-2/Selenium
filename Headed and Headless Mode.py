# headless speed is more in execution time than headed mode
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")
    driver = webdriver.Chrome(options=ops)
    return driver
driver = headless_chrome()
driver.get("https://www.google.com/")
print(driver.title)


def headless_edge():
    ops = webdriver.EdgeOptions()
    ops.add_argument("--headless")
    driver = webdriver.Edge(options=ops)
    return driver
driver = headless_edge()
driver.get("https://www.cricbuzz.com/")
print(driver.title)

driver.quit()

