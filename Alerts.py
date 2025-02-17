# Handle Simple Alerts

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.alert import Alert
# driver = webdriver.Chrome()
# driver.get("https://example.com")
# button = driver.find_element(By.ID, "trigger-alert")
# button.click()
# alert = Alert(driver)
# print(f"Alert message: {alert.text}")
# alert.accept()
# print("Alert accepted.")
# driver.quit()
# ----------------------------------------------------------------------

# Explicit Wait for Alerts
# Sometimes alerts may take time to appear. Use explicit waits to handle such scenarios.

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# WebDriverWait(driver, 10).until(EC.alert_is_present())
# alert = Alert(driver)
# alert.accept()

# ---------------------------------------------------------------------------------------

# Example

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://example.com")
# Handle a simple alert
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = Alert(driver)
print(f"Alert message: {alert.text}")
alert.accept()
# Trigger and dismiss a confirmation alert
driver.find_element(By.ID, "trigger-confirm").click()
alert = Alert(driver)
alert.dismiss()
# Trigger a prompt alert, send text, and accept it
driver.find_element(By.ID, "trigger-prompt").click()
alert = Alert(driver)
alert.send_keys("Test input")
alert.accept()
driver.quit()

# ------------------------------------------------------------------------------

# Example

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice-automation.com/popups/")
driver.find_element(By.XPATH,"//button[@class='custom_btn btn_hover']").click()
time.sleep(2)
alert = Alert(driver)
time.sleep(5)
alert.accept()
driver.find_element(By.XPATH,"//button[@id='confirm']").click()
time.sleep(5)
Confirm = Alert(driver)
Confirm.dismiss()
driver.find_element(By.XPATH,"//button[@id='prompt']").click()
time.sleep(2)
Prompt = Alert(driver)
Prompt.send_keys("Amar")
Prompt.accept()
Expected = "Nice to meet you, Amar!"
actual = driver.find_element(By.XPATH,"//*[@id='promptResult']").text
if Expected == actual:
    print("Passes")
else:
    print("Failed")
time.sleep(5)
driver.close()