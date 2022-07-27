| Daily Workshop |
8기 서울 1반 임성아

# Python 02. 데이터 타입 및 형 변환

### 1. 숫자의 입력과 출력
입력 받은 데이터를 숫자로 변환하고 덧셈해서 출력하는 프로그램을 작성하시오
(힌트 : `input()` 함수를 활용하여 데이터를 입력받을 수 있다 .)

    a = int(input())
    b = int(input())
    sum = a + b
    print(sum)

### 2. Dictionary를 활용하여 평균 구하기
좋아하는 점심메뉴를 이용하여 key 는 메뉴 , value 는 가격인 dictionary 를 만들고 점심메뉴의 평균 값을 출력하시오    

    lunch = {
    'sushi': 30000,
    'chicken': 20000,
    'pizza': 27000
    }

    average = sum(lunch.values()) / len(lunch)

    print(average)
