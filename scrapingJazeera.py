import requests
from bs4 import BeautifulSoup
import urllib.request
import csv

filecsv = open('PoliticsArticlesExp4.csv', 'w',encoding='utf-8-sig')


url = 'https://www.aljazeera.net/politics/'
data = {}
csv_columns = ['title','article','categorie']
writer = csv.DictWriter(filecsv, fieldnames=csv_columns)

writer.writeheader()
r = requests.get(url)
article_count = 0

soup = BeautifulSoup(r.content, "html.parser")
allarticles = soup.find_all("div", {'class': 'gc__content'})
while article_count<1000:
   for pt in allarticles :
       title = pt.find('h3', {'class' : 'gc__title'})
       article = pt.find('div', {'class' : 'gc__body-wrap'})
       categorie = soup.find('div', {'class' : 'section-header__title'})
       article_count+=1
       writer.writerow({'title': title.text.strip(), 'article': article.text.strip(), 'categorie': categorie.text.strip()})
       data['title'] = title.text.strip()
       data['article'] = article.text.strip()
       data['categorie'] = categorie.text.strip()
       if article_count == 1000:  # Sortir de la boucle lorsque 1000 articles sont extraits
           break

filecsv.close()