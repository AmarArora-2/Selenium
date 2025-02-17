from selenium import webdriver  # For launching the browser
from selenium.webdriver.common.by import By  # For locating elements
from selenium.webdriver.common.keys import Keys  # For simulating keyboard input

# Set up the Selenium WebDriver
# Step 1: Launch the browser
driver = webdriver.Chrome()  # Use Chrome as the browser

# Step 2: Navigate to Amazon's homepage
driver.get('https://www.amazon.com')

# Step 3: Verify the title of the page
expected_title = "Amazon.com. Spend less. Smile more."
actual_title = driver.title
if expected_title == actual_title:
    print("Test passed: Title matches.")
else:
    print("Test Failed")

# Step 4: Close the browser
driver.close()
