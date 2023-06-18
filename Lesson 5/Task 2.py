from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pymongo import MongoClient
from pprint import pprint

# mongo db
client = MongoClient('127.0.0.1', 27017)
db_goods = client['igor_mongo']  # database
goods = db_goods.best_novelties  # collection inside db_vacancies

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(8)

driver.get('https://www.citilink.ru/')

best_novelties = driver.find_elements(By.XPATH,
                                      "//div[@data-meta-name='ProductsCompilation__best-novelties']//div[@data-meta-name='ProductsCompilation__slide']")

for i in best_novelties:
    dict_goods = {}
    dict_goods["link"] = i.find_element(By.XPATH, ".//a[@data-meta-name='Snippet__title']").get_attribute('href')
    dict_goods["name"] = i.find_element(By.XPATH, ".//a[@data-meta-name='Snippet__title']").get_attribute('title')
    dict_goods["price"] = int(i.find_element(By.XPATH, ".//span/span/span[1]").text.replace(" ", ""))
    dict_goods['currency'] = i.find_element(By.XPATH, ".//span/span/span[2]").text
    goods.insert_one(dict_goods)

for good in goods.find({}):
    pprint(good)

goods.drop()
