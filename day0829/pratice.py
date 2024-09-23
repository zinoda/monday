# pratice.py
import random

def mysetlotto() :
    print('로또번호생성중')
    lotto = set()
    while len(lotto) < 6 :
        number = random.randint(1 ,45)
        lotto.add(number)
        
        lotto_list = list(lotto)
        lotto_list.sort()
     
    print('생성 로또 번호 :' , lotto_list)


mysetlotto( )
              