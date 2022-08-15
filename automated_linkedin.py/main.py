import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome('c:/Development/chromedriver.exe')

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3222514449&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

# click on sign in
driver.find_element(By.LINK_TEXT, "Sign in").click()

my_email = os.environ['EMAIL']
my_password = os.environ['PASSWORD']


# entering email and password
driver.find_element(By.NAME, "session_key").send_keys(my_email)
driver.find_element(By.NAME, "session_password").send_keys(my_password)

# click on sign in
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()

time.sleep(2)
# select first job
driver.find_element(By.CSS_SELECTOR, ".full-width a").click()

# apply for the first job
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button").click()

# fill phone number
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".display-flex input").send_keys('050505')

# click Next
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".display-flex button").click()

# close the window
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".artdeco-modal button").click()

# click Discard
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar button").click()

time.sleep(1)
driver.quit()




