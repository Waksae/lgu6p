menus = {
    '피자': ['페퍼로니피자', '스테이크피자', '시푸드피자'],
    '토핑': ['햄', '페퍼로니', '트러플', '올리브', '새우']
        }
prices = {
        '피자': [29000, 32000, 32000],
        '토핑': [500, 500, 800, 300, 800]
         }
order={'피자': [], '토핑': []}
categories=['피자', '토핑']

def main():
    print('빅데이터 피자 가게에 오신 것을 환영합니다.')
    print('')
    a = 0
    i = 0
    while True:
        current_category = categories[i]
        print(f'{current_category}를 선택하세요. 수량 추가를 위해 여러 번 선택 가능합니다.')
        for id, it in enumerate(menus[current_category]):
            print(f'{id+1}. {it} ({prices[current_category]}원)')

        a = input('번호를 입력하고 Enter를 누르세요. (다음단계:n, 이전단계:p, 주문완료:f): ')
        print('')
        
        if a == 'n':
            i = 1
        elif a == 'p':
            i = 0
        elif a.isdigit():
            N = int(a)-1
            print(f'선택된 메뉴: {menus[current_category][N]}\n')
            order[current_category].append (menus[current_category][N])
        elif a.isdigit() == False and a != 'f' and a != 'p' and a != 'n':
            print('')
            print('정확히 입력해주세요.')
            print('')
        elif a == "f":
            print('')
            print(f'주문 내역: \n {order}')
            break
main()