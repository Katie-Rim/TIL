#---------------------------------------------------
# 데코레이터 없이 함수 꾸미기
#---------------------------------------------------

def hello():
    print("hello")

# 데코레이팅 함수
def add_print(original):
    def wrapper():
        print("함수 시작")
        original()
        print("함수 끝")
    return wrapper

add_print(hello)()
print_hello = add_print(hello)
print_hello()
