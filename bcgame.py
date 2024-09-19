from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bc.game/game/wheel")
driver.execute_script('''
        var hiddenElements = document.querySelectorAll('.hidden-element-class');
        hiddenElements.forEach(function(element) {
            element.style.visibility = 'visible';  // Or element.style.display = 'block';
        });
    ''')


# driver.get("https://www.sportybet.com")
# Execute JavaScript to unhide elements
# Function to unhide elements
def unhide_elements():
    driver.execute_script('''
            var hiddenElements = document.querySelectorAll('.hidden-element-class');
            hiddenElements.forEach(function(element) {
                element.style.visibility = 'visible';  // Or element.style.display = 'block';
            });
        ''')


# Retry mechanism
retry_attempts = 3
for attempt in range(retry_attempts):
    try:
        # Wait for elements to be hidden
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.hidden-element-class')))
        # Unhide elements
        unhide_elements()
        break  # Exit loop if unhide successful
    except Exception as e:
        print(f"Attempt {attempt + 1} failed: {e}")
else:
    print("Unable to unhide elements after multiple attempts.")
time.sleep(150)
# #
# # close1 = driver.find_element(By.CLASS_NAME, "close-icon i1gm0mn8")
# # close1.click()
# signin = driver.find_element(By.CLASS_NAME, "sign-in")
# signin.click()
# driver.implicitly_wait(30)
# login = driver.find_element(By.CSS_SELECTOR, '.ui-input.first-input input[type="text"]')
# login.send_keys("afolabisamguy@gmail.com")
# driver.implicitly_wait(30)
# password = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, '.ui-input.pjkqlcx input[type="password"]'))
# )
#
# password.send_keys("oladipupo1")
# driver.implicitly_wait(30)
# loginbutton = driver.find_element(By.CLASS_NAME, "ui-button")
# loginbutton.click()
time.sleep(30)
parent_class = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'recent-list')))
bet = driver.find_element(By.CLASS_NAME, "bet-button")

if parent_class:
    # Find all child elements with the specific class name you're interested in
    child_classes = parent_class.find_element(By.CLASS_NAME, "item-wrap is-lose ")
    # Initialize a counter to keep track of consecutive occurrences
    consecutive_count = 0
    for child in child_classes:
        print(child.text)

while True:
    bet.click()
