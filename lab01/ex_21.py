n = int(input("자연수 입력: "))
count = 0
for j in range(1,n+1):
    # print(f"{count} + {j} = {count + j}")
    count += j
print(count)

x = 1
count2 = 0
while x <= n:
    count2 = count2 + x
    x = x + 1
print(count2)