import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

# Service("")
# Approach-1
service_obj= Service(r"E:\SDET-P\Driver SDET\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.google.com/")
text_box = driver.find_element(By.NAME,"q")
text_box.send_keys("selenium")
time.sleep(5)
Click = driver.find_element(By.NAME,"btnK")
Click.click()
exp_title = 'selenium - Google Search'
act_title = driver.title
.is_pr
if act_title == exp_title:
    print("Test Pass")
else:
    print("Test Failed")
# driver.find_element(By.NAME,"q").send_keys("Virat Kohli")

# optionsl approach only for learning process
time.sleep(5)



# Approach-2
# Latest Approach
# this will open the browser
# driver = webdriver.Chrome()


