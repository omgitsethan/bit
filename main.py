import requests, json

gitpat = ""
username = ""

def saveData(data):
    with open("data.json", "w") as f:
        json.dump(data, f)

def loadData():
    global gitpat, username
    with open("data.json", "r") as f:
        data = json.load(f)
        if data["gitpat"] and data["username"]:
            gitpat,username = data["gitpat"], data["username"]

# gitpat = input("whats ur pat? ")
# username = input("whats ur user? ")
# saveData({"gitpat": gitpat, "username": username})

loadData()

headers = {"Authorization": f"Bearer {gitpat}", "Accept": "application/json"}
res = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)
for repo in res.json():
    print(repo["name"])