# Implicit Wait

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# service_obj=Service(r"E:\SDET-P\Driver SDET\chromedriver-win64\chromedriver.exe")
# driver=webdriver.Chrome(service=service_obj)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.implicitly_wait(2)
# textbox1=driver.find_element(By.NAME,"username")
# textbox1.send_keys("Admin")
# textbox2=driver.find_element(By.NAME,"password")
# textbox2.send_keys("admin123")
# Click = driver.find_element(By.CLASS_NAME,"oxd-button")
# Click.click()
# textbox2.send_keys(Keys.RETURN)

# --------------------------------------------------------------------------------

# Explicit Wait

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# service_obj = Service(r"E:\SDET-P\Driver SDET\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.google.com/")
# mywait = WebDriverWait(driver,timeout=2)
# link = mywait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='gLFyf']")))
# link.send_keys("Cricbuzz")
# time.sleep(2)
# driver.close()

# ---------------------------------------------------
# Fluent wait

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# mywait = WebDriverWait(driver,timeout=5, poll_frequency=.2,ignored_exceptions=[Exception])
# username = mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))
# username.send_keys("Admin")
# password_hrm = mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
# password_hrm.send_keys("admin123")
# Login = mywait.until(EC.presence_of_element_located((By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")))
# Login.click()
# time.sleep(5)
# driver.close()

# ----------------------------------------------------------------------------------
# Fluent Wait

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver=webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# mywait = WebDriverWait(driver,timeout=5,poll_frequency=.2, ignored_exceptions=[Exception])
# username = mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))
# username.send_keys("Admin")
# password_hrm = mywait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
# password_hrm.send_keys("admin123")
# Login = mywait.until(EC.presence_of_element_located((By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")))
# Login.click()
# time.sleep(5)
# driver.close()