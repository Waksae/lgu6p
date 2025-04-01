def dev(a, b):
    n = 0
    while a >= 0 :
        a = a - b
        n = n + 1
    a = a + b
    return (n-1, a)



R = dev(int(input('나눠질 수를 입력하세요: ')),int(input('나눌 수를 입력하세요: ')))
print(R)