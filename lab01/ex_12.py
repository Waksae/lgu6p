name = input('너의 이름: ')

kor = float ( int ( input ( '국어 점수: ' ) ) )
eng = float ( int ( input ( '영어 점수: ' ) ) )
mat = float ( int ( input ( '수학 점수: ' ) ) )
sci = float ( int ( input ( '과학 점수: ' ) ) )

total = kor + eng + mat + sci
avg = (kor + eng + mat + sci) / 4

print(f'{name}의 총점은 {total}이고 평균은 {avg}입니다.')
