from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time

option = uc.ChromeOptions()
option.add_argument('--user-data-dir=/home/your_username/.config/google-chrome/Default')

driver = uc.Chrome(option=option)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3627380463&f_AL=true&f_E=2%2C3&f_JT=F&keywords=python%20developer&refresh=true&sortBy=R")
driver.maximize_window()

login = 'EMAIL@gmail.com'
password = 'PASS'
MOBILE = 'MOBILE'

# Click on the "Sign in" button
sign_in_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Sign in')))
sign_in_button.click()

# Fill in email and password fields and click "Sign in"
try:
    input_email = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
    input_email.send_keys(login)

    input_pass = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
    input_pass.send_keys(password)
    input_pass.send_keys(Keys.ENTER)
except TimeoutException:
    print("Email or password input fields not found.")

# Scroll to the pagination element
try:
    scroll_to_pagination = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#ember294')))
    driver.execute_script("arguments[0].scrollIntoView(true);", scroll_to_pagination)
except TimeoutException:
    print("Pagination element not found.")

# Get the list of job propositions
block_vacations = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'scaffold-layout__list-container')))
vacations_propositions = block_vacations.find_elements(By.TAG_NAME, 'a')

# Iterate over the job propositions
for proposition_link in vacations_propositions:

    time.sleep(5)

    print(proposition_link.text)

    try:
        choose_vac = driver.find_element(By.LINK_TEXT, proposition_link.text)
        choose_vac.click()

        time.sleep(5)

        easy_to_apply = driver.find_element(By.CSS_SELECTOR,
                                            '#main > div > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.job-view-layout.jobs-details > div:nth-child(1) > div > div:nth-child(1) > div > div.relative.jobs-unified-top-card__container--two-pane > div.jobs-unified-top-card__content--two-pane > div:nth-child(4) > div > div')
        easy_to_apply.click()

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # If the submit_button is a "Next" button, then this is a multistep application, so skip.
        if submit_button.get_attribute("aria-label") == "Continue to next step":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
    except NoSuchElementException:
        print(f"Job proposition link '{proposition_link.text}' not found.")
        continue

driver.quit()
