# HWsetlotto.py

# 추천 lotto = set() , set 항목 추가 함수는 add()  ex) lotto.add()
# 금지 lotto = list[] , 리스트 추가 append() 임
# 추천 while ~ while ~ if  ~ else  쓰거나 ,  while~for 쓰거나 , while ~ if 쓰거나.. 
# 난수 로또숫자 발생 , 중복체크 , set 추가
# set데이터타입을 list 변환 후에 sort 적용 -> 출력은 오름차순

import random

def mysetlotto() :
    print('로또 번호 생성')
    lotto = set()
    while len(lotto) < 6 :
        number = random.randint(1,45)
        lotto.add(number)
        
    lotto_list = list(lotto)
    lotto_list.sort()

    print('생성 된 로또 번호 :' , lotto_list)

mysetlotto()