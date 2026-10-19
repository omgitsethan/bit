import requests
from libs import data

db = data.init()
username,pat = db[0]

data.save_login(input("Username, Pat?: ").split(","))

# headers = {"Authorization": f"Bearer {gitpat}", "Accept": "application/json"}
# res = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)
# for repo in res.json():
#     print(repo["name"])