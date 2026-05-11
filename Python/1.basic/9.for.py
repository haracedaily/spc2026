#numbers = [1,2,3,4,5]
numbers = [x for x in range(1,6)]
even_numbers =[]
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        print(f"{num} is even")
    else:
        odd_numbers.append(num)
        print(f"{num} is odd")

print(f"Even numbers : {even_numbers}")
print(f"Odd numbers : {odd_numbers}")

import time
start_time = time.time()

n=100
count = 0
# 시간 복잡도 O(n^4) : n이 증가할수록 실행 시간이 급격히 증가한다.
# 공간복잡도 O(1) : 추가적인 공간이 필요하지 않다.
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                count+=1
print("합산 : ",count)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.1f} seconds")
