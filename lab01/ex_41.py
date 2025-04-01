def mean(a):
    x = 0
    y = 0
    for i in range(len(a)):
        x = x + a[i]
        y += 1
    return x/y
X = [[78,80,95,55,67,43],[45,67,90,87,88,93]]

AVG = [ round(mean(c),2) for c in X]

AVG = []
for c in X:
    m = mean(c)
    AVG.append (round(m,2))

print(AVG)