weight = float(input("몸무게: "))
height = float(input("키: "))
if height > 100 :
    height = height / 100
else :
    height = height

BMI = weight / (height**2)
print("-"*30)
print(f'당신의 BMI는 {round(BMI,2)}입니다.')
if BMI < 18.5 :
    print('당신은 저체중입니다.')
elif BMI < 23 :
    print('당신은 정상체중입니다.')
elif BMI < 25 :
    print('당신은 과체중입니다.')
else :
    print('당신은 비만입니다.')
