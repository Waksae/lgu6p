# for i in range(9):
#     for j in range(9):
#         print(f'{i+1} x {j+1} = {(i+1)*(j+1)}')
#     if i !=8:
#         print("-"*11)
#     else :
#         pass

for a in range(0, 9, 3):
    for b in range(9):
        print(f'{a+1} x {b+1} = {(a+1)*(b+1)} | {a+2} x {b+1} = {(a+2)*(b+1)} | {a+3} x {b+1} = {(a+3)*(b+1)}')
    if a != 7:
        print("-"*33)
    else :
        pass