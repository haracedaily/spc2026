import requests

url = 'https://api.github.com/users/haracedaily/repos'

resp = requests.get(url)
repos = resp.json()

data = []
print(repos)
if not (repos['message']):
    for repo in repos:
        name = repo["name"]
        html_url = repo['html_url']
        description = repo['description']
        data.append({'name':name,"html_url":html_url,"desc":description})

    for d in data:
        print(f"{d['name']:<25} {d['html_url']:<60} {str(d['desc']):<20} ")