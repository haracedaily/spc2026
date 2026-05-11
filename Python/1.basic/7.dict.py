"""
딕셔너리
키:밸류로 쌍을 이루고 있는 자료구조
"""
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict["name"]) # 딕셔너리에서 "name" 키에 해당하는 값을 반환한다.
print(my_dict["age"]) # 딕셔너리에서 "age" 키에 해당하는 값을 반환한다.
print(my_dict["city"]) # 딕셔너리에서 "city" 키에 해당하는 값을 반환한다.
for key in my_dict: # 딕셔너리의 키를 반복한다.
    print(f"{key} : {my_dict[key]}") # 딕셔너리에서 key에 해당하는 값을 반환한다.
for key, value in my_dict.items(): # 딕셔너리의 키와 값을 동시에 반복한다.
    print(f"{key} : {value}") # key와 value를 출력한다.

my_dict["car"] = "Tesla" # 딕셔너리에 "car" 키와 "Tesla" 값을 추가한다.
print(my_dict)
del my_dict["age"] # 딕셔너리에서 "age" 키와 해당하는 값을 제거한다.
print(my_dict)

my_city = my_dict.pop("city") # 딕셔너리에서 "city" 키와 해당하는 값을 제거하고 반환한다.
print(my_city) # "New York"이 출력된다.
print(my_dict) # "city" 키와 해당하는 값이 제거된 딕셔너리가 출력된다.
print(my_dict.keys()) # 딕셔너리의 모든 키를 반환한다.
print(my_dict.values()) # 딕셔너리의 모든 값을 반환한다.
print(my_dict.items()) # 딕셔너리의 모든 키-값 쌍을 반환한다.
my_dict.clear() # 딕셔너리의 모든 키와 값을 제거한다.
print(my_dict) # 빈 딕셔너리가 출력된다.
#list처럼 딕셔너리도 컴프리헨션이 있다.
squared_dict = {x: x**2 for x in range(1, 6)} # 1부터 5까지의 숫자를 키로 하고, 해당 숫자의 제곱을 값으로 하는 딕셔너리를 생성한다.
print(squared_dict)
print(squared_dict.keys()) # 딕셔너리의 모든 키를 반환한다. dict_keys([1, 2, 3, 4, 5])가 출력된다.
print(squared_dict.values()) # 딕셔너리의 모든 값을 반환한다. dict_values([1, 4, 9, 16, 25])가 출력된다.
for x in squared_dict.values(): # 딕셔너리의 모든 값을 반복한다.
    print("value : " , end="") # 딕셔너리의 모든 값을 출력한다.
    print(x) # 딕셔너리의 모든 값을 출력한다.

"""
list = []   => list = list() # 리스트는 대괄호로 생성할 수 있지만, list() 함수를 사용하여 생성할 수도 있다.
tuple = ()  => tuple = tuple() # 튜플은 소괄호로 생성할 수 있지만, tuple() 함수를 사용하여 생성할 수도 있다.
dict = {}   => dict = dict() # 딕셔너리는 중괄호로 생성할 수 있지만, dict() 함수를 사용하여 생성할 수도 있다.
set = set() # 집합은 중괄호로 생성할 수 있지만, set() 함수를 사용하여 생성할 수도 있다.
"""

s = {1,2,3} # 집합을 중괄호로 생성한다.
print(s)
print(2 in s) # 집합에 2가 있는지 확인한다.
s.add(4) # 집합에 4를 추가한다.
print(s)
s.remove(2) # 집합에서 2를 제거한다.
print(s)