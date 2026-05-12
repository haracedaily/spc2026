#pip install bs4
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>Hello</title>
    </head>
    <body>
        <h1>Title</h1>
        <p>여기는 첫번째 파라그래프</p>
        <p>여기는 두번째 파라그래프</p>
    </body>
</html>

"""

soup = BeautifulSoup(html,"html.parser")

print(soup)
# 문자열로 보이지만 데이터임(자료구조) 돔트리로 구성되어있는 것

heading = soup.find_all("h1")
print(heading)
paragraph = soup.find_all("p")
print(paragraph)