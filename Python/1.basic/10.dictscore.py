def calculate_grade(student) :    
    for name, score in student.items() :
        if score >= 85 :
            grade = 'A+'
        elif score >= 80 :
            grade = 'A'
        elif score >= 70 :
            grade = 'B'
        elif score >= 60 :
            grade = 'C'
        else :
            grade = 'F'
        print(f'{name} 학생의 점수는 {score}이고, 성적은 {grade}입니다.')

        
students = {
    "김철수" : 70,
    "이영희" : 85,
    "박민수" : 75,
    "최지수" : 85,
    "정수진" : 70,
    "장성호" : 85,
    "홍길동" : 70,
    "김길동" : 85,
    "이영애" : 70,
    "고길동" : 85,
    "길영애" : 70,
    "이지영" : 85,
    "이지훈" : 70,
    "김교희" : 85,
    "김길수" : 70,
    "이시현" : 85,
}
calculate_grade(students)
#definition : 이과/공대
#justice : 문과/법대 