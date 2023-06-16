import os
from dotenv import load_dotenv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

load_env()


chrome_path = os.getenv(CHROME_PATH)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_path,))



passkey = os.getenv(PASS_KEY)
email = os.getenv(EMAIL)
link = 'https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in'
driver.get(link)

driver.find_element(By.NAME, 'session_key').send_keys(email)
driver.find_element(By.NAME, 'session_password').send_keys(passkey)
driver.find_element(By.CLASS_NAME, 'login__form_action_container').click()

time.sleep(15)

search_Item = "developer"

try:
    driver.find_element(By.CLASS_NAME, 'search-global-typeahead__collapsed-search-button').click()
    driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input').send_keys(search_Item, Keys.ENTER)
except:
    driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input').send_keys(search_Item, Keys.ENTER)

time.sleep(3)

# driver.find_element(By.XPATH,'//*[@id="4T87R4/1TxmA/KOy9mRG2g=="]/div/div[2]/a').click()


time.sleep(3)





driver.find_element(By.CLASS_NAME, "search-results__cluster-bottom-banner").click()
time.sleep(5)



jobs = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")

save = driver.find_element(By.CLASS_NAME, "jobs-save-button")


for job in jobs:
    job.click()
    time.sleep(3)

    save.click()
    time.sleep(3)
    job.location_once_scrolled_into_view



    time.sleep(2)







