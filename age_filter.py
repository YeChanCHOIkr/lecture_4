def adult_func(n) :
    if n > 19 :
        return '성인입니다'
    else :
        return '미성년입니다'
print(adult_func(31))
print(adult_func(14))

print('')

# 필터 !
def adult_filter_func(n) :
    if n > 19 :
        return True
    else :
        return False
ages = [34, 25, 17, 13, 15, 54]
print('성년리스트1')
for a in filter(adult_filter_func, ages) :
    print(a)

print('')

# 필터 + 람다 !
ages = [63, 7, 10, 20, 30, 19]
print('성년리스트2')
for a in filter(lambda x: x>19, ages) :
    print(a)

print('')

# 필터 + 람다 + 인풋 !
ages = int(input('나이를 입력하세요'))
print('성년리스트2')
for a in filter(lambda x: x>19, ages) :
    print(a)