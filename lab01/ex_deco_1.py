import time
print(time.time())


def timing_decorator(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f'실행시간: {end_time - start_time:.10f}')
        return result
    return wrapper

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

@timing_decorator
def F_deco(n):
    return [ _ for _ in F(n)]

@timing_decorator
def F_dp(n):
    a = 0
    b = 1
    c = 2
    while c == n+1:
        f = b + a
        print((f'{c} : {f}'))
        c += 1
        a = b
        b = f
# F_dp = timing_decorator(F_dp)

F_dp(4000)
F_deco(4000)