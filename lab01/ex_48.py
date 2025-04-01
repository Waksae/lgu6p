# with open("file_w.txt","w",encoding="utf-8") as f:
#     f.write("Hello Python\n")
#     f.write("안녕 파이썬")
# encoding을 제대로 하지 않으면 한글은 다 깨질 수 있다. utf-8, euc-kr (비권장)

# with open("file_w.txt","r",encoding="utf-8") as f: 
#     lines = f.readlines()
#     print(lines,type(lines))
#     for line in lines:
#         print(line, end="")
import os
import ex_45
for score_txt in os.listdir('./data'):
    with open(f"./data/{score_txt}", 'r', encoding='utf-8') as f :
        if f"./data/{score_txt}"[-3:] == 'txt':
            lines = f.readlines()
            name = score_txt[:-4:]
            sc_list = []

            for line in lines:
                sc = line[0:2]
                sc_list.append (int(sc))
                
            print(f'{name:>6}: {round(ex_45.mean(sc_list),2):.2f}, {round(ex_45.std(sc_list),2):.2f}')
        else:
            pass