from bs4 import BeautifulSoup as BS
import requests
import time

url_google_form = 'https://docs.google.com/forms/d/e/1FAIpQLSca6LI836SxYv4HzrMzSK_QBFoJT4dTPYcwVcoKyKTUdhE_aA/viewform?usp=sf_link'
url_zillow = 'https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.52482451391602%2C%22east%22%3A-122.34183348608398%2C%22south%22%3A37.66054921486579%2C%22north%22%3A37.88985588644496%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(url_zillow, headers=header)
rental_listing = BS(response.text, 'html.parser')
# print(rental_listing)
listing = rental_listing.find_all('ul')[5].find_all('li')
print(listing)
# links = [link.find("a", {"data-test": "property-card-link"})['href'] for link in listing]
# print(links)
links_arr = []
for i in listing:
    try:
        href = i['href']#.get('href')
        if "http" not in href:
            links_arr.append(f"https://www.zillow.com{href}")
        else:
            links_arr.append(href)
        links_arr.append(href)
        print(i['href'])
    except:
        pass
print(links_arr)