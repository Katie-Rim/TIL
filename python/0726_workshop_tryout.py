# workshop problem01

def duplicated_letters(word):
  word_list = list(word)
  dup_list = []
  for i in word_list:
    if word_list.count(i) > 1:
      if i not in dup_list:
        dup_list.append(i)
      else:
        continue
  return dup_list
        
print(duplicated_letters('apple')) # ['p']
print(duplicated_letters('banana')) # ['a', 'n']



# workshop problem02

def low_and_up(word):
  word_list = list(word)
  new_list = []
  i = 0
  for i in range(len(word_list)):
    if i % 2 == 0:
      x = word_list[i]
      new_list.insert(i, x)
      i += 1
    else:
      new_list.insert(i, word_list[i].upper())
      i += 1
  new_word = ''.join(new_list)    
  return new_word

print(low_and_up('apple'))
print(low_and_up('banana'))



# workshop problem03

def lonely(lonely_list):
  result_list = []
  result_list.append(lonely_list[0])
  for i in range(1, len(lonely_list)):
    if lonely_list[i] == lonely_list[i-1]:
      i += 1
    else: 
      result_list.append(lonely_list[i])
      i += 1
  return result_list

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))
