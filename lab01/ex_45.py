import math

def mean(a):
    x = 0
    y = 0
    for i in a:
        x = x + i
        y += 1
    return x/y

def std(l):
    # x = 0
    # S = 0
    # for i in l:
    #     x = i - mean(l)
    #     S += x**2
    m = mean(l)
    var = mean([(x-m)**2 for x in l])
    return math.sqrt(var)

if __name__ == '__main__':  
    print('TEST CODES')
    L = [1,2,3,4,5,6,7,8,9,10]
    print(std(L))