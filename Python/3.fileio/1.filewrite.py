#파일 제어
with open("file.txt","a",encoding="UTF-8") as file:
    """여기에서 파일에 기록한 내용을 적음""" 
    file.write("원하는 데이터\n")
    file.write("hello World")