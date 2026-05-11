import math

print(f"{math.pi:.2f}")
print(math.sqrt(16))
print(math.sin(0)) # degree x, radian으로 변환해야한다. math.sin(math.radians(5))로 해야한다.
print(math.sin(math.pi*2))

import datetime as dt # datetime 모듈을 dt라는 이름으로 사용하겠다. alias 사용

# module/class/function()
print(dt.datetime.now())
print(dt.datetime.now().strftime("%Y-%m-%d")) # strftime : datetime 객체를 문자열로 변환하는 함수, format 지정 가능
print(dt.datetime.now().strftime("%H:%M:%S"))

a_day = dt.datetime(2025, 1, 1, 10, 0, 0) # datetime 객체를 생성한다. (year, month, day, hour, minute, second)
print(a_day)
print(a_day.year)
print(a_day.month)
print(a_day.day)
print(a_day.hour)
print(a_day.minute)
print(a_day.second)
# MDN <- HTML/CSS/JS 문서 참고
# JavaDocs <- Java 문서 참고
# Python Docs <- Python 문서 참고 => search에서 module로 검색하면 된다.
import random
print("-" * 20 , "Random Module", "-" * 20)
print(random.randint(1, 10)) # 1부터 10까지의 정수 중에서 랜덤한 정수를 반환한다.
# random int 줄여서 randint
print(random.random()) # 0.0부터 1.0까지의 랜덤한 실수를 반환한다.
print(random.choice([1, 2, 3, 4, 5])) # 리스트에서 랜덤한 요소를 반환한다.
print(random.sample([1, 2, 3, 4, 5], 3)) # 리스트에서 랜덤한 요소를 3개 반환한다. 중복되지 않는다.

#주사위 던지기
def roll_dice():
    my_number = random.randint(1, 6) # 1부터 6까지의 정수 중에서 랜덤한 정수를 반환한다.
    return my_number
    # return random.randint(1, 6)
print("내 주사위의 숫자는 ", roll_dice())
print("내 주사위의 숫자는 ", roll_dice())
print("내 주사위의 숫자는 ", roll_dice())
print("내 주사위의 숫자는 ", roll_dice())
print("내 주사위의 숫자는 ", roll_dice())
print("내 주사위의 숫자는 ", roll_dice())
print("내 주사위의 숫자는 ", roll_dice())
print("내 주사위의 숫자는 ", roll_dice())
print("내 주사위의 숫자는 ", roll_dice())
print("내 주사위의 숫자는 ", roll_dice())

fruits = ["apple", "banana", "cherry", "grape", "orange", "pineapple","melon"]
def pick_fruit():
    my_num = random.randint(0, len(fruits)-1)
    return fruits[my_num]
def pick_fruit2():
    return random.choice(fruits)
print("내 과일은 ", pick_fruit())
print("내 과일은 ", pick_fruit())
print("내 과일은 ", pick_fruit())
print("내 과일은 ", pick_fruit())
print("내 과일은 ", pick_fruit())
print("내 과일은 ", pick_fruit())
print("내 과일은 ", pick_fruit2())
print("내 과일은 ", pick_fruit2())
print("내 과일은 ", pick_fruit2())
print("내 과일은 ", pick_fruit2())
print("내 과일은 ", pick_fruit2())
print("내 과일은 ", pick_fruit2())
print("내 과일은 ", pick_fruit2())