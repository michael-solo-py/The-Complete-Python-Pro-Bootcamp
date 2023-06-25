from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
import json
import time

url_google_form = 'https://docs.google.com/forms/d/e/1FAIpQLSca6LI836SxYv4HzrMzSK_QBFoJT4dTPYcwVcoKyKTUdhE_aA/viewform?usp=sf_link'
url_zillow = 'https://www.zillow.com/'
url_zillow_endpoint = 'search/GetSearchPageState.htm?searchQueryState=%7B"pagination"%3A%7B%7D%2C"mapBounds"%3A%7B"west"%3A-122.52808608007813%2C"east"%3A-122.33857191992188%2C"south"%3A37.66054921486579%2C"north"%3A37.88985588644495%7D%2C"mapZoom"%3A12%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"price"%3A%7B"max"%3A872627%7D%2C"beds"%3A%7B"min"%3A1%7D%2C"isForSaleForeclosure"%3A%7B"value"%3Afalse%7D%2C"monthlyPayment"%3A%7B"max"%3A3000%7D%2C"isAuction"%3A%7B"value"%3Afalse%7D%2C"isNewConstruction"%3A%7B"value"%3Afalse%7D%2C"isForRent"%3A%7B"value"%3Atrue%7D%2C"isForSaleByOwner"%3A%7B"value"%3Afalse%7D%2C"isComingSoon"%3A%7B"value"%3Afalse%7D%2C"isForSaleByAgent"%3A%7B"value"%3Afalse%7D%7D%2C"isListVisible"%3Atrue%7D&wants={"cat1":["mapResults"]}&requestId=2'
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url_zillow + url_zillow_endpoint, headers=header)
data = json.loads(response.text)


def get_href():
    links = [link['detailUrl'] for link in data['cat1']['searchResults']['mapResults']]
    print(links)
    return links


def get_price():
    prices = [price['price'] for price in data['cat1']['searchResults']['mapResults']]
    print(prices)
    return prices


def get_address():
    addresses = [address['address'] for address in data['cat1']['searchResults']['mapResults']]
    print(addresses)
    return addresses


# ------------------------------ FILL FORM ------------------------------------------
driver = webdriver.Chrome()
driver.get(url_google_form)
driver.maximize_window()

def fill_inputs(address, price, link):
    address_property = driver.find_element(By.XPATH,
                                           '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    for a in get_address():
        address_property.send_keys(a)

    price_property = driver.find_element(By.XPATH,
                                         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    for p in get_price():
        price_property.send_keys(p)

    link_property = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    for l in get_href():
        link_property.send_keys(l)

fill_inputs()

time.sleep(10)
driver.quit()
