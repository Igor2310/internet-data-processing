# from bs4 import BeautifulSoup
# import requests
# import re
import pandas as pd

from pymongo import MongoClient
from pprint import pprint

# from pymongo.errors import DuplicateKeyError

client = MongoClient('127.0.0.1', 27017)

db_vacancies = client['igor_mongo']  # database

vacancies = db_vacancies.vacancies  # collection inside db_vacancies

my_salary = 50000

count = 0
for vacancy in vacancies.find({}):
    if pd.isna(vacancy.get('max_salary')) and vacancy.get('min_salary') >= 0:
        pprint(vacancy)
        count += 1
    if vacancy.get('max_salary') >= my_salary:
        pprint(vacancy)
        count += 1

print(f'Number vacancies {count} from {my_salary}')


# count=0
# for vacancy in vacancies.find({'min_salary': {'$gt':0}}):
#     if pd.isna(vacancy.get('max_salary')):
#         pprint(vacancy)
#         count+=1
#
# for vacancy in vacancies.find({'max_salary': {'$gt':my_salary}}):
#         pprint(vacancy)
#         count += 1
# print(count)
