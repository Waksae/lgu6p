a = 0
b = 0
while a != 3:
    a = input(f'[메뉴를 입력하세요] \n 1.게임시작  2.랭킹보기  3.게임종료\n ->')
    if a == '1' and b == 'alert':
        print('->이미 실행 중입니다.')
    elif a == '1' and b != 'alert':
        print('->게임을 시작합니다.')
        b = 'alert'
    elif a == '2':
        print('->실시간 랭킹')
    elif a == '3' :
        print('->게임을 종료합니다.')
        break
    else :
        print('->다시 입력해주세요.')
        