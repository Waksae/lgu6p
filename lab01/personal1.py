# x = int(input('x= '))
# i = 1
# while i <= 10 :
#     print(x**i)
#     i = i + 1
i = input('입력: ')
print(len(i))
a = len(i)
for k in range(a+1 ,1 , -1):
    print(i,"\b"*k,'')
print("-"*10)
print(i,"\b"*2,'')
# print(i,"\b"*(len(i)+1),'') # 7
# print(i,"\b"*(len(i)),'')   # 6
# print(i,"\b"*(len(i)-1),'') # 5
# print(i,"\b"*(len(i)-2),'') # 4
# print(i,"\b"*(len(i)-3),'') # 3
# print(i,"\b"*(len(i)-4),'') # 2
# print(i,"\b"*(len(i)-5),'') # 1
