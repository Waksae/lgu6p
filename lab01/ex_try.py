operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y 
}
# a = float(input('첫 번째 숫자를 입력하세요: '))
# b = float(input('두 번째 숫자를 입력하세요: '))
# p = input('연산자를 입력하세요 (+, -, *, /): ')
# if p in operations:
#     print(f'{a} {p} {b} = {operations[p](a,b)}')
# else :
#     print("올바른 연산자가 아닙니다.")
try:
    a = float(input('첫 번째 숫자를 입력하세요: '))
    b = float(input('두 번째 숫자를 입력하세요: '))
    p = input('연산자를 입력하세요 (+, -, *, /): ')
    print(f'{operations[p](a,b)}')
except ZeroDivisionError as e:
    print('오류: 0으로 나눌 수 없습니다.')
except KeyError as e:
    print('올바른 연산자가 아닙니다.')
except ValueError as e:
    print('숫자를 입력해주세요.')
except Exception as e:
    print('알 수 없는 오류가 발생했습니다.')
finally:
    print('프로그램을 종료합니다.')