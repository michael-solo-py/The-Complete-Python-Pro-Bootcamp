from bs4 import BeautifulSoup as BS
import requests

url = "https://news.ycombinator.com/"

response = requests.get(url=url)
response.raise_for_status()

table = BS(response.text, "html.parser").select('table table')[1]

title = [item.find("span", class_="titleline").find("a").text for item in table.find_all(name="tr", class_="athing")]
print(title)

link = [link.find("span", class_="titleline").find("a").get("href") for link in
        table.find_all(name="tr", class_="athing")]
print(link)

point = [int(point.find("span", class_="score").text.split()[0])for point in table.find_all(name="tr")[1::2] if
         point.find("span", class_="score") is not None]
print(point)
point.sort(reverse=True)

for max_point in point:
    index_max_point = point.index(max_point)

    print(title[index_max_point])
    print(link[index_max_point])
