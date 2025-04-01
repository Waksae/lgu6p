def IG():
    x = 0
    while True:
        x += 1
        yield x

number = IG()

for i in range(50):
    print(next(number))
