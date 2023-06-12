from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading

url = 'http://orteil.dashnet.org/experiments/cookie/'

driver = webdriver.Chrome()
driver.get(url)


def clicker():
    while True:
        cookie_click = driver.find_element(By.XPATH, '//*[@id="cookie"]')
        cookie_click.click()


def cookies_count():
    cookies = driver.find_element(By.CSS_SELECTOR, '#money').text

    return cookies


def purchase():
    time_machine = driver.find_element(By.ID, 'buyTime machine')
    portal = driver.find_element(By.ID, 'buyPortal')
    lab = driver.find_element(By.ID, 'buyAlchemy lab')
    shipment = driver.find_element(By.ID, 'buyShipment')
    mine = driver.find_element(By.ID, 'buyMine')
    factory = driver.find_element(By.ID, 'buyFactory')
    grandma = driver.find_element(By.ID, 'buyGrandma')

    time_machine_num = ''.join(sum for sum in time_machine.text if sum.isdigit())
    portal_num = ''.join(sum for sum in portal.text if sum.isdigit())
    lab_num = ''.join(sum for sum in lab.text if sum.isdigit())
    shipment_num = ''.join(sum for sum in shipment.text if sum.isdigit())
    mine_num = ''.join(sum for sum in mine.text if sum.isdigit())
    factory_num = ''.join(sum for sum in factory.text if sum.isdigit())
    grandma_num = ''.join(sum for sum in grandma.text if sum.isdigit())

    if cookies_count() > time_machine_num:
        driver.find_element(By.ID, 'buyCursor').click()
    elif cookies_count() > portal_num:
        driver.find_element(By.ID, 'buyPortal').click()
    elif cookies_count() > lab_num:
        driver.find_element(By.ID, 'buyAlchemy lab').click()
    elif cookies_count() > shipment_num:
        driver.find_element(By.ID, 'buyShipment').click()
    elif cookies_count() > mine_num:
        driver.find_element(By.ID, 'buyMine').click()
    elif cookies_count() > factory_num:
        driver.find_element(By.ID, 'buyFactory').click()
    elif cookies_count() > grandma_num:
        driver.find_element(By.ID, 'buyGrandma').click()


if __name__ == "__main__":
    thread1 = threading.Thread(target=clicker)
    thread1.start()
    while True:
        time.sleep(5)
        purchase()
