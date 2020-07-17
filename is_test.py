list_a = [10, 20, 30]
list_b = [10, 20, 30]

if list_a is list_b :
    print('list_a is list_b')
else :
    print('list_a is not list_b')
# 결과 : list_a is not list_b

# 증명
print('list_a =', id(list_a))
print('list_b =', id(list_b))

# 참고 1
if 3 is 3 :
    print('3 is 3')
else :
    print('3 is not 3')
print('3 =', id(3))
print('3 =', id(3))

# 참고 2
if list_a == list_b :
    print('list_a is list_b')
else :
    print('list_a is not list_b')

# 참고 3 : 문자열, 수, 튜플 is 가능 / set, dict, list 불가능 -> 직접 찍어보며 확인해보기