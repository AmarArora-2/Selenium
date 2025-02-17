# 1. switch_to.frame()
# Switches the context to the specified frame.
# Options for Selecting Frames:
# By index (zero-based).
# By name or ID.
# By WebElement.
# 2. switch_to.default_content()
# Switches the context back to the main page from a frame.
# 3. switch_to.parent_frame()
# Switches the context to the parent frame, useful for nested frames.

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frameID")))

# General Frame

# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://www.hyrtutorials.com/p/frames-practice.html#google_vignette")
# frame=driver.find_element(By.ID,"frm1")
# driver.switch_to.frame(frame)
# s=Select(driver.find_element(By.ID,"selectnav1"))
# op=s.options
# for i in op:
#     # print(i.text)
#     if i.text=="- Java":
#         i.click()
#         break
# time.sleep(5)
# driver.switch_to.default_content()
#
# frame2=driver.find_element(By.ID,"frm2")
# driver.switch_to.frame(frame2)
# driver.find_element(By.ID,"firstName").send_keys("AMAR")
# driver.find_element(By.ID,"lastName").send_keys("ARORA")
# time.sleep(5)

# ------------------------------------------------------------

# Embedded Frame

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
a = driver.find_elements(By.XPATH,"//*[@class='analystic']")
a[1].click()
time.sleep(2)
f1=driver.find_element(By.XPATH,'//*[@id="Multiple"]/iframe')
driver.switch_to.frame(f1)
time.sleep(2)
f2=driver.find_element(By.XPATH,"//*[@class='iframe-container']/iframe")
driver.switch_to.frame(f2)
time.sleep(2)
driver.find_element(By.XPATH,"//input").send_keys("AMAR")
time.sleep(2)
driver.switch_to.default_content()
driver.quit()
