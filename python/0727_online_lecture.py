# 객체 비교
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b, a is b) # True False

a = [1, 2, 3]
b = a 
print(a == b, a is b) # True True


# 속성
class Person:
    blood_color = 'red' # 클래스 변수
    population = 100 # 클래스 변수

    def __init__(self, name):
        self.name = name # 인스턴스 변수

person1 = Person('지민')
print(person1.name)


# 인스턴스 변수

class Person:

    def __init__(self, name): # 인스턴스 변수 정의
        self.name = name

john = Person('john') # 인스턴스 변수 접근 및 할당
print(john.name) # john
john.name = 'John Kim' # 인스턴스 변수 접근 및 할당
print(john.name) # John Kim


# 클래스 변수
class Circle():
    pi = 3.14 # 클래스 변수 정의

    def __init__(self, r):
        self.r = r # 인스턴스 변수

c1 = Circle(5)
c2 = Circle(10)
print(Circle.pi) # 3.14
print(c1.pi) # 3.14 
print(c2.pi) # 3.14

Circle.pi = 5
print(Circle.pi) # 5
print(c1.pi) # 5
print(c2.pi) # 5
