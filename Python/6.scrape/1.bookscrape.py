# 1. books.toscrape.com 에 접속해서 페이지를 받아온다
# 2. DOM 을 bs4로 구성한다
# 3. 첫 페이지의 도서명, 평점, 가격을 받아온다
# 4. CSV파일로 저장한다.

from bs4 import BeautifulSoup
import requests
import csv

resp = requests.get("https://books.toscrape.com/")
resp.encoding="UTF-8" #유니코드 글자로 인식시켜서 깨지는 글자 제거

soup = BeautifulSoup(resp.text,"html.parser")

lists = []
rating_map={"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
articles = soup.find_all("article",class_="product_pod")
# books = soup.select("article.product_pod") article이면서 product_pod 클래스가 있는 거
# print(articles)
for elem in articles:
    quo = {}
    heading = elem.h3
    print("제목 : ",heading.a.get("title"))
    quo["title"]=heading.a.get("title")
    print(elem.find("h3").find("a")["title"])
    # paragraph = elem.p
    paragraph = elem.find("p",class_="star-rating")
    # if "star-rating" in paragraph.get("class"):
    # elem.p["class"][1]
    print("평점 : ",rating_map[paragraph.get("class")[1]])
    quo["star"]=rating_map[paragraph.get("class")[1]]
    # price = elem.find_all("div")[1].p.text
    # price = elem.select_one(".price_color").text
    price = elem.find("div",class_="product_price").p.text
    price = price.replace("£","")
    quo["price"]=price
    print("가격 : ",price)
    lists.append(quo)


with open("books.csv","w",encoding="utf-8",newline="") as file:
    """
    csv_writer = csv.writer(file)
    csv_writer.writerow("도서명","평점","가격")
    for in 여기에 넣고 csv_writer.writerow({title,star,price})
    
    """
    headers = lists[0].keys()
    # print(headers)
    csv_writer = csv.DictWriter(file,fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerows(lists)
