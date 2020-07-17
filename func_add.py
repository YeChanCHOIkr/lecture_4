def add(x, y) :
    return x + y
print(add(10, 50))

# 람다 함수!
add_another = lambda x, y : x + y
print(add_another(11,40))

def add_plus(x, y, z) :
    result_1 = x + y
    result_2 = lambda y : y**3
    return result_1 + result_2(y)
print(add_plus(1, 2, 3))