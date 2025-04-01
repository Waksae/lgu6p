import ex_45

s = input('평균을 구할 숫자 입력(콤마 또는 공백으로 구분): ')
L = [int(i) for i in s.replace(',',' ').split()]

print(ex_45.mean(L))


