import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

aritcle_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(aritcle_upvotes[0].split()[0])

print(article_texts)
print(article_links)
print(aritcle_upvotes)

largest_number = max(aritcle_upvotes)
print(largest_number)
largest_index = aritcle_upvotes.index(largest_number)
print(largest_index)

print(article_texts[largest_index])
print(article_links[largest_index])