def leap_year(n):
    if n % 4 == 0 and n % 100 != 0:
        a = '%d년은 윤년입니다.' % n
        return a
    elif n % 400 == 0:
        a = '%d년은 윤년입니다.' % n
        return a
    else:
        a = '%d년은 윤년이 아닙니다.' % n
        return a

# 입력 에시
print(leap_year(2021))
print(leap_year(2020))