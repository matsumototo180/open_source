import requests
import csv
import time
from bs4 import BeautifulSoup

# Webページを取得して解析する
# https://codezine.jp/article/detail/12230

base_url = "https://www.tokushima-u.ac.jp"
load_url = "https://www.tokushima-u.ac.jp/ias/event/"
soup = BeautifulSoup(requests.get(load_url).content, "html.parser")

# HTML全体を表示する
print(soup)

articles = soup.find_all("article")

articles[0].find("time")["datetime"]

articles_parsed = [{"pubdate": item.find("time")["datetime"], "title": item.find("h2").text, "url": item.find("a")["href"]} for item in articles]
articles_parsed = articles_parsed[0:10]

articles_content = []
for item in articles_parsed:
    tmp = requests.get(base_url + item["url"])
    article = BeautifulSoup(tmp.content, "html.parser")
    articles_content.append(article.find("article", class_="body").text)
    time.sleep(1)

articles_content = [item.encode("cp932", "ignore").decode("cp932") for item in articles_content]

articles = []
for parsed, content in zip(articles_parsed, articles_content):
    parsed.update({"content": content})
    articles.append(parsed)

with open('output.csv', 'w', encoding="cp932", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=articles[0].keys())
    writer.writeheader()
    writer.writerows(articles)

