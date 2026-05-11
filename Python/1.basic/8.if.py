print('--- if 구문 ---')

#score = int(input('점수를 입력하세요: '))
score = 85
if score >= 85 :
    print('성적은 A+ 입니다.')
    grade = 'A+'
elif score >= 80 :
    print('성적은 A 입니다.')
    grade = 'A'
elif score >= 70 :
    print('성적은 B 입니다.')
    grade = 'B'
elif score >= 60 :
    print('성적은 C 입니다.')
    grade = 'C'
else :
    print('성적은 F 입니다.')
    grade = 'F'

print(f'학생의 성적은 {score}이고 점수는 {grade} 입니다.')


month = 3

#month = int(input('월을 입력하세요: '))
if month in [12, 1, 2] :
    print('겨울입니다.')
elif month in [3, 4, 5] :
    print('봄입니다.')
elif month in [6, 7, 8] :
    print('여름입니다.')
elif month in [9, 10, 11] :
    print('가을입니다.')
else :
    print('잘못된 입력입니다. 1부터 12 사이의 숫자를 입력하세요.')

#height = float(input('키를 입력하세요 (cm): '))
#weight = float(input('몸무게를 입력하세요 (kg): '))
height = 170
weight = 65
bmi = weight / (height / 100) ** 2
print(f'당신의 BMI는 {bmi:.2f}입니다.')
if bmi < 18.5 :
    category = '저체중'
elif bmi < 23 :
    category = '정상'
elif bmi < 25 :
    category = '과체중'
else :
    category = '비만'

print(f'당신의 키는 {height}cm, 몸무게는 {weight}kg이며, bmi지수는 {bmi:.2f}이고 체중 상태는 {category}입니다.')

username = "user"
password = "1234"

if username and password :
    if username == "admin" and password == "1234" :
        print("관리자로 로그인 되었습니다.")
    elif username == "user" and password == "1234" :
        print("일반 사용자로 로그인 되었습니다.")
    else :
        print("잘못된 ID 또는 비밀번호입니다.")
else :
    print("아이디와 비밀번호를 입력하세요.")

