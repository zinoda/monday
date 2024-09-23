# 14def.py

# 파이썬에서 함수 정의 시작 키워드 def 함수 이름 ( ) :
# 사용자정의 함수 매개인자
# 사용자정의 함수 리턴값
# 사용자정의 함수 매개인자 + 리턴값

# 함수 정의 = 구현 = 기술 함수=fuction=기능

import time

def gugudan(name , dan) :
    print('구구단 작성자')
    for k in range(1,10) :
        print(f'{dan} * {k} = {dan*k}')
        time.sleep(0.5)

# 함수호출
# gugudan('choi' , 7)

# if __name__ == '__main__' : # 생략가능
#         gugudan('lee'  ,7)
#         print()

kor = 90
eng = 85
mat = 60
myTotal =(kor,eng,mat)

# myTotal 함수 기술  총점 , 평균 출력

def myTotal(kor,eng,mat) :
    print('myTotal 함수영역')
    hap = kor+eng+mat
    avg = hap//3
    print('myTotal 총점 =', hap)
    print('myTotal 평균 =', avg)

myTotal(60,70,80)
