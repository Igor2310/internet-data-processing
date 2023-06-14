import requests
from lxml import html

from pymongo import MongoClient
from pprint import pprint

# mongo db
client = MongoClient('127.0.0.1', 27017)
db_vacancies = client['igor_mongo']  # database
vacancies = db_vacancies.vacancies  # collection inside db_vacancies

# session
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
session = requests.Session()
response = session.get('https://lenta.ru/', headers=headers)

dom = html.fromstring(response.text)
top_news_dom = dom.xpath("//div[@class='topnews']")[0]

name_source = 'https://lenta.ru/'
name_news = top_news_dom.xpath(".//*[@class='card-big__title']/text() | .//*[@class='card-mini__title']/text()")
link_news = top_news_dom.xpath(
    ".//*[@class='card-big__title']/../../@href | .//*[@class='card-mini__title']/../../@href")
time = top_news_dom.xpath(".//time/text()")

list_vacancies = {}

for i in zip(name_news, link_news, time):
    dict_vacancy = {}
    dict_vacancy['name_source'] = name_source
    dict_vacancy['name_news'] = i[0]
    dict_vacancy['link_news'] = name_source + i[1]
    dict_vacancy['date_publication'] = i[2]
    vacancies.insert_one(dict_vacancy)

for vacancy in vacancies.find({}):
    pprint(vacancy)

vacancies.drop()


