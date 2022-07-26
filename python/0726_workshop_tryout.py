def duplicated_letters(word):
    word_list = list(word)
    dup_list = []
    for i in word_list:
        if word_list.count(i) > 1:
            dup_list.append(i)
            word_list.remove(i)
    return dup_list
        

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))

def low_and_up(word):
    word_list = list(word)
    new_list = range(len(word_list))
    for i in range(len(word_list)):
        if i % 2 == 0:
            new_list[i].insert(i, word_list[i])
            i += 1
        else:
            new_list[i].insert(i, word_list[i].upper())
            i += 1
    return new_list


print(low_and_up('apple'))
print(low_and_up('banana'))

# workshop problem03

def lonely(lonely_list1):
    result_list = []
    result_list[0] = lonely_list1[0]
    for i in range(1, len(lonely_list1)):
        if lonely_list1[i] == lonely_list1[i-1]:
            result_list.append(i)
            lonely_list1.remove(i)
            i += 1
        else: 
            result_list.append(i)
            lonely_list1.remove(i)
            i += 1
    return result_list

print(lonely([1, 1, 3, 3, 0, 1, 1]))
        
list1 = [1, 3, 5, 4, 2]
print(f'sorted: {sorted(list1)}')

list2 = [1, 3, 5, 4, 2]
list2.sort()
print(f'sort(): {list2}')
