from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Drivers\chromedriver\chromedriver.exe"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org/")

events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
event = events.find_elements(By.TAG_NAME, "li")

dict = {}
for n in range(len(event)):
    time = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{n + 1}]/time').text
    year = driver.find_element(By.CLASS_NAME, 'say-no-more')
    year.get_attribute()
    new = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{n + 1}]/a').text

    dict[n] = {'time': f"{year}{time}", 'name': f'{new}'}
print(dict)
driver.quit()
