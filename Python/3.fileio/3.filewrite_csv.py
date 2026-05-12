import csv

# 예전 방식
data = [
    ["Name","Age","City"], # Heading = first line
    ["John",25,"Seoul"],
    ["James", 23, "Busan"],
    ["Bob", 24, "Seoul"]
]

filename = "data.csv"
with open(filename,"w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

# Modern한 방식
# 메모리 낭비하는 경향 => 직관적이면 어느정도의 메모리 누수는 감수하려는 경향 => 메모리 중시 ->
data2 = [
    {"Name":"John","Age":25,"City":"Seoul"},
    {"Name":"James", "Age":23, "City":"Busan"},
    {"Name":"Bob", "Age":24, "City":"Seoul"}
]

with open(filename,"w",newline="") as file:
    # headers = ["Name","Age","City"]
    headers = data2[0].keys()
    print(headers)
    csv_writer=csv.DictWriter(file, fieldnames=headers)
    # dictionary parsing 
    csv_writer.writeheader() # 첫줄에 헤더 적기
    csv_writer.writerows(data2) # dict를 csv로 파싱해서 저장