import pandas as pd

df = pd.read_excel("./data/scores.xlsx")
# df.to_dict()     열방향
# df.T.to_dict()   # 행방향
print(df.to_dict())
print(df.T.to_dict())
# df = df.T.to_dict()
# data = [v for k, v in df.items()]
# print(data)

# nta = {}
# for d in data :
#     X = 0
#     A = 0
#     for value in d.values():
#         if type(value) == str :
#             nta[value] = [0,0]
#             A = value
#         else :
#             X += value
#         nta[A][0] = X
#         nta[A][1] = round(X/3,3)
# print(nta)