# 08jumin.py

import datetime
import time

jumin = '971230-1835064'
jum1 = '971230'  # len() 6자릿수 체크
jum2 = '971230-1835064' # len() 7자릿수 체크

#문제 1) 성별체크  1/3 남자 2/4 여자
#문제 2) 생일  12월 30일 생일 축하합니다
#문제 3) 나이계산 2024-1997 = ???
#문제 4) split() 사용해보기 [시 : 끝 +1]


# 성별체크

gender = jumin[7]

if gender in ['1' , '3'] :
    print('성별 : 남자')
elif gender in ['2','4'] :
    print('성별 : 여자')
else :
    print('성별 오류발생')

print()

# 생일
birth = (jumin[:6])
year = int(jumin[:2])
month =jumin[2:4]
day =jumin[4:6]

print(f'{year}년{month}월{day}일 생일 축하합니다')

print()

# 나이 계산

mytime = time.localtime()
current_year = int(mytime.tm_year)

if gender in ['1' , '2'] :
    birth_year = 1900 + year
else :
    birth_year = 2000 + year

age = current_year -birth_year 

print(f'현재 나이는 {age}살 입니다')

print()

print('-' * 50)

spjumin = '971230-1835064'

spjumin_part =spjumin.split('-')

sp_birth = spjumin_part[0]
sp_gender = spjumin_part[1]

gender = sp_gender[0]

if gender in ['1' , '3'] :
    print('성별 : 남자')
elif gender in ['2' , '4'] :
    print('성별 : 여자') 
else :
    print('에러 발생')

sp_year = int(sp_birth[:2]) 
sp_month = sp_birth[2:4]
sp_day = sp_birth[4:6]

print(f'{sp_year}년 {sp_month}월 {sp_day}일 생일 축하합니다')















# 틀림
# len1 = jum1.len()
# len2 = jum2.len()
# if jum1.__len__



















# x = datetime.now( ) 에러남
y = datetime.datetime.now() #정답 2024-08-28 11:18:49.161207



# print(y)
# print(str(y)) # 문자화 안전화 
# print(str(y)[0:4]) # 2024

# z = str(y)
# print(z[0:4])  #나이계산 가능

# dt = datetime.datetime.now()
# print( dt.strftime('%Y년-%M월-%d일'))
# print( dt.strftime('%H시-%M분-%S초'))
# print()

# mytime = time.localtime()
# print(mytime)
# print(mytime.tm_year) # 2024년도