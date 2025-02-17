# cookies = driver.get_cookie("name")
# add cookies/cookie
# delete cookies/ cookie

# A.I tools for QE testing
# Presentation on this A.I. Tool

driver.get("https://example.com/login")
# Perform login steps here

# Save session cookies
session_cookies = driver.get_cookies()

# Use cookies in a new browser session
driver.quit()
driver = webdriver.Chrome()
driver.get("https://example.com")
for cookie in session_cookies:
    driver.add_cookie(cookie)
driver.refresh()  # Ensure cookies are applied
# ------------------------------------------------------------------------
import time
from selenium import webdriver




# driver = webdriver.Chrome()        #   use only when we want to open the browser

# def headless_chrome():
#     ops = webdriver.ChromeOptions()
#     ops.add_argument("--headless")
#     driver = webdriver.Chrome(options=ops)
#     return driver




# driver = headless_chrome()
driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(2)

print(driver.title, "from chrome")

cookies = driver.get_cookies()
print(cookies, len(cookies))

driver.add_cookie({'name': 'hellow', 'value': '123'})

cookies = driver.get_cookies()
print(cookies, len(cookies))

