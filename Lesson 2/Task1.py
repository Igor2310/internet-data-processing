from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

name_vacancy = "programmist_python"

url = f"https://nn.hh.ru/vacancies/{name_vacancy}"
session = requests.Session()

flag = True

list_names = []
list_min_salary = []
list_max_salary = []
list_currency = []
list_link = []
list_site_link = []

while flag:
    response = session.get(url, headers=headers)
    dom = BeautifulSoup(response.text, 'html.parser')
    divs = dom.find_all('div', {'class': 'serp-item'})
    for div in divs:
        tag_a = div.find('a', {'class': 'serp-item__title'})
        list_names.append(tag_a.text)

        tag_span = div.find('span', {'data-qa': "vacancy-serp__vacancy-compensation"})

        min_salary = None
        max_salary = None
        currency = None
        if tag_span is None:
            pass
        else:
            div_salary = tag_span.text.replace("\u202f", "")
            if re.search('от', div_salary):
                min_salary = int(div_salary.split()[1])
                currency = div_salary.split()[2]
            elif re.search('до', div_salary):
                max_salary = int(div_salary.split()[1])
                currency = div_salary.split()[2]
            else:
                min_salary = int(re.split(" – | ", div_salary)[0])
                max_salary = int(re.split(" – | ", div_salary)[1])
                currency = re.split(" – | ", div_salary)[2]

        list_min_salary.append(min_salary)
        list_max_salary.append(max_salary)
        list_currency.append(currency)
        list_link.append(tag_a.get('href'))
        list_site_link.append(url)

    try:
        url_next_page = f"https://nn.hh.ru{dom.find('a', {'data-qa': 'pager-next'}).get('href')}"
        url = url_next_page
    except AttributeError:
        flag = False

dict_vacancies = {'name': list_names, 'min_salary': list_min_salary, 'max_salary': list_max_salary,
                  'currency': list_currency, 'link': list_link, 'site_link': list_site_link}

df = pd.DataFrame(dict_vacancies)
print(df)
df.to_csv(f'{name_vacancy}.csv', encoding='UTF-8')
