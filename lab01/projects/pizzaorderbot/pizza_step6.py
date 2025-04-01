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
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    a = 0
    i = 0
    total_price = 0
    while True:
        if str(a).isdigit() :                                        # 숫자 입력 시
            if int(a) > 0 and int(a) <= S:                      # 올바른 메뉴 선택 시
                clear_screen()
                print('')          
                print('')      
            else :                                              # 메뉴 번호 이외의 숫자 입력 시
                pass
        elif str(a).isdigit() == False :                             # 문자 입력 시
            if a != 'f' and a != 'p' and a != 'n':              # f, n, p 외 입력 시
                pass
            else :
                clear_screen()  
                print('')
                print('')              
        current_category = categories[i]
        S = len(menus[current_category])
        print('빅데이터 피자 가게에 오신 것을 환영합니다.')
        print('')
        print(f'{current_category}를 선택하세요. 수량 추가를 위해 여러 번 선택 가능합니다.')
        print('')
        print(f'현재 장바구니: {order}')
        for id, it in enumerate(menus[current_category]):
            print(f'{id+1}. {it} ({prices[current_category][id]}원)')

        a = input('번호를 입력하고 Enter를 누르세요. (다음단계:n, 이전단계:p, 주문완료:f): ')
        print('')

        if a.isdigit() :                                        # 숫자 입력 시
            if int(a) > 0 and int(a) <= S:                      # 올바른 메뉴 선택 시
                N = int(a)-1
                print(f'선택된 메뉴: {menus[current_category][N]}\n')
                order[current_category].append (menus[current_category][N])
                total_price += prices[current_category][N]
            else :  
                clear_screen()                                            # 메뉴 번호 이외의 숫자 입력 시
                print('[!] 잘못된 선택입니다.')
                print('')
        elif a.isdigit() == False :                             # 문자 입력 시
            if a != 'f' and a != 'p' and a != 'n':              # f, n, p 외 입력 시
                clear_screen()                                  # 화면 지우고 경고문구 출력
                print('[!] 정확히 입력해주세요.')
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
                print('-'*9)
                print('주문 내역')
                print('-'*9)
                for I in categories:                            # 카테고리 종류 순차 출력
                    print(f'{I}: ',end="")                      
                    for K in range(len(order[I])):              # order 카테고리 별 주문 메뉴 개수
                        if K == (len(order[I])-1):              # 마지막 메뉴 출력 시 ',' 미출력, 줄바꿈.
                            print(f'{order[I][K]}',end='')
                        else :                                  # 출력 메뉴 남았을 시 ','출력, 줄 안바꿈.
                            print(f'{order[I][K]}, ',end='')
                    print('')
                price_word='총 금액: '
                print(f'{price_word}{total_price:,}원')
                print('주문이 완료되었습니다. 감사합니다.')
                break
main()