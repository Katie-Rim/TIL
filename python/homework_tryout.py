from re import A


list1 = [1, 3, 5, 4, 2]
result = list1.sort()
print(f'list.sort(): {result}')

list1 = [1, 3, 5, 4, 2]
result = sorted(list1)
print(f'sorted(list1): {result}')


# problem02

list2 = ['apple', 'banana', 'cherry']
list2.append('durian')
print(list2) # ['apple', 'banana', 'cherry', 'durian']
list2.extend(['durian'])
print(list2) # ['apple', 'banana', 'cherry', 'durian', 'durian']
list2.extend('durian')
print(list2) # ['apple', 'banana', 'cherry', 'durian', 'durian', 'd', 'u', 'r', 'i', 'a', 'n']


# problem03

a = [1, 2, 3, 4, 5]
b = a 
print(f'a: {a}') # a: [1, 2, 3, 4, 5]
print(f'b: {b}') # b: [1, 2, 3, 4, 5]

a[2] = 5

print(f'a: {a}') # a: [1, 2, 5, 4, 5]
print(f'b: {b}') # b: [1, 2, 5, 4, 5]

a1 = [1, 2, 3]
a1[2] = 5
b1 = a1

print(f'a1: {a1}') # a: [1, 2, 5, 4, 5]
print(f'b1: {b1}') # b: [1, 2, 5, 4, 5]