data=[
{'name':'철수', 'math':85, 'eng':90, 'sci':75},
{'name':'준호', 'math':73, 'eng':85, 'sci':93},
{'name':'영희', 'math':92, 'eng':88, 'sci':90}
]
nta = {}
for d in data :
    X = 0
    A = 0
    for value in d.values():
        if type(value) == str :
            nta[value] = [0,0]
            A = value
        else :
            X += value
        nta[A][0] = X
        nta[A][1] = round(X/3,3)
print(nta)