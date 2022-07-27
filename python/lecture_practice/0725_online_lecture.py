word = 'python'
print(word)             # python
print(id(word))         # 2357210340592
print(word.upper())     # PYTHON
print(id(word.upper())) # 2357210281712

# .replace 메소드
print('katie'.replace('k', 'c'))
print('woooow'.replace('o','w',3))  # count 지정하여 해당 개수만큼만 시행

# .strip 메소드
print("너???".rstrip('?'))

# .split 메소드
print('a b c'.split())

# 'separator'.join([iterable]) 메소드 
# 구분자(separator)로 합쳐 문자열 반환
print('!'.join('ssafy'))
print(' '.join(['3', '5']))


# insert
cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe)
cafe.insert(0, 'start')
print(cafe)

# extend
cafe.extend('coffee')
print(cafe)

# pop
numbers = [1, 2, 0, 3, 4]
numbers.pop(2)
print(numbers)

# List.clear()
deleteall = [1,2,3]
print(deleteall)
deleteall.clear()
print(deleteall)

# List.index(x)
list1 = [1, 2, 3, 4, 5]
print(list1.index(3))

# List.count(X)
list2 = [1, 1, 1, 1, 1, 0]
print(list2.count(1))

# List.sort()
list3 = [5, 4, 2, 1, 3]
list3.sort()    # 원본이 변경됨
result_list3 = sorted(list3)
print(list3)
print(result_list3)


# 5. 얕은 복사와 깊은 복사
# 할당
original_list = [1, 2, 3]
copy_list = original_list
print(original_list, copy_list)

copy_list[0] = 'hello'
print(original_list, copy_list)
