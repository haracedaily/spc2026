
# ZeroDivisionError /0
# NameError O 
# TypeErr X ValueError O
# IndexError => 초과되는 인덱스 접근
# FileNotFoundError => 없는 파일 접근 ex) with open("없는파일.txt","r")

try:
    result = 10/0
except NameError:
    print("0으로 나눌수 없다.")
except:
    print("알수없는 에러")

print("다음 코드 정상 진행")

try:
    number = int("Hello")
except ValueError:
    print("해당 글자는 숫자 변환되지 않습니다.")
except:
    print("알수 없는 에러")


alist = [1,2,3]
try:
    alist[3]
except IndexError:
    print("없는 리스트 접근")


try:
    with open("없는파일명.txt","r") as file:
        data = file.read()
except FileNotFoundError:
    print("없는 파일 접근")
except FileExistsError:
    print("처리전 이미 파일이 꺼짐")
except:
    print("알수없는 에러")


# 커스텀 에러 raise <- 에러 강제 유발

# raise CustomError