from person import Person

class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        # name과 age는 person에서 self로 저장하는 루틴 그대로 상속 받으니까 안씀
        self.company = company
    
    def greet(self): # override
        print(f"안녕하세요, 저는 {self.company}에 다니고 있는 {self.name}입니다.")






