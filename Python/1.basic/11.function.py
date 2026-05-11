def add_numbers(a,b):
    """이 함수는 인자를 두개 받아서 합을 반환하는 함수 입니다."""
    result = a + b
    return result

sum = add_numbers(3, 4)
print(f"두 수의 합은 {sum}입니다.")

def add_numbers2(a,b):
    """이 함수는 인자를 두개 받아서 합을 반환하는 함수 입니다."""
    return a,b,a + b
input1,input2,sum = add_numbers2(3, 4)
print(f"두 수는 {input1}과 {input2}이며, 합은 {sum}입니다.")

def calculate_all(a,b):
    """이 함수는 원의 반지름을 받아서 원의 넓이를 반환하는 함수입니다."""
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition, subtraction, multiplication, division

add, sub, mul, div = calculate_all(3,4)
print(f"덧셈 : {add}, 뺄셈 : {sub}, 곱셈 : {mul}, 나눗셈 : {div}")

add, _, mul, _ = calculate_all(3,4) # 언더바(_)는 사용하지 않는 값을 무시하는 데 사용된다. 언더바는 변수 이름으로 사용할 수 있지만, 일반적으로 사용되지 않는 값을 나타내는 데 사용된다.
# 만약 리턴값보다 많은 변수를 할당하려고 하면 ValueError가 발생한다. 만약 리턴값보다 적은 변수를 할당하려고 하면 ValueError가 발생한다.
# 예를 들어, add, mul = calculate_all(3,4) 라고 하면 ValueError가 발생한다. add, sub, mul = calculate_all(3,4) 라고 하면 ValueError가 발생한다. add, sub, mul, div, extra = calculate_all(3,4) 라고 하면 ValueError가 발생한다.
# 언더바는 사용하지 않는 값을 무시하는 데 사용된다. 언더바는 변수 이름으로 사용할 수 있지만, 일반적으로 사용되지 않는 값을 나타내는 데 사용된다. 예를 들어, add, _, mul, _ = calculate_all(3,4) 라고 하면 add에는 덧셈 결과가 할당되고, mul에는 곱셈 결과가 할당되며, 뺄셈과 나눗셈 결과는 무시된다.
print(f"덧셈 : {add}, 곱셈 : {mul} 입니다.")


print("-" * 20)

def create_profile(name, age, city="Seoul"):
    profile = f"이름 : {name}, 나이 : {age}, 도시 : {city}"
    return profile

print(create_profile("홍길동", 23, "Busan"))
print(create_profile("김길동", 25, "Jeju"))
print(create_profile("박길동", 27, "Incheon"))