menus = {
    '피자': ['페퍼로니피자', '스테이크피자', '시푸드피자'],
    '토핑': ['햄', '페퍼로니', '트러플', '올리브', '새우'],
    '사이드': ['치즈오븐스파게티', '리조또', '치킨윙'],
    '음료': ['콜라', '스프라이트', '오렌지쥬스']
        }
prices = {
        '피자': [29000, 32000, 32000],
        '토핑': [500, 500, 800, 300, 800],
        '사이드': [9900, 8900, 8900],
        '음료': [1000, 1000, 1000]
         }
order={}
categories=[]

for menu in menus.keys():
    order[menu] = []
    categories.append (menu)

def main():
    print('빅데이터 피자 가게에 오신 것을 환영합니다.')
    print('')
    a = 0
    i = 0
    while True:
        current_category = categories[i]
        S = len(menus[current_category])
        print(f'{current_category}를 선택하세요. 수량 추가를 위해 여러 번 선택 가능합니다.')
        for id, it in enumerate(menus[current_category]):
            print(f'{id+1}. {it} ({prices[current_category]}원)')

        a = input('번호를 입력하고 Enter를 누르세요. (다음단계:n, 이전단계:p, 주문완료:f): ')
        print('')

        if a.isdigit() :                                        # 숫자 입력 시
            if int(a) > 0 and int(a) <= S:                      # 올바른 메뉴 선택 시
                N = int(a)-1
                print(f'선택된 메뉴: {menus[current_category][N]}\n')
                order[current_category].append (menus[current_category][N])
            else :                                              # 메뉴 번호 이외의 숫자 입력 시
                print('잘못된 선택입니다.')
                print('')
        elif a.isdigit() == False :                             # 문자 입력 시
            if a != 'f' and a != 'p' and a != 'n':              # f, n, p 외 입력 시
                print('정확히 입력해주세요.')
                print('')
            elif a == 'n':                                      # 다음단계
                if i == (len(menus) - 1):                       # 마지막 카테고리 도달 상태에서 다음 선택 시
                    pass
                else:
                    i += 1
            elif a == 'p':                                      # 이전단계
                if i == 0:                                      # 첫 카테고리 도달 상태에서 이전 선택 시
                    pass
                else:
                    i -= 1
            elif a == "f":                                      # 주문종료
                print('')
                print(f'주문 내역: \n {order}')
                break
main()