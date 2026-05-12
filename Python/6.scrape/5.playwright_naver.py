from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.naver.com/")

    div = page.locator("div.ContentHeaderSubView-module__news_box___dH9b3 div div div a").inner_text()
    print(div)