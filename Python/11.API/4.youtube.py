import requests
import os
from dotenv import load_dotenv
# pip install python-dotenv
# import 알파벳 순 or 의미 순 or grouping or *회사*rule

load_dotenv()#.env 파일을 읽어서 해당 key/value를 메모리(환경변수)에 올린다.

# 메모리를 읽어야하니 os에서 env 접근
API_KEY = os.getenv("YOUTUBE_KEY")


url ="https://www.googleapis.com/youtube/v3/search"

search_query = "파이썬 튜토리얼"

params = {
    'part':'snippet',
    'q': search_query,
    'type':'video',
    'maxResults':50,
    'key':API_KEY
}
response = requests.get(url,params)
data = response.json()
search_results=data['items']
print(data)
for item in data["items"]:
    title = item["snippet"]["title"]
    video_id = item['id']['videoId']
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    description = item['snippet']['description']
    # search_results.extend(item)
    print(f"제목 : {title} , 비디오ID : {video_id} , 비디오 url:{video_url}, 설명 : {description}")

