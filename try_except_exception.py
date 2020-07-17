try :
    a, b = input('두 수를 입력하시오').split()
    result = (int(a)/int(b))
    print(result)

except Exception as err :
    print('에러 형태는 {}'.format(err))

# print(result)
# print('test')