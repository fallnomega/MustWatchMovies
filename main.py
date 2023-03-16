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

# a more pythonic way discovered so replacing with old
# code that used lists,str re.splits, and sorting
movie_titles = [movie.getText() for movie in all_of_them]
movies = movie_titles[::-1]

with open(file='movies.txt',mode='w') as file:
    for movie in movies:
        file.write(f"{movie}\n")