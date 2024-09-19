from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def verify_title():
    driver.get("https://www.dropbox.com/s/vx9bvgx3scl5qn4/200k.txt?e=1&dl=0")
    driver.implicitly_wait(30)
    texter = driver.find_element(By.CLASS_NAME, 'highlight')
    print(texter.text)
    sam = texter.text.strip
    # with open('200k.txt',  'w') as f:
    #     f.write(sam)

    # lang_select = driver.find_element(By.ID, "langSelect-EN")
    # lang_select.click()
    # driver.implicitly_wait(30)
    #
    # cookie = driver.find_element(By.ID, "bigCookie")
    # cookie_count = driver.find_element(By.ID, "cookies")
    #
    # items = [driver.find_element(By.ID, "productPrice1")]
    # items += [driver.find_element(By.ID, "productPrice0")]
    #
    # for i in range(5000):
    #     actions = ActionChains(driver)
    #     actions.click(cookie)
    #     actions.perform()
    #     count = int(cookie_count.text.split(" ")[0])
    #     for item in items:
    #         value = int(item.text)
    #         if count == 500:
    #             while value <= count:
    #                 upgrade_actions = ActionChains(driver)
    #                 upgrade_actions.move_to_element(item)
    #                 upgrade_actions.click()
    #                 upgrade_actions.perform()

    # print(driver.title)
    #
    # search = driver.find_elements_by_name("s")
    # search.send_keys("test")
    # search.send_keys(Keys.RETURN)
    # # Close the webdriver
    # time.sleep(5)
    driver.quit()


verify_title()
