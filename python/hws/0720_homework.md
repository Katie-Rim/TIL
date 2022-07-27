0720  Daily Homework 

## Python 03. 제어문과 함수

#### 1. Built-in 함수
Python에서 기본으로 사용할 수 있는 built-in 함수를 최소 5가지 이상 작성하시오.

    abs()
    aiter()
    all()
    any()
    anext()
    ascii()
    

#### 2. 홀수만 담기
range와 slicing을 활용하여 1부터 50까지의 숫자 중, 홀수로만 이루어진 리스트를 만드시오.

    # range
    num_list = list(range(1, 51))
    # print(num_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

    # slicing
    odd_list = num_list[0:50:2]
    print(odd_list) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

#### 3. 반복문으로 네모 출력
두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를
별(*) 문자를 이용하여 출력하시오. 단, 반복문을 사용하여 작성하시오.
    
    n = 5
    m = 9
    for i in range(m):
        print('*'*n)
        i += 1

#### 4. 조건 표현식
주어진 코드의 조건문을 조건 표현식으로 바꾸어 작성하시오.

    temp = 36.5
    if temp >= 37.5:
        print('입실 불가')
    else:
        print('입실 가능')

    #조건 표현식
    result = '입실 불가' if temp >= 37.5 else '입실 가능'
    print(result)

#### 5. 정중앙 문자

문자열을 전달 받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를 작성하시오. 
단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다.

    get_middle_char('ssafy’) # => a
    get_middle_char('coding’) # => di

풀이:

```
def get_middle_char(word):
  middle_char = len(word) // 2
  if len(word) % 2 ==0:
    return word[middle_char-1] + word[middle_char] 
  else:
    return word[middle_char]

print(get_middle_char('ssafy')) # a
print(get_middle_char('coding')) # di
```
