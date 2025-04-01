def mean(a):
    x = 0
    y = 0
    for i in range(len(a)):
        x = x + a[i]
        y += 1
    return x/y
avg = mean([1,2,100])
print(avg)

# def mklist(a):
#     B = []
#     x = ' '
#     for i in a:
#         if type(i) == int:
#             x += 'i'
#             print(x)
#         else:
#             B.append(x)
#             print(f'{x} 추가')
#             x = ' '
#     return B
# L = mklist(str(input('숫자열 입력: ')))
# print(L)


