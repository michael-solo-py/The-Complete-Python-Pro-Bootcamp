# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import time

EMAIL = 'wefw34243@gmail.com'
PASS = 'ebkvcrclbvszcokt'

chrome_options = uc.ChromeOptions()

location_script = """
    var mockLocation = {
        coords: {
            latitude: 37.7749,  
            longitude: -122.4194
        }
    };
    navigator.geolocation.getCurrentPosition = function(success) {
        success(mockLocation);
    };
"""

prefs = {
    "profile": {
        "managed_default_content_settings": {
            "notifications": 2,
            "geolocation": 1,
        }
    }
}

chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-device-for-media-stream")

driver = uc.Chrome(options=chrome_options)
driver.get('https://tinder.com/app/recs')
driver.maximize_window()
driver.implicitly_wait(10)

time.sleep(5)
log_in = driver.find_element(By.XPATH,
                             '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log_in.click()
time.sleep(5)

continue_with_google = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
continue_with_google.click()

window_handle = driver.current_window_handle
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
for handle in driver.window_handles:
    if handle != window_handle:
        driver.switch_to.window(handle)
        break

input_email = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
input_email.send_keys(EMAIL)
input_email.send_keys(Keys.ENTER)

input_pass = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
input_pass.send_keys(PASS)
input_pass.send_keys(Keys.ENTER)

driver.switch_to.window(window_handle)

time.sleep(10)

# -- Allow alerts --
# allow_location = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[1]/div/div/div[3]/button[1]/div[2]')))
# allow_location.click()

# notification = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[1]/div/div/div[3]/button[2]/div[2]')))
# if notification.get_attribute('aria-label') == 'Not interested':
#     notification.click()

proposition = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div/div/div[3]/button[2]')))
if proposition.get_attribute('draggable') == 'false':
    proposition.click()

cookies = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/main/div[2]/div/div/div[1]/div[1]/button/div[2]')))
if cookies.get_attribute('class') == 'l17p5q9z':
    cookies.click()

time.sleep(10)

while True:
    swipe = driver.find_element(By.CSS_SELECTOR, '.Bgi\(\$g-ds-background-like\)\:a > span:nth-child(1)')
    swipe.click()

time.sleep(120)

driver.quit()
