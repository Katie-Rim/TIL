20220725

# 데이터 구조

## 목차:

### 순서가 있는 데이터 구조
- 문자열(string)
- 리스트(list)
- 튜플(tuple)

### 순서가 없는 데이터 구조
- 셋(set)
- 딕셔너리(dictonary)

### 얕은 복사와 깊은 복사

--- 

# 1. 문자열 

### 문자열 조회/탐색 및 검증 메서드

| 문법          | 설명                                         | 예시 |
| -----------   | -----------                                 | ------|
| s.find(x)     | s에서 x의 첫번째 위치 반환. 없으면 -1 반환     | print('apple'.find('k')) # -1|
| s.index(x)    | s에서 x의 첫번째 위치 반환. 없으면 오류 발생   | print('apple'.index('k')) # ValueError: ... |
| s.isalpha()   | 유니코드 상 letter 여부                       ||
| s.isupper()   | 대문자 여부                                   ||
| s.islower()   | 소문자 여부                                   ||
| s.istitle()   | 타이틀 형식 여부                               | print('Title Title!'.istitle()) # True |

--- 

### 문자열 관련 검증 메서드
- .isdecimal() $\subseteq$ .isdigit() $\subseteq$ .isnumeric()

--- 

### 문자열 변경 메서드
- s.replace(old, new[,count])
- s.strip([chars])
- s.split(sep=None, maxsplit=-1)
- 'separator'.join([iterable])
- s.capitalize()
- s.title()
- s.upper()
- s.lower()
- s.swapcase()

s.capitalize()은 가장 첫 번째 글자만 대문자로 변경, s.upper()는 모두 대문자로 변경

---

### 문자열은 변경되는 것이 아니라 새롭게 정의되는 것:
예시 코드)
```python
word = 'python'
print(word)             # python
print(id(word))         # 2357210340592
print(word.upper())     # PYTHON
print(id(word.upper())) # 2357210281712
```

# 2. 리스트(list)

- 리스트는 여러 개의 값을 *순서가 있는 구조로 저장*하고 싶을 때 사용
- 가변 자료형

### 리스트 메서드
- L.append(x)
- L.insert(i, x)
- L.remove(x)
- L.pop()
- L.pop(i)
- L.extend(m)
- L.index(x, start, end)
- L.reverse()
- L.sort()
- L.count(x)


# 3. 튜플(Tuple)
- 튜플은 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
- 불가변 자료형 
- 리스트 메서드 중 항목을 *변경*하는 메서드들을 제외하고 대부분 동일

---
# 비시퀸스형 데이터 구조
---
# 4. 셋(Set)
- 중복되는 요소가 없이, 순서에 상관없는 데이터들의 묶음
(인덱스 이용한 접근 불가능)
- 집합 연산 가능
- 가변 자료형

### 셋 메서드
- s.copy()
- s.add(x)
- s.pop()
- s.remove(s)
- s.discard(x)
- s.update(*others)
- s.clear()
- s.isdisjoint(t)
- s.issubset(t)
- s.issuperset(t)


s.copy()는 셋의 *얕은 복사본*을 반환

remove는 삭제하고 하는 요소가 없으면 KeyError, discard는 셋에서 요소가 없어도 에러가 발생하지 않음

# 4. 딕셔너리(distionary)
- 딕셔너리의 key: key는 변경 불가능한 데이터만 활용 가능 (string, integer, float, boolean, tuple, range)
- 각 key의 값(values): 어떠한 형태든 관계 없음

### 딕셔너리 메서드
- d.clear()
- d.copy()
- d.keys()
- d.values()
- d.items()
- d.get(k)
- d.get(k, v)
- d.pop(k)
- d.pop(k, v)
- d.update([other])

# 5. 얕은 (shallow) 복사와 깊은 (deep) 복사

### 복사 방법
- 할당 (assignment)
- 얕은 복사 (shallow copy)
- 깊은 복사 (deep copy)

### 할당
- 대입 연산다 (=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사
- 해당 주소의 일부 값을 변경하는 경우, 이를 참조하는 모든 변수에 영향

### 얕은 복사(shallow copy)
- slice 연산자를 활용하여, 같은 원소를 가진 리스트지만 연산된 결과를 복사 (다른 주소)

### 깊은 복사(shallow copy)

```python
import copy
a = [1,2, ['a', 'b']]
b = copy.deepcopy(a)
print(a, b)
b[2][0] = 0
print(a,b)
```