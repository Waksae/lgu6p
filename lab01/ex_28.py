# for i in range(6):
#     print("*"*(i+1),end='')
#     for j in range(6):
#         pass
#     print()
n=5
# for i in range(n):
#     for j in range(i+1):
#         print('*', end='')
#     print()

for i in range(n,0,-1):
    for j in range(i):
        print('*', end='')
    print()