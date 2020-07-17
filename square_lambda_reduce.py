from functools import reduce

n_list = [10, 20, 30, 40, 50]

result_1 = reduce(lambda x, y: x + y, n_list)
print(result_1)

result_2 = reduce(lambda x, y: x * y, n_list)
print(result_2)