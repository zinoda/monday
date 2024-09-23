# HWyear.py


# if 제어문 or / and 중첩 if
# 윤년기준 1) 4의 배수 2) 100의 배수가 아닌 4의 배수 3) 400의 배수
# 문제 ) 2024  2 입력하면 윤년입니다 나오게



days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


year = int(input("년 year >>>> "))
month = int(input("월 month >>>> "))


leap_year = False
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            leap_year = True
    else:
        leap_year = True


if leap_year:
    print(f"{year}년은 윤년입니다.")
    
    days_in_month[2] = 29
else:
    print(f"{year}년은 윤년이 아닙니다.")
 
    days_in_month[2] = 28


if 1 <= month <= 12:
    print(f"{month}월은 {days_in_month[month]}일입니다.")
else:
    print("잘못된 월입니다. 1부터 12 사이의 값을 입력하세요.")

