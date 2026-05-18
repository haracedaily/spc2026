import requests
import os
from dotenv import load_dotenv
# pip install python-dotenv
# import 알파벳 순 or 의미 순 or grouping or *회사*rule

load_dotenv()#.env 파일을 읽어서 해당 key/value를 메모리(환경변수)에 올린다.

# 메모리를 읽어야하니 os에서 env 접근
API_KEY = os.getenv("YOUTUBE_KEY")


url ="https://www.googleapis.com/youtube/v3/search"
main_video_url ="https://www.googleapis.com/youtube/v3/videos"

search_query = "파이썬 튜토리얼"

search_params = {
    'part':'snippet',
    'q': search_query,
    'type':'video',
    'maxResults':50,
    'key':API_KEY
}

response = requests.get(url,params=search_params)
data = response.json()
search_results=data['items']

table = []
table_header = ['index','title','view count','video url']
for index, result in enumerate(search_results, start=1):
    title = result['snippet']['title']
    video_id = result['id']['videoId']
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    video_params = {
        'part':'statistics',
        'id':video_id,
        'key':API_KEY
    }

    video_response = requests.get(main_video_url,params=video_params)
    video_data = video_response.json()

    if 'items' in video_data and video_data['items']:
        view_count = video_data['items'][0]['statistics']['viewCount']
    else :
        view_count ="N/A"

    table.append([title,video_id,video_url,view_count])
print(table)