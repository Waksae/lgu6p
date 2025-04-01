def F_dp(n):
    a = 0
    b = 1
    c = 2
    while c == n+1:
        f = b + a
        print(f'{c} : {f}')
        c += 1
        a = b
        b = f

def F(n):
    a = 0
    b = 1
    c = 2
    while c == n+1:
        f = b + a
        yield (f'{c} : {f}')
        c += 1
        a = b
        b = f

def F_deco(n):
    return [ _ for _ in F(n)]

F_dp(12)