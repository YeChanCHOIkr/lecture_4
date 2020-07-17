try :
    a, b = input('두 수를 입력하시오').split()
    result = (int(a)/int(b))
    print(result)

except ZeroDivisionError : # 0으로 나누기
    print('0으로 못 나눠')

except TypeError :
    print('지원되지 않는 연산자를 사용하였습니다')

except : 
    print('오류를 확인하세요')

print('test')