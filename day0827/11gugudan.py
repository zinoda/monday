#11gugudan.py 문서 함수

# 파이썬 함수 def 함수이름( ) :
# 파이썬 함수 매개인자
# 파이썬 함수 리턴값
# 함수는 호출 call


# 내장함수
# list() , len () , tuple() , set() 
# str() , int() , round() , print() , input()

def book() :
    #서점 , 예약 , 내용위주
    pass
def main() :
    #메인함수 진입시작
    pass



import time
def gugudan(dan) :
    for k in range(1,10,1) :
        print(f'{dan} * {k} = {k*dan}')
        time.sleep(0.3)

def mysum(a,b) :
    print(a,b, '합계=',(a+b))

mysum(1,2)

gugudan(5) #함수 이름(21매개인자)
print('구구단연습 4:35')
print()