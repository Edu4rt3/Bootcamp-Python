from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "lxml")
# print(soup.title)

all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())