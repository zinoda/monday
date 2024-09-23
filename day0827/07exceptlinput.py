# 07exceptinput. py
# 문제 1 )dan 입력 키보드 input( ) , 형변환
# 문제 2 )dan 입력 범위 정수 1이상 2~9 사이 숫자만 입력
# 문제 3 ) 예외처리 try :  ~ except : ~
# 1건이상처리는 무조건 반복문
import time

# dan = 3
# for k in range(1,10,1) :
#     print(f'{dan} * {k} = {dan*k}')
#     time.sleep(0.5)

# print()
# time.sleep(0.5)
# print('포인트 7점획득')
# print('포인트 5점이상이면 vip 자격만족 대상입니다.')

# print()
# print('-' * 50)

dan = 0 #초기값s

while True :
    try :
        dan = int(input(" 원하는 단 입력 >>>>"))
        if dan < 2 or dan >9 :
            print('숫자 범위는 2~9사이 숫자입니다\n다시 입력하세요')
            continue

        for k in range (1, 10) :
            print(f'{dan}*{k} = {dan*k}')
            time.sleep(0.5)
        break
    
    except :
        print('유효하지 않는 입력입니다\n다시 입력하세요')
