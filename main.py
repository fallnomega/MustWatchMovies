import requests
import re
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
one_of_them = soup.find(name="h3", class_="title")
all_of_them = soup.find_all(name='h3', class_='title')
split_list = []
for x in all_of_them:
    temp = re.split('[:)]', x.get_text())
    entry = {'rank': int(temp[0]), 'movie': temp[1]}
    split_list.append(entry)
split_list.sort(key=lambda d: d['rank'])
with open(file='movies.txt',mode='w') as file:
    for x in split_list:
        file.write(f"{x['rank']}) {x['movie']}\n")


