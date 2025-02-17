# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://online.btes.co.in/login/index.php")
# time.sleep(2)
# Login_page = driver.find_element(By.XPATH,"//input[@name='username']").send_keys("amar@123")
# time.sleep(2)
# pass_page = driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Amar@123")
# time.sleep(2)
# Login = driver.find_element(By.XPATH,"//*[@class='btn btn-primary btn-block mt-3']")
# Login.click()
# time.sleep(2)
# act = driver.find_element(By.XPATH,"//*[@class='usertext mr-1']").text
# exp = "Amar Arora"
# if exp == act:
#     print("Test Pass")
# else:
#     print("Test Fail")
# time.sleep(2)
# second_page = driver.find_element(By.XPATH,"//*[@class='card-img dashboard-card-img']")
# second_page.click()
# time.sleep(2)
# actual = driver.find_element(By.XPATH,"//*[@class='page-header-headings']/h1").text
# exp = "SDET with Python-AI for IT&R"
# if exp == actual:
#     print("test Pass after login")
# else:
#     print("test failed bro")
# time.sleep(5)
# driver.close()
# -------------------------------------------------------
# XPATH with OR, AND
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.facebook.com/login/")
# time.sleep(2)
# facebook_user =driver.find_element(By.XPATH,"//input[@name='email' or @id='email']").send_keys("amararora456@gmail.com")
# time.sleep(2)
# facebook_pass =driver.find_element(By.XPATH,"//input[@name='pass' and @tabindex='0']").send_keys("Baldev.1990")
# time.sleep(2)
# Login = driver.find_element(By.XPATH,"//button[@name='login' or @id='loginbutton']")
# Login.click()
# time.sleep(5)
# driver.close()
# -------------------------------------------------
# XPATH with contains()
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.facebook.com/login/")
# time.sleep(2)
# facebook_user =driver.find_element(By.XPATH,"//input[contains(@name,'email')]").send_keys("amararora456@gmail.com")
# time.sleep(2)
# facebook_pass =driver.find_element(By.XPATH,"//input[contains(@name,'pass')]").send_keys("Baldev.1990")
# time.sleep(2)
# Login = driver.find_element(By.XPATH,"//button[contains(text(),'Log in')]")
# Login.click()
# time.sleep(5)
# driver.close()
# -----------------------------------------------------------
# XPATH with text()
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.facebook.com/login/")
# time.sleep(2)
# facebook_user =driver.find_element(By.XPATH,"//input[contains(@name,'email')]").send_keys("amararora456@gmail.com")
# time.sleep(2)
# facebook_pass =driver.find_element(By.XPATH,"//input[contains(@name,'pass')]").send_keys("Baldev.1990")
# time.sleep(2)
# Login = driver.find_element(By.XPATH,"//button[text()='Log in']")
# Login.click()
# time.sleep(5)
# driver.close()
# -----------------------------------------------------
# XPATH with starts-with
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.facebook.com/login/")
# time.sleep(2)
# facebook_user =driver.find_element(By.XPATH,"//input[starts-with(@name,'email')]").send_keys("amararora456@gmail.com")
# time.sleep(2)
# facebook_pass =driver.find_element(By.XPATH,"//input[starts-with(@name,'pass')]").send_keys("Baldev.1990")
# time.sleep(2)
# Login = driver.find_element(By.XPATH,"//button[starts-with(text(),'Log in')]")
# Login.click()
# time.sleep(5)
# driver.close()
# -----------------------------------------------------
# XPATH with ends-with
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.facebook.com/login/")
# time.sleep(2)
# facebook_user =driver.find_element(By.XPATH,"//input[ends-with(@name,'email')]").send_keys("amararora456@gmail.com")
# time.sleep(2)
# facebook_pass =driver.find_element(By.XPATH,"//input[endss-with(@name,'pass')]").send_keys("Baldev.1990")
# time.sleep(2)
# Login = driver.find_element(By.XPATH,"//button[ends-with(text(),'in')]")
# Login.click()
# time.sleep(5)
# driver.close()
# ------------------------------------------------------
# XPATH Nodes/Axes
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver= webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://money.rediff.com/gainers/bse/daily/groupall")
# time.sleep(2)
# self_name = driver.find_element(By.XPATH,"//*[contains(text(),'Olympic Cards Ltd.')]").text
# print(self_name)
# parent = driver.find_element(By.XPATH,"//*[@href=\"//money.rediff.com/companies/olympic-cards-ltd/17028056\"]/parent::*")
# print("Parent: ",parent.tag_name)
# print(len(parent.tag_name))
# time.sleep(2)
# following = driver.find_element(By.XPATH,r'//*[@href="//money.rediff.com/companies/olympic-cards-ltd/17028056"]/following::*')
# print("Following: ",following.tag_name)
# print(len(following.tag_name))
# time.sleep(2)
# preceding = driver.find_elements(By.XPATH,"//*[@href=\"//money.rediff.com/companies/olympic-cards-ltd/17028056\"]/preceding::*")
# # print("Preceding: ",preceding.tag_name)
# for i in preceding:
#     print("Preceding: ",i.tag_name)
#     print("Preceding Length: ",len(i.tag_name))
# time.sleep(2)
# Ancestor = driver.find_elements(By.XPATH,"//*[@href=\"//money.rediff.com/companies/olympic-cards-ltd/17028056\"]/ancestor::*")
# for i in Ancestor:
#     print("Ancestor: ",i.tag_name)
# time.sleep(2)
# driver.close()

# -----------------------------------------------------------
# Homework of XPATH axes:
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/login/")
time.sleep(2)
preceding_element = driver.find_elements(By.XPATH,"//input[@name='email']/preceding::*")
count = 0
for i in preceding_element:
    count += 1
    print(f"Preceding Tag Names are: {i.tag_name} and Count is: {count}")
print(f"Total Elements are: {count}\n")

time.sleep(2)
user_name = driver.find_element(By.XPATH,"//input[@name='email']").send_keys("amararora456@gmail.com")
following_element = driver.find_elements(By.XPATH,"//input[@name='email']/following::*")
count = 0
for i in following_element:
    count+=1
    print(f"Following Tag Names are: {i.tag_name} and its Respective Count is: {count}")
print(f"Total Elements are: {count}")
time.sleep(2)
driver.close()



