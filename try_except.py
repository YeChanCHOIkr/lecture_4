# 에러 여부를 확인해 줌

try :
    a, b = input('두 수를 입력하시오').split()
    result = (int(a)/int(b))
    print(result)

except :
    print('입력한 수가 정확한지 확인하시오')

print('test')

# try:
#     a,b = input('두수를 넣으세요').split()
#     result = (int(a)/int(b))
#     print(result)
# except:
#     print('대입한 수가 정확한지 확인하세요')

# print('test')