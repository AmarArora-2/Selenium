# import os
from selenium import webdriver
import base64
driver = webdriver.Chrome()
driver.get("https://hianime.to/home")
# Use DevTools Protocol for full-page screenshot
screenshot_base64 = driver.execute_cdp_cmd("Page.captureScreenshot", {"format": "png"})
with open("devtools_page.png", "wb") as file:
    file.write(base64.b64decode(screenshot_base64['data']))
print("Full-page screenshot captured using DevTools!")
driver.quit()

# driver.save_screenshot(os.getcwd() + "\\Homepage.png")
# ----------------------------------------------------------------------
# driver.save_screenshot("anime.png")
# --------------------------------------------------------------------
# driver.save_screenshot(r"C: full path")
# -----------------------------------------------------------------------
# screenshot_base64 = driver.get_screenshot_as_base64()
# print(screenshot_base64)  # Useful for embedding in reports
# ------------------------------------------------------------------------

# element = driver.find_element(By.ID, "logo")
# element.screenshot("element_screenshot.png")
# ------------------------------------------------------------------
# On test failures
# try:
#     assert driver.title == "Expected Title"
# except AssertionError:
#     driver.save_screenshot("failure_screenshot.png")
# ---------------------------------------------------------------------
# Use DevTools Protocol for full-page screenshot



