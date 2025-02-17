# Assertion means validation
# use keyword: assert
# Mouse and keyboard events:
# writing built is not necessaary before perform. the steps created by built will execute by perform
# ActionChains class
# mouse hover
# right click
# double click
# drag and drop
# scroller
# slider
import time

# Keyboard unit
# ctrl+a,tab,enter

# Mouse Hover

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# time.sleep(5)
# computer = driver.find_element(By.XPATH,'//a[@href=\'/computers\']')
# Notebook = driver.find_element(By.XPATH,'//a[@href=\'/notebooks\']')
# time.sleep(5)
# act = ActionChains(driver)
# act.move_to_element(computer).move_to_element(Notebook).click().perform()
# time.sleep(5)
# driver.quit()

# ------------------------------------------------------------------------

# Right Click
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.alert import Alert
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# time.sleep(5)
# rightclick = driver.find_element(By.XPATH,"//*[@class='context-menu-one btn btn-neutral']")
# time.sleep(5)
# act = ActionChains(driver)
# act.context_click(rightclick).perform()
# driver.find_element(By.XPATH,"//*[text()='Copy']").click()
# time.sleep(5)
# alert = Alert(driver)
# print(f"Message is:{alert.text}")
# alert.accept()
# time.sleep(2)
# driver.quit()


# -------------------------------------------------------------------

# Double Click

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
# time.sleep(5)
# frame = driver.find_element(By.XPATH,"//*[@id='iframeResult']")
# driver.switch_to.frame(frame)
# field1 = driver.find_element(By.XPATH,"//*[@id='field1']")
# field1.clear()
# field1.send_keys("Welcome")
# time.sleep(5)
# button = driver.find_element(By.XPATH,"//*[@ondblclick='myFunction()']")
# act = ActionChains(driver)
# act.double_click(button).perform()
# time.sleep(5)
# field2 = driver.find_element(By.XPATH,"//*[@id='field2']")
# print("hello", field2.text)
# print(field2.get_attribute("value"))
# if field2.get_attribute("value") == field1.get_attribute("value"):
#     print("Test is passes")
# else:
#     print("Test is Failed")
# driver.quit()

# -------------------------------------------------

# Drag and Drop
# the element to be moved is called source

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("--disable-notifications")
# # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# time.sleep(2)
# drag  = driver.find_element(By.XPATH,"//*[@id='box5']")
# drop = driver.find_element(By.XPATH,"//*[@id='box105']")
# time.sleep(2)
# act = ActionChains(driver)
# act.drag_and_drop(drag,drop).perform()
# time.sleep(5)
# assert "box5" in drop.get_attribute("innerHTML"),"Seoul was not drooped in South Korea"
# time.sleep(2)
# driver.quit()

# -------------------------------------------------

# sliders
# slider are 2 types: X-axis and y-axis
# first check horizontal or vertical ?
# use method location for locating the element, it will give in pixels
# min.location ,  max.location
# use drag and drop by offset
# act.drag and drop by offset(min,100,0).perform()
# (name of element, offset,x-axis, y-axis)

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/#google_vignette")
# time.sleep(5)
# min = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
# max = driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')
# time.sleep(2)
# print(f"The minimum Slider position is:{min.location}")
# print(f"The minimum Slider position is:{max.location}")
# time.sleep(2)
# act = ActionChains(driver)
# act.drag_and_drop_by_offset(min,100,0).perform()
# act.drag_and_drop_by_offset(max,-50,0).perform()
# time.sleep(4)
# print(f"The minimum Slider position is:{min.location}")
# print(f"The minimum Slider position is:{max.location}")
# time.sleep(2)
# driver.quit()

# -------------------------------------------------------------

# SCROLLER
# Usage of Javascript executor Class in Selenium

# driver.execute script("window.scrollBy(0,3000)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:",value) #3000
# time.sleep(2)

# 1. Scroll down page by pixel
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.orangehrm.com/")
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,3000)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:",value) #3000
# time.sleep(2)
# driver.quit()


# SCROLL DOWN TILL THE page element is visible
# logo = driver.find_element(By.XPATH,"//div[@class='homepage-product-content ']")
# driver.execute_script("arguments[0].scrollIntoView();",logo)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of Pixels moved:",value)
# time.sleep(5)
# driver.quit()
#
# # Scroll till the end of page
# # scrollHEIGHT move the scroller till the end
# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of Pixels moved:", value)
# driver.quit()



# ------------------------------------------------------------------------

# Keyboard Event

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://text-compare.com/")
# time.sleep(3)
# driver.find_element(By.XPATH,"//textarea[@id='inputText1']").send_keys("Welcome")
# act = ActionChains(driver)
# # pressing ctrl+a
# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
# # pressing ctrl+c
# act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
# # press tab to navigate input box 2
# act.send_keys(Keys.TAB).perform()
# # Input 2 use ctrl+v
# act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
# # input2 = driver.find_element(By.XPATH,"//*[@id='inputText2']")
# # input2.send_keys(Keys.CONTROL,'v')
# time.sleep(5)
# driver.quit()