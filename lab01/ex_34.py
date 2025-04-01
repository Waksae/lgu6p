numbers = [10,4,5,-1,6,12,40]
# even_total = numbers[1::2]
# print(even_total)
# O = 0
# for N in even_total:
#     print(N)
#     O = O + N
# print(f'total = {O}')

for i in numbers:
    maximum = i
    for j in numbers[1::]:
        if maximum > j :
            print(maximum)
        elif maximum < j :
            maximum = j
            print(f'최대값 변경 : {maximum}')
        else :
            break
print(maximum)