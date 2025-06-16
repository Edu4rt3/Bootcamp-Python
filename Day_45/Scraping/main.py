from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
articles_texts = []
articles_links = []
for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link  = article_tag.get("href")
    articles_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(articles_texts[largest_index])
print(articles_links[largest_index])

# print(articles_texts)
# print(articles_links)
# print(article_upvotes)