AUTH = False
user_id = 'Python Master'
user_pw = 'p1234'

# 사용 승인 체크 데코레이터
def auth_required(func):
    def wrapper(*args,**kwargs):
        if AUTH :
            func(*args,**kwargs)
        else :
            print('\n로그인이 필요한 메뉴입니다.\n다시 선택해주세요.\n')
    return wrapper

def log_in():
    global AUTH
    id = input('\nID:')
    if id == user_id:
        count = 0
        pw = input("\nPassword: ")
        for b in range(5):
            count = count + 1
            if pw == user_pw:
                print('\n로그인 성공\n')
                AUTH = True
                break
            else:
                if b <4:
                    pw = input(f'{count}회 오류 \n  재입력: ')
                else:
                    print('5회 오류. 로그인 실패')
    else :
        print('없는 ID입니다.')
        AUTH = False

# 이 함수에 완성된 데코레이터를 적용해주세요.
@auth_required
def order_list():
    print("*********************")
    print("구매 리스트 출력")
    print("만두, 아이스크림, 콜라")
    print("*********************")

# 이 함수에 완성된 데코레이터를 적용해주세요.
@auth_required
def return_list():
    print("*********************")
    print("반품 리스트 출력")
    print("커피, 책")
    print("*********************")

# 이 함수에는 데코레이터를 적용하지 마세요.
def recommend_list():
    print("*********************")
    print("추천 목록 출력")
    print("참치, 라면, 피자")
    print("*********************")

while True:
    print("============================")
    if AUTH:
        print("[0] : 로그아웃")
    else:
        print("[0] : 로그인")
    print("[1] : 구매 리스트")
    print("[2] : 교환 반품 리스트")
    print("[3] : 오늘의 추천 상품")
    c = input("메뉴 선택: ")

    if c == "0":
        if AUTH:
            print("\n로그아웃 되었습니다.\n")
            AUTH = False
        else:
            log_in()
    elif c == "1":
        order_list()
    elif c == "2":
        return_list()
    elif c == "3":
        recommend_list()
    else:
        break


