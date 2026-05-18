import requests

url = "https://api.github.com/search/repositories"

keyword="python"

params = {
    'q':keyword
}

resp = requests.get(url,params)
data = resp.json()

# print(data)

#print(data)
if 'items' in data:
    repos = data['items']
    for repo in repos : 
        name = repo['name']
        full_name = repo['full_name']
        desc = repo['description']
        html_url = repo['html_url']

        print(f"리포명 : {name} 풀네임 {full_name}, url: {html_url} , 설명 : {desc}")
