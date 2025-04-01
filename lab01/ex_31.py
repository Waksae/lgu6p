teams = ['타이거즈', '라이온즈', '트윈스', '베어스', '위즈',
         '랜더스', '자이언츠', '이글스', '다이노스즈', '히어로즈']

for a in teams :
    print(f'{teams.index(a)+1}위: {a}')

teams.sort()
print(teams)
print()
teams.sort(reverse=True)
print(teams)