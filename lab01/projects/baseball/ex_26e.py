import baseball

digit3 = baseball.Digit3()

while True:
    print("[메뉴를 입력하세요]")
    c = input("1.게임시작   2.랭킹보기   3.게임종료 >>>") 

    if c == '3':
        print("->게임을 종료합니다.")
        break
    elif c == '1':
        print("->게임을 시작합니다.")
        # os.system('python baseball.py')
        digit3.start_game()
    elif c == '2':
        print("->실시간 랭킹")

        digit3.rank()
    else:
        print("다시 입력해주세요.")


