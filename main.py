import requests
from libs import data, console

db = data.init()
username, pat = data.get_login()[0]

if username and pat:
    console.init()
else:
    print('not logged in', username,pat,data.get_login())

    data.save_login(input("Username, Pat?: ").split(","))