# 숫자를 할당하면 타입은 int로 주어짐
x = 5
y = 3
print(x)
print(type(x))
print(y)
print(type(y))
# 사칙연산
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y) # 몫
print(x % y) # 나머지
print (x ^ y) # XOR
print(x ** y) # 제곱
print(x << y) # 비트 왼쪽 시프트 0000_0101 -> 0000_1010
print(x >> 1) # 비트 오른쪽 시프트 0000_0101 -> 0000_0010
print(~x) # 비트 NOT 00000101 -> 11111010 # 2의 보수로 표현하기 때문에 -6이 나옴 첫째자리가 부호비트이기 때문에 1이면 음수, 0이면 양수


x=11
print(bin(x)) # 2진수로 변환
print(oct(x)) # 8진수로 변환 (잘안씀)
print(hex(x)) # 16진수로 변환

y = 4.5
print(y)
print(type(y))
print(int(y)) # 실수를 정수로 변환
print(float(x)) # 정수를 실수로 변환

z = "100"
print(z)
print(type(z))
print(int(z)) # 문자열을 정수로 변환

a, b = divmod(x, int(y)) # x를 y로 나눈 몫과 나머지를 반환
print(a) # 몫
print(b) # 나머지