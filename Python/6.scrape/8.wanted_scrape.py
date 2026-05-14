from playwright.sync_api import sync_playwright
import time

time.sleep(1)
with sync_playwright() as p:
    # sync_playwright 안의 크롬 connector launch 하여 새로운 웹을 연다<=
    browser = p.chromium.launch(headless=True        )
    page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36")

    addr = "https://www.wanted.co.kr"
    page.goto(addr)
    li = page.locator('div[data-cy="job-card"]')

    links = []

    for i in range(li.count()):
        dict = {}
        a = li.nth(i).locator('a')
        dict["href"]=addr+a.get_attribute('href')
        dict["company"] = li.nth(i).locator('span.CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu').inner_text()
        links.append(dict)
        # break

    for link in links[:10]:
        page.goto(link["href"])
        jd = page.locator("article.JobDescription_JobDescription__s2Keo").inner_text()
        print("="*33)
        print(link["company"],end=" ")
        print("Job Description : ")        
        print(jd)
        # break