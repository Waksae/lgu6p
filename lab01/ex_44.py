operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "오류: 0으로 나눌 수 없습니다"
}
a = float(input('첫 번째 숫자를 입력하세요: '))
b = float(input('두 번째 숫자를 입력하세요: '))
p = input('연산자를 입력하세요 (+, -, *, /): ')
if p in operations:
    print(f'{a} {p} {b} = {operations[p](a,b)}')
else :
    print("올바른 연산자가 아닙니다.")