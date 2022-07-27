프로그램이란?
- 특정 작업을 수행하는 일련의 명령어들의 모음

주석(comment)
- 개발자에게 주석을 다는 습관은 매우 중요
- `#`: 한 줄 주석
- ''' OR """: 여러 줄 주석

변수의 할당
- 할당 연산자(=)를 통해 값 할당(assignment)
- 같은 값을 동시에 할당할 수 있음
```python
a = b = 2000
```
- 다른 값을 동시에 할당할 수 있음
```python
a, b = 2000, 3000
```
각 변수의 값을 바꿔서 저장하기

- 방법1: 임시 변수 활용
```python
x, y = 10, 20
tmp = x
x = y
y = tmp
print(x, y) # 20, 10
```
- 방법2: Pythonic
```
x, y = 10, 20
y, x = x, y
print(x,y) # 20 10
```

변수 이름 규칙
- 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성
- 첫 글자에 숫자 X
- 길이 제한 없음
- 대소문자 구별
- 다음의 키워드는 예약어로 사용할 수 없음:
```python
import keyword
print(keyword.kwlist)

# 출력 결과
['False', 'None,' 'True', '__peg_parser__', 'and', 'as', 'assert', 
'async', 'await', 'break', 'class', 'continue', 'def', 'del',
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```
- 내장 함수나 모듈 등의 이름 사용 X

```python
print(5)
print = 'hi'
print(5) # 에러 발생
```

---

| 연산자       | 내용            |
| ----------- | -----------     |
| **         | 거듭제곱          |
| /         | 나눗셈            |
| //        | 몫                |
| %         | 나머지            |

---

### 자료형 분류
- 수치형(Numeric Type)
    - int (정수)
    - float (실수)
    - complex (복소수)
- 문자열 (string type)
- 불린형 (bollean type)
- None

진수 표현
- 2진수: 0b
- 8진수: 0o
- 16진수: 0x

실수 연산시 주의할 점
- 실수의 값을 처리할 때 의도하지 않은 값이 나올 수 있음 (floating point rounding error)
- 원인: 부동 소수점
- 해결책: math 모듈 활용

삼중 따옴표 
- 따옴표 안에 따옴표를 넣을 때,
- 여러 줄을 나눠 입력할 때, 편리

Escape sequence
| 예약문자 | 내용(의미) |
| ----------- | ----------- |
| \n | 줄 바꿈 |
| \t | 탭 |
| \r | 캐리지 리턴 | 
| \\ | \ | 
| \' | ' |
| \" | " |

문자열 연산
- 덧셈 (string concatenation)
- `print("Hello"+"World") # HelloWorld
- 곱셈 
- print("Python" * 3) # PythonPythonPython

String Interpolation 
- 문자열을 변수로 활용하여 만드는 법
- % formatting
```python
name = 'Kim'
score = 4.5

print('Hello, %s' % name) # Hello, Kim
print('내 성적은 %d' % score) # 내 성적은 4 (%d -> int)
print('내 성적은 %f' % score) # 내  성적은 4.500000
```
- str.format()
```python
name = 'Kim'
score = 4.5

print('Hello, {}! 성적은 {}'.format(name, score)) # Hello, Kim!  성적은 4.5
```
- f-strings: python 3.6+
``` python
name = 'Kim'
score = 4.5

print(f'Hello, {name}! 성적은 {score}') # Hello, Kim!  성적은 4.5
```

---

### None
- 파이썬 자료형 중 하나
- 값이 없음을 표현하기 위해 None 타입 존재
- 일반적으로 반환 값이 없는 함수에서 사용하기도 함

---

### 불린형

- Falsy: False는 아니지만 False로 취급되는 값
    - 0, 0.0, (), [], {}, None, ""(빈 문자열)

---

### 컨테이너

컨테이너란?
- 여러 개의 값(데이터)을 담을 수 있는 것(객체)으로, 서로 다른 자료형을 저장할 수 있음
    - 예시: List
- 컨테이너의 분류
    - 순서가 있는 데이터 (ordered) *정렬되어 있다!*
    - 순서가 없는 데이터 (unordered)


### 리스트
``` python
boxes = ['A', 'B', ['apple', 'banana', 'cherry']]

print(len(boxes)) # 3
print(boxes[2][-1]) # cherry
print(f'boxes[-1][1][0]: {boxes[-1][1][0]}') # b
```

### 슬라이싱 연산자
``` python
print([1, 2, 3, 5][1:4]) # [2, 3, 5]
print((1,2,3)[:2]) # (1,2)
print(range(10)[5:8]) # range(5, 8)
print('abcd'[2:4]) # cd
print('abcdefghi'[2:5:2]) # 'ce
print('abcdefghi'[5:2:-1]) # fed
print(s[::-1]) # ihgfedcba
```

### 셋(set)

- 셋이란 중복되는 요소가 없이, 순서에 상관없는 데이터들의 묶음
    - 데이터의 중복을 허용하지 않기 때문에 중복되는 원소가 있다면 하나만 저장
    - 순서가 없기 때문에 인덱스를 이용한 접근 불가능
    - 순서가 중요한 경우, 사용 X
- 가변 자료형

### 셋 연산자
- | : 합집합
- & : 교집합
- \- : 차집합
- ^ : 대칭차집합
- (여집합 없음)

``` python
A_set = {1, 2, 3, 4}
B_set = {1, 2, 3, "hello", (1, 2, 3)}
print(A_set ^ B_set) # {'hello', 4, (1,2,3)}
```
