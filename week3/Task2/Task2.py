from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def get_data():
    links = []
    url = "https://www.ptt.cc/bbs/Lottery/index.html"
    req = Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "cookie": "over18=1"})
    response = urlopen(req)
    root = BeautifulSoup(response, "html.parser")
    for page in range(3):
        articles = root.find_all("div", class_="r-ent")
        for article in articles:
            if article.find('a'):
                link = "https://www.ptt.cc" + article.find("a")["href"]
                links.append(link)
    
        prev_link = root.find("a", string="‹ 上頁")["href"]
        url = "https://www.ptt.cc" + prev_link
    return links

def get_article_title_and_time(article_link):
    req = Request(article_link, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "cookie": "over18=1"})
    response = urlopen(req)
    root = BeautifulSoup(response, "html.parser")
    meta_values = root.find_all("span", class_="article-meta-value")
    if len(meta_values) >= 4:
        title = meta_values[2].text
        time = meta_values[3].text
        push_tag = root.find_all("span", class_="push-tag")
        push_count = sum(1 for tag in push_tag if tag.text.strip() in ["推","噓"])
            
        return title, push_count, time
    
lottery_links = get_data()

import csv
with open("article.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    for link in lottery_links:
        data = get_article_title_and_time(link)
        if data:
            writer.writerow(data)