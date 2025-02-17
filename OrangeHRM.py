import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service_obj=Service(r"E:\SDET-P\Driver SDET\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
textbox1=driver.find_element(By.NAME,"username")
textbox1.send_keys("Admin")
time.sleep(5)
textbox2=driver.find_element(By.NAME,"password")
textbox2.send_keys("admin123")
time.sleep(5)
Click = driver.find_element(By.CLASS_NAME,"oxd-button")
Click.click()
driver.
# textbox2.send_keys(Keys.RETURN)
time.sleep(5)
