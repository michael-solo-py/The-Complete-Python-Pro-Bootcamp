from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://londonappbrewery.com/sendy/subscription?f=m7Xj2bDOCQnlJ27yezLEAtJi1mhUIxOaJcJGZYMLLX6wx5MZd0b2FunBI8dOomNt&_ga=2.153417786.309660921.1685534675-1339180169.1685534675'
chrome_driver_path = r"C:\Drivers\chromedriver\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)

name = driver.find_element(By.CSS_SELECTOR, '#name')
email = driver.find_element(By.CSS_SELECTOR, '#email')
check_mark = driver.find_element(By.CSS_SELECTOR, '#gdpr')

name.send_keys('misha')
email.send_keys('this.is.my@email.com')
check_mark.click()


