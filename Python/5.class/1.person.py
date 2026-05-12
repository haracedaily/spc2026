class Person:
    # 정의할때 주로 사용 attr method 객체생성(instance ==instantiation)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"안녕하세요, 저는 {self.name} 입니다.")
    
    def study(self, sub="Cs"):
        print(f"{self.name}는 {sub}를 공부하고 있습니다.")

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name=name
        self.age = age
    
    def cry(self):
        print(f"{self.name} crying")
person1 = Person("Alice",25)
person2 = Person("Bob",27)

child1 = Child("James",10)
child1.greet()
person1.greet()
person2.greet()

person1.study("Python")
person2.study()
child1.study()
child1.cry()