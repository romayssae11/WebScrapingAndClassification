import requests
from bs4 import BeautifulSoup
import urllib.request
import json

url = 'https://www.alarabiya.net/sport/archive?pageNo='
file = open('SportsArticles.json', 'w',encoding='utf-8-sig')
file.write('[\n')
data = {}
for page in range(1,100):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    links=[]
    allarticles = soup.find_all("span", {'class': 'latest_content'})
    for pt in allarticles :
        article_link = pt.find('a')
        href = article_link.get("href")
        links.append(href)
    n = len(links)
    for link in range(n):
        r1 = requests.get('https://www.alarabiya.net' + links[link])
        soup1 = BeautifulSoup(r1.content, "html.parser")
        title = soup1.find("h1", {'class': 'headingInfo_title'})
        categorie = soup1.find("a", {'href' : '/sport'})
        allParagraphs = soup1.find_all("p", {'class': 'body-1'})
        article = ""
        l = len(allParagraphs)
        for p in range(l):
            article = article + allParagraphs[p].text.strip()
        data['title'] = title.text.strip()
        data['article'] = article.strip()
        data['categorie'] = categorie.text.strip()
        json_data = json.dumps(data, ensure_ascii=False)
        file.write(json_data)
        file.write(",\n")
file.write("\n]")
file.close()