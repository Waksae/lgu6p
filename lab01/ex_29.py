n = 5
for i in range (n):
    print(' '*(n-i-1),end='')
    for j in range(i*2+1):
        print("*",end='')
    print()
K = n*2-1
for a in range(n):
    count = 0
    for b in range(a*2+1):
        count = count + 1
        if count == (a*2+1):
            print(f"{'*'*count:^{K}}")