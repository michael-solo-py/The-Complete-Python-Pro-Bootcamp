from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time

url = "https://www.linkedin.com/jobs/search/?currentJobId=3627380463&f_AL=true&f_E=2%2C3&f_JT=F&keywords=python%20developer&refresh=true&sortBy=R"
driver = webdriver.Chrome()
driver.get(url)

login = 'forprogramming23@gmail.com'
password = ''
MOBILE = ''

sing_in_button = driver.find_element(By.LINK_TEXT, 'Sign in')
sing_in_button.click()

time.sleep(2)  # wait until load

input_email = driver.find_element(By.CSS_SELECTOR, '#username')
input_email.send_keys(login)

input_pass = driver.find_element(By.CSS_SELECTOR, '#password')
input_pass.send_keys(password)

sing_in_to_acc = driver.find_element(By.CSS_SELECTOR, '.btn__primary--large')
sing_in_to_acc.click()

time.sleep(2)

# -- SCROLLING --
scroll_to_pagination = driver.find_element(By.CSS_SELECTOR, '#ember294')
driver.execute_script("arguments[0].scrollIntoView(true);", scroll_to_pagination)

# -- JOBS LIST --
vacations_propositions = driver.find_element(By.CLASS_NAME, 'scaffold-layout__list-container')
test1 = vacations_propositions.find_elements(By.TAG_NAME, 'a')
time.sleep(1)
for v in test1:
    print(v.text)

    choose_vac = vacations_propositions.find_element(By.LINK_TEXT, v.text)
    choose_vac.click()

    # -- Save and Follow  --
    save_button = driver.find_element(By.CSS_SELECTOR,
                                      '#main > div > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.job-view-layout.jobs-details > div:nth-child(1) > div > div:nth-child(1) > div > div.relative.jobs-unified-top-card__container--two-pane > div.jobs-unified-top-card__content--two-pane > div:nth-child(4) > div > button')
    save_button.click()

    wait = WebDriverWait(driver, 10)
    follow_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'follow')))
    follow_button.click()


time.sleep(1000)
driver.quit()
