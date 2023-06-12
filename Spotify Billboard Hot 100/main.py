import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup as BS

time = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{time}/"

response = requests.get(url)
response.raise_for_status()

bs = BS(response.text, "html.parser")

top_list_songs = {
    "singer": "",
    "song": "",
}

table = bs.find("div2", class_="chart-results-list // lrv-u-padding-t-150 lrv-u-padding-t-050@mobile-max").find_all(
    "div", class_="o-chart-results-list-row-container")


def get_songs(table):
    song_list = [(one_song.find("h3", id="title-of-a-story").text.strip()) for one_song in table]
    return song_list


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="CLIENT_ID",
        client_secret="CLIENT_SECRET",
        show_dialog=True,
        cache_path="token.txt"
    )
)

current_user_id = sp.current_user()["id"]
print(current_user_id)

tracks = []


def songs_uri(time, song_name, sp):
    time = time.split("-")[0]
    for name in song_name:
        res = sp.search(q=f"track:{name} year:{time}", type="track")
        print(res)
        try:
            uri = res["tracks"]["items"][0]["uri"]
            tracks.append(uri)
        except IndexError:
            print(f"{name} doesn't exist in Spotify. Skipped.")


def create_playlist():
    playlist = sp.user_playlist_create(user=current_user_id,
                                       name=f"{time} Billboard 100",
                                       public=False,
                                       collaborative=False,
                                       description="This app will create a playlist with my youth's song")

    add_songs = sp.playlist_add_items(playlist_id=playlist["id"], items=tracks)
    print(add_songs)


if __name__ == "__main__":
    songs_uri(time=time, song_name=get_songs(table=table), sp=sp)
    create_playlist()
    print(tracks)
