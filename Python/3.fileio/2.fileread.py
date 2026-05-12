# 1.작은파일 열기
with open("file.txt","r",encoding="utf-8") as file:
    data = file.read()
    print("파일 내용 : "+data)


# 2. 레거시 파일 open / read / close
# # file = open("file.txt","r",encoding="utf-8")
# data = file.read()
# file.close()
# print(data)

# 3. 큰 파일 읽기
with open("file.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
    print("파일 내용 : ", lines)
    for line in lines:
        print("한줄 읽기:",line)

# xml or csv ( split = "," not space)