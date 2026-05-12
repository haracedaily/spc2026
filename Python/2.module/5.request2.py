import requests

url = "https://www.example.com"

response = requests.get(url)

#  https = http + ssl

html = response.text

print(html)

print("-"*30)

start = html.find("<h1>")
end = html.find("</h1>")

text = html[start+4:end]

print(text)