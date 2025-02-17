# Static Dropdown by using Select class and options tag for available options

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# driver=webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# state = Select(driver.find_element(By.XPATH,"//select[@id='country']"))
# state.select_by_visible_text("India")
# All_options = state.options
# for i in All_options:
#     print(i.text)
# time.sleep(5)
# driver.quit()

# --------------------------------------------------------------------------------------------

# Dynamic Dropdown Example

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://example.com/dynamic-dropdown")
# dropdown_button = driver.find_element(By.ID, "dropdown_button_id")
# dropdown_button.click()
# option = driver.find_element(By.XPATH, "//div[text()='Option 1']")
# option.click()
# driver.quit()

# -------------------------------------------------------
# Dynamic Checkboxes
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "subscribe")))
# checkbox.click()
# print("Checkbox clicked after dynamic loading.")

# -------------------------------------------------------------------------------------------

# Handling Checkbox Groups
# if u want to select all Checkboxes

# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# for checkbox in checkboxes:
#     if not checkbox.is_selected():
#         checkbox.click()

# Alternative Way

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# Checkbox = driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
# for i in range(len(Checkbox)):
#     Checkbox[i].click()
# time.sleep(2)
# driver.close()

# -------------------------------------------------------------------------------------

# Select the specific checkboxes

# checkbox = driver.find_element(By.XPATH, "//input[@value='Option1']")
# checkbox.click()
# print("Option1 checkbox selected.")

# --------------------------------------------------------

# Select Checkboxes by Choice

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
# Checkbox = driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
# for i in Checkbox:
#     week_name = i.get_attribute("id")
#     if week_name== "wednesday" or week_name== "saturday":
#         i.click()
# time.sleep(10)
# driver.close()

# ------------------------------------------------------------------------

# Hidden Checkboxes:

# Some checkboxes may be hidden with CSS (display: none) or placed off-screen.
# Use JavaScript to interact with such elements:
# driver.execute_script("arguments[0].click();", checkbox)
