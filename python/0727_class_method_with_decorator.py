#---------------------------------------------------
# 데코레이터
#---------------------------------------------------

def add_print(original):
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper

@add_print
def print_hello():
    print('hello')

print_hello()

#---------------------------------------------------
# 메서드 정리
#---------------------------------------------------

class MyClass:
    def method(self):
        return 'instance method', self
    
    @classmethod
    def classmethod(cls):
        return 'class method', cls
    
    @staticmethod
    def staticmethod():
        return 'static method'

# 인스턴스 메서드를 호출한 결과
obj = MyClass()
print(obj.method())
print(MyClass.method(obj))

# 클래스 자체에서 각 메서드를 호출하는 경우
## 인스턴스 메서드는 호출할 수 없음
print(MyClass.classmethod())
print(MyClass.staticmethod())
# MyClass.method() # TypeError: method() missing 1 required positional argument: 'self'

# 인스턴스는 클래스 메서드와 스태틱 메서드 모두 접근할 수 있음
print('인스턴스는 클래스 메서드와 스태틱 메서드 모두 접근할 수 있음')
print(obj.classmethod())
print(MyClass.classmethod())
print(obj.staticmethod())

#---------------------------------------------------
#  상속
#---------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.department = gpa

p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 20, 3.5)

p1.talk()
s1.talk()