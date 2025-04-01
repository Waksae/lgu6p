import random

lottery=[]

while len(lottery) < 6:
    n = random.randrange(1,46)
    print(n)
    lottery.append(n)
    i = len(lottery)
    print(lottery)
    ir = i - 1
    if ir >= 1 :    
        for j in range(1,ir+1):
            if j > 0 :
                if lottery[ir] - lottery[ir-j] == 0:
                    del lottery[ir]
                else :
                    pass
            else :
                pass
    else : 
        pass
print(lottery)

# while len(lottery) < 6:
#     n = random.randrange(1,46)
#     if n not in lottery:
#         lottery.append(n)

# print(lottery)
