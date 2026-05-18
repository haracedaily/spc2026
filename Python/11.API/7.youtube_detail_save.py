import csv
import requests
import os
from dotenv import load_dotenv
# pip install python-dotenv
# import 알파벳 순 or 의미 순 or grouping or *회사*rule

load_dotenv()#.env 파일을 읽어서 해당 key/value를 메모리(환경변수)에 올린다.

# 메모리를 읽어야하니 os에서 env 접근
API_KEY = os.getenv("YOUTUBE_KEY")

main_video_url ="https://www.googleapis.com/youtube/v3/videos"
video_ids = []

with open("search_result.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        video_ids.append(row["video_id"])

# print(video_ids)

params = {
    "part":"snippet,statistics",
    "id":",".join(video_ids),
    "key":API_KEY
}

response = requests.get(main_video_url,params=params)
data = response.json()
print("-"*30)
print(data["items"])
# 최종 결과 저장용
table = []

# 테이블 헤더
table_header = ['video_id','title','view_count',"like_count","comment_count"]

with open("video_stats.csv","w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(table_header)
    for item in data["items"]:
        video_id = item['id']
        title = item['snippet']['title']
        stats = item['statistics']
        view_count = stats.get("viewCount",0)
        like_count = stats.get("likeCount",0)
        comment_count = stats.get("commentCount",0)

        writer.writerow([video_id,title,view_count,like_count,comment_count]) 

# 데이터 결과    # 

# 각 영상 상세조회
# for result, index in enumerate(data["items"], start=1):
#     title = result['snippet']['title']
#     video_id = result['id']['videoId']
#     video_url = f"https://www.youtube.com/watch?v={video_id}"

#     video_params = {
#         'part':'statistics',
#         'id':video_id,
#         'key':API_KEY
#     }

#     video_response = requests.get(main_video_url,video_params)
#     video_data = video_response.json()

#     if 'items' in video_data and video_data['items']:
#         view_count = video_data['items'][0]['statistics']['viewCount']
#     else :
#         view_count =" N/A"

#     table.append([title,video_id,video_url,view_count])
# print(table)