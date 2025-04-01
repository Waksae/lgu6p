# PW = '1234'
# user_pw = ''

# while PW != user_pw:
#     user_pw = input('PW: ')

#     if PW == user_pw:
#        print('로그인 성공')
#     else :
#        print('재입력')


# for a in range(5):
#     G = a * 0 + 1
#     PW = input('비밀번호 입력: ') * G
#     if PW == "1234":
#         print('성공')
#         break
#     else :
#         print('실패')
# print('본인인증을 진행해주세요.')

count = 0
a = input("PW: ")

for b in range(4):
    count = count + 1
    if a == "1234":
        print('성공')
        break
    else:
        a = input(f'{count}회 오류 \n  재입력: ')
else:
    print('5회 오류. ID 잠금')
