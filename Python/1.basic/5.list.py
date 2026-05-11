my_list = [1,2,3,4,5]
print(my_list)
print(type(my_list))
print(my_list[0]) # 리스트의 첫 번째 요소에 접근한다.
print(my_list[1]) # 리스트의 두 번째 요소에 접근한다.
print(my_list[-1]) # 리스트의 마지막 요소에 접근한다.
print(my_list[1:4]) # 리스트의 두 번째 요소부터 네 번째 요소까지 접근한다.
print(my_list[:2]) # 리스트의 두 번째 요소부터 네 번째 요소까지 접근한다.
print(my_list[2:]) # 리스트의 두 번째 요소부터 네 번째 요소까지 접근한다.
my_list.append(6) # 리스트의 끝에 요소를 추가한다.
print(my_list)
my_list.insert(0, 0) # 리스트의 첫 번째 위치에 요소를 추가한다.
my_list.insert(0, -1) # 리스트의 첫 번째 위치에 요소를 추가한다.
print(my_list)
my_list.remove(3) # 리스트에서 첫 번째로 나오는 3을 제거한다.
print(my_list)
my_list.pop() # 리스트의 마지막 요소를 제거하고 반환한다.
print(my_list)
my_list.pop(0) # 리스트의 첫 번째 요소를 제거하고 반환한다. -1은 마지막에서 첫번째 요소(즉 뒤에서 두번째)를 제거한다.
print("pop 0 : " + str(my_list))
my_list[0] = 10 # 리스트의 첫 번째 요소를 10으로 변경한다.
print(my_list)
my_list[1:3] = [20, 30] # 리스트의 두 번째 요소부터 세 번째 요소까지를 [20, 30]으로 변경한다.
print(my_list)
my_list[3:5] = [] # 리스트의 세 번째 요소부터 다섯 번째 요소까지를 제거한다.
print(my_list)
my_list.remove(20) # 리스트에서 첫 번째로 나오는 20을 제거한다.
print(my_list)
my_list.clear() # 리스트의 모든 요소를 제거한다.
print(my_list)

my_list = [8,10,1,2,3,4,5]
sorted_list = sorted(my_list) # 리스트를 오름차순으로 정렬한 새로운 리스트를 반환한다. 원래 리스트는 변경되지 않는다.
print(sorted_list)
print(my_list)
my_list.sort() # 리스트를 오름차순으로 정렬한다. 반환값은 None이다.
print(my_list)

copy_list = my_list.copy() # 리스트의 얕은 복사본을 반환한다. 원래 리스트는 변경되지 않는다.
print(copy_list)
copy_list.append(6) # copy_list에 요소를 추가한다.
copy_list.sort(reverse=True) # copy_list를 내림차순으로 정렬한다.
print(copy_list)
print(my_list) # my_list는 변경되지 않는다.

#리스트 컴프리헨션 (어려운데, 쓰면 매우매우 편함)

numbers = [x*2 for x in range(1, 10)] # 1부터 9까지의 숫자를 포함하는 리스트를 생성한다.
print(numbers)
numbers = [x for x in range(5)] # 0부터 4까지의 숫자를 포함하는 리스트를 생성한다.
print(numbers)
numbers = [x*2 for x in range(1, 10) if x % 2 == 0] # 1부터 9까지의 숫자 중에서 짝수인 숫자를 포함하는 리스트를 생성한다.
print(numbers)
print(list(enumerate(numbers))) # 리스트의 요소와 인덱스를 동시에 반복하는 enumerate 객체를 반환한다.
for i, x in enumerate(numbers): # 리스트의 요소와 인덱스를 동시에 반복한다.
    print(f"index : {i}, value : {x}")
    if x % 4 == 0: # x가 4의 배수인 경우
        print(f"{x} is a multiple of 4")
for x in numbers:
    print(x)

numbers = [x                 for x in range(1,10)                if x % 2 == 0] # 1부터 9까지의 숫자 중에서 짝수인 숫자를 포함하는 리스트를 생성한다.
print(numbers)

list1 = [1,2,3]
list2 = [4,5,6]
combined_list = list1 + list2 # 두 리스트를 결합한다.
print(combined_list)
print(list1*3) # 리스트를 3번 반복한다.
print(list1*2 + list2) # 리스트를 2번 반복한 후에 다른 리스트를 결합한다.
