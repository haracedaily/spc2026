from bs4 import BeautifulSoup
# import bs4
# soup = bs4.BeautifulSoup
import requests


url = "https://www.example.com"
resp = requests.get(url)
soup = BeautifulSoup(resp.text,"html.parser")
print(soup)
title = soup.find("title")
print(title)

headings = soup.find_all("h1")
print(headings)

divs = soup.find_all("div")
print(divs)
for elem in divs:
    link = elem.a
    if link:
        href = link.get("href")
        print("link주소는 : ", href)


# 웹 크롤러
# 구글 검색 엔진
# bs4 html을 가지고 dom을 파싱해주는 애
# requests 요청해서 html을 바다아 와주는 애
# google thesis search 
# 생각 이론 => 실용성이 없다 => b급 이하 판정 논문 => 구글
# 전화번호부
# Yahoo  == 전화번호부 (등록해야지 볼수 있음)

# books.toscrap.com
# python web scraping book 고전도서인데 저자가 데모 사이트로 만든 스크래퍼 사이트

