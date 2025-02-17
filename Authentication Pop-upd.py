# Authentication pop-ups are browser-level dialogs. You can include the credentials in the URL to handle them:
# driver.get("https://username:password@example.com")

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
driver=webdriver.Chrome()
driver.maximize_window()
url = driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)
expedtedline= "Congratulations! You must have the proper credentials."
actualline=driver.find_element(By.XPATH,'//*[@id="content"]/div/p').text
print(actualline)
if expedtedline==actualline:
    print('passed')
else:
    print('failed')
driver.quit()

# ----------------------------------------------------------------------------------------

# usingtitle
# url= 'https://the-internet.herokuapp.com/basic_auth'
# expedtedtitle = "The Internet"
# if expedtedtitle == driver.title:
#     print('passed')
# else:
#     print('failed')