import os

for score_txt in os.listdir('./data'):
    with open(f"./data/{score_txt}", 'r', encoding='utf-8') as f :
        if f"./data/{score_txt}"[-3:] == 'txt':
            lines = f.readlines()
            name = score_txt[:-4:]
            sc_list = []

            for line in lines:
                sc = line[0:2]
                sc_list.append (int(sc))
                
            # print(f'{name:>6}: {round(ex_45.mean(sc_list),2):.2f}, {round(ex_45.std(sc_list),2):.2f}')
        else:
            pass