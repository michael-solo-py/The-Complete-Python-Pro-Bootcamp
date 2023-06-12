from bs4 import BeautifulSoup as BS
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=url)
response.raise_for_status()

table = BS(response.text, "html.parser")

name = table.find("div", class_="article__content").find_all("div", class_="article-title-description")

movie_arr = [movie.find("h3", class_="title").text for movie in name]

print(movie_arr[::-1])

with open("100 movie.txt", 'w') as txt:
    for i in movie_arr[::-1]:
        txt.write(f"{str(i.encode('utf-8'))}\n")