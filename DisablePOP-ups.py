# Pop-ups can be disabled using the --disable-popup-blocking argument.
# chrome_options.add_argument("--disable-popup-blocking")
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(chrome_options)
# driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://whatmylocation.com/")
print("Notifications are disabled.")
time.sleep(5)
driver.quit()

# ----------------------------------------------------------

# Pop-ups can be disabled using the --disable-popup-blocking argument.
# chrome_options.add_argument("--disable-popup-blocking")

# --------------------------------------------------------------
# You can set browser preferences to block notifications by configuring the profile.default_content_setting_values.notifications preference.
# chrome_options.add_experimental_option(
#     "prefs",
#     {
#         "profile.default_content_setting_values.notifications": 2  # 1: Allow, 2: Block
#     }
# )

# ------------------------------------------------------------------

# To remove the "Chrome is being controlled by automated test software" banner:
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])