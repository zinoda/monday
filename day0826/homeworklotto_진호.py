# 04 lotto.py

import random

# 로또 1~45사이 숫자
# 로또 정수
# 반복문 for, while , if
# 난수발생 6개 숫자 중복 체크
# 난수발생 후 출력은 sort 정렬
# set 이용하지 마세요

# lotto = []
# for k in range(6) :
#     com = random.randint(1,45)
#     print(com, end = '\t')

lotto = []
while len(lotto) < 6 :
    number = random.randint(1, 45)
    if number not in lotto :
        lotto.append(number)

lotto.sort()

print('로또번호', lotto, end='\t')


