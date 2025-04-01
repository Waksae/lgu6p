from datetime import date


from days_utils import MONTH_DAYS, is_leap_year, get_month_days


def my_days(birth_year, birth_month, birth_day, cur_year, cur_month, cur_day):

    days_part_1 = 0


    days_part_1 += MONTH_DAYS[birth_month] - birth_day 
    
    if birth_month == 2 and is_leap_year(birth_year):
        days_part_1 += 1
    

    for m in range(birth_month+1, 13):
        days_part_1 += get_month_days(birth_year, m)
    

    days_part_2 = 0


    for y in range(birth_year+1, cur_year):

        for m in range(1,13):

            days_part_2 += get_month_days(y, m)


    days_part_3 = 0


    for m in range(1, cur_month):
        days_part_3 += get_month_days(cur_year, m)
        

    days_part_3 += cur_day
    

    return days_part_1 + days_part_2 + days_part_3

def true_days(birth_year, birth_month, birth_day, cur_year, cur_month, cur_day):
    d1 = date(birth_year, birth_month, birth_day)
    d2 = date(cur_year, cur_month, cur_day)
    delta = d2 - d1
    
    return delta.days 


if __name__ == '__main__':

    def filter_int_input(msg):

        while True:
            user_input = input(msg)

            if user_input.isdigit() == False:
                print("숫자만 입력하세요.")
            elif user_input < 0 or type(user_input) == float:
                print('자연수를 입력하세요.')
            else:
                user_input = int(user_input)
                break
        
        return user_input
    
    def month_filter(a, b):
        while True:
            if 0 < int(a) <= 12:
                break
            else:
                print('1부터 12 내의 숫자를 입력해주세요.')
        return True
    
    def day_filter(a, b):
        while True:
            if 0 < int(a) <= b:
                break
            else:
                print(f'1부터 {b} 내의 숫자를 입력해주세요.')
        return True



    birth_year = filter_int_input("태어난 연도를 입력: ")
    birth_month = filter_int_input("태어난 달을 입력: ")
    birth_day = filter_int_input("태어난 일을 입력: ")
        

    while True:
        cur_year = filter_int_input("현재 연도를 입력: ") 
        if cur_year <= birth_year:
            print("현재 연도는 태어난 연도 보다 커야 합니다.")
            continue

        cur_month = filter_int_input("현재 달을 입력: ")

        cur_day = filter_int_input("현재 일을 입력: ")
        
        break
    
    print('내가 계산한 날 수      : ', my_days(birth_year, birth_month, birth_day, cur_year, cur_month, cur_day) )
    print('datetime이 계산한 날 수: ',  true_days(birth_year, birth_month, birth_day, cur_year, cur_month, cur_day) )
