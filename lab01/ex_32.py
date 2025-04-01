# jisoo = [90, 85, 93]
# mansoo = [78, 92, 89]
# total=[]

# for i in range(len(jisoo)):
#         T = jisoo[i] + mansoo[i]
#         total.append(T)
# print(total)

score = [ [90, 85, 93],
          [78, 92, 89] ]
subject = ['국어', '수학', '영어']
student = ['지수', '만수']

print('과목 별 총점')
for i in range(len(score[1])):
    S = 0
    for j in range(len(score)):
        S+=score[j][i]
    print(f'{subject[i]} 총점 : {S}')
print('')
#
print('학생 별 총점')
for J in range(len(score)):
    K = 0
    for I in range(len(score[1])):
        K+=score[J][I]
    print(f'{student[J]} 총점 : {K}')
