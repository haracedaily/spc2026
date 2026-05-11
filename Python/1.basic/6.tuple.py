my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0]) # 튜플의 첫 번째 요소에 접근한다.
print(my_list[0]) # 리스트의 첫 번째 요소에 접근한다.
my_list[2] = 10 # 리스트의 세 번째 요소를 10으로 변경한다.
print(my_list)
#my_tuple[2] = 10 # 튜플의 세 번째 요소를 10으로 변경하려고 하면 TypeError가 발생한다.

print(my_tuple[-1]) # 튜플의 마지막 요소에 접근한다.
print(my_list[-1]) # 리스트의 마지막 요소에 접근한다.
print(my_tuple[1:4]) # 튜플의 두 번째 요소부터 네 번째 요소까지 접근한다.
print(my_list[1:4]) # 리스트의 두 번째 요소부터 네 번째 요소까지 접근한다.
print(my_tuple[0:1]) # (1) 이 아니고 (1,) 이다. 튜플의 첫 번째 요소부터 첫 번째 요소까지 접근한다. 슬라이스 연산은 항상 튜플을 반환한다.
print(my_list[0:1])

# 튜플은 받아 왔는데, 값을 쓰고 싶으면??
new_list = list(my_tuple) # 튜플을 리스트로 변환한다.
new_list[2] = 10 # 리스트의 세 번째 요소를 10으로 변경한다
print(new_list)
print(my_tuple) # 튜플은 변경되지 않는다. 튜플은 변경할 수 없지만, 리스트로 변환해서 변경한 후 다시 튜플로 변환하면 새로운 튜플을 만들 수 있다.
my_new_tuple = tuple(new_list) # 리스트를 튜플로 변환한다. 튜플은 변경할 수 없지만, 리스트로 변환해서 변경한 후 다시 튜플로 변환하면 새로운 튜플을 만들 수 있다.
print(my_new_tuple)
new_list[2] = 3 # 리스트의 세 번째 요소를 3으로 변경한다.
print(new_list)
print(my_new_tuple) # 튜플은 변경되지 않는다. 튜플은 변경할 수 없지만, 리스트로 변환해서 변경한 후 다시 튜플로 변환하면 새로운 튜플을 만들 수 있다. 하지만, 이미 만들어진 튜플은 변경할 수 없다.

a,b,c,d,e = my_tuple # 튜플의 요소를 각각 a, b, c, d, e에 할당한다. 언패킹이라고도 한다.
print(a)
print(b)
print(c)
print(d)
print(e)
print(len(my_tuple)) # 튜플의 길이를 반환한다.
for i in my_tuple: # 튜플의 요소를 반복한다.
    print(i)

a_person = ("John", 23, "Student") # 튜플을 사용하여 사람의 이름, 나이, 직업을 저장한다.
name, age, occupation = a_person # 튜플의 요소를 각각 name, age, occupation에 할당한다. 언패킹이라고도 한다.
print(name)
print(age)
print(occupation)
print(a_person)