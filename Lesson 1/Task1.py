#1. Посмотреть документацию к API GitHub, разобраться как вывести
# список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.

import requests
import json

username = "igor2310"
github_api = f"https://api.github.com/users/{username}/repos"

req = requests.get(github_api)
data = json.loads(req.text)

# output name repositories
list_repositories = [i.get("name") for i in data]

# save file
with open('data.json', 'w') as f:
    json.dump(list_repositories, f)
