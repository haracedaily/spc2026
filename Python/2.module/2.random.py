import random
import string
def generate_random_password(length=8):
    # characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    characters = string.ascii_letters + string.digits + string.punctuation # string 모듈의 ascii_letters, digits, punctuation을 사용하여 characters를 생성한다.
    print(characters)
    return "".join([random.choice(characters) for _ in range(length)]) # characters에서 length만큼 랜덤하게 선택하여 문자열로 반환한다.


print("생성된 랜덤 비밀번호: ", generate_random_password())
