# homework lotto set. py

import random

lotto = set()  
while len(lotto) < 6 :
    number = random.randint(1,45)
    lotto.add(number)

lotto = list(lotto)
lotto.sort()


print('로또번호' , lotto , end='\t')