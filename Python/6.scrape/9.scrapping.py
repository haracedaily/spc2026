from playwright.sync_api import sync_playwright

# 1. 각 페이지마다 상품제목 가격가져오기
# 2. 그 다음에 각 페이지 안의 설명 구매량, 댓글 가져오기
# 3. 로그인후 추가 상품정보 가져오기

# 이후 다음주에는 거기서 LLM 연동해서 가져온 글로 감정분석 등 진행 예정입니다

with sync_playwright() as p:
    # sync_playwright 안의 크롬 connector launch 하여 새로운 웹을 연다<=
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36")
    addr = "https://makemyproject.net/shop/"
    page.goto(addr,wait_until="networkidle")
    pager = page.locator("div#pager.pager").inner_text()[-1]
    divs = page.locator('div#products > div')

    links = []
    print(pager)
    for i in range(divs.count()):
        dict={}
        a= divs.nth(i).locator("a")
        dict["title"] = a.inner_text()
        dict["href"] = addr+a.get_attribute("href")
        links.append(dict)
        break
    
    for link in links:
        page.goto(link["href"])
        print(link["title"])
        print("상품설명 : "+page.locator("div.muted").first.inner_text())
        print("누적판매량 : "+page.locator("div#sales").inner_text())
        print("후기 : "+ page.locator("div#wrap").last.inner_text())
        break

    page.goto(addr,wait_until="networkidle")
    page.fill("input#uid","user123")
    page.fill("input#upw","password1234")
    page.click('button#loginBtn')
    log_pagers = page.locator("div#pager.pager > button")
    print(log_pagers.count())
    for pager in range(log_pagers.count()):
        print(pager)