# 15def return.py


def book ( ) :
    title = '몽블랑' #지역변수 = local variable = 휘발성
    return title
def pay ( ) :
    m = 7800 # 지역변수 = local variable=휘발성
    return m

# 일반함수 리턴값 x 매개인자 x 일반함수를 출력하면 none
def blue () :
    color = 'dark'


def main ( ) :
    print("main함수")
    print('책제목' , book())
    print('책가격' , pay())
    print('블 루' , blue()) # none 출력



if __name__ == '__main__' :
    main( )