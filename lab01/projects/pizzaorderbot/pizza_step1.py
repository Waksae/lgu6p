menus = ['페퍼로니피자', '스테이크피자', '시푸드피자']
price = [29000, 32000, 32000]
order = []

def main():
    print('빅데이터 피자 가게에 오신 것을 환영합니다.')
    print('')
    a = 0
    while True:
        print('피자를 선택하세요. 수량 추가를 위해 여러 번 선택 가능합니다.')
        for id, it in enumerate(menus):
            print(f'{id+1}. {it} ({price[id]}원)')

        a = input('번호를 입력하고 Enter를 누르세요.(주문완료는 f를 누르세요.): ')

        if a.isdigit():
            if int(a) > 0 and int(a) <= 3:
                N = int(a)-1
                print(f'선택된 메뉴: {menus[N]}\n')
                order.append (menus[N])
            if int(a) <= 0 or int(a) >3 or type(a) == float:
                print('')
                print('1, 2, 3 중에 선택해주세요.')
                print('')
        elif a == "f":
            print('')
            print(f'주문내역: \n {order}')
            break
        else:
            print('')
            print('정확히 입력해주세요.')
            print('')
main()