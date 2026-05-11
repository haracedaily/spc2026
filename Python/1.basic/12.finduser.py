users = [
    {"name": "강민호", "age": 28, "location": "서울", "car": "현대 아반떼"},
    {"name": "김지수", "age": 31, "location": "부산", "car": "기아 K5"},
    {"name": "하유나", "age": 24, "location": "인천", "car": "테슬라 모델 3"},
    {"name": "다니엘", "age": 35, "location": "대구", "car": "BMW 520i"},
    {"name": "이수진", "age": 27, "location": "대전", "car": "제네시스 G80"},
    {"name": "크리스", "age": 30, "location": "광주", "car": "아우디 A6"},
    {"name": "김하나", "age": 22, "location": "수원", "car": "기아 모닝"},
    {"name": "김케빈", "age": 40, "location": "울산", "car": "벤츠 E클래스"},
    {"name": "이은지", "age": 26, "location": "제주", "car": "현대 투싼"},
    {"name": "알렉스", "age": 33, "location": "세종", "car": "볼보 XC60"}
]

def find_user(name):
    for user in users:
        #if user["name"] == name: 정확한 매칭 찾기
        if user["name"].startswith(name): # 이름이 name으로 시작하는 사용자 찾기
            print(user)

find_user("김")
find_user("이")
print("-" * 20)
def find_user_and_return(name):
    return [user for user in users if user["name"].startswith(name)]
    # for user in users:
    #     if user["name"].startswith(name):
    #         return user # 이름이 name으로 시작하는 사용자 찾기 ???? 하나만 리턴?
    # return None # 이름이 name으로 시작하는 사용자가 없는 경우 None을 반환한다.

found_user = find_user_and_return("오")

found_user and print(found_user) or print("사용자를 찾을 수 없습니다.")
print(found_user)


print("=" * 50)

"""
def find_users2(keyword):
    #이름 또는 나이를 입력받아 매칭되는 사람을 반환한다
    return [user for user in users if user["name"].startswith(keyword) or str(user["age"]).startswith(keyword)]
print(find_users2(input("이름 또는 나이를 입력하세요 : ")))
"""

def find_users2(name=None, age=None):
    #이름 또는 나이를 입력받아 매칭되는 사람을 반환한다
    print(f"name : {name}, age : {age}")
    found = []
    if name is not None and age is not None:
        return [user for user in users if name == user["name"] and age == user["age"]]
    elif name is not None:
        return [user for user in users if name == user["name"] or user["name"].startswith(name)]
    elif age is not None:
        return [user for user in users if age == str(user["age"]) or str(user["age"]).startswith(age)]
    
    return found
print(find_users2("김하나", 22))
print(find_users2("김하나", 24))
print(find_users2("김하나"))
print(find_users2(age="22"))#age로만 찾기

print("-" * 40)
def find_users2_better(name=None, age=None, location=None):
    """이름 또는 나이를 입력 받아 매칭되는 사람을 반환한다 """
    found = []
    for user in users:
        if (name is None or user["name"] == name) \
        and (age is None or user["age"] == age) \
        and (location is None or user["location"] == location) :
            found.append(user)
    return found
#print(find_users2_better("김하나", 22))
#print(find_users2_better("김하나", 24))
#print(find_users2_better("김하나"))
print(find_users2_better(age=22))#age로만 찾기
#print(find_users2_better(location="수원"))#location으로만 찾기


print("=+" * 20)

search_condition1 = {
    "name" : "이은지"
}

search_condition2 = {
    "name" : "이은지",
    "age" : 25
}

search_condition3 = {
    "age" : 26
}

def find_users2_best(condition):
    found = []
    for user in users:
        if user.get("name") == condition.get("name",user.get("name")) and \
        user.get("age") == condition.get("age",user.get("age")) and \
        user.get("location") == condition.get("location",user.get("location")) :
            found.append(user)
    return found
"""def find_users2_best(condition):
    found = []

    for user in users:
        if all(user.get(key) == value for key, value in condition.items()):
            found.append(user)

    return found"""
print(find_users2_best(search_condition1))