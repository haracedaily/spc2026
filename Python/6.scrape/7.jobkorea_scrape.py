from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # 여기가 잡코리아에서 개발자로 검색
    page.goto("https://www.jobkorea.co.kr/Search/?stext=개발자&tabType=recruit")
    div = page.locator('div[data-sentry-component="JobList"]>div').nth(1).locator(">div")
    print(div.count())
    for i in range(div.count()):
        notice = div.nth(i)
        href = notice.locator("a").first
        href = href.get_attribute("href")
        print(href)
        title = notice.locator('span.truncate').first.inner_text()
        print("공고명 : ",title)
    # lis = page.locator("div.as_headline ul li")
