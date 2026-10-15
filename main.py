import requests, json

gitpat = input("whats ur pat? ")
username = input("whats ur user? ")

headers = "Authorization: Bearer {gitpat}"
res = requests.get(f"https://api.github.com/users/{username}/projectsV2", headers=headers)
print(res)