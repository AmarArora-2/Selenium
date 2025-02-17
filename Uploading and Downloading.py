from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
#
# location = os.getcwd()
# def Chrome_setup():
#     prefernces = {"download.default_directory":location}
#     ops = webdriver.ChromeOptions()
#     ops.add_experimental_option("prefs",prefernces)
#     driver = webdriver.Chrome(options=ops)
#     return driver
#
# def Edge_setup():
#     preferences = {"download.default_directory":location}
#     ops = webdriver.ChromeOptions()
#     # ops.add_argument("--download.default_directory":)
#     ops.add_experimental_option("prefs",preferences)
#     driver = webdriver.Chrome(options=ops)
#     return driver
# driver = Chrome_setup()
# driver.get("https://unsplash.com/photos/a-couple-of-cars-parked-in-front-of-a-building-mwJBOWcAN6U")
# time.sleep(5)
# button = driver.find_element(By.XPATH,"//a[normalize-space()='Download free']")
# button.click()
# time.sleep(10)
# driver.quit()




# --------------------------------------------------------------------

driver = webdriver.Chrome()
driver.get("https://www.filemail.com/features/upload-files")
driver.maximize_window()
file_input = driver.find_element(By.XPATH,"//div[@role='presentation']")
file_path = r"C:\Users\Amar\Documents\Rescued document.doc"
file_input.send_keys(file_path)
time.sleep(10)
driver.quit()