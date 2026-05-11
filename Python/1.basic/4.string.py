#문자열을 변수에 할당하면 string 타입
x = "Hello, World!"
print(x)
print(type(x))
print(x.lower()) # 문자열을 모두 소문자로 변환
print(x.upper()) # 문자열을 모두 대문자로 변환
print(x.capitalize()) # 문자열의 첫 글자만 대문자로 변환
print(x.title()) # 문자열의 각 단어의 첫 글자만 대문자로 변
y = 'Hello, Python!'
print(y)
print(type(y))
z = """Hello, Python!"""
print(z)
print(type(z))
a = 'Hello, "Python"!' # 문자열 안에 작은따옴표가 포함되어 있을 때는 큰따옴표로 감싸주면 된다.
print(a)
print(a.count('o')) # 문자열에서 'o'의 개수를 세어준다.
print(a.find('o')) # 문자열에서 'o'가 처음으로 나오는 위치를
print(a.find('o', 5)) # 문자열에서 'o'가 5번째 위치 이후로 처음으로 나오는 위치를 반환한다.
print(a.find('x')) # 문자열에서 'x'가 없는 경우 -1을 반환한다.
print(a.index('o')) # 문자열에서 'o'가 처음으로 나오는 위치를 반환한다. find와 달리 없는 경우 에러가 발생한다.
print(a.index('o', 5)) # 문자열에서 'o'가 5번째 위치 이후로 처음으로 나오는 위치를 반환한다. find와 달리 없는 경우 에러가 발생한다.

s = "    Hello,      World!    "
print(s.strip()+"!!") # 문자열의 양쪽 공백을 제거한다.
print(s.lstrip()+"!!") # 문자열의 왼쪽 공백을 제거한다.
print(s.rstrip()+"!!") # 문자열의 오른쪽 공백을 제거한다.
print(s.replace(" ", "")) # 문자열의 모든 공백을 제거한다.
print(s.split()) # 문자열을 공백을 기준으로 나누어 리스트로 반환한다
print(s.split(", ")) # 문자열을 ", "를 기준으로 나누어 리스트로 반환한다.
print(s.split(" ", 1)) # 문자열을 ", "를 기준으로 나누어 리스트로 반환하는데 최대 1번만 나눈다.

s = "apple banana cherry"
print(s.split()) # 문자열을 공백을 기준으로 나누어 리스트로 반환한다.
s="apple, banana, cherry"
print(s.split(",")) # 문자열을 ","를 기준으로 나누어 리스트로 반환한다.
s="apple,banana,cherry" # csv = comma separated values    csv는 띄워쓰기가 없음
print(s.split(",")) # 문자열을 ","를 기준으로 나누어 리스트로 반환한다.
print(s.split())# 문자열을 공백을 기준으로 나누어 리스트로 반환한다. 공백이 없기 때문에 전체 문자열이 하나의 요소로 반환된다.

s_list = s.split(",") # 문자열을 ","를 기준으로 나누어 리스트로 반환한다.
print(s_list)
print(",".join(s_list)) # 리스트의 요소들을 ","로 연결하여 문자열로 반환한다.
print(".".join(s_list)) # 리스트의 요소들을 ","로 연결하여 문자열로 반환한다.
print(" ".join(s_list)) # 리스트의 요소들을 ","로 연결하여 문자열로 반환한다.

s = "Hello, World"
print(s)
print(s.startswith("H")) # 문자열이 "Hello"로 시작하는지 확인한다.
print(s.startswith("h")) # 문자열이 "Hello"로 시작하는지 확인한다.
print(s.endswith("World")) # 문자열이 "World"로 끝나는지 확인한다.
print(s.endswith("D")) # 문자열이 "World"로 끝나는지 확인한다.
"""
docstring : 문자열로 된 주석
"""