from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://news.naver.com/section/105")

    lis = page.locator("div.as_headline ul li")

    links = []

    for i in range(lis.count()) :
        # 접근선택자 selector처럼 굳이 자식하나씩 내려가지 않아도 됨 > 선택자 x 그냥 지정 find같은 느낌
        a = lis.nth(i).locator("div.sa_text a").first

        href = a.get_attribute("href")
        # print(a.inner_text().strip())
        # a.inner_text()해도 무관하게 잘 나오지만 공백이 들어가져서 strip으로 공백을 날려줘야함
        # print(href)
        title = a.locator("strong").inner_text()
        # print(title)
        # 굳이 공백제거 하지 않아도 원하는 요소에 직접적으로 접근하여 출력한거라 그런가 text 자체를 가져옴
        links.append({"title":title,"href":href})

    for news in links:
        print("-"*30)
        print("제목 : ",news["title"])
        print("href : ",news["href"])
        page.goto(news["href"])
        print(
        page.locator("#dic_area").inner_text().strip()
        )