import requests
from bs4 import BeautifulSoup

urls = [
    "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20240520&hh=12&rtm=Y&pg=1",
    "https://www.genie.co.kr/chart/top200?ditc=D&ymd=20240520&hh=12&rtm=Y&pg=2"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}


def song(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    songs = []
    rows = soup.select('table.list-wrap tbody tr')
    for row in rows:
        title = row.select_one('a.title.ellipsis').get_text(strip=True)
        artist = row.select_one('a.artist.ellipsis').get_text(strip=True)
        songs.append({'title': title, 'artist': artist})
    return songs


all_songs = []
for url in urls:
    all_songs.extend(song(url))


for i in range(100):  
    rank = str(i + 1)
    if i < len(all_songs):
        song = all_songs[i]  
        print(f"{rank}위 {song['title']}-{song['artist']}")

