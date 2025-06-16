import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

movies_list = []

movies = soup.find_all(name="h3", class_="title")
for movie in movies:
    movies_list.append(movie.getText())

movies_list = movies_list[::-1]

with open("movies.txt", "w") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
