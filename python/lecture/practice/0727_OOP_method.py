#---------------------------------------------------
# OOP 메서드
#---------------------------------------------------

class Person:
    def talk(self):
        print('안녕')
    
    def eat(self, food):
        print(f'{food}를 냠냠')

person1 = Person()
person1.talk() 
person1.eat('피자')
person1.eat('치킨')

#---------------------------------------------------
# 생성자 메서드
#---------------------------------------------------

class Person:
    def __init__(self, name):
        print(f'인스턴스가 생성됨. {name}')

person1 = Person('성아')

#---------------------------------------------------
# 소멸자 메서드
#---------------------------------------------------

class PersonBye:
    def __del__(self):
        print('인스턴스가 소멸됨')

person1 = PersonBye()

#---------------------------------------------------
# 매직 메서드 예시
#---------------------------------------------------

class Circle:

    def __init__(self, r):
        self.r = r
    
    def area(self):
        return 3.14 * self.r ** 2
    
    def __str__(self):
        return f'[원] radius; {self.r}'
    
    def __gt__(self, other):
        return self.r > other.r

c1 = Circle(10)
c2 = Circle(1)

print(c1) # [원] radius; 10
print(c2)
print(c1.area())
print(c1 > c2)
print(c1 < c2)
