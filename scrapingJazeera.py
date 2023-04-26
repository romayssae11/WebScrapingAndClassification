import requests
from bs4 import BeautifulSoup
import urllib.request
import csv

filecsv = open('PoliticsArticles.csv', 'w',encoding='utf-8-sig')


url = 'https://www.aljazeera.net/politics/'
data = {}
csv_columns = ['title','article']
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
allarticles = soup.find_all("div", {'class': 'gc__content'})
writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
i=0
writer.writeheader()
for pt in allarticles :
    title = pt.find('h3', {'class' : 'gc__title'})
    article = pt.find('div', {'class' : 'gc__body-wrap'})
    writer.writerow({'title': title.text.strip(), 'article': article.text.strip()})
    data['title'] = title.text.strip()
    data['article'] = article.text.strip()

filecsv.close()