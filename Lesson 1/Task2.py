# 2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis). Найти среди них любое,
# требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.


import requests

url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

querystring = {"lat": "35.5", "lon": "-78.5", "units": "metric", "lang": "en"}

headers = {
    "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
    "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

# api взял с сайта https://rapidapi.com/weatherbit/api/weather/
# "SIGN-UP-FOR-KEY" - ключ ставится в эту фразу
