#pip install playwright
#playwright install <-- 각장 브라우저 드라이버를 관리
# chromium, firefox, webkit, ffme
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #크롬을 실행한다
    # headless True => GUI창을 안 띄움
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.naver.com")

    print(page.title())
    input("Enter를 누르면 종료됩니다.")

#pip install selenium  webdriver 사람이 수동으로 하지말자?<
# 브릿지 chromedriver

# nvidia 그래픽 nvidir 디바이스 드라이버