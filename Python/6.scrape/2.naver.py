from bs4 import BeautifulSoup
import requests
import csv

resp = requests.get("https://www.naver.com/")
resp.encoding="UTF-8" #유니코드 글자로 인식시켜서 깨지는 글자 제거

soup = BeautifulSoup(resp.text,"html.parser")

# JS를 파싱해서 실행 => 웹
# 브라우저를 제어하는 SW => Selenium

# req<--요청하는 애
# bs4<--DOM parsing
# selenium <-- Browser Control

# (selenium과 bs4가 의존)

# playwright <-MS가 만듬 
# 디바이스, 해상도, 브라우저들